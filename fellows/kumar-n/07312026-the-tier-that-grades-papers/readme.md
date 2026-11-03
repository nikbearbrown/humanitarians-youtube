# The Tier That Grades the Papers

**Channel:** Humanitarians AI (@HumanitariansAI) &nbsp;·&nbsp; **Format:** ai-explainer
**Runtime:** ~2.3 minutes &nbsp;·&nbsp; **Slug:** `sers-tier-framework`

## What this video is about

This is an explainer review of a machine-learning-for-SERS research paper
(the same paper covered in the `claude-liam-sers-ml-story` production --
see that video's own README for the writing-process story). Where that
earlier video is about *how the paper got rewritten*, this one is about
*what the paper actually argues* -- and uses one moment from that rewrite
process as its twist, not its subject.

**The paper's real contribution**, per this video: it isn't a new machine
learning method. It's a three-tier framework for grading whether a
published SERS-ML result is actually trustworthy:

- **Tier 1** -- multi-site, prospective validation. No published study has
  reached this.
- **Tier 2** -- strong proof-of-concept (independent cohort validation, or
  a very large single-site dataset). A small number of studies sit here or
  near the boundary.
- **Tier 3** -- hypothesis-generating only. Where most of the field's
  published work actually sits.

The video plots two real studies from the paper into this framework (Dong
et al., 95.81% accuracy across two independent cohorts, reaching Tier 2;
Huang et al., 97.33% accuracy on 66,000 spectra, sitting right on the
Tier 2/3 boundary because it's single-site) to make the tier system
concrete rather than abstract.

**The twist:** partway through, the video turns the paper's own grading
logic back on itself -- is the paper's *own writing* trustworthy? The
answer draws on a real editorial episode: a methodology section that
listed techniques without justifying them, read as possibly AI-generated,
flagged independently by two different people (a PM and a teammate) before
being fixed through an actual revision cycle, not just a polish pass. That
process -- diagnose, confirm independently, then genuinely fix -- becomes
a small real-world demonstration of the exact discipline the paper argues
the whole field needs more of. It closes as a single supporting line inside
the verdict, tied to Kumar's fellowship renewal -- it is deliberately never
the main subject of the episode.

## Structure (10 beats, ~2.3 min)

| Beat | Act | Component | What happens |
|---|---|---|---|
| B00 | ASK | ClaudeComposerAsk | Cold open -- frames the whole episode as a real test of the paper's framework |
| B01 | EXHIBIT | TierPyramidBeat | The empty three-tier scale is introduced, unplotted |
| B02 | GRADE-METHODS | TierPyramidBeat | Classical vs. deep learning methods compared against the field's actual (small) datasets |
| B03 | GRADE-TIERS | TierPyramidBeat | Real studies (Dong et al., Huang et al.) plotted into their tiers; no study reaches Tier 1 |
| B04 | PREDICT | PredictCard | Viewer commits to a guess before the twist is revealed |
| B05 | TWIST | TierPyramidBeat | The paper's own draft had an unjustified, possibly AI-written section -- caught, then independently confirmed |
| B06 | GRADE-FIX | TierPyramidBeat | The actual fix cycle: first pass still flawed, second pass clean -- rigor, not polish |
| B07 | VERDICT | ClaudeVerdictArtifact | One-page recap; the renewal line appears here only |
| B08 | HANDOFF | ClaudeComposerAsk | "Your turn" -- a prompt template for grading any paper's own trustworthiness |
| B09 | OUTRO | ClaudeTitleOutro | Title restate |

## Visual system

Two palettes are deliberately in play:
- **Claude skin** (cream, ink, terracotta) for the UI-pattern beats: B00,
  B07, B08, B09.
- **Humanitarians AI palette** (cream #F3EBDD, ink #2F2A26, teal #1F4E5F
  for validated/confirmed, crimson #E4572E for red-flag/unresolved, slate
  #29335C for structure, gold #F3A712 reserved for highlight-only) for the
  TierPyramid exhibit itself: B01-B03, B05-B06.

This is intentional, not inconsistent: per ILLUSTRATE LAW, the pyramid
exhibit gets its own visual language because the pyramid framework *is*
the artifact under review, not a UI chrome element.

## Files in this folder

| File | Purpose |
|---|---|
| `beat_sheet.json` | The full beat-by-beat script and Remotion prop configuration |
| `scenes.py` | Stub file -- this reel has no Manim beats; see the file's own docstring |
| `PEDAGOGY.md` | Act-structure and evidence-discipline sign-off (VERDICT: PASS) |
| `FACTCHECK.md` | Every factual claim in the narration, checked against the source paper and internal team reports |
| `NARRATION-GATE-P.md` | The narration script as originally submitted for human sign-off before audio generation |
| `BUILD-PROMPT.md` | The original Claude Code build prompt used to construct the `TierPyramidBeat` component and render this reel |

## Provenance note

Every dataset figure quoted in this video (95.81%, 382/1,582 patients,
66,000 spectra, 22 factories, 97.33%) is taken verbatim from the source
paper -- see `FACTCHECK.md` for the exact section references. No numbers
in this script were invented or estimated.
