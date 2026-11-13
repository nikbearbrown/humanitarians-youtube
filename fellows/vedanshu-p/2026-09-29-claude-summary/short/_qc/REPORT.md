# _qc/REPORT.md — Every Fix Has A Ceiling. (9:16 short)

Frame-level visual QC of the portrait cut. Every verdict comes from reading
rendered PNGs in `_qc/frames/`; ffprobe is a FILE check, never QC.

| Field | Value |
|---|---|
| Master | `claude-rag-every-fix-has-a-ceiling-short.mp4` (in `short/`) |
| Resolution | **2160×3840** — confirmed by ffprobe after compile |
| Frame rate | 24 fps |
| Duration | 124.39s (2:04), 8 beats — inside the 3:00 Shorts cap |
| Size | 7.7 MB |
| Audio | peak −0.485 dB, Flat factor 0, Abs Peak count 1 — no clipping |
| Cut type | clean master (`compile.py` without `--review`); frames at 60s and 122s carry no beat marker |
| Voice | Kokoro `am_onyx`, local. **$0.00** |

**Re-band, not a crop.** All seven Remotion beats render through their `916`
compositions. Nothing is centre-cut.

---

## The cut, and why it needed one

The parent is 2:28 against a 3:00 cap, so a short could technically have shipped
the whole reel re-banded. That would not be a derivative cut — it would be the
same video in a different aspect. So this drops the Chapter 7 and Chapter 8 acts
and keeps one concrete case.

| Kept | Role |
|---|---|
| B00 | INTRO — still names all three chapters in its output lines |
| B01 | BLUF — the ceiling thesis |
| B04 | the one worked case: Chapter 9's shortlist |
| B05 | the stand-ins, named |
| BVDT | VERDICT — **rewritten, see MAJOR-01** |
| BHTF | the layer-audit handoff |
| BOUT | OUTRO — **rewritten, see MAJOR-02** |
| END | silent branded endcard, 4.5s |

Dropped: B02 (Ch. 7 fault table), B03 (Ch. 8 drift figure).

---

## Content defects found and fixed

### MAJOR-01 — the verdict asserted two findings the short no longer shows

**Predicted by the parent BUILD-PROMPT**, which says: *"Whatever you drop,
rewrite BVDT and B05."*

BVDT's first two lines read "Ch. 7 — the pipeline names which stage broke" and
"Ch. 8 — assembly improves the odds", and the narration asserted both in the
same breath. With B02 and B03 cut, those are verdict claims with no evidence
behind them in this cut — the NO-SOURCE-NO-VERDICT failure.

**Fixed** by claiming only the case shown and pointing at the rest:

| # | before | after |
|---|---|---|
| 1 | Ch. 7 — the pipeline names which stage broke… | Ch. 9 — a re-ranker reorders. It cannot retrieve what stage 1 missed. |
| 2 | Ch. 8 — assembly improves the odds… | The pipeline and the prompt each stop somewhere too — that is the full video. |
| 3–5 | unchanged | unchanged |

Six lines to five; re-measured at 19.22s (parent: 19.43s).

**B05 was checked against the same warning and deliberately kept unchanged.**
Its claim is about the three source *videos* — which B00 still names in its
output lines — not about beats in this cut. The stand-in declaration is the most
valuable thing in the reel and it survives the edit intact.

### MAJOR-02 — auto-rewritten outro was unusable

`shorts.py`'s outro rewrite truncates dropped beats' `narration_text`:

> "That's the short version. The full video also covers Chapter seven built the
> five-stage… and Chapter eight assembled the prompt… — watch Every Fix Has A
> Ceiling. for the whole story."

Hand-written instead, naming the two ceilings that were cut:

> "That's the short version. The full video adds the other two ceilings — the
> pipeline that names a fault without repairing it, and the prompt that improves
> the odds without compelling anything. The whole story is linked right below."

12.12s, in line with the Ch. 5 (10.84s), Ch. 7 (11.48s), Ch. 8 (11.61s) and
Ch. 9 (11.58s) shorts.

### MAJOR-03 — endcard rendered in an 11px bitmap font at half resolution

`shorts.py`'s `find_serif()` probes only macOS and Linux font paths; on Windows
it returns `None` and the bare `except` in `endcard_png` falls back to
`ImageFont.load_default()`, an ~11px bitmap that ignores the requested size.

Regenerated at **2160×3840** with `runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf`,
reproducing `shorts.py`'s own palette and layout scaled ×2.

---

## B01 — both hesitant-writer traps checked, neither fired

The parent build hit a defect where the final line was still typing at the cut,
and the BUILD-PROMPT now lists three conditions instead of two. All three
verified here:

1. media ≥ 8s — **13.9s** ✓
2. correction on screen before the cut — ✓ (`correct` → `easier to diagnose`)
3. **final line finished typing** — ✓ ("Each one stops somewhere." complete)

The parent's narration fix carried into the short, so the trap did not recur.

**Type size checked rather than assumed.** `BrutalistHesitantWriter` scales by
`min(w/1920, h/1080)`, so portrait takes the width ratio and parent-sized type
usually renders undersized — the Ch. 4 and Ch. 8 shorts both needed a bump.
Measured here: text width **1616px against a 1858px `maxWidth` — 87% fill**. No
bump needed, because this reel's corrected line is 41 characters against Ch. 8's
35 and fills the width at the inherited size.

---

## Beat-by-beat verdict

| Beat | Composition | Verdict | Note |
|---|---|---|---|
| B00 | ClaudeComposerAsk916 | PASS | title on one line; all four output lines legible, so all three chapters are still named |
| B01 | BrutalistHesitantWriter916 | PASS | 87% fill, correction applied, all three lines complete |
| B04 | ShortlistReorder916 | PASS | both columns fit; connectors cross; absent answer in terracotta |
| B05 | EvidenceTiers916 | PASS | tiers stack; bars still visibly unequal; stand-in declaration reads in full |
| BVDT | ClaudeVerdictArtifact916 | **PASS after MAJOR-01** | five lines; claims only the shown case |
| BHTF | ClaudeComposerAsk916 | PASS | full layer-audit prompt renders |
| BOUT | TitleOutroChannel916 | **PASS after MAJOR-02** | title wraps to two lines; **signature "Vedanshu Daxesh Patel"** renders |
| END | STILL | **PASS after MAJOR-03** | legible at 4K |

---

## Compile-stage lint — all three adjudicated, none is a defect

| Lint | Verdict |
|---|---|
| `B00: COLD OPEN LAW wants ClaudeComposerAsk` | The beat **is** `ClaudeComposerAsk`, in its portrait twin. The lint matches composition ids literally and does not know about `916` variants |
| `END: outro is 'un-annotated'` | `END` is `shorts.py`'s own silent branded endcard. The real outro is BOUT immediately before it |
| `remotion carries 7/8 beats (87%)` | Accepted, same as the parent and Chapters 3–9 |

---

## Rubric sweep

| # | Check | Result |
|---|---|---|
| 1 | Edge bleed / clipping | PASS |
| 2 | Title-safe margins | PASS |
| 3 | Container overflow | PASS — all four body components inherit budget fixes made in their source reels |
| 4 | Collision | PASS |
| 5 | Offscreen anchors | PASS |
| 6 | Legibility | PASS — B04's mono ids are the smallest and read clearly |
| 7 | Brand bug placement | Deviation logged in the parent's SOURCES.md |
| 8 | Aspect | PASS — 2160×3840 |
| 9 | Canvas fill | PASS — B01 measured at 87% of `maxWidth` |
| 10 | Short claims nothing it did not show | **PASS after MAJOR-01** |

---

## Audio note

Peak −0.485 dB with `Flat factor: 0` and a single sample at peak — no clipping,
and healthier headroom than the parent's −0.039 dB. The two beats that pushed
the parent to the ceiling (B02, B03) are exactly the two this edit drops.
