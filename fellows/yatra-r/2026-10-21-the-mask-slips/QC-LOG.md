# VISUAL QC — The Mask Slips.

`yatra-the-mask-slips` · frame-level pass per VISUAL QC LAW.
The mp4 probe is a FILE check and does not count as QC — every entry below comes from
actually reading rendered PNGs.

---

## Defects found and fixed

Both were caught by looking at frames. Neither would have been caught by any numeric
check, and neither was a crash — the renders "succeeded" in both cases.

### 1. B05 `MskArc` — the rise label collided with the curve · **MAJOR** · FIXED

`riseLabel` ("created → viral") was positioned at `Y0 − 86`, which is inside the region
the rising curve sweeps through. The curve drew straight across the word "viral". The
render reported success; only the frame showed it.

**Fix:** label moved to `Y0 + 22` — below the baseline, where nothing crosses it.

### 2. B03 `MskMoney` — the accent rule read as underlining the CITATION · **MAJOR** · FIXED

This one is a brand-law defect rather than a layout one. The beat is designed so the
terracotta rule underlines the *caveat* ("Reported, not audited…") and never the money —
the reel's whole accent grammar is that the gold-rush half does not glow. But `SourceLine`
defaults to `SAFE.b − 128` and the rule sits at `SAFE.b − 78`, so on screen the rule
landed immediately beneath the source line and read as emphasising
*"Source: Garbage Day, October 2026"*.

In this brand a citation is provenance, never emphasis — `SourceLine` is `MUTE` precisely
so a source can never take the accent. The rule's position was undoing that.

**Fix:** the source line lifted to `SAFE.b − 196`, clear of the rule, so the accent
attaches unambiguously to the caveat.

---

## Nine-point rubric — final state

| # | Check | Result |
|---|---|---|
| 1 | Edge bleed / clipping | PASS |
| 2 | Title-safe margins | PASS — every scene authored from the `SAFE` constant |
| 3 | Container overflow | PASS |
| 4 | Collision | PASS after fix 1 |
| 5 | Offscreen anchors | PASS |
| 6 | Legibility | PASS — smallest type is the 22px eyebrow and 25–26px source lines at 1920×1080, i.e. 44–52px in the 4K render |
| 7 | Brand bug placement | PASS — `@Yatra` wordmark, lower-right, inside the safe inset, every beat |
| 8 | Aspect | PASS — 3840×2160 |
| 9 | Canvas fill | PASS |

**Accent grammar audit** (this reel's own rule, checked separately): one terracotta event
per beat, and never on the gold-rush half. B03 was the one violation and is fixed.

**Zero BLOCKER, zero MAJOR remaining.**

---

## Frames read

B01 · B02 · B03 · B05 · B06 · B07 · B08 · B09 at ~90–95% of span (where every element has
landed). B00, B04 and B11 are `ClaudeComposerAsk`, verified at B00. B10 and B12 are the
shared verdict/outro components, proven across seven prior reels. Frames kept in
`_qc/frames/`.

---

## Render environment — two toolkit-level failures, neither a reel defect

Logged because they cost hours and will recur.

### A. Orphaned Chrome after a machine sleep

Every render began failing with:

```
TimeoutError: Timed out after 25000 ms while trying to connect to the browser!
Chrome logged the following:
```

(empty Chrome log). Cause: the machine slept mid-render, leaving `chrome-headless-shell`
processes alive at 0% CPU — one had been up **4h21m** — plus stale
`puppeteer_dev_chrome_profile-*` directories under `/var/folders`. Remotion could not get
a clean browser.

**Fix:** `pkill -9 -f chrome-headless-shell`, delete the stale profile dirs, retry. The
Chrome binary itself was fine (`--version` responded normally), which is what ruled out a
corrupt install.

### B. Remotion's 30s per-frame timeout is too low for this pipeline

After A was cleared, renders failed differently:

```
Error: Timeout (30000ms) exceeded rendering the component at frame 225.
```

A `--scale=2` frame of full-bleed EB Garamond on a loaded machine can exceed 30s. This was
already flagged as a risk in the Interest Media QC log; here it became a hard blocker.

**Fix:** added an `ART_TIMEOUT` knob to `runtime/scripts/remotion_scenes.py` (default
**120000**), alongside the existing `ART_SCALE` / `ART_CONCURRENCY` knobs, and passed
`--timeout` through to the render. Raising the ceiling costs nothing on a fast frame — it
only changes how long the pipeline waits before calling a slow one a failure.

**Also learned:** do not render and encode 4K at the same time. Concurrency is what pushes
frames past the ceiling in the first place.

---

## Toolkit gates — status

**GATE V (`runtime/qc/final_frame_check.py`) — NOT USED, deliberately.** Its
`BURN_IN_EXCLUDE` masks only the bottom strip while the review cut's beat label is drawn
top-right, so it reports BLOCKERs on every beat of every reel built in this tree. Ink
coverage measured directly with its own `analyze_frame()` on the clean master instead.
**Toolkit bug, not a reel defect — the reel was not altered to satisfy it.**

**GATE T (`scripts/type_check.py`) — NOT RUN. The script does not exist in this tree.**
The skill lists it as mandatory. §8.1 min-size, §8.2 overflow and §8.3 contrast were
substituted by the frame inspection above; §8.6 golden-strings by the numeral sweep in
`FACTCHECK.md`. Substitution logged rather than silently passed.
