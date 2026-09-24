# -*- coding: utf-8 -*-
"""Part 4 beat checker — verifies the beat sheet against the SCENE DATA.

Not a linter. This asserts the things a human reader cannot reliably eyeball,
and every check exists because its absence cost a rebuild somewhere:

  * COUNTS AND LABELS come from `midjourneySettings.tsx`, not from this file.
    A count typed in two places is how Suno shipped "four submenus" against a
    five-item menu.
  * NO VERSION NUMBER, on screen or in the voice. `prompt settings.png` shows
    `8.2` and the playbook forbids reproducing it.
  * NO WEIRDNESS RANGE. The docs search returned ranges for stylize and chaos
    but not for weird. A remembered "0-3000" is not evidence.
  * The documented stylize steps and chaos range must be stated CORRECTLY if
    they are stated at all.

Run from this directory:  python check_beats.py
"""
import io, json, re, sys

KIT = ('../../../RohanClaudeHAIbrutalist.art/runtime/remotion/src/scenes/'
       'midjourneySettings.tsx')

blockers, warnings = [], []
def B(m): blockers.append(m)
def W(m): warnings.append(m)

sheet = json.load(io.open('beat_sheet.json', encoding='utf-8'))
beats = {b['beat_id']: b for b in sheet['beats']}
allnar = ' '.join(b['narration_text'] for b in sheet['beats'])
allprops = json.dumps([b['shot']['remotion'].get('props', {})
                       for b in sheet['beats']], ensure_ascii=False)
blob = allnar + ' ' + allprops

# ---------------------------------------------------------------- scene data
try:
    kit = io.open(KIT, encoding='utf-8').read()
except OSError as e:
    B('cannot read %s (%s)' % (KIT, e))
    kit = ''

titles = re.findall(r"title:\s*'([^']+)'", kit)
if len(titles) != 4:
    B('expected 4 panel card titles in the kit, found %d: %s' % (len(titles), titles))
else:
    for tt in titles:
        if tt.lower() not in blob.lower():
            B('panel card "%s" is never mentioned in narration or props' % tt)

# every MjL4 beat must carry the Part 4 kicker
for bid, b in beats.items():
    pat = b['shot']['remotion']['pattern']
    if not pat.startswith('MjL4'):
        continue
    k = b['shot']['remotion']['props'].get('kicker', '')
    if 'PART 4' not in k:
        B('%s (%s) kicker is not PART 4: %r' % (bid, pat, k))

# card indices must be in range
for bid, b in beats.items():
    for i in b['shot']['remotion']['props'].get('card', []) or []:
        if not 0 <= i < 4:
            B('%s references panel card %d, out of range' % (bid, i))

# ---------------------------------------------------------------- forbidden
# a version number, in any shape
for pat, why in [
    (r'\bv?\s?8\.\d\b',            'a model version number'),
    (r'\bV[0-9]\b',                'a model version like V7/V8'),
    (r'\bversion\s+\d',            'a numbered version'),
]:
    m = re.search(pat, blob, re.I)
    if m:
        B('%s appears (%r) - forbidden on screen and in voice' % (why, m.group(0)))

# a weirdness range
wnd = re.search(r'weird(?:ness)?[^.]{0,80}?\b(\d{2,4})\b', blob, re.I)
if wnd and wnd.group(1) not in ('0',):
    B('a Weirdness figure appears (%r). The docs search returned no range for '
      'weird; only "starts at zero" is evidenced.' % wnd.group(0)[:60])

# pricing / plan language
for w in ['\\$', 'per month', 'subscription', 'plan costs', 'free tier',
          'gpu hour', 'credits cost', 'pricing']:
    if re.search(w, blob, re.I):
        B('pricing language "%s" - register forbids it' % w)

# series count
if re.search(r'(first|one) of (three|four|five|six|\d)', blob, re.I):
    B('the series length is stated - Suno Part 1 did this and it forced a '
      'cramped Part 3')

# ---------------------------------------------------------------- figures
# if the stylize steps are stated, they must be the documented ones
if re.search(r'styliz', blob, re.I):
    spoken_nums = set(re.findall(r'\b(fifty|one hundred|two hundred and fifty|'
                                 r'seven hundred and fifty)\b', blob, re.I))
    if spoken_nums and len(spoken_nums) < 4:
        W('Stylization steps are partially stated (%s). The docs give four: '
          '50 / 100 / 250 / 750.' % sorted(spoken_nums))
    if re.search(r'stylization[^.]{0,60}default', blob, re.I) and \
       not re.search(r'one hundred', blob, re.I):
        B('Stylization default is claimed without saying one hundred')

# chaos/variety range, if stated, must be 0-100
if re.search(r'variety', blob, re.I):
    if re.search(r'variety[^.]{0,80}\b(1000|3000|255)\b', blob, re.I):
        B('Variety range is wrong. Documented range is 0 to 100.')

# ---------------------------------------------------------------- register
b00 = beats.get('B00', {}).get('narration_text', '')
if "Rohaan from Humanitarians AI" not in b00:
    B('B00 does not open with the required greeting')
n_full = len(re.findall(r'Rohaan, Humanitarians AI', allnar))
if n_full != 1:
    B('sign-off spoken %d times, must be exactly once' % n_full)
if 'Rohaan, Humanitarians AI' not in beats.get('BOUT', {}).get('narration_text', ''):
    B('the sign-off is not in BOUT')

# ---------------------------------------------------------------- heteronyms
HET = ['live', 'read', 'lead', 'bow', 'close', 'record', 'present', 'use',
       'wind', 'tear', 'object', 'produce', 'contract', 'content', 'separate',
       'minute', 'refuse', 'desert']
for bid, b in beats.items():
    for h in HET:
        if re.search(r'\b%s\b' % h, b['narration_text'], re.I):
            W('%s: heteronym "%s" - Kokoro may stress it wrong' % (bid, h))

# ---------------------------------------------------------------- bare numerals
# Kokoro mis-reads bare digits; Part 4 is figure-heavy so this matters here
for bid, b in beats.items():
    # "Part 2" / "Part 5" are exempt: that exact form is spoken in three
    # already-delivered videos in this series, so flagging it here would only
    # make Part 4 inconsistent with them. It stays on the ear-check list.
    txt = re.sub(r'Part\s+\d', 'Part N', b['narration_text'])
    for m in re.finditer(r'(?<![\w.])\d+(?![\w.])', txt):
        W('%s: bare numeral %r in narration - spell it as words for Kokoro'
          % (bid, m.group(0)))

# ---------------------------------------------------------------- report
print('=' * 72)
for m in blockers:
    print('BLOCKER  ' + m)
for m in warnings:
    print('warning  ' + m)
print('=' * 72)
print('%d blockers, %d warnings' % (len(blockers), len(warnings)))
sys.exit(1 if blockers else 0)
