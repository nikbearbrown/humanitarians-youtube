# Om Mali

Om Mali is a Humanitarians AI fellow. Unlike the `fellows/maya-r/` series, which is explicitly a
**fictional** demonstration, these are **real** weekly research reports.

Each episode folder begins with `YYYY-MM-DD` and summarizes that week's actual work. Reports
document the author's own projects; no accomplishment, metric, or result is invented — see each
report's `FACTCHECK.md` for what still needs the author's own confirmation before publishing.

Om Mali selected the Kokoro voice `am_onyx` for this report series and keeps it across weekly
reports, per the male-coded-name default described in the top-level `fellows/README.md` (a
fellow's own stated preference always overrides that name-based suggestion — this is the fellow's
actual, already-recorded choice, not an unconfirmed guess).

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Om Mali

This folder organizes **5 video projects** built around beat sheets. Each project README explains
the subject, supplies research and fact-check prompts, and documents the free local rebuild
workflow.

## Rebuild toolkit

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Brutalist is audio-first and local: the beat sheet drives narration, measured audio becomes the
clock, generated visual beats compile immediately, and unavailable media remains as labeled
slates until a human fills the pantry. The human conducts, watches, fact-checks, refines, and
decides whether anything is published.

## Projects in this folder

*(The Private AI Valuation Agent runs as a weekly series from 2026-08-08 onward — same channel,
same persistent voice, same ai-explainer spine each week.)*

- [2026 07 27 Building Buzz Tracker Dashboard](./2026-07-27-Building-Buzz-Tracker_Dashboard/)
- [2026 08 01 Creating Signal Endpoint](./2026-08-01-Creating-Signal-Endpoint/)
- [2026 08 08 Verifying Private AI Valuations](./2026-08-08-Verifying-Private-AI-Valuations/) — *week 1. Built with brutalist.art (`ai-explainer` / `claude-hai`), 10 beats, 2:35, 3840×2160. GATE P signed, all 20 FACTCHECK rows confirmed, GATE V clean. The earlier 6-beat static cut is archived at `_previous-build/`.*
- [2026 08 15 Bulk Ingestion at Scale](./2026-08-15-Bulk-ingestion-at-scale/) — *week 2. 11 beats, 3:00, 3840×2160. GATE P signed, GATE L + GATE V clean, 20 FACTCHECK rows traced (row 16 is derived, not quoted). The three week-2 figures and their SVG sources now live in this folder's `pantry/`, moved out of the Mycroft working tree.*
- [2026 08 22 Entity Resolution and the Golden Set](./2026-08-22-Entity-resolution-and-the-golden-set/) — *week 4 (there is no week 3 episode). 12 beats, 3:22, 3840×2160. GATE P signed, GATE L + GATE V clean, 20 FACTCHECK rows traced (read 2, 12 and 16). The episode argues against its own author in three places — a precision loss, an approved label overturned, and a limit no threshold fixes — and keeps all three.*
- [2026 08 28 Measuring a Local LLM Against the Matcher](./2026-08-28-Measuring-a-local-LLM-against-the-matcher/) — *week 5. 12 beats, 3:35, and the first episode shipped in **both orientations** — 3840×2160 and 2160×3840, re-laid-out rather than cropped, from one set of components and one set of narration files. GATE L + GATE V clean, GATE P signed, 20 FACTCHECK rows traced (read 3, 9, 13 and 18). A **negative result**: a local 8B model was given exactly what the deterministic matcher gets, lost 5.1 points of precision, and was not adopted. The plan pre-committed to that outcome before the model was run, which is the only reason the finding is worth anything.*
- [2026 09 04 Building the Human Review Queue](./2026-09-04-Building-the-human-review-queue/) — *week 6. 12 beats, 3:21, in **both orientations** — 3840×2160 and 2160×3840, re-laid-out rather than cropped, from one set of components and one set of narration files. GATE L + GATE V clean, GATE P signed, 20 FACTCHECK rows traced (read 6, 12, 18 and 19). The queue resolved 78% of 5,806 holdings unaided and stopped at the rest — 42 cards that were only 8 real questions. The episode's central claim is a **subtraction**: the software routed, grouped and presented, and decided nothing. Reading the rendered frames caught the reel contradicting itself (the three price steps are not the same magnitude) and two source lines citing a file that did not contain the claim.*

<!-- END BRUTALIST REBUILD GUIDE -->
