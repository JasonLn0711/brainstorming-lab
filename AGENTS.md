# AGENTS.md

This repo is the detailed brainstorming workspace beside `planning-everything-track`.

## Mission

Help ideas become clearer without turning the planning repo into a warehouse.

This repo owns:
- raw idea development
- critical thinking
- assumption tests
- option comparison
- critique and objections
- project-graduation packets

This repo does not own:
- daily planning
- weekly capacity
- final project execution
- credentials
- sensitive raw evidence
- full project implementation once the project becomes real

## Relationship To Planning

`planning-everything-track` is the brain-centric control plane.

It owns:
- priority
- capacity
- commitments
- daily and weekly status
- durable lesson promotion
- links to this repo and to project repos

This repo owns the detailed thinking.

When updating both repos:
- keep planning notes short
- link from planning to the canonical idea file here
- do not duplicate full brainstorms into planning
- update planning only when priority, capacity, project status, or durable knowledge changes

## Lifecycle Rules

1. Capture sparks lightly.
   - If the idea is tiny, a day-note line in planning is enough.
   - If it needs depth, create an `ideas/<date-slug>.md` file here.

2. Develop ideas with bounded sessions.
   - Name the question.
   - Write raw thoughts.
   - Test assumptions.
   - Compare options.
   - Decide the smallest next test.

3. Park or kill ideas honestly.
   - Not every idea deserves a project.
   - Preserve the reason so future agents do not reopen the same loop blindly.

4. Graduate only when real.
   - Create a packet in `projects-ready/`.
   - Name the standalone project repo.
   - Move execution material into that new repo.
   - Keep only locator/status notes in planning.

5. Promote durable lessons sparingly.
   - Reusable lessons go back to `planning-everything-track/data/knowledge/`.
   - Link back to the idea file or graduation packet.

## Durable Rule Rules

Use FIRST PRINCIPLE before adding rules here.

This repo may own rules about:
- how to develop an idea;
- how to test assumptions;
- how to compare options;
- when to park, kill, or graduate an idea;
- what a graduation packet must contain.

This repo must not own rules about:
- weekly capacity;
- daily must-win priority;
- project execution details after a standalone repo exists;
- credentials, private evidence, or production operations.

If a brainstorm produces a durable rule:
- keep the detailed reasoning in the idea file;
- add only the reusable rule to `AGENTS.md`, README, or `docs/`;
- update planning only with the rule's capacity/status impact;
- move execution-specific rules into the execution repo when the idea graduates.

Do not add a rule just because an idea is exciting. Add a rule when it prevents repeated confusion.

## File Rules

- Prefer Markdown and CSV.
- Idea records are now canonical YAML files under `ideas/raw/`, `ideas/evolving/`, `ideas/structured/`, `ideas/executing/`, or `ideas/archived/`.
- Markdown may explain history or reasoning, but future agents should update YAML first when changing idea status, maturity score, tags, next steps, or connections.
- Generated graph, clustering, research, and index files should be rebuilt with CLI scripts rather than edited by hand.
- Keep files readable in plain text.
- Use dates in filenames when chronology matters.
- Avoid vague names like `notes.md` unless the parent folder provides enough context.
- Keep sensitive material out unless a local-only policy is explicitly documented.

## Idea OS Rules

- Treat ideas as data: normalize, score, link, cluster, and review them through the YAML schema.
- Use the 100-point `maturity_score`; the retired compact score is not a decision input.
- Use `scripts/normalize_problem.py` and `scripts/score_maturity.py` before weekly review or research-candidate generation.
- Use `scripts/weekly_review.py` as the adaptive weekly decision engine; it mixes exploitation, novelty exploration, and controlled randomness.
- Use `scripts/link_ideas.py` for bidirectional links instead of editing only one file.
- Before promoting a tool-shaped idea, capture at least one friction source: implementation, experiment, operation, field observation, lecture-time mental execution, or paper-to-workflow simulation.
- Separate problem, symptom, tool, metric, and constraint before raising maturity for technique excitement.
- The smallest next test should confirm, revise, or kill a bottleneck hypothesis, not only try a tool.
- Planning sync must remain short: title, ID, status, maturity score, next test, canonical path, and capacity note only.
- Feedback from planning must come from explicit Idea OS marker blocks; do not infer feedback from free-form daily-note prose.

## Good Output

Good work in this repo produces one of:
- clearer next action
- killed idea with a reason
- parked idea with a review trigger
- project-graduation packet
- distilled lesson for the planning knowledge tree
