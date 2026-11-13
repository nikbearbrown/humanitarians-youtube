# Frictional log — Madison: week two, technical design

2026-09-24 — making the Madison week-two progress update

* Video / Drive: https://drive.google.com/drive/folders/1fJAA92dC6Rvwrlc5mhOTIM0Pl8g6m9sp?usp=drive_link

What I was working on. A ~195-second progress update covering the week's actual
output: turning the section-five methodology into a concrete technical design for
the Ruler archetype, across inputs, scoring and evaluation. Also naming the
blocker — sample data — and the next step. Fourteen beats, reuse-only.

What I tried, and what I expected.

* I expected a design-stage update to be thinner than a build update, and worried
  it would have nothing to show.
* I expected to compile this one without the review footer, straight to a clean
  master.
* I expected the reused components to behave, since this was the fourth build.

Where it resisted, and what I did next.

* A design is showable, but only if it is specific. Vague design talk would have
  been worse than no video. What made it work was committing to the three parts
  on screen — what text goes in and in what format, how a trait score carries
  the quoted line that earned it, and how a hand-labelled brand set
  distinguishes reading voice from matching keywords.
* The keyword question turned out to be the spine. A luxury brand can read
  unmistakably Ruler and never use the word "luxury" — its copy says heritage,
  mastery, by appointment. That single observation justifies the whole evaluation
  design, so I planted it as a prediction early and paid it off later rather than
  asserting it.
* Compiling without the review footer failed outright, twice. Dropping that flag
  switches to the master path, which runs a hard visual gate and writes nothing
  if the gate objects. The first attempt found two genuine blockers: my
  right-hand branch text was long enough to run past the title-safe edge of the
  frame. That was my text, not the component — the equivalent text in the
  previous video was a third the length. Shortened and re-rendered; blockers
  cleared.
* The second attempt still refused, on ten lower-severity "underfill" flags
  spread across shared components — a centred-text beat, a chip grid, the verdict
  page. Those are the components' own layouts, used by other reels, so clearing
  them is not a change I should make unilaterally for one video. The cut was
  produced on the review path with the footer suppressed instead, which is
  visually identical.
* Worth recording that attempting the stricter path was still the right call: it
  is the only reason the edge-bleed blocker was found at all. The easier path
  would have hidden it.

What Claude contributed, and what I accepted, changed or rejected.

* The design is mine — the three-part structure, the auditability requirement,
  the evaluation approach and the scoping decision. Claude drafted the beat sheet
  and narration from it and built the reel.
* Accepted: labelling the scored output as a design target with placeholder
  values rather than plausible-looking numbers. Realistic scores would have read
  as results.
* Accepted: fixing the blocker rather than routing around it, then reporting
  honestly that the remaining flags were not mine to fix.
* Changed: kept collaborator and internal tool names out of the video. The
  methodology is referred to generically and the next step as "design review",
  since this publishes to a channel outside the team.
* Rejected: putting a timeline in. There is no basis for one at design stage and
  it would date the video immediately.

What I understand now, and what I still do not.

* Understood: an unauditable score is not evidence. That is the one sentence the
  video closes on, and it is the reason every trait score in the design carries
  the line of copy behind it.
* Understood: evaluation comes before scale. Proving one archetype end to end is
  worth more than twelve archetypes nobody has tested, which is why Ruler is
  first and the other eleven are explicitly not scheduled.
* Not understood: what the sample set actually needs to be — format, size, and
  who assembles it. This is the blocker, and no accuracy claim is quotable until
  it is resolved.
