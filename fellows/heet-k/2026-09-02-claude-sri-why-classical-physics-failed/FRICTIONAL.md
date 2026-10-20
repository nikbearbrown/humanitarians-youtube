# Frictional log — Why Classical Physics Failed (QM Vol. 1, Ch. 1)

## 2026-09-02 — the skill's first real test build

> Written 2026-09-28, after the week it describes. Reconstructed from
> [beat_sheet.json](beat_sheet.json) and the Week 14 report; not a contemporaneous entry.

- **Drive:** https://drive.google.com/drive/folders/15BtMVhwD9_A7J0Pt2pc2DHLcuF9RWxl7
- **Beat sheet:** [beat_sheet.json](beat_sheet.json) — 14 beats, 228.4s
- **Skill:** [`sri-explainer`](../2026-08-24-sri-explainer-skill/)

**What I was working on.** Running `sri-explainer` end to end against a real
chapter for the first time. The beat sheet says so in its own `purpose` field:
"first real test build of the sri-explainer skill." The chapter was the natural
one — Chapter 1, the historical failure of classical physics.

**What I tried, and what I expected.** I expected the chapter's two big episodes —
the ultraviolet catastrophe and the photoelectric effect — to fall out as two acts,
and they did. What I expected to be easy was the pacing: I assumed I could estimate
beat durations from the narration text and get close enough.

**Where it resisted, and what I did next.**

- **Estimated durations were not close enough.** The beat sheet carries both
  `estimated_duration_s` and `actual_duration_s`, and they disagree — B00 was
  estimated at 22s and measured 17.7s. Eyeballed estimates drift by a fifth, which
  is enough to desync a Manim animation from the sentence it illustrates. I moved
  the build to `clock: narration` — generate the audio, measure it, and let the
  measured length drive the visual. The visual waits for the voice, never the
  other way round.
- **Two acts was a decision, not a given.** The chapter has more than two threads.
  Compressing to ultraviolet catastrophe + photoelectric effect meant leaving
  material out, and I chose coverage of two things properly over a tour of
  everything.
- **The golden-test rule cost me a beat.** The register requires honesty on every
  number shown, so the 10⁻²⁰ Rayleigh-Jeans/Planck ratio could not just be stated
  in passing — it got its own beat (B05, 19.6s) building the number on screen.
  That is 8% of the runtime spent on one ratio. I kept it, because the whole point
  of the register is that a number you cannot see derived is a number the viewer
  has to take on faith.
- **Verdict and handoff felt like overhead until they weren't.** B11 and B12 are
  40 seconds of a 228-second video with no physics in them. I nearly cut them.
  I kept them because the bookend structure is inherited law from `ai-explainer`
  and I had decided in the skill that nothing here repeals a parent law — including
  when it is inconvenient to me.

**What Claude contributed, and what I accepted, changed or rejected.**

- Accepted: narration as the clock. This is the single change that made the
  builds sync reliably.
- Accepted: Manim for all ten derivation beats and Remotion only for bookends and
  act cards — the split keeps the physics in a tool that can actually draw a
  diverging curve.
- Accepted: rendering both looks rather than choosing. I did not know which read
  better for this content and said so by shipping both.
- Changed: beat durations, all of them, from estimates to measured values.

**What I understand now, and what I still do not.**

I understand that "the clock" is a real architectural choice, not a setting.
Letting narration drive length removed an entire class of desync bug that I had
been planning to fix beat by beat.

I do not know whether the numbers are right. The golden-test rule makes me *show*
the derivation, which is not the same as verifying it — no FACTCHECK pass was run
on this build, and the 10⁻²⁰ ratio and the sodium worked example are asserted, not
checked against a source. I also do not know which of the two looks is better; I
shipped both because I could not decide, which is a deferral, not an answer.

*Partly answered 2026-10-17 — see the entry below.*

---

## 2026-10-17 — a factcheck was run

> Written 2026-10-17, well after the week it describes. Appended; the entry
> above stands as written.

Confirmed: **a factcheck was run** on this build. The entry above says the
numbers were "asserted, not checked against a source" and names that as the
thing it did not know. It was checked.

That matters for the register. The skill's fifth property is golden-test
honesty on every number shown — the 10⁻²⁰ Rayleigh-Jeans/Planck ratio and the
sodium worked example each got screen time on that basis. Showing a derivation
and verifying it are different acts, and the entry above was right to separate
them; this closes the second one.

**No FACTCHECK document was committed**, so the check happened but its record
did not survive. Same shape as the rest of this period: the work was done, the
artifact was not kept.

On the two looks: both were rendered and both shipped. No preference between
cream/parchment and the dark Notebook was recorded, and the question was never
put to a decision — the pair stands as the deliverable.
