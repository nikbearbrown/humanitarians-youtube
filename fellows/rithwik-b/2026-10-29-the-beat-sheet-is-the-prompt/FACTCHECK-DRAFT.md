# FACTCHECK — hai-beat-sheet-is-the-prompt (DRAFT — NOT SIGNED)

Status: **drafted by Claude, awaiting human review.** GATE F stays closed until a
person checks every row and renames this file to `FACTCHECK.md`.

| Beat | Claim (as narrated) | Verdict | Source |
|---|---|---|---|
| B00/B03 | Brutalist builds every video from a beat_sheet.json | TRUE | HOW-TO.md §1; film 1 build |
| B03 | Film 1 B03 beat shown on screen | TRUE (verbatim, trimmed) | hai-fluent-isnt-finished/beat_sheet.json |
| B04 | audio_file filled in after generation, measured to 0.01 s | TRUE (log) | generate_audio_kokoro.py output |
| B05 | Audio-first: measured durations are the master clock | TRUE | CLAUDE.md rule 2; HOW-TO §1 |
| B05 | Kokoro is a free local voice | TRUE | HOW-TO §2 (model ships locally, no key) |
| B06 | Film 1 beat lengths 13.5 / 15.1 / 16.0 / 11.1 / 18.0 / 2.9 s | TRUE (log) | film 1 audio run |
| B06 | Fix timing by rewriting + regenerating, not by hand | TRUE | CLAUDE.md rule 2 |
| B07/B08 | GATE L refused film 1 over a missing topic; one line fixed it | TRUE (log) | film 1 ./art run output |
| B09 | A sentence is enough for one-off work | JUDGMENT | framed as advice |

**Sign-off:** pending. Signing = checking every row, then renaming this file to `FACTCHECK.md`.
