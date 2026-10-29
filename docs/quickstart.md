# Start with one real task

Install the skill closest to a recurring problem. Give your agent the task, the relevant evidence, the tools it can use, and the decisions already authorized. Ask it to use the named skill. You can also point an agent directly at a skill's `SKILL.md` before installing it.

## Try a task with the public suite

```text
Use $jstack to help me launch an online course about smartphone photography.
Draft a landing-page outline, a two-week marketing test, and a way to measure
email signups. Keep everything as drafts for me to review.
```

Replace the course with your own idea and add what you know about your audience, deadline, and budget. `jstack` chooses the skills needed; you can also name one directly, such as `scrum-master` for planning a sprint. This draft-only example needs no private profile, connected accounts, or existing ticket queue.

## Optional: add project setup

When you want to reuse project settings or work with connected services, copy a skill's profile template into a private folder outside this checkout, or an ignored `.local/` folder. Tell the agent where it lives. Profiles are read only when supplied or configured by the user; the skills do not assume the host automatically loads them.

Include the details relevant to your task: a ticket queue, repository, metric sources, environment, owners, or action limits. Use secret-manager references instead of credentials. Verify the selected account before a real mutation. Start with drafts when the required authority or integration is missing.

```text
Use $software-factory for ticket APP-42.
My profile is in the private local folder I supplied.
You may implement, test, and open a draft PR.
Production deployment needs my approval of the final revision.
```

For a task without integrations, provide sanitized files and ask for local artifacts. A draft ticket is useful, but it should be labeled a draft rather than represented as a real queue update.

## Updates and removal

Installed skills are copies of the checkout at install time. To update, inspect the diff, back up the existing installation outside the destination, remove it yourself when ready, and rerun the installer. It never overwrites an existing skill. To uninstall, remove only the copied skill folder you installed. The tool does not change agent settings, accounts, connectors, or shell configuration.

For a reproducible version, check out a reviewed tag or commit before installing. Review third-party skill changes as you would any instructions that can guide an agent's tools.

## Start without a cloud bill

Memory, story drafting, campaign analysis from exported data, experiment design, and website planning can all begin with local files. Actual cloud hosting and paid advertising require provider accounts and can incur charges. Use the web publishing skill to compare current options before provisioning anything.
