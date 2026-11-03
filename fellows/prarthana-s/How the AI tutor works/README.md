# How the Tutor Stays Grounded in Your Textbook

**Fellow:** Prarthana Ganesh Shetty
**Project:** Medhavy
**Series:** The Living Textbook — Episode 02

## What This Video Covers

Episode 01, *What Is Medhavy?*, said the tutor is grounded in the textbook. This
episode shows the machinery that makes that true.

The core idea: the tutor was never trained on the textbook and never will be. Every
time a student asks a question, the system searches the book, finds the passages that
match, and puts them in front of the model at that moment. Then it lets them go. The
model itself is rented, off the shelf, and unchanged.

That has a practical consequence for instructors, which is really what the video is
for: if the tutor gets something wrong about your book, it is almost never the AI that
needs fixing. It is the search, or the content, or a rebuild that was skipped — and all
three of those you can fix yourself, in minutes.

## How We Structured the Video

Ten beats, roughly three minutes, aimed at instructors and anyone onboarding a
textbook. No coding background assumed.

It opens on the puzzle — the tutor quotes your book accurately, but nobody trained it.
Then the whole answer in one breath, so the rest has something to hang on. Then a
side-by-side of the two ways a tutor could know a book, and which one Medhavy uses.

The middle follows a single question through the system: the four steps that run when a
student presses enter, then a pause that asks the viewer to guess where the book
actually lives, then the reveal — one file, one real chunk of it, and why a line of
labels has to exist.

It closes on a test the viewer can run themselves, and an honest recap that names the
cost as plainly as the benefit: a stale index gives no warning.

## How the Video Was Built

Brutalist workflow — `beat_sheet.json`, Kokoro narration in Bella (`af_bella`) at speed
0.9, and the Medhavy palette, matching episode 01 so the two read as one playlist.

Every scene used is a prop-driven Medhavy composition already registered in the toolkit:
`MedhavyTerminalAsk`, `MedhavyOpen`, `MedhavyTwoColumnCard`, `MedhavyConceptCard`,
`MedhavyPredictCard`, `MedhavyCodeBlock`, `MedhavyOutro`. All seven were checked
renderable before any beat was written, so the first compile is a complete cut rather
than a previz full of placeholder cards.

Episode 01's custom scenes (`MedhavyHook`, `GroundedTutor`, `MedhavyBookTutor` and the
rest) are hardcoded with no props — they were built for that episode's specific content
and cannot carry new material, so they are deliberately not reused here.

No two consecutive beats share a scene, which keeps the video from settling into one
layout the way the first draft of episode 01 did.

## Accuracy

Every factual claim traces to the actual product code, not to documentation — read on
2026-09-08 across `medhavi-quantum-volume-1`. Each claim and its source line is listed
in `SOURCES.md`, along with four things that were deliberately left out or scoped down.

Model names and version numbers appear nowhere in the narration or on screen. They date
a video quickly, and the episode's whole point is that the model is interchangeable.

## Main Files

- `beat_sheet.json` — narration, timing, and scene instructions
- `SOURCES.md` — every claim traced to a source line, plus corrections applied
- `CHECKS-REPORT.md` — the pre-compile gate report
- `mp3/` — Kokoro narration, ten beats, 3:02 total
