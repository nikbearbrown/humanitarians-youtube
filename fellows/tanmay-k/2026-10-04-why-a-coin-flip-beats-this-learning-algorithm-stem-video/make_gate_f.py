#!/usr/bin/env python3
"""Writes the GATE F records compile.py requires for a final: SHOTLIST.md, PROMPTS.md (both cuts) and
short/FACTCHECK.md. Generated from the beat sheets, so they can't describe a different film."""
import json
from pathlib import Path

HERE = Path(__file__).parent

PROMPTS = """# PROMPTS

No AI-image, AI-video or CLI-explainer beats in this project. Every beat is a Remotion scene drawn in
code (`CorridorOFL`, `CoinCurveOFL`, `ClaudeArtifactCardFullOFL`, `ClaudeTitleOutroFullOFL`, and their
916 variants), with its content written into `beat_sheet.json`'s `shot.remotion.props` by
`build_beat_sheet.py` / `short/build_short_sheet.py`. All numbers on screen come from
`experiment/results.json`, `experiment/rps_results.json` or the book (FACTCHECK.md). There are no
prompts to record.

Narration is Kokoro TTS (`am_onyx`, local) voicing the Gate P-signed scripts (`PEDAGOGY.md`).
"""


def heading(p):
    return p.get("heading") or p.get("artifactHeading") or p.get("title") or ""


def shotlist(sheet, title):
    rows = [f"# SHOTLIST: {title}", "",
            "Generated from `beat_sheet.json` by `make_gate_f.py`. Every beat is a code-drawn Remotion scene",
            "rendered in SIL OFL fonts only (`withOflFonts`). No photographs, stock, logos or AI-generated",
            "imagery. The book's own figures (CC BY-NC-ND) are never reproduced; every chart is drawn from our",
            "data.", ""]
    for b in sheet["beats"]:
        rem = b["shot"]["remotion"]
        rows.append(f"{b['beat_id']} {rem['pattern']} (Remotion, {b['shot'].get('motion', '')}) · "
                    f"{b.get('actual_duration_s', b['estimated_duration_s'])}s · {heading(rem['props'])}")
    return "\n".join(rows) + "\n"


long_sheet = json.loads((HERE / "beat_sheet.json").read_text())
short_sheet = json.loads((HERE / "short" / "beat_sheet.json").read_text())
(HERE / "SHOTLIST.md").write_text(shotlist(long_sheet, long_sheet["metadata"]["title"]))
(HERE / "short" / "SHOTLIST.md").write_text(shotlist(short_sheet, short_sheet["metadata"]["title"]))
(HERE / "PROMPTS.md").write_text(PROMPTS)
(HERE / "short" / "PROMPTS.md").write_text(PROMPTS)

refs = []
for b in short_sheet["beats"]:
    refs.append(f"| {b['beat_id']} | {', '.join(r.split()[-1] for r in (b.get('factcheck_ref') or [])) or '— (sign-off / task, no claim)'} |")
(HERE / "short" / "FACTCHECK.md").write_text(
    "# FACTCHECK: the Short\n\nThe Short makes no claim the long form doesn't. Every row it relies on is "
    "audited in `../FACTCHECK.md`, against the book (pages cited) and our runs.\n\n| Beat | FACTCHECK rows |\n|---|---|\n"
    + "\n".join(refs) + "\n")
print("SHOTLIST.md, PROMPTS.md (both cuts), short/FACTCHECK.md written")
