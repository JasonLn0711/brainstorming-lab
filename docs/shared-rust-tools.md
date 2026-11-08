# Shared validation and measured improvements

The private [kairos-rust-tools](https://github.com/JasonLn0711/kairos-rust-tools)
repository owns reusable verification mechanisms. Its
[activity scope and explicit-source contract](https://github.com/JasonLn0711/kairos-rust-tools/blob/main/docs/activity-scope.md)
explains how `workspace-review-sources.json` supplements filename-based discovery.
This repository declares the paper validators and their shared YAML dependency;
these remain review candidates, not completed Rust migrations. Inventory support
requires source commit `f4bc9d86d9e62a9921ab271aad09beb97730beb4` or a compatible
successor. Follow the source repository's installation instructions with authorized
private-repository access. Existing paper checks require no Rust installation.

## Single-read paper validation — 2026-11-08

`validate_paper_folder` now reuses the parsed `paper.yaml` mapping to pass the
expected paper ID into quality validation. Previously it reopened and reparsed the
same file. Domain checks and quality identity checks remain in their Python owner;
YAML parsing already has one shared implementation in `idea_os/yaml_io.py`.

Verification against pre-change commit `176c718` on the current checkout found
identical ordered findings (8), with paper YAML loader calls reduced from 2 to 1.
The reduction is in this function's reads/parses, not total repository I/O or
elapsed time. `python3 -m unittest -q` passed 25 tests, including mapping, malformed,
nonmapping and missing-input cases plus ID handoff and single-read assertions.
The shortlist CLI passed. Both paper-lab and quality CLIs still report the same
8 existing boolean-checklist findings in the scientific evaluation; this change
neither suppresses those findings nor claims the current corpus is clean.

No wall-time, energy, maintenance-hour or LLM-token saving has been established.
Any Rust replacement must preserve the domain findings and demonstrate a benefit
under the central [measurement protocol](https://github.com/JasonLn0711/kairos-rust-tools/blob/main/docs/performance.md).
Planning owns priority and capacity; this document owns the implementation receipt.
