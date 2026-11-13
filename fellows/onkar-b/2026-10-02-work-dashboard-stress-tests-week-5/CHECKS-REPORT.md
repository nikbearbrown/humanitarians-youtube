# CHECKS-REPORT — Expose The Ledger

Reel: `claude-gatekeeper-dashboard-stress` · 9 beats · **measured 128.4s (2:08)** vs 2:45 target
**GATE V (16:9): 18 frames · 0 BLOCKER · 0 MAJOR ✓**

## Deliverables

| | File | Format |
|---|---|---|
| 16:9 master | `claude-gatekeeper-dashboard-stress-slate.mp4` | 3840×2160 @ 24fps |
| 9:16 companion | `vertical/claude-gatekeeper-dashboard-stress-vertical-slate.mp4` | 1080×1920 @ 24fps |

## Per-beat classification

| Beat | Class | Measured | Pattern |
|---|---|---|---|
| B00 | SHOW | 18.33s | ClaudeComposerAsk |
| B01 | SHOW | 10.41s | BrutalistHesitantWriter — ≥9s ✓ |
| B02 | SHOW | 21.01s | ThreeStageBand (two stages) |
| B03 | SHOW | 7.10s | ClaudeComposerAsk — clears the ≥7s typing floor |
| B04 | SHOW | 20.20s | AlertSplit |
| B05 | SHOW | 16.19s | ThreeStageBand — failure mode, `failIndex: 1` of 3 |
| B06 | SHOW | 12.99s | ClaudeCodeBeat |
| BHTF | SHOW | 13.27s | ClaudeComposerAsk |
| BOUT | SHOW | 8.75s | HaiTitleOutro |

**9 SHOW / 0 HOLD / 0 PUNT.** Slots 9/9. No slates.

## Zero new components

`ThreeStageBand` covered both the two-box framework (N-length `stages`) and the
falsifiability beat (`failIndex`); Scene 3 fit `AlertSplit` with relabelled props.

**Regression check passed.** B05 uses `failIndex: 1` of three stages — the middle
position, which is the configuration that exposed the travel-scaling bug on the Week 4
STEM reel. Verified on frame: the verdict token now **stops at the human step** instead
of sailing past it.

## Illustrative data — the main open item

Nothing from the running system was supplied:

- **B00** — `1,240 rows / 0 human queries`, dramatising the failure class.
- **B04** — the two payload rows, **captioned on screen** as illustrative.
- **B04's right panel** — a generic verdict card, not a screenshot of the real dashboard,
  whose HTML was not provided.

Swap in real values and the narration still fits; it is a two-beat re-render.

## A cross-reel finding worth checking

Scene 3's VO says the normalizer "safely strips the malicious characters." The **STEM
Week 5 reel demonstrates a naive version of exactly that strip failing** —
`re.sub(r'[^0-9.]', …)` returns `'4.5.'` on a sentence-terminated payload and
`float()` raises, and it silently drops magnitude suffixes. If the Gatekeeper's
normalizer shares that shape, it has the same two holes. Nothing is asserted either way
on screen here; worth verifying in the codebase before publish.

## Teaching arc

```
FRAMEWORK ✓      B01 BLUF + B02 the two additions, before the attack.
WORKED EXAMPLE ✓ B04 — a hostile payload fired, intercepted, and surfaced.
FALSIFIABILITY ✓ B05 — the chain breaks at a person, not a service.
SCAFFOLDED TASK ✓ B06 stands it up and attacks it; BHTF finds the untested categories.
BOOKENDS ✓       B00 cold open · B01 BLUF · BHTF handoff · BOUT restate.
NO-SOURCE-NO-VERDICT ✓ no false-positive rate or adoption metric claimed as measured.
```

## Build note

The landscape render hit the 10-minute background ceiling after 5 of 9 beats and was
stopped; resuming rendered only the remaining 4, since `remotion_scenes.py` skips beats
already on disk. Both Week 5 reels hit the same ceiling at the same point — roughly
2 minutes per 4K beat at `--scale=2` means 9 beats does not fit one window on this
machine. No work was repeated.

## Open items

1. **Replace the illustrative rows and the B00 figures** with real data.
2. **Check the normalizer** against the STEM reel's finding (above).
3. **Runtime 2:08 vs 2:45 target.** Not padded; duration is an output.
4. **Lane-mix warning (not blocking).** `remotion` carries 9/9 beats.
5. **SKIN LINT warning (expected).** `BOUT` uses `HaiTitleOutro`.
6. **Paperwork.** Built with `ART_FACTS=0`.
7. **`./art final` not run** — no label-free master yet.
