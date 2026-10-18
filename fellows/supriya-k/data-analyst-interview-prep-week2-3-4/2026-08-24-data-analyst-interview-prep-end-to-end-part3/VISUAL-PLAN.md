# Visual Plan — The STAR Method

Palette: **humanitarians** — CREAM `#F3EBDD` ground, INK `#2F2A26` text, TEAL `#1F4E5F` (good/kept/true), CRIMSON `#E4572E` (bad/broken/missing), SLATE `#29335C` (structure/entity cards), GOLD `#F3A712` (highlighter fill only, never text), SAGE `#A8C686` (unused this reel — no human/growth motif needed). Typography: EB Garamond (serif, labels/greeting) + Montserrat (sans, UI chrome).

No screenshots of any real product UI except the Claude-style composer bookends (B00, B10). No paid stock/AI image generation — every visual is Remotion-native (`shot.source: "own"` / `"remotion"`), so nothing needs sourcing from `pantry/`.

| Beat | Shot type | Component | What's on screen | Motion |
|---|---|---|---|---|
| B00 | REMOTION | `ClaudeComposerAsk` | Question typed, answered with 3 output lines | type-on |
| B01 | GRAPHIC | `StateCardPair` | 4 cards (S/T/A/Result) build left→right | illustrate |
| B02 | GRAPHIC | `LabelChip` | 5 question-type chips + anchor phrase | illustrate |
| B03 | GRAPHIC | `StateCardPair` | S-T-A filled TEAL, Result empty + CRIMSON flash | illustrate |
| B04 | GRAPHIC | `QuoteCard` | Question card → weak-answer quote, CRIMSON strike | illustrate |
| B05 | GRAPHIC | `StateCardPair` | S, T, A cards type in from the real story | illustrate |
| B06 | GRAPHIC | `StateCardPair` + highlight | R card + GOLD sweep under "~12% inflation" | illustrate |
| B07 | GRAPHIC | `LabelChip` (paired) | 5 story cards → 5 competency tags | illustrate |
| B08 | GRAPHIC | `QuoteCard` (before/after) | "it went faster" struck → "3h→20min" in GOLD | illustrate |
| B09 | GRAPHIC | `ClaudeVerdictArtifact` | 3 bare-sentence recap lines, card ~84% frame width | stagger |
| B10 | REMOTION | `ClaudeComposerAsk` (greeting "Your turn.") | Full suggested prompt typed | type-on |
| B11 | REMOTION | `ClaudeTitleOutro` | Title restated + `@HumanitariansAI` handle | fade |

## Rules applied
- **SHOW-DON'T-TELL**: every body beat's `show` block (in `beat_sheet.json`) names the on-screen event tied to the spoken phrase — nothing is a static slide with narration over it.
- **One accent per beat**: TEAL for "correct/complete," CRIMSON for "missing/wrong," GOLD strictly as a highlighter sweep (B06, B08), never as text color.
- **No screenshots** beyond the two composer bookends; all concept beats are native Remotion components, in-repo palette tokens (`runtime/remotion/src/tokens/humanitarians.ts`).
- **Bookend spine** (mandatory, shared skeleton across all three builder skills): cold open (`ClaudeComposerAsk`, ask answered) → body → `ClaudeVerdictArtifact` recap → `ClaudeComposerAsk` "Your turn." handoff (prompt read + discussed) → `ClaudeTitleOutro`.
- **`@HumanitariansAI` first-beat overlay**: per the `hai` skill, `compile.py` burns the channel handle as a centered bottom-of-frame ink serif caption on B00 only (auto — no manual beat needed).

## Resolution checklist (for the render step — not done yet)
- [ ] Every beat renders natively at **3840×2160** (4K) — run Remotion/Manim exports at that frame size, not upscaled from 1080p.
- [ ] `compile.py [reel] --height 2160` for the final master (default height is 720 — must be overridden).
- [ ] Before compiling the master, spot-check each beat's rendered clip resolution (`ffprobe -show_entries stream=width,height`) and confirm 3840×2160 for all 12 beats.
- [ ] No placeholder/slate frames survive into the final master — every beat above is a native Remotion component (no pantry stills needed), so there should be zero un-filled slots by the time of final compile.
