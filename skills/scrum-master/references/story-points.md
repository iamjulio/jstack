# Story points and decomposition

Points express relative size informed by complexity, uncertainty, and risk. They are not elapsed time, individual productivity, or portable units between teams. Prefer the team's existing scale and reference stories.

When no policy exists, offer this convention explicitly as a starting point:

| Points | Typical shape | Planning response |
| --- | --- | --- |
| 1 | Familiar, small, no meaningful unknowns | Ready after acceptance is clear |
| 2 | A little variation or coordination | Check the dependency |
| 3 | Several clear steps with limited uncertainty | Compare with a completed reference story |
| 5 | Multiple moving parts or a material unknown | Resolve the main risk before commitment |
| 8 | High uncertainty or coupled dependencies | Flag the risk and propose a smaller slice |
| 13 | Too large or uncertain for a useful commitment | Split into useful stories, or run discovery |
| 21 | An epic or unresolved body of work | Decompose before sprint selection |

An 8 needs visible discussion under this convention. A 13 or 21 should not enter a sprint unchanged. A team can explicitly choose a different policy; do not mislabel the convention as a rule of Scrum.

Ask only about uncertainties that affect the estimate. Use independent team estimates before discussing divergence when facilitating a group; avoid anchoring everyone to the assistant's first number.

## Split by outcome

For “customers can manage subscriptions,” possible slices are viewing the current plan, canceling at renewal, and changing the plan. Each includes its own behavior, permissions, failure handling, and evidence. “Build frontend / backend / tests” creates dependent components rather than independently accepted outcomes.

For “investigate a new attribution provider,” a spike can deliver verified API capabilities, privacy constraints, a sample data comparison, and an adoption decision by a stated timebox. Do not assign a delivery promise while the core feasibility remains unknown.

Revisit estimates when scope or dependencies materially change. Preserve the original commitment and scope-change history when reporting a sprint; do not rewrite the baseline to make performance appear better.
