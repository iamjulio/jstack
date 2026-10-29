# Engineer the delivery system

Use this mode when the requested change affects how work is selected, executed, graded or released. A product defect discovered during delivery does not automatically authorize replacing the factory.

1. **Trace the actual failure.** Identify the broken boundary: intake, claim, adapter, artifact, evaluation, review, release, live verification or feedback. Capture a representative failed run and current baseline.
2. **Define the contract change.** Version the work-unit/evidence contract and map it to the real queue/provider. Name owner, migration/compatibility, permission boundary, retry semantics, limits and rollback. Preserve product acceptance separately.
3. **Implement the smallest runtime needed.** Where runtime work is requested, implement and test real persistence, supported concurrency/claiming, adapters, receipts, recovery and observability. Procedures or local fixtures alone do not prove a deployed system.
4. **Evaluate independently.** Use fixed fixtures and held-out cases. Separate the executor from the scorer/reviewer where available. Freeze acceptance before the comparison; never change a rubric to rescue the candidate's result.
5. **Roll out under the grant.** Start with replay/dry-run or a limited project where appropriate. Verify the deployed factory revision, real intake-to-receipt behavior and recovery. Persist defects and follow-up ownership.

A useful fixture set includes ordinary success, duplicate intake, a timed-out write that actually succeeded, stale approval after a revision, expired claim, unavailable integration, partial deployment, live-QA failure and exhausted limits. Compare candidate to baseline on completion correctness, false success, duplicate effects, recovery, latency and total cost. Report individual failures and sample size alongside aggregates.

Never use a self-awarded score as sole proof. For substantive changes, have an independent executor apply the final instructions to a realistic task in an isolated workspace, with minimal raw evidence and no supplied answer. Restrict effects to approved fixtures. Review the resulting artifact and decision, repair material failures, and repeat affected cases against the final revision.

## Handoffs

When another factory owns a dependency, persist parent/child IDs, shared root/dedupe key, both owners and organization scopes, acceptance, source revision, allowed data, resource reservation, status and final receipt. Query existing requests before resubmitting. A dependency request grants no external action at the receiving side. Each side verifies its own grants; a parent budget is shared, not copied per child.

Track prepared, acknowledged, in progress, submitted and accepted using native fields, with failed/blocked/unknown outcomes where needed. Stop cyclic equivalent dependencies and stale-result acceptance. Use links rather than unnecessary customer data. Messaging another chat or person still requires the user's authorization.
