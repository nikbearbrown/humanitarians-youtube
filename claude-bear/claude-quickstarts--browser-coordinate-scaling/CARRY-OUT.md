# CARRY-OUT — claude-quickstarts--browser-coordinate-scaling

**Carry-out line (written before the body, per CARRY-OUT LAW):**

> A Claude coordinate isn't wrong — it's just measured on a smaller picture.
> Multiply back by the resize ratio, and the click lands exactly where you meant.

**Test:** repeatable by someone half-listening next week, and still true — yes.
It compresses the distinction (resized measurement vs. real pixels), not the
topic (browser automation).

**The wrong guess it's built to defeat:** that the (x, y) Claude hands back is
already a real screen pixel, so clicking it directly should just work. It looks
reasonable because Claude clearly saw the button and named a location — the
error is invisible until the click lands somewhere else entirely.

**Falsifying case:** Claude's vision encoder resizes every 16:9 screenshot to a
fixed 1456×819 before the model ever looks at it (`CLAUDE_ACTUAL_WIDTH` /
`CLAUDE_ACTUAL_HEIGHT` in `coordinate_scaling.py`). A 1920×1080 screen is a
different canvas at a different scale. Take Claude's own worked number — a
click at (728, 364) on the 1456×819 image — and place it raw on a 1920×1080
screen: it lands short of the button, not on it. Only multiplying by the
resize ratio (viewport / 1456, viewport / 819) recovers the real pixel.
