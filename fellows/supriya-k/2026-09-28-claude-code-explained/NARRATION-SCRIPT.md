# NARRATION-SCRIPT — claude-code-explained

**Format:** CLI-explainer, 12-beat required spine · **Skin:** `claude` · **Persona:** none — direct
author attribution, visible on-screen handle "Supriya" (no "in for X") · **Register:** Teardown ·
**Voice:** Kokoro `af_bella` · **Words:** 420 · **Estimated runtime:** ~170s (at the measured 2.56 words/s
from the v2 banking reel) — must stay under 180s with the 4.5s 9:16 endcard so the 9:16 is full-length.

Generated from `beat_sheet.json` — the sheet is the source of truth; edit it, then regenerate.

---

**B00 — INTRO** · ~11.0s
> Hi, I am Supriya and this video is about how Claude Code actually works: plan, gate, execute, verify. Every example is from real work in this toolkit.

**B01 — PROBLEM** · ~18.9s
> Here's the problem. Claude writes the code for a video faster than I can. It can't watch the video. An earlier vertical cut of mine was true four K, and the text filled a fifth of the frame, at most. Bitrate: one hundred thirty-nine kilobits a second.

**B02 — MECHANISM** · ~20.8s
> So the work runs as a loop. Plan: nothing is built until I approve it. Gate: I sign the narration before any audio exists, and the agent never signs its own gate. Execute: Claude writes the code and runs the renders. Verify: look at real frames. When verify fails, back to plan.

**B03 — CLI** · ~13.4s
> Example one. The plan said the vertical composer was already portrait-ready. Before running the pipeline, one beat got a standalone render. Everything sat in the top half. So the ask: rebuild the layout.

**B04 — CODE** · ~15.7s
> Here's the fix. Type size was never the problem; position was. The old layout stacked everything between ten and forty percent of the height. The rebuild spreads the anchors down the frame, and the card starts at forty-four percent.

**B05 — OUTPUT** · ~13.4s
> Render it again. Content now spans about eighty-six percent of the frame's height, up from fifty-five. Bitrate rose from two hundred seventy-six to three hundred forty-one kilobits a second, with no encoder change.

**B06 — CLI** · ~12.6s
> Example two is worse, because the check passed. The vertical Manim scenes cleared the layout audit with no errors, and the frames still looked nearly empty. The revision: find out why.

**B07 — CODE** · ~18.5s
> Here's what was happening. A portrait resolution doesn't change Manim's coordinate frame. The scenes drew in landscape coordinates and shrank into the middle. The audit set portrait coordinates in its own process, so it checked a space the real render never used. Two lines fixed it.

**B08 — OUTPUT** · ~14.6s
> Before, the scenes used roughly the center quarter of the canvas. After, they span the full frame, and the final frame check passed. The audit was right about its own coordinates and wrong about the video.

**B09 — SUMMARY** · ~10.7s
> So that's the loop. Plan, approved first. Gate, signed by a person. Execute, where Claude is fastest. Verify, by looking. Both bugs looked fine on paper.

**B10 — NEXT STEPS** · ~16.1s
> Your turn. Before your next change, paste this: write a plan, list what you'll verify and how, then wait for my approval. Watch the middle part. If Claude can't say how it will check the result, the plan isn't finished.

**B11 — OUTRO** · ~4.4s
> Claude Code, Explained. Plan, gate, execute, verify. I am Supriya.
