# Let jstack choose the right skills

`jstack` selects skills and connects their outputs. A sprint report can use `scrum-master` alone. A campaign may use marketing to define the experiment, software to instrument a page, publishing to verify its release, and ad buying for paid execution. Independent preparation can run in parallel; dependent effects wait for accepted inputs.

## Public suite

Install the router and any companions you need, or point the agent at this verified checkout. The [public routing catalog](../routes/catalog.json) describes the seven specialists and pins their entrypoint hashes. The router is excluded from its own leaf routes to prevent recursion.

```sh
python3 scripts/jstack.py install --all --host codex
```

Existing installations are preserved: the installer aborts on collisions. You can install only `jstack` and use catalog pointers to a checkout while keeping other installed skill variants intact. The router archive contains routing guidance and fictitious configuration examples; it does not contain the companion instructions or your private configuration.

## Try a task

After installing the public suite, give your agent a concrete outcome:

```text
Use $jstack to help me launch an online course about smartphone photography.
Draft a landing-page outline, a two-week marketing test, and a way to measure
email signups. Keep everything as drafts for me to review.
```

The router selects the skills needed and passes each result to the next step. You can start with an idea and a few constraints; no routing profile or existing ticket system is needed for this draft-only task. When work requires a connected service, the agent checks the available tools and permissions before taking action.

## Optional: add your own private skills

If you have custom skills for your business or projects, you can connect them alongside the public suite. Keep private routing metadata in a private repository or local configuration folder. Follow the [profile/catalog contract](../skills/jstack/references/catalogs.md). Use an explicit profile for a task, or configure `~/.config/jstack/profile.json` with catalog pointers:

```json
{
  "profile_version": 1,
  "catalogs": [
    {
      "id": "public-suite",
      "visibility": "public",
      "path": "/path/to/jstack/routes/catalog.json",
      "scope": {"kind": "global", "id": "*"}
    },
    {
      "id": "private-work",
      "visibility": "private",
      "path": "/path/to/private-configuration/catalog.json",
      "scope": {"kind": "global", "id": "*"}
    }
  ]
}
```

The global container groups entries; each private route can narrow to a personal, project, or organization scope. Names may overlap. `public-suite:one-person-company` and a private organization variant have distinct identities. Explicit selection wins; otherwise a relevant scoped specialist takes precedence. A same-named skill from another organization is not a fallback.

Read summaries to choose a route, then only the selected instructions. Catalogs carry discovery metadata and source provenance. They do not store credentials, transfer grants, authorize reading all private state, or declassify private context for public artifacts. An unavailable or changed private source holds its affected actions while useful permitted preparation continues.

## Use and resume a chain

```text
Use $jstack to continue the online course launch we started.
Check the completed drafts, show what remains, and work through the next steps.
Keep anything that would go live ready for my review.
```

The router keeps one outcome coordinator, explicit deliverable owners, shared resource limits, and revision-bound handoffs. It can work in one session; skill chaining does not require new chats or delegate messages. On resume it checks completed work and uncertain external effects before retrying or changing routes. It does not restart the chain, create duplicate work, or multiply its budget.

## Maintain the public metadata

After changing the package manifest or a specialist entrypoint, regenerate and review the catalog:

```sh
python3 scripts/jstack.py catalog > routes/catalog.json
python3 scripts/jstack.py check
```

The checker rejects stale metadata. A recorded hash establishes consistency with this catalog, not a signed trust decision. Private catalog maintenance and real environment access remain separate from public package checks.
