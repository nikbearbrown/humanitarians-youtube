# PEDAGOGY.md — Shipped, Then Blocked (GATE P)

**Reel:** `hai-shipped-then-blocked` · 14 beats · Bella (`af_bella`) · Humanitarians AI
**Target length:** ~3 minutes (projected 3m07s at Bella's measured 2.242 words/sec)
**Source:** a user-supplied explainer transcript, ~5m21s spoken, about a 12-week sprint.

---

## 1. What changed from the source

**Compressed ~60%** (≈1,050 words → 421). The source is a conversational podcast-style
explainer; this cut keeps its facts and its ending provocation but drops the verbal
filler ("let's just jump right in cuz", "I mean", "isn't it?") and the restated framing.

**No individual is named.** Per explicit instruction, every personal attribution was
removed. The source credits a named engineer four times; this cut attributes the work
to the project and to humanitarians.ai, using passive or project-subject phrasing.
A programmatic name-guard runs in the build script and reports CLEAN.

**Dropped for time** (all present in the source, none contradicted here):
- the "why this matters for international students" framing (B00 carries it implicitly)
- the detailed explanation of what canonical tags are for a non-SEO audience
- the "we've all waited on an IT ticket" aside
- the closing thank-you

## 2. Claims, and where each comes from

Every figure is the source transcript's own:

| Claim | Beat |
|---|---|
| 23,000 inert listings classified + backfilled, under 2 minutes, batch writes on production | B01 |
| 4-step pipeline: scrape → US-detect → classify → tag | B02 |
| fifth tier joins company H-1B sponsorship history; never overrides higher-confidence tags | B03 |
| JSON-LD + rich snippets + canonicals; no duplicate-content penalty | B04 |
| Claude defined expected distribution ranges per tag and generated SQL sanity checks | B05 |
| sitemaps to 50,000 URLs; 30 US tech hubs × 15 roles | B06 |
| unique FAQ rich snippets per templated page, from live DB stats | B07 |
| week 10: Lighthouse SEO consistently 90+; all Search Console enhancement warnings cleared | B08 |
| week 11: single-listing lifecycle proof; documented; handoff-ready | B09 |
| week 12: zero code written, blocked on GitHub repository access | B10 |

**Nothing was strengthened.** The source says "90 and above"; `IdxOutcomes` renders a
dial at 90, not 100 — the component was given a `score` prop for exactly this reason
rather than reusing the previous reel's hardcoded 100.

## 3. Where this could mislead

- **B04's split-pane** reuses the scene built for the previous reel, including its
  sample rows and a `jobsekr.com` snippet. These are illustrative, not screenshots.
- **B06's matrix** renders 450 cells (30 × 15). The source says sitemaps handle "up to
  50,000 URLs" — a ceiling, not a count. The scene shows the route matrix, not the URL
  total, so the two numbers should not be read as the same thing.
- **B07's FAQ card** shows sample open-role counts (412 / 187 / 96). Placeholders.

## 4. The editorial risk worth naming

The source frames week 12 as a "relatable corporate reality check" and ends on a
rhetorical question about organizational speed. This cut keeps that, and the verdict
beat states plainly that "a permission stopped it." That is the source's own reading.
It is a claim about an organization, so if this is ever shown outside a personal
portfolio, confirm it is a characterisation you are comfortable standing behind.

## 5. Verdict

```
VERDICT: PENDING — awaiting human sign-off.
```

Audio was generated with `--no-gate`, on the record. GATE P is a human signature and
Claude must not forge one. Read §1–§4, then replace this block with `VERDICT: PASS`
and your date.
