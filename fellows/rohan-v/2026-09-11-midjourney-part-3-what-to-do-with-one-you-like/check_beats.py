# -*- coding: utf-8 -*-
"""Verify midjourney-part-3 against its sources, by script rather than by eye.

`VIDEO-PIPELINE.md` §8 step 3. Suno shipped "four submenus" against a
five-item menu because a human counted lines in a document.

What this checks:
  1. The six rail rows and their button labels match MJ_RAIL_ROWS, in order.
  2. Every count the narration asserts (six rows, seven entries, three off)
     matches the arrays the scenes actually render.
  3. The three hidden entries named in narration ARE the unchecked ones.
  4. Register: name once, greeting, no version numbers, no pricing, no count.
  5. Heteronyms, and claims about uncaptured surfaces.
"""
import io, json, re, sys

SHEET = 'beat_sheet.json'
RAIL_TSX = (r'D:\Rohan\Claude\HAI\RohanClaudeHAIbrutalist.art\runtime'
            r'\remotion\src\scenes\midjourneyRail.tsx')

blockers, warnings = [], []
B = blockers.append
W = warnings.append

sheet = json.load(io.open(SHEET, encoding='utf-8'))
beats = {b['beat_id']: b for b in sheet['beats']}
allnar = ' '.join(b['narration_text'] for b in sheet['beats'])
low = allnar.lower()
src = io.open(RAIL_TSX, encoding='utf-8').read()

# ---------------------------------------------------------------- 1. the rail
rows = re.findall(r"label:\s*'([^']+)',\s*\n\s*buttons:\s*\[([^\]]*)\]", src)
rail = rows[:6]
EXPECTED = ['Vary', 'Upscale', 'More', 'HD', 'Use', 'Edit']
if [r[0] for r in rail] != EXPECTED:
    B('MJ_RAIL_ROWS drifted from the captured order.\n'
      '      got      %s\n      expected %s' % ([r[0] for r in rail], EXPECTED))

if 'six labelled rows' not in low and 'six rows' not in low:
    B('narration never states the row count though the spine is a six-row panel')
if len(rail) != 6:
    B('%d rail rows in the data, but the narration says six' % len(rail))

BTN = set()
for r in rail:
    for b in r[1].split(','):
        b = b.strip().strip("'")
        if b:
            BTN.add(b)
for spoken in ['Subtle', 'Strong', 'Creative', 'Rerun', 'Run batch as HD',
               'Style', 'Prompt', 'Quick Edit', 'Open Editor']:
    if spoken not in BTN:
        B('narration/scene references button "%s" which is not in '
          'MJ_RAIL_ROWS: %s' % (spoken, sorted(BTN)))

# ---------------------------------------------------------------- 2. the menu
menu = re.findall(r"\{name:\s*'([^']+)',\s*on:\s*(true|false)\}", src)
if len(menu) != 7:
    B('MJ_MENU has %d entries, not 7' % len(menu))
off = [m[0] for m in menu if m[1] == 'false']
on = [m[0] for m in menu if m[1] == 'true']
if 'seven entries' not in low:
    W('narration does not say "seven entries" for the More Options checklist')
if len(off) != 3:
    B('%d unchecked menu entries but the narration says three' % len(off))
for name in off:
    if name.lower() not in low:
        B('"%s" is unchecked in the data but never named in narration' % name)

# ---------------------------------------------------------------- 3. animate
anim = rows[6:8]
if [r[0] for r in anim] != ['Auto', 'Loop']:
    B('MJ_ANIMATE_ROWS drifted: %s' % [r[0] for r in anim])
for w in ['auto', 'loop', 'low motion', 'high motion']:
    if w not in low:
        B('Animate row term "%s" never spoken' % w)

# ---------------------------------------------------------------- 4. register
if not re.search(r"Hi, I'm Rohaan from Humanitarians AI",
                 beats['B00']['narration_text']):
    B('B00 does not open with the required host line')
fullname = len(re.findall(r'Rohaan, Humanitarians AI', allnar))
if fullname != 1:
    B('sign-off spoken %dx - must be exactly once, in BOUT' % fullname)
if 'Rohaan, Humanitarians AI' not in beats['BOUT']['narration_text']:
    B('the one full-name mention is not in BOUT')

for bad, why in [
    (r'\bV\s?[0-9]', 'a model version number'),
    (r'\b8\.[0-9]\b', 'a model version number'),
    (r'\$', 'a price'),
    (r'\b(?:per month|subscription|plan|tier|GPU hour)\b', 'pricing language'),
    (r'\bfirst of (?:three|four|five|six)\b', 'a series count'),
    (r'\b(?:three|four|five|six) (?:part|video)s?\b', 'a series count'),
    (r'\bfree\b', 'promotional framing'),
]:
    m = re.search(bad, allnar, re.I)
    if m:
        B('narration contains %s: "%s"' % (why, m.group(0)))

# Pan, Zoom and Remix have NO capture in use. They may be named and described,
# never depicted producing a result.
for bad in ['pan gives you', 'zoom produces', 'remix returns',
            'here is what pan', 'here is what zoom']:
    if bad in low:
        B('depicts an uncaptured surface: "%s"' % bad)

# ---------------------------------------------------------------- 5. heteronyms
HET = ['live', 'read', 'lead', 'bow', 'close', 'record', 'present', 'wind',
       'tear', 'object', 'produce', 'contract', 'separate', 'minute',
       'content', 'refuse', 'desert', 'invalid']
for b in sheet['beats']:
    for h in HET:
        if re.search(r'\b%s\b' % h, b['narration_text'], re.I):
            W('%s: heteronym "%s" - Kokoro may stress it wrong'
              % (b['beat_id'], h))

for b in sheet['beats']:
    n = len(b['narration_text'].split())
    if b['beat_id'] not in ('B00', 'BOUT', 'BVDT', 'BHTF'):
        if not (40 <= n <= 72):
            W('%s: %d words (body beats want 45-70)' % (b['beat_id'], n))
    if 'actual_duration_s' not in b:
        B('%s: no actual_duration_s - audio not locked' % b['beat_id'])

for b in sheet['beats']:
    k = b['shot']['remotion'].get('props', {}).get('kicker')
    if k and 'PART 3' not in k:
        B('a scene passes the wrong kicker: %r' % k)

# ---------------------------------------------------------------- report
print('=' * 72)
for x in blockers:
    print('BLOCKER  ' + x)
for x in warnings:
    print('warning  ' + x)
print('=' * 72)
print('%d blockers, %d warnings' % (len(blockers), len(warnings)))
sys.exit(1 if blockers else 0)
