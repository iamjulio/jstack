# Hosting and access architecture

Provider sources checked October 28, 2026. Recheck current limits and product support before implementation. The topology choices below are engineering recommendations derived from these capabilities; they are not predeployed infrastructure.

## Public site: GitHub → S3 → CloudFront

Use a regular S3 REST origin, Block Public Access, bucket-owner-enforced ownership, and OAC with requests always signed. Scope the bucket policy to the intended CloudFront distribution and object prefix. S3 website endpoints cannot use OAC. Treat an existing public bucket as a migration requiring an inventory of consumers, not an invitation to change access blindly. See [AWS OAC guidance](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html).

Require HTTPS. Custom CloudFront viewer certificates from ACM belong in `us-east-1`, with domain names matching distribution aliases. Preserve DNS validation records for renewal. See [AWS certificate requirements](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-requirements.html).

## Restricted admin: select a complete boundary

Prefer an isolated admin hostname and output artifact. Do not put private JSON, downloads, maps, or prerendered HTML into the public artifact merely because the navigation is hidden.

### Keep restricted static content on S3/CloudFront

Use a separate private bucket and distribution. Place Cloudflare Access on the proxied admin hostname with an explicit identity allowlist and no broad bypass policy. Also validate the Access JWT at CloudFront's **viewer-request** stage for every behavior capable of returning admin content, including the default behavior. Validate signature, trusted algorithm, issuer, audience, expiration, and required identity claims; handle signing-key rotation and verifier failures by denying requests. Restrict accepted hostnames as defense in depth. Do not accept a header merely because it is present, and do not rely on a shared header as user authentication.

Cloudflare documents token validation and its application-specific audience in [Validate JWTs](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/). AWS documents that viewer-request processing runs before cache lookup, whereas origin-request processing runs only on cache misses in [CloudFront trigger events](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-cloudfront-trigger-events.html). Combining these is a design requiring a maintained JWT verifier, supported edge runtime, deployment tests, and additional cost; it is not accomplished by a DNS toggle.

An origin-request-only verifier is insufficient: a cached protected object could otherwise bypass it. Avoid shared caching of identity-dependent data; initially disable caching for restricted responses while establishing correctness. Keep access checks outside cached content generation. Error documents, SPA fallbacks, URL normalization, and rewrites must not expose a protected object through a behavior without the check. Never use confidential content as a custom error response.

Verify denial via the default `cloudfront.net` hostname, every alias, HTTP/HTTPS, alternate paths, and direct S3 endpoints. All unauthenticated routes to private bytes must deny or reach the same access boundary. If a reliable edge verifier cannot be maintained, keep private material unpublished and use the alternative below.

### Lower operational complexity: isolated admin origin through Access + Tunnel

Keep the public site on S3/CloudFront and serve admin content from an isolated service reached through Cloudflare Tunnel. Create the Access application before publishing the route. Block inbound origin access; enable the tunnel's token validation or validate tokens in the origin. Confirm the service has no alternate public listener. This adds a running host/service and does not use S3 as the admin serving origin. See [self-hosted application setup](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) and [Tunnel's outbound connection model](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

### Cloudflare Pages alternative

If the user accepts different hosting, Pages can simplify static delivery. Its preview Access toggle protects previews, not automatically the production `pages.dev` hostname or custom domain. Inventory and protect each production, branch, historic deployment, and custom hostname before storing restricted content. A redirect to a protected domain is useful only when the source URL cannot still serve protected bytes. See [preview access scope](https://developers.cloudflare.com/pages/configuration/preview-deployments/) and [default-domain configuration](https://developers.cloudflare.com/pages/configuration/custom-domains/).

## Cost decision

Cloudflare's [Access product page](https://www.cloudflare.com/sase/products/access/) currently advertises a $0 plan for teams under 50 users. Confirm account eligibility, seat counting, feature limits, and current terms; do not promise a permanent allowance.

Estimate monthly requests, storage, transfer, build minutes, logs, invalidations, and edge/auth execution separately. Consult [CloudFront pricing](https://aws.amazon.com/cloudfront/pricing/), [S3 pricing](https://aws.amazon.com/s3/pricing/), and the selected authentication/hosting plan. State region, traffic assumptions, included allowances, and likely overage drivers. Budget alerts are notification mechanisms, not guaranteed spend caps.
