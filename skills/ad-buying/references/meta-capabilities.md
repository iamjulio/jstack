# Meta connector capability checks

Verify current connector schemas and official platform documentation when technical requirements matter. The names below describe capabilities, not guaranteed tools or fixed parameter contracts.

| Capability | Verify before acting |
| --- | --- |
| Accounts and publishing identities | Correct account/business, currency, timezone, Page/identity access |
| Metrics | Supported level/fields, pagination, date window, attribution window and freshness |
| Campaign / ad set creation | Supported objective, budget placement/units, schedule and explicit paused state |
| Conversion optimization | Valid event, dataset/pixel, destination and any required promoted object |
| Video upload and listing | Upload support, actual file-to-ID match, processing status, thumbnail fields |
| Creative and preview | Actual primary-text/headline/description mapping, required thumbnail, placement preview |
| Duplicate | Which source settings copy, which fields remain unreadable, and read-back access |

## Failure patterns to investigate

- A browser editor URL may identify an unpublished draft that the API cannot see. Empty search results can also mean the wrong account, missing access, filters, pagination, or a connector restriction. Check name, ID, scope and native draft state. Do not ask the user to publish merely to make it queryable: publishing can affect delivery. Establish paused state and authorization first.
- Some connectors expose only partial fields by default. Missing targeting or a dataset in a list response is not proof it is absent. Request supported detail fields or inspect the native record.
- Some connectors lack video upload; others support it. Use the discovered capability. Do not encode “no upload tool exists” as a platform rule.
- Some creative creation paths require an explicit video thumbnail. Read the current schema and video metadata. Supply a verified thumbnail when required; do not assume the first frame will be generated.
- A duplication endpoint can still require explicit settings or omit audience details. Native duplication is a fallback when authorized, not proof an API can never clone. Compare the resulting settings before calling a copy faithful.

In some Meta schemas primary text appears as `body` on reads and `message` inside a creative, headline as `title`, and description as `link_description`; other schemas wrap or rename them. Validate the actual API shape. Resolve current objective/optimization enums rather than copying old examples.

Distinguish a configured status from effective delivery. An active parent can expose spend as soon as a child is activated. Conversely, an `IN_PROCESS` review state does not establish that a paused entity is delivering. Verify the platform's reported state instead of inferring it from a label.
