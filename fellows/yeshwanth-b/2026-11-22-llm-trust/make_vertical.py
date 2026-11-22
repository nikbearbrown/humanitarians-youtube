"""Finish the `./art vertical` plan for this reel.

    python3 make_vertical.py

./art vertical rewires every beat to its *916 composition. This copies the parent's padded
audio (the exact beat lengths), sets the portrait canvas, and gives the hesitant writer a
shorter overview: the 9:16 writer card allows 12 words, counting the corrected phrase.
"""
import json
import shutil
from pathlib import Path

REEL = Path(__file__).resolve().parent
parent = {b['beat_id']: b for b in json.loads((REEL / 'beat_sheet.json').read_text())['beats']}
path = REEL / 'vertical/beat_sheet.json'
sheet = json.loads(path.read_text())
(REEL / 'vertical/audio').mkdir(exist_ok=True)
for b in sheet['beats']:
    pb = parent[b['beat_id']]
    shutil.copy2(REEL / pb['audio_file'], REEL / 'vertical' / pb['audio_file'])
    b['audio_file'] = pb['audio_file']
    b['actual_duration_s'] = pb['actual_duration_s']
    b['shot']['remotion']['props']['durationSeconds'] = pb['actual_duration_s']
    if b['beat_id'] == 'B01':
        props = b['shot']['remotion']['props']
        props.update(text='Trusting an AI\nis a feeling.\nTest it four ways.', triggerWords='is a feeling',
                     replacementWords='is something you measure', fontSize=150, lineSpacing=1.5)
        final = props['text'].replace(props['triggerWords'], props['replacementWords'])
        assert len(props['text'].split()) <= 12 and len(final.split()) <= 12
    if b['beat_id'] == 'B11':   # phone-length checklist details; the 16:9 cut keeps the full wording
        short = {'Can I verify it?': 'from another source', 'Does rewording change it?': 'ask another way',
                 'Does the reasoning hold?': 'read the steps', 'Are the stakes high?': 'a person checks'}
        for it in b['shot']['remotion']['props']['items']:
            it['detail'] = short[it['label']]
    if b['beat_id'] == 'B13':   # the shared portrait verdict card sets small type; fuller lines fill the tall frame
        b['shot']['remotion']['props']['artifactLines'] = ['Trust in AI isn’t a feeling. It’s something you measure, in four ways that work together.', 'Metrics and benchmarks measure how often the model is right, on the same test for every model.', 'Bias tests change one detail and check whether the answer stays fair.', 'Interpretability looks inside: embeddings and explanations show why it answered.', 'Human review catches the tone, context and subtle errors that scores miss.', 'Each one catches what the others miss, so use them together.']
    if b['beat_id'] == 'B08':   # portrait map: the fruit label sits below its cluster, clear of "kitten"
        b['shot']['remotion']['props']['groupBelow'] = ['fruit']
md = sheet['metadata']
md['width'], md['height'], md['aspect_ratio'] = 2160, 3840, '9:16'
md['note'] = md.get('note', '') + ' Vertical companion: every beat re-rendered with its native *916 composition; same narration and timing.'
path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
for f in ('SHOTLIST.md', 'FACTCHECK.md', 'PROMPTS.md', 'SOURCES.md'):
    if (REEL / f).exists():
        shutil.copy2(REEL / f, REEL / 'vertical' / f)
print('vertical sheet ready')
