# BUILD-NOTES — chinese-room-explainer-vox

Vox mixed-media conversion of `chinese-room-explainer` (NEU/George → KORE/af_kore).
Final cut: 71.2 s · 8 beats · all slots filled · never publish.

## Beat list

| ID  | Shot type | Medium | One-line narration |
|-----|-----------|--------|--------------------|
| B00 | GRAPHIC   | ClaudeComposerAsk (type-on) | "Kia ora, Kore — Can a machine truly think?" cold open |
| B01 | STILL     | searle_1.png (Searle at desk) | Searle alone in a locked room with a rulebook and Chinese symbols |
| B02 | GRAPHIC   | MedhavyConceptCard (illustrate) | "picture this" — the sealed-room image made concrete |
| B03 | STILL     | searle_03.png (frantic papers) | He shuffles paper perfectly — and understands nothing |
| B04 | STILL     | chinese-speaker-04.png (person holding message) | From outside, the room speaks Chinese; from inside, silence |
| B05 | STILL     | turing_05.png (Turing caricature) | The Turing Test passes; Searle says that's not enough |
| B06 | GRAPHIC   | ClaudeVerdictArtifact (stagger) | Five-line summary card — "syntax is not semantics" punchline |
| B07 | GRAPHIC   | ClaudeTitleOutro (fade) | "Kore, in for Humanitarians AI." sign-off |

## Slot status

All 8/8 slots filled — no slates.

| ID  | Source file | Size | Notes |
|-----|-------------|------|-------|
| B01 | `public/chinese-room-explainer/searle_1.png` | 999×677 | **Undersized** — upscale recommended |
| B03 | `public/chinese-room-explainer/searle_03.png` | 1456×816 | Slightly undersized — minor upscale |
| B04 | `public/chinese-room-explainer/chinese-speaker-04.png` | 555×816 | **Undersized** — upscale recommended |
| B05 | `public/chinese-room-explainer/turing_05.png` | 896×1344 | Undersized — minor upscale |

Compiler warned: upscale artifacts possible on all four stills. Run through an AI upscaler (e.g. Topaz, Real-ESRGAN) at 2× before final delivery if crispness matters.

## Motion histogram warnings

- `kenburns` carries 4/8 beats (50%) — over the ~40% pantry cap. Acceptable for this ink-illustration format; the source imagery is static by nature.
- No hard errors. Compile completed cleanly.

## IN-FOR-BEAR LAW compliance

- B00 greeting: "Kia ora, Kore" ✓
- Narration opens: "…this is Kore, in for Humanitarians AI." ✓
- B07 subline: "Kore, in for Humanitarians AI." ✓
- "Wagwan" does not appear anywhere ✓

## Open the cut

```
open ai1-cli/remotion/demos/chinese-room-explainer-vox/chinese-room-explainer-vox-cut.mp4
```
