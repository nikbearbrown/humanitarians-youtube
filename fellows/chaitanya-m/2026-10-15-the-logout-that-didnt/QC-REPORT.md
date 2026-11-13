# VISUAL QC — The Logout That Didn't

**Reel:** `claude-hai-the-logout-that-didnt` · ai-explainer (postmortem) · claude-hai · Bella
**Date:** 2026-10-15

| Cut | File | Resolution | Duration | Slots |
|---|---|---|---|---|
| 16:9 master | `claude-hai-the-logout-that-didnt.mp4` | 3840×2160 @30 | 232.80s (3:53) | 14/14, no slates |
| 9:16 short | `short/claude-hai-the-logout-that-didnt-short.mp4` | 1080×1920 @30 | 162.03s (2:42) | 11/11, no slates |

Every beat's source render probes 3840×2160 before compile; the master probes the same
after. No upscaling anywhere.

---

## Sampling method, and a standing warning

Frames are taken by **exact frame index**, never with input-side `-ss` (which snaps to
the nearest keyframe and on a 4K master can be seconds out).

**A second trap found on this reel:** `select='eq(n\,A)+eq(n\,B)+…'` in a single ffmpeg
call does *not* reliably return frames in the order requested — `n` counts in decode
order, so with many terms the outputs can pair up with the wrong beat ids. It mislabelled
the tail of both cuts here, twice, and both times the *video* was correct and the
*contact sheet* was wrong.

**Anything load-bearing is therefore confirmed with a single-frame extraction using
output-side seek** (`-i file -ss T -frames:v 1`), which is slow and unambiguous. That is
how B09's caveat was verified in both cuts.

## Defects found and fixed

| # | Sev | Beat | Rubric | Defect | Fix |
|---|---|---|---|---|---|
| 1 | MAJOR | B09 | signalling | The `main — FIXED` row resolved at p=0.30, but "the fix is on main" is spoken at ≈p=0.53. **A reveal landing before its word** — the viewer reads the answer before hearing it, which flattens the beat's one piece of suspense. | Row reveals re-keyed to `0.52 + i·0.10`, so `main` lands on its word and `development` on its own at ≈0.61. Consequence line pushed to 0.84. |
| 2 | MAJOR | B07 | canvas fill | The reach box and the survivor box sat in a thin horizontal band with the frame mostly empty — 5.0% ink. | Both boxes `alignSelf: stretch` with a 420px min-height row, padding and gaps roughly doubled. Now 11.6%. |
| 3 | MAJOR | B04 | canvas fill | The carried-over checklist rendered as a thin strip; the `evidence = session` equation was undersized for the beat's whole argument. | Card widened to 1420 and padded, equation type 44→54, the `=` 56→70, eyebrow 28→34. Now 16.8%. |
| 4 | MINOR | B01, B02, B03, B05, B08 | canvas fill | First pass sized content for a smaller stage; several beats read timid on 1920×1080. | Browser 1180→1420 wide, race lanes 52→78 tall, cleanup card 1320→1480, platform 760→980, panes stretched to the well height. |
| 5 | MINOR | both `.srt` | correctness | 2 overlapping cues. `cues_for_beat` de-overlaps *within* a beat, so a beat's last cue could still run past the next beat's first — a final word often rings past the measured boundary. | A global de-overlap pass added to `make_srt.py` after all beats are assembled. Now 0 overlaps in both files. |
| 6 | MINOR | short / endcard | brand | `shorts.py` hardcodes `dark=True`; the endcard rendered near-black against a cream fidelity palette. | Regenerated with `endcard_png(..., dark=False)`; ground pixel verified `(243,235,221)`. `shorts.py` untouched. |

**Remaining: zero BLOCKER, zero MAJOR.**

Carried over from the previous reel and confirmed working here: the `haiKit` preroll that
pre-plays the shared Claude scenes' intro. **Zero blank frames at all 13 boundaries of the
16:9 and all 10 of the 9:16** (the automated pass flags B13→END on the short; inspection
shows that is the silent endcard's own low ink, not a hole).

## Opening-state audit (t = beat start + 0.12s)

| Beat | 16:9 | 9:16 | Opens dressed? |
|---|---|---|---|
| B00 | 1.9%¹ | 4.4% | yes — chrome, eyebrow, title, greeting, composer, footer |
| B01 | 41.6% | 23.3% | yes — browser drawn, SIGNED IN lit, button in place |
| B02 | 47.7% | 37.9% | yes — both panes framed, identical code blocks visible |
| B03 | 47.4% | 23.2% | yes — full checklist drawn, all rows unticked |
| B04 | 14.9% | 8.5% | yes — B03's completed list carried over |
| B05 | 9.3% | (dropped) | yes — app on its platform, code pinned |
| B06 | 36.6% | 30.0% | yes — both diagrams framed, cookie slots drawn |
| B07 | 5.3%² | 9.6% | yes — cookies drawn inside and outside the boundary |
| B08 | 5.9%² | 7.1% | yes — both lanes and the finish box drawn at the start line |
| B09 | 15.0% | 8.8% | yes — status board drawn, both branch rows labelled |
| B10 | 22.2% | (dropped) | yes — both lesson cards framed |
| B11 | 38.4% | (dropped) | yes — artifact page open, heading set |
| B12 | 45.5% | (dropped) | yes — composer, greeting, prompt already typing |
| B13 | 5.5% | 9.7% | yes — title set |

¹ Thin dark type on a cream page; low ink is correct, frame read to confirm.
² Post-fix figures; both were lower before #2 and #3.

**No scene opens empty in either cut.**

## Rubric sweep

| Point | 16:9 | 9:16 |
|---|---|---|
| Edge bleed / clipping | pass | pass |
| Title-safe margins | pass | pass |
| Container overflow | pass | pass |
| Collision | pass | pass |
| Offscreen anchors | pass | pass |
| Legibility | pass | pass, with one note³ |
| Brand bug placement | pass — every beat; full size on B13 | pass |
| Aspect | 3840×2160 throughout | 1080×1920 throughout |
| Canvas fill | pass (fixes #2–#4) | pass |
| Opening state at t=0 | pass | pass |
| Blank frames at cuts | 0 of 13 | 0 of 10 |

³ On the 9:16, B09's secondary detail text (`merged 2026-10-13`, `fix still open`) is
small. The load-bearing words — `main · FIXED` and `development · NOT YET` — are set
large and read clearly, and the consequence line beneath them is legible. Verified by
single-frame extraction at 146.0s, not by thumbnail.

## Author's constraints — verified on the built artefacts

| Check | 16:9 | 9:16 |
|---|---|---|
| Narration implying `development` has the fix | **0** | **0** |
| PR #13 caveat present, spoken | yes (B09, B11) | yes (B09) |
| PR #13 caveat present, **on screen** | yes (B09 board + B11 card line) | yes (B09 board) |
| "fully solved" or equivalent overclaim | **0** | **0** |
| Hedging on the three verified facts | **0** | **0** |
| Textbook-revocation reconciliation stated | yes (B11) | n/a — B11 dropped, but the short makes no recap claim at all |

Every sentence mentioning `development` was extracted and read individually; all five
either describe the *environment* (B05, B06, B10) or state that the branch lacks the fix
(B09, B11). None pairs it with a fixed state.

## PR #13 — re-checked at delivery, not taken from the brief

```
2026-10-15T19:46:04Z
$ gh pr view 13 --repo Medhavy/medhavi-hub
{"state":"OPEN","mergedAt":null,"mergeStateStatus":"CLEAN","baseRefName":"development"}

development · signOut( calls ............ 0
development · stale "No Clerk signOut" ... 1
main · signOut({ redirectUrl }) .......... 1
main · stale "No Clerk signOut" .......... 0
```

**Still open at delivery.** The caveat is accurate as cut. If #13 merges before publish,
re-record B09 and B11 and re-render those two beats; nothing else depends on it.

## Subtitles

| Cut | Cues | Coverage | Overlaps |
|---|---|---|---|
| 16:9 | 84 | 0.00–232.41s of 232.80s; all 14 beats, bookends included | 0 |
| 9:16 | 57 | 0.00–157.22s of 162.03s; tail is the silent endcard | 0 |

The caveat appears in the subtitle file as its own cue (#57 on the master):
"The development branch does not have it yet…".
