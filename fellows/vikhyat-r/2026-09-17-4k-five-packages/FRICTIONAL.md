# FRICTIONAL — Five Ways to Catch a Resolution Problem

Append-only. Newest entry at the bottom.

---

## 2026-09-13 — Expected to build a 4K checker, found there was nothing to fix

**Tried / expected.** The brief was that fellows keep submitting non-4K videos,
so I expected to find the toolkit's 4K support missing or broken and to build
the missing piece.

**Where it resisted.** It wasn't missing. `./art final` appends `--height 2160`
and produces a correct 3840×2160 master. The capability has worked since the
repo's first commit.

**What I did next.** Audited instead of building. The real finding was that four
different resolutions are in circulation across the written guidance — 2160 in
the main command, 1080 in two skill guides, 720 as the code's built-in fallback,
1920 in the vertical helper — and that nothing anywhere checks the finished
file's dimensions.

**Claude's contribution.** Did the repo reading and produced the audit. I set
the questions and decided which findings were worth acting on.

**Accepted / rejected.** Accepted the audit. Rejected my own starting premise.

**Understood now.** The problem was never capability. It was that the guidance
around a fast-growing toolkit hadn't caught up, and nothing verified the output.

---

## 2026-09-17 — The gates found six things I could not see

**Tried / expected.** I expected rendering to be the slow part and QC to be a
formality.

**Where it resisted.** It was the reverse. Six defects were caught by the
toolkit's own gates, none of which I would have noticed watching the video:

1. **GATE A** refused a scene whose shapes never changed — my Drive-report
   table was text fading into a fixed grid, which the gate reads as a text
   slide regardless of how much text it holds.
2. **GATE V** found a beat filling only 46% of the frame; a transform had left
   the top third empty.
3. **GATE B** found the title box overshooting the safe area by 0.05 units —
   invisible, real, and affecting every titled scene at once.
4. **GATE V** found white cards on a cream ground scoring 0.00–0.05 contrast
   against a 0.30 minimum. They looked fine to me; they were nearly the same
   luminance as the background.
5. **GATE V** found text clipped out of a card — my four items needed 2.54
   units and the card was 2.5.
6. **GATE V** found a card crossing the frame's right edge that **GATE B had
   passed**, because GATE B measures text bounding boxes and never rectangles.

**What I did next.** Fixed every one at source. Did not lower `ART_STRICT` or
`ART_QC` at any point, which was a standing instruction and turned out to
matter — finding 3 was warning-level, and a warn-and-slot run would have
written a clipping bug into the master.

**Claude's contribution.** Diagnosed each failure and proposed fixes. I insisted
on fixing causes rather than loosening gates, and rejected one proposed fix
(narrowing boxes to make labels fit) as treating a symptom.

**Understood now.** These gates are good, and they are pointed at craft rather
than at output. The pipeline will refuse to render a scene because a title is a
rounding error too high, and will write a 720p master without a word. That
contrast became the strongest argument in the reel itself.

**Still open.** Whether a resolution check gets added upstream is not my call.

---

## 2026-09-17 — Windows, and the same bug twice

**Tried / expected.** That the documented commands would run.

**Where it resisted.** Five separate portability failures:

- `python3` resolves to a Microsoft Store placeholder, so every documented
  command fails. `setup` then reports all five Python dependencies missing
  when all five are installed, and advises installing a Python already present.
- `shorts.py` reads `Root.tsx` with no encoding and swallows the error, so the
  portrait check saw an empty registry and reported every 916 composition as
  missing.
- `scene_search.py` crashes printing a description containing `→`.
- `remotion_scenes.py` calls `npx`, which Windows resolves only as `npx.cmd`
  and cannot execute from Python.
- `compile.py` builds an ffmpeg filter with an unescaped Windows path.

**What I did next.** A `python3` shim, `PYTHONUTF8=1`, `PYTHONIOENCODING=utf-8`,
`ART_NO_DRAWTEXT=1` (a switch the file already supports), and a small runner
that drives the same Remotion CLI through `node` instead of `npx`.

**Worth recording:** the 4 Sept reel hit the identical `npx` bug and solved it
by hand-writing a props file per beat. Same bug, two solutions, six weeks apart,
because it was never reported. That is the argument for logging friction rather
than just working around it.

**Understood now.** On Windows the sanctioned Remotion path cannot run at all,
so every Remotion beat in the toolkit is unreachable for a Windows fellow. It
is a one-line fix.

---

## 2026-09-17 — A wrong prediction about the portrait cut

**Tried / expected.** Assumed Manim derives a narrow frame from a portrait pixel
canvas.

**Where it resisted.** It doesn't. At `-r 2160,3840` it keeps `frame_width` at
14.2222 and scales the two axes differently, so the content landed distorted in
a small central band.

**What I did next.** Measured it rather than assuming a second time, then forced
`config.frame_width = 4.5`. A low-resolution test render caught this before nine
4K renders were spent on it.

**Also predicted wrongly:** that the vertical master would pass GATE V because
it carries no burn-in labels. It failed anyway — a second overlay, the channel
caption, renders 225px outside the gate's mask at 2160×3840. I asserted it would
pass before checking, and was wrong.

**Understood now.** Every problem in this build was a measurement I had assumed
instead of read. That is also precisely the audit's argument about resolution,
which I did not expect to demonstrate on myself.

**Still open.** The portrait cut ships without the channel caption
`hai/SKILL.md` asks for. The handle is on the outro instead. A proper fix needs
a change to the toolkit.
