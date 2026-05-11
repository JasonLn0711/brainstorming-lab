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

- Treat `weekly-paper-lab/` as the doctoral-training input layer for Idea OS.
- Use `weekly-paper-lab/shortlists/<YYYY-Www>.yaml` to record 3 to 5 candidate papers before creating the selected paper folder.
- Shortlist scoring must be evidence-driven: raw observable evidence, fixed rubric rules, recomputed score.
- A score is invalid unless every subscore is backed by observable evidence; missing or unknown evidence counts as false and contributes 0.
- Previously selected papers or essays are excluded from new shortlists by normalized `paper_id`, title, or identity URL. Revisit work belongs in the original paper folder or an Idea OS update, not as a new weekly pick.
- Each selected paper gets one folder under `weekly-paper-lab/papers/<YYYY-Www>-<slug>/`.
- `paper.yaml` is canonical for paper status, triage score, reproduction level, artifact path, links, and planning sync.
- Selected papers must include `idea_connections` with objective 100-point `paper_connection_rubric_v2` scores before reading or implementation starts.
- `paper_connection_rubric_v2` evidence list fields must contain the actual observed items; do not replace them with bare counts.
- Selected papers must include `synthesis_assessment` with objective `paper_synthesis_rubric_v1` scores to decide whether the paper can combine with existing ideas into a future research method or reference.
- Keep the Markdown files as the human lab notebook: metadata, problem, method, figures, RTX 5080 log, bottlenecks, research seed, selection/connection scoring report, and scientific evaluation report.
- Every selected paper must include `07_scoring_report.md` explaining why the shortlist, connection, and synthesis scores were assigned; unknown evidence must be named instead of guessed.
- Every selected paper must include `scientific_evaluation.yaml` and `08_scientific_evaluation.md` for post-reading paper quality evaluation under `scientific_paper_evaluation_v1`.
- Scientific quality scoring is separate from shortlist triage: triage decides whether to read the paper; scientific evaluation decides whether the paper's problem, method, evidence, claims, limits, and reproducibility are strong.
- Scientific evaluation coefficients are limited to `0`, `0.25`, `0.5`, `0.75`, or `1`; every subscore must have an evidence note, and validator-recomputed penalties/caps/confidence/risk fields must match the YAML.
- Use the three-week cycle: `main_a`, `main_b`, then `cross_domain`.
- Use `scripts/check_paper_shortlist.py` before selecting the weekly paper and `scripts/check_paper_lab.py` plus `scripts/check_paper_quality.py` before weekly review or planning sync when paper folders changed.
- Weekly Paper Lab must stay coupled to `planning-everything-track`: update the current day note when a paper is selected or run, update the weekly plan with the scheduled reading/run block and next test, and keep planning notes short.
- Keep large models, datasets, checkpoints, caches, credentials, sensitive evidence, and generated run artifacts out of git.
- If a paper produces a real research question, create or update an Idea OS YAML record and link back to the paper folder.
- Planning receives only title, paper ID, status, next test, canonical path, linked idea IDs, and capacity note.

## Paper Writing Rules

- Use `docs/paper-writing-engineering-process.md` for reusable manuscript drafting and revision.
- A paper must protect one main problem, one main method, one main evidence stack, and one contribution statement.
- Before drafting, write the one-sentence claim, reviewer question list, contribution-to-evidence map, Figure 1 overview, and main-text vs appendix split.
- Abstracts must follow problem, gap, method, result, and contribution-plus-boundary order.
- Introductions should use the six-part structure: problem, gap, core distinction, method, evidence, contribution.
- Every contribution must start with a strong verb, name a concrete scientific object, and map to a method section plus evidence artifact.
- Method sections must define input, output, assumptions, definitions, procedure or algorithm, failure conditions, and reproducibility path.
- Every result table must include a take-away sentence that states what claim the table supports.
- Claim boundaries must be explicit, but detailed ledgers, role tables, and defensive exclusion lists should move to appendix unless needed to understand the method.

## Safety Note

For security or AI-safety brainstorms, keep notes defensive and research-oriented.

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
