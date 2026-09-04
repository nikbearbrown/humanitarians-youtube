# CHECKS-REPORT.md — autonomy-vs-control

Written before the first slate compile, per PROOF GATE (ai-explainer SKILL.md).

## Per-beat classification (SHOW / HOLD / CARD — nopunt SKILL.md)

| Beat | Class | Scene / pattern | Reason |
|------|-------|------------------|--------|
| B00 | SHOW | ClaudeComposerAsk (Remotion) | Cold-open bookend; the UI is the subject |
| B01 | SHOW | B01_TheBet (Manim) | Names three escalating quantities — nopunt "magnitudes on one axis" / stat-chip row |
| B02 | SHOW | B02_BlastRadius (Manim) | Names a part-to-whole spread — nopunt "concentric / scale" figure, drawn on cue |
| B03 | SHOW | B03_ThreeModels (Manim) | Names a ladder of three tiers — nopunt "ladder / tiers / hierarchy" row |
| B04 | SHOW | B04_TheTradeoff (Manim) | Names two plotted curves — nopunt "trend / scaling curve → axes + plotted curve" row |
| B05 | SHOW | B05_SpeedAndVisibility (Manim) | Names three bounded precedents + a two-timeline comparison — "panel of N things" + "two things compared, two-up aligned" |
| B06 | SHOW | B06_TheQuestion (Manim) | Names a measured extent (rope vs. reach) with gates placed along it — animated scale figure |
| B07 | SHOW | ClaudeVerdictArtifact (Remotion) | Verdict bookend; recaps, asserts nothing new |
| B08 | SHOW | ClaudeComposerAsk (Remotion) | Handoff bookend; prompt typed, read aloud, discussed with rubric |
| B09 | SHOW | ClaudeTitleOutro (Remotion) | Outro bookend; title restate |

**10 SHOW / 0 HOLD / 0 PUNT**

**The one place this reel could have punted, and didn't:** the source
script's B05 called for "three quiet images — a company credit card, an
autopilot switch, a power-of-attorney document." Those are generic objects
standing in for concepts, which is a PUNT costume under nopunt, not a HOLD —
only a *genuine archival photograph of a real person, place, document, or
event* qualifies as a legitimate HOLD. All three are rebuilt as drawn line
marks, each stating its actual bound. Logged in SOURCES.md.

**Other punt costumes avoided:** the dark-door title card (rebuilt into B06's
rope figure; the question survives as the B09 subline) and the greyed/green
send control (retinted to activation + label, since green is not in the
Claude palette).

## Whole-sheet teaching-arc checklist

- [x] **FRAMEWORK beat** — B02 establishes blast radius as the measuring
  instrument, on a physical example first (bulb / room / building), then
  transfers the same rings onto AI permissions. It lands **before** the three
  control models in B03 and before the worked example in B04.
- [x] **WORKED EXAMPLE** — B04 walks one financial agent across all three
  tiers (shows spending → drafts a payment → pays automatically) with the
  tradeoff curves and the tier axis on screen throughout. The example visibly
  *uses* the framework rather than sitting adjacent to it.
- [x] **FALSIFIABILITY / edge-case beat** — B05 is the dedicated stress test,
  and it attacks the reel's own most reassuring move. It grants the "humans
  have always delegated with bounds" analogy in full across three real
  precedents, then finds the single axis where it breaks: there is no
  catchable interval between an agent's decision and its action. The framework
  survives, but only after being genuinely tested. A full beat with its own
  two-timeline comparison, not a caveat in passing.
- [x] **SCAFFOLDED viewer task** — B08 ships a real prompt ("Map the blast
  radius of every permission I've granted an AI agent") plus a 3-item rubric:
  every permission classified read/approve/act / names what physically moves
  if it fires wrong / names the concrete loss on the riskiest one. It also
  names a failing answer to reject (a feature list instead of a blast radius).
  **See the note below — this item carries a deliberate tension.**
- [x] **Four bookends** — B00 (cold open), B07 (verdict), B08 (Your Turn),
  B09 (title-restate outro).
- [x] **No source, no verdict** — every claim-bearing beat carries its
  artifact on screen: the three stake marks (B01), the concentric rings
  (B02), the three lit markers (B03), the two curves and the walked agent
  (B04), the precedent cards and paired timelines (B05), the rope and its
  gates (B06). B07 and B08 are exempt (they recapitulate).

**Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓ |
SCAFFOLDED TASK ✓* | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓**

### * The SCAFFOLDED-TASK tension (flagged, not silently passed)

Source ¶14, preserved verbatim at B06, explicitly refuses a checklist: *"Not
a rule. Not a checklist, this time."* HANDOFF LAW and this checklist both
require one.

**Resolution taken:** the refusal stays exactly where the author put it — in
the body, as the reel's close. B08 then hands the viewer an instrument for
reaching their own conclusion rather than a rule to adopt. The video declines
to tell you what to conclude and gives you the means to conclude it.

Per the PROOF GATE, this is recorded rather than silently passed. If the
human prefers the stricter reading of the author's intent, drop B08's rubric
and log the resulting SCAFFOLDED-TASK violation in `BUILD-LOG.md`. Full
discussion in `PEDAGOGY.md`; the GATE P signature settles it.

## Slate rules audit (Step 4b, automated)

`runtime/qc/sheet_check.py` — **clean, 10 beats, no findings**, including
under `--strict`. Every non-wrapping field is inside its hard limit and every
wrapping field is inside its *recommended* count.

## Legibility contract (per beat)

Every SHOW beat names its on-screen artifact and every Manim beat carries an
ordered `show` block. Scenes hold ~15–35% negative space; un-highlighted
elements stay at INK/SOFT and are never dropped below GHOST. B03 holds all
three markers on screen simultaneously once lit, B04 holds both curves for
the full comparison, and B05 holds both timelines aligned on one shared axis.

**B03 is the longest beat in the series (~62s).** It holds a single idea —
the three-point control spectrum — across three markers, so one-idea-per-beat
is satisfied. If it reads long on the animated slate at GATE P, the natural
split is noted in `PEDAGOGY.md`.

## PPT test

No beat is a headline over a paragraph. Motion enacts the sentence in every
body beat: stake marks growing as the bets escalate (B01), rings drawing
outward then redrawing as permissions (B02), an agent mark stopped by a
boundary then released by a human press (B03), a risk curve staying flat and
then bending on the spoken word (B04), two timelines where one has catchable
gaps and the other collapses to a single tick (B05), a rope extending while
its reach ring grows with it (B06).

## Status

Beat sheet, gate docs, and `scenes.py` are authored and internally
consistent. This pass closes the PROOF GATE for authoring.

**Blocked on:** GATE P signature in `PEDAGOGY.md` (currently `VERDICT:
PENDING`). No audio may be generated until a human signs it — and for this
reel, the signature also settles the B06/B08 question above.
