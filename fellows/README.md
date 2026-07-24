# Fellows

This top-level collection is reserved for Humanitarians AI fellow-profile and fellow-showcase video projects.

Use one lowercase-kebab folder per fellow, named `first-name-last-initial`, then
one dated weekly-report folder per video:

```text
fellows/
  maya-r/
    2026-07-10-building-the-verified-data-gate/
```

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

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Fellows

This folder organizes **3 video projects** built around beat sheets. Each project README explains the subject, supplies research and fact-check prompts, and documents the free local rebuild workflow.

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
