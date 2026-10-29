# Contributing

Fix a demonstrated recurring problem. Keep the skill useful to someone with a different company, account, tool provider, and machine.

1. Describe the request and failure with sanitized evidence.
2. Make the smallest instruction or helper change that improves the decision.
3. Put detailed conditional guidance in linked references. Keep the entrypoint short.
4. Add or improve a behavioral case for a consequential decision; test executable helper behavior when it changes.
5. Run `python3 scripts/jstack.py check`, `python3 -m unittest discover -s tests -v`, and `python3 scripts/jstack.py bundle --all`.
6. Independently forward-test changed factory, spending, access-control, or memory boundaries. Report the actual scope and limitations.

Use simple frontmatter: `name` as an unquoted slug and `description` as a single JSON-quoted string. Each skill has a short `agents/openai.yaml` and is fully usable when copied alone. Do not reference files outside the skill from its runtime instructions.

Never submit private profiles, transcripts, account IDs, client identities, personal paths, credentials, or live campaign data. Confirm you can redistribute contributed material. A pattern scanner can miss context-sensitive disclosures; manually review the full staged tree before publication.

When changing a provider runbook, check primary documentation and record the review date. A known connector limitation is a dated observation, not a universal API rule.
