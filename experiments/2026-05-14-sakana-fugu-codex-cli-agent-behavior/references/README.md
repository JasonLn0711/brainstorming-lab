# Reference Library

This folder contains downloaded literature and official-method snapshots for the
Fugu Ultra x Codex CLI long-horizon agent behavior packet.

## Contents

| Path | Contents |
| --- | --- |
| `papers/` | Downloaded open-access PDFs, mostly arXiv papers |
| `official-snapshots/` | Downloaded official web snapshots from Sakana, OpenAI, and Anthropic |
| `reference-inventory.yaml` | Bibliographic inventory with local filenames and relevance notes |
| `literature-comparison.md` | Traditional Chinese literature comparison and analysis |

## Scope

The closest research area is not one single paper. It is the intersection of:

- long-horizon native-runtime agent evaluation;
- CLI / coding-agent benchmarks;
- agent memory and context-management research;
- trace, process, and safety evaluation;
- long-running agent harness design;
- multi-agent orchestration and coordinator models.

No downloaded reference exactly studies `fugu-ultra` running inside Codex CLI on
this specific Project II Phase II task. The closest gap is an opaque
OpenAI-compatible multi-agent orchestrator embedded in a CLI coding harness,
evaluated by trace forensics, token efficiency, memory behavior, and official
validation closure.

As of the latest update, the local library includes 17 paper PDFs and 14
official/product snapshots. The added layer covers OpenAI compaction, Anthropic
effective context engineering, Claude Code, Claude Cowork, OpenCode, and
Terminal-Bench, long-horizon reliability science, and terminal-agent benchmark
task-design guidance.
