---
name: web-publisher
description: "Publish and maintain static websites from GitHub through private S3 and CloudFront, with verified access control for admin pages and release rollback. Use for hosting, deployment, protected static content, and live publishing checks."
---

# Web Publisher

Turn a repository revision into a reproducible release with working URLs, protected content, a cost estimate, and a tested recovery path. This skill supplies a workflow; cloud resources and credentials must be configured in the target environment.

## Establish the publishing contract

Read the existing repository, build command, deployment configuration, domains, cloud account identity, and authorization. Discover available connectors or CLIs rather than inventing tool names. Reuse a working pipeline when it meets the request.

Record the actual repository/ref, output directory, environment, public and restricted routes, permitted identities, budget, deployment grant, and previous release. Use [the profile template](assets/publishing-profile.yaml) if no equivalent exists. Keep real profiles and credentials outside a public skill repository. A site request can authorize preparing a release; use existing session authorization to determine whether its deployment is also included.

Before cloud changes, choose the topology using [architecture](references/architecture.md). Default public static hosting is private S3 through CloudFront OAC. Restricted content needs its own complete authorization boundary. A Cloudflare login page on the custom domain does not protect the CloudFront distribution URL.

## Prepare, release, verify

1. Build from the intended commit using pinned dependencies. Check generated files, links, mobile layout, accessibility basics, 404 behavior, and exposed configuration. Public build output must exclude restricted documents, source maps containing private data, credentials, and server-only configuration. A public source repository cannot keep committed admin content confidential.
2. Produce the reviewable release artifact and manifest. Separate public assets from admin assets; use distinct buckets/distributions when that simplifies the boundary. Configure least-privilege deployment identity and an explicit rollback target. Follow [deployment](references/deployment.md) for AWS, GitHub OIDC, caches, and rollback.
3. Apply the authorized release and wait for provider completion. Reconcile remote state before retrying a timed-out write; do not repeat DNS, resource creation, or publication on uncertain outcomes. Stop dependent changes after a second unresolved failure and report the evidence needed to recover.
4. Run [live verification](references/verification.md). Inspect actual response bodies as well as status codes. Test a permitted identity, a denied identity, a clean anonymous session, alternate hostnames, direct object URLs, protected assets, and warm caches. Verify the deployed commit/build identifier.
5. Record the revision, deployment receipt, URLs, verification results, actual resource changes, cost assumptions, rollback instructions, and remaining gaps. Use [the release receipt](assets/release-receipt.md). Say "prepared", "deployed", or "live verified" according to the evidence. A passing build alone does not establish live success.

## Access and operating constraints

- Private S3 access is origin protection; it does not authenticate website visitors. CORS, hidden navigation, robots rules, client-side passwords, and unguessable URLs do not provide authorization.
- Authenticate every request that can return restricted content, including cache hits. Authorize backend actions separately; a gated static shell cannot secure an unprotected API.
- Fail closed for missing/invalid tokens, verifier errors, and unknown routes. Never disable access control to recover availability without a new, explicit scope decision.
- Avoid storing confidential data in service-worker caches or shared CDN responses. Keep browser tokens out of logs, public build artifacts, and screenshots.
- Recheck provider terms and usage before cost-sensitive changes. Free identity seats do not make AWS hosting, edge execution, domains, logs, or bandwidth free.

## Example requests

- "Publish this lead magnet from the release branch and verify the download."
- "Keep the site on S3 and CloudFront, but protect the entire admin distribution."
- "Prepare a GitHub Actions deployment and a rollback rehearsal; leave production deployment for the release window."
