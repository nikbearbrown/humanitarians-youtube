# Beat Sheet (APPROVED — Gate P, 2026-08-31): "The Synonyms the Classifier Never Learned"

**Creator:** Sai Pranavi Jeedigunta | Weekly work report
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo, `scripts/regulatory-intel/`)
**Phase:** 2 — approved for narration lock / audio generation. Both FACTCHECK items resolved
2026-08-31: B06's "deliberate tradeoff" framing kept as drafted; the "eighteen" count confirmed
fine stated plainly. See `FACTCHECK.md`.

---

## Premise

**What this covers:** the fourth report in the Layer 1 hardening series — a partial fix, honestly
reported. After the B2 fix (the CFTC-classification report), 18 items across the two Google News
feeds still fell through to `'Unknown Source'`. Google News items carry no `dc:creator` field (the
fix that solved B2), so this needed a different approach: reading all 18 real titles and adding
feed-agnostic synonym keywords (`adviser`/`advisor`/`RIA`, `broker-dealer`/`Reg BI`) for the ones
that were genuinely recoverable from title text. Result: 10 of 18 recovered, live-verified,
zero unexpected reclassifications. The remaining 8 are honestly left open — this video's second
half is about that honesty, not just the fix.

**Why this one is different from the prior 3 reports:** those were each a clean, complete
before/after. This one is a **partial** fix with a real, reasoned remainder — some items are
genuinely unclassifiable from title text alone (generic overview pieces, or items about a
different regulator entirely, like the UK's FCA) without accepting a much higher false-positive
risk. That tradeoff was made deliberately, not glossed over.

**What this deliberately leaves out:** a fuzzier NLP/content-based approach to the remaining 8 is
a candidate for a future report, not this one — flagged as a real, explicit tradeoff (lower
confidence for more coverage), not pursued here.

**Source status:** Real engineering work. Every number below traces to
`/Users/pranavijs/mycroft/scripts/regulatory-intel/UNKNOWN-SOURCE-INVESTIGATION.md` (2026-08-30).
See `SOURCES.md` for the full claim → source mapping.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated |
| B03 Setup | Why the B2 `dc:creator` fix doesn't apply here (Google News has no `dc:creator`) | Legible before any live data shown |
| B04 Discovery | Two real title examples, one recoverable ("RIA"/"adviser") one not (different regulator/no named regulator) | Both shown together, contrast is the point |
| B05 Proof/Fix | Full before/after table, all 5 feeds, 18→8 total | All 5 feed rows visible, not just the improved ones |
| B06 Honest Limit | The 8 remaining items' two failure categories, named | Not glossed over — shown as a real, reasoned tradeoff |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi Jeedigunta |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "The Synonyms the Classifier Never Learned" + @HumanitariansAI. No narration.

**B01. Exec summary (~0:04–0:20)**
VO: "Hi, I'm Sai Pranavi Jeedigunta. This video is about eighteen items that were falling through
this pipeline's source classifier into 'Unknown Source' — and an honest partial fix that
recovered ten of them, while leaving eight open on purpose."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:20–0:32)**
VO: "Eighteen real items, live, still landing in a bucket called 'Unknown Source.' Last week's fix
didn't touch these — they don't have the field it relied on."
Visual: a feed list with 18 rows stamped "Unknown Source."

**B03. Setup (~0:32–0:52)**
VO: "Last week's fix worked because Federal Register items carry a real issuing agency in their
feed data. Google News items don't — they carry a publisher name instead, like 'Mayer Brown,'
which tells you nothing about which regulator the article is about. The classifier had to fall
back to reading the title itself, and it only knew a few phrases to look for."
Visual: side-by-side field comparison — Federal Register's `dc:creator` field (populated) vs.
Google News's `<source>` field (a law firm name, not a regulator).
*[Source: UNKNOWN-SOURCE-INVESTIGATION.md "Starting point"]*

**B04. Discovery (~0:52–1:18)**
VO: "I read all eighteen real titles. They split into two groups. Some just used a word the
classifier didn't check for — 'adviser' alone, or the acronym 'RIA,' or 'Reg BI.' Others had no
named regulator at all, or named a completely different one — one item was about the UK's
Financial Conduct Authority, which this pipeline doesn't even track. Calling that one 'Unknown
Source' isn't a bug. It's correct."
Visual: two title cards side by side — a recoverable example ("What Are Exempt Reporting Advisers
(ERAs)?") and a genuinely-not-recoverable one ("FCA Decision Notice...", UK regulator).
*[Source: UNKNOWN-SOURCE-INVESTIGATION.md "What was actually failing"]*

**B05. Fix + Proof (~1:18–1:48)**
VO: "The fix: two feed-agnostic synonym checks, added after the existing rules — one for
adviser-related language, one for broker-dealer and Reg BI language. I ran the updated classifier
against all five live feeds. Unknown Source dropped from eighteen to eight — ten recovered, zero
items that were already correctly labeled got reclassified."
Visual: results table, all 5 feeds, Unknown-Source-before and Unknown-Source-after columns,
18→8 highlighted.
*[Source: UNKNOWN-SOURCE-INVESTIGATION.md "The fix" and "Live verification (2026-08-30)"]*

**B06. Honest limit (~1:48–2:10)**
VO: "The remaining eight aren't a bug I missed. They're generic pieces with no named regulator, or
items about a regulator this pipeline was never built to track. Chasing those would mean guessing
from vague text — trading a small, real gap for a much bigger risk of mislabeling something with
false confidence. I left it open on purpose."
Visual: the two remaining-failure categories named on screen, with one real example title each,
NOT a promise of a future fix — framed as a documented, deliberate stopping point.
*[Source: UNKNOWN-SOURCE-INVESTIGATION.md "What's still open, and why this isn't a full close" —
NOTE for FACTCHECK: do not imply "will fix later," this was an explicit deliberate tradeoff, not
a TODO.]*

**B07. Takeaway (~2:10–2:25)**
VO: "Not every fix should chase a hundred percent. Sometimes the honest engineering call is
knowing exactly where to stop — and saying so."
Visual: statement card.

**B08. Sign-off (~2:25–2:30)**
VO: "Fixed with Claude Code — ten recovered, eight left open, on the record."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi Jeedigunta.

---

## Production Gate Self-Check (pre-review)

- [x] B03 explains why the B2 fix doesn't transfer, before any new fix is shown
- [x] B04's two example titles are real, quoted verbatim, not constructed
- [x] B05's table shows all 5 feeds, not just the 2 that changed
- [x] B06 frames the remaining 8 as a deliberate tradeoff, not an unsolved bug or a promise to fix later
- [x] Silent title card present; brand/fellow sign-off card present

**Runtime:** 131.6s measured (16:9 master), 136.1s (9:16 short, 9 beats + silent endcard) — real
Kokoro `af_bella` durations, per the toolkit's audio-first rule. Both under the ~150s target and
well under the 180s Shorts cap.

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-08-31. Both FACTCHECK open items
resolved (see `FACTCHECK.md`). Cleared to generate Kokoro audio and proceed to previz.

---

## Production complete — 2026-09-07

Audio generated and measured (Kokoro `af_bella`, all 9 beats + silent B00). `scenes.py` authored
(9 Manim scenes) and timed to measured durations. GATE A/W static pre-flight, GATE B post-render
layout audit, and GATE V frame-level visual QC all clean (0 BLOCKER/0 MAJOR on all 9 authored
beats) on both the 16:9 master (3840x2160, 131.58s) and the 9:16 short (1080x1920, 136.1s). See
`BUILD-LOG.md` for the full gate-by-gate record and `README.md` for the production-state summary.
