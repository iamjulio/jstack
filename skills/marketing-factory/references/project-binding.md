# Project binding and channel adapters

Use the organization's existing systems before proposing a replacement. Inspect available tool schemas and current provider documentation when platform details matter. An old workflow's missing capability or account default does not apply automatically to another connector or organization.

| Binding | Decisions to record |
| --- | --- |
| Scope | Organization/tenant, owner, execution identity and permitted data |
| Queue | Canonical campaign/task project, IDs, native states and deduplication |
| Assets | Versioned brief/creative repository, review status and final revision |
| Customer/offer | Audience evidence, source of offer/pricing truth, claims substantiation |
| Channel | Publication/ad account, sender identity, supported draft/pause, preview and read-back |
| Measurement | Analytics/CRM source, event definitions, attribution window, deduplication and cohort joins |
| Authority | Granted actions, exact account/audience, caps, expiry and evidence reference |
| Limits | Spend/volume/time/attempt caps, stop rule and escalation owner |

Do not fill missing campaign budgets, audiences, customer evidence or claims by analogy to another organization. Continue research and draft production where possible. Save a local campaign draft if the canonical queue is unavailable; label it unsynced until a verified write returns its ID.

## Channel-specific verification

- **Paid ads:** inspect account currency, timezone and budget units. Read campaign/ad-set/ad hierarchy and effective status. Confirm the optimization event, destination, placements and audience. Create paused entities where supported and authorized; detect any active parent whose settings could make child changes spend. Reconcile platform conversion totals against the selected business record and attribution basis.
- **Email/outreach:** confirm actual sender and audience source, recipient scope, suppression/unsubscribe handling, and test/preview capability. Do not turn a draft request into send permission. Use a test recipient only within the grant; avoid logging unnecessary recipient data.
- **Organic publishing:** confirm account, final content/media revision, alt text where relevant, destination and scheduled timezone. A scheduler's accepted request needs subsequent status verification; do not assume it has published.
- **Website/landing page:** bind deployed revision, form/action and business event. Exercise a safe acceptance journey without creating duplicate payments, customer messages or CRM records. Confirm unauthorized access behavior where gating is required.

Record the provider's returned ID, status, timestamp, actual settings and preview/live URL. On partial success, query each affected object and preserve the receipt before any retry. Do not claim a provider enforces dedupe, locking or caps unless it actually does.

Keep API keys, account exports and raw customer lists out of public asset repositories. Store only approved aggregate or redacted evidence in shareable tickets. Missing integrations are a concrete prerequisite, not an implied permission to use another account or scrape private data.
