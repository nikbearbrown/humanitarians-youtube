# SHOTLIST — Your Feature Importance Is Lying

Typed work order. All ten beats are Remotion; no human media, no open slots.

| Beat | Act | Composition | What must be on screen | Accent (terracotta) |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | "Merhaba, Liam"; the ask; `@HumanitariansAI`; `Fable 5` | send button |
| B01 | BLUF | `BrutalistHesitantWriter` | "matters" typed, reconsidered, replaced with "is missed" | the doomed word |
| B02 | SETUP | `BarChart` | 1 copy: temp 1.68 vs day 0.27, **accent on temp** (correct answer) | temp bar |
| B03 | TURN | `BarChart` | 2 copies: 0.58 / 0.58 / day 0.27, **accent on day** (closing in) | day bar |
| B04 | HERO | `BarChart` | 3 copies: day 0.27 **on top**, three temp bars at 0.12, accent on day | day bar |
| B05 | EVIDENCE | `FormACard` | Two **verbatim** scikit-learn quotes + source line. Must stay exact | — |
| B06 | LAND | `WantQuote` | Pull quote; spark "Duplicate a signal and you hide it." `dataCite` empty | quote mark |
| B07 | FIX | `FormACard` | Four remedies | — |
| B08 | HANDOFF | `ClaudeComposerAsk` | "Your turn."; a pasteable prompt | send button |
| B09 | OUTRO | `HaiTitleOutro` | Title restate + SUBSCRIBE + `@HumanitariansAI`. No mascot, no subline | — |

**B02 → B03 → B04 is the argument.** Same composition, same scale, only the
data changes, so the inversion is visible as a reordering. The accent moves
from temp to day deliberately: it tracks what the *ranking* says is most
important, which is the thing going wrong.

**Every number on those three charts comes from `importance_evidence.py`.**
Do not adjust them for visual balance.

**B06 `dataCite` must be empty** (see bugs-and-fixes X14).

**Segment titles ALL CAPS** per the published style.

**Declared sparse** (`qc.sparse: true`): B01, B02, B03, B04, B05, B06, B07, B09.

**Shorts:** all compositions have `916` variants; `BarChart916` was built in
the 09-18 run.
