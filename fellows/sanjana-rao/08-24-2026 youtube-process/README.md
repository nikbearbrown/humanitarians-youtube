# youtube-process — CLI-explainer reel

**Register:** Teardown (NikBearBrown). **Skin:** Claude (default).
**Voice:** Kokoro `am_echo` (Sanjana, in for Bear) — see `beat_sheet.json`.
**Persona law:** IN-FOR-SANJANA everywhere IN-FOR-BEAR would appear.

## What this reel teaches

How to ship a video into the Humanitarians AI review chain without eating a
REITERATE. The CLI-video spine (INTRO → PROBLEM → ASK → CODE → OUTPUT →
CHANGE → OUTPUT → SUMMARY → NEXT STEPS → OUTRO) is used to reconstruct how
`submission_check.py` — the six-criteria gate validator — gets built with
Claude in two prompts.

The ACTUAL-CODE LAW is satisfied: the code shown in B03 is trimmed from
`submission_check.py` in this folder — real source, not pseudocode.

## Files

- `beat_sheet.json` — the 10-beat spine, all beats voiced `am_echo`.
- `submission_check.py` — the artifact the reel builds (the CODE beat's source).
- `README.md` — this file.

## Build (from repo root)

```bash
python3 runtime/scripts/generate_audio_kokoro.py "../YouTube Process/youtube-process"
bash scripts/vox_run.sh "../YouTube Process/youtube-process"
```

The audio pass reads `metadata.voice_kokoro: am_echo` (and each beat's
`voice: am_echo`) — the `am_echo` allowlist entry was added to
`runtime/scripts/generate_audio_kokoro.py` for this reel.

Output beats B04 and B06 ship as slates until a terminal-run motion clip is
dropped into `media/B04.mp4` and `media/B06.mp4` (see the OUTPUT-beat notes in
`skills/make/cli-explainer/SKILL.md`).

## Persona swap

Every string that would say "Liam, in for Bear" has been rewritten to
"Sanjana, in for Bear":

- B00 `greeting: "Hola, Sanjana"`, `runningText: "this is Sanjana, in for Bear…"`
- B00 / B09 narration open with "This is Sanjana, in for Bear."
- B09 (ClaudeTitleOutro) `subline: "Sanjana, in for Bear · build it, then take it apart"`
