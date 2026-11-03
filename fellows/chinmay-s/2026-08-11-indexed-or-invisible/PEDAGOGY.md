# PEDAGOGY.md — Indexed or Invisible (GATE P)

**Reel:** `hai-indexed-or-invisible` · 42 beats · Bella (`af_bella`) · Humanitarians AI
**Source:** a narration transcript supplied by the author (spoken ~8m44s), covering the
Jobsekr visa-classification + technical-SEO delivery chain.

---

## 1. What the reel teaches

One thesis, stated at both ends: **discoverability is architecture, not marketing.**
A correct back end that no crawler can reach delivers zero user value.

The spine is five layers, built bottom-up, each one a prerequisite for the next:

| Layer | Mechanism taught | Beats |
|---|---|---|
| 1 — Database | idempotent migration (`IF NOT EXISTS`), 1,000-row batching on `IS NULL`, tier-5 inference join that is overwrite-safe by predicate | B06–B13 |
| 2 — Exposure | JSON-LD `JobPosting`, mandatory vs optional fields, canonical URL resolving the modal/standalone duplicate, `noindex` on expired roles | B14–B19 |
| 3 — Discovery | dynamic route handlers, sitemap index → sub-sitemaps → auto-sharding under the 50,000-URL ceiling, crawl budget as a finite resource | B20–B25 |
| 4 — Programmatic | 30 cities × 15 roles, static param generation + ISR, duplicate-content penalty, per-route FAQPage payload for uniqueness | B26–B32 |
| 5 — Validation | Search Console as the only verdict, remediation loop, Lighthouse + indexed-URL outcomes | B33–B38 |

Bookends: `ClaudeComposerAsk` cold open (B00) → body → verdict recap (B39) →
YOUR TURN handoff (B40) → title outro (B41).

## 2. Narration provenance

Beats **B01–B38 are the author's own words**, transcribed. Editing was restricted to
repairing speech-to-text artefacts and spelling numerals so Kokoro pronounces them.
No claim was added, removed, or strengthened.

**ASR repairs applied — please verify these are what you meant:**

| Transcript said | Rendered as | Why |
|---|---|---|
| "item potent" (×3) | **idempotent** | ASR mis-split; would be read aloud as two words |
| "splitfane" | **split-pane** | ASR artefact |
| "Nex.js" / "next.js" | **Next.js** | consistent product name |
| "layered reax" | **layered rules** | ASR artefact; best reading from context |
| "RO parameters" | **role parameters** | ASR artefact — matches the city × role matrix |
| "batches of 1,00" | **batches of one thousand** | truncated numeral |
| "23,000" | **twenty-three thousand** | TTS reads digits awkwardly mid-sentence |
| "FAQ page JSON LD" | **FAQ-page JSON-LD** | hyphenation for correct prosody |
| "application/xml response" | **application XML response** | the slash is not speakable |
| "rowby row", "highintent longtail", "databacked", "datadriven" | row by row, high-intent long-tail, data-backed, data-driven | ASR word-joins |

**B00, B39, B40, B41 are newly written** (cold open, verdict recap, YOUR TURN, outro) —
these are not from the transcript and need the closest read.

## 3. Claims and their support

Every factual claim traces to the supplied transcript. Two visual specifics were
introduced by the scene set and are **illustrative, not measured**:

- `IdxFaqVariation` shows sample counts (412 / 187 / 96 open roles) for three
  city-role pages. These are placeholders demonstrating per-route variation.
- `IdxSitemapTree` shows sub-sitemap sizes (23,000 / 3,100 / 48). Only the 23,000
  figure comes from the transcript.

Replace both with real numbers before this is ever shown as a factual record.

## 4. Where this could mislead

- The reel presents the five layers as a clean upward sequence. Real delivery
  interleaved them; the transcript already frames this as a retrospective trace,
  not a schedule.
- "Top-tier Lighthouse SEO scores" is the transcript's phrasing. `IdxOutcomes`
  renders a 100. If the real score was lower, change it — a dial is a claim.

## 5. Verdict

```
VERDICT: PENDING — awaiting human sign-off.
```

Audio for the first previz was generated with `--no-gate`, deliberately and on the
record: the narration is the author's own script, but GATE P is a *human* signature
and Claude must not forge one. Read §2 and §3 above, then replace this block with
`VERDICT: PASS` and your date to make the gate real.
