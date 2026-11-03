# Frictional log — `sri-explainer` skill

Append-only. Three dated entries follow, covering the build, the extension, and
the finalization. All three were written 2026-09-28, after the weeks they
describe, and are reconstructions — not contemporaneous notes.

---

## 2026-08-30 — building the skill

> Written 2026-09-28, after the week it describes.

- **Skill definition:** [SKILL.md](SKILL.md)
- **Register reference:** [reference/prof-sridhar-style.md](reference/prof-sridhar-style.md)

**What I was working on.** A fourth sibling on the explainer skeleton, taking a
textbook chapter as input and producing a video in Sridhar's own written voice.

**What I tried, and what I expected.** I expected this to be mostly a register
problem — swap the narration voice, keep everything else. I expected to reuse the
`ai-explainer` arc unchanged.

**Where it resisted, and what I did next.**

- **A chapter is not a concept, and the short arc broke on it.** `ai-explainer`
  assumes one mechanism you can walk end to end. A QM chapter is six to ten
  derivation sections plus grounding plus dynamics. The short arc kept forcing me
  to either drop sections or flatten them into a list. I re-parented the skill
  onto the `deep-explainer` multi-act chassis as the *normal* case, and kept the
  short arc only as the exception for a chapter that genuinely is one mechanism.
- **"Sridhar's voice" was not a real spec until I made it one.** My first attempt
  was imitation by feel, which is unreviewable. I went back to the prose and
  extracted five properties that can actually be checked against a draft — the
  historical cold open, derivation beats that name what is *not yet true*, ruling
  out edge cases before the result, physical-scale grounding, and golden-test
  honesty on numbers. Writing them down is what turned the register from a vibe
  into something a reviewer could fail.
- **Deciding what the skill must never do.** I set GATE P — narration reviewed
  before any audio is generated — and made the skill never publish.

**What Claude contributed, and what I accepted, changed or rejected.**

- Accepted: the lineage rule that nothing in this skill repeals a parent law, so
  the brand, bookends and ILLUSTRATE/SHOW-DON'T-TELL laws stay governed by
  `ai-explainer`. It keeps the four explainers consistent instead of drifting.
- Changed: the chassis. The first draft extended the short arc; I moved it to
  `deep-explainer` for the multi-section case.
- Rejected: imitating the register by example alone. Replaced with the five
  named, checkable properties.

**What I understand now, and what I still do not.** I understand that a "voice"
is only reusable once it is decomposed into properties someone else can verify.
I do not yet know whether the five properties are sufficient or whether a reader
familiar with Sridhar would still hear something off — nobody had reviewed it at
this point.

---

## 2026-09-06 — extending it, and the honest state of it

> Written 2026-09-28, after the week it describes.

- **Weekly report:** Week 14 (31 Aug – 6 Sep), logged 10 hrs on this thread.
- **Test builds:** [Chapter 1](../2026-09-02-claude-sri-why-classical-physics-failed/),
  [Chapter 2](../2026-09-02-claude-sri-matter-waves/)
- **Walkthrough recording (2 Sep):** in [Drive](https://drive.google.com/drive/folders/15BtMVhwD9_A7J0Pt2pc2DHLcuF9RWxl7)

**What I was working on.** Extending the skill and running it for real against two
chapters, plus recording a walkthrough of how it works.

**What I tried, and what I expected.** I expected the first real build to expose
gaps, and it did. I also expected — wrongly — that this week would end with the
skill delivered. It did not.

**Where it resisted, and what I did next.**

- **Two looks instead of one.** A single cream/parchment palette matched the other
  explainers but read flat for spatial physics content. Rather than replace it, I
  added the dark Notebook look as a second option with its own spec, including the
  rule that the camera orbits only on beats whose content is *physically spatial*
  — roughly a third of beats, not just the cold open. Keeping the camera static
  everywhere else was the part I had to be disciplined about; orbiting everything
  looks impressive and teaches nothing.
- **I did not send it for review.** The intros were finalized this same week and
  the outros went out for review, but the explainer stayed with me. It was
  self-reviewed only.

**What Claude contributed, and what I accepted, changed or rejected.**

- Accepted: the orbit-only-on-spatial-beats rule, and writing it into the spec as
  a proportion rather than a vibe.
- Accepted: keeping cream as the default so the four explainers still match by
  default, with Notebook as an opt-in for when a human asks for dark/cinematic.

**What I understand now, and what I still do not.** I understand that the
explainer's status was genuinely different from the intros' that week, and that
the intros being confirmed said nothing about the explainer. Recording them
separately was the right call. What I did not know was whether the register
survived contact with a reader who knows Sridhar — that was still unverified.

---

## 2026-09-13 — finalized, confirmed, committed

> Written 2026-09-28, after the week it describes.

- **Weekly report:** Week 15 (7–13 Sep), logged 9 hrs on this thread.
- **Confirmation:** professor reviewed and confirmed.
- **Commit:** skill committed to GitHub; hash not recorded.

**What I was working on.** Getting the skill from ongoing to delivered.

**What I tried, and what I expected.** I expected review to come back with
register corrections, since that was the part I was least sure of. It came back
confirmed.

**Where it resisted, and what I did next.** The friction this week was mostly
mine — after several weeks logged as setup, first-draft, self-verified and
ongoing, the temptation was to call it done on my own assessment. I sent it
instead and let the confirmation, not the self-check, be what made it final.

**What Claude contributed, and what I accepted, changed or rejected.**

Not recorded at the time, and I will not reconstruct it. On the branding thread
the pattern was Claude proposing and me revising (see
[the Brutalist pass](../2026-10-01-intro-outro-brutalist-pass/FRICTIONAL.md)),
but I cannot honestly claim the same split applied here without having logged it.

**What I understand now, and what I still do not.** I understand the difference
between self-verified and confirmed, and that only one of them closes a thread.

The commit hash was not recorded at the time.
