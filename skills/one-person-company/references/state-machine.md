# State machine and transition rules

Use three independent state layers: business lifecycle, continuous operating loops, and individual initiatives. Record transitions with prior/new state, time, evidence, decision owner, and unresolved conditions. Lifecycle states summarize readiness; they neither grant permissions nor prevent useful parallel work.

## Business lifecycle

| State | Entry evidence | Exit guard and next state |
|---|---|---|
| Framing | Outcome is requested; material assumptions remain unknown | Charter, scope, accountable owner, initial constraints and authority recorded → Discovery |
| Discovery | Customer/problem and value hypotheses are explicit | Evidence supports an initial offer and testable delivery path → Validation; revise or stop if contradicted |
| Validation | Offer/prototype can be tested safely with a defined audience | Proportional readiness checks and evidence of customer value support delivery → Operating; unresolved delivery gaps return to Discovery/Validation |
| Operating | Value can be delivered and monitored with support/recovery ownership | Repeatable demand, activation/retention, capacity and viable economics justify → Scaling |
| Scaling | A demonstrated mechanism and resource/quality guardrails exist | Increase investment only within authority; deteriorating economics, experience or reliability → Operating or Recovery |
| Recovery | Incident, breached guardrail or material failure threatens the outcome | Containment, cause assessment, restored service/value, verification and follow-up ownership → prior justified state |
| Closed | Explicit stop/transfer or verified goal closure | No automatic restart; a new authorized mandate may reopen with reconciled state |

An existing product can enter at Validation or Operating when evidence warrants it. “Mostly built” is not readiness evidence. A numeric target being reached does not automatically close a continuing retention mandate: verify the charter's observation period and ongoing ownership. Archive decisions and hand off customer/data obligations before closing.

### Readiness proportional to the intended action

For launch, feature rollout, or increased demand, verify the relevant customer journey (offer → purchase → entitlement → activation → support/cancellation), accuracy of public claims, instrumentation, operational ownership, realistic capacity, and recovery/rollback. Validate privacy/security and financial obligations relevant to that specific change. Use available test or staging environments. A draft experiment need not pass a production launch audit. Report unverified areas; do not claim launch readiness from code presence alone.

## Continuous loops

Each loop (strategy/learn, build/deliver, acquire/sell, serve/retain, finance/coordinate) can be Ready, Working, Waiting, Verifying, or Recovering. Record local blockers separately from the lifecycle.

- Ready → Working: actionable priority, required inputs/access, authority, and resources exist.
- Working → Waiting: a specific approval, dependency, customer response, or access is missing. Name the owner, requested decision, and permitted parallel work.
- Working → Verifying: output/action finished; acceptance or outcome evidence is pending.
- Verifying → Ready: results accepted and learning recorded; next work may begin.
- Any active state → Recovering: guardrail breach, failure or uncertain harmful effect; contain and investigate before normal execution resumes.

A blocked outreach initiative need not block support or product work. Escalate operation-wide constraints only when they prevent all meaningful progress.

## Initiative lifecycle

**Proposed → Prepared → Authorized → Running → Evaluating → Decided → Closed**

- Proposed: tie a hypothesis to a charter measure and customer evidence; identify uncertainty and alternatives.
- Prepared: exact deliverable/action, baseline, success/failure signals, evaluation window or event, resource cap, dependencies, risks and stopping/recovery plan are reviewable. Unknown resources mean bounded preparation only, not an invented spend cap.
- Authorized: existing grant covers the complete action, or a specific approval is recorded. An already authorized low-impact action can pass this guard without a new approval request.
- Running: inputs available, instrumentation adequate, and external-action record reserved; observe limits and customer impact.
- Evaluating: reconcile actual action completion, wait for the defined evidence, compare with baseline and caveats. Insufficient data remains insufficient, not a win or loss.
- Decided: choose stop, iterate, or scale with supporting evidence. Scaling is a new initiative when resource exposure/scope changes; recheck authority.
- Closed: outcome, learning, costs and follow-ups stored; owned tickets and dependencies transferred or resolved.

Prepared may enter Awaiting Approval; any state may enter Blocked (named dependency), Recovery, or Stopped (reason). Resume to the last justified state after reconciling intervening changes. Rejected approval → redesign or stop. Expired approval → reauthorization before effect. A failed hypothesis is useful evidence and can close normally; it is not inherently an operational incident.

## Recovery and uncertain effects

Contain proportionally: suspend the affected action or channel, preserve data and logs, protect customers, and use authorized reversible recovery. Do not destroy evidence or broaden scope to “fix everything.” Record symptoms, verified facts, competing causes, impact and uncertainty. Establish causal evidence where possible; distinguish correlation from cause. Escalate urgent customer/financial risk to the accountable owner through an authorized communication route.

Before any retry, inspect receipts, external state and action keys. If the effect is uncertain and duplication could matter, hold replay and reconcile or request resolution. Set a retry/stop boundary proportional to risk; do not loop indefinitely. Verify recovery, assign prevention tickets, and reassess the initiative and authority before restarting.
