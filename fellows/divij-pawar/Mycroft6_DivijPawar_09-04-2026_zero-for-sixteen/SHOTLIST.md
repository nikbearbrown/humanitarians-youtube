# SHOTLIST.md — zero-for-sixteen (GATE F)

This file satisfies the toolkit's GATE F requirement. It is the per-beat
shot list, condensed from `CHECKS-REPORT.md`'s SHOW/HOLD/PUNT classification
(the full reasoning per beat lives there). **16 SHOW, 0 HOLD, 0 PUNT** — no
beat uses a stock/generic stand-in; every shot is either a live UI bookend
or a diagram that enacts a real, sourced claim (see `FACTCHECK.md`).

| Beat | Shot type | Scene / pattern | On-screen artifact |
|---|---|---|---|
| B00 | REMOTION | `ClaudeComposerAsk` | Cold-open composer card: the question, topic, greeting, resolved output lines |
| B01 | MANIM | `B01_RecapAndGap` | Recap panel + §3.4 verbatim quote card |
| B02 | MANIM | `B02_LedgerTable` | `self_report.py` ledger rows, `null` vs `false` chips |
| B03 | MANIM | `B03_OneFetchNotTwo` | Struck-through wrong 2-fetch layout → corrected 4-band diagram |
| B04 | MANIM | `B04_ProvenanceRows` | Real reconciled number vs. fabricated number, rendered as provenance rows |
| B05 | MANIM | `B05_SnapshotDiff` | Six-layer architecture diagram, byte-identical snapshot diff |
| B06 | MANIM | `B06_DedupCollapse` | Three duplicated regex instances collapsing into one |
| B07 | MANIM | `B07_LayeringViolations` | Real test broken three times live, each producing a named failure |
| B08 | MANIM | `B08_CorpusBuckets` | 31 real stored runs sorted into counted outcome buckets |
| B09 | MANIM | `B09_DisjointVocabularies` | Two concept vocabularies with an explicit empty intersection |
| B10 | MANIM | `B10_TwoFixesOneRecord` | Record `f4a4c782` replay, suppression-mechanism timeline |
| B11 | MANIM | `B11_RegexTruncation` | Real number truncating live on screen |
| B12 | MANIM | `B12_TrueNowList` | "True now" callback list to prior confirmed beats |
| B13 | MANIM | `B13_StillNotTrueAndUncommitted` | Honest-ledger warning list, commit hash, file counter |
| B14 | MANIM | `B14_SixteenZeroReprise` | Cold-open counter reprise + dense end-card stats |
| B15 | REMOTION | `ClaudeTitleOutro` | Title restate, handle, subline — kept simple per OUTRO-LAW |

Dense-layout beats flagged for extra render-time attention (per
`CHECKS-REPORT.md` "Legibility contract"): B13 (7-line list + commit panel +
counter in one frame) and B14 (7-bullet end card beneath the counter
reprise). Both were visually QC'd against real rendered frames at 1080p and
4K before this master was compiled.
