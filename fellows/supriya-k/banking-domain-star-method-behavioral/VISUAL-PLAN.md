# Visual Plan — "The STAR Method Banking Panels Actually Score"

## Lane-mix decision (documented deviation)

**VOX = 0%.** The beat-mix contract's default band is VOX ~20-25%, but this topic — the STAR
framework, banking-specific behavioral competencies, and a self-scoring mock-interview loop — has
no archival-photo referent for the pantry-still (VOX) lane to animate. There is no photograph that
illustrates "risk awareness" or "a self-scoring rubric" the way a tumor-histology still illustrates
a drug-distribution claim. This is the identical justification the structural reference
(`hai-interview-end-to-end`) used for the same deviation on a similarly conceptual topic (the
data-analyst interview's six-stage map and 2026 trends).

The freed capacity moved to MANIM (38.9%) and REMOTION (38.9%), with CARD absorbing the remainder
(22.2%) — within the contract's MANIM 25-40% / REMOTION 30-45% bands, and matching the reference's
own actual split almost exactly (its measured histogram was manim 10/23, remotion 9/23, card 4/23
— same card count, same shape).

## Component note (palette split — not persona branding)

Bookends (`B00`, `B_VERDICT`, `B_YOURTURN`, `B_OUTRO`) render via `ClaudeComposerAsk`,
`ClaudeVerdictArtifact`, and `ClaudeTitleOutro` — all fixed to the **claude** fidelity skin (cream
`#FAF9F5` / ink `#3D3929` / one terracotta accent), no palette prop exists to change this.

Body Remotion cards (`QuoteCard`, `StateCardPair`, `LabelChip`) hardcode the **humanitarians**
accent set (teal `#1F4E5F` / crimson `#E4572E` / slate `#29335C` / gold `#F3A712`, cream
`#F3EBDD` ground) directly in their source — no palette prop exists on these either. This is the
*only* color wiring these three specific shared components have; it is not the "hai" persona or its
channel branding, which this project drops entirely (no `@handle`, no channel name, no "Supriya
for Humanitarians AI" narrator identity — narration says "in for Supriya," full stop).

Body Manim scenes (all 11, including the 4 act cards) are authored to match that same humanitarians
set, so the body reads as one consistent visual language even though it necessarily differs from
the bookends' claude skin. This exact bookend/body split exists in the reference project too, for
the identical structural reason (its `style_preset: "claude-hai"` literally means "claude bookends
+ this card family's body").

## Resolution requirement (render-time, not now)

4K (3840×2160) target, matching the SQL video's precedent in this same toolkit. `compile.py` needs
`--height 2160`; Manim scenes render at `-qk` (4K), not `-qh`.

## Beat-by-beat visual notes

| Beat | Visual |
|---|---|
| B00 | Claude composer, ask answered, "Hi, in for Supriya" greeting |
| B01 | Act card — teal mark, "ACT I / The STAR Framework" |
| B02 | Four badge+label+detail rows (S/T/A/R) building top to bottom |
| B03 | QuoteCard, eyebrow + quote, crimson accent |
| B04 | Act card — crimson mark, "ACT II / What a Banking Panel Listens For" |
| B05 | Three side-by-side panels (risk awareness / control judgment / examiner comfort) |
| B06 | LabelChip, three chips landing in sequence, footer line |
| B07 | QuoteCard before/after mode — struck phrase replaced by the accepted one |
| B08 | Strike-through replacement — "We fixed it." crossed out, replaced by the named-control sentence |
| B09 | Act card — slate mark, "ACT III / Weak Answer, STAR Rewrite" |
| B10 | QuoteCard, the book's weak-answer quote in full |
| B11 | StateCardPair, four cards (S/T/A/R), Result card gold-highlighted |
| B12 | Animated checklist, three checkmarks (vector shapes, not glyphs) |
| B13 | Act card — gold mark, "ACT IV / Daniel's Full-Loop Mock" |
| B14 | Five boxes left to right, Behavioral (4th) highlighted crimson |
| B15 | QuoteCard, the Stage 4 prompt |
| B16 | QuoteCard, Daniel's answer, crimson accent (where it stops) |
| B17 | Five-bar horizontal chart, Behavioral flagged crimson at 1/3, others slate at 2/3 |
| B18 | Allocation bars, Behavioral longest (crimson), one light rep each for the rest, closing line |
| B_VERDICT | ClaudeVerdictArtifact, three-line recap |
| B_YOURTURN | Claude composer, "Your turn." handoff prompt |
| B_OUTRO | ClaudeTitleOutro, title restate + "in for Supriya" sign-off |

## No placeholder slates in the final cut

Every beat resolves through an existing component or a purpose-written, smoke-tested Manim scene
(all 11 verified via low-quality render before this plan was finalized — see build notes). No
`pantry/` request, no slate, no unfilled slot anywhere in `beat_sheet.json`.
