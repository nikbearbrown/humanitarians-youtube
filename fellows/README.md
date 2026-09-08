# Fellows

This top-level collection is the source record for Humanitarians AI fellow work.
It holds the text, code, research, prompts, review notes, and beat sheets that make
each film reproducible and auditable. In that sense, this is where **film as
code** lives—and where a film becomes evidence of the work behind it rather than
just a finished upload.

Use one lowercase-kebab folder per fellow, named `first-name-last-initial`, then
one dated weekly-report folder per video:

```text
fellows/
  maya-r/
    2026-07-10-building-the-verified-data-gate/
```

Profile introduction videos live under
`fellows/profiles/first-name-last-initial/`. Weekly work reports remain under
the fellow's direct folder.

## GitHub for text, Drive for video

Keep source and evidence here. Keep rendered media in the shared Google Drive
and link it from the relevant project README. MP3 and MP4 files do not belong in
this repository, including generated narration, beat clips, review cuts, and
final masters.

- GitHub: beat sheets, scripts, source code, prompts, citations, build logs,
  checks, review notes, and README files.
- Google Drive: landscape and vertical video masters, audio, and other large
  binary media.

Every directory under `fellows/` uses lowercase kebab-case. This keeps paths
portable, predictable, and safe to use in scripts.

## One contract, many films

The current collection is deliberately varied. Its beat sheets range from short
four-beat briefs to 32-beat deep explainers, with a median of ten beats. Most use
the shared `metadata` plus `beats` structure, while the visual evidence ranges
across Remotion scenes, fellow-owned artifacts, Manim demonstrations, stills,
and archival sources. Some projects carry separate vertical beat sheets; others
use a nested `short/` variant or a named `beat-sheet-short.json` file.

That range is a feature, not noise. The beat sheet is the common production
contract, not a demand that every fellow tell the same story. A project update
can foreground owned screenshots and results. A technical explainer can use
Manim or code-driven scenes. A research report can make sources and uncertainty
visible. What matters is that the repository preserves the claim, evidence,
creative decisions, and verification trail needed to rebuild and review the
film.

The `maya-r/` example is explicitly fictional and demonstrates deep-explainer
reports grounded in actual Madison research. Keep review, rights, attribution,
fictional-person disclosures, and publishing gates explicit.

## Fellow voice choice

Each fellow chooses one Kokoro voice for their reports and then keeps that
voice across the series. Kore (`af_kore`) and Bella (`af_bella`) are
ready-to-use options, but any available Kokoro voice may be selected. Record
the choice in the fellow-folder README and every episode's `beat_sheet.json`,
then obtain the fellow's approval before the first audio generation. A later
voice change is an explicit, documented re-voice decision—not a per-episode
default.

When no preference has been supplied, use the fellow's name only as a starting
heuristic: a female-coded name receives a female Kokoro voice suggestion
(`af_*`), and a male-coded name receives a male Kokoro voice suggestion
(`am_*`). This is a production default, not a claim about anyone's identity.
The fellow's stated preference always overrides the name-based suggestion.

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Fellows

This folder organizes **4 video projects** built around beat sheets. Each project README explains the subject, supplies research and fact-check prompts, and documents the free local rebuild workflow.

## Rebuild toolkit

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Brutalist is audio-first and local: the beat sheet drives narration, measured audio becomes the clock, generated visual beats compile immediately, and unavailable media remains as labeled slates until a human fills the pantry. The human conducts, watches, fact-checks, refines, and decides whether anything is published.

This is currently a collection or support folder. Add each new video in its own lowercase kebab-case subfolder with a `beat_sheet.json` and README.

<!-- END BRUTALIST REBUILD GUIDE -->
