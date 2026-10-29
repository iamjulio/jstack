# Measurement and experiment design

## Define the result before launch

Specify a primary outcome, unit of analysis, eligible population, denominator, attribution/event window, data source and decision threshold. Choose an economically relevant outcome where observable: qualified activation, retained customer, incremental revenue or contribution after variable costs. Keep leading metrics to diagnose the funnel.

| Metric | Definition to establish |
| --- | --- |
| Conversion rate | Unique eligible units reaching the named event / unique eligible exposed units in the stated window |
| Cost per qualified outcome | Attributable campaign costs / deduplicated outcomes meeting a documented qualification rule |
| CAC | The included acquisition costs / new customers in the selected cohort; state cost coverage and attribution assumptions |
| ROAS | Attributed revenue / ad spend using the same currency and attribution window; it omits margin and may omit other costs |
| Contribution | Revenue less the declared variable costs; state refund, fulfillment, media and platform-cost coverage |
| Incremental lift | Treatment/control difference under a credible assignment design; observational attribution alone is insufficient |

Use null/unavailable for missing values, never zero. Handle zero denominators explicitly. Report source currency/timezone, window and any conversion/reporting delay. Do not combine incompatible attribution windows, deduplicate by name alone or sum overlapping platform totals.

## Choose a credible design

For a controlled experiment, write a falsifiable hypothesis and freeze the primary metric, practical minimum effect, allocation unit, sample/window, guardrails and decision rule before activation. Randomize at a unit that reduces cross-variant contamination where feasible. Keep the offer or other confounds fixed if testing creative. Use a holdout when estimating incrementality warrants its cost.

Determine a traffic/sample plan from the baseline and useful effect size with a suitable calculation or available statistical tool. If traffic is too low, narrow the question, lengthen within the grant, use qualitative research, or label the result directional. Do not invent statistical power, certainty or a universal minimum sample.

Observe the planned window and lag. A fixed-horizon test should not be repeatedly stopped on a favorable p-value; use an appropriate preregistered sequential method if continuous statistical stopping is needed. Safety/economic guardrails may stop a run independently and should be reported as such. Account for multiple variants/comparisons when making significance claims.

An observational campaign can still teach useful lessons. Record selection effects, changing audiences, seasonality and missing baseline. Describe associations and hypotheses; avoid causal claims without a credible design.

## Data validation before interpretation

Check event firing, unique identifiers, duplicate ingestion, missing cohorts, bot/test traffic, allocation balance, attribution lag and the path from channel click to business outcome. Compare tracking and business systems on an aligned cohort rather than forcing exact totals from different definitions.

Invalid measurement means the experiment is inconclusive even if the platform graph improves. Preserve the defect as a separate ticket and stop or limit further spend according to the actual grant and guardrails.

## Decision and feedback

Show absolute counts, denominators, costs, effect sizes and uncertainty; use confidence intervals or the stated statistical method where justified. Record decisions as keep/change/stop/inconclusive against the frozen rule. A statistically detectable effect can still fail the economic threshold. A non-significant result does not prove equivalence.

Turn one specific supported learning into the next test. Link the preceding experiment and document what changed. Do not change audience, offer, channel and creative simultaneously and attribute the result to one of them. Preserve failed and inconclusive experiments to avoid survivorship bias. Set a review owner and observation window for delayed outcomes such as retention, refunds or sales qualification.
