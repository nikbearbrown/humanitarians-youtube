# FACTCHECK — hai-workflow-is-the-lesson (DRAFT — NOT SIGNED)

Status: **drafted by Claude, awaiting human review.** GATE F stays closed until a
person checks every row and renames this file to `FACTCHECK.md`.

| Beat | Claim (as narrated) | Verdict | Source |
|---|---|---|---|
| B00/B05 | One script (build_films.py) wrote the beat sheets for films 2–4 | TRUE | ai-fluency/youtube/build_films.py |
| B00/B04 | 39 scenes rendered at 4K for films 2–4 | TRUE (log) | remotion_scenes.py runs, 13 × 3 |
| B03 | Loop: author → audio → render → check → sign | TRUE | HOW-TO.md §4; CLAUDE.md rules 2, 4, 5 |
| B06 | Compiles to a clean cut: film 1 = 4, film 2 = 3, films 3 & 4 = 2 | TRUE (log) | GATE V runs; BUILD-LOG.md |
| B07 | First loop run: 170.1 s / 167.7 s / 167.2 s; MAJOR 0 / 1 / 1 | TRUE (log) | films 2–4 pipeline output |
| B08 | build_films.py docstring shown on screen | TRUE (trimmed + re-wrapped to fit the card) | build_films.py module docstring |
| B09 | Automate only after doing it by hand enough | JUDGMENT | framed as advice |

**Sign-off:** pending. Signing = checking every row, then renaming this file to `FACTCHECK.md`.
