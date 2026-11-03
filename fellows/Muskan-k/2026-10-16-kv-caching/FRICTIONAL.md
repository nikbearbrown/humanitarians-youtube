# Frictional log — Explainer: KV Caching

## 2026-10-16 — claude-hai explainer, 16:9 + 9:16
- **Drive:** https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G
Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `PROOF-REVIEW.md`
(11/12, gate PASS), `_qc/REPORT.md`, `kv-caching.mp4`, `short/kv-caching-short.mp4`.
(YouTube / Drive: TBD.)

**What I was working on.** An explainer on KV caching, framework-first: generation is
token-by-token and each token needs every prior token's Key and Value, so cache them
once and reuse instead of recomputing the history — memory for speed. Mechanism kept
qualitative (no FLOPs/param numbers).

**What I tried, and what I expected.**
* I expected `python3 make_cards.py` to just work, the way it had on every prior reel.

**Where it resisted, and what I did next.**
* It failed with `ModuleNotFoundError: No module named 'PIL'`. The shell's default
  `python3` had switched to Homebrew 3.13 (no Pillow) sometime mid-run; earlier reels
  had resolved `python3` to the system 3.9, which *does* have Pillow. The compiler
  (`compile.py`) uses PIL for slates/labels too, so it would have broken the same way.
  Switched the card generator, `compile.py`, and `remotion_scenes.py` to
  `/usr/bin/python3` explicitly. Everything then ran clean.

**What Claude contributed, and what I did with it.**
* Mine: the topic, the framework (memory for speed), GATE P, review.
* Claude's: the beat sheet; diagnosed the PIL breakage and pinned the interpreter;
  rendering/compiling; PROOF.

**What I understand now, and what I still do not.**
* Understood: the toolkit's PIL dependency lives in `/usr/bin/python3`; the default
  `python3` can change underfoot. At least this one failed *loudly* (an import error),
  unlike most of the bugs this project throws.
* Not resolved: PROOF flagged that the cost claims ("quadratic waste", "grows with
  length × layers") are asserted, not shown as a counter or a growth curve.
