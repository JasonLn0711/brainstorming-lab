# Synthetic Consensus Research Line

Canonical ideas:

- `idea_000023`: evidence provenance under recursive AI web contamination
- `idea_000024`: search trust collapse under AI-generated web pollution
- `idea_000025`: effective evidence collapse in AI-mediated search
- `idea_000026`: synthetic consensus and source laundering in AI-generated web pollution

## First Principle

The core problem is not whether a page was written by AI.

The scarce resource is independent, verifiable evidence. A claim becomes risky
when many pages, citations, snippets, summaries, or retrieved documents make it
look widely supported, while the underlying evidence lineages collapse to one
weak source, a circular citation cluster, or no primary source at all.

Working definition:

```text
Web Pollution = high apparent support with low independent evidential support
```

This protects the research from the weak assumption that `AI-generated =
polluted`. AI-written content can be useful and faithful. Human-written content
can be wrong. The research target is evidential distortion.

## Core Distinctions

| Weak framing | Strong framing |
| --- | --- |
| Is this article AI-generated? | Does this claim create false evidential weight? |
| How many sources mention the claim? | How many independent evidence lineages support the claim? |
| Are there citations? | Do the citations faithfully support the claim? |
| Is the answer correct? | Is the answer verifiable through primary or accountable evidence? |
| Is the page ranked high? | Is primary evidence being displaced by derivative content? |

## Key Concepts

### Synthetic Consensus

Many AI-generated, AI-assisted, SEO-style, or derivative pages repeat the same
claim. Search engines, RAG systems, or users may read repetition as independent
agreement even when the pages share one lineage.

### Source Laundering

A weakly supported claim gains apparent legitimacy through paraphrase,
summary, citation, SEO packaging, authority-looking source placement, or a
high-authority citation that does not support the actual claim.

### Truthful Derivative Pollution

Pollution is not only falsehood. A derivative page can be factually correct but
still displace primary evidence, reduce source diversity, and train users or
RAG systems to rely on summaries instead of original evidence.

## Metrics

```text
AS(c) = number of documents that appear to support claim c
IES(c) = number of independent primary evidence lineages supporting claim c
SCG(c) = AS(c) - IES(c)
SCG_ratio(c) = AS(c) / (1 + IES(c))
```

Additional metrics:

- `EWSC`: exposure-weighted synthetic consensus
- `PSDR`: primary source displacement rate
- `SF`: evidence support fragility after pruning derivative sources
- `CFR`: citation faithfulness rate
- `SLR`: source laundering rate
- `RSSE`: RAG synthetic source exposure

## Minimum Pilot

Use a defensive scam / cybercrime domain first.

1. Select 10 public scam or cybercrime claims.
2. Collect top 10 public web results for each claim.
3. Normalize claims and group documents into provenance clusters.
4. Label evidence tier: primary, reputable secondary, derivative with
   citation, uncited, circular / synthetic / unverifiable.
5. Compute `AS`, `IES`, `SCG`, and `SF`.
6. Check citation faithfulness for the top three cited documents per claim.
7. Compare baseline retrieval with a simple provenance-aware reranker.

## Pressure Test

Question for each claim:

```text
If we remove near-duplicates, same-lineage derivative pages, unsupported
citations, and circular citation clusters, does the claim still have support?
```

If support collapses, the issue is not just authorship. It is synthetic
consensus and source laundering.

## Boundaries

- Use public pages only.
- Keep cybercrime examples defensive and non-operational.
- Do not accuse specific domains without a separate evidence packet.
- Do not use AI-text detection as ground truth.
- Do not collect personal browsing behavior without ethics review.
- Treat Common Crawl, SERP snapshots, and answer-engine citations as different
  exposure surfaces, not interchangeable ground truth.
