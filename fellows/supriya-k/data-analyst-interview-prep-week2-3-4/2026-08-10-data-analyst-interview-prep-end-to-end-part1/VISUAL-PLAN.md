# Visual Plan — "The Data Analyst Interview, End to End"

deep-explainer · 16:9 · palette `humanitarians` (CREAM `#F3EBDD`, INK `#2F2A26`,
TEAL `#1F4E5F` good/kept, CRIMSON `#E4572E` bad/lost, SLATE `#29335C` structure,
GOLD `#F3A712` highlighter-only, SAGE `#A8C686` human) · type EB Garamond (serif) /
Montserrat (sans).

## Lane-mix decision (documented deviation)

The deep-explainer quota targets ~20–25% VOX (pantry stills, Ken-Burns/cutout
treatment). **This episode uses 0% VOX by deliberate choice.** The content —
an interview-process map, a "what's tested" scoring matrix, three abstract
2026 trend shifts, and a prep-plan calendar — has no archival or photographic
referent. A stock photo of "two people at a job interview" or "a laptop with
code on it" would be generic filler standing in front of the narration rather
than teaching anything extra, which is precisely what the VOX lane exists to
avoid when it's forced. Instead:

- **MANIM (10 beats, ~43% of body+card lanes)** carries anything structural/
  countable: the six-stage chip sequence, the three-row matrix builds, the
  line-by-line AI-code check, Maya's profile chips, and the three weekly
  calendar blocks.
- **REMOTION (9 beats, ~39%)** carries comparisons and scale: the
  compressed-vs-stretched timeline, the quote card, the three 2026-shift chips,
  the raw-compute-vs-framing scale, the can/can't divergence, and the final
  uneven-bars payoff visual.
- **CARD (4 beats, ~17%)** — one per act.

This is logged as an intentional deviation from the ~20–25% VOX target,
per the deep-explainer skill's own allowance to use judgment and document the
call rather than force an ill-fitting lane. Re-open this decision only if a
future revision finds a genuine photographic angle (e.g., real interview-room
photography with proper rights clearance).

## Resolution requirement (render-time, not now)

Every beat and the final master must render at **3840×2160 (4K)**.
`compile.py` defaults to `--height 720`; use `--height 2160` and confirm the
computed width lands at 3840 (16:9). **Check each beat's actual rendered
frame resolution before compiling the master** — a per-beat resolution
checklist should be run as part of the render step (not part of this planning
package).

## Beat-by-beat

| Beat | Act | Lane | Component | Visual |
|---|---|---|---|---|
| B00 | OPEN | bookend | `ClaudeComposerAsk` | Cold open, ask lands answered, greeting "Supriya, Humanitarians AI" |
| B01 | I | card | `HaiSegmentCard` | "The Six Stages" |
| B02 | I | manim | `B02_SixStageChips` | Six chips light TEAL in sequence, narration-timed |
| B03 | I | remotion (scale) | `HaiScale` | Startup (short bar) vs. larger co. (long bar) timeline |
| B04 | I | remotion (structure) | `HaiLayerStack` | Chips collapse into a column — bridges to the matrix |
| B05 | II | card | `HaiSegmentCard` | "What's Tested Where" |
| B06 | II | manim | `B06_MatrixRows12` | Table build, rows 1–2 |
| B07 | II | manim | `B07_MatrixRows34` | Table build, rows 3–4 |
| B08 | II | manim | `B08_MatrixRows56` | Table build, rows 5–6, full matrix holds |
| B09 | II | remotion (quote) | `HaiQuoteCard` | Verbatim Ch.3 "what's tested here" quote, cited |
| B10 | II | remotion (structure) | `HaiLayerStack` | Matrix dims to one line: "correct ≠ landed" |
| B11 | III | card | `HaiSegmentCard` | "What Changed by 2026" |
| B12 | III | remotion (structure) | `HaiChipGrid` | Chip 1/3 lands: AI-tool fluency |
| B13 | III | manim | `B13_LineByLineCheck` | Code scan, one line flags CRIMSON |
| B14 | III | remotion (structure) | `HaiChipGrid` | Chip 2/3 lands: messy-data take-homes; jumble→clock+slide |
| B15 | III | remotion (scale) | `HaiScale` | Chip 3/3 lands: balance tips to framing/judgment |
| B16 | III | remotion (structure) | `HaiLayerStack` | Condenses to a calendar icon — bridges to Act IV |
| B17 | IV | card | `HaiSegmentCard` | "The Worked Plan" |
| B18 | IV | manim | `B18_MayaProfile` | Profile chip stack + 3-week countdown |
| B19 | IV | remotion (divergence) | `HaiDivergence` | Can-do (TEAL) vs. hasn't-done (CRIMSON) |
| B20 | IV | manim | `B20_Week1Block` | Calendar strip, Week 1, 90 min/day blocks |
| B21 | IV | manim | `B21_Week2Block` | Calendar strip, Week 2, uneven block sizes |
| B22 | IV | manim | `B22_Week3Block` | Calendar strip, Week 3, mock-loop + re-drill arrow |
| B23 | IV | remotion (scale) | `HaiScale` | Six uneven bars — the thesis payoff image |
| B_VERDICT | CLOSE | bookend | `HaiVerdictArtifact` | Five-line recap card |
| B_YOURTURN | CLOSE | bookend | `ClaudeComposerAsk` | "Your turn." — full prompt typed + read |
| B_OUTRO | CLOSE | bookend | `HaiTitleOutro` | Title re-read, `@HumanitariansAI` handle |

## Component note

`HaiSegmentCard`, `HaiScale`, `HaiChipGrid`, `HaiLayerStack`, `HaiDivergence`,
`HaiQuoteCard`, `HaiVerdictArtifact`, `HaiTitleOutro` are the humanitarians-palette
equivalents of the claude-liam Remotion patterns already in
`runtime/remotion/src/scenes/` (`FluencySegmentCard`, `DtlScale`, `DtlChipGrid`,
etc. — see the reference deep-explainer example). If these HAI-retint variants
don't exist yet in `runtime/remotion/src/scenes/`, they need to be added as a
palette retint (swap `tokens/claude.ts` for `tokens/humanitarians.ts`) before
render — not a new component design, a token swap. This is a render-time task,
not part of this planning package.

## No placeholder slates in the final cut

Per the project's requirement, none of the above beats are planned as
permanent slates — every beat has an assigned MANIM/REMOTION component. The
only acceptable "slate" state is a temporary one during the render pipeline's
first-pass previz (Gate D1), before the components above are actually
rendered.
