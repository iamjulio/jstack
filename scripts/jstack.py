#!/usr/bin/env python3
"""Local skill catalog, validation, installation, and deterministic packaging."""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {'.git', '.venv', '__pycache__', 'dist', '.local', 'profiles', 'memory'}
SENSITIVE = [
    ('private key', r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    ('AWS access key', r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b'),
    ('GitHub token', r'\bgh[pousr]_[A-Za-z0-9]{30,}\b|github_pat_[A-Za-z0-9_]{40,}'),
    ('machine-specific home', r'/(?:Users|home)/[A-Za-z0-9_.-]+/'),
    ('possible account identifier', r'\b[0-9]{12,}\b'),
]


class Invalid(ValueError):
    pass


def catalog(root=ROOT):
    data = json.loads((root / 'jstack.json').read_text())
    seen = set()
    for item in data['skills']:
        name = item['name']
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or name in seen:
            raise Invalid('Invalid or duplicate skill name')
        if item['path'] != f'skills/{name}':
            raise Invalid(f'Unexpected path for {name}')
        seen.add(name)
    if (root / 'VERSION').read_text().strip() != data['version']:
        raise Invalid('VERSION and catalog version differ')
    return data


def files_under(path):
    for parent, dirs, names in os.walk(path, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in IGNORED)
        for d in dirs:
            if (Path(parent) / d).is_symlink():
                raise Invalid(f'Symlink directory is not distributable: {d}')
        for name in sorted(names):
            file = Path(parent) / name
            if file.is_symlink():
                raise Invalid(f'Symlink file is not distributable: {file.name}')
            if not name.endswith(('.pyc', '.pyo')):
                yield file


def skill_files(skill):
    # Skills must be entirely portable, including any otherwise ignored folders.
    for file in sorted(skill.rglob('*')):
        if file.is_symlink():
            raise Invalid(f'Symlinks are not allowed inside skills: {file.name}')
        if file.is_file() and '__pycache__' not in file.parts and not file.name.endswith(('.pyc', '.pyo')):
            yield file


def selected(args, data):
    known = {s['name']: s for s in data['skills']}
    names = list(known) if args.all else list(dict.fromkeys(args.skills))
    if not names:
        raise Invalid('Select at least one skill, or use --all')
    if args.all and args.skills:
        raise Invalid('Use skill names or --all, not both')
    if any(name not in known for name in names):
        raise Invalid('Unknown skill name; run list for valid names')
    return [known[name] for name in names]


def frontmatter(file):
    text = file.read_text()
    match = re.match(r'\A---\nname: ([a-z0-9-]+)\ndescription: ("[^\n]*")\n---(?:\n|$)', text)
    if not match:
        raise Invalid(f'{file.parent.name}: use name and a single JSON-quoted description')
    description = json.loads(match[2])
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        raise Invalid(f'{file.parent.name}: invalid description')
    if match[1] != file.parent.name:
        raise Invalid(f'{file.parent.name}: frontmatter name differs from folder')
    return text


def check(root=ROOT, deny_file=None):
    data = catalog(root)
    errors = []
    if (root / '.git').exists():
        tracked = subprocess.run(['git', '-C', str(root), 'ls-files', '-z'],
                                 check=True, capture_output=True).stdout.decode().split('\0')
        for name in filter(None, tracked):
            path = Path(name)
            if (any(part in IGNORED - {'.git'} for part in path.parts)
                    or (path.name.startswith('.env') and path.name != '.env.example')
                    or path.suffix == '.skill'):
                errors.append(f'{name}: private/generated path is tracked; .gitignore does not unpublish it')
    declared = {s['name'] for s in data['skills']}
    actual = {p.name for p in (root / 'skills').iterdir() if p.is_dir()}
    if declared != actual:
        errors.append('Skill directories and catalog do not match')
    for item in data['skills']:
        folder = root / item['path']
        try:
            frontmatter(folder / 'SKILL.md')
            if (folder / 'LICENSE').read_bytes() != (root / 'LICENSE').read_bytes():
                errors.append(f"{item['name']}: standalone license differs or is absent")
            ui = (folder / 'agents/openai.yaml').read_text()
            for field in ('display_name', 'short_description', 'default_prompt'):
                if not re.search(rf'^  {field}: "[^\n]+"$', ui, re.M):
                    errors.append(f"{item['name']}: missing quoted UI {field}")
            if f"${item['name']}" not in ui:
                errors.append(f"{item['name']}: UI prompt must name the skill")
            list(skill_files(folder))
        except (OSError, ValueError) as exc:
            errors.append(str(exc))
    extra = []
    if deny_file:
        extra = [re.compile(line.strip(), re.I) for line in Path(deny_file).read_text().splitlines()
                 if line.strip() and not line.startswith('#')]
    for file in files_under(root):
        relative = file.relative_to(root)
        try:
            content = file.read_text()
        except UnicodeDecodeError:
            errors.append(f'{relative}: unexpected binary file; review redistribution rights')
            continue
        for label, pattern in SENSITIVE:
            if re.search(pattern, content):
                errors.append(f'{relative}: {label} pattern needs review')
        if any(pattern.search(content) for pattern in extra):
            errors.append(f'{relative}: private deny-list match')
        for address in re.findall(r'[A-Za-z0-9_.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', content):
            if not address.endswith(('@example.com', '@example.org', '@users.noreply.github.com')):
                errors.append(f'{relative}: non-example email needs review')
        if file.suffix == '.md':
            # Fenced shell snippets are not Markdown navigation links.
            prose = re.sub(r'```[^\n]*\n.*?```', '', content, flags=re.S)
            for target in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', prose):
                target = target.strip('<>')
                if urlsplit(target).scheme or target.startswith('#'):
                    continue
                path = unquote(target.split('#')[0])
                resolved = (file.parent / path).resolve()
                if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                    errors.append(f'{relative}: broken or escaping local link: {target}')
                if len(relative.parts) > 2 and relative.parts[0] == 'skills':
                    skill_root = (root / 'skills' / relative.parts[1]).resolve()
                    if not resolved.is_relative_to(skill_root):
                        errors.append(f'{relative}: runtime link leaves its standalone skill')
    cases = json.loads((root / 'evals/cases.json').read_text())['cases']
    ids = [case['id'] for case in cases]
    if len(ids) != len(set(ids)):
        errors.append('Duplicate evaluation case IDs')
    if {c['skill'] for c in cases} != declared:
        errors.append('Every skill must have behavioral cases')
    for case in cases:
        if not case.get('request') or not case.get('checks') or not case.get('evidence'):
            errors.append(f"Incomplete evaluation case: {case.get('id')}")
    if errors:
        raise Invalid('\n'.join(errors))
    return data


def install(items, destination, root=ROOT):
    destination = Path(destination).expanduser()
    destination.mkdir(parents=True, exist_ok=True)
    for item in items:
        target = destination / item['name']
        if os.path.lexists(target):
            raise Invalid(f'Refusing to overwrite {target}')
        list(skill_files(root / item['path']))
    reserved = []
    try:
        # Exclusive mkdir reserves each target. Never write through an existing folder/link.
        for item in items:
            target = destination / item['name']
            target.mkdir()
            reserved.append(target)
        for item, target in zip(items, reserved):
            source = root / item['path']
            for file in skill_files(source):
                output = target / file.relative_to(source)
                output.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file, output)
    except BaseException:
        for target in reversed(reserved):
            shutil.rmtree(target)
        raise
    return reserved


def bundle(items, output, root=ROOT):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    archives = []
    for item in items:
        target = output / f"{item['name']}.skill"
        if os.path.lexists(target):
            raise Invalid(f'Refusing to overwrite {target}')
    with tempfile.TemporaryDirectory(prefix='jstack-bundle-', dir=output) as staging:
        for item in items:
            source = root / item['path']
            target = Path(staging) / f"{item['name']}.skill"
            with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
                for file in skill_files(source):
                    member = f"{item['name']}/{file.relative_to(source).as_posix()}"
                    info = zipfile.ZipInfo(member, date_time=(1980, 1, 1, 0, 0, 0))
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.external_attr = 0o100644 << 16
                    archive.writestr(info, file.read_bytes())
            archives.append(target)
        results = []
        try:
            for staged in archives:
                target = output / staged.name
                # Record ownership only after exclusive creation succeeds. A raced file
                # must never be removed by rollback; a partial write we own must be.
                with target.open('xb') as stream:
                    results.append(target)
                    stream.write(staged.read_bytes())
        except BaseException:
            for target in reversed(results):
                target.unlink()
            raise
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('list', help='Show available skills')
    validate = sub.add_parser('check', help='Validate structure and common disclosure patterns')
    validate.add_argument('--deny-file', help='Private newline-separated regex patterns; never committed')
    for command in ('install', 'bundle'):
        p = sub.add_parser(command)
        p.add_argument('skills', nargs='*')
        p.add_argument('--all', action='store_true')
        if command == 'install':
            group = p.add_mutually_exclusive_group(required=True)
            group.add_argument('--host', choices=['codex', 'claude'])
            group.add_argument('--dest', type=Path)
        else:
            p.add_argument('--output', type=Path, default=ROOT / 'dist')
    sub.add_parser('eval-list', help='List behavioral cases without running a model')
    export = sub.add_parser('eval-prompt', help='Export a candidate packet without reviewer checks')
    export.add_argument('case_id')
    args = parser.parse_args()
    try:
        data = catalog()
        if args.command == 'list':
            for item in data['skills']:
                print(f"{item['name']:20} {item['summary']}")
        elif args.command == 'check':
            check(deny_file=args.deny_file)
            print(f"PASS: {len(data['skills'])} skills; structure, references, metadata, disclosure patterns, eval catalog")
        elif args.command in ('install', 'bundle'):
            check()
            items = selected(args, data)
            if args.command == 'install':
                destination = args.dest or Path.home() / ('.codex' if args.host == 'codex' else '.claude') / 'skills'
                for path in install(items, destination):
                    print(f'Installed {path}')
            else:
                for path in bundle(items, args.output):
                    digest = hashlib.sha256(path.read_bytes()).hexdigest()
                    print(f'{digest}  {path.name}')
        else:
            cases = json.loads((ROOT / 'evals/cases.json').read_text())['cases']
            if args.command == 'eval-list':
                for case in cases:
                    print(f"{case['id']:30} {case['skill']}")
            else:
                case = next((c for c in cases if c['id'] == args.case_id), None)
                if not case:
                    raise Invalid('Unknown evaluation case')
                print(json.dumps({k: case[k] for k in ('id', 'skill', 'request', 'evidence')}, indent=2))
    except (Invalid, OSError, ValueError, KeyError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
