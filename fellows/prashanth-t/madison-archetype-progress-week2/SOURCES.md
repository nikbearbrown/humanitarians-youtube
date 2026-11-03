# SOURCES — madison-archetype-progress-week2

## What this reel is

A **design-stage progress update**, week two on the Madison brand-archetype
detector. The source is the project's own design work and the owner's current
status. Nothing here is a research finding, and nothing is a detector output.

## Continuity with week one

The first reel (`madison-archetype-progress`) reported a **scope**. This one
reports a **technical design** and a blocker. The Ruler-first decision and the
evidence-based / hybrid-aware / ends-in-application commitments carry over; this
reel does not restate them, it reports what turning them into a design produced.

## Names kept generic — a deliberate choice

At the project owner's instruction, no personal names and no internal tool names
appear on screen or in voice. The methodology is "the section-five methodology";
the next step is "design review" producing "a proper SDD". This is a presentation
decision, not a sourcing gap: the underlying work has named authors and tooling
inside the team.

## The illustrative material

Three things could be mistaken for results. All are labelled on screen:

1. **The Ruler copy phrases** (B02) — *heritage, mastery, by appointment* — are
   **constructed** for teaching. No real brand is named and no real copy is quoted.
2. **The scored output** (B06) — scores are `0.0` placeholders and the evidence
   quotes are invented. The file tab reads "design target, not produced" and the
   block closes `// NOT OUTPUT. This is the shape I am designing toward.`
3. **The evaluation branches** (B07) — `slideMeta` reads "illustrative — the test
   design, not a produced result". No evaluation has been run.

Plain register's move 4 requires one concrete running example, specific enough to
visualise; "a luxury brand" would not do the work, so a constructed-but-labelled
instance carries it.

## Claims about the design

| Claim | Basis |
|---|---|
| Inputs are published brand text, not a self-report questionnaire | Design decision, week two |
| Every trait score carries the line of copy behind it | Design decision — the auditability requirement |
| Evaluation uses a small hand-labelled brand set first | Design decision — the accuracy check |
| Distinguishing keyword-matching from voice-reading requires human labels | Follows from the method: without a reference label, agreement is uninterpretable |
| Blocked on sample data: format, count, owner | The owner's stated blocker |
| Next: design review → SDD → build and prove Ruler → then scale | The stated plan |

## Deliberately excluded

No model names or versions. No real brand named or quoted. No accuracy target or
figure. No timeline or ship date. No claim that the approach works — the reel
argues what an auditable output would look like and says plainly that producing one
has not started.

## Corrections applied during authoring

- **No real brand copy.** An earlier draft quoted a recognisable luxury brand's
  tagline. Replaced with constructed phrases: quoting a real brand would invite the
  reading that the detector had analysed it.
- **Scores shown as 0.0.** An earlier draft used plausible values like 0.86, which
  read as a result. Placeholders make the design-stage status unmistakable.
- **No design judgment.** Plain explains and stops. Lines rating keyword matching
  as lazy were cut; B07 states mechanically what keyword agreement would imply.
- **One inference flag only**, at B04, on whether published copy carries archetype
  signal at all — the project's real unknown.

## Determinism / seeds

| Beat | Seed or determinism note |
|---|---|
| B01 | `seed: "madison-week2-b01"` — same seed, identical typing performance forever |
| BOUT | polarity seeded by slug (`seedHash % 2`); no mascot, so no mascot seed |
| all illustration beats | pure functions of `useP()`; no `Math.random()`, no timers |

## Components

Reuse only — **no new components built, and none modified**. All ten were already
registered, confirmed RENDERABLE, and confirmed to re-time via `calculateMetadata`.
