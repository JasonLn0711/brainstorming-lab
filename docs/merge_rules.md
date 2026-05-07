# Merge Rules

Merge detection compares idea pairs with a 100-point readiness score:

| Dimension | Points |
| --- | ---: |
| Normalized problem similarity | 25 |
| Semantic similarity | 15 |
| Tag overlap | 10 |
| Complementary value | 20 |
| Evidence alignment | 10 |
| Complexity control | 20 |

## Decisions

| Score | Decision |
| --- | --- |
| 0-39/100 | `do_not_merge` |
| 40-59/100 | `keep_related` |
| 60-74/100 | `suggest_cluster` |
| 75-89/100 | `strong_cluster_or_synthesis` |
| 90-100/100 | `duplicate_merge` |

## Merge Types

`duplicate_merge` means the ideas have the same normalized problem, same method,
and no unique contribution. These can become one canonical idea.

`cluster_merge` means the ideas share a problem family but have complementary
methods or evidence. Keep them as separate idea nodes under one cluster.

`research_synthesis` means several clusters may form a broader research
direction. Do not collapse the individual ideas too early.

## When Not To Merge

Do not merge when the overlap is only a loose tag, when the methods answer
different questions, or when merging would hide a useful objection, baseline, or
negative case.
