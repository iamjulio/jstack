# Deployment and recovery runbook

## Repository and identity

- Confirm account identity and intended environment before writing. Use infrastructure as code for repeatable resources when the project already supports it; show the plan before applying an authorized material change.
- Separate build/test jobs from cloud deployment. Grant `contents: read` and grant `id-token: write` only to the deployment job. Prefer GitHub OIDC over long-lived AWS keys. Constrain AWS trust to the intended repository and branch or GitHub environment, plus the expected audience; environment-based subjects need matching environment branch restrictions. Scope IAM actions to the deployment bucket/prefix and intended distribution. Fork pull requests must not assume production credentials. See [GitHub's AWS OIDC guide](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws).
- Pin third-party Actions to reviewed full commit hashes, use lockfiles, and serialize deployments per environment. Do not introduce a broad `pull_request_target` deployment path executing untrusted code.
- Keep source public only when all committed content is suitable for public access. Build-time credentials never belong in client bundles. Store confidential admin data in an authorized private source and runtime boundary.

## Artifact and promotion

Build once. Record commit SHA, dependency lock digest, artifact digest, build command, content manifest, and environment. Scan actual output for private files and unintended routes. A manifest must classify public/admin content and list served assets, not just entry pages.

Upload immutable hashed assets before publishing HTML that references them. Use long-lived caching for immutable public assets and a short/no-cache policy for mutable HTML. Restrict the deployment role to its release prefix. Keep the previous release available; avoid a blanket `sync --delete` over a shared bucket. See [AWS versioned file guidance](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/UpdatingExistingObjects.html).

Promote by the project's established release switch, versioned origin prefix, or controlled entry-file update. Record the exact state change. Wait for asynchronous distribution updates and invalidations before declaring completion. Invalidate only necessary mutable paths; test against cached and uncached responses. Preserve correct content types, security headers, and compression. Test deep links without rewriting authorization errors into public success pages.

## Authorization changes

Deploy access checks and private origin policies before private bytes become reachable. For existing content exposure, establish the restriction first and purge cached copies; cache invalidation cannot revoke files already downloaded. Keep admin responses and service-worker handling conservative until warm-cache and identity-boundary tests pass. OAC, CDN auth, Access policies, API auth, and DNS are distinct configurations; verify each rather than inferring one from another.

## Rollback and uncertain outcomes

Record the prior release manifest and configuration revision. Before promotion, rehearse restoration in a preview or staging environment when available. Restore the prior known-good artifact through the same controlled mechanism, wait for propagation/invalidation, and repeat live checks. A content rollback must preserve the current access restrictions; do not restore an old permissive security policy merely because it accompanied the old content.

After a timeout, inspect deployment status and served revision before resubmitting. Reuse release identifiers and provider idempotency where supported; compare resource state before creating duplicates. Record partial effects and stop after two unresolved reconciliation attempts. Continue diagnosis and artifact preparation without changing additional production resources.

No preview environment or live access: deliver the exact artifact, plan, commands adapted to verified tool versions, unresolved prerequisites, and rollback steps. Label every unexecuted check. Do not invent provider receipts or claim a dry run exercised the live boundary.
