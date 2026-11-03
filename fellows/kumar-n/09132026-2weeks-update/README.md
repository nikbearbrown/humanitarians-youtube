# Transformers in SERS-ML: What the Rewrite Actually Fixed

**Channel:** claude-liam &nbsp;&middot;&nbsp; **Format:** deep-explainer
**Runtime:** ~3.5 minutes &nbsp;&middot;&nbsp; **Slug:** `claude-liam-sers-transformer-fix`

## What this video is about

This video compares the **initial draft** of Section 4.2 (Transformer
Architectures) of a SERS-ML review paper against its **current, revised
version**, covering three real, independently-verifiable changes:

1. **A missing recommendation, added.** The original draft summarized
   three transformer studies (Wang et al., Zhang et al./TMNet, Hajikhani
   et al.'s SERSFormer-2.0) and then simply stopped -- no verdict on when
   a transformer is actually worth choosing over a CNN. The current
   version adds an explicit closing recommendation: default to a CNN for
   most SERS classification work, and reach for a transformer only when
   the problem genuinely needs multi-task output or long-range spectral
   dependencies.

2. **An unqualified claim, given real context.** The original draft stated
   Wang et al.'s transformer network achieved a "100% positive
   identification rate" with no elaboration on what that meant. The
   current version adds the real testing conditions found by going back
   to the source paper: a validation set of just 75 spectra, under two
   laser power levels and a narrow range of integration times -- turning
   an unqualified perfect score into an honestly-scoped result.

3. **A real evidence gap, actually closed.** The original draft never
   addressed whether a transformer architecture actually outperforms a
   CNN on comparable SERS data at all -- three transformer studies are
   cited, but none are benchmarked against a CNN. The current version
   finds a real, independent answer: a 2026 peer-reviewed study by
   Sineesh and Kamsali directly compared five deep learning architectures
   on the same Raman classification task, with the transformer finishing
   last, more than five points behind the best model -- while explicitly
   noting this benchmark uses general Raman data, not SERS-specific data,
   rather than overstating what it proves.

## Structure (9 beats, ~3.5 min)

| Beat | Act | Component | What happens |
|---|---|---|---|
| B00 | ASK | ClaudeComposerAsk | Cold open -- frames the comparison between the initial draft and the current text |
| B01 | BLUF | BrutalistHesitantWriter | The core idea in one line: a draft that read "complete" was actually only descriptive |
| B02 | THE MISSING VERDICT | Manim (`B02_TheMissingVerdict`) | Three study cards, then an empty recommendation slot that fills in |
| B03 | QUALIFYING THE CLAIM | Manim (`B03_QualifyingTheClaim`) | A bare "100%" figure gets annotated with its real test conditions |
| B04 | THE GAP IDENTIFIED | Manim (`B04_TheGapIdentified`) | Transformer and CNN boxes with a large question mark between them |
| B05 | CLOSING THE GAP | Manim (`B05_ClosingTheGap`) | The real five-architecture benchmark that resolves the gap, transformer finishing last |
| B06 | VERDICT | ClaudeVerdictArtifact | One-page recap of all three changes |
| B07 | HANDOFF | ClaudeComposerAsk | "Your turn" -- a prompt for auditing your own writing's before/after claims |
| B08 | OUTRO | ClaudeTitleOutro | Title restate |

## Evidence discipline

Every claim about the *difference between the two drafts* (items 1-3
above) is independently verifiable by comparing the original and current
texts directly. Two claims about the content of external sources cited
within the revision -- Wang et al.'s real test conditions, and the
Sineesh & Kamsali benchmark -- are carried through faithfully from the
author's own account of going back to those sources, and this is stated
plainly in `FACTCHECK.md` rather than implied as independently
re-verified against the primary papers.

## Files in this folder

| File | Purpose |
|---|---|
| `beat_sheet.json` | The full beat-by-beat script and Remotion/Manim configuration |
| `scenes.py` | The four Manim scenes (B02, B03, B04, B05) |
| `FACTCHECK.md` | Every claim checked against the two source drafts, with an explicit boundary noted on which claims rely on author-reported source-checking |
| `PROMPTS.md` | Confirms this reel required no external media or generation prompts -- every beat resolves through the pipeline's own renderers |
