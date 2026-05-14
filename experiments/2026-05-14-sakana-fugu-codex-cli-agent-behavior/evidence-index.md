# Evidence Index

This file extracts the decision-relevant evidence from the copied logs. It does
not replace the source logs.

## Primary Fugu Ultra Log

Source:
`source-logs/2026-05-13-ubuntu-fugu-ultra-phase2-validation-source.md`

| Lines | Evidence | Interpretation |
| --- | --- | --- |
| 1-13 | Codex CLI v0.130.0, `fugu-ultra high`, YOLO mode, objective to make official IC produce `/shared/success.txt`. | The run had a clear success artifact and high tool freedom. |
| 11 | Token usage: `total=6,319,482`, `input=6,136,936`, cached input `23,226,988`, `output=182,546`, `reasoning=3,437,721`. | Extreme token amplification relative to unfinished outcome. |
| 17-35 | Memory search, repo/docs inspection, lab extraction, Docker/grader/backdoor/config reading. | Strong initial environment discovery. |
| 21 | Direct EC success-file creation identified as grading bypass. | The model initially understood an important proof boundary. |
| 39-79 | ELF, stack, ROP/gadget, `.text`, `.bss`, `user_input`, and related binary checks. | Real technical analysis, not random command use. |
| 45, 87-95, 101-105, 129-131, 145 | Repeated `zsh: ... == not found` and permission/TTY friction. | Environment-command style was not stabilized into a clean procedure. |
| 87-107 | Docker IC setup required manual correction after script permission and non-TTY issues. | The run recovered locally but did not preserve a compact reusable runbook. |
| 111 | Manual `/backdoor` execution occurred. | Valid only as a sanity check; invalid as official success proof. |
| 113-123 | Tiny input consumed; overflow input produced `blogic-694.core`; RIP/coredump inspection followed. | Concrete progress: crash/control-flow evidence was found. |
| 141-147 | `one_gadget`, libc `system`, `execve`, and `pop rdi; ret` in libc were explored. | Plausible route exploration, but not proof of exploit completion. |
| 193-203 | Patterned coredump showed controlled stack bytes near `[LOG]: JNCLAWCMD_/backdoor_#_...`. | The run had valuable state evidence that should have been externalized earlier. |
| 262-270, 288 | Symlink/target sweeps and 653-address sweep did not produce success. | Broad exploration reached a bounded negative result. |
| 304-324 | The run wrote `PHASE2_SUCCESS_VALIDATION.md`, ran static checks, compile checks, and found pytest unavailable. | Late-stage documentation/validation happened, but after very high context cost. |
| 334-338 | Plan items were marked complete even though official success did not occur. | Self-report calibration issue: plan status contradicted outcome evidence. |
| 340-432 | Final answer correctly refused to claim completion and named the blocker. | The final conclusion was honest, but expensive and late. |

## GPT-5.5 Ubuntu Handoff Log

Source:
`source-logs/2026-05-13-ubuntu-gpt55-phase2-handoff-source.md`

| Lines | Evidence | Interpretation |
| --- | --- | --- |
| 1-14 | Codex CLI v0.130.0, `gpt-5.5 xhigh`, same `nycu_network_security_practice_114-2` repo, Full Access, explicit handoff task. | Same project/runtime family as the Fugu run, but different task objective. |
| 16-52 | User explicitly framed context pollution, state compression, and `HANDOFF_PHASE2.md`. | The task was to externalize memory, not continue blind exploration. |
| 284-368 | GPT-5.5 rechecked repo, container, binary, Docker, coredump, and config state. | The model verified before writing the handoff. |
| 370-466 | `HANDOFF_PHASE2.md` was created with objective, facts, theory, reproduction, and next-agent steps. | Strong state compression pattern for long-running agents. |
| 521-547 | Readback and final summary confirmed the handoff remained uncommitted and the run took 6m21s. | The closeout preserved git state and did not overclaim. |

## Same-Environment Fugu vs GPT-5.5 Comparison Notes

| Evidence | Interpretation |
| --- | --- |
| Fugu lines 1-13 and GPT-5.5 lines 1-14 show the same Codex v0.130.0 and the same repo name. | The comparison is useful for environment-level behavior analysis. |
| Fugu lines 13 and 340-348 show an official success-validation task that ended without `/shared/success.txt`. | Fugu was evaluated on direct solving/validation behavior. |
| GPT-5.5 lines 14-52 and 370-466 show a handoff/state-compression task, not direct exploit solving. | The contrast must not be treated as a same-prompt success-rate benchmark. |
| GPT-5.5 lines 370-466 define FACT, REPORTED-UNVERIFIED, THEORY, proof rules, environment facts, and next steps. | GPT-5.5's supplied run demonstrates memory repair and evidence stratification. |
| Fugu lines 334-338 marked all plan items complete even though lines 340-348 and 432 state official success was not achieved. | Fugu showed plan/outcome calibration drift under a long run. |
| Fugu lines 416-424 name the real blocker: `rdi` was not controlled at `maintenance_task+5` and the bounded sweep found no success target. | Fugu did identify a valuable technical blocker, but only after high exploration cost. |

## GPT-5.5 Mac Publish / Validation Log

Source:
`source-logs/2026-05-14-mac-gpt55-git-publish-source.md`

| Lines | Evidence | Interpretation |
| --- | --- | --- |
| 4, 17, 193 | Started as `gpt-5.5 medium fast` for git publish, Full Access, then switched to `gpt-5.5 xhigh`. | The Mac log combines an initial git synchronization pass and a later completion/validation attempt. |
| 27-117 | Clean git publish flow: status, remote, fetch, ancestry check, fast-forward, push `Everything up-to-date`. | Good bounded tool loop and history-preserving behavior. |
| 178-189 | Existing Project II evidence still said Phase II success had not been observed and `/shared/success.txt` was absent. | GPT-5.5 did not start from a false-success assumption. |
| 275-285, 329-367 | Docker, qemu user-mode, gdb, and Python Capstone were initially unavailable; host OS was Darwin/MacBook-Air/ARM64. | The Mac host had higher validation friction than the Ubuntu native runs. |
| 372-424 | Mac environment lacked working Docker initially; Docker path was a broken symlink. | The run separated environment blockers from task completion. |
| 452-483 | QEMU was installed through Homebrew, but only `qemu-system-x86_64` was available. | The agent explored a local validation fallback but did not overclaim user-mode compatibility. |
| 529-542 | Colima and Docker CLI were installed and verified. | Environment repair progressed from static-only analysis to a possible official-like runtime. |
| 552-568 | First x86_64 Colima start failed because Lima x86 guest agent was missing; `lima-additional-guestagents` was installed. | The run diagnosed a concrete environment blocker and installed the missing component. |
| 608-625 | The failed default Colima instance was deleted and a clean `phase2` profile started using QEMU; Docker context became `colima-phase2`. | The run established a working x86_64 Docker VM on macOS ARM64. |
| 635-665 | Lab extraction was moved under `/Users`, `linux/amd64` IC image was built, and `IC_PHASE2` was started manually with ASLR disabled and `/runserver.sh`. | The run rebuilt an official-like Phase II validation path despite Docker script interactivity assumptions. |
| 692-706 | `gdb`, `binutils`, and `file` were installed inside the IC container. | Dynamic validation tooling was moved into the target Linux runtime. |
| 723-749 | Shared-volume coredump output was unreliable, so the run switched to direct `/blogic` / gdb execution inside IC. | The run adapted the validation method to host/runtime constraints. |
| 796-813 | Stack shellcode reached the intended target but faulted under NX. | Direct stack shellcode was converted into a verified negative path. |
| 816-1005 | Bounded one-shot partial-return sweep ran over text-section targets and four prefixes; no success after 10,328 combinations. | A broad but bounded negative result was produced instead of open-ended guessing. |
| 1120-1312 | The later pass recorded reproducible Phase II lab evidence and sweep harness artifacts. | A more structured validation/handoff package emerged. |
| 1563-1730 | README, completion audit, success-validation doc, requirements traceability, static checks, and handoff were updated to reference the deep validation attempt and sweep harness. | Negative evidence became durable repo state. |
| 1738-1848 | `git diff --check`, static gate, compile/build checks, Docker build, pytest unavailable. | Validation was reported with explicit limitations. |
| 1769-1820 | `colima-phase2` remained active; a tiny live IC sweep smoke ran 24 candidates with no fake success, then `/runserver.sh` was restarted. | The new sweep harness was smoke-tested without fabricating success. |
| 1892-1957 | Logical commit and push to `origin/main` after ancestry checks. | The run completed a durable checkpoint without rewriting remote history. |
| 1971-1999 | Final summary stated Project II/Phase II was not full-credit complete, documented deep validation and sweep harness, named commit `ab319c0`, and said worktree was clean. | The closeout preserved an honest completion boundary and a clean handoff state. |
| 2002 | Worked for 44m02s. | The Mac validation attempt was shorter than the Fugu Ubuntu run despite higher host friction. |
| 2003 | Token usage: `total=1,098,226`, `input=988,858`, cached input `28,131,328`, `output=109,368`, `reasoning=52,062`. | Still large, but much lower reasoning-token amplification than Fugu. |

## Mac ARM64 Comparison Notes

| Evidence | Interpretation |
| --- | --- |
| Mac lines 275-367 and 552-625 show Docker/qemu/gdb/capstone gaps followed by QEMU/Colima/Docker repair. | GPT-5.5 dealt with a harder host environment than the native Ubuntu Fugu run. |
| Mac lines 635-665 show a manually reconstructed `linux/amd64` IC path under Colima because the lab script assumed interactive Docker. | The run transformed host friction into a reproducible validation runbook. |
| Mac lines 796-813 and 816-1005 show NX and one-shot text-section sweep negative results. | The Mac run's main technical value is stronger negative evidence, not success. |
| Mac lines 1120-1312 and 1563-1730 show docs/script/handoff/audit updates. | The run externalized memory into durable repo artifacts. |
| Mac lines 1892-1999 show commit, push, clean worktree, and explicit no-success boundary. | The run closed cleanly without false completion. |
| Fugu line 11 vs Mac line 2003 shows 6.3M vs 1.1M total tokens and 3.44M vs 52k reasoning tokens. | Even with higher host friction, GPT-5.5 produced a more bounded engineering trace. |

## Token Ratios

| Run | Total | Input/output | Reasoning/output | Reasoning/total | Outcome |
| --- | ---: | ---: | ---: | ---: | --- |
| Fugu Ultra Ubuntu | 6,319,482 | 33.6:1 | 18.8:1 | 54.4% | No official `/shared/success.txt` |
| GPT-5.5 Mac | 1,098,226 | 9.0:1 | 0.48:1 | 4.7% | Durable checkpoint pushed |

These are not a controlled model benchmark because the tasks and environments
were different. They are still useful behavioral evidence: Fugu's run shows a
larger exploration-to-state-compression gap, while GPT-5.5 shows stronger
bounded closeout behavior in the supplied logs.

The Ubuntu Fugu-vs-GPT-5.5 comparison is narrower but still not a fair solving
benchmark: it uses the same Codex/repo/IC problem family, but Fugu was asked to
continue official validation while GPT-5.5 was asked to produce a handoff.
It supports conclusions about state compression, not direct exploit success.
