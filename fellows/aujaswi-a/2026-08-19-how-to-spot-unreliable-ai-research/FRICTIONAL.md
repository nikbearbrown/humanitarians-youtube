# Frictional Log — How to Spot Unreliable AI-Generated Research

**Entry date:** 2026-09-24

**What I was working on:** Building the very first video in this batch end-to-end, to establish the real production pipeline before repeating it eleven more times.

**What I tried, and what I expected:** First attempt used a custom ffmpeg drawtext text-card renderer for the on-screen visuals. Expected it to be an acceptable quick house style.

**Where it resisted, and what I did next:** Rejected on review — it did not use the required Claude-desktop composer UI look, so it did not read as an authentic Brutalist/Claude-branded video. Fully rebuilt on the real `ClaudeComposerAsk` Remotion component instead. That first ffmpeg draft also had a real bug: UTF-8 em-dash bytes were being misread as CP1252 by ffmpeg's drawtext filter, rendering as garbled characters on screen — fixed by replacing every em dash with an ASCII hyphen. After the rebuild, GATE V (automated frame QC) flagged two more real problems on the vertical cut: a MAJOR canvas-fill violation (the composer card filled only ~30% of the tall frame) and a BLOCKER edge-bleed on beat B03, where the segment title "Check 2: Source Authority" (26 characters) overflowed the safe margin at large-text size. Fixed the fill issue via the component's own `largeText` prop, and shortened the title to "Source Authority" (17 characters).

**What Claude contributed, what I accepted/changed/rejected:** Claude designed and built the whole composer-based render pipeline from scratch after the first approach was rejected, and diagnosed both GATE V failures directly from the QC report rather than guessing. I accepted the rebuilt pipeline and both fixes as-is; the ffmpeg approach was fully discarded, not patched.

**What I understand now, and what I still don't:** Template compliance isn't a cosmetic preference — it's the first thing review actually checks, and portrait framing needs real safe-margin headroom, not just a rescale. Applied a standing rule after this: every segment title in every later video stays at or under 22 characters. What I still don't know: whether the fix generalizes to segment titles with different character sets (numerals, punctuation-heavy phrasing) since only this one overflow case was observed directly.
