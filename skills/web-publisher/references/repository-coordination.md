# Repository and concurrent publishing

Use a repository as the durable publishing contract. The source and deployment tooling can live in separate repositories, but record their identities, release refs, build/output mapping and artifact provenance. Keep private content in private repositories or private artifact storage. Do not infer repository privacy from a gated website URL.

## Source integration

Fetch the current remote before editing or integrating. Give concurrent agents separate branches and worktrees/checkouts; do not pull, stash, reset or switch another agent's working directory. Respect the project's existing review and branch rules. A publishing request does not authorize merging unrelated changes.

Merge or rebase the intended update against the current release branch using the project's convention. Preserve a conflicting branch and surface the concrete conflict; do not resolve it with blanket ours/theirs, force-push over others' work or publish a pre-merge artifact. After integration changes source, rebuild and rerun the checks affected by that change. Record the actual integrated commit and artifact digest.

Use normal fast-forward pushes or explicit compare-and-swap updates. On a rejected push, fetch and inspect what changed. Disjoint updates can be merged with a bounded retry; same-site content/policy conflicts need deliberate integration. Do not retry an identical stale release until it overwrites the winner. Reconcile a lost push response by reading the remote ref before creating another commit or retrying.

## Pages sharing a site

Record a page's destination namespace, owned file manifest and baseline release. A path-aware adapter may compose disjoint page updates against the latest complete site under its shared claim, provided it detects same-path drift and prevents overlapping ownership. Do not assume a path option exists for every audience or adapter.

For an adapter that accepts only complete-site output, copy the current archive in an isolated checkout, replace only the intended page's owned files, and verify untouched sibling bytes. Preserve existing routing, backend mounts and access configuration. Bind the prepared release to the same baseline used for composition. If the live/shared receipt advances, inspect the competing change and rebuild before preparing again; merely accepting the new receipt for an old composed folder can silently erase a sibling update.

Save the integrated source revision, base release/provider version, artifact digest and preservation results in the existing project receipt. A source push alone does not establish a deployed page. Rollback of a complete site also affects its other pages and requires that intended scope.

## Deployment coordination

Serialize promotion for every shared mutable resource. A per-site claim is sufficient only if sites do not also mutate shared authentication, DNS, routing or project configuration; otherwise use an environment/project claim. Source editing and local builds can remain parallel.

Use a real shared mechanism, such as the existing CI concurrency group or an atomic remote lease. A lock under one checkout cannot coordinate another worktree or computer. Persist the owner/attempt identity before acquiring the claim, confirm ownership before each provider mutation, and release only the exact claim owned by that attempt. Owner-specific local recovery files avoid one agent deleting another's receipt during handoff.

Read the deployed provider version under the claim and compare it with the expected prior release. Reject stale or out-of-band state before mutation and again before promotion. Providers without conditional release APIs cannot be made fully transactional by Git alone: document that all cooperating publishers must use the coordinator and treat bypass/manual-console changes as drift to investigate.

## Journal, crashes and rollback

Persist immutable artifact bytes, digest and release intent before provider effects. Keep durable identifiers for resource creation, upload, promotion and verification. Recover an existing matching artifact after an interrupted metadata write; do not overwrite it or mistake an old live version for proof that a new attempt deployed.

Write a submission-uncertain intent before a non-idempotent create call. If its response is lost, inspect the original operation/resource; an empty eventually consistent listing is not permission to create another resource. If an operation remains unknown, hold dependent effects.

Do not expire or steal a lease just because a timer elapsed or its parent PID died. Child processes and asynchronous cloud operations can still be running. Resume only after verifying the original writer and its provider operations have stopped/settled, using the exact expected claim identity and an atomic owner change. Cross-machine recovery without the original recovery evidence needs an explicit inspected recovery procedure.

Keep the claim when a provider effect is uncertain or a recovery fails. Use bounded reconciliation and preserve receipts/workspaces on unresolved conflicts. Rollback is another coordinated release: restore known-good content using current access policy, compare the expected live version, wait for completion and verify the result.

Acceptance should exercise two independent clones, same-resource exclusion, disjoint and conflicting pushes, stale artifacts, lost push/create responses, crash recovery and rollback artifact restoration. Local coordination tests do not establish live provider fencing or access-control success.
