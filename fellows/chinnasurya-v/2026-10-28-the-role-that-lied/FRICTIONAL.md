# Frictional — The Role That Lied

## 2026-10-28 — designing for two aspects at once

Wrote this one knowing a 9:16 cut was required, which changed how I built it.
Every previous reel in this series lays beats out horizontally — two system blocks
facing each other, two cards side by side, two numerals in a row — and all of that
breaks in portrait. So this reel is a single stacked column throughout: full-width
rows, vertical arrows, nothing positioned by a fraction of the frame width.

That decision paid for itself immediately. The portrait render needed no second
layout and no portrait branch.

## 2026-10-28 — the defect that mattered

Four QC defects, three of them dead frame space. The one worth recording is B02:
**the closing caption never rendered at all.** My state list was
`[draw(0), draw(1), draw(1)]` — I called the second state twice and never reached
the third, so the two lines explaining why the one-line check is tempting simply
did not exist in the output. The beat looked finished. The mp4 was the right
length. Nothing failed.

This is a different class of error from the geometry defects I have been fixing.
Those are visible the moment you look at the frame. This one is invisible unless
you know what was supposed to be there, which is an argument for the contact sheet
being read against the script rather than on its own.

## 2026-10-28 — a shared bug surfaced by the portrait pass

Rendering portrait exposed something that had been wrong in every reel in this
series: `footer()` drew its caption at a constant size with no width check. At
16:9 the captions happened to fit. At 9:16 the frame is narrower and every single
footer was clipped mid-word. Fixed in the shared core and propagated to all six
reels.

The pattern holds: anything drawn at a size I chose rather than a size I measured
is a defect waiting for a different canvas.

## 2026-10-28 — what I chose not to put on camera

The re-audit this week found a signature-verification fallback that accepts an
unverified payload. That is a live, unfixed weakness, and I am not making a video
explaining it before it is fixed. It is recorded in the research plan instead.
Same reasoning as the September reels, which kept their findings off camera for
the same reason. The role-matching change, by contrast, shipped months ago with
tests, so explaining it costs nothing.

## 2026-10-28 — still open

No captions or word clock. `PEDAGOGY.md` is not self-signed.
