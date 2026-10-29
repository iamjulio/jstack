# Live verification contract

Run checks against the deployed artifact and configuration, using minimal test data and the authorized environment. Record timestamp, URL/route class, identity class, response status, body assertion, build identifier, and evidence location. Remove tokens and personal identity data from retained evidence.

| Check | Required observation |
| --- | --- |
| Public landing and download | Expected content, correct revision, readable on mobile, working links and downloads |
| Unknown public route | Intended 404; no private fallback content |
| HTTP and TLS | HTTPS policy works; certificate/hostname valid; no mixed content |
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

If authorization tests fail, block restricted publication and restore the safe serving configuration within the existing release grant. Report the exact failing path, affected revision, and containment evidence. Do not claim all-host security from one successful login test.
