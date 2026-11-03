"""Writes SHOTLIST.md from the beat sheet, cues.json and the word clock: the beat table, then every
cue with its anchor phrase, measured fraction and time. Run after sync_cues.py.

python write_shotlist.py "<one-paragraph intro>"
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sheet = json.loads((HERE / "beat_sheet.json").read_text(encoding="utf-8"))
cues = json.loads((HERE / "cues.json").read_text(encoding="utf-8"))
NEW = {p.stem for p in (HERE.parents[3] / "HAI/RohanClaudeHAIbrutalist.art/runtime/remotion/src/scenes").glob("*.tsx")}
intro = sys.argv[1] if len(sys.argv) > 1 else ""
LIB = {"ClaudeComposerAsk", "HaiApplyCard", "HaiTitleOutro", "HaiProgressSignupChain", "HaiProgressOverturned",
       "HaiVerdictSplit", "HaiProgressRoadmap"}

beats = sheet["beats"]
total = sum(b["actual_duration_s"] for b in beats)
n_auth = sum(len([k for k in v]) for k, v in cues.items() if k != "_comment")
n_res = sum(len(b["shot"]["remotion"]["props"].get("cues", {})) for b in beats)
out = [f"# SHOTLIST — \"{sheet['metadata']['title']}\"", "",
       f"{len(beats)} beats, {total:.2f}s ({int(total // 60)}:{int(total % 60):02d}). Every duration is the measured "
       "Kokoro narration length (plus, where noted, the listening clips appended by mix_listen.py); the visuals are "
       "cut to fit the audio, never the other way round.", "",
       f"**Word-clock choreographed.** `align.py` (faster-whisper) measured when every word is spoken, `cues.json` "
       f"names an anchor phrase per reveal, and `sync_cues.py` wrote the resolved fractions into "
       f"`shot.remotion.props.cues`. {n_auth} cues authored, {n_res} resolved.", ""]
if intro:
    out += [intro, ""]
out += ["| Beat | Act | In | Dur | Component | Lane |", "|---|---|---|---|---|---|"]
t = 0.0
for b in beats:
    pat = b["shot"]["remotion"]["pattern"]
    lane = "library" if pat in LIB else "**new**"
    out.append(f"| {b['beat_id']} | {b.get('act','')} | {int(t // 60)}:{int(t % 60):02d} | {b['actual_duration_s']:.2f}s | `{pat}` | {lane} |")
    t += b["actual_duration_s"]
out += ["", "## Choreography — what happens, and on which word", ""]
for b in beats:
    bid, pat = b["beat_id"], b["shot"]["remotion"]["pattern"]
    out += [f"### {bid} — {b.get('act','')} · `{pat}`", "", f"> {b['narration_text']}", ""]
    c = b["shot"]["remotion"]["props"].get("cues", {})
    if c:
        out += ["| cue | anchor phrase | fraction | at |", "|---|---|---|---|"]
        for k, v in sorted(c.items(), key=lambda kv: kv[1]):
            phrase = cues.get(bid, {}).get(k, "")
            out.append(f"| `{k}` | “{phrase}” | {v:.3f} | {v * b['actual_duration_s']:.2f}s |")
        out.append("")
    for clip in b.get("listen_clips", []):
        out.append(f"- listening clip **{clip['label']}** `{clip['file']}` {clip['start_s']:.2f}–{clip['end_s']:.2f}s "
                   f"(gain {clip['gain_db']:+.2f} dB to the narration's level)")
    if b.get("listen_clips"):
        out.append("")
(HERE / "SHOTLIST.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("wrote SHOTLIST.md", len(out), "lines")
