---
name: ad-buying
description: "Analyze paid-media performance, prepare campaign and creative experiments, build paused ads, and verify authorized launches in the selected ad account. Use for media buying rather than general organic marketing."
---

# Ad buying

Operate from the selected business, offer, account, and measured business outcome. A prepared campaign is not a live campaign, platform-attributed revenue is not causal lift, and a successful API response is not a verified launch.

## Establish the brief and authority

Read existing account and campaign records before requesting missing details. Verify business/account identity, currency, timezone, billing units, objective, conversion event and dataset, destination, brand or publishing identity, audience, exclusions, geography, placements, budget owner, and dates. Keep organization-specific facts in the user's private project profile, not this reusable skill.

Record the requested action and existing authorization. Reporting or preparing ads does not grant permission to activate them, increase spend, edit live delivery, or delete records. Honor a prior explicit grant within its actual limits; do not ask for the same permission twice. Build authorized new entities paused at every controllable level, and verify the persisted and effective statuses. If safe paused creation cannot be guaranteed, prepare the reviewed specification locally instead.

Discover available connector schemas and current platform requirements. For Meta work, read [connector capability checks](references/meta-capabilities.md) before building or duplicating. No tool name or old limitation in a source document is proof of today's capability.

## Analyze performance

Specify the reporting window, account timezone, currency, attribution window, conversion definition, and data freshness. Read enough history for the requested comparison and account for conversion lag, late revenue, refunds, and tracking changes.

Report spend and the relevant funnel: impressions/CPM, clicks/CTR/CPC, qualified conversions/CPA, attributed revenue/ROAS, and downstream quality when available. Distinguish all-click CTR from link CTR. Calculate aggregate ratios from summed numerators and denominators; do not average row-level CPA or ROAS. A zero or missing denominator yields unavailable, not zero performance.

Connect observed changes to a testable explanation. Compare like periods and cohorts; flag small samples and confounding changes. Use attributed results as directional evidence, and use a valid holdout or experiment for causal claims. Do not claim certainty from a platform recommendation or benchmark.

## Prepare creative and a test

Read [copy and evidence](references/copy-and-evidence.md) for offer grounding and aligned copy fields. For video batches, read [video pipeline](references/video-pipeline.md).

Define the audience, hypothesis, variable being changed, primary outcome and guardrails, allocation/budget cap, observation window, conversion-lag treatment, and stop/continue decision before launch. Label exploratory tests when the available volume cannot support a decisive result. Changing the success metric after seeing results starts a new decision; preserve the original result.

Build a reviewable campaign specification with exact account, publishing identity, objective, conversion tracking, audience, exclusions, budget placement, amount and units, dates/timezone, placements, URL/UTMs, creative mapping, and status. Inspect the destination and conversion path. Verify current policy and any special category requirements relevant to the actual campaign; do not assume an old creative approval still applies.

## Build, verify, and launch

Use supported operations and reconcile existing entities before creating duplicates. Validate one representative creative before a batch. Preserve receipts and a file-to-copy-to-platform-ID mapping. Read back targeting, optimization, budgets, schedule, destination, identity, tracking, and all relevant statuses. Inspect rendered previews for the intended placements, including mobile, cropping, caption readability, and CTA alignment.

An exact clone requires verified source settings. If the connector cannot read or copy targeting, exclusions, conversion settings, or placement controls, use an authorized native duplication flow or leave a staged specification. Never silently replace a curated audience with broad targeting.

Before an authorized activation, present or reference the concrete reviewed entities, spend limit, schedule, success/stop rules, and material changes since approval. Activate only within the user's grant. Re-read effective delivery statuses and budgets afterward; distinguish paused, pending review, scheduled, active, and delivering. If a mutation times out, reconcile account state before retrying.

## Close the loop

Return preview/record links, what was prepared versus actually changed, spend exposure, verification evidence, open blockers, and the next decision date or trigger. Persist the result in the existing work/experiment record. Recommend the next test from evidence; do not automatically schedule monitoring or spend without authorization. Pause or rollback only under an existing applicable grant or a new user instruction.
