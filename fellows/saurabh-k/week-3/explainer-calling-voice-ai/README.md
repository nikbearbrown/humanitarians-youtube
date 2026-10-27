# Calling Voice AI

**Group:** Brutalist team · **Reporting week:** 2026-10-26

## Executive Summary

What actually happens when you call a voice model. The text never reaches the network — it is converted to phonemes first, and the voice itself is a block of numbers rather than a recording of anyone. Built self-referentially: the engine being explained is the one narrating, so every claim is checkable against the audio the viewer is hearing. 54 voices across nine languages, 310 MB of model, 26 MB of voices, no account and no key.

Runtime 1:59 across 10 beats.

## Evidence — Open Directly

- [Beat sheet](beat_sheet.json) — 10 beats, `voice_kokoro: am_onyx`.
- [Build log](BUILD-LOG.md) — per-beat record, toolkit commit, final build state.
- [Sources](SOURCES.md) — where every on-screen figure came from.
- [Fact check](FACTCHECK.md) — claim-level verdicts.
- [Checks report](CHECKS-REPORT.md) — every gate, with the result as the tool reported it.
- [Pedagogy](PEDAGOGY.md) · [Shot list](SHOTLIST.md) · [Prompts](PROMPTS.md)
- [How to rebuild](README-RUN-THIS.md) · [Shopping](SHOPPING.md) · [Replace log](replace_log.md)
- **Video (16:9):** NOT PROVIDED — 3840x2160 master rendered locally. Drive link pending.
- **Video (9:16):** NOT PROVIDED — 2160x3840 master rendered locally. Drive link pending.
- **Supervisor feedback:** NOT PROVIDED.

## Folder Contents

README.md is the report and evidence index. `beat_sheet.json` is the production plan and
carries the per-beat build record. `FRICTIONAL.md` records the process.
