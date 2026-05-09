# Codex-Wrapped AI Scientist Research OS

Date: 2026-05-09

Canonical Idea OS record:

```text
ideas/structured/idea_000019_codex_wrapped_ai_scientist_research_os.yaml
```

Execution repo:

```text
../auto-research-os
```

## First Principle

The scarce resource is not another autonomous research step.

The scarce resource is trustworthy research-cycle evidence:

- what was run
- what changed
- what failed
- what supports each claim
- where citations came from
- whether another researcher could reproduce the result
- where the system must stop for human judgment

Because v0.1 explicitly removes four hard controls, the design cannot pretend to
be protected by isolation:

- no Docker container for every run
- no hard block on launcher-script edits
- no network restriction
- no GPU / CPU / disk quota

So the v0.1 protection model is different:

```text
Do not rely on isolation to protect the system.
Use traceability, recovery, review, and human gates to protect research quality.
```

This is a research-quality control plane, not an unattended paper factory.

## Design Decision

Keep Sakana AI Scientist-v2 mostly as an upstream research engine.

Put the custom control layer around it:

```text
Sakana AI Scientist-v2 core
+ Codex CLI orchestration
+ git-based run tracking
+ run manifests
+ experiment logging
+ reproducibility reports
+ claim boundary review
+ citation traceability review
+ safety / public-action gates
+ weekly report synthesis
```

Codex CLI acts as the conductor:

- check repo state
- create a timestamped run directory
- invoke preflight
- inspect upstream scripts before running them
- run a dry-run or small experiment first
- capture logs and diffs
- write governance reports
- stop before external publication, upload, email, or submission

AI Scientist remains the research engine. Codex does not replace the core
research logic in v0.1.

## v0.1 Acceptance Rule

A run is acceptable only if it produces a reviewable bundle:

```text
research_runs/<run_id>/
├── run_manifest.json
├── preflight.log
├── command_candidate.md
├── experiment_summary.md
├── novelty_assessment.md
├── reproducibility_report.md
├── claim_boundary_review.md
├── next_step_recommendation.md
├── git_diff_summary.md
├── git_diff.patch
└── git_status_after.txt
```

The run does not need to produce a paper, benchmark result, or novelty claim in
v0.1.

The run must make failure inspectable.

## Implemented Local State

Created sibling repo:

```text
../auto-research-os
```

Committed there:

```text
26ec2be Initialize soft-control auto research OS
a8047c2 Fix Codex exec runner invocation
f8c13a5 Use configurable Codex sandbox mode
795f44d Finalize failed dry-run artifacts
```

Implemented:

- `README.md`
- `AGENTS.md`
- `Makefile`
- `upstream/README.md`
- `research_topics/ai_agent_cybersecurity.md`
- `prompts/00_codex_orchestrator.md`
- `prompts/10_idea_reviewer.md`
- `prompts/20_experiment_reviewer.md`
- `prompts/30_claim_boundary_reviewer.md`
- `prompts/40_weekly_report_writer.md`
- `governance/claim_boundary_checklist.md`
- `governance/citation_checklist.md`
- `governance/reproducibility_checklist.md`
- `governance/reviewer_scorecard_100.md`
- `scripts/setup_env.sh`
- `scripts/preflight.sh`
- `scripts/make_run_manifest.py`
- `scripts/run_ideation.sh`
- `scripts/run_scientist_cycle.sh`
- `scripts/run_codex_review.sh`
- `scripts/weekly_auto_research.sh`
- `scripts/run_weekly_report.sh`
- `scripts/finalize_run_artifacts.py`

## Validation Evidence

Local validation passed:

```bash
make preflight
make smoke
```

Latest validated smoke run:

```text
../auto-research-os/research_runs/20260509_070115_auto_research/
```

The local smoke run proved:

- run directory creation works
- manifest generation works
- preflight logging works
- topic copy works
- required report placeholders are created
- failed or incomplete runs can still be finalized into reviewable artifacts

## Dry-Run Findings

The Codex dry-run inspected AI Scientist-v2 entrypoints and captured blockers
before any full experiment was accepted.

Latest dry-run:

```text
../auto-research-os/research_runs/20260509_065539_auto_research/
```

Findings:

- `python` is not available as a bare command in the local environment; use
  `python3` or the project venv.
- AI Scientist-v2 ideation import currently needs `tiktoken`.
- AI Scientist-v2 BFTS launcher import currently needs `torch`.
- Codex CLI `workspace-write` sandbox failed on this Ubuntu host with a `bwrap`
  network namespace error, so the runner currently defaults to documented
  `CODEX_SANDBOX_MODE=danger-full-access` while preserving the stricter retry
  path.

These are environment-readiness results, not scientific results.

## Claim Boundary

Allowed local claim:

> The wrapper scaffold can create traceable local run directories and preserve
> failure-aware review artifacts.

Not allowed:

- The research topic is novel.
- AI Scientist-v2 produced a validated result.
- The system is safe for unattended public release.
- The system can generate paper-ready claims.
- The dependency setup is complete.

## Next Step Series

### Step 1: Environment Setup

Run in `../auto-research-os`:

```bash
./scripts/setup_env.sh
```

Acceptance:

- `.venv` exists
- upstream requirements install or fail with a recorded blocker
- `python` inside the venv can import the required ideation dependencies

### Step 2: Reconfirm Smoke

Run:

```bash
make smoke
```

Acceptance:

- a new `research_runs/<run_id>/` appears
- all required reports exist
- `run_manifest.json` records root and upstream commits

### Step 3: Reviewed Codex Dry-Run

Run:

```bash
make run
```

Acceptance:

- Codex reads the topic
- Codex inspects local upstream README and scripts
- `command_candidate.md` exists
- no public action occurs
- all required review reports exist

### Step 4: Human Gate Before Real Ideation

Before running real AI Scientist-v2 ideation, review:

- `command_candidate.md`
- `reproducibility_report.md`
- `claim_boundary_review.md`
- `next_step_recommendation.md`
- dependency and cost readiness

Only then run a bounded ideation command.

### Step 5: First Real Small Experiment

Run only a low-cost, short, public-safe experiment.

Acceptance:

- command recorded
- config recorded
- seed recorded if available
- output path recorded
- failed attempts preserved
- no paper claim promoted

### Step 6: Weekly Report

After one or more accepted runs:

```bash
./scripts/run_weekly_report.sh
```

Acceptance:

- `reports/weekly/*.md` exists
- the report identifies kill / revise / promote recommendations
- no result becomes paper-ready without human review

### Step 7: Cron Only After Manual Stability

Do not add cron until at least one reviewed Codex dry-run and one small
experiment produce acceptable artifacts.

Cron is an automation step, not a correctness proof.
