# Future Research Directions: Long-Horizon Stateful Agent Reliability

Date: 2026-05-14

## First Principle

The scarce resource is not more model output or more candidate tasks. The scarce
resource is **trustworthy long-horizon state**:

- What has been verified?
- What has failed?
- What should not be repeated?
- What proof boundary controls success claims?
- What external artifact lets the next human or agent continue without starting
  from zero?

Therefore the research object is no longer only:

```text
Can an agent solve this exploit / coding task?
```

It is:

```text
Can a long-running AI agent maintain stable, verified task state in a real
CLI/repo/Docker/security workflow under token, tool-output, and proof-boundary
pressure?
```

## Best Current Research Umbrella

Recommended umbrella:

```text
Long-Horizon Stateful Agent Reliability
```

More specific version:

```text
Long-Horizon Stateful AI Agents for Real-World Cybersecurity and Software
Engineering Tasks
```

This umbrella fits the actual evidence:

- real Codex CLI traces;
- real repo and Docker state;
- real tool-output pressure;
- real token amplification;
- real drift and repeated exploration;
- real proof-boundary constraints;
- real handoff and negative-evidence artifacts.

## Twelve Research Directions

### 1. Long-Horizon Agent Reliability

Study how agents degrade across long tasks.

Observed failure modes:

- reasoning collapse;
- exploratory explosion;
- state fragmentation;
- tool-output entropy;
- recursive re-discovery;
- task-frame regression.

Candidate question:

> At what task length, tool-call count, or no-new-evidence streak does an agent
> begin to lose objective alignment?

### 2. Agent Memory Systems

Treat memory as a write-manage-read system, not as a longer context window.

Subdirections:

- hierarchical memory: hot / warm / cold / archive;
- verified memory: only command/file/test-backed facts become durable;
- failed-hypothesis memory: preserve dead ends so future agents do not retry;
- compaction policy: decide what to summarize, externalize, or forget.

Candidate question:

> Does a failed-hypothesis ledger reduce duplicate commands and token cost in
> Codex-style long tasks?

### 3. Context Engineering

Study externalized context artifacts as a replacement for raw conversation
history.

Existing artifact pattern:

```text
HANDOFF_PHASE2.md
PHASE2_PROGRESS.md
FAILED_HYPOTHESES.md
EVIDENCE_INDEX.md
VALIDATION_LOG.md
```

Candidate question:

> Which handoff schema best preserves verified facts while preventing speculative
> claims from becoming future-agent facts?

### 4. Agent Drift Detection

Detect when an agent begins to leave the task frame.

Candidate metrics:

- tool-call entropy;
- duplicate command rate;
- repeated repo-inspection regression;
- no-new-evidence streak;
- objective-distance score;
- hallucinated progress count.

Candidate question:

> Can drift be detected before the agent spends another million tokens?

### 5. Agent Evaluation and Native-Runtime Benchmarking

Convert the current packet into a repeatable benchmark protocol.

Required benchmark properties:

- real CLI;
- real repo;
- real file side effects;
- Docker / runtime state;
- official success oracle;
- trace-level scoring;
- false-completion detection.

Candidate question:

> How different are model rankings when evaluated by official side effects,
> trace quality, and artifact handoff rather than final answer only?

### 6. AI Cybersecurity Agents

Keep this line defensive and evaluation-oriented.

Useful cybersecurity-agent capabilities:

- proof-boundary discipline;
- negative evidence preservation;
- coredump / debugger evidence summarization;
- official verifier alignment;
- invalid bypass detection.

Candidate question:

> How often do cybersecurity agents confuse crash, sanity check, bypass, and
> official success proof?

### 7. AI Orchestration Systems

Fugu is especially relevant because it is an opaque multi-agent orchestration
endpoint, not just a single model.

Subdirections:

- subagent routing;
- recursive self-call control;
- token budget allocation;
- collaboration topology;
- branch-level failed-hypothesis cache;
- orchestration observability.

Candidate question:

> Does learned orchestration improve exploration at the cost of trace
> observability and convergence stability?

### 8. AI Software Engineering OS

Study the repo as an operating system for long-running agents.

Key primitives:

- handoff;
- audit;
- traceability;
- progress file;
- validation log;
- git checkpoint;
- runbook;
- proof oracle.

Candidate question:

> Which repo-local artifacts make a coding agent continuation reliable after
> context compaction or model handoff?

### 9. AI Scientific Research Agents

The same state problem appears in AI scientist systems.

Core needs:

- hypothesis tracking;
- negative result preservation;
- reproducible evidence;
- claim boundary;
- handoff across sessions;
- research-state compression.

Candidate question:

> Can a progress-ledger protocol improve AI scientist continuity across failed
> experiments?

### 10. Failure Science

Most agent papers emphasize success. This packet is strongest as failure
forensics.

Possible taxonomy:

| Failure type | Definition |
| --- | --- |
| Token amplification | Cost grows faster than verified evidence |
| State fragmentation | Important facts are present but not used |
| Recursive rediscovery | Agent repeats already-known investigation |
| Proof-boundary drift | Agent blurs sanity checks and official proof |
| Self-report drift | Plan status says progress that evidence does not support |
| Tool-output entropy | Raw logs bury decision-relevant facts |

Candidate question:

> Which failure type predicts final non-completion earliest?

### 11. Human-AI Co-Reasoning

The user is acting as a supervisor, not a passive requester.

Research levers:

- human checkpoint insertion;
- uncertainty escalation;
- human override design;
- trust calibration;
- bounded intervention timing.

Candidate question:

> When should a human inject a checkpoint to prevent drift without destroying
> useful agent autonomy?

### 12. Agent Operating Procedures

Agents need SOPs, not only models.

Relevant SOP elements:

- phase gate;
- allowed proof definitions;
- invalid proof list;
- tool-output handling rule;
- command budget;
- evidence file policy;
- handoff requirement;
- closeout honesty rule.

Candidate question:

> Do explicit agent SOPs reduce false completion and duplicate exploration in
> long CLI tasks?

## Prioritized Research Attempts

### Attempt A: Failure Taxonomy Paper

Working title:

```text
A Failure Taxonomy for Long-Horizon CLI Agents
```

Minimum contribution:

- classify the Fugu/GPT-5.5 traces;
- define failure labels;
- define observable metrics;
- show why final-answer scoring misses the failure.

### Attempt B: External Memory Protocol

Working title:

```text
Verified External Memory for Long-Horizon CLI Agents
```

Minimum contribution:

- design `STATE.md`, `FAILED_HYPOTHESES.md`, `EVIDENCE_INDEX.md`;
- compare no-memory vs memory-artifact runs;
- measure token cost, duplicate commands, handoff quality, and drift point.

### Attempt C: Drift / Meltdown Detector

Working title:

```text
Early Drift Detection for Tool-Using CLI Agents
```

Minimum contribution:

- parse traces into tool-call sequences;
- compute duplicate command rate, no-new-evidence streak, and objective-distance;
- flag the point where the agent regresses to generic repo inspection.

### Attempt D: Model + Harness Comparative Study

Working title:

```text
Model or Harness? A Controlled Study of Long-Horizon Codex CLI Agents
```

Minimum contribution:

- run Fugu Ultra, GPT-5.5, and optionally Claude/OpenCode style agents under
  matched prompts;
- compare clean-start, handoff-start, and handoff-only tasks;
- separate direct solving from state compression.

### Attempt E: Stateful Cybersecurity Agent Evaluation

Working title:

```text
Proof-Boundary Evaluation for Stateful Cybersecurity Agents
```

Minimum contribution:

- define success, invalid proof, sanity check, and partial progress;
- score agents on proof-boundary discipline;
- show how security tasks differ from ordinary coding benchmarks.

## Recommended Next Action

Create a reusable protocol file:

```text
agent_behavior_eval_protocol.md
```

It should contain:

1. task definition and official success oracle;
2. allowed and forbidden proof types;
3. required external memory artifacts;
4. drift / loop / token metrics;
5. model comparison matrix;
6. scoring rubric;
7. minimal repeatable experimental workflow.

## One-Sentence Research Position

> This research does not evaluate whether an agent can solve one task once; it
> evaluates whether a long-running agent can maintain verified state, preserve
> negative evidence, respect proof boundaries, and converge under real CLI
> tool-output pressure.
