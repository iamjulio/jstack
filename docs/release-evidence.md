# Release evidence — 0.1.0

Prepared October 28, 2026. This is the initial skill library release, with local tooling and synthetic workflow verification.

## Executed checks

| Check | Result | Scope |
| --- | --- | --- |
| Official skill-creator `quick_validate.py` | Six skills pass | Frontmatter, naming, unfinished scaffolding |
| Local installer and bundle tests | 10 pass | Portable copies, collisions, rollback, symlinks, traversal, deterministic ZIP contents, candidate/rubric separation |
| Video preparation helper tests | 2 pass with FFmpeg | Exact audio deduplication, same-stem names, corrupt input, explicit ASR failure |
| Independent scenario applications | Six skills pass their scoped synthetic scenarios | Requests and supplied evidence, no external effects |
| Independent tooling review | Pass after one repaired defect | Failed archive publication now removes its own partial files and preserves concurrent files |

The scenario [summary and actual candidate artifacts](../evals/results/2026-10-28/summary.json) include skill content hashes and limitations. The applying agent differed from the author for each skill. Scenarios covered missing private memory configuration, sprint capacity uncertainty, unreadable targeting, unsupported ad claims, stale software reviews, uncertain deployment outcomes, invalid marketing tracking, and protected-site bypass.

These six scenario applications do not represent completion of the entire [18-case catalog](../evals/cases.json). They were qualitative forward tests, with no repeated runs or baseline comparison. Exact model/runtime versions and decoding settings were not separately recorded. No superiority claim follows from these results.

## Publication review

Structural validation checks catalog consistency, standalone licenses, local references, metadata, common disclosure patterns, and accidentally tracked private/generated folders. A separate private deny-list derived from supplied source material is used for the initial publication review and is kept outside the repository. All examples and scenario evidence in this repository are synthetic.

The CI checkout action's full commit pin was verified against the provider repository. Web hosting guidance links primary provider documentation and records its review date. Release archives contain each standalone skill and its license; generated archives are distributed as release assets rather than committed into source.

## Not verified by this release

No live ticket queue, CRM, advertising account, cloud resource, browser login, end-to-end speech recognition, or cross-session memory backend was connected or exercised. No actual marketing campaign or production site was deployed. The included factory skills are operating procedures and templates, not hosted automation services.

Live deployment, account capabilities, current pricing, and outcome measurement must be verified in the environment where a skill is used. GitHub-hosted CI status is available in the repository's Actions tab and is separate from these local results.
