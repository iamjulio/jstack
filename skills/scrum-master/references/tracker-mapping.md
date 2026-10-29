# Map the existing tracker

Map concepts to actual records before writing:

| Concept | Discover and verify |
| --- | --- |
| Team / workspace | Correct organization, access, and execution identity |
| Backlog / epic | Existing project, parent, or label convention |
| Sprint | Identifier, start/end dates, timezone, membership semantics |
| Story points | Numeric field or enumeration and exact valid IDs |
| Status | Allowed transitions, board section versus status field |
| Owner | Actual user identifier, not an ambiguous display name |
| Acceptance | Supported body format and evidence location |

Tool names and parameter shapes vary across providers and connector versions. Discover them instead of treating an example name as a callable API.

For Asana, check field and enum GIDs, membership and section semantics, and whether the connector accepts plain text or `html_notes`. Multi-homing must be performed through a supported explicit operation and read back; creating in one project does not prove membership in another. Avoid duplicating the same task to represent epic and sprint membership.

For Jira, verify issue types, project-required fields, sprint/points custom-field IDs, and permitted transitions. For GitHub Issues/Projects, verify whether sizing and iteration live in project fields rather than issue fields. Map the team's native states instead of inventing a parallel state machine.

Before retrying a create after a timeout, search for the intended record using its stable source or dedupe key. An unknown response is not proof the write failed. Read back material writes, preserve record links, and report any reconciliation needed before another attempt.
