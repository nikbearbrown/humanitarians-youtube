# SHOTLIST.md — What is Brutalist?

One row per beat: beat ID · shot type · source · what it shows.

| Beat | Act      | Type    | Source | What it shows |
|------|----------|---------|--------|---------------|
| B00  | INTRO    | REMOTION | own   | BrutalistTerminalOpen: `$ art explainer-video "What is Brutalist?"` types out; checklist ticks in |
| B01  | HOOK     | GRAPHIC  | own   | Manim: big button → click → filmstrip → SLOP stamp (teardown palette) |
| B02  | ARGUMENT | GRAPHIC  | own   | Manim: screen playing vs AI node with crossed-out eye; dashed line never connects |
| B03  | ARGUMENT | GRAPHIC  | own   | Manim: three question cards flip up ("funny?", "interesting?", "did it land?"); human checks them |
| B04  | ARGUMENT | REMOTION | own   | NikBearBrownCodeBlock: Manim code snippet, "the machine's native tongue" |
| B05  | ARGUMENT | GRAPHIC  | own   | Manim: 20:00:00 clock (human debugging) vs 0:00:03 (machine fixed); waste bar drains |
| B06  | TURN     | GRAPHIC  | own   | Manim: balance beam — "all human" sinks (time-sink), "all machine" rises (slop); BRUTALIST marks the middle |
| B07  | REVEAL   | GRAPHIC  | own   | Manim HERO: baton stroke on dark canvas; "YOU ARE THE CONDUCTOR" in EB Garamond; tool row below |
| B08  | REVEAL   | GRAPHIC  | own   | Manim: split frame — score annotations (left) driving tool-orchestra (right); baton arrow |
| B09  | HOW      | GRAPHIC  | own   | Manim: beat_sheet.json glows at center; arrows fan out to todo.json, STATUS.md, the cut |
| B10  | HOW      | REMOTION | own   | NikBearBrownTerminalAsk: `$ art fill-in` with multi-line fill output |
| B11  | HOW      | GRAPHIC  | own   | Manim: request card → pantry → timeline slot (auto-conformed) |
| B12  | DEMO     | REMOTION | own   | NikBearBrownTerminalAsk: `$ ./setup` with capability readiness table |
| B13  | DEMO     | REMOTION | own   | NikBearBrownCodeBlock: three ./art commands (--list, todo, run) |
| B14  | CLOSE    | GRAPHIC  | own   | Manim: playlist rail builds left to right — five video types with ./art commands |
| B99  | OUTRO    | REMOTION | own   | BrutalistCommentCTA: "// you bring the taste — the machine brings the hands" |

All beats: `source = own`. No external footage, stock video, or AI-generated media.
All Manim beats: rendered by pipeline. All Remotion beats: rendered by pipeline.
Zero request cards — this reel is 100% pipeline-renderable.
