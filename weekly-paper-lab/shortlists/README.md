# Weekly Shortlists

Each week should have one auditable shortlist:

```text
weekly-paper-lab/shortlists/<YYYY-Www>.yaml
```

The shortlist is canonical for paper selection scoring. It records 3 to 5
candidate papers, observable evidence, recomputed scores, the selected paper,
and rejection reasons for the others.

Previously selected papers or essays are not valid new candidates. The checker
compares normalized `paper_id`, title, and identity URLs against earlier selected
items from `weekly-paper-lab/papers/` and prior shortlists.

Use `weekly-paper-lab/templates/shortlist.yaml` as the starting shape, then run:

```bash
python3 scripts/check_paper_shortlist.py
```
