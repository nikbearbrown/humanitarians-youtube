# BUILD-LOG — "Memory and Context"

Built 2026-08-13, dated Friday 2026-08-28. Toolkit `brutalist.art` (`ai-explainer`),
Kokoro `am_onyx`, **cost $0.00**.

## Result

| Cut | Format | Runtime | Beats | Slates |
|---|---|---|---|---|
| 16:9 master | 3840×2160 | ~3:31 | 13 | 0 |
| 9:16 Short | 2160×3840 | ~2:47 | 9 + endcard | 0 |

## Visual QC

**Zero defects, first pass.** The defect classes that cost re-renders on earlier videos were
designed out at authoring time: feed labels short enough not to orphan a word, mono-table
widths computed from the longest line before authoring, and both `ClaudeWindow` beats
authored `numbered: false` so no table could render as a numbered list.

Two contact-sheet frames looked incomplete (B02, B06) and were checked at full resolution
before being believed — both were mid-animation. That is now the fifth and sixth false alarm
of that kind; the contact sheet samples one frame per beat, so a missing item there is a
question, never a finding.

## The error worth recording

`first_overflow()` originally capped at 40 turns, so the largest budget returned `None`. Left
alone, B07 would have shown **"first overflow at turn None"** on screen while the narration
claimed overflow is unavoidable — the video contradicting its own falsifiability beat, in the
one beat whose entire job is honesty. Caught before audio; horizon raised to 500; the real
answer is turn 81.

Also corrected before audio: the narration said "nine lines" for `budget_row()`; the counted
answer is ten.

## Toolkit work this build required

The 9:16 half was **blocked** — only three portrait compositions existed. Five were written
and registered (`runtime/remotion/src/scenes/ClaudeIllu916.tsx`, ~310 lines):
`ClaudeScienceLayerStack916`, `ClaudeScienceSourceFlow916`, `ClaudeScienceChipGrid916`,
`CwcConceptCard916`, `ClaudeCodeBeat916`. They are **native portrait layouts, not scaled
landscape** — centre-cropping generated graphics slices code and tables mid-word.

Also fixed: `ClaudeWindow916` never honoured `numbered`, so both tables rendered as numbered
lists with collapsed columns; and its line type is now auto-fitted to the longest line so a
wide column cannot run past the card edge.

These changes live in the **`brutalist.art` repo**, not this one, and need their own PR —
without them the 9:16 half of this build is not reproducible.

## Late revision

After the cuts were first mastered, the fellow set a standing rule: **no episode or week
numbers anywhere.** B00's narration and `greeting`, and BOUT's narration and `subline`, were
rewritten and re-rendered across all four cuts; the video now opens "Today we are going to
learn …" and signs off on the title alone.

## Status

Both cuts rendered, QC clean, gates signed. **Not published, not uploaded.**
