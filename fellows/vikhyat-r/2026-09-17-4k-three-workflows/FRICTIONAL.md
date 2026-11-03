# FRICTIONAL — Three Workflows, and What Separates Them

Append-only. Newest entry at the bottom.

Companion to `2026-09-17-4k-five-packages`, built immediately after it. Most of
the friction here is the *absence* of friction, and why.

---

## 2026-09-17 — The lessons transferred almost completely

**Tried / expected.** After six fix cycles on the companion reel, I expected a
similar grind.

**What happened instead.** I wrote the companion reel's six lessons into this
reel's `scenes.py` as comments before drawing anything — title buff 0.65 rather
than 0.55, outline-only cards, content inside ±6.3 × ±3.4, bottom content
arriving before the long hold, real shape change in every scene, the outro
period paired with its own final line.

All eight scenes passed GATE A and GATE B on the first attempt. The portrait
set was seven of eight.

**Understood now.** Those six defects were not bad luck; they were a fixed set
of measurable constraints. Written down, they transfer completely. That is the
argument for the starter kit the reels propose, demonstrated accidentally: the
knowledge that separates a clean render from six wasted cycles is small,
specific, and completely transferable.

---

## 2026-09-17 — One defect, and it was a judgement not a measurement

**Tried / expected.** That if GATE A and GATE B passed, the scene was fine.

**Where it resisted.** GATE V rejected B06 at 42% frame fill against a 55%
minimum. Both structural gates had passed it, correctly — nothing overlapped
and nothing left the frame. It was simply a left-heavy composition with half a
14.2-unit-wide frame empty.

**What I did next.** Rather than pad it, gave each row a consequence on the
right: "A — upstream of everything — *nothing reaches B*". Fill went to ~91%
and the beat got better, because the new column says what each position buys
you, which is what the scene was arguing.

**Claude's contribution.** Proposed the fix. I rejected an earlier version that
just widened spacing.

**Understood now.** GATE A and GATE B read structure; only GATE V sees what a
frame looks like. They are not redundant.

---

## 2026-09-17 — I broke the file myself

**Tried / expected.** To apply six small numeric edits with a script.

**Where it resisted.** I generated Python source through a Python string inside
a shell heredoc — three layers of escaping — and `\n` resolved into real
newlines, leaving two unterminated string literals and a file that would not
parse.

**What I did next.** Repaired with direct edits. A second attempt then failed an
assertion because `self.wait(2.2)` appeared twice, in two different scenes —
the check caught it instead of silently editing the wrong one.

**Understood now.** Generated edits to source need either a parse check
afterwards or an assertion that the target is unique. Both were cheap; skipping
them was not.

---

## 2026-09-17 — Portrait was a rewrite, not a re-render

**Tried / expected.** That the portrait cut would be mostly repositioning.

**Where it resisted.** This reel leans on horizontal arrangements far more than
its companion — a left-to-right flow with a return loop, a funnel narrowing
sideways, two folders side by side, a stays-versus-goes pair. In a 4.5-unit-wide
frame none of them survive.

**What I did next.** Restructured rather than squeezed. The flow runs downward
with the refusal looping up the left; the funnel tapers top-to-bottom, which
reads better than sideways anyway; the folder pair and the stays/goes pair
stack.

One measurement I got wrong twice: I derived the portrait safe area as ±2.0
from scaling a constant, when GATE B reports ±1.95. My cards sat exactly on the
boundary. Then, fixing a bottom overflow, I moved a chain up and pushed the
first box into the title — fixing one edge by breaking another.

**Understood now.** Portrait is a different composition, not a different
resolution. `shorts.py` refusing to center-crop generated graphics is right,
and the work it forces is real work.

---

## 2026-09-17 — The bug the reels are about, hit while making them

**Tried / expected.** Nine portrait scenes rendered natively at 2160×3840, both
bookends at 2160×3840, every scene gate-clean. I expected a correct master.

**Where it resisted.** The compile wrote **1216×2160**. `run.sh` hardcodes
`HEIGHT=2160`, which against a 9:16 sheet computes a width of 1216. My genuine
4K portrait beats were letterboxed down into a frame nobody wants.

Worse: GATE V reported it as `edge-bleed — content crosses the title-safe
bottom edge` on all 22 frames. That is a true statement about a letterboxed
frame and it points straight at scene layouts. I only found the real cause by
probing the clips.

**What I did next.** Passed `--height 3840` to **both** the run and the final.

**Understood now.** This is exactly the defect the reels describe, and I walked
into it while making them, knowing it existed. A check reading the finished
file's dimensions would have caught in one second what the toolkit's best
frame-level gate could only describe as a symptom. That is now the strongest
evidence in the proposal, and it is not hypothetical.

**Still open.** Three places disagree about the vertical target — `run.sh` says
2160, `shorts.py` prints 1920, three documents say 3840. Only the documents are
right, and they are the ones not enforced by code.
