# Frictional log — Explainer: What Is Multimodal AI?

## 2026-09-04 — the first claude-hai reel in this run, 16:9 + 9:16

- **Drive:** https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `PROOF-REVIEW.md`
(10/12, gate PASS), `_qc/REPORT.md`, `multimodal-ai.mp4`, `short/multimodal-ai-short.mp4`.
(YouTube / Drive links: TBD — not uploaded yet.)

**What I was working on.** An `ai-explainer` on what "multimodal AI" is, in the
house claude-hai style (cream/ink/terracotta, EB Garamond, "AI, Explained" banner,
"Hey, Muskan"), cut at 16:9 and 9:16 in true 4K. Built framework-first — the
definition before any example — specifically so it would pass PROOF.

**What I tried, and what I expected.**
* I assumed the body cards would render from the beat sheet's `shot.remotion.pattern`
  (ChipGrid / LayerStack), the way the bookends do.
* I assumed the short could just reuse the 16:9 body cards.
* Both were wrong, and neither failed loudly.

**Where it resisted, and what I did next.**
* The body cards are NOT produced by the remotion pattern. They're bespoke 4K PIL
  cards; the `pattern` field for body beats is vestigial (ChipGrid needs an `items`
  prop the sheet never passes — it would crash). So there was no generator — I had
  Claude write one (`make_cards.py`) from the `shot.card` specs.
* B04 (the "versus" edge-case card): the left note collided with the caption because
  a 3-step flow pushed it too low. Fixed by pinning the note at a fixed y.
* B05 (5-item grid): overflowed both canvas edges — card width was too wide for 3
  columns. Fixed by sizing columns per count. Subtitle/title clearance too.
* Caught by reading the actual rendered PNGs, not by trusting the build.

**What Claude contributed, and what I did with it.**
* Mine: the topic, the framework-first decision, GATE P approval of the narration
  (run-straight-through), and reviewing every card and frame.
* Claude's: authored `beat_sheet.json` + `PEDAGOGY.md`; wrote `make_cards.py`;
  rendered the Remotion bookends and the Kokoro (Bella) audio; compiled 16:9 and 9:16
  at true 4K; QC by pulling real frames and reading them; ran the PROOF review.
* Caught without being asked: the ChipGrid-would-crash / vestigial-pattern problem,
  before it produced a broken render.

**What I understand now, and what I still do not.**
* Understood: the body visuals are PIL cards generated from `shot.card`, not the
  remotion pattern — so QC has to read the artifact, not read the config.
* Not resolved: PROOF docked the worked example (B03) for being a scripted card
  rather than a real captured multimodal run.

