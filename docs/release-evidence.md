# Release evidence

## 0.3.0 — Public and private routing

Prepared October 28, 2026. Added the eighth skill, `jstack`, with metadata-first discovery, verified scoped selection, shared-limit handoffs, and bounded chain recovery. The public package contains only public routing metadata and fictitious private configuration examples.

- Public package, reference, privacy-pattern, and official router-format validation pass.
- Twelve installer/catalog/package fixture tests pass, including source-drift detection and excluding the router from leaf routes.
- An independent agent applied the router to seven synthetic tasks covering single-skill work, multi-skill dependencies, matching private scope, missing catalogs, explicit public selection, circular dependencies/shared budgets, and changed source pins. Routing and authority checks pass; unavailable live outcomes remain inconclusive.
- The [actual candidate outputs and assessment](../evals/results/2026-10-28/router/report.json) retain the tested instruction hashes and limitations. No live provider or business operation was exercised.

The public catalog now contains 30 regression cases across eight skills. The seven new forward applications are not a repeated model benchmark or a run of that complete catalog. Exact model/runtime settings were not separately recorded. Private catalogs, configured paths, credentials, and real business context are excluded from the public artifacts.

## 0.2.0 — One Person Company

Prepared October 28, 2026. Added the seventh independently installable skill, preserving the reusable operating methodology and three references while excluding private company profiles and grants.

- Official new-skill validation, seven-skill catalog/reference/privacy checks, and a temporary installation pass.
- All 10 installer and packaging tests pass; tooling code and the six existing skills are unchanged.
- Independent public-release review passes: no private company profile, identity, account, path, or inherited grant is included.
- Two independent synthetic applications pass: uncertain-action resumption with parallel support work; and explicit stop/transfer with unmet outcome criteria and evidence-backed positioning. See the [candidate artifacts and content hash](../evals/results/2026-10-28/one-person-company/summary.json).
- Seven skill archives built successfully; the six existing archives match v0.1.0 byte for byte.

The catalog now contains 22 behavioral regression cases, including four for the new skill. The two new forward-test scenarios are qualitative exercises, not a completed 22-case benchmark. No live business system, outgoing message, campaign, schedule, or operating-state store was changed by the tests. Exact model/runtime settings were not separately recorded. GitHub CI remains a separate check on the published commit.

## 0.1.0

Prepared October 28, 2026. This is the initial skill library release, with local tooling and synthetic workflow verification.

### Executed checks

| Check | Result | Scope |
| --- | --- | --- |
| Official skill-creator `quick_validate.py` | Six skills pass | Frontmatter, naming, unfinished scaffolding |
| Local installer and bundle tests | 10 pass | Portable copies, collisions, rollback, symlinks, traversal, deterministic ZIP contents, candidate/rubric separation |
| Video preparation helper tests | 2 pass with FFmpeg | Exact audio deduplication, same-stem names, corrupt input, explicit ASR failure |
| Independent scenario applications | Six skills pass their scoped synthetic scenarios | Requests and supplied evidence, no external effects |
| Independent tooling review | Pass after one repaired defect | Failed archive publication now removes its own partial files and preserves concurrent files |

The scenario [summary and actual candidate artifacts](../evals/results/2026-10-28/summary.json) include skill content hashes and limitations. The applying agent differed from the author for each skill. Scenarios covered missing private memory configuration, sprint capacity uncertainty, unreadable targeting, unsupported ad claims, stale software reviews, uncertain deployment outcomes, invalid marketing tracking, and protected-site bypass.

These six scenario applications do not represent completion of the entire [18-case catalog](../evals/cases.json). They were qualitative forward tests, with no repeated runs or baseline comparison. Exact model/runtime versions and decoding settings were not separately recorded. No superiority claim follows from these results.

### Publication review

Structural validation checks catalog consistency, standalone licenses, local references, metadata, common disclosure patterns, and accidentally tracked private/generated folders. A separate private deny-list derived from supplied source material is used for the initial publication review and is kept outside the repository. All examples and scenario evidence in this repository are synthetic.

The CI checkout action's full commit pin was verified against the provider repository. Web hosting guidance links primary provider documentation and records its review date. Release archives contain each standalone skill and its license; generated archives are distributed as release assets rather than committed into source.

### Not verified by this release

No live ticket queue, CRM, advertising account, cloud resource, browser login, end-to-end speech recognition, or cross-session memory backend was connected or exercised. No actual marketing campaign or production site was deployed. The included factory skills are operating procedures and templates, not hosted automation services.

Live deployment, account capabilities, current pricing, and outcome measurement must be verified in the environment where a skill is used. GitHub-hosted CI status is available in the repository's Actions tab and is separate from these local results.
