# Live verification contract

Run checks against the deployed artifact and configuration, using minimal test data and the authorized environment. Record timestamp, URL/route class, identity class, response status, body assertion, build identifier, and evidence location. Remove tokens and personal identity data from retained evidence.

| Check | Required observation |
| --- | --- |
| Public landing and download | Expected content, correct revision, readable on mobile, working links and downloads |
| Canonical page and cache variant | Plain visitor URL and fresh query variant both return the intended content; compare with the artifact digest |
| Shared-site neighbors | Existing sibling pages/assets and configured app mounts are preserved |
| Unknown public route | Intended 404; no private fallback content |
| HTTP and TLS | HTTPS policy works; certificate/hostname valid; no mixed content |
| Redirecting apex or alias | Plain homepage reaches the canonical HTTPS host; independent path and encoded query survive without loops |
| Anonymous restricted page | Denied or sent to authentication; private body absent |
| Denied signed-in identity | Access denied; no private body or asset bytes |
| Permitted identity | Correct admin document and dependent assets work |
| Missing, malformed, expired, wrong issuer/audience token | Denied; no cache or error fallback leak |
| Default CDN hostname and every alias | Cannot bypass the restriction |
| S3 REST/website/object URLs | No anonymous protected object access |
| Protected data/assets/downloads | Same boundary as the admin page, including direct URLs |
| Warm cache | Authorized fetch followed by anonymous/denied fetch still denies |
| Path variants | `/admin`, `/admin/`, encoded and normalized forms, query variants, and rewritten/fallback routes stay protected |
| API action, if any | Backend authenticates and authorizes independently; denied identity cannot act |
| Preview/history URLs | No protected content leaks via preview, branch, historic deploy, or default hosting domains |
| Logout/revocation | Session behavior matches the documented expiry/revocation policy; test with a fresh session |
| Recovery | Known-good release restored in rehearsal; access restrictions retained |

A `200` login screen is not the private document; a `403` containing confidential fallback HTML is still a leak. Assert absence of an unmistakable nonsecret test marker from restricted content as well as expected status/redirect. Use a clean browser context for anonymous tests. Test cache behavior after an authorized request instead of relying only on a cold request.

Use separate disposable test identities when authorized. Never paste live credentials or tokens into reports, third-party JWT debugging websites, public issue comments, or screenshots. Keep a sanitized evidence receipt and retain sensitive logs only in the organization's permitted system.

For a content-only update, first confirm that gate code, identity policy, routing, backend mounts and host/origin inventory are unchanged. Existing complete boundary evidence can then support the release alongside fresh owner/content, dependent-asset, sibling-preservation and anonymous/no-store checks against the current artifact and all relevant serving hosts. New or changed access behavior requires the full identity, logout and warm-cache sequence. Record the prior evidence revision and name identity tests not repeated; a CLI's pending identity entry is not a completed browser test.

## Domain and stale-cache diagnosis

Compare the exact plain URL, explicit index file, fresh query variant and provider aliases. A provider's generic site-not-found page differs from the intended application 404; identify the body, release and cache headers before concluding the artifact is missing. Check a redirect's homepage independently: a new path can work while `/` still has a cached error.

Separate authoritative DNS, recursive/provider lookup state, certificate provisioning and CDN content. If authoritative records are correct but provider checks show older values, retain the working records and inspect propagation before making another DNS edit or recreating a binding. Use an official cache-refresh mechanism only when the stale lookup is demonstrated, then verify the provider and actual HTTPS again. Do not bypass a certificate warning.

Once the binding is ready and a stale public CDN response is demonstrated, use the provider's supported invalidation or coordinated redeployment of the intended artifact. Preserve the expected prior release and sibling pages. Verify the same plain URL afterward; adding a query string is a diagnostic probe, not the final fix. An uncertain previous write still requires reconciliation before another release.

Provider documentation reviewed October 29, 2026: Firebase Hosting includes hostname, path and query in cache selection, and a site redeployment clears its CDN content. See [Firebase cache behavior](https://firebase.google.com/docs/hosting/manage-cache), [custom-domain validation](https://firebase.google.com/docs/hosting/custom-domain) and [Google Public DNS cache refresh](https://developers.google.com/speed/public-dns/cache). Apply provider-specific remedies only to a matching configured stack.

If authorization tests fail, block restricted publication and restore the safe serving configuration within the existing release grant. Report the exact failing path, affected revision, and containment evidence. Do not claim all-host security from one successful login test.
