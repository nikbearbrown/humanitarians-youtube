# Frictional log — The Context Window Isn't Memory

*Drafted with Claude from the build logs; reviewed by me.*

## 2026-09-28 — first draft and sources

- **Drive:** https://drive.google.com/drive/folders/1sdOqDlg0ozhcLBl_1GrlOm84u4vkGuPX?usp=share_link
- **Folder:** [README.md](README.md) · [SOURCES.md](SOURCES.md) · [BUILD-LOG.md](BUILD-LOG.md)

**What I was working on.** A Claude explainer on context windows for students:
the window is a fixed token budget shared by the system prompt, tools, history,
the new message and Claude's reply, not memory. First draft: a 9-beat long cut,
154.5 s.

**What I tried, and what I expected.** I started from the toolkit's template
persona ("Liam, in for Bear", `@NikBearBrown`) and expected to change only the
names.

**Where it resisted, and what I did next.**
- The first draft said the oldest turns are always dropped when the window fills.
  Anthropic's *Context windows* page says the behaviour depends on the app: an
  error, a compaction summary, or a rolling first-in-first-out drop. I corrected
  the claim to that.
- The draft left Claude's own reply out of the budget; the docs count it. Added.
- Chart values in two beats were invented. They are now labelled `ILLUSTRATIVE`,
  and one axis uses abstract units so nothing reads as a measurement.
- One claim (code, numbers, jargon and non-English text cost more tokens per word)
  has no Anthropic source. I kept it and flagged it as inference in `SOURCES.md`.
- The rebrand was more than names: three toolkit files disagree on the HAI voice,
  and the locked Bear outro is only allowed on Bear's channel, so it had to go.

**What Claude contributed, and what I did with it.**
- Claude drafted the sources table, narration and beat sheet, and found the voice
  conflict and the outro lock in the toolkit docs.
- I chose Kokoro `af_bella`, and renamed the narrator from Liam to Bella so the
  on-screen name matches the voice: "Bella, in for Gomathy", `@HumanitariansAI`.

**What I understand now.** Behaviour at the limit is set by the application, not
the model; the draft's "always" generalized one app's behaviour; checking the
source caught it.

## 2026-09-29 — reworked to 60 seconds, 12 beats

**What I tried, and what I expected.** Cut the long cut to the first-project spec
(60 s, 12 beats) with the same thesis, facts and sources.

**Where it resisted, and what I did next.**
- The layer-stack scene has a fixed 30 s render, which can't finish inside a
  ~5 s beat, so it became two card beats.
- The worked example and the falsifiability beat are thinner than in the long cut.
  I disclosed both in `CHECKS-REPORT.md` rather than claim the arc still passes.

**What Claude contributed, and what I did with it.**
- Claude proposed the cuts and merges and logged each one in `SHOTLIST.md`.
- My instructions: put "context rot" back as one line; make the summary restate
  the thesis plainly; remove the on-screen inference tag on the token-density
  beat (the caveat stays in `SOURCES.md`).
- Pedagogy gate: PASS, as a fresh pass, since the long cut's verdict did not carry
  over to new content.

**What I understand now.** At 60 seconds every beat is a trade. Saying what was
cut is part of the work, not an admission of failure.

## 2026-10-01 — final 16:9 master

Final beat sheet and the 16:9 4K master (63.4 s), verified. Two open items are
justified in `BUILD-LOG.md`: the three-outcome list got its own card beat, and the
inference tag was removed at my direction.

**Where it resisted, and what I did next.**
- The final export's type check (GATE T) failed two components:
  - the scale chart's text was too small at 4K, so it became a card list;
  - the original outro had a colour collision between the handle and its pill, so
    it was replaced.
- I kept "often" in the card sub-lines so they matched the sources, rejected a
  toolkit edit, and removed the bar's accent colour instead.

## 2026-10-07 — the 9:16 version

**Where it resisted, and what I did next.**
- The review cut failed visual QC on every frame. The cause was the review
  overlays (timecode, beat label) running past masks sized for 16:9, not the
  content, so I gated the clean master instead and did not use lenient mode.
- Real defects still turned up and were fixed: a title above the title-safe line,
  an underfilled summary beat, a portrait card that crashed without icons,
  two-line labels that pushed titles out of frame, and terracotta status text
  that failed contrast at large size.
- Beats with no portrait component were rebuilt as native portrait Manim scenes.

**What I understand now.** 9:16 is a separate layout, not a crop, and a gate
failure has to be read before it is fixed: some are the content, some are the
check.
