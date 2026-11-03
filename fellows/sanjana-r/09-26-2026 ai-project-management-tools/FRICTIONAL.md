# FRICTIONAL — AI in Your Project Management Tools (long + Short)

Process log for this reel, both cuts. Append-only: add new dated entries below;
never rewrite an earlier one. Not graded. Evidence lives beside this file — see
[BUILD-LOG.md](BUILD-LOG.md), [PROOF-REVIEW.md](PROOF-REVIEW.md), [SOURCES.md](SOURCES.md),
[FACTCHECK.md](FACTCHECK.md), [CHECKS-REPORT.md](CHECKS-REPORT.md), the beat sheets
(`beat_sheet.json` and `ai-project-management-tools-short/beat_sheet.json`), the scene
source (`scenes.py`, `ai-project-management-tools-short/scenes_short.py`), and the
deliverables (`AI-in-Project-Management-Tools__16x9_4K_YouTube.mp4` and the 9:16 in
`ai-project-management-tools-short/`).

---

## 2026-09-29 — building the reel (long + short) with Claude Code

**What I tried, and what I expected.**
- Wanted a Humanitarians AI Fellows video on AI in project-management tools (Jira,
  Trello, etc.), in the ai-explainer / Claude-background style, female voice, two
  cuts (a 4K YouTube long and a 9:16 Short), delivered locally, nothing pushed to
  GitHub, branded @HumanitariansAI, self-checked with PROOF.md.
- Expected it to run mostly like films 1–3: pick the topic, let Claude author the
  beat sheet + scenes, generate af_bella audio, render, QC, done. Expected the Short
  to be a quick re-slate of the long. Expected the toolkit to "just work" like last time.

**Where it resisted, and what I did next.**
- The topic isn't a framework by itself. Claude pushed back toward a *reusable*
  method instead of "5 AI features in Jira." Landed on **The Ticket Test**
  (mechanical? / reversible? / in the tool? → AI drafts & surfaces, a human decides
  & commits). Accepted that framing.
- The toolkit was a *fresh unzip* and several things were missing/changed, none of
  which happened last time:
  - The free Kokoro voice model was gone. → I approved re-downloading it.
  - The Remotion project had no `node_modules`. → `npm install` (189 pkgs).
  - A Windows `npx` patch had reverted. → re-applied.
  - A new build-safety gate demanded a recorded *human* voice approval. The
    auto-mode classifier **blocked** Claude from writing that record (flagged it as
    weakening a security control). → I approved af_bella in chat and authorized the
    record; only then did it go through. This one felt right — a machine shouldn't
    be able to self-approve the "a human signed off" field.
  - The toolkit special-cases beats named B04/B05/B06 for fellow-report reels (skips
    B04's audio, gates B05/B06). My reel isn't a report. → renumbered to a T-prefix.
  - `GATE F` refused the final until FACTCHECK / SHOTLIST / PROMPTS existed. → wrote them.
  - The @HumanitariansAI channel forces a fixed kicker string, "Irreducibly Human,"
    not a per-video topic (a lint caught it). → set it; re-rendered the composer beats.
- Rendering resisted the most. `GATE V` (frame-level visual QC) kept refusing the
  final for real reasons I could see once I looked at the frames: the BLUF text
  touched both edges; ticket cards collided with a title; a verdict box was clipped
  off the bottom; a couple of scenes were "underfilled" at the mid-beat sample
  because content revealed in sequence. → fixed each by looking at the actual PNGs,
  not the mp4 duration: shrank/reflowed type, redesigned the worked-example scene,
  and **front-loaded** reveals so a scrubbed mid-frame is already full. Paced every
  Manim scene so the audio-conform never slows it past ~1.3×.
- The outro shipped wrong: it said **@NikBearBrown**. The house `ClaudeTitleOutro`
  hardcodes that handle and a mascot and ignores the handle prop — there's an "outro
  lock" for a different channel. I flagged it mid-build. → Claude built a **custom
  @HumanitariansAI outro card** (for both cuts), and I had it re-audit every surface
  so no @NikBearBrown remained anywhere in the renders. A stale copy of the old outro
  also had to be deleted or it kept winning the slot.
- The Short specifically. 9:16 is a different layout, not a crop. The first portrait
  pass overflowed the safe area: the long composer segment titles ran off both edges,
  and the Ticket-Test scene was too wide (the red column bled off the right). →
  shortened the on-screen labels ("AI in PM Tools", "Run the test") and redrew the
  scene for a narrow-but-tall frame (everything inside x[-4.1, 4.1]); front-loaded
  the rows and the outro. The portrait composer beats then tripped a *bottom
  edge-bleed* I could not reproduce with frame-accurate analysis — the ink was inside
  the safe box, but the compiled candidate's frame sampling flagged it anyway. →
  declared those two composer beats `full_bleed` in the beat sheet (the toolkit's own
  per-beat waiver for full-frame UI plates), with a written reason. Compiled clean after.

**What Claude contributed — and what I accepted, changed, or rejected.**
- Claude did the technical build end to end for both cuts: framework design, beat
  sheets, the Manim/Remotion scenes, audio, the render pipeline, QC, and the write-ups.
- Accepted: The Ticket Test framework; the worked example + falsifiability case; the
  front-loading fix; the custom outro approach; the portrait `full_bleed` waiver
  (after Claude showed me the accurate analysis proving the frame was actually clean).
- Changed / directed: the topic (mine), the two-cut + local-delivery + no-GitHub
  constraints (mine), the voice (af_bella, mine and pre-approved), and the branding
  correction (I caught @NikBearBrown; Claude fixed it across both cuts).
- Rejected: the locked house outro (long and Short) — it couldn't carry our handle,
  so it was replaced, not reused.
- Every AI-generated number/example on screen is illustrative and self-authored; no
  external stats were invented (logged in SOURCES/FACTCHECK).

**What I understand now, and what I still don't.**
- Understand: the difference between the two Claude formats — this one (ai-explainer)
  teaches a concept with illustrations and a required hesitant-writer summary, vs the
  earlier build-with-code loop. That "audio is the clock" is literal: fix timing by
  regenerating audio and re-pacing scenes, never by hand. And that a Short is
  authored, not cropped — its own beat sheet and scene geometry.
- Understand better now: the QC gate is worth obeying — every time it refused, the
  frame really did have a defect I could see once I looked.
- Still open: why the portrait composer tripped a *false* edge-bleed in the compiled
  candidate when frame-accurate analysis showed it clean — I waived it with the
  toolkit's own `full_bleed` declaration, but I don't fully understand the encoder
  keyframe artifact behind it, and the 16:9 cut never hit it. Also open: whether a
  fresh unzip should ship with the Kokoro model + node_modules so the next fellow
  doesn't hit the same setup wall.
- Open for a next film: a second worked case in an *ambiguous* quadrant (mechanical
  but irreversible, e.g. AI bulk-closing stale tickets) to stress the "reversible?"
  axis harder.
