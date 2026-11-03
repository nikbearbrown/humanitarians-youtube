# CHECKS-REPORT.md — when-two-agents-disagree

Written before the first slate compile, per PROOF GATE (ai-explainer
SKILL.md). This reel is **12 beats (B00-B11)**, not the ai-explainer
default of 10 — see "Beat-count deviation" below.

## Per-beat classification (SHOW / HOLD / PUNT — nopunt SKILL.md)

| Beat | Class | Scene / pattern | Reason |
|------|-------|------------------|--------|
| B00 | SHOW | ClaudeComposerAsk (Remotion) | Cold-open bookend; the UI is the subject |
| B01 | SHOW | B01_OneVoiceThenMany (Manim) | Names the single-voice-to-many reframe as a real diagram (one mic multiplying into four, two glowing in contradiction) — nopunt "one thing splits into N, two of which conflict" row |
| B02 | SHOW | B02_TheNaiveFix (Manim) | Names a blending mechanism and its failure mode as a literal diagram (two bubbles into a blender, one grey bubble out, checked against the "A was right" case) — nopunt "two things combined into one, worse than either" row |
| B03 | SHOW | B03_DetectingDivergence (Manim) | Names a threshold-comparator mechanism with a real dial/gauge and two structured signal cards — nopunt "two values compared against a calibrated threshold" row |
| B04 | SHOW | B04_ArbitrationSetup (Manim) | Names a bounded-exchange mechanism, contrasted against a crossed-out unbounded alternative — nopunt "claim visibly corrected/bounded" row |
| B05 | SHOW | B05_ArbitrationOutcomes (Manim) | Names a branching outcome (one path merges, one stays split) — nopunt "one process, two named outcomes" row |
| B06 | SHOW | B06_UnresolvedHandling (Manim) | Names a real vs. ghosted-failure document comparison — nopunt "two things compared, one correct one wrong" row |
| B07 | SHOW | B07_SharedContamination (Manim) | Names the falsifiability turn as a diagram (two nameplates glowing the same color, a crack neither notices) — nopunt "structural blind spot shown, not just asserted" row |
| B08 | SHOW | B08_TheFramework (Manim) | Names a set of four transferable rules in a 2×2 grid — nopunt "panel/list of N things" row |
| B09 | SHOW | ClaudeVerdictArtifact (Remotion) | Verdict bookend; recaps, asserts nothing new |
| B10 | SHOW | ClaudeComposerAsk (Remotion) | Handoff bookend; prompt typed, read aloud, discussed with a 3-step scaffold |
| B11 | SHOW | ClaudeTitleOutro (Remotion) | Outro bookend; title restate + bridge to STEM7 |

**12 SHOW / 0 HOLD / 0 PUNT**

No beat requires an archival photograph — the only legitimate HOLD in this
catalog. Every claim in this script is a general architectural pattern
(structured-signal comparison, bounded debate, branching outcomes,
structural blind spot), all of which are animatable diagrams, not
stand-ins for a real system this project has built.

**Punt costumes explicitly avoided:** the source script's two-desks title
card and its "AFFIDAVIT OF DISAGREEMENT" end-card ledger are rebuilt into
real diagram beats and Remotion bookend props rather than carried as
stills or a literal courtroom-prop illustration. No gen-AI clip, no stock
icon of a handshake or gavel, no unfilled pipeline slate, no card whose
narration names a visual that isn't actually on screen.

## Beat-count deviation (12, not 10)

`agents.md`'s Quick Start default is a fixed 10-beat B00-B09 structure.
This reel authored 12 (B00-B11) because "The Arbitration Step" carries two
independently-checkable ideas that need their own on-screen artifact:

- **The single-round mechanic** (B04) — the bounded exchange itself,
  contrasted against an unbounded debate's failure mode — and **the
  resolved/unresolved branch** (B05) — the two named outcomes that round
  produces — are each their own idea. Forcing both into one beat would
  either cut the unbounded-debate contrast (the mechanism's own
  justification for why it's bounded at all) or crowd two distinct
  diagrams into one hold.
- This matches the reel's actual content mass rather than forcing a fixed
  count — `youtube/CLAUDE.md`'s "one idea per beat" rule was prioritized
  over matching the 10-beat default exactly, the same reasoning STEM5
  applied to its own mechanism splits.

## Whole-sheet teaching-arc checklist

- [x] **FRAMEWORK beat** — B01 states the episode's central reframe
  (disagreement between independent agents is a signal, not a bug)
  **before** the naive fix, detection, or arbitration mechanisms are
  described.
- [x] **WORKED EXAMPLE** — the "Agent A: margins improving / Agent B:
  margins declining" scenario is introduced in B00 and carried through
  B02 (blended into a worse answer), giving the naive-fix beat a concrete
  instance rather than an abstract description alone.
- [x] **FALSIFIABILITY / edge-case beat** — B07 is the dedicated stress
  test, and it stress-tests the reel's *own proposed mechanism*:
  arbitration only fires on disagreement, so two agents drawing on one
  contaminated source will confidently agree their way past it,
  undetected. The framework in B08/B09 explicitly closes on "it lowers
  your risk, it doesn't take it to zero" rather than presenting
  arbitration as airtight.
- [x] **SCAFFOLDED viewer task** — B10 ships a real, ordered 3-step task:
  name the structured signal you'd compare in your own multi-agent
  system, pick an actual threshold, and decide in advance what
  "unresolved" looks like in your own output. This is directly actionable
  against the viewer's own work, not "learn more."
- [x] **Four bookends** — B00 (cold open), B09 (verdict), B10 (your turn),
  B11 (title-restate outro, bridging to STEM7).
- [x] **No source, no verdict** — every claim-bearing beat carries its own
  on-screen artifact: the multiplying-mic reframe (B01), the blender and
  its worse-than-either output (B02), the gauge and threshold (B03), the
  bounded-exchange stamp and crossed-out unbounded ghost (B04), the
  branching resolved/unresolved paths (B05), the boxed-vs-folded report
  comparison (B06), the shared document with its unnoticed crack (B07),
  the four-rule grid (B08).

**Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓ |
SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓**

## Slate rules audit (Step 4b, automated)

Not yet run against `runtime/qc/sheet_check.py` — see BUILD-PROMPT.md Step
1. All `ClaudeComposerAsk` (B00, B10) and `ClaudeVerdictArtifact` (B09) /
`ClaudeTitleOutro` (B11) props were hand-checked against the hard-limit
table in `agents.md` Step 4 during authoring:

| Beat | Field | Length | Limit | OK? |
|---|---|---|---|---|
| B00 | `topic` | 24 chars ("MULTI-AGENT DISAGREEMENT") | 125 hard | yes |
| B00 | `greeting` | matches `metadata.greeting` ("Olá, Divij") | 55 hard | yes |
| B00/B10 | `command` | single-line, well under 100 chars | wraps, not hard | yes |
| B09 | `artifactLines[]` | each line under 90 chars | wraps, not hard | yes |
| B11 | `title` | "When Two Agents Disagree", 25 chars, clean 2-line wrap | wraps, not hard | yes |

Run `./art check` (or `sheet_check.py` directly) before rendering to get
the automated pass — this table is a manual pre-check, not a substitute.
Note the 9:16 short's tighter limits (`topic` ~45, `greeting` ~21) have
**not** been checked yet — that happens against the derived short's own
sheet, per `youtube/CLAUDE.md` §2, after the 16:9 master is built and QC'd.

## Legibility contract (per beat)

Every SHOW beat names its on-screen artifact and every Manim beat carries
an ordered `show` block in `beat_sheet.json`. Scenes should hold ~15-35%
negative space; un-highlighted elements stay at INK/SOFT and are never
dropped below GHOST. B03's gauge and its two signal cards should hold
simultaneously for the full comparison; B06's real-vs-ghosted report pair
should be shown side by side, not in sequence, so the "folded away"
failure mode is visibly a corruption of the same document, not a
different one; B08's four-rule grid should hold all four simultaneously
once revealed, not cycle through them.

## PPT test

No beat is a headline over a paragraph. Motion should enact the sentence
in every body beat: one microphone literally multiplying into four
(B01), two speech bubbles physically entering a blender and one worse
bubble emerging (B02), a gauge needle crossing a drawn threshold line
(B03), a debate stamped "1 ROUND ONLY" beside a crossed-out spiral (B04),
one arrow forking into two named outcomes (B05), a boxed report set beside
its own folded-away ghost (B06), a crack running through a document two
glowing-identical nameplates both miss (B07), four icons each collecting
a rule (B08).

## Status

Beat sheet, gate docs, and `scenes.py` are authored and internally
consistent — verified by direct diff: every `shot.manim.scene_class` in
`beat_sheet.json` has exactly one matching `class` in `scenes.py`, no
extras, no gaps (`B01_OneVoiceThenMany` through `B08_TheFramework`). This
pass closes the PROOF GATE for authoring.

**GATE P signed 09/07/2026 — build completed end to end.** Full pipeline
run: Kokoro audio (12 beats, ground truth), retiming, Manim 4K render,
Remotion bookends, 4K compile, captions, `./art shorts` derivation. See
below for the real defects this pass caught and fixed — none were caught
by the mp4-probe/manifest check alone; all came from actually reading
extracted frames per §6 of the channel `CLAUDE.md`.

## Post-audio retiming (Step 3)

Every beat came in shorter than its pre-audio `estimated_duration_s`
(Kokoro reads faster than the ~2.7 words/sec planning assumption), but
more significantly, the *scenes themselves* as first authored ran shorter
still than even those estimates — a low-quality pre-audio render measured
each scene at roughly 65-80% of its own `estimated_duration_s`. Every
Manim beat needed time **added** (7-17s each), the opposite direction from
STEM5's note about `self.wait()` overshooting. Fixed by scaling up 2-3 of
the longer holds near each beat's end (never dumping it all into one
hold), computed directly from `actual_duration_s - measured_-ql_duration`.
All 8 scenes landed within 0.3s of `actual_duration_s` after correction.

## Real defects found in mid-scene/frame QC (not caught by any automated check)

1. **B01** — the four agent-type labels beneath the microphones
   (`financial · competitive · patents · earnings calls`) collided into
   unreadable overlap. Root cause: `label()`'s legibility floor
   (`graphics_lib.py` `FLOOR = 24`) silently clamps any requested size
   under 24pt back up to 24 — the original `size=18` request was actually
   rendering at 24pt at the original `buff=1.1` mic spacing, too wide for
   four labels including the two-word "earnings calls". Fixed by widening
   mic spacing (`buff=2.0`) and shortening to single words instead of
   trying to shrink text below the floor.
2. **B08** — the checkmarks above each of the four framework rules
   rendered as blank tofu boxes instead of ✓ glyphs. Root cause: Montserrat
   (the font `label()` uses) has no ✓ glyph — exactly the gotcha
   `graphics_lib.py`'s own `checked()` docstring warns about, missed here
   by calling `label("✓", ...)` directly instead of `checked()` or plain
   `Text()`. Fixed by using `Text("✓", font_size=22, ...)`, which resolves
   to Manim's default font where the glyph exists.
3. **B02** — the two conclusion bubbles briefly sat almost fully
   overlapped at near-full size and opacity while converging on the
   blender, an illegible text collision caught in mid-scene QC (invisible
   in a final-frame check, since both bubbles fade out entirely by the
   settled frame). Fixed by having both bubbles shrink and fade
   *continuously* while moving to the blender's center in one animation,
   rather than parking side-by-side at near-full size first.
4. **short/B02_TheNaiveFix916** (portrait re-layout) — the top conclusion
   bubble, and separately the "Agent A — right / Agent B — wrong" column
   later in the same scene, both collided with the scene's title, which
   never fades out. Root cause: `title()`'s `to_edge(UP, buff=0.7)` puts
   its bottom edge around y≈2.75, and both elements were placed at
   y=2.6-2.7 without accounting for that persistent header. Fixed by
   pushing the whole vertical layout down (bubbles to UP\*2.1 and below,
   the column to UP\*1.9) to clear the title with margin.

All four were caught by actually reading extracted PNG contact sheets
sampled evenly across each clip's full duration (not just the final
settled frame), never by a render or compile succeeding — consistent with
the channel's "the mp4 probe has never once caught a real layout defect"
rule.

## 9:16 short — beat selection

`./art shorts` auto-dropped B01, B02, B03, B04, B06, B07 as the "cheapest"
combination under the cap, which would have opened the short cold on B05
("Two Outcomes" / resolved-unresolved) with no prior explanation of what
arbitration even is — an incoherent stand-alone narrative, the same
failure mode STEM5's own build notes flagged. Manually overridden via
`--drop B01 B03 B04 B05 B06 B07 B08` to keep B00 (cold open) + **B02 only**
(The Naive Fix, fully self-contained: averaging two agents' conclusions is
argued and shown wrong without depending on B01's reframe or B03-B07's
detection/arbitration mechanics) + B09/B10/B11 (verdict, handoff, outro) —
a complete arc: problem → one fully-illustrated argument → recap → task →
outro, at 124.3s (well under the 180s cap). B09's verdict card already
restates all four framework rules as text, so dropping B08 (the Manim
framework beat) specifically does not lose the framework message — the
same reasoning STEM5 applied when it dropped its own B09 Manim beat in
favor of its B10 verdict card. The auto-rewritten outro narration was
regenerated via Kokoro (`--no-gate`, since this is a mechanical re-cut of
already-GATE-P-approved content, not new material) after `shorts.py`
rewrote it to reference the cuts.

The portrait re-layout (`short/scenes.py`, `B02_TheNaiveFix916`) restacks
the parent's horizontal bubble-pair and 9-unit-wide number line into
vertical arrangements sized to the ~4.5-unit portrait frame width — see
"Real defects" above for the title-collision fix this required.

## Final status

16:9 4K master (`when-two-agents-disagree_DivijPawar_09-07-2026.mp4`,
3840×2160@30, 368.8s, captions muxed as `mov_text`) and 9:16 short
(`short/when-two-agents-disagree-short_DivijPawar_09-07-2026.mp4`,
1080×1920@30, 124.3s, captions muxed as `mov_text`) both compiled with
zero slates. Both passed frame-level visual QC across every beat,
including the Remotion bookends and a whole-video overview pass — no
`_qc/PROOF-REVIEW.md` self-review has been run yet against the full PROOF
rubric in `youtube/PROOF.md`; that's the recommended next step before
treating either file as ready to publish (even unlisted).
