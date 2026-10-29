# Delivery and acceptance

## Intake and sizing

Read the source issue, related incidents, repository conventions and existing work before editing. Establish the user-visible defect or desired outcome, testable acceptance, explicit exclusions and the owner who can accept it. Separate facts from inferred requirements. Ask only for missing choices that materially change the result; continue independent work.

Apply the team's estimation and decomposition rules. Split work when it has independently useful outcomes or uncertainty prevents a reliable acceptance check. Use a bounded discovery task for a material unknown. Do not impose a story format or story-point threshold on a team that uses another method.

Record a checkpoint after meaningful transitions so another executor can resume from actual artifacts. Include revision, completed criteria, remaining work and any outstanding remote effect.

## Implementation and evaluation

Choose checks by failure mode, not by check count:

| Change | Evidence that matters |
| --- | --- |
| Bug fix | Reproduce the bug or establish a concrete cause; demonstrate the corrected behavior and relevant regression boundary |
| User flow | Loading, normal, error, empty and permission states that the change affects; responsive/keyboard access when relevant |
| API/job | Contract, authentication, duplicate/retry behavior, partial failure and actual completion signal |
| Data/schema | Migration compatibility, data integrity, rollback/forward recovery and realistic sample behavior |
| LLM workflow | Representative task fixtures, scoring rubric, baseline comparison, cost/latency and a failure/abuse case relevant to the change |

Use required existing checks. Add tests when they catch a meaningful regression, not simply to restate implementation. Do not broaden a passing test run without a new concern. Disclose skipped or unavailable checks and their practical impact.

Independent reviewers should receive the acceptance and final diff/revision, not a proposed verdict. Select scopes proportional to the change: correctness, security/authorization, data, reliability, UX or economics. Reconcile findings and rerun affected validation. Inconclusive review stays visible; a human release grant and technical review answer different questions.

## Release and live QA

Prepare the concrete change and evidence before seeking any missing release grant. Record target, candidate revision, required-check result, rollback and expected verification. Honor an existing scoped grant without re-asking.

Before a retry, query merge/deploy state. If the release partially completed, establish the actual deployed state and recovery owner. Do not force-push, overwrite unrelated work or disable checks to clear the path without applicable authorization.

Live QA verifies the acceptance against the actual target using sanitized fixtures. Record the deployed revision, test method, timestamp, evidence and cleanup. Check that the release is active before attributing behavior to it. A local pass plus a green deploy job is still missing live behavior evidence.

On regression, stop further dependent rollout. Roll back only through an authorized, compatible path; do not assume a code rollback reverses a migration or an external write. Preserve diagnostics and open/link the follow-up or incident.

## Feedback quality

Useful delivery metrics have explicit definitions:

- **Lead time:** elapsed time from the project's selected ready/accepted timestamp to verified delivery; publish that boundary and exclude or disclose blocked time consistently.
- **Change failure rate:** releases requiring rollback, hotfix or incident response divided by eligible releases in the stated window; disclose small samples.
- **Acceptance:** verified criteria divided by applicable criteria, with evidence per criterion. Do not treat this ratio as a substitute for a mandatory criterion.
- **Product result:** a user outcome such as successful signup rate, with event/cohort definition, numerator, denominator, baseline and observation window.

Do not optimize ticket closure or test count at the expense of the outcome. Record measurement limitations and distinguish delivery evidence from causal product impact. Turn repeated failures into separately owned factory improvements; preserve the original failure instead of rewriting its score.
