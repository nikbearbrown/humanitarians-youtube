# Machine Learning for SERS: From a Draft to a Real Paper

**Channel:** claude-liam &nbsp;&middot;&nbsp; **Format:** deep-explainer
**Runtime:** ~5 minutes &nbsp;&middot;&nbsp; **Slug:** `claude-liam-sers-ml-story`

## What this video is about

This video is a chronological account of turning a hollow, AI-generated
literature-review draft on machine learning for SERS (Surface-Enhanced
Raman Spectroscopy) into a rigorously cited research paper. It walks
through the actual editorial process, in order: identifying what was
wrong with the first draft, building a guidelines document to fix it,
dividing the work, running a repeating two-week research-then-rewrite
cycle across five weeks, and the specific citation, data-leakage, and
honesty corrections that resulted.

The throughline is a simple distinction: a draft can read as complete
while only *defining* its subject matter, without ever *explaining* why
any of it matters or what to do about it. Closing that gap -- forcing
every section to answer what's been done, why it works or fails, and
what to recommend -- is what the five weeks of rewriting were actually
spent on.

## Structure (14 beats, ~5 min)

| Beat | Act | Component | What happens |
|---|---|---|---|
| B00 | ASK | ClaudeComposerAsk | Cold open -- frames the whole rewrite process as the subject |
| B01 | BLUF | BrutalistHesitantWriter | States the core distinction: a draft that looked complete was actually hollow |
| B02 | THE PROBLEM | Manim (`B02_TheProblem`) | The original draft's disconnected sections and unreliable references |
| B03 | THE FIX | Manim (`B03_TheFix`) | The guidelines document's three forced questions |
| B04 | THE SPLIT | Manim (`B04_TheSplit`) | How the paper's sections were divided between two co-authors |
| B05 | THE RHYTHM | Manim (`B05_TheRhythm`) | The real five-week timeline and weekly workload |
| B06 | ALIGNMENT & LEAKAGE | Manim (`B06_LeakageDiagram`) | The correct vs. incorrect order for fitting PCA, and why it matters |
| B07 | SERS-SPECIFIC EVIDENCE | Manim (`B07_HotspotEvidence`) | Two real findings: hot-spot variability as signal, and cross-instrument drift |
| B08 | THE CONDITIONAL CALL | Manim (`B08_ConditionalEnsemble`) | When model ensembling helps versus actively hurts |
| B09 | THE HONEST CUT | BrutalistHesitantWriter | Removing an unsupported number and replacing it with an honest "this hasn't been measured" |
| B10 | THE TABLE FIX | Manim (`B10_TableFix`) | Three live corrections to the paper's summary table |
| B11 | VERDICT | ClaudeVerdictArtifact | One-page recap of the whole rewrite process |
| B12 | HANDOFF | ClaudeComposerAsk | "Your turn" -- a prompt for auditing your own writing's citations |
| B13 | OUTRO | ClaudeTitleOutro | Title restate |

## Evidence discipline

Every dataset figure and citation named in this video is drawn from the
actual source paper and its real supporting literature -- nothing is
invented or estimated:

- The PCA data-leakage warning cites Savorani (2010) and Liu (2017).
- The hot-spot variability finding (an 84.8% error reduction from training
  on deliberately varied conditions) cites Zhao et al., 2025.
- The cross-instrument calibration drift finding (35 instruments across
  15 institutes) cites Guo et al., 2020.
- The ensemble comparison uses real reported accuracy figures (97.9%,
  97.4%, 76.1%), with the underperforming case explicitly labeled as
  drawn from a preprint.
- The PLSR citation gap fix cites Hou et al., 2016.

Where the original draft's own claims could not be sourced -- such as a
specific "10 to 30 percentage point" performance-gap figure -- the video
shows that number being removed and replaced with an honest statement
that the gap has never actually been measured, rather than repeating an
unsupported figure.

## Files in this folder

| File | Purpose |
|---|---|
| `beat_sheet.json` | The full beat-by-beat script and Remotion/Manim configuration |
| `scenes.py` | The eight Manim scenes (B02, B03, B04, B05, B06, B07, B08, B10) |
