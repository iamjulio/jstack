"""Observable installer, packaging, and evaluation isolation guarantees."""
import importlib.util
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('jstack', ROOT / 'scripts/jstack.py')
js = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(js)


class ToolingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.source = self.base / 'source'
        self.source.mkdir()
        self.items = []
        for name in ('alpha', 'beta'):
            folder = self.source / 'skills' / name
            folder.mkdir(parents=True)
            (folder / 'SKILL.md').write_text(f'{name} instructions\n')
            (folder / 'reference.md').write_text('Useful reference\n')
            self.items.append({'name': name, 'path': f'skills/{name}'})

    def tearDown(self):
        self.temp.cleanup()

    def test_install_is_portable_copy(self):
        dest = self.base / 'installed'
        js.install(self.items, dest, self.source)
        (self.source / 'skills/alpha/SKILL.md').write_text('changed source')
        self.assertEqual((dest / 'alpha/SKILL.md').read_text(), 'alpha instructions\n')
        self.assertEqual((dest / 'beta/reference.md').read_text(), 'Useful reference\n')

    def test_collision_aborts_entire_batch_and_preserves_existing(self):
        dest = self.base / 'installed'
        (dest / 'beta').mkdir(parents=True)
        (dest / 'beta/SKILL.md').write_text('user customized version')
        with self.assertRaises(js.Invalid):
            js.install(self.items, dest, self.source)
        self.assertFalse((dest / 'alpha').exists())
        self.assertEqual((dest / 'beta/SKILL.md').read_text(), 'user customized version')

    def test_broken_symlink_is_a_collision(self):
        dest = self.base / 'installed'
        dest.mkdir()
        (dest / 'alpha').symlink_to(self.base / 'missing')
        with self.assertRaises(js.Invalid):
            js.install(self.items, dest, self.source)
        self.assertTrue((dest / 'alpha').is_symlink())

    def test_failure_rolls_back_only_new_installations(self):
        dest = self.base / 'installed'
        (dest / 'unrelated').mkdir(parents=True)
        (dest / 'unrelated/keep').write_text('preserve')
        with patch.object(js.shutil, 'copy2', side_effect=OSError('disk full')):
            with self.assertRaises(OSError):
                js.install(self.items, dest, self.source)
        self.assertFalse((dest / 'alpha').exists())
        self.assertFalse((dest / 'beta').exists())
        self.assertEqual((dest / 'unrelated/keep').read_text(), 'preserve')

    def test_source_symlink_cannot_copy_external_content(self):
        external = self.base / 'private'
        external.write_text('not distributable')
        (self.source / 'skills/alpha/link').symlink_to(external)
        with self.assertRaises(js.Invalid):
            js.install(self.items, self.base / 'installed', self.source)

    def test_archives_are_reproducible_self_contained_and_non_overwriting(self):
        first = js.bundle(self.items, self.base / 'first', self.source)
        second = js.bundle(self.items, self.base / 'second', self.source)
        self.assertEqual([p.read_bytes() for p in first], [p.read_bytes() for p in second])
        with zipfile.ZipFile(first[0]) as archive:
            self.assertEqual(set(archive.namelist()), {'alpha/SKILL.md', 'alpha/reference.md'})
            self.assertTrue(all('..' not in Path(p).parts for p in archive.namelist()))
        old = first[0].read_bytes()
        with self.assertRaises(js.Invalid):
            js.bundle(self.items, self.base / 'first', self.source)
        self.assertEqual(first[0].read_bytes(), old)

    def test_catalog_cannot_select_path_traversal(self):
        (self.source / 'jstack.json').write_text(json.dumps({
            'version': '0.1.0', 'skills': [{'name': '../private', 'path': '../private'}]}))
        with self.assertRaises(js.Invalid):
            js.catalog(self.source)

    def test_bundle_publication_failure_cleans_only_its_own_files(self):
        output = self.base / 'bundles'
        real_open = Path.open

        def raced_open(path, mode='r', *args, **kwargs):
            if path == output / 'beta.skill' and mode == 'xb':
                path.write_bytes(b'created by concurrent process')
                raise FileExistsError('concurrent writer')
            return real_open(path, mode, *args, **kwargs)

        with patch.object(Path, 'open', raced_open):
            with self.assertRaises(FileExistsError):
                js.bundle(self.items, output, self.source)
        self.assertFalse((output / 'alpha.skill').exists())
        self.assertEqual((output / 'beta.skill').read_bytes(), b'created by concurrent process')

    def test_bundle_failed_write_removes_incomplete_archive(self):
        output = self.base / 'bundles'
        real_open = Path.open

        class BrokenWrite:
            def __enter__(self):
                self.stream = real_open(output / 'alpha.skill', 'xb')
                return self

            def write(self, value):
                self.stream.write(value[:8])
                raise OSError('disk full')

            def __exit__(self, *args):
                self.stream.close()

        def failing_open(path, mode='r', *args, **kwargs):
            if path == output / 'alpha.skill' and mode == 'xb':
                return BrokenWrite()
            return real_open(path, mode, *args, **kwargs)

        with patch.object(Path, 'open', failing_open):
            with self.assertRaises(OSError):
                js.bundle(self.items, output, self.source)
        self.assertFalse(list(output.glob('*.skill')))

    def test_candidate_packet_excludes_reviewer_rubric(self):
        import subprocess
        result = subprocess.run([__import__('sys').executable, str(ROOT / 'scripts/jstack.py'),
                                 'eval-prompt', 'memory-no-store'], capture_output=True, text=True, check=True)
        packet = json.loads(result.stdout)
        self.assertEqual(set(packet), {'id', 'skill', 'request', 'evidence'})
        self.assertNotIn('checks', packet)


if __name__ == '__main__':
    unittest.main()
