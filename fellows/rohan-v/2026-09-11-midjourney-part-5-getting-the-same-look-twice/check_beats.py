# -*- coding: utf-8 -*-
"""Part 5 beat checker — verifies the beat sheet against the SCENE DATA.

Every check exists because its absence cost a rebuild somewhere in this series:

  * COUNTS AND LABELS come from `midjourneyAesthetics.tsx`, never typed twice.
  * NO VERSION NUMBER. The product labels these surfaces `V8 Profiles` and
    `Global V7 Profile`; both are omitted per VIDEO-PIPELINE.md section 7.
  * THE 200-POINT FIGURE must match the scene data that renders it.
  * NOTHING UNCAPTURED. Three surfaces are named in the spec as gaps - the
    ranking interface, what `Rate More Images` opens, and a finished Style
    Creator style. Mentioning any of them as if shown is a blocker.

Run from this directory:  python check_beats.py
"""
import io, json, re, sys

KIT = ('../../../RohanClaudeHAIbrutalist.art/runtime/remotion/src/scenes/'
       'midjourneyAesthetics.tsx')

blockers, warnings = [], []
def B(m): blockers.append(m)
def W(m): warnings.append(m)

sheet = json.load(io.open('beat_sheet.json', encoding='utf-8'))
beats = {b['beat_id']: b for b in sheet['beats']}
allnar = ' '.join(b['narration_text'] for b in sheet['beats'])
allprops = json.dumps([b['shot']['remotion'].get('props', {})
                       for b in sheet['beats']], ensure_ascii=False)
blob = allnar + ' ' + allprops

try:
    kit = io.open(KIT, encoding='utf-8').read()
except OSError as e:
    B('cannot read %s (%s)' % (KIT, e))
    kit = ''

# ---------------------------------------------------------------- scene data
# the four systems must all be accounted for somewhere
sys_names = re.findall(r"name: '(A [^']+)'", kit)
if len(sys_names) != 4:
    B('expected 4 systems in the kit, found %d: %s' % (len(sys_names), sys_names))

# the attach panel's four product labels
attach = re.findall(r"label: '(Attach to prompt|Style reference|Image Prompts|Animate)'", kit)
if len(attach) != 4:
    B('expected the 4 attach labels in the kit, found %s' % attach)
for a in ('Style reference', 'Image Prompts'):
    if a.lower() not in blob.lower():
        B('attach slot "%s" is never mentioned - it is the beat\'s whole point' % a)

# the three add-sources and two apply-actions
for a in ('Upload Images', 'Add from Link', 'Add from Creations'):
    if a.lower() not in blob.lower() and a.split()[-1].lower() not in blob.lower():
        W('moodboard add-source "%s" is not mentioned' % a)
for a in ('Set as Default', 'Use in Prompt'):
    if a.lower() not in blob.lower():
        B('moodboard apply-action "%s" is never mentioned' % a)

# the unlock figure must agree with the data
m = re.search(r'unlockPoints:\s*(\d+)', kit)
if not m:
    B('unlockPoints not found in the kit')
else:
    pts = int(m.group(1))
    words = {200: 'two hundred'}.get(pts)
    if words and words not in allnar.lower():
        B('the narration does not state the unlock figure as "%s" (kit says %d)'
          % (words, pts))
    if re.search(r'\b%d\b' % pts, allnar):
        W('the unlock figure appears as a bare numeral in narration - Kokoro '
          'mis-reads digits; spell it out')

# every MjL5 beat carries the Part 5 kicker
for bid, b in beats.items():
    pat = b['shot']['remotion']['pattern']
    if pat.startswith('MjL5'):
        k = b['shot']['remotion']['props'].get('kicker', '')
        if 'PART 5' not in k:
            B('%s (%s) kicker is not PART 5: %r' % (bid, pat, k))

# ---------------------------------------------------------------- forbidden
for pat, why in [
    (r'\bV[0-9]\b',        'a model version like V7/V8'),
    (r'\bv?\s?8\.\d\b',    'a model version number'),
    (r'V\d+\s+Profiles',   'the product\'s versioned "V8 Profiles" label'),
    (r'Global\s+V\d+',     'the product\'s versioned "Global V7 Profile" label'),
]:
    m = re.search(pat, blob, re.I)
    if m:
        B('%s appears (%r) - omitted on purpose, see FACTCHECK' % (why, m.group(0)))

# uncaptured surfaces must not be described as if shown
for pat, why in [
    (r'ranking (screen|interface|page)', 'the ranking interface is NOT captured'),
    (r'Rate More Images[^.]{0,40}(opens|shows)', 'what Rate More Images opens is NOT captured'),
    (r'(finished|saved|applied) style', 'a finished Style Creator style is NOT captured'),
]:
    m = re.search(pat, blob, re.I)
    if m:
        B('%s (%r)' % (why, m.group(0)))

# pricing / plan language
for w in ['\\$', 'per month', 'subscription', 'plan costs', 'free tier',
          'gpu hour', 'credits cost', 'pricing']:
    if re.search(w, blob, re.I):
        B('pricing language "%s" - register forbids it' % w)

if re.search(r'(first|one) of (three|four|five|six|\d)', blob, re.I):
    B('the series length is stated')

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

# ---------------------------------------------------------------- numerals
for bid, b in beats.items():
    # "Part N" is exempt: that form is spoken in four delivered videos already
    txt = re.sub(r'Part\s+\d', 'Part N', b['narration_text'])
    for m in re.finditer(r'(?<![\w.])\d+(?![\w.])', txt):
        W('%s: bare numeral %r in narration - spell it for Kokoro'
          % (bid, m.group(0)))

# ---------------------------------------------------------------- cue staging
# A late cue leaves its card almost no screen time. The rule is TIME-BASED,
# not a flat fraction: 0.898 of a 22.6s beat still leaves 2.3s and reads fine,
# while 0.939 of a 19.8s beat leaves 1.2s and does not. A flat 0.88 threshold
# flagged the former as a defect, which it is not.
MIN_TAIL_S = 1.8
for bid, b in beats.items():
    dur = b.get('actual_duration_s') or b.get('estimated_duration_s') or 20.0
    for name, frac in (b['shot']['remotion']['props'].get('cues') or {}).items():
        tail = dur * (1.0 - frac)
        if tail < MIN_TAIL_S:
            B('%s cue %r resolves at %.3f, leaving %.1fs of a %.1fs beat - too '
              'little to be read. Re-anchor to the START of its clause, or '
              'reorder the narration.' % (bid, name, frac, tail, dur))
        if frac < 0.02 and name not in ('cards', 'page', 'drop', 'panel', 'slab'):
            W('%s cue %r resolves at %.3f - almost frame zero' % (bid, name, frac))

print('=' * 72)
for m in blockers:
    print('BLOCKER  ' + m)
for m in warnings:
    print('warning  ' + m)
print('=' * 72)
print('%d blockers, %d warnings' % (len(blockers), len(warnings)))
sys.exit(1 if blockers else 0)
