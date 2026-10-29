# Project binding and adapters

Bind to the project already selected by the user. Read existing repository instructions and discover available connector/CLI schemas; do not invent provider field names or replace the canonical tracker because another tool is easier.

Record the following in existing configuration or a project-local profile:

| Binding | Required decision |
| --- | --- |
| Identity | Organization/tenant, accountable owner, execution account and permitted data scope |
| Queue | Provider, project/board, supported status mapping, work-item lookup and deduplication key |
| Repository | Remote, base branch, branch/worktree convention, PR and review policy |
| Evaluation | Required checks, risk-specific review, acceptance fixtures and evidence retention |
| Release | Environment, release mechanism, authorized actors, confirmation evidence and rollback |
| Live QA | Target URL/API/job, safe test identity/data, acceptance scenario and cleanup |
| Limits | Time/cost/attempt caps, lease/reconciliation behavior, stop and escalation owner |
| Feedback | Outcome metric, baseline, observation window, data source and follow-up owner |

Reference credentials by secret-manager or environment-variable name only. Do not copy secret values into profiles, work items, commits or receipts. Public repository templates contain no actual customer/account bindings.

## Minimum adapter checks

Before a first write, confirm the selected identity and project, inspect required fields/enums and supported operations, then perform the authorized narrow write and read it back. Preserve the returned remote ID, URL and revision. A tool name resembling the needed operation does not prove schema compatibility.

- **Queue:** map proposed states such as ready, in progress, review, releasing, verified and blocked to native states. If a transition is unavailable, use an existing field/comment and disclose the mapping. Never imply the provider enforces a custom state machine.
- **Repository:** read the actual base/head, respect local changes, and avoid overwrites. Look up existing branch/PR before creating another after an interrupted run.
- **CI:** bind a check to commit SHA and verify its completion/conclusion; a queued run or success on a sibling branch is insufficient.
- **Release:** verify the target's deployed revision or immutable release ID through the actual platform. If the platform cannot expose a commit, record the available linkage and its limit.
- **QA:** use a permitted test identity. Email, billing, destructive jobs and customer-facing notifications need a test mode or separately scoped grant. Never repeat an effectful action solely to obtain a cleaner screenshot.

When an integration is unavailable, complete implementation, tests and review artifacts locally where possible. Save a clearly labeled queue/release draft and name the missing capability. Do not fabricate a ticket URL, PR, CI result, release or live-QA pass.
