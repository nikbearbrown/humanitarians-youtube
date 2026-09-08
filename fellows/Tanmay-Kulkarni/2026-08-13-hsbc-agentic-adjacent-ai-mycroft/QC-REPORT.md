# QC REPORT — build log

Append-only, dated. Every defect below was found by looking at frames or by measuring output —
not by reading code and assuming.

**Film:** *Their Numbers, My Arrows — Reading an AI Announcement Without Adding to It*
**Built:** 2026-08-18/19 · Brutalist toolkit (Kokoro + Manim + Remotion) · `deep-explainer`
**Output:** 3840×2160 · 16 beats · 513.61s (8:33) · `af_bella` · presenter Tanmay Kulkarni

---

## Gate summary — all clean

| Gate | Result |
|---|---|
| **Gate P** — premise | ✅ PASS (author, 2026-08-18) |
| **Gate P** — narration | ✅ PASS (author read-aloud) |
| **Gate F** — paperwork | ✅ satisfied (FACTCHECK · SHOTLIST · PROMPTS) |
| **Gate L** — beat-mix lint | ✅ clean |
| **Gate A** — static pre-flight | ✅ 10/10 scenes clean |
| **Gate W** — WCAG contrast / margins / overlap | ✅ 10/10 clean |
| **Gate B** — layout audit on rendered clips | ✅ 10/10 clean under `--png --curve-strict` |
| **Gate V** — frame QC on the compiled reel | ✅ **0 BLOCKER, 0 MAJOR** across 32 frames |
| Silence sweep | ✅ 0 gaps >0.55s across 16 beats |
| PROOF Phase 3 | ✅ clear-for-public · teaching **12/12** · production gate **PASS** |

**Verified against the output, not inferred:** `ffprobe` confirms 3840×2160 and 513.61s, which
equals the sum of `mp3/timings.json` exactly. `slots: 16/16 filled`.

---

## 1. Structure v1 was scrapped for being the previous film's shape

v1 used four numbered questions, a framework board at ~14s, questions applied in order, and a
four-step viewer task. **Film 5 (`bs-01-pick-and-scope`) used all four of those.** Back to back, a
viewer would have seen one container twice.

v1 had been checked against prior films on *rhetorical motion* and judged different. **Rhetorical
motion is invisible to a viewer; form is what they experience.** Wrong layer of comparison.

Rebuilt on a **two-column ledger** audited line by line. Standing lesson, recorded in `SCRIPT.md`:
PROOF criterion 1 rewards "a structure before the examples," and the cheapest route to that score
is always a numbered list — so films drift into the same shape unless the form is chosen
deliberately against the previous one. **Log the form, not the argument.**

## 2. The evidence changed under verification, and got stronger

The film was to name kingy.ai and metaintro.com as having conflated HSBC's $1.8bn severance figure
with "AI investment," per case study §6.4. **Both were read directly. Neither did.** kingy.ai
explicitly distinguishes reallocation from new spending.

Primary verification of HSBC's own FY2025 transcript then produced a better example: **two
different $1.5bn figures inside one document** — simplification saves taken to the bottom line,
reallocation costs redirected to growth. Primary-sourced, one document, nobody's error.

**A film about not repeating other people's connections could not have shipped an accusation it
took on trust.** Full record in `VERIFICATION.md`; audit in `FACTCHECK.md`.

Also caught: the PDF extractor splits figures across lines (`$1.` + `5 billion`), and a
first-pass quote came out **truncated mid-sentence**. Standing rule: re-extract with line breaks
joined before any HSBC quote goes on screen.

## 3. Scene detection — three silent-failure modes, all hit

`run.sh` finds Manim scenes by **regex over raw source text**; it never imports or parses Python.

1. **A base class breaks detection.** `class B04_LedgerFull(LedgerBase)` does not match `(Scene)`,
   so **zero scenes were found** and every ledger beat would have silently failed. Beat classes now
   inherit `Scene` directly and share code through a module-level function.
2. **Duplicate scenes per beat.** After adding fixes, B07 and B10 each had two scenes — `run.sh`
   picks one arbitrarily. Verified 1:1 thereafter.
3. **A Manim scene on a Remotion beat overwrites the Remotion render.** `B09_LedgerStruck4` was an
   orphan for a beat whose shot is `REMOTION`. Removed.

## 4. Scenes must animate, and my probe could not see it

A `construct()` that only calls `self.add()` plays zero animations, so Manim writes a **still PNG**
and `run.sh` reports *"no output"*. Every scene now ends with `self.play()`.

**My probes used `manim render -s` — the still flag — which bypasses exactly what was broken.** A
probe that cannot fail the way production fails is not a probe. GATE A had warned
`0 clean · 1 warn` on every scene beforehand; I read "continuing" as "fine."

## 5. Layout — five defects, each caught by a different gate

| Defect | Found by | Cause |
|---|---|---|
| `TypeError: can't multiply sequence by float` | GATE A | ledger data lists named `LEFT`/`RIGHT` shadowed manim's direction constants; `RIGHT * 0.25` multiplied a list of strings. Renamed `SAID`/`ADDED`. |
| Coordinates outside safe area | GATE A | safe area is **6.3 × 3.4**, tighter than the visible frame |
| Column collision ("to the bottom **Sione**") | eye, then GATE B | `max_r` clamped text **width**, not **end position** — a row starting at x=0.42 ran to 6.71 |
| Text sitting **on** a rule line | GATE B | header box y 3.11–3.33 overlapped rules at y 3.18 |
| Text-on-text 58% then 26% | GATE B | B10 stacked condition, tag and caveat in the same band; fixed by computing the gap rather than nudging |

**The strikethrough had to be abandoned.** `run.sh` runs GATE B as `--curve-strict`, under which a
line crossing text is an *error* — and a strikethrough is definitionally that. Cancelled rows now
use a terracotta cross in the left margin plus de-emphasised text. Same meaning, no line on a
glyph, and the check is satisfied honestly rather than disabled.

**`ART_STRICT` defaults to 1, so GATE B blocks on warnings too.** Audit with the flags `run.sh`
uses, not the defaults — that single misunderstanding cost several passes.

## 6. Gate V measures ink, not extent

"Content fills only X% of the safe area" is a **coverage** metric. Three rounds of fixes spread
content wider and thinner — the wrong direction — and B07 went 46% → **41%**, worse.

The clue was the previous film: `ClaudeSplitComparator` scored **94%**, and those beats had
**filled white cards**. My Manim rectangles used `fill_color=PAGE`, identical to the background,
so they contributed nothing. Cards behind B07's quotes and `CARD` fill on B11's boxes cleared it.

## 7. THE CRITICAL ONE — animations stretched 18× and no gate could see it

`compile.py` conforms each clip to its beat's measured audio. The scenes were authored at 1–5s
against beats of 19–55s, so the compile **time-stretched** them:

| | Before | After |
|---|---:|---:|
| Mean stretch | **18.19×** | **1.00×** |
| Worst (B13) | 31.65× | 1.00× |
| B07's second quote lands at | ~83% of beat | **12% of beat** |

A `FadeIn` authored at 1.1s played over 20 seconds. On B07 — the beat the film turns on — the
second verbatim quote did not finish arriving until ~83%, while the narration reads it around 60%.
PLAYBOOK §1b names exactly this: *"an artifact that fades in at 80% of a beat does not cover a
claim made in its first sentence."* It was also simply sluggish to watch.

**Fix:** `scenes.py` reads `mp3/timings.json`; every scene calls `hold_to_beat()` to pad itself to
its measured duration. Reveals play at authored speed up front, then hold.

**Why nothing caught it.** GATE A checks statics. GATE B audits a raw clip. GATE V samples
compiled frames for fill and edges. **None compares animation duration to beat duration** — and
isolated probes have no audio to stretch against. Every automated check was blind to it by
construction. It surfaced only by extracting frames from the *compiled* film at specific
percentages, which is what the production gate actually asks for.

## 8. A stale report read as a current one

The render before the fix **never executed**: a failed shell glob (`media/B0[2-8].mp4` matching
nothing) short-circuited an `&&` chain. But `_qc/REPORT.md` persists between runs, so it still
said *"Clean ✓"* and *"slots: 16/16"* from the prior pass. Taken at face value, the timing bug
would have been declared fixed with nothing rendered.

**What exposed it:** printing the stretch factor beside its previous value. An unchanged
**18.19×** could only mean nothing had rendered. **Verify against a number you expect to change.**

## 9. Components and assets

| Language | Beats | Share |
|---|---|---:|
| Manim — the ledger and its states | 10 | **62%** |
| Remotion | 6 | 38% |

**This inverts Film 5's 94% Remotion**, which PROOF Phase 3 tagged as that film's single biggest
weakness. Variety comes from the ledger changing state, not a different card per beat.

No pantry assets, no generated media, no LaTeX (equation beats are blocked in this install; every
glyph is Pango `Text()`). Reused from Film 5: `ClaudeComposerAsk`, `ClaudeArtifactCardFull`,
`ClaudeTitleOutroFull`.

## 10. Process lessons

1. **Read the checker, don't infer from its error string.** Four failures came from guessing.
   "Shapes never change" was assumed to mean animation geometry; fifteen seconds of `grep` showed
   it signatures **non-text shapes only**, and the fix was an accent rule, not an animation change.
   Both times the source was read, the fix worked first try.
2. **Match the probe to production exactly** — same flags, same output format, same strictness.
   `-s` stills hid the no-MP4 failure; default flags hid `--curve-strict` and `ART_STRICT=1`.
3. **A gate warning is a finding.** `gate A warning … (continuing)` named the animation failure
   before a single frame rendered.
4. **Verify against a value you expect to change**, not against a report that persists.
5. **Clean up in Python, not shell globs.** Failed globs silently short-circuit `&&` chains.

## 11. Small-text letter spacing, and a fix that two gates correctly rejected

Reported from the compiled 4K frames: irregular letter spacing in the ledger, and the terracotta
labels on B07 crossing into the white cards.

**The spacing.** Not a font-fallback problem — Georgia resolves in Pango. Manim rounds glyph
advances at the size it rasterises, so small text loses even spacing. A size ladder rendered at
**2160p**, the shipping resolution:

| font_size | Result |
|---:|---|
| 17 | `Allfigures self-repor ted and unaud ited. HSBC's o wn numbers.` |
| 19 · 20 · 21 | words fuse — `figuresself-reported`, `HSBC'sown` |
| 22 | `All figu res … u naud ited … nu mbers` |
| **23 · 24** | **clean** |

**The first fix was wrong, and GATE A caught it.** Shadowing `Text` to render everything at 4x
`font_size` and `.scale(0.25)` produced clean glyphs, then failed:

- **GATE A** models text width as `len(text) * font_size * 0.012` and its `scale()` is a **no-op**
  (`static_scene_check.py:212`). Small text was therefore modelled 4x too wide, and computed row
  positions like `x_r + width/2` ran off-frame: *"3 explicit coord(s) outside the frame, e.g.
  (7.6,3.2)"*. Ten scenes, nothing rendered.
- **GATE B** read geometry through a similar patch, and supersampling the 42pt head changed its
  line-wrap width enough to add a third line — box top **3.57** against a 3.4 safe area.

Both gates model layout from `font_size`. **Supersampling with `.scale()` makes `font_size` a lie
to them**, so the fix was invisible to the checks by construction. The answer was not to relax the
gates.

**The shipped fix** rasterises small text at 48 and calls `scale_to_fit_width(width * size / 48)`.
Spacing is fixed at rasterisation and survives uniform scaling, verified side by side: `@24`,
`@34` and `@48` scaled to 17pt's width are all clean at the same physical size as native 17pt.
And `scale_to_fit_width` **sets** width (`:213`), so GATE A's stub arrives at
`len(text) * font_size * 0.012` — identical to a native `Text` at that size. Every sub-24pt call
site routes through one `small_text()` helper, sizes unchanged, **so no layout moved**.

**The label overlap** was arithmetic, not judgement. Card height `q.height + 0.72` puts its bottom
edge at `y - q.height/2 - 0.36`; the label sat at `-0.46` with ~0.11 half-height, so its top edge
was **0.01 inside the card**. Moved to `-0.62`.

**Also fixed, unprompted:** B07's two cards were each sized to their own quote, so they had
different widths and the accent bars did not line up — sloppy for two quotes meant to read as a
matched pair. Both now share one width from the wider quote.

### Two self-inflicted failures in this round

1. **I ran `run.sh` without the toolkit venv on PATH.** It calls bare `python3`, so every gate
   died with `ModuleNotFoundError: numpy` / `manim`, `run.sh` logged them as warnings and
   continued, and I first read that as a fault in the scenes. Nothing was slotted, so no bad
   output survived. **Record the invocation, not just the command.**
2. **My revert deleted live code.** Slicing from the `manim` import to `_TIMINGS` took the Claude
   colour tokens and `FONT` with it. GATE A caught it instantly — `NameError: name 'PAGE' is not
   defined` on all ten scenes — and the block was restored verbatim from the session transcript
   rather than retyped from memory. **Delete by name, not by slice.**

**And once more, a stale Gate V report read as current.** After the GATE A block, `_qc/REPORT.md`
still printed *"Frames sampled: 32 · BLOCKER: 0 · MAJOR: 0 · Clean"* while **all ten clips were
missing**. Same trap as §8. The tell was the per-clip table printed beside it.

## 12. Ellipses added to B07's quotes

Both on-screen sentences stop before the end of what HSBC said:

| | |
|---|---|
| Transcript | "…straight to the bottom line**, with immaterial revenue impact.**" |
| Transcript | "…low-returning businesses**, the medium-term intent being to reallocate these costs to areas of competitive strength and generate accretive returns.**" |

The displayed words were exact, both remainders were grammatically complete, and neither omitted
clause changes the meaning — so this was defensible, not an error. But **a film arguing against
adding to what someone said should not present a shortened sentence as a whole one.** Both quotes
now end `line …"` and `businesses …"`.

Verified rather than assumed: Georgia carries U+2026, so the glyph renders from the same face with
no Pango fallback — checked on a 2160p still before re-rendering. GATE A, GATE W and GATE B all
clean; card widths and label clearances unchanged. Narration is untouched (an ellipsis is not
spoken), so the audio, the timings and the 513.61s total are identical.

---

## Final verification — 2026-08-19 (re-verified after the letter-spacing fix)

- [x] **Gate V: 0 BLOCKER, 0 MAJOR** · `run.sh` exit 0
- [x] **3840×2160** — probed on the file, not inferred from `--height` (PLAYBOOK §6 records a
      silent 720p once)
- [x] **513.61s == sum of `mp3/timings.json`** — audio is the clock and the clock holds
- [x] **slots: 16/16 filled**
- [x] **Stretch 1.00× on all 10 Manim beats** (was 18.19×)
- [x] **Moment-of-assertion confirmed on the compiled film** — B07 shows both verbatim quotes,
      both labels and the dated transcript at 6.0s of a 50.0s beat
- [x] **Silence sweep: 0 gaps >0.55s** across all 16 beats
- [x] **Contact sheet reviewed end to end** — the ledger arc reads without sound
- [x] **GATE A: 10/10 clean, 0 warnings** after the spacing fix (was 10 errors under the
      rejected supersampling approach)
- [x] **Letter spacing verified on the COMPILED film, not on isolated stills** — frames pulled
      from `2026-08-18-their-numbers-my-arrows.mp4` at B04 116.6s, B07 196.9s, B10 341.5s
- [x] **B07 labels clear the card borders** and both cards share one width
- [x] **Fresh render confirmed by a value expected to change** — B08 23.0s→22.9s,
      B11 55.6s→55.0s versus the previous build
- [x] **B07 quotes carry a marked ellipsis**, glyph confirmed rendering in Georgia at 2160p
- [x] `@HumanitariansAI` and the `Irreducibly Human` kicker on every Remotion beat

**Nothing outstanding.** Film 5 shipped with a known monoculture weakness carried forward; this one
ships with none.
