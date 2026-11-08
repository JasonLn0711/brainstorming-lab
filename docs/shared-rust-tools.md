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

## Quoted-key parsing correction — 2026-11-08

Follow-up investigation identified the eight earlier findings as fallback-parser
false positives: a YAML key written as `'yes'` was retained with its quote
characters, so the quality validator could not find the actual `yes` field.
The underlying evaluation data was not changed. The shared fallback loader now
decodes single/double-quoted mapping keys, including embedded colons, doubled
single quotes and JSON-compatible double-quote escapes. List mappings use the
same key parser; quoted list scalars remain scalars. Malformed quoted mapping
keys raise errors. This is support for the documented YAML subset, not a claim
of complete YAML specification conformance or complete PyYAML equivalence.

After the fix, 28 unit tests and all three paper CLI checks pass on the existing
corpus (one paper folder, one scientific evaluation and one shortlist). The prior
8-finding observation above remains the pre-fix measurement, not the current
corpus status. This improves validation correctness and reuse of the existing
shared parser; no Rust migration or speed/token-saving claim follows from it.

## Batch shortlist read reuse — 2026-11-08

`validate_shortlists` now shares successful YAML reads across current validation
and historical-selection lookups for one invocation. Each resolved source is
parsed once per batch; the cache is discarded when the call ends. Parse failures
are not cached. Standalone file and registry calls retain their default behavior.
This treats a batch as a source snapshot; concurrent source edits require rerunning
validation. No persisted cache or source-record mutation is introduced.

All 29 tests pass. The current corpus produces identical ordered findings (zero)
with three loader calls reduced to two. A two-shortlist/one-paper fixture reduces
eight reads to three, preserves ordered findings and detects a changed historical
selection on the next call. These are read-count measurements, not elapsed-time,
energy or LLM-token savings.

Ownership review: scientific quality weights, penalties, caps and adjudication
remain in `paper_quality.py`; shortlist recency, selection identity, arXiv URL
normalization and scoring remain in `paper_shortlist.py`. `yaml_io.py` is the
application's read/write codec, not a standalone generic validator. Paper Lab
mixes required files/text sections with training policy and remains a candidate
for separately justified extraction. The
[shared ownership ledger](https://github.com/JasonLn0711/kairos-rust-tools/blob/main/docs/reviewed-sources.json)
pins these decisions to source and regression evidence. Shared Rust syntax or
presence checks do not replace these complete domain entrypoints.
