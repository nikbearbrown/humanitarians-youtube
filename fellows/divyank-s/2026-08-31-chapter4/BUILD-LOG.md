# BUILD-LOG — Claude, Rewritten.

## Decisions

- **Source:** `ai1-cli/chapters/04-rewrite-a-chapter-in-another-voice.md`,
  read in full — same book as the `llm-as-a-judge` build's predecessor
  reels, different chapter.
- **4-act structure derived from the chapter's own shape:** I (the voice
  mechanism + the 7-voice catalog), II (diff-not-read + per-reader
  judgment), III (the verdict-needs-quotes worked example, using the
  chapter's real Socratic/Pragmatist quotes), IV (the 4 failure modes +
  bridge to Chapter 5).
- **No Smithsonian imagery**, per explicit instruction — all 5 archival
  stills sourced via the Wikimedia Commons API instead (consistent with
  every prior build this session, since Smithsonian's own search returns
  `HTTP 403` to non-browser fetches anyway).
- **No Manim** (same `pangocairo` gap as every prior build) — absorbed
  into REMOTION.
- **9:16 portrait coverage planned at authoring time, not retrofitted.**
  The `llm-as-a-judge` build discovered late that only `BinaryBranch` and
  `DivergentFates` have real portrait (`916`) coverage; this build assigns
  those two patterns to one hero beat per act from the start (A1-5, A2-2,
  A2-5, A3-3, A4-3), so deriving the Short should need no new Root.tsx
  work and no post-hoc drop-list surgery.
- **Two-deliverable plan:** one 16:9 master (this folder) and one 9:16
  Short (`short/`, via `shorts.py`), both at 4K.
