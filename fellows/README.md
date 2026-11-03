# Fellows

## Example of a month-one renewal report

Start with [Example Fellow — Brutalist team](example-f/README.md) for a complete
reporting structure: a fellow executive summary, descriptive work folders, direct
evidence links, weekly hours, Frictional logs, a research plan, and a
[Markdown renewal request](example-f/renewal-requests/2026-09-21-renewal-request.md).
The fellow and hours are fictional. The four beat sheets are attributed adaptations
of existing Claude/Bear productions; no new finished videos, employment records,
or supervisor approvals are claimed. Missing evidence is explicitly marked.
Use the structure with your own actual records. Professor Bear must be able to
open the evidence directly; finding it is the fellow's reporting responsibility.

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

## Folder naming and the fellow README

Every directory under `fellows/` is lowercase kebab-case and named
`first-name-last-initial` — `asavari-s/`, `rohan-v/`. Where two fellows share a first
name and a last initial, and only there, the name extends to two surname letters
(`arjun-pa/` and `arjun-pu/`). Nothing else identifying goes in a path.

**No personal information anywhere in this tree beyond a first name, a last initial and
a GitHub id.** No surnames, no email addresses, no phone numbers, no student or employee
numbers — not in folder names, READMEs, beat sheets, descriptions or build logs.

Every fellow folder carries a `README.md` opening with exactly this block:

```markdown
# Firstname L.

**Role:** <role>
**Project:** <project>
**GitHub:** [@handle](https://github.com/handle)
```

Below that block the README says what is in the folder — one line per dated work
subfolder — followed by the Frictional note. Each piece of work keeps its own
`YYYY-MM-DD-short-slug/` subfolder holding its `beat_sheet.json`, README, sources and
build assets.

## Frictional logs

Every work subfolder carries its own `FRICTIONAL.md` — `fellows/first-name-last-initial/
YYYY-MM-DD-slug/FRICTIONAL.md` — logging the process behind *that* piece of work, beside
the evidence it describes. Dated entries: what was tried and expected, where the work
resisted and what was done next, what Claude or another person contributed and what was
accepted, changed or rejected, and what is now understood or still open. Append as you
go; never rewrite an earlier entry. It is not graded. It is documentation of practical
learning, written while the work happens rather than reconstructed later.
See <https://www.humanitarians.ai/fellows>.

## GitHub for source and assets, Drive for renders

Keep source, evidence, and build assets here. Keep rendered media in the shared
Google Drive and link it from the relevant project README. The line is *what the
pipeline produced* versus *what the pipeline consumed*:

- GitHub: beat sheets, scripts, source code, prompts, citations, build logs,
  checks, review notes, README files — **and the assets used to build the
  video**: browser or screen captures, source recordings, sound effects and
  licensed cues, pantry stills and clips, fixtures. An MP4 or MP3 is fine when
  it is an input (put it in `capture/`, `assets/`, `sfx/`, or `pantry/`). Keep
  each file under GitHub's 100 MB limit.
- Google Drive: **renders** — generated narration (`mp3/`, `audio/`), beat clips
  (`media/`, `clips/`), Manim output, review cuts, landscape and vertical
  masters, Topaz/8K variants. The root `.gitignore` excludes these by location
  and by `-slate`/`-cut`/`-topaz` suffix, not by file type.

(Rule changed 2026-09-18 at Bear's direction; before that all MP3/MP4 files were
excluded by extension.)

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
