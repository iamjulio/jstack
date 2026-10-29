# Task A — finish migration verification and repair the homepage

## Decision and present state

Proceed with the already authorized homepage repair through the configured shared deployment coordinator: redeploy the immutable intended r9 complete artifact using the provider-supported cache-clearing behavior available through that coordinator. Preserve its siblings, routing, authentication, API mounts, domain bindings and certificates. Do not edit DNS, recreate a site/binding, migrate providers, or substitute a query-string URL for the visitor homepage.

The supplied observations demonstrate a stale public CDN error at the plain canonical homepage: `https://www.example.test/` returns 404, generic `Site Not Found`, `x-cache: HIT`, while its explicit index, query variant and both provider aliases serve the expected r9 bytes. Bindings/certificates are ACTIVE and authoritative DNS is correct. The apex homepage has its own cached 404; success for its new-path redirect does not verify that homepage.

Actual completion state: the migration is reported deployed, but live homepage verification fails. The repair has not been submitted or executed in this restricted exercise. It is not live verified. No successful deployment receipt, invalidation result or post-repair response is invented.

## Concrete next actions

1. In the intended project repository, read the existing deployment configuration/profile and normal coordinator entry point. Resolve the actual repository/ref, immutable r9 artifact location, manifest/digest, r9 provider version, account/environment, configured aliases, sibling manifest and current access configuration. Use the configured pinned toolchain; do not create an ad hoc uploader. If immutable r9 bytes need reconstruction, build from their recorded commit with the pinned dependencies and require equality with the r9 manifest before release.
2. Persist a unique repair attempt and release intent, immutable artifact digest, expected prior release r9 and existing rollback information. Confirm no prior provider write is uncertain; if one is uncertain, reconcile it before any redeployment.
3. Acquire the existing shared coordinator claim at its configured site or environment/project scope. Verify claim ownership and execution identity, then read actual provider state under that claim. Compare it with the provider version represented by r9. Refuse promotion on mismatch; inspect the winner and rebuild/replan against current content rather than overwriting a concurrent release.
4. Through that coordinator, submit the normal redeployment of the exact intended r9 artifact. This is the selected cache repair, not merely a proposal for investigation. Supply the existing deployment grant, immutable artifact and digest, expected prior provider version, unchanged route/access configuration and attempt/claim identity. Confirm claim ownership before provider mutation and again before promotion. No additional user permission is needed for this authorized repair.
5. Wait for provider deployment and applicable cache refresh/invalidation completion. Retain the provider operation identifier, resulting release/version and timestamps. On a timeout, read operation status and served revision before retrying. After two unresolved reconciliation attempts, retain the claim/recovery evidence and stop dependent mutations.
6. Verify the exact plain canonical and apex homepages again, followed by the explicit index, a new unique query variant and all configured aliases. Verify the apex path/query redirect independently. Check expected bodies/build identifiers and relevant headers, preserved siblings/assets/app mounts, intended unknown-route behavior and HTTPS/TLS. For any restricted routes on this content-only repair, first confirm gate code, identity policy, routing, backend mounts and host/origin inventory are unchanged. Existing complete boundary evidence may support those unchanged boundaries, with fresh owner/content, dependent-asset, sibling-preservation and anonymous/no-store checks on the current artifact and relevant serving hosts. Record its prior revision and identity checks not repeated. If the boundary changed or complete prior evidence is unavailable, collect the full applicable boundary checks; no prior successful boundary evidence was supplied in this exercise. Query success alone cannot close the repair.
7. Save a sanitized release receipt with actual changes, observed statuses/body hashes, identities, URLs, timestamps, resulting provider release and unexecuted checks. Release only the exact owned coordinator claim once operations are settled according to the established workflow.

## Commands and inputs needed

The real repository path, coordinator command/tool, adapter and verified tool versions were not supplied. Read them from the configured project before execution; do not invent a CLI name or invoke provider-specific Firebase/AWS commands based only on this scenario. Invoke that existing coordinator with these concrete inputs:

| Input | Required value |
| --- | --- |
| Operation | Normal redeployment of intended artifact, with configured cache clearing |
| Artifact | Immutable complete r9 artifact; exact recorded manifest and digest |
| Expected prior release | r9 and its actual recorded provider version, checked under the claim |
| Target | Existing configured account, project/site and environment |
| Scope | Existing site claim, or environment/project claim if shared configuration is involved |
| Policy/routes | Current access policy, sibling pages and app mounts preserved |
| Recovery | Current configuration plus a known-good content target from recorded history; do not invent one |
| Journal | Unique persisted attempt, exact claim owner, provider operation and resulting receipt |

The following are unexecuted response-capture commands for the authorized execution environment. Set `EVIDENCE_DIR` to its approved evidence folder and `EXPECTED_R9_ROOT_BODY_SHA256` to the expected response-body hash from the r9 manifest. An archive digest must not be mistaken for an HTML response-body digest. `curl` must validate TLS; do not add `-k`.

```sh
curl --silent --show-error --max-redirs 0 --dump-header "$EVIDENCE_DIR/www-root.headers" --output "$EVIDENCE_DIR/www-root.body" 'https://www.example.test/'
curl --silent --show-error --max-redirs 0 --dump-header "$EVIDENCE_DIR/www-index.headers" --output "$EVIDENCE_DIR/www-index.body" 'https://www.example.test/index.html'
curl --silent --show-error --max-redirs 0 --dump-header "$EVIDENCE_DIR/www-fresh.headers" --output "$EVIDENCE_DIR/www-fresh.body" "https://www.example.test/?release=$UNIQUE_REPAIR_PROBE"
shasum -a 256 "$EVIDENCE_DIR/www-root.body" "$EVIDENCE_DIR/www-index.body" "$EVIDENCE_DIR/www-fresh.body"
curl --silent --show-error --max-redirs 0 --dump-header "$EVIDENCE_DIR/apex-root.headers" --output "$EVIDENCE_DIR/apex-root.body" 'https://example.test/'
curl --silent --show-error --location --max-redirs 5 --dump-header "$EVIDENCE_DIR/apex-root-chain.headers" --output "$EVIDENCE_DIR/apex-root-final.body" --write-out '%{http_code} %{url_effective}\n' 'https://example.test/'
curl --silent --show-error --max-redirs 0 --dump-header "$EVIDENCE_DIR/apex-path.headers" --output "$EVIDENCE_DIR/apex-path.body" 'https://example.test/new-path?x=one%20two'
```

Capture the equivalent plain and fresh probes for both actual provider alias URLs from the profile. Record HTTP status from headers, compare each intended success body with its manifest assertion, and record time and build identifier. For the path test require `Location: https://www.example.test/new-path?x=one%20two` with no loop; the final unknown-path status must match the site's intended routing, not be forced to 200. The apex homepage must redirect to the canonical HTTPS homepage and terminate in the expected r9 body. Repeat plain-root probes after the initial success to exercise warm caches.

## Acceptance and recovery

Acceptance remains open until the coordinated operation has completed and both the plain visitor homepage and an independently fresh variant return the expected r9 content; the apex plain homepage must reach that canonical content. Require correct explicit index/aliases, preserved path/query redirect, no loop/TLS warning, preserved neighboring content/mounts and applicable access checks. Retain status, body assertion/hash, release, timestamp and evidence location for each observation.

The supplied pre-repair evidence passes artifact availability, authoritative DNS and active binding/certificate diagnosis. It fails both plain homepage checks. All post-repair and remaining applicable live checks are unexecuted here.

Use the same coordinator for any needed rollback, comparing against the then-current provider release and retaining current access restrictions. Redeploying r9 for cache repair is not evidence of a recovery rehearsal. The actual known-good historical target/rehearsal evidence must come from the configured publisher; availability failure alone does not authorize disabling access controls. No infrastructure or cost-model change is proposed, and no price or live cost claim is made.

Instruction sources used: `SKILL.md`, `references/repository-coordination.md`, `references/deployment.md`, `references/verification.md`, and `assets/release-receipt.md` under `skills/web-publisher/`. No repository evals, changelog, external service or other user files were read.

## Final instruction revision

The entrypoint and verification reference were re-read after their documentation update. The content-only evidence rule above reflects those final contents. SHA-256 hashes actually observed:

- `SKILL.md`: `a10704a239ea2c4a21b2d98baf4cd4d6e67101dabac7e97820e8dd0b2bfa1af0`
- `references/verification.md`: `91fd376c89df9d640b07904681df7b5a89d7104bc27dcb81f10e06cd7b42ab92`
