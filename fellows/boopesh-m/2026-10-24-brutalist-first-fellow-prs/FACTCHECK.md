# FACTCHECK — Brutalist, Shared (Boopesh M., week of 2026-10-18 → 10-24)

Every claim below was checked against `nikbearbrown/brutalist.art` git history
(`git log 4115560a..a99b5323`, fetched 2026-10-24). Commit hashes are the evidence.

| Beat | Claim | Evidence | Status |
|---|---|---|---|
| B00/B20 | Three fellow pull requests were merged on 23 Oct 2026 | merges `f7b72dd4` (PR #4, 20:12:21 −0400), `61ae45ef` (PR #3, 20:12:24), `a99b5323` (PR #1, 20:12:28) | ✅ |
| B20 | "all within ten seconds" | 20:12:21 → 20:12:28 = 7 s | ✅ |
| B00 | "the first three pull requests in its history" | `git log --grep "Merge pull request"` over the full 112-commit history returns only these three | ✅ (PR #2 not merged — not claimed) |
| B20/B60 | 18 Oct: building-walkthrough and blender-build added | `4b4a8834` 2026-10-18 | ✅ |
| B20/B60 | 21 Oct: blender-modelbuild added; blender-build moved to an image-based lesson | `d45a9554`, `a187fab7` 2026-10-21 | ✅ |
| B30 | PR #1 by gaurav-bakale: HTML templates → YouTube-size PNGs, faceless, uses toolkit design tokens | `runtime/thumbnails/README.md` | ✅ |
| B30 | Claude Skills series locked to one template; only the command changes | README "The locked series template" (`--cmd`, `--mascot`); the @3x outputs shown (cropped to title + command) differ only in the command | ✅ |
| B30 | Images shown are real outputs | `runtime/thumbnails/out/claude-skills/@3x/*.png` (3840×2160) | ✅ |
| B40 | PR #3 by meenuviji, eleven commits | `git log --author=meenuviji 4115560a..a99b5323`, merges excluded = 11 | ✅ |
| B40 | Python ≥ 3.10; live faster-whisper check; `av` capped below 19; fellows loudness match | `a51c14bf`, `87e054bb`, `1a65e188`, `7458a94c` | ✅ |
| B50 | PR #4 (Aditi, branch `aditi/seis-speaker-series`): 1–4 h Teams recording → film; logo reveal → speaker card → talk + Q&A uncut; word-level profanity mutes | `skills/make/seis-speaker-series/SKILL.md` | ✅ |
| B60 | building-walkthrough measures the camera before rendering | its SKILL.md description ("MEASURES the camera … before a frame is rendered") | ✅ |
| B60 | blender-build teaches building a similar model from finished images | its SKILL.md | ✅ |
| B60 | blender-modelbuild writes beat sheets from real build evidence, separating AI-script steps from hand steps | its SKILL.md | ✅ |

Names: contributors are named only by first name or public GitHub handle, per the fellows
privacy rule. No surnames are spoken or shown.
