"""Writes SHOTLIST.md, PROMPTS.md and script.md from beat_sheet.json (run after `make_sheet.py finish`)."""
import json
from pathlib import Path

REEL = Path(__file__).resolve().parent
s = json.loads((REEL / 'beat_sheet.json').read_text())
T = s['metadata']['title']
beats = s['beats']
total = sum(b['actual_duration_s'] for b in beats)

sl = [f'# SHOTLIST — {T}', '',
      f'16:9 master 3840×2160, 30 fps, {total:.1f} s; a native 9:16 companion (2160×3840) is built from the same beats. '
      'Every beat is a Remotion composition rendered at 4K; no stock footage, no screenshots, no generated images.', '',
      '| Beat | Act | Start | Length | Composition | What the viewer sees |', '|---|---|---|---|---|---|']
t = 0.0
for b in beats:
    r = b['shot']['remotion']
    sl.append(f"| {b['beat_id']} | {b['act']} | {t:6.1f} s | {b['actual_duration_s']:5.2f} s | `{r['pattern']}` | {b['shot']['show'][0]['event']} |")
    t += b['actual_duration_s']
(REEL / 'SHOTLIST.md').write_text('\n'.join(sl) + '\n')

pr = [f'# PROMPTS — {T}', '', 'Every prompt typed on screen. None was sent to a model during the build; '
      'the cold-open answer lines summarize the survey and are labelled illustrative.', '']
for b in beats:
    p = b['shot']['remotion']['props']
    if b['shot']['remotion']['pattern'] == 'ClaudeComposerAsk':
        pr += [f"## {b['beat_id']} · {b['act']} · greeting \"{p['greeting']}\"", '', '```text', p['command'], '```', '',
               f"Running line: {p['runningText']}", ''] + [f'- {o}' for o in p.get('output', [])] + ['']
(REEL / 'PROMPTS.md').write_text('\n'.join(pr) + '\n')

sc = [f'# Script — "{T}"', '', '**Narrator:** Yeshwanth Balaji, voiced by the local AI voice Kokoro `am_onyx` (speed 0.95; '
      'not a recording) · **Channel:** @HumanitariansAI · **Skill:** `ai-explainer` (claude-hai)', '',
      f'Full narration, every beat, exactly as synthesized. Total {total:.1f} s. The audio is the master clock.', '']
for b in beats:
    sc += [f"**{b['beat_id']} · {b['act']} · {b['actual_duration_s']:.1f} s**", '', b['narration_text'], '']
(REEL / 'script.md').write_text('\n'.join(sc) + '\n')
print('wrote SHOTLIST.md PROMPTS.md script.md', round(total, 1))
