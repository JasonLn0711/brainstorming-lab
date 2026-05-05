# Project Graduation: Statement Interview Question MVP

Date: 2026-05-05
Source idea: idea_000011
Target repo: `/Users/iKev/Desktop/02_Projects_and_Code/everything_on_git/statement-interview-question-mvp`
State: executing

## Why This Is Real Now

The system has moved from architecture discussion to a runnable MVP-0 repo. The first executable boundary is intentionally small: transcript input, Extract Node, Question Node, SQLite audit, and FastAPI/CLI entrypoints.

## First Output

MVP-0 returns three neutral next-question suggestions from a toy investment-scam transcript, writes Extract/Question audit rows, and now uses file-backed prompt package `interview-assist-v0.1`.

## User / Audience / Owner

Primary user: officer or legal-review workflow designer testing an interview-assist prototype.

Owner: local execution repo. `brainstorming-lab` keeps only the idea, rationale, and locator.

## Scope

In:
- LangGraph two-node workflow.
- GPT-OSS 20B via Ollama integration point.
- SQLite audit log.
- Mock mode for no-model verification.
- FastAPI and CLI entrypoints.
- File-backed prompt package, schemas, local Markdown knowledge, and sample-case runner.

Out:
- Real victim data.
- Autonomous investigation.
- Classify/Missing/Safety/RAG until MVP-0 is stable.
- Kafka, streaming ASR, frontend, multi-model routing.

## Evidence

- Repo created: `/Users/iKev/Desktop/02_Projects_and_Code/everything_on_git/statement-interview-question-mvp`
- `.venv` dependency install succeeded with LangGraph and FastAPI.
- `pytest` passed: 2 tests.
- After prompt-package pass, `pytest` passed: 5 tests.
- Mock CLI demo returned three next questions.
- Mock sample-case runner returned three next questions and audit rows with prompt/version/runtime/hash metadata.
- FastAPI `/health` and `/recommend` with `mock=true` returned OK.
- `ollama` CLI is not installed, so real gpt-oss:20b runtime is still blocked.

## First Repo Structure

```text
statement-interview-question-mvp/
  README.md
  AGENTS.md
  pyproject.toml
  src/statement_interview_mvp/
  tests/
  scripts/
  data/
```

## Planning Bridge Update

- Project locator: `statement-interview-question-mvp`
- Next action: install Ollama, pull `gpt-oss:20b`, run the CLI without `--mock`.
- Capacity impact: small engineering spike; do not expand to full legal/RAG workflow until real model output is observed.
- Review date: 2026-05-06

## Move Checklist

- [x] Create standalone repo
- [x] Move execution docs/materials there
- [x] Add repo README and AGENTS
- [ ] Update planning locator/status
- [ ] Promote only reusable lessons to knowledge
