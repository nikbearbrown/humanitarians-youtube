"""Finish the `./art vertical` plan for this reel.

    python3 make_vertical.py

./art vertical rewires every beat to its *916 composition. This copies the parent's padded
audio (the exact beat lengths), sets the portrait canvas, and gives the hesitant writer a
shorter overview: the 9:16 writer card allows 12 words, counting the corrected phrase.
"""
import json
import shutil
import sys
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
        props.update(text='An AI agent\nis a smarter chatbot.\nYou review the work.', triggerWords='is a smarter chatbot',
                     replacementWords='runs its own loop', fontSize=150, lineSpacing=1.5)
        final = props['text'].replace(props['triggerWords'], props['replacementWords'])
        assert len(props['text'].split()) <= 12 and len(final.split()) <= 12
# Phone-length card text (about 21 characters a line at the portrait type size); the 16:9 cut keeps the full wording.
PORTRAIT_ITEMS = {
    'B06': [('What changed', 'dates.py · one line'), ('The evidence', '1 failing, then 3 passing'),
            ('Not checked', '"2026-02-30" passes; no-dash dates crash'), ('Your call', 'merge it, or send it back')],
    'B07': [('Mistakes compound', 'one wrong step derails the rest'), ('Prompt injection', 'content can hide instructions'),
            ('Cost', 'long loops burn compute'), ('Accountability', 'someone still reviews it')],
    'B09': [('A scoped goal', 'with a written “done”'), ('Least privilege', 'only the access it needs'),
            ('Human review', 'nothing ships without you'), ('A junior teammate', 'delegate, then check')],
}
for b in sheet['beats']:
    if b['beat_id'] in PORTRAIT_ITEMS:
        items = b['shot']['remotion']['props']['items']
        for item, (label, detail) in zip(items, PORTRAIT_ITEMS[b['beat_id']]):
            item['label'], item['detail'] = label, detail
# The recap: the shared portrait verdict page underfills a 9:16 frame, so the same four lines are shown as a
# large-type portrait checklist, revealed on the spoken words.
sys.path.insert(0, str(REEL))
import make_sheet as ms  # noqa: E402
RECAP = [('Chatbot:', 'Chatbot', 'you drive the loop', '1'), ('Agent:', 'Agent', 'it drives the loop', '2'),
         ('Background agent', 'Background agent', 'drives while you’re away', '3'), ('So the skill', 'The skill now', 'delegating, then reviewing', '→')]
for b in sheet['beats']:
    if b['beat_id'] == 'B11':
        pb = parent['B11']
        b['shot']['remotion'] = {'pattern': 'AgentChecklist916', 'props': {
            'title': 'Who Drives the Loop?', 'tone': 'practice', 'handle': ms.HANDLE, 'logo': ms.LOGO, 'avatar': 'profile',
            'items': [{'label': l, 'detail': d, 'mark': m} for _, l, d, m in RECAP],
            'cues': [ms.place(pb['narration_text'], ph, 0.0, pb['kokoro_duration_s'], 'B11') for ph, *_ in RECAP],
            'durationSeconds': pb['actual_duration_s']}}
md = sheet['metadata']
md['width'], md['height'], md['aspect_ratio'] = 2160, 3840, '9:16'
md['note'] = md.get('note', '') + ' Vertical companion: every beat re-rendered with its native *916 composition; same narration and timing.'
path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
for f in ('SHOTLIST.md', 'FACTCHECK.md', 'PROMPTS.md', 'SOURCES.md'):
    if (REEL / f).exists():
        shutil.copy2(REEL / f, REEL / 'vertical' / f)
print('vertical sheet ready')
