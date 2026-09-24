# -*- coding: utf-8 -*-
"""Part 6 beat checker — verifies the beat sheet against the SCENE DATA.

Every check earns its place by naming a defect that shipped or nearly did:

  * COUNTS come from `midjourneyEditor.tsx`. Four tools, six filter groups.
    A count typed twice is how Suno shipped "four submenus" against five.
  * NO VERSION NUMBER. Organize's Version filter lists them; the group is
    depicted without its values, so none may appear in narration or props.
  * SERIES FINALE. BHTF must NOT tease a Part 7 — this is the last part, and
    Part 5's tease already promised that.
  * UNCAPTURED EDITOR STATES must not be claimed: the sparkle icon, a second
    layer, Restore in action, a resolved Smart Select, the finished results.
  * NO CUE PAST 0.85. A card that resolves in the last 15% gets no reading
    time; B06 originally landed one at 0.892.

Run from this directory:  python check_beats.py
"""
import io, json, re, sys

KIT = ('../../../RohanClaudeHAIbrutalist.art/runtime/remotion/src/scenes/'
       'midjourneyEditor.tsx')

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
    B('cannot read %s (%s)' % (KIT, e)); kit = ''

# four tools, by name, each must be mentioned somewhere
tools = re.findall(r"name: '([^']+)'", kit)
tools = [t for t in tools if t in ('Move / Resize', 'Paint', 'Smart Select', 'Edit')]
if len(tools) != 4:
    B('expected 4 tools in the kit, found %d: %s' % (len(tools), tools))
for t in tools:
    probe = t.replace(' / ', '').lower()
    if probe not in blob.lower().replace(' / ', '').replace('/', ''):
        B('tool "%s" is never mentioned in narration or props' % t)

# six filter groups; the spoken count must match
# Count ONLY inside the MJ_FILTERS array. A bare `kit.count("{heading:")`
# also matched the `FilterGroup` TYPE declaration and reported 7 for a
# six-entry array - the checker was wrong, not the data. Measure the thing
# you mean to measure.
_start = kit.find('MJ_FILTERS: FilterGroup[] = [')
_end = kit.find('];', _start) if _start >= 0 else -1
groups = kit[_start:_end].count('{heading:') if _end > _start else -1
if groups != 6:
    B('expected 6 filter groups in the kit, found %d' % groups)
if re.search(r'\bsix ways\b|\bsix groups\b', blob, re.I) and groups != 6:
    B('narration says six but the kit has %d groups' % groups)
if groups == 6 and not re.search(r'\bsix\b', blob, re.I):
    W('the kit has six filter groups but the narration never says six')

# every MjL6 beat carries the Part 6 kicker
for bid, b in beats.items():
    pat = b['shot']['remotion']['pattern']
    if not pat.startswith('MjL6'):
        continue
    if 'PART 6' not in b['shot']['remotion']['props'].get('kicker', ''):
        B('%s (%s) kicker is not PART 6' % (bid, pat))

# ---------------------------------------------------------------- forbidden
for pat, why in [
    (r'\bv?\s?8\.\d\b', 'a model version number'),
    (r'\bV[0-9]\b', 'a version like V7/V8'),
    (r'\bversion\s+\d', 'a numbered version'),
]:
    m = re.search(pat, blob, re.I)
    if m:
        B('%s appears (%r) - forbidden on screen and in voice' % (why, m.group(0)))

# uncaptured Editor states
for pat, why in [
    (r'\bsparkle\b', 'the sparkle icon (its function is not captured)'),
    (r'second layer|another layer|layer two', 'a second layer (not captured)'),
    (r'\bRestore\b[^.]{0,40}\b(shows|reveals|brings back the)\b',
     'Restore in action (not captured)'),
    (r'selection (is|has) resolved|once selected it',
     'a resolved Smart Select selection (never captured un-disabled)'),
    (r'finished results|the four results (are|look)',
     'the finished results of an edit (capture stops at Submitting)'),
]:
    if re.search(pat, blob, re.I):
        B('claims %s' % why)

# register
for w in ['\\$', 'per month', 'subscription', 'free tier', 'pricing']:
    if re.search(w, blob, re.I):
        B('pricing language "%s" - register forbids it' % w)
if re.search(r'(first|one) of (three|four|five|six|\d)', blob, re.I):
    B('the series length is stated')

# ---------------------------------------------------------------- finale
bhtf = beats.get('BHTF', {})
bh = bhtf.get('narration_text', '') + json.dumps(
    bhtf.get('shot', {}).get('remotion', {}).get('props', {}), ensure_ascii=False)
if re.search(r'Part\s*7|next part|next time|in the next', bh, re.I):
    B('BHTF teases a further part - Part 6 is the finale')
if not re.search(r'that is the series|the series\b', bh, re.I):
    W('BHTF does not read as a series close')

# ---------------------------------------------------------------- register 2
if "Rohaan from Humanitarians AI" not in beats.get('B00', {}).get('narration_text', ''):
    B('B00 does not open with the required greeting')
n = len(re.findall(r'Rohaan, Humanitarians AI', allnar))
if n != 1:
    B('sign-off spoken %d times, must be exactly once' % n)
if 'Rohaan, Humanitarians AI' not in beats.get('BOUT', {}).get('narration_text', ''):
    B('the sign-off is not in BOUT')

# ---------------------------------------------------------------- cue timing
for bid, b in beats.items():
    for k, v in (b['shot']['remotion']['props'].get('cues') or {}).items():
        if v > 0.85:
            B('%s cue %r resolves at %.3f - under 15%% of the beat left to read it'
              % (bid, k, v))

# ---------------------------------------------------------------- heteronyms
HET = ['live', 'read', 'lead', 'bow', 'close', 'record', 'present',
       'wind', 'tear', 'object', 'produce', 'contract', 'content', 'separate',
       'minute', 'refuse', 'desert']
for bid, b in beats.items():
    for h in HET:
        if re.search(r'\b%s\b' % h, b['narration_text'], re.I):
            W('%s: heteronym "%s" - Kokoro may stress it wrong' % (bid, h))

# bare numerals ("Part N" exempt - spoken that way in five shipped videos)
for bid, b in beats.items():
    txt = re.sub(r'Part\s+\d', 'Part N', b['narration_text'])
    for m in re.finditer(r'(?<![\w.])\d+(?![\w.])', txt):
        W('%s: bare numeral %r - spell it as words for Kokoro' % (bid, m.group(0)))

print('=' * 72)
for m in blockers: print('BLOCKER  ' + m)
for m in warnings: print('warning  ' + m)
print('=' * 72)
print('%d blockers, %d warnings' % (len(blockers), len(warnings)))
sys.exit(1 if blockers else 0)
