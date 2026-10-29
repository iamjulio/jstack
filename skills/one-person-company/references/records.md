# Persistent operating memory

Choose the smallest durable store available for the operation: workspace files, an existing project system, or an authorized connected service. Reuse existing records. Agree on location and access when absent; a local draft may live in the current permitted workspace with its provisional location stated. Do not invent connected apps or write sensitive credentials into records. Reference secrets through approved storage.

Use stable operation/initiative/ticket/action IDs. Separate concurrent initiative updates to avoid overwriting each other's history; append decision/action events and maintain a compact current-state snapshot. Store links or receipts as evidence, with timestamps and source limitations. The fields below are schemas, not a requirement to create a file for every noun.

## Charter and current snapshot

- Operation ID, scope, accountable owner, stakeholders, customer/problem and value/positioning.
- Primary outcome, baseline, target, counting semantics, horizon or unknown, completion/continuing responsibilities.
- Health and constraint measures; resources/capacity/budget known, unknown, committed and available.
- Lifecycle state and parallel loops; evidence for state, current initiatives, priorities and unresolved assumptions.
- Authority per capability: status, exact grant/evidence, issuer, limits, expiry, escalation/revocation conditions.
- Dependencies/handoffs, record locations, latest reconciliation, next action and required input.

## Metric contract

For each metric record definition, entity/unit, numerator/denominator or formula, inclusions/exclusions, period/cohort, source, owner, baseline and timestamp, current value and timestamp, freshness expectation, target/guardrail and uncertainty. Missing observations are unknown, never zero. Label derived estimates and do not mix cohorts/windows to imply causal uplift.

Use a headline outcome plus explanatory metrics. Acquisition, activation, retention, revenue and cost reveal why it moves; qualify attribution and sample limits. When sources disagree, reconcile identity/time/count semantics before asserting progress. Distinguish gross acquisitions from net active customers after churn. Freshness expectations depend on the decision and business rhythm; stale data cannot justify aggressive scaling.

## Initiative and experiment record

ID/owner; outcome linkage; customer evidence; hypothesis and mechanism; baseline; deliverable/channel/audience; success/failure thresholds and evaluation event/window; resource cap and actual cost/time; authority link; dependencies; state/transition evidence; instrumentation; action receipts; result and attribution limitations; stop/iterate/scale decision and rationale; follow-up tickets.

## Decision, approval and action ledger

- Decision: question/options, evidence/unknowns, tradeoff, deciding owner/time, decision, review trigger and related initiative.
- Approval request: exact reviewable action/content/audience, cost/resource exposure, limits, risks/recovery, requested grant, requester/approver, pending/approved/denied/expired status, actual human approval evidence. Changes outside the approved envelope need a new authority check.
- External action: stable ID or idempotency key where supported, intended effect, authorization, attempt time, destination/provider, request/receipt reference, pending/confirmed/failed/uncertain status, reconciliation evidence, retry boundary. Preparation and a submitted request do not prove the effect happened.

Check the action ledger and external state before resuming sends, purchases, deployments or other consequential effects. Use provider idempotency when supported; otherwise inspect actual receipts/state. Never claim exactly-once execution merely because a local ID exists.

## Ticket and handoff

Ticket: source/support evidence with privacy protection; customer impact and affected scope; reproducibility/uncertainty; outcome linkage; priority rationale; owner; acceptance criteria; dependency; implementation/verification evidence; release/customer follow-up and measure to observe. Urgent incidents can precede experiments.

Handoff: sending/receiving owners, desired output and acceptance, input/access/authority boundary, dependencies, agreed timing or unknown, escalation route, acknowledgement and receipt. Ownership remains explicit until accepted; avoid two operators independently contacting the same customer or changing the same resource.

## Reporting and session resume

Report according to the user's chosen rhythm or meaningful decision event: headline result against baseline/target with as-of date; supporting health metrics; shipped/delivered value with evidence; initiative decisions; spend/commitments/runway assumptions; incidents/customer risks; dependencies/approval requests; next priorities and resource tradeoffs. Activity totals may provide context but are not the main result.

On resume: read snapshot and recent events → check authority and revocations → reconcile pending/uncertain effects → refresh decision-critical metrics → check customer/dependency changes → select the next authorized action. End work with an updated snapshot and resume pointer. If persistent writes are unavailable, return a complete handoff and disclose that memory was not saved.
