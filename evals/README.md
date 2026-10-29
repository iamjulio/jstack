# Evaluate decisions, not headings

File validation checks packaging. These cases evaluate what an agent does with ambiguous evidence, stale reviews, missing integrations, uncertain effects, and existing authority.

## Run a case

1. Freeze the skill revision and record agent/runtime/model settings.
2. Pick a case with `python3 scripts/jstack.py eval-list`.
3. Export its candidate packet: `python3 scripts/jstack.py eval-prompt web-alternate-domain`.
4. Give an independent agent the packet, the skill folder, and only the raw artifacts needed for the task. Keep the case's `checks` out of the candidate context. Use temporary files and simulated effects; do not spend money or touch live accounts to run this suite.
5. Save the actual response/actions. A separate reviewer compares observable behavior to the checks. Mark pass, fail, or inconclusive per check, with a quoted decision or artifact reference.
6. Report demonstrated failures, make a focused change, and repeat affected cases. Use new held-out cases to assess generalization; these public cases are regression examples, not a hidden benchmark.

Record the case ID, skill commit or content hash, candidate settings, allowed tools, output artifact, reviewer, per-check outcome, and limitations. Put private run data under ignored `evals/runs/` or outside the checkout. Publish only sanitized receipts.

No included command invokes a model or scores quality automatically. Exporting a prompt does not run the case. A simulated pass does not verify a live cloud configuration or paid-media account. Do not claim measured superiority without a comparable baseline, repeated runs, and outcome evidence.
