# Fact-check gate

Status: **AUTHOR CONFIRMATION NEEDED** (see note below — this is not a normal external-source
fact-check)

## Why this file looks different from a typical FACTCHECK.md

Most fact-checks in this repository verify claims against public, independently-checkable
sources (a paper, a press release, a government dataset). This project has no such external
source: every claim is a first-person description of the author's own private n8n
workflow/Postgres database/dashboard. Nobody outside the author (Om Mali) can independently
verify that "the fix took this branch from zero working to nine of twelve," or that the specific
Bento/Show HN misattribution happened exactly as narrated — those are facts about a private
system, not public record. This table exists to make every such claim explicit so the author can
confirm each one against the actual system before publishing, not to imply Claude verified them
against an outside source.

| # | Claim | Beat | Verdict | Note |
|---|---|---|---|---|
| 1 | Buzz Score has four capped components: volume+engagement (30 pts), front-page impact (20 pts), acceleration (20 pts) | B06 | AUTHOR-ASSERTED | Confirm point weights match the current `Compute Buzz Score` node logic. |
| 2 | Story counts are log-scaled so one company's high story count doesn't dominate | B06 | AUTHOR-ASSERTED | Confirm this transform is actually present in the scoring code. |
| 3 | Acceleration is measured against yesterday's base score with yesterday's own acceleration stripped out | B06 | AUTHOR-ASSERTED | Confirm this isn't simplified/inaccurate relative to the real formula. |
| 4 | Cold start (no history) reads a flat zero for every entity | B06 | AUTHOR-ASSERTED | Confirm current behavior, in case this changed since the narration was written. |
| 5 | Community Opinion uses Llama 3.3 70B on Groq, chosen for speed since a full run makes 12+ calls | B09 | AUTHOR-ASSERTED | Confirm model name/version is still current at publish time. |
| 6 | An opinion built on fewer than 3 comments is flagged low-confidence | B04, B10 | AUTHOR-ASSERTED | Confirm threshold value (3) is still accurate. |
| 7 | Groq's strict JSON mode was rejecting quote-heavy comment text; the fix (drop strict mode, parse leniently, ask for paraphrases) took the branch from 0/12 to 9/12 working | B10 | AUTHOR-ASSERTED | This is a specific, falsifiable claim about a real bug — confirm the before/after numbers are accurate, not rounded for effect. |
| 8 | Early on, with every entity degraded, the model still confidently invented a sector narrative from nothing (before the `Has Usable Opinions` guard existed) | B11 | AUTHOR-ASSERTED | Confirm this describes a real observed failure, not a hypothetical. |
| 9 | A Show HN post for "Bento" (a slide tool) hit 1,000+ points while only name-dropping OpenAI and Anthropic in passing, and became the top story for both due to popularity-only ranking | B16 | AUTHOR-ASSERTED | Specific, checkable against the actual Postgres run row / HN thread — confirm the story name, point count, and which two companies were affected are all accurate as narrated. |
| 10 | Community Opinion rated both misattributed companies positively based on comments about presentation software, and the low-confidence guard (fewer than 3 comments) didn't catch it because 15 real comments existed | B17 | AUTHOR-ASSERTED | Confirm the comment count (15) and that this is the actual reason the guard didn't trigger. |
| 11 | The next scheduled fix is requiring the company name to appear in the story title itself | B17 | AUTHOR-ASSERTED | Confirm this is still the planned fix at publish time, not superseded by other work. |
| 12 | The system runs "end to end, every day" via a schedule trigger, covering 12 companies | B00, B01 | AUTHOR-ASSERTED | Confirm the pipeline is still live/scheduled and the entity count (12) is current at publish time. |

## What's already checked

`PEDAGOGY.md` (carried over from the original build) confirms narration structure, act order,
utility-framing lint, and a node-naming check (every workflow node named in narration is visible
in its corresponding screenshot) — all PASS. That's a structural/pedagogical check, not a
factual-accuracy check against an external source; it doesn't substitute for the author
confirming the 12 claims above.

## Before publishing

Every row above needs a human check mark from Om Mali specifically (not from a general reviewer),
since only the author has access to the real n8n workflow, Postgres data, and Groq usage this
narration describes.
