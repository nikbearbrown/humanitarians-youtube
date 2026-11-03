# CARRY-OUT — claude-quickstarts--macos-computer-use-coordinate-roundtrip

**Carry-out line (written before the body, per CARRY-OUT LAW):**

> A Claude coordinate on macOS isn't wrong — it's measured on a resized copy of your
> Retina screen. Multiply back by native over sent, and the click lands exactly where
> you meant.

**Test:** repeatable by someone half-listening next week, and still true — yes. It
compresses the distinction (resized measurement vs. real Retina pixels), not the
topic (macOS computer use).

**The wrong guess it's built to defeat:** that the (x, y) Claude reports is already a
real pixel on your actual screen, so clicking it directly should just work. It looks
reasonable because Claude clearly saw the button on the screenshot — the error is
invisible until the click lands somewhere else entirely.

**Falsifying case:** macOS Retina screenshots (e.g. 2560×1600) are far bigger than the
API's image budget — long edge under 1568 px, tile count under 1568 across 28×28
tiles (`computer_use/image.py`). `target_image_size()` resizes first, down to
1344×840 for a 2560×1600 screen, before Claude ever looks. Take Claude's own reported
click — (630, 420) on the 1344×840 image — and place it raw on the 2560×1600 screen:
it lands nowhere near the button. Only multiplying by the resize ratio
(native / sent, applied to both x and y) recovers the real pixel: (1200, 800).
