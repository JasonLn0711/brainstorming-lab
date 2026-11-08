# Ideas

Idea YAML files are the canonical database.

| Folder | Status values |
| --- | --- |
| `raw/` | `raw` |
| `evolving/` | `emerging` |
| `structured/` | `structured`, `research_candidate`, `execution_ready` |
| `executing/` | `executing` |
| `archived/` | `archived` |

Use:

```bash
python3 scripts/new_idea.py "Idea title" --tags tag1,tag2
python3 scripts/normalize_problem.py
python3 scripts/score_maturity.py
python3 scripts/link_ideas.py idea_000001 idea_000002
```

Current generated overview:

```text
index/idea_index.md
index/tag_index.md
index/cluster_index.md
index/research_candidate_index.md
```

## 2026-11-08 API 選型研究

[GLM-5.3 非中國 API 與資料流評估](2026-11-08-glm-5-3-non-china-api.md)（`idea_000051`）：供稿保存、來源查核、三層地域條件與 Planning 雙向橋接。

## 2026-11-08 人生體驗反思

[幸福、回憶與人生機會的時效性](2026-11-08-experience-memory-life/README.md)（`idea_000052`）：截圖保存、完整供稿、哲學歸因與幸福概念查核，以及生活原則／日週規劃雙向連結。
