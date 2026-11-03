# Frictional log — Explainer: Agentic Dev Life Cycle

## 2026-10-09 — claude-hai explainer, 16:9 + 9:16
- **Drive:** https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G
Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `PROOF-REVIEW.md`
(11/12, gate PASS), `_qc/REPORT.md`, `adlc.mp4`, `short/adlc-short.mp4`. (YouTube / Drive: TBD.)

**What I was working on.** An explainer on the Agentic Development Life Cycle: the agent
builds, but your leverage moves to the two ends — Specify and Verify — around a loop
(Specify → Plan → Build → Verify → Iterate). Reused the "loop" visual, this time with an
owner label on each node (you / agent).

**What I tried, and what I expected.**
* I expected the loop card to handle four nodes the same way it handled three on the
  agent-harness reel.

**Where it resisted, and what I did next.**
* The *portrait* loop broke at four nodes: the taller stack pushed the "iterate" label
  down until it overlapped the caption (the 3-node version had cleared it fine). A
  layout that worked at N=3 failed at N=4. Had Claude rework the generator so the
  portrait loop distributes any node count inside a fixed vertical band, leaving room
  for the label and caption. Re-rendered the short and re-read the frame to confirm
  before shipping.

**What Claude contributed, and what I did with it.**
* Mine: the topic, the framework (you own specify + verify), GATE P, review.
* Claude's: the beat sheet; the portrait-loop fix in `make_cards.py`; rendering; PROOF.

**What I understand now, and what I still do not.**
* Understood: a card layout that passes at one element count can collide at another —
  the generator now scales node spacing to a fixed band, and I re-check the frame, not
  just the card spec.
* Not resolved: the worked example is schematic, not a captured agent cycle; and "ADLC"
  as five named phases is my synthesis, not a standardized spec (said so in the reel).
