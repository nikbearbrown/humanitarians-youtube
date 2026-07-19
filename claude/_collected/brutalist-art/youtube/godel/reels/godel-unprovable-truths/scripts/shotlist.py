#!/usr/bin/env python3
import json, os, urllib.parse
GODEL="/sessions/affectionate-sharp-rubin/mnt/bear-textbooks/books/unreal-reels/music/godel"
REELS=os.path.join(GODEL,"reels","godel-unprovable-truths")
bs=json.load(open(os.path.join(REELS,"beat_sheet.json")))
m=bs["metadata"]; beats=bs["beats"]

def links(terms):
    out=[]
    for t in terms:
        q=urllib.parse.quote(t)
        out.append(f'  - `{t}` — '
            f'[LOC](https://www.loc.gov/search/?q={q}&fo=json) · '
            f'[Wikimedia](https://commons.wikimedia.org/w/index.php?search={q}) · '
            f'[Internet Archive](https://archive.org/search?query={q}) · '
            f'[Smithsonian](https://www.si.edu/search?edan_q={q})')
    return out

L=[]
L.append(f"# SHOTLIST — {m['title']}")
L.append("")
L.append(f"*{m['series']} · {' · '.join(m['artists'])} · slate cut (vox-explainer pass 1)*")
L.append("")
L.append(f"**Master audio:** `{m['master_audio']}` · **{m['total_duration_s']}s** · "
         f"{m['width']}×{m['height']} @ {m['fps']}fps · style: {m['style']}")
L.append("")
L.append(f"**Slots:** {m['n_beats']} beats — **{m['n_filled']} filled** from the pantry, "
         f"**{m['n_slate']} slates** to build/source.")
L.append("")
L.append("**How the slot contract works:** every beat on the timeline is a per-beat mp4 in "
         "`clips/`. To fill or swap a slot, drop a file in `media/` named after the beat "
         "(`media/B08.png` as a still/i2v seed, or `media/B08.mp4` to upgrade). "
         "Precedence at rebuild: `media/B08.mp4` > `media/B08.png` > slate placeholder. "
         "Re-run the assembler to recompile only changed slots. Timing is **EST** "
         "(word-weighted, pinned to the song's energy anchors at 6 / 40 / 196 / 217 s) — "
         "replace with forced alignment when ready; it is the master clock.")
L.append("")
L.append("---")
L.append("")

scene=None
for b in beats:
    if b["scene_index"]!=scene:
        scene=b["scene_index"]
        L.append(f"## Scene {scene}")
        L.append("")
    s=b["shot"]
    head=(f'### {b["beat_id"]} · {b["t_start_s"]}–{b["t_end_s"]}s ({b["duration_s"]}s) · '
          f'{s["type"]} × {s["source"]} · {b["slot_status"]}')
    L.append(head)
    if b["lyric"]:
        L.append(f'> {b["lyric"]}')
    L.append("")
    L.append(f'**On-screen caption:** {b["caption"] or "—"}')
    L.append("")
    L.append(f'**Teaches:** {b["teach"]}')
    L.append("")
    if b["media"]:
        L.append(f'**Filled from pantry:** `{b["media"]}` → treated (desaturate ~80%, '
                 f'contrast 1.12, cream wash) and conformed to {b["duration_s"]}s.')
        L.append(f'*Swap:* replace `media/{b["beat_id"]}.mp4` to change this shot.')
    else:
        L.append(f'**Build prompt:** {b["fill_prompt"]}')
        if b["viz"]:
            L.append(f'**viz:** `{json.dumps(b["viz"])}`')
        if b["archive_queries"]:
            L.append("**Archive search:**")
            L+=links(b["archive_queries"])
        L.append(f'*Fill:* `media/{b["beat_id"]}.png` (placeholder / i2v seed) or '
                 f'`media/{b["beat_id"]}.mp4` (final).')
    L.append("")
    L.append("---")
    L.append("")

open(os.path.join(REELS,"SHOTLIST.md"),"w").write("\n".join(L))
print("wrote SHOTLIST.md", len(L), "lines")

# histogram / rhythm lint
from collections import Counter
c=Counter(b["shot"]["type"] for b in beats)
print("shot-type histogram:", dict(c))
run=1; flags=[]
for i in range(1,len(beats)):
    if beats[i]["shot"]["type"]==beats[i-1]["shot"]["type"]:
        run+=1
        if run>2: flags.append(beats[i]["beat_id"])
    else: run=1
print("rhythm-lint >2 same-type-in-a-row at:", flags or "none")
