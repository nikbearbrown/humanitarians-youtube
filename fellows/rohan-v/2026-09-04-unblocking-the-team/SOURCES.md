# SOURCES — "Unblocking the Team."

## Primary source

Rohan Vijaykumar's own account of the week, given 2026-08-29. Reproduced in
full in [SOURCE-brief.md](./SOURCE-brief.md). This is a progress report, so the
presenter is the primary source for what he did; everything with a number
attached was independently verified below.

## Verified by execution

These were measured, not recalled. Commands run 2026-08-29 on the actual files.

| What | How | Result |
|---|---|---|
| Suno Part 1 duration + resolution | `ffprobe -select_streams v:0 -show_entries stream=width,height -show_entries format=duration` | 3840×2160, 236.55s |
| Suno Part 2 duration + resolution | same | 3840×2160, 188.94s |
| Suno Part 3 duration + resolution | same | 3840×2160, 209.21s |
| All three parts exist | `Test-Path` on each master | all present |
| Series total | arithmetic on the three probed durations | 634.70s = 10:34.70 |
| Beat narration durations | `generate_audio_kokoro.py` output | 19.35 / 24.11 / 30.27 / 22.68 / 12.63 / 10.71 s |
| Reel total | sum of the above | 119.75s = 1:59 |
| The four new components render | `./art scenes --check` | all four `RENDERABLE 16:9` |
| Library gap was real | `./art scenes "<need>"` × 4 | no existing component matched; all four punts genuine |

## Repository sources

| Source | Used for |
|---|---|
| `D:\Rohan\Claude\HAI\lyrical-literacy\SERIES-PLAN.md` | Part titles, core skill per part, the no-screen-recordings standard |
| `D:\Rohan\Claude\HAI\lyrical-literacy\youtube\suno-part-{1,2,3}\` | Existence and measured properties of the three shipped masters |
| `youtube/week-01/2026-08-28-agent-first-brutalist/` | Confirming the walkthrough video referenced in B01 exists and shipped |
| `RohanClaudeHAIbrutalist.art/runtime/remotion/src/tokens/claude.ts` | The exact palette values used by all four new scenes |
| `RohanClaudeHAIbrutalist.art/CLAUDE.md` | Library-first doctrine, audio-first rule, 4K render path |

## Brand hues in B03

The four tool cards use each product's own accent so the chain is scannable.
Discord `#5865F2` is the published blurple. Suno is magenta `#E5197F` — **not**
purple, per the verified Suno UI reference screenshots. Midjourney is rendered
in warm ink `#2F2A26`, which is accurate: its brand is monochrome. Adobe CC is
`#DA1F26`. These are identifying accents on a card, not reproductions of any
logo — no marks are used.

## Not used

- No external web sources. Every claim is either first-hand or measured locally.
- No screen recordings of any product. Every interface in this reel and in the
  Suno series it reports on is drawn in code.
- No AI-generated video. All six beats are deterministic Remotion renders.
