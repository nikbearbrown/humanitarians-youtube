---
name: sri-explainer
description: >
  Chapter-to-video explainer in Prof Sridhar's own written voice. Give it one
  chapter of a Prof Sridhar book (e.g. `quantum-mechanics-vol1/chapters/`)
  and it builds a video that teaches what that chapter is about — narrated in
  a register derived directly from Sridhar's own textbook prose: cold-open
  historical hook, stepwise derivation beats that name what's not yet true,
  explicit ruling-out of edge cases before the real result, concrete
  physical-scale grounding, and golden-test honesty on every number shown.
  Extends the deep-explainer chassis (Claude bookends; vox/Manim/Remotion
  mix) for a multi-section chapter — the normal case — or the shorter
  ai-explainer arc when a chapter really is one mechanism end to end. Use
  when the user types `sri-explainer`, `sri [chapter]`, or hands over a
  chapter file (or pasted chapter text) and asks for a video/explainer of it.
  Register: Sridhar. Default channel claude-sri (persona Prof Sridhar; voice
  kokoro am_onyx, reused from claude-liam pending a dedicated voice). Body
  beats support two visual looks — the default cream/parchment palette
  (static camera, matching the other three explainers), or a dark
  "Notebook" look for when the human asks for a NotebookLM-style/dark/
  glowing/cinematic chapter video: gradient background, a static/locked-off
  camera on ordinary 2D beats, real 3D hero objects with camera orbit for
  any beat whose content is physically spatial (roughly a third of beats,
  not just the cold open), glowing accent curves, gridlined charts, bold
  sans titles, red box callouts — see reference/notebook-look.md. GATE P
  before any audio spend. Never publishes.
---

> **BRUTALIST (pared-down) EDITION.** This copy of the skill lives in the
> free-only `brutalist` toolkit. Kokoro is the ONLY TTS engine. The toolkit's
> `generate_audio_kokoro.py` currently ships exactly two voices — `am_onyx`
> ("Onyx") and `af_bella` ("Bella") — so `claude-sri` reuses `am_onyx` as an
> interim default (see "Persona & channel" below); giving Sri a voice of his
> own means extending `ALLOWED_VOICES` there first, which has NOT been done
> yet. GATE P remains in force as a QUALITY gate (narration review before
> audio), not a cost gate.

# sri-explainer — the chapter-to-video sibling

A sibling of `ai-explainer`, `cli-explainer`, and `deep-explainer` on the same
shared skeleton: Claude bookends, different SOURCE CONTRACT and a new
REGISTER. Where `ai-explainer` takes a concept and `cli-explainer` takes a
build, `sri-explainer` takes **one chapter** of a Prof Sridhar book and turns
it into a video that teaches what that chapter is about, written the way
Sridhar himself writes it.

## Lineage — what governs when

This skill EXTENDS `ai-explainer`, which extends `explainer` — nothing below
repeals a parent law; this file adds the genre's own contracts, the same way
`deep-explainer` does.

- **Chassis** → `../deep-explainer/SKILL.md` for a multi-section chapter (the
  normal case — a QM chapter runs 6–10 derivation sections plus grounding
  plus dynamics: genuinely multi-act). `../ai-explainer/SKILL.md`'s shorter
  arc for a chapter that really is one mechanism end to end. Same decision
  rule deep-explainer already states in its own "when this skill and when
  not" — applied here to a chapter instead of a concept.
- **Bookends, brand, laws** → `../ai-explainer/SKILL.md` governs unchanged:
  COLD OPEN LAW, ASK→RESULT LAW, ILLUSTRATE LAW, SHOW-DON'T-TELL LAW,
  SPARK-LINE LAW, REBUILD LAW, DOUBLE-CHECK LAW, FILL-THE-CANVAS, LOGO LAW,
  VISUAL QC LAW, HANDOFF LAW, OUTRO LAW, GATE P.
- **Closing block** → the `your-turn` skill's three-beat standard: VERDICT
  recap (`ClaudeVerdictArtifact`) → YOUR TURN prompt read in full
  (`ClaudeComposerAsk`, greeting `Your turn.`) → TITLE re-read
  (`ClaudeTitleOutro`).
- **How graphics are made** → `../explainer/` doctrine: MOTION.md,
  EQUATIONS.md (equation tangents — the default medium here, since a chapter
  is mostly derivation), REMOTION.md, the slot contract, the pantry law, the
  slate system.
- **Beat-mix, vox treatment, continuity, the two hard gates** → when running
  on the deep-explainer chassis, `../deep-explainer/SKILL.md` governs those
  in full (THE BEAT-MIX CONTRACT, vox-run continuity, Gate D1 previz, Gate D2
  shopping list) — this file does not restate them.
- **This file** governs: the chapter input contract, the Sridhar register,
  the derivation-compression rule, the persona/channel, and the
  handoff-from-the-chapter rule.

## When this skill (and when not)

Use `sri-explainer` whenever the source is **a chapter file from a Prof
Sridhar book** (`quantum-mechanics-vol1/chapters/*.md` today; any future
Sridhar book the same way) — not a bare concept, not a build, not a video
idea card. If the human wants a video about a *topic* without a chapter
behind it, that is `ai-explainer`; if about a *build*, `cli-explainer`. One
chapter in, one video out — never combine chapters into a single build
without being asked explicitly.

## Trigger

```
sri-explainer [chapter path]
```

Aliases: `sri [chapter]`. Also triggers on handing over a chapter file (or
pasted chapter text) and asking for a video/explainer of it.

`[chapter path]` is a chapter markdown file from a Prof Sridhar book, e.g.
`quantum-mechanics-vol1/chapters/05-the-infinite-square-well.md`.

## Persona & channel

| Slot | Value |
|---|---|
| Persona | **Prof Sridhar** — the book's own author voice, teaching the chapter directly. Not a Claude-workflow demo persona like Liam or HAI: Sridhar narrates in first person as the chapter's author, the way the book itself is voiced. |
| Channel key | `claude-sri` (new — added by this skill, not yet present in `ai-explainer`'s channel table or `brand_variant.py`) |
| Folder chip | `@HumanitariansAI` (`quantum-mechanics-vol1`'s publisher of record — see `book.md`) |
| Voice | Kokoro `am_onyx` — reused from `claude-liam` as an interim default. **Not yet wired into `generate_audio_kokoro.py` (`ALLOWED_VOICES`) or `brand_variant.py`'s channel table — do that as a follow-up before the first real build.** |
| Register | Sridhar (below) |

The Claude UI chrome (bookends) is unchanged from `ai-explainer` — this is
still a fidelity brand there; only the persona voicing the narration and the
source contract differ. The **body-beat palette** (the Manim GRAPHIC beats
in between) has two looks — see "Visual look" below.

## Visual look (body beats)

Two looks for the Manim GRAPHIC beats between the Claude bookends — the
bookends themselves (Remotion) never change look:

| Look | Palette | When |
|---|---|---|
| **Cream (default)** | `BG=#F2F0E9` `INK=#3D3929` `ACC=#D97757` `SOFT=#6E6A57` `GHOST=#A8A491` — see the existing reel `scenes.py` files | Use unless the notebook look is asked for. |
| **Notebook (dark)** | `BG_DARK=#14151A` `INK_LIGHT=#F5F5F0` `GLOW=#4DE8E0` `CALLOUT=#D9524F` `MUTE=#6B6E76` — full recipe: `reference/notebook-look.md` | Use when the human names this look, points at NotebookLM-style reference videos, or asks for "dark"/"glowing"/"chalkboard-style" visuals. |

The notebook look is a from-scratch Manim reproduction of both the *feel*
and the *craft level* of Google NotebookLM's Video Overview output — not a
call into that (proprietary, API-less) product, and not a literal pixel
copy of its photoreal rendering. It is more than a palette swap:

- **Gradient background** on every scene (never a flat single color).
- **`BaseScene` extends `MovingCameraScene` for API convenience, but
  ordinary 2D beats keep a static, locked-off camera** — no
  `self.camera.frame.animate` zoom/pan on a Write/FadeIn beat. This was
  tried both ways: no camera motion at all read as a plain palette reskin;
  a later pass added a zoom/pan to every single 2D beat and that was
  called out as gimmicky and reverted. Camera motion is earned by real 3D
  geometry, not added to a flat beat as a matter of course.
- **Real 3D hero objects with camera orbit** (`BaseScene3D`, a
  `ThreeDScene`) for every beat whose own content is a physical object or
  event in space — not just the cold-open hook. Across the two rebuilt
  reels, 5 of 16 GRAPHIC beats are full 3D (a heated block, a crystal
  lattice that both anneals and diffracts a beam, a photon-electron
  collision, an electron through a biprism); the rest are 2D with a static
  camera. Don't force 3D onto a chart/calculation beat just to have more of
  it — that reads as decoration, not craft.
- **Faint gridlines** on every `Axes` chart.
- Direct end-labeling on ≤3-series charts (stronger than a legend at that
  count); a real legend box only past ~4 series.

Full recipe, validated render notes, and the GOTCHAs discovered while
building it (fixed-in-frame backgrounds occluding rotating 3D objects;
Transform targets wrongly also added as their own fixed-in-frame mobject;
a constructed-but-never-`.play()`ed mobject silently dropping a caption;
Unicode superscript/subscript characters in `Text()` rendering as blank
boxes — use `MathTex` for any exponent/subscript instead; near-white text
placed on a light card/box being invisible, not just low-contrast) are in
`reference/notebook-look.md` — read it before writing a new `BaseScene3D`
scene or any label with an exponent/subscript, the gotchas are easy to
reintroduce by accident.
Whichever look is chosen, it applies to every GRAPHIC beat in the video —
never mix looks within one build.

## The Sridhar register

Derived directly from reading `quantum-mechanics-vol1` (the `chapters/` and
`griffiths/` variants) — not invented. Full writing-style doctrine, chapter
structure, and the golden-test discipline: `reference/prof-sridhar-style.md`.
The short version, split the way it must be applied:

- **Voice (sentence-level, carries into narration):** cold open on the
  chapter's own concrete scene, never "in this chapter we will…"; state what
  a result is NOT before affirming what it IS; short punch-sentences after a
  longer explanatory one; concrete physical-scale comparisons over abstract
  claims; numbers always anchored to something felt (an eV, a room-temperature
  $k_BT$), never a bare symbol.
- **Structure (maps to the beat spine below):** the chapter's own section
  order — hook → setup → derivation → grounding → (dynamics, if present) →
  bridge-forward — is the video's own act order. Don't reinvent an arc; adapt
  the chapter's.
- **Discipline (a DOUBLE-CHECK LAW sharpening, not a separate rule):** every
  number shown on screen carries its own check, spoken and shown — the
  ratio, limit, or conservation law it satisfies — mirroring the book's own
  golden-test law (`running-project-system-prompt.md`: never assert a result
  is "physically correct" without an independent check).

## The chapter → beat spine (default act structure)

Map the chapter's own sections onto acts — adapt to what the chapter actually
has, never pad to a template:

```
B00  cold open (ClaudeComposerAsk, ask answered, Sridhar signs in)
HOOK       the chapter's own opening scene (a real photo → vox beat with
           provenance sidecar, e.g. the STM quantum-corral image; otherwise a
           Remotion C3 illustration) — never invented, always the chapter's
           actual hook.
SETUP      the potential/problem as stated — equation on screen (Manim).
MECHANISM  DERIVATION-COMPRESSION LAW (below) — the 2–4 turns that actually
           decide something, each its own beat, bold-lead framed ("Can E be
           negative? …") the way the chapter itself frames it.
GROUNDING  the chapter's own worked numeric example — an on-screen
           counter/comparison, never a narrated number with nothing to look at.
DYNAMICS   only if the chapter has one (e.g. time evolution / sloshing) — a
           Manim animation of the actual physical behavior described.
VERDICT (ClaudeVerdictArtifact)   the chapter's ONE idea, restated plainly,
           with its golden-test citation.
YOUR TURN (ClaudeComposerAsk, "Your turn.")   HANDOFF-FROM-THE-CHAPTER LAW —
           drawn from the chapter's own "LLM Exercises" section, never
           invented fresh; read aloud and discussed per HANDOFF LAW.
OUTRO (ClaudeTitleOutro)   restates the chapter title + the book's handle.
```

On the deep-explainer chassis this spine expands to full acts (4–8 beats
each) under THE BEAT-MIX CONTRACT; on the ai-explainer chassis it compresses
to a single tight arc. Either way the ORDER above is fixed because it is the
chapter's own order.

## Hard rules (this skill's own, beyond the parents')

1. **DERIVATION-COMPRESSION LAW.** Never narrate all $N$ steps of the
   chapter's derivation verbatim — that is lecture-capture, not an explainer.
   Extract the 2–4 points where something is actually decided (the moment a
   continuous quantity collapses to a discrete one; the moment a boundary
   condition kills a term) and give each its own illustrated beat. This is
   ILLUSTRATE LAW applied to a physics derivation: one beat per genuine turn,
   never one beat per algebra line.
2. **GOLDEN-TEST-ON-SCREEN LAW.** Any number shown carries its own check,
   spoken and shown (the ratio/limit it satisfies) — sharper than the
   parent's generic DOUBLE-CHECK LAW because the book's own system prompt
   makes this non-negotiable: never assert a numeric result is physically
   correct without an independent, checkable comparison on screen.
3. **NEGATION-BEFORE-AFFIRMATION.** Mirror the book's own rhetorical move —
   state what a result is NOT before affirming what it IS, in the narration
   and, where it fits, on screen (a struck-through wrong reading replaced by
   the right one).
4. **HANDOFF-FROM-THE-CHAPTER LAW.** The Your Turn prompt is always drawn
   from the chapter's own "LLM Exercises" section (adapt, don't invent fresh)
   — the same instinct as `skill-teardown`'s SELF-DEMO LAW: use the source's
   own material as the demo.
5. **BRIDGE-HONESTY LAW.** The verdict states plainly what the chapter did
   NOT resolve and which future chapter does — matching the book's own "What
   Comes Next" honesty. Never imply the chapter closed a question it left
   open.
6. **One chapter, one video.** Never combine multiple chapters into a single
   build without being asked explicitly.
7. **NO-COLLISION LAW (custom Manim scenes).** When a beat's own Manim scene
   writes more than one on-screen text/label in the same screen region, the
   earlier one must be explicitly `FadeOut` (or `Transform`ed away) before the
   next is `Write`ten there — never leave a prior label sitting under a new
   one on a shared axis/region (this is what produced the illegible
   double-exposed text bugs the first time these scenes were built: a stale
   `poly_label` still on screen under a freshly written `anneal` line, and a
   `slope_label` parked at the same edge as the axis's own `frequency` label).
   Prefer placing an annotation in genuinely empty canvas space (e.g.
   `.move_to(ax.c2p(x, y))` into a quadrant nothing else occupies) over
   `to_edge` collisions with an axis/caption that's already anchored there.
   A label attached to a mobject that is later `.rotate()`d or `.shift()`ed
   (e.g. a scattered-ray line) must be (re)anchored with
   `.move_to(mobject.point_from_proportion(...))` AFTER those transforms, not
   `next_to` chained onto the pre-transform mobject — the fragile version
   drifts the label away from what it's labeling. VISUAL QC LAW's frame
   sample for a custom Manim beat must include one frame at the moment each
   new label appears, not only the beat's establishing frame, and any
   suspected math/rendering anomaly (e.g. a curve that looks like it dips
   where the underlying function can't) gets a zoomed crop check before it's
   called a bug — a compressed overview frame can make two crossing curves
   look like one dipping curve.

(COLD OPEN, ASK→RESULT, ILLUSTRATE, SHOW-DON'T-TELL, SPARK-LINE, REBUILD,
FILL-THE-CANVAS, LOGO, VISUAL QC, HANDOFF, OUTRO, one-terracotta,
never-publish, and GATE P — cited inline above — bind unchanged from
`ai-explainer`.)

## Workflow

1. **Read the whole chapter** — prose, every figure placeholder, the worked
   examples, the References, the Exercises, and (if present) the LLM
   Exercises / Running Project block. The video is built from what the
   chapter actually contains, not a summary of it.
2. **`plan`** — map the chapter's sections onto the beat spine above; mark
   which figures are real archival images (vox + provenance) vs. need a
   Remotion/Manim rebuild (REBUILD LAW governs); pick the 2–4 derivation
   turns (DERIVATION-COMPRESSION LAW); pick the LLM-exercise prompt for the
   handoff. Present the act map. **GATE: approve.**
3. **`factcheck`** — verify every number and named claim against the chapter
   itself (the chapter is the source of truth here, not an external check);
   strip nothing the chapter itself doesn't strip — this is Sridhar's own
   verified content, so the sharpening is completeness, not skepticism.
   `FACTCHECK.md` in the reel folder.
4. **GATE P** — narration reviewed on an animated slate. Then audio
   (Kokoro `am_onyx`, pending the dedicated-voice follow-up above).
5. **Audio lock → visuals → assemble** — same mechanics as
   `ai-explainer`/`deep-explainer` (Steps 3–5 there): audio-first conform,
   Manim/Remotion/vox fill per the beat spine, `compile.py`.
6. **Review cut → VISUAL QC LAW pass** (NO-COLLISION LAW governs custom Manim
   beats specifically — sample the label-appearance frame, not just the
   establishing frame, for each one). `BUILD-PROMPT.md` ships in the folder
   (a reel without its build prompt is unfinished).

## Output contract

```
[book]/youtube/claude-sri-[chapter-slug]/
  beat_sheet.json      the heart (schema: runtime/schema/beat_sheet.schema.json)
  BUILD-PROMPT.md      paste-ready end-to-end build prompt
  BUILD-LOG.md         decisions, MISSING: lines, gate signatures
  FACTCHECK.md         claim | verdict | chapter location
  SOURCES.md           chapter file + book edition, figure provenance, LLM-exercise source
  pantry/  media/  manim/  clips/  mp3/   (parent slot contract)
```

Slug convention: `claude-sri-[chapter-slug]` (e.g.
`claude-sri-the-infinite-square-well`), built into the OWNING BOOK's
`youtube/` folder — e.g. `quantum-mechanics-vol1/youtube/` — never into the
toolkit.

## Reference files (this folder)

- `reference/prof-sridhar-style.md` — the full writing-style doctrine
  extracted from `quantum-mechanics-vol1`: opening/structure/derivation
  rules, the golden-test law, the variant law, and the four-tier exercise
  system, with the video-narration translation for each.
- `reference/notebook-look.md` — the dark "Notebook" visual register: full
  palette, the glow-curve/callout-box/gradient-background/3D-hero-object/
  gridline Manim recipes (each validated by a real render, incl. several
  GOTCHAs found and fixed during that validation — 3D occlusion and
  Transform/fixed-in-frame bugs, a silently-dropped caption, Unicode
  super/subscript tofu-boxes, near-white-on-white text), the current
  static-2D-camera / 3D-orbit-only camera-motion rule, and what it
  deliberately does not reproduce from the source videos (photoreal PBR
  rendering, the literal NotebookLM engine).
