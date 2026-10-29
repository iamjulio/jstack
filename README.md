# jstack

**Give your AI agent a better way to work.**

A router and seven focused skills for running a business with AI agents, remembering what matters, shipping software, running marketing experiments, publishing websites, planning sprints, and buying ads. Use one directly, or let `jstack` choose and chain the capabilities needed for your outcome.

Built by [Julio](https://github.com/iamjulio). Free to use, adapt, and share under the [MIT license](LICENSE).

## Pick a skill

| You want to… | Start here | Try asking… |
| --- | --- | --- |
| Choose and connect the right workflows | [jstack](skills/jstack/SKILL.md) | “Use jstack to prepare this launch, using the right public and configured private skills.” |
| Own a business outcome with AI agents | [one-person-company](skills/one-person-company/SKILL.md) | “Help me run this business outcome with clear measures, bounded initiatives, and durable operating records.” |
| Stop repeating preferences and decisions | [remember](skills/remember/SKILL.md) | “Remember that I want drafts before anything is published.” |
| Turn a ticket into a verified release | [software-factory](skills/software-factory/SKILL.md) | “Take this ticket through implementation, review, CI, and live verification.” |
| Learn which marketing ideas work | [marketing-factory](skills/marketing-factory/SKILL.md) | “Design a bounded experiment for this offer and define how we'll judge it.” |
| Publish a site with protected admin pages | [web-publisher](skills/web-publisher/SKILL.md) | “Plan an S3 and CloudFront site, with admin access that can't be bypassed.” |
| Make the next sprint achievable | [scrum-master](skills/scrum-master/SKILL.md) | “Turn this backlog into clear stories and a realistic sprint.” |
| Build and improve paid campaigns | [ad-buying](skills/ad-buying/SKILL.md) | “Review these results, then prepare the next test as paused ads.” |

## Get started in two minutes

Clone the repo and choose one skill. Python 3.10+ is needed for the included tools; the skill instructions themselves are Markdown.

```sh
git clone https://github.com/iamjulio/jstack.git
cd jstack
python3 scripts/jstack.py list
python3 scripts/jstack.py install --all --host codex
```

Use `--host claude` for Claude Code, or choose a project destination:

```sh
python3 scripts/jstack.py install scrum-master --dest /path/to/project/.agents/skills
python3 scripts/jstack.py install jstack --host claude
```

The installer copies skills and refuses to replace any existing installation. Generic names such as `remember` may already be installed: compare versions and choose a separate destination before changing anything. Restart or reload your agent if it does not discover the skill immediately. Other agents can use the `SKILL.md` folders with their own supported installation method.

The router can also use a verified suite checkout and explicitly configured private catalogs; its archive does not bundle the other skills. [Configure public and private routing](docs/router.md), then try:

```text
Use $jstack to prepare a landing-page experiment and paused ads.
Use the existing project queue. Keep publication and activation as drafts.
```

Prefer an uploadable file? Download an individual `.skill` archive from [Releases](https://github.com/iamjulio/jstack/releases), when a release is available, or build one locally:

```sh
python3 scripts/jstack.py bundle --all
```

## What makes this useful

- **A clear finish line.** Work starts with acceptance criteria and ends with evidence tied to the delivered artifact.
- **A complete loop.** Capture the request → do the work → evaluate → verify real results → improve the next run.
- **Personalization stays yours.** Account IDs, customers, budgets, credentials, and brand details belong in private local profiles.
- **Your tools, your authority.** Discover the available integrations; honor existing grants; prepare concrete work before asking for a missing decision.
- **Failures are part of the workflow.** Reconcile uncertain writes, preserve rollback options, and stop when a retry or experiment limit is reached.

The skills are reusable procedures. They do not install a ticket system, CI service, advertising connector, memory backend, or cloud account. [Start here](docs/quickstart.md) for setup and [connect the skills](docs/working-together.md) for a complete workflow.

## Quality you can inspect

```sh
python3 scripts/jstack.py check
python3 -m unittest discover -s tests -v
python3 scripts/jstack.py eval-list
```

CI checks the skill catalog, local references, metadata, common private-data patterns, installer behavior, and archive contents. The [behavioral cases](evals/cases.json) test decisions that file validation cannot establish. They need independent agent runs and review; a passing linter is not proof of campaign performance, secure deployment, or better model behavior. See [evaluation guidance](evals/README.md) and [release evidence](docs/release-evidence.md).

## Make it better

Found a repeatable failure or a useful improvement? [Open an issue](https://github.com/iamjulio/jstack/issues). Include a sanitized example and what a successful outcome would look like. See [contributing](CONTRIBUTING.md).

Inspired by the independently installable skill format in [cstack](https://github.com/goodnight000/cstack). jstack has its own workflows and tooling; it is not affiliated with other projects using the jstack name.
