# FACTCHECK — when-cowork-helps-claude-code

All terminal output shown is **illustrative — real transcript, lightly trimmed**.
The session described is the actual `installs` build (video 2), not a reconstruction.

## Figures in this video — all real

| Figure | Claim | Source |
|--------|-------|--------|
| **43** | `ps aux \| grep -i chrome \| wc -l` returned 43 during the stall | real terminal output from the installs session |
| **9 beats** | Nine Manim concept beats had rendered before the stall | `ls youtube/installs/manim/ \| wc -l` confirmed 9 |
| **15/15** | Final compile filled all 15 slots | `compile.py` output: "slots: 15/15 filled — done." |
| **4m 47s** | Shell kept running that long during the stall | `✻ Brewed for 4m 47s · 1 shell still running` — Claude Code status line |

## Source doc

`docs/cowork-and-claude-code.md` — the written form this video is the spoken form of.
All narrative claims trace back to that doc.

## Illustrative vs. reconstructed

- Terminal beats (B00, B02, B04, B09, B12, B99): these show real commands and outputs,
  lightly trimmed for pacing. The B04 chrome count (43), the B02 wait loop, the B12 fix
  commands, and the B09 directory listing are all faithful to the actual session.
- No facts in the narration are fabricated.
