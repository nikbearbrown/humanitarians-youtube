# Build prompt — Weekly Research Report: Building the Mycroft Finance Investigator

Use the `brutalist.art` `deep-explainer` / `cli-explainer` workflow on this folder. Run the
toolkit from a Python 3.12 virtualenv (system python3 is 3.13 and is incompatible with the
pinned Manim): `source /Users/adwaitchangan/Study/Brutalist/brutalist.art/.venv/bin/activate`.

1. Read `beat_sheet.json`, `SOURCES.md`, and `FACTCHECK.md`.
2. This is a REAL fellow report. Every number on screen must resolve to a real Mycroft
   project artifact (run log, report file, test output). Do not invent or round beyond the
   source. Resolve every `[VERIFY]` in `FACTCHECK.md` before audio.
3. Fellow voice is Kokoro `am_onyx` ("Onyx, in for Humanitarians AI"), persistent across
   Adwait Changan's series. Do not select a new voice per episode.
4. Present the act map + lane histogram for human plan approval.
5. Complete and obtain human approval for `FACTCHECK.md`.
6. Review narration on animated slates; record the verdict in `PEDAGOGY.md` before audio.
7. Generate Kokoro audio; measured durations are the master clock. Never hand-fix timing.
8. Render the slate previz, run frame-level visual QC (`_qc/`), fix root causes, re-render.
9. Never publish. A successful render is not authorization to upload.

Suggested command after all required gates (from the toolkit root, venv active):

```bash
./art run "/Users/adwaitchangan/Study/Brutalist/humanitarians-youtube/fellows/adwait-changan/2026-07-27-building-the-mycroft-finance-investigator"
```
