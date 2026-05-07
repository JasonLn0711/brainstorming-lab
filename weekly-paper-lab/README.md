# Weekly Paper Lab

Weekly Paper Lab is the doctoral-training module inside `brainstorming-lab`.
Its job is not to chase papers. Its job is to turn one paper per week into a
bounded cycle:

```text
read -> decompose -> reproduce lightly -> fail clearly -> define a better question -> seed Idea OS
```

Detailed paper work stays here. If a paper produces a real research direction,
create or update an Idea OS YAML record under `ideas/` and link back to the
paper folder.

## Three Week Cycle

| Slot | Topic | Default domain type |
| --- | --- | --- |
| Week A | AI agent, LLM, or cybersecurity | `ai_agent_llm_cybersecurity` |
| Week B | AI agent, LLM, or cybersecurity | `ai_agent_llm_cybersecurity` |
| Week C | Broad cross-domain paper | `cross_domain` |

Cross-domain papers may come from sociology, biology, medicine, economics,
psychology, human factors, UX, entomology, physics, chemistry, mathematics,
cryptography, mechanical engineering, environmental science, nature, or any
other field that can teach a method or problem frame.

## Sources

Use these as the first-pass discovery layer:

- Hugging Face Trending Papers: daily, weekly, and monthly discussion signals.
- arXiv API: recent preprints and topic-specific queries.
- Papers With Code 2: code, benchmark, and dataset links.
- OpenAlex: broad scholarly metadata, citations, and cross-domain search.

Do not treat popularity as authority. Popularity only earns a paper a triage
slot; the weekly selection still needs a clear learning goal and a feasible
minimum experiment.

## Per Paper Folder

Each selected paper lives at:

```text
weekly-paper-lab/papers/<YYYY-Www>-<slug>/
  paper.yaml
  00_metadata.md
  01_problem.md
  02_method_breakdown.md
  03_key_figures.md
  04_rtx5080_implementation_log.md
  05_bottleneck_and_question.md
  06_research_idea_seed.md
  07_scoring_report.md
  08_scientific_evaluation.md
  scientific_evaluation.yaml
```

`paper.yaml` is the canonical record for status, scoring, links, reproduction
level, artifact path, and planning sync. Markdown files hold the human thinking.

Before reading or implementation starts, selected papers must also contain:

- `idea_connections`: typed links to existing Idea OS records, with a
  recomputed 100-point `paper_connection_rubric_v2` score.
- `synthesis_assessment`: a recomputed `paper_synthesis_rubric_v1` score for
  whether the paper can combine with existing ideas into a future research
  method, evaluation fixture, or reference.

This keeps papers connected to brainstorming ideas instead of becoming isolated
reading notes.

`07_scoring_report.md` is required. It explains why the triage, connection, and
synthesis evidence fields were assigned before the validators recompute the
numbers. The score can be mechanical; the report is the human audit trail.

`scientific_evaluation.yaml` and `08_scientific_evaluation.md` are the
post-reading scientific-quality layer. They do not decide which paper to read.
They evaluate whether the paper itself is scientifically strong after reading:
problem value, literature gap, novelty, method soundness, evidence strength,
results analysis, reproducibility, honesty, and communication.

The scientific-quality score uses `scientific_paper_evaluation_v1`:

- every subitem has a weight, coefficient, score, and evidence note;
- coefficients are limited to `0`, `0.25`, `0.5`, `0.75`, or `1`;
- raw score is recomputed from item weights and coefficients;
- penalties, caps, confidence score, overclaim risk, and reproducibility risk
  are validated separately;
- `not_started` is allowed before a final quality review, but a preliminary or
  final score cannot use `not_evaluated` risk or decision fields.

This keeps "interesting paper" separate from "well-supported scientific paper."
If evidence is missing, record the gap. Do not fill a high score from taste,
authority, popularity, or assumed author competence.

Create a blank machine-checkable score record with:

```bash
python3 scripts/new_paper_quality_evaluation.py weekly-paper-lab/papers/<YYYY-Www-slug>
```

The 100-point connection score has five 20-point dimensions:

| Dimension | Evidence shape |
| --- | --- |
| Topical alignment | overlapping keywords, shared tags, explicit topic match |
| Method/workflow alignment | shared methods, shared workflow stages, same artifact/failure type |
| Next-step impact | whether the paper updates a next step, produces an artifact, reduces named uncertainties |
| Metric/baseline support | shared metrics, baseline, fixture, measurable success condition |
| Research-generation value | named new tests, synthesis paths, YAML update value, citation value |

List fields must contain the actual observed items. The validator scores by
list length and fixed caps, so a bare count is not accepted.

## Doctoral Questions

Every paper should answer:

1. What exact problem are the authors trying to solve?
2. Why is this problem important now?
3. What assumptions make the method work?
4. What is the smallest meaningful RTX 5080 Ubuntu experiment?
5. When the experiment fails or becomes hard, what type of failure is it?
6. Can the bottleneck be redefined as a better research question?

## Auditable Shortlist

Before creating a selected paper folder, write one weekly shortlist:

```text
weekly-paper-lab/shortlists/<YYYY-Www>.yaml
```

The shortlist is canonical for paper selection scoring. It must contain 3 to 5
candidate papers, exactly one `selected: true`, a selection reason for the
winner, and rejected reasons for the others.

A score is valid only if it can be recomputed from observable evidence. Missing
or unknown evidence is `false` and contributes 0.

Previously selected papers or essays are excluded before scoring can matter. The
validator builds a registry from earlier selected `paper.yaml` records and prior
shortlists, then blocks any new candidate with a matching normalized `paper_id`,
title, or identity URL. A revisit should become a follow-up note under the
original paper folder or an Idea OS update, not a new weekly pick.

Run:

```bash
python3 scripts/check_paper_shortlist.py
```

## Triage Rubric

Score candidate papers out of 100:

- recency and discussion signal
- connection to current Idea OS records
- RTX 5080 feasibility
- code, dataset, or benchmark availability
- research-question potential
- novelty or cross-domain transfer value, for the weekly pick score

The candidate score is the sum of the five 20-point base dimensions. The weekly
pick score is recomputed with this weighting:

```text
5 * (
  0.25 * research_question_potential
+ 0.20 * rtx5080_feasibility
+ 0.20 * idea_os_connection
+ 0.15 * code_data_benchmark
+ 0.10 * recency_discussion
+ 0.10 * novelty_or_transfer
)
```

For `cross_domain` weeks, `cross_domain_transfer` replaces
`novelty_or_transfer`.

## Reproduction Levels

| Level | Meaning |
| ---: | --- |
| 1 | Read and reconstruct the concept |
| 2 | Run the official demo |
| 3 | Rerun with small parameter changes |
| 4 | Replace data or model |
| 5 | Produce a variant method |

The default target is Level 2 or 3 when official code exists. If a paper is too
large, use Level 1 and write the bottleneck clearly.

## RTX 5080 Boundary

Large models, datasets, caches, checkpoints, and run artifacts stay outside git:

```text
/home/jnln3799/research-artifacts/weekly-paper-lab/
```

This repo records commands, versions, metrics, failures, and interpretation.
It does not store large raw artifacts, credentials, sensitive evidence, or
production outputs.

## Planning And Idea OS Links

Planning sync must stay short:

```text
title, paper_id, status, next test, canonical path, linked idea IDs, capacity note
```

Weekly Paper Lab is a weekly schedule item, so it must also update
`planning-everything-track` when a paper is selected, run, parked, killed, or
turned into an Idea OS update. Planning should receive:

- today's day-note status line;
- this week's scheduled reading / minimum-run block;
- next test and capacity note;
- canonical path back to this paper folder;
- linked Idea OS IDs;
- no detailed scoring tables, source notes, run artifacts, or raw experiment data.

If the paper generates a research idea, update Idea OS through `ideas/*.yaml`.
Use `source`, `evidence`, `connections`, and `next_steps` to link back here.

Run the structural check with:

```bash
python3 scripts/check_paper_lab.py
python3 scripts/check_paper_quality.py
```
