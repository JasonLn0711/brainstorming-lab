# OpenClaw Personal Ops Node

Date: 2026-05-04
State: active idea / parked from W19 execution
Planning bridge: `/Users/iKev/Desktop/02_Projects_and_Code/everything_on_git/planning-everything-track/weeks/2026-W19/days/2026-05-04.md`
Execution / research repo: `/Users/iKev/Desktop/02_Projects_and_Code/everything_on_git/second-brain-openclaw`

## One-Line Idea

Use a low-power always-on node, such as a Raspberry Pi or mini PC, as a safe personal operations host for OpenClaw / Codex-heavy workflows: remote entrypoint, task watcher, approval relay, logs, redaction, rollback, and notification.

## Why It Might Matter

The useful part is not that Raspberry Pi is interesting hardware. The reusable pattern is:

```text
low-power always-on node
  -> private network entry
  -> strong cloud model or Codex session
  -> deterministic scripts / browser / files / APIs
  -> action log
  -> human approval
  -> git / backup rollback
```

This connects to Mailman, Slack/Codex routing, Gmail triage, planning control-plane work, and future research/CIB workflows because those lanes need provenance, reviewability, and recoverability more than they need a flashy autonomous assistant.

## Source Spark

- OpenClaw Chinese-community discussion about keeping OpenClaw alive on Raspberry Pi 5 through Tailscale while operating the node remotely.
- Community details included Raspberry Pi 5 / Pi 4 use, headless operation, GitHub backups, remote control, Telegram-style entrypoints, and cloud-model-backed execution.
- Planning capture originally lived in the 2026-05-04 day note; this file is now the canonical brainstorm home.

## Core Insight

The target is not "many autonomous agents." The target is a verifiable operations loop:

```text
input channel
  -> redaction
  -> task router
  -> tool execution
  -> action log
  -> approval gate
  -> notification
  -> rollback / recovery
```

OpenClaw should provide the long-running channel/router/watcher layer only where it adds system value. Codex should remain the main coding and workspace execution engine when the task is code-heavy.

## Architecture Options

| Option | When it fits | Risk | Next test |
| --- | --- | --- | --- |
| Direct `Telegram -> Codex` | Single prompt, short action, no long-lived state | Loses retry/checkpoint/audit value | Use for one-shot questions only |
| OpenClaw as workflow layer | Needs state, retry, scheduling, approvals, notifications, or external side effects | Can become over-engineered | Write one-page minimal design before implementation |
| OpenClaw supervising Codex CLI | Codex-heavy repo work needs mobile/remote status and approval relay | Fragile if it tries to replace Codex's native harness | Test with `SSH + tmux + Codex CLI` first |
| Custom web UI | Demo, multi-user operation, or repeated workflows that terminal/chat cannot manage | Auth/session/streaming/approval/logging complexity | Defer until terminal/chat loop proves repeated value |

## OpenClaw And Codex Connection Model

Three separate paths should not be confused:

| Path | Shape | Meaning |
| --- | --- | --- |
| CLI backend / fallback | `Telegram / LINE -> OpenClaw Gateway -> OpenClaw Agent -> codex-cli/<model>` | OpenClaw routes to a CLI backend for bounded tasks |
| Remote supervisor | `Telegram -> OpenClaw -> tmux/hook -> Codex CLI -> repo/shell/MCP/apply_patch` | OpenClaw watches or drives an existing Codex-heavy workflow |
| MCP bridge opposite direction | `Codex / MCP client -> openclaw mcp serve -> OpenClaw Gateway conversations` | Codex reads or replies through OpenClaw-known channels |

Recommended first version: remote supervisor, not hard fusion.

## Hardware Notes

- Main reference setup: Raspberry Pi 5, 8GB RAM, Ubuntu, headless/server-only.
- Other possible setups: Raspberry Pi 4B with 4GB/8GB RAM plus SSD, or a mini PC with 16GB RAM and SSD.
- Hardware requirement is not local GPU. It is stable 24/7 uptime, enough RAM for orchestration, reliable storage, and private-network reachability.
- Browser automation, forms, and scraping can run on CPU.
- LLM reasoning should be offloaded to cloud models for long, tool-heavy, or audit-sensitive work.

## Taiwan Hardware-Cost Spot Check

Checked on 2026-05-04:

- Raspberry Pi 5 8GB board showed a wide local-channel range: about NT$4,500-8,800 depending on channel, stock, tax, and procurement route.
- Raspberry Pi 4B 8GB was not clearly cheaper enough to justify buying new if a cheaper Pi 5 or mini PC is available.
- Raspberry Pi 5 official 512GB SSD kit looked closer to NT$4,500-5,000 before adding case, power, cooling, or UPS-style accessories.
- Stable Pi 5 plus official SSD path should be budgeted around NT$11,000-15,000.
- Mini PC with 16GB RAM and SSD should be compared before buying a fresh Pi stack.

Purchase rule: reuse existing Pi hardware first. If buying new for Codex/research workflows, compare against a mini PC before buying a Pi.

## Model Routing

Do not judge small/local models only by parameter count. Judge them by end-to-end workflow reliability under agent load.

| Model class | Suitable role |
| --- | --- |
| `0-7B` | narrow classification, extraction, simple generation, embeddings |
| `7-13B` | chat and simple snippets; not stable enough for agent ownership |
| `13-30B` | one- or two-step guarded tasks |
| `30-70B` | short workflows and basic tool use, still risky for long context and recovery |
| `70B+` | serious local decision ability begins, but cost/latency rise |
| cloud SOTA / coding-tuned systems | long, tool-heavy, audit-sensitive, side-effectful work |

Core math: if a 10-step workflow is 90% reliable per step, end-to-end success is only about `0.9^10 = 35%`. A model that looks acceptable on single turns can still be unusable as an autonomous worker.

## Safety Stack

Required layers before any real external side effect:

1. Redaction before model upload.
2. Action log after each tool step.
3. Approval gate before send/upload/pay/delete/publish.
4. Git or backup checkpoint for rollback.
5. Private network boundary such as Tailscale or SSH tunnel.
6. No public Gateway exposure until auth, logs, and recovery are tested.

## Use-Case Map

- Browser automation: scraping, form filling, ticket purchase.
- Personal operations: email, calendar, customer / LinkedIn tracking.
- Analysis: industry brief, financial analysis, flight price tracking.
- Repeated workflow: screenshot -> classify -> spreadsheet update -> upload -> notification.
- Learning support: language-learning reminder or daily lesson push.

## Smallest Next Test

Do not implement first. Write a one-page design note in `second-brain-openclaw`:

- minimum architecture
- entrypoint
- redaction point
- approval gate
- action log
- rollback path
- one sandbox task

Sandbox task:

```text
Telegram/Slack command
  -> tmux Codex CLI session
  -> read fake receipt fixture
  -> produce redacted summary
  -> append action log
  -> no upload and no external send
```

## Capacity Impact

Maybe.

This is exciting and system-shaped, so it can easily become a new build lane. It should not become W19 execution unless an existing priority is explicitly deferred.

## Routing

- Keep here: idea development, architecture tradeoffs, purchase gates, model-routing gates, safety stack, and project-graduation thinking.
- Planning repo: keep only status, capacity effect, next test, and links.
- `second-brain-openclaw`: owns OpenClaw research notes, baseline docs, and any future one-page design note or experiment packet.
- Mailman / Slack / Gmail work: may reuse safety conclusions, but should not inherit this idea as automatic scope.

## Decision

Park as a serious but non-primary idea.

The next real action is a bounded design note, not a purchase and not an implementation sprint.
