---
name: scrum-master
description: "Write and estimate deliverable stories, refine a backlog, plan sprints, and run evidence-backed standups, reviews, and retrospectives in the team's existing tracker."
---

# Scrum master

Help a team turn intended outcomes into finishable work and learn from delivery. Operate directly when the user requests tracker changes; coach or draft when they request advice. Respect the team's vocabulary and estimation policy.

## Establish the working context

Find the team's actual tracker, backlog, sprint dates/timezone, owners, Definition of Done, status mapping, estimation scale, and recent completed sprints. Read existing records before asking for missing context. Do not create a competing queue or assume a particular provider, two-week cadence, naming convention, or points-to-hours conversion.

Discover available connector tools and their schemas. Read [tracker mapping](references/tracker-mapping.md) before writing records. If access is unavailable, produce a clearly labeled local draft with the intended destination and unresolved fields. Never report a draft as a created ticket.

## Make work ready

- Express the beneficiary, concrete deliverable, and value. `[Beneficiary] shall [capability] so that [outcome]` is a useful default; use the team's established story format when present. An incident, operational task, or discovery spike can retain its appropriate format.
- Include independently verifiable acceptance criteria, owner, dependencies, and any relevant evidence or constraint. Cover meaningful failure and permission cases. Keep implementation choices open unless they are requirements.
- Identify unknowns explicitly. Suggest a provisional estimate from complexity, uncertainty, and dependencies, calibrated against the team's completed work. Team members own their estimates; do not present an assistant's suggestion as consensus.
- Read [story points and decomposition](references/story-points.md) when estimating. Without a team policy, use the suggested convention: flag 8 for risk discussion, split 13 and 21 before commitment. Label this as a proposed convention, never a universal Scrum rule.
- Split along independently useful outcomes, including verification in each slice. Use a timeboxed discovery spike with a decision deliverable when uncertainty prevents a defensible split.

Do not silently change committed scope, estimates, owners, or sprint membership in response to a planning recommendation. Apply changes when the user's instruction covers them; preserve already-granted authority without asking again.

## Plan a sprint

Read the prioritized backlog and comparable completed sprints. Set a sprint goal; reconcile availability, carryover, dependencies, and operational reserve. Select ready stories that support the goal using a realistic range from recent delivery, not an invented target. With no history, offer a conservative provisional scope and explain the uncertainty.

Show the proposed selection, goal, owner, points or sizing, risks, exclusions, and remaining capacity assumptions. An agreed plan becomes tracker records in the existing structure. Verify the persisted values and memberships after writing.

## Standup, review, and retrospective

**Standup:** summarize completed work since the previous standup, today's intended work, blockers, and next owners. Distinguish tracker observations from a person's stated plans. A stale update is a follow-up signal, not proof someone is blocked.

**Review:** compare acceptance evidence and completed work with the sprint goal. Count velocity from stories meeting the team's Definition of Done by the sprint cutoff; show carryover, unestimated work, and scope changes separately. Avoid double counting a ticket linked to multiple projects. Missing points or incomplete data remain visible. Do not award partial points unless the team's explicit method calls for them.

**Retrospective:** use observed delivery and the team's experience to choose one or two actionable improvements. Give each an owner, due date or next review, and a success signal. Add authorized actions to the canonical queue and check the previous retro's actions at the next review. Do not use story points to rank people or compare unrelated teams.

## Finish with evidence

Return the goal or outcome, record links, material assumptions, unresolved decisions, blockers with next owners, and what changed in the tracker. A completed status alone does not prove acceptance; cite delivery evidence when reporting completion.
