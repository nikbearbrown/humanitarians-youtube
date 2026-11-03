# CHECKS-REPORT.md — engineering-the-ai-agent

Written before the first slate compile, per PROOF GATE (ai-explainer SKILL.md).
Covers the revised, 12-beat version of this reel (see PEDAGOGY.md's revision
note for what changed and why).

## Per-beat classification (SHOW / HOLD / CARD — nopunt SKILL.md)

| Beat | Class | Scene / pattern | Reason |
|------|-------|------------------|--------|
| B00 | SHOW | ClaudeComposerAsk (Remotion) | Cold-open bookend; the UI is the subject |
| B01 | SHOW | B01_TwoWaysToWriteCode (Manim) | Names a structural contrast — nopunt "two things compared, two-up aligned" |
| B02 | SHOW | B02_OrchestrationPatterns (Manim) | Names a second structural contrast — an uncertain fan-out vs. a fixed sequence |
| B03 | HOLD + SHOW | B03_ThePotholeCase (Manim) | The project's own real documentation photo (`assets/example-pothole.jpg`, MIT-licensed) is HELD on screen — a genuine archival photo of the actual project being covered, the strongest possible nopunt HOLD — while a bounding box and confidence chip SHOW/animate on top of it |
| B04 | SHOW | B04_TheContextGap (Manim) | Names a capability vs. a gap — nopunt "knows/doesn't-know" contrast, resolving to named tools |
| B05 | SHOW | B05_PipelinePerceptionTool (Manim) | Names an ordered sequence — nopunt "pipeline / ordered stages" row, with the active stages lit |
| B06 | SHOW | B06_PipelineGroundingAction (Manim) | Continues the same pipeline figure; names a database match and a filled-in artifact (the email) |
| B07 | SHOW | B07_TheGuardrails (Manim) | Names three parallel mechanisms, each demonstrating its own stopping behavior, plus the general method that derives them |
| B08 | SHOW | B08_TheAntiPattern (Manim) | Names a failure event (one wrong case in a field of right ones) — nopunt "panel of things, one singled out" |
| B09 | SHOW | ClaudeVerdictArtifact (Remotion) | Verdict bookend; recaps, asserts nothing new |
| B10 | SHOW | ClaudeComposerAsk (Remotion) | Handoff bookend; prompt typed, read aloud, discussed with rubric |
| B11 | SHOW | ClaudeTitleOutro (Remotion) | Outro bookend; title restate |

**11 SHOW / 1 HOLD+SHOW / 0 PUNT** (B03 upgraded from a drawn stand-in to a
genuine HOLD this pass — see below)

**Punt costumes identified in the source script and avoided** (unchanged
from the first pass): the Intro's dashcam pothole photo, Act 2's
phone-on-dashboard shot, Act 1's "AI Thought Bubble" cartoon, and Act 3's
stop-sign/shield icon. All rebuilt as drawn diagrams; logged in `SOURCES.md`.

**New in this pass — B08's dot field.** A 96-dot grid with one struck
terracotta is an abstract diagram illustrating "rare but real," not a
literal statistic or a stand-in for a real photograph — this is a legitimate
SHOW (nopunt's "panel of things, one singled out" pattern), not a PUNT,
because it isn't costuming a generic stock image as something specific; it's
an honest abstraction, and SOURCES.md explicitly declares it illustrative
rather than measured.

## Whole-sheet teaching-arc checklist

- [x] **FRAMEWORK beat(s)** — this reel now has **two** independent framework
  beats: B01 (the truth-table test, for finding the model's job) and B02
  (pipeline vs. agent loop, for choosing who controls sequencing). Both land
  before the case study or any mechanism beat.
- [x] **WORKED EXAMPLE** — B03–B08 walk one concrete system (Pothole
  Reporter) through both frameworks end to end: the unstructured piece and
  its blast radius (B04), the deterministic pipeline (B05–B06), and the
  guardrail method (B07). The example visibly *uses* the vocabulary from
  B01/B02 throughout rather than sitting adjacent to it.
- [x] **FALSIFIABILITY / edge-case beat** — **strengthened this pass.** B08
  is now a dedicated stress-test beat, separate from the mechanism beats: it
  doesn't show the pipeline working, it shows the specific way teams
  undermine it (skipping human review because the model is "usually
  right"), and states that this is exactly the failure mode B07's
  guardrails exist to catch. This is a stronger falsifiability beat than
  the first pass's B06 (guardrails), which had to do double duty as both
  mechanism and stress-test.
- [x] **SCAFFOLDED viewer task** — B10 ships a real, answerable prompt
  ("Where would a fixed pipeline be safer than an agent loop in my own AI
  feature?") plus a concrete 3-item rubric covering all three frameworks:
  run the truth-table test, choose pipeline vs. loop on purpose, derive one
  guardrail.
- [x] **Four bookends** — B00 (cold open), B09 (verdict), B10 (Your Turn),
  B11 (title-restate outro).
- [x] **No source, no verdict** — every claim-bearing beat carries its
  artifact on screen: the if/else-vs-hub diagram + truth-table caption
  (B01), the agent-loop-vs-pipeline split (B02), the drawn pothole and
  bounding box (B03), the knows/doesn't-know contrast + blast-radius label
  (B04), the lit pipeline stages with the GPS/geocode mechanism (B05), the
  database match and filling email (B06), the three guardrail mechanisms +
  the three-question caption (B07), the dot field and struck outlier (B08).
  B09 and B10 are exempt (they recapitulate).

**Teaching arc: FRAMEWORK ✓ (×2) | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
(strengthened) | SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓**

## Slate rules audit (Step 4b, automated)

Not yet run in this pass — run before generating audio:

```bash
/c/Users/divij/AppData/Local/Programs/Python/Python312/python \
  "/c/Users/divij/Desktop/mycroft/brutalist.art/runtime/qc/sheet_check.py" \
  "/c/Users/divij/Desktop/mycroft/accountability_layer/youtube/STEM4" --strict
```

Manual pre-check against `runtime/qc/slate_rules.json` limits (all beats):
`topic` "AGENTIC WORKFLOW DESIGN" (24 chars, ≤125 hard / ≤30 rec — clean on
both B00 and B10); `segment` "Engineering the Agent" (22) / "Explore Deeper"
(15) — clean; `greeting` "Olá, Divij" (10) / "Your turn." (10) — clean;
`handle` "@DivijPawar" (11, ≤100/~40) — clean; B11 `title` "Engineering the
AI Agent" (25, ≤48 rec) — clean; `subline` "Isolate the reasoning. Choose
the pipeline. Derive the guardrails." (68 chars) — over the tight ≤60
recommendation but well within the safe ≤110 2-line wrap range, same
category of soft overage as the first pass.

## Legibility contract (per beat)

Every SHOW beat names its on-screen artifact and every Manim beat carries an
ordered `show` block in `beat_sheet.json`. All 8 Manim scenes were smoke-
tested in two rounds:

**Round 1 (first authoring pass)** caught and fixed two real layout defects
before any full render:
1. B01 — the vertical divider extended the full frame height and pierced
   the landing serif line once it faded in. Fixed by fading the divider out
   with the left column's scratch content.
2. B01 — the "Memory" chip's corners touched "Tools" and "Action" at the
   original 1.5-unit spacing. Fixed by widening the spread.
3. B07 (then B06) — "national highway" / "local road" labels, positioned
   via `next_to(fork_line, DOWN)`, centered under the line's midpoint rather
   than its endpoint and overlapped into "nationalocal road highway". Fixed
   by anchoring each label under its branch's actual endpoint.
4. B07 (then B06) — "a person reviews, then presses it" was placed above
   the Send control and overlapped the "Human-in-the-loop" column header.
   Fixed by placing it below Send instead.

**Round 2 (this content-deepening pass)**, covering the two new scenes
(B02, B08) plus the re-verification of all renamed/edited scenes: both
still-frame tested (final state) and mid-scene tested (low-quality video,
frames extracted at 1-second intervals) specifically because B02's
dashed-line fan-out and B08's 96-dot field are the kind of dense,
many-element layouts that hide collisions in a final-frame-only check.
**No defects found** — dashed lines, the scaled-down pipeline row, the dot
field, and the diagonal callout arrow all render inside frame bounds with no
overlaps.

**Round 3 (this verification pass)**, covering the real-data rewrite of
B03, B04, B05, B06, and B07: still-frame tested all five after the content
changes. Found and fixed three defects, one of them **pre-existing since
Pass 2** and missed by that round's smoke test:

1. **B03** — moving the repo chip up to `y=2.6` to make room for the new
   photo asset put its box border directly through the "Pothole Reporter"
   title. Fixed by returning it to `y=2.15` and adjusting the photo/caption
   layout beneath it instead.
2. **B04 (pre-existing, missed in Pass 2)** — the arrow from the
   vision-model box to its output box was drawn between two mobjects that
   share an x-center with the "rain / night / any angle" row sitting
   between them; the arrow rendered directly through the word "night,"
   showing as a stray vertical mark. Not caught in Pass 2 because the
   still-frame check only samples final/settled frames closely, and this
   defect is subtle at a glance — caught on closer re-inspection this pass.
   Fixed by starting the arrow from the conditions row's bottom edge
   instead of the vision-model box's, so it no longer crosses any text.
3. **B07** — the new "hands off to official channel" two-line replacement
   for "terminate" was wider than the original word and, anchored at the
   fork's already-near-edge left branch (`x=-6.0`), ran past the frame's
   left edge. Fixed by narrowing the fork's spread (`x=-5.6`/`-3.6` instead
   of `-6.0`/`-3.4`) and shortening the text to "hands off — no guess."

One transient issue, not a code bug: an interrupted render (killed by a
tool timeout) left a corrupted cached SVG in `media/texts/`, which then
threw a `ParseError` on the next render attempt. Clearing `media/texts/`
(safe, regenerable scratch) resolved it immediately — logged here only so
a future agent recognizes the symptom and doesn't mistake it for a real
scene bug.

Full-video visual QC (compiled master, sampled frames) is still required per
Step 7 of BUILD-PROMPT.md once audio and final Manim renders exist — the
smoke tests above only catch static/mid-scene layout collisions, not
in-motion or retimed-hold issues, and B04, B06, and B07's longer runtimes
in particular should be re-checked once real audio duration is known.

## PPT test

No beat is a headline over a paragraph. Motion enacts the sentence in every
body beat, including the two new ones: an agent's tool calls fan out
uncertainly on dashed lines while a fixed pipeline sits lit and ordered
beside it (B02); a field of otherwise-identical dots holds one silently
different member that the narration then calls out by name (B08).

## Status

Beat sheet, gate docs, `scenes.py`, `graphics_lib.py`, and the real photo
asset (`assets/example-pothole.jpg`) are authored, internally consistent,
and all 8 Manim scenes have passed still-frame, mid-scene, and (for the
five scenes touched this pass) re-verification layout smoke tests across
three authoring passes. This pass closes the PROOF GATE for authoring,
including both the content-deepening revision and the live-repo
verification.

**Blocked on:** GATE P signature in `PEDAGOGY.md` (currently `VERDICT:
PENDING`). No audio may be generated until a human signs it.
