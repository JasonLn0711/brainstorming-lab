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
   - If it needs depth, create or continue the canonical Idea OS YAML record;
     use `ideas/<date-slug>.md` only as a companion reasoning/source note.

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

## Document Voice Rules

- Write repo documents in an affirmative, confident, and generous voice.
- Frame constraints as clear ownership, scope, evidence, and next-action guidance.
- Prefer positive formulations such as "this repo owns", "use this path", "the next test is", and "the boundary is".
- When a limit matters, state the constructive reason and the working alternative.
- Replace hesitation-driven caveats with evidence-backed boundaries, decision criteria, and explicit review triggers.
- Keep critique direct and useful: name the assumption, pressure-test it, and identify the smallest test that would clarify it.

## Legacy Markdown Notes

The repo now treats YAML Idea OS records as canonical, but this checkout also
contains pre-Idea-OS Markdown brainstorms at `ideas/*.md`.

Use those Markdown files as preserved reasoning sources. When changing status,
maturity score, tags, next tests, or connections, update or create the relevant
YAML record first, then keep the Markdown as explanation, history, critique, or
graduation rationale.

Current important legacy Markdown notes:
- `ideas/ai-aware-grid-decision-twin-power-grid-brainstorm.md`
- `ideas/ant-colony-pheromone-graph-search-social-simulation.md`
- `ideas/classical-chinese-jailbreak-cross-lingual-safety-blind-spot.md`
- `ideas/japan-local-systems-as-legacy-distributed-infrastructure-brainstorm.md`
- `ideas/taiwan-academic-research-team-scale-structure-incentives.md`
- `ideas/transformers-inherently-succinct-theory-backbone-ai-safety.md`
- `ideas/youtube-download-terminal-yt-dlp-ubuntu.md`

## Idea OS Rules

- Treat ideas as data: normalize, score, link, cluster, and review them through the YAML schema.
- Use the 100-point `maturity_score`; the retired compact score is not a decision input.
- Use `scripts/normalize_problem.py` and `scripts/score_maturity.py` before weekly review or research-candidate generation.
- Use `scripts/weekly_review.py` as the adaptive weekly decision engine; it mixes exploitation, novelty exploration, and controlled randomness.
- Use `scripts/link_ideas.py` for bidirectional links instead of editing only one file.
- Before promoting a tool-shaped idea, capture at least one friction source: implementation, experiment, operation, field observation, lecture-time mental execution, or paper-to-workflow simulation.
- Separate problem, symptom, tool, metric, and constraint before raising maturity for technique excitement.
- Before raising an idea to `research_candidate` or `execution_ready`, add a real-world pressure test.
  - A pressure test names the concrete messy setting where the idea may fail: crowding, occlusion, latency, deployment hardware, weak labels, human review burden, privacy boundary, cost, weather, noise, distribution shift, near-duplicate cases, or operational accountability.
  - It should convert the abstract idea into a field-like scenario, such as "find my bicycle in a dense NTU bike lot" rather than only "run object detection."
  - It must include the expected failure mode, the smallest observable test, and the metric or human decision that would confirm, revise, or kill the idea.
  - Use `docs/real-world-pressure-tests.md` for playful but bounded experiment patterns.
  - Keep detailed reasoning in the idea YAML or companion Markdown; put only reusable pressure-test rules here.
- The smallest next test should confirm, revise, or kill a bottleneck hypothesis, not only try a tool.
- Planning sync must remain short: title, ID, status, maturity score, next test, canonical path, and capacity note only.
- Feedback from planning must come from explicit Idea OS marker blocks; do not infer feedback from free-form daily-note prose.

## Weekly Paper Lab Rules

Before selecting, scoring, recording or reviewing a weekly paper, read the
[weekly paper-lab contract](docs/weekly-paper-lab-agent-contract.md). Preserve
objective evidence-backed scores, separate selection from scientific quality,
keep `paper.yaml` canonical and keep Planning mirrors thin. Run its declared
validators when paper records change; a general idea capture does not load the
paper-selection workflow.

## Paper Writing Rules

- Use `docs/paper-writing-engineering-process.md` for reusable manuscript drafting and revision.
- A paper must protect one main problem, one main method, one main evidence stack, and one contribution statement.
- Before drafting, write the one-sentence claim, reviewer question list, contribution-to-evidence map, Figure 1 overview, and main-text vs appendix split.
- Abstracts must follow problem, gap, method, result, and contribution-plus-boundary order.
- Introductions should use the six-part structure: problem, gap, core distinction, method, evidence, contribution.
- Every contribution must start with a strong verb, name a concrete scientific object, and map to a method section plus evidence artifact.
- Method sections must define input, output, assumptions, definitions, procedure or algorithm, failure conditions, and reproducibility path.
- Every result table must include a take-away sentence that states what claim the table supports.
- Claim boundaries must be explicit, while detailed ledgers, role tables, and scope-boundary lists belong in the appendix when the main text already carries the method.

## Safety Note

For security or AI-safety brainstorms, keep notes protective, research-oriented,
and focused on responsible evaluation.

Prefer:
- threat models
- benchmark design
- governance implications
- safe explanations
- non-operational placeholders

Avoid:
- optimized attack prompts
- step-by-step harmful instructions
- credential, exploit, or evasion details

## Good Output

Good work in this repo produces one of:
- clearer next action
- killed idea with a reason
- parked idea with a review trigger
- project-graduation packet
- distilled lesson for the planning knowledge tree
