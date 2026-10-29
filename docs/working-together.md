# Connect the skills

Each skill is usable alone. For larger work, keep one outcome owner and one canonical ticket per work unit.

```mermaid
flowchart LR
  Q[Ticket and acceptance criteria] --> F[Software or marketing factory]
  F --> W[Versioned work]
  W --> E[Independent evaluation]
  E --> A[Authorized release or experiment]
  A --> V[Live verification and measurement]
  V --> L[Learning and follow-up ticket]
  L --> Q
```

| Skill | Owns | Hands back |
| --- | --- | --- |
| scrum-master | Readiness, decomposition, capacity, sprint feedback | Testable stories with owners and dependencies |
| software-factory | Code delivery and release evidence | Reviewed revision, CI results, release identity, QA evidence |
| marketing-factory | Hypothesis, experiment, outcome measurement | Artifact revision, exposure window, result and limitations |
| ad-buying | Paid media preparation and authorized execution | Actual entity states, previews, spend and conversion evidence |
| web-publisher | Site delivery and access verification | Release artifact, URLs, access matrix, rollback evidence |
| remember | Durable approved preferences and decisions | Scoped entries with source and review dates |

Marketing may request an instrumented landing page from software. Software returns the deployed revision and event verification; marketing then checks the measurement contract before running its own authorized experiment. A handoff never grants the recipient extra spending, publishing, or deployment authority.

Use a handoff record with parent ticket, receiving owner, objective, acceptance, source revision, permitted data, action limits, remaining budget, due date, and result evidence. Search for an existing handoff before retrying. If a response is unknown, reconcile it before duplicating a ticket, deployment, or campaign.

Change the reusable workflow only from repeated evidence or a demonstrated consequential failure. Keep product work and changes to its evaluator separate, so an operator cannot declare success by changing the grading rule after seeing the result.
