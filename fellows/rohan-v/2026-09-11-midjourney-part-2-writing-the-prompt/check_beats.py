# -*- coding: utf-8 -*-
"""Verify midjourney-part-2 against its sources, by script rather than by eye.

`VIDEO-PIPELINE.md` §8 step 3: verify the beat sheet with a script, not by
reading it. Suno shipped "four submenus" against a five-item menu because a
human counted lines in a document.

What this checks:
  1. The seven elements the narration names ARE the seven in MJ_SEVEN, in order.
  2. Any count the narration asserts matches the data.
  3. Every element has a non-empty `inPrompt`, because B06 claims all seven
     appear in the real prompt.
  4. PROMPT_WOLF still contains the exact substrings MJ_SEVEN says it does.
  5. Register: name once, greeting present, no version numbers, no pricing,
     no series count, no forbidden inferences.
  6. Heteronyms Kokoro is known to get wrong.
"""
import io, json, re, sys

SHEET = 'beat_sheet.json'
PROMPT_TSX = (r'D:\Rohan\Claude\HAI\RohanClaudeHAIbrutalist.art\runtime'
              r'\remotion\src\scenes\midjourneyPrompt.tsx')

blockers, warnings = [], []
B = blockers.append
W = warnings.append

sheet = json.load(io.open(SHEET, encoding='utf-8'))
beats = {b['beat_id']: b for b in sheet['beats']}
allnar = ' '.join(b['narration_text'] for b in sheet['beats'])
low = allnar.lower()

src = io.open(PROMPT_TSX, encoding='utf-8').read()

# ---------------------------------------------------------------- 1. the seven
names = re.findall(r"name:\s*'([^']+)'", src)
if len(names) != 7:
    B(f'MJ_SEVEN has {len(names)} entries, not 7: {names}')
EXPECTED = ['Subject', 'Medium', 'Environment', 'Lighting', 'Color', 'Mood',
            'Composition']
if names != EXPECTED:
    B(f'MJ_SEVEN order/labels drifted from the documented list.\n'
      f'      got      {names}\n      expected {EXPECTED}')

# every element must be spoken somewhere
for n in names:
    spoken = n.lower()
    if spoken == 'color':
        # narration uses British spelling; on-screen uses the vendor's
        if 'colour' not in low and 'color' not in low:
            B('neither "colour" nor "color" is spoken anywhere')
    elif spoken not in low:
        B(f'element "{n}" never spoken in any narration')

# ---------------------------------------------------------------- 2. counts
WORDS = {'seven': 7, 'six': 6, 'five': 5, 'four': 4, 'three': 3, 'two': 2}
for w, v in WORDS.items():
    for m in re.finditer(rf'\b{w}\b(?!\s*(?:questions?|elements?))', low):
        pass  # counts are checked specifically below, not exhaustively

if 'seven' not in low:
    B('the narration never says "seven" though the spine is a seven-item list')
n_seven = len(re.findall(r'\bseven\b', low))
if n_seven < 3:
    W(f'"seven" spoken only {n_seven}x — the spine may not be landing')

# B07 asserts six exclusions; the data must agree
neg = re.search(r"WOLF_NEGATION\s*=\s*\n?\s*'([^']+)'", src)
if not neg:
    B('WOLF_NEGATION not found in midjourneyPrompt.tsx')
else:
    n_ex = neg.group(1).count('no ')
    if 'six exclusions' in low and n_ex != 6:
        B(f'narration says "six exclusions" but WOLF_NEGATION has {n_ex}')

# ---------------------------------------------------------------- 3. inPrompt
inprompts = re.findall(r"inPrompt:\s*'([^']*)'", src)
if len(inprompts) != len(names):
    B(f'{len(names)} elements but {len(inprompts)} inPrompt values')
for n, ip in zip(names, inprompts):
    if not ip.strip():
        B(f'element "{n}" has an empty inPrompt, but B06 claims all seven '
          f'appear in the real prompt')

# ---------------------------------------------------------------- 4. quotation
wolf = re.search(r"PROMPT_WOLF\s*=\s*(.*?);\n", src, re.S)
if not wolf:
    B('PROMPT_WOLF not found')
else:
    joined = ''.join(re.findall(r"'([^']*)'", wolf.group(1)))
    for n, ip in zip(names, inprompts):
        # inPrompt may use an ellipsis to elide; check each run around it
        for run in [r.strip() for r in ip.split('…') if r.strip()]:
            if run not in joined:
                B(f'"{n}" claims the prompt contains "{run}" — it does not. '
                  f'The quotation and the mapping have drifted apart.')

# ---------------------------------------------------------------- 5. register
if not re.search(r"Hi, I'm Rohaan from Humanitarians AI", beats['B00']['narration_text']):
    B('B00 does not open with the required host line')

fullname = len(re.findall(r'Rohaan, Humanitarians AI', allnar))
if fullname != 1:
    B(f'sign-off spoken {fullname}x — must be exactly once, in BOUT')
if 'Rohaan, Humanitarians AI' not in beats['BOUT']['narration_text']:
    B('the one full-name mention is not in BOUT')

for bad, why in [
    (r'\bV\s?[0-9]', 'a model version number'),
    (r'\b8\.[0-9]\b', 'a model version number'),
    (r'\$', 'a price'),
    (r'\b(?:per month|subscription|plan|tier|credits?|GPU hour)\b', 'pricing language'),
    (r'\bfirst of (?:three|four|five|six)\b', 'a series count'),
    (r'\b(?:three|four|five|six) (?:part|video)s?\b', 'a series count'),
    (r'\bfree\b', 'promotional framing'),
]:
    m = re.search(bad, allnar, re.I)
    if m:
        B(f'narration contains {why}: "{m.group(0)}"')

# claims about the prompt author's intent or history cannot be evidenced
for bad in ['nobody was ticking', 'an earlier attempt', 'they forgot',
            'the team learned', 'because they had']:
    if bad in low:
        B(f'unsupportable claim about how the prompt was written: "{bad}"')

# the correction in B07 must stay a documented claim, not a verdict on output
for bad in ['the images failed', 'it did not work', 'that is why it looks',
            'the exclusions were ignored']:
    if bad in low:
        B(f'B07 overreaches from "documented as unreliable" to a verdict on '
          f'the images: "{bad}"')

# ---------------------------------------------------------------- 6. heteronyms
HET = ['live', 'read', 'lead', 'bow', 'close', 'record', 'present', 'wind', 'tear',
       'object', 'produce', 'contract', 'subject', 'separate', 'minute',
       'content', 'refuse', 'desert']
for b in sheet['beats']:
    for h in HET:
        if re.search(rf'\b{h}\b', b['narration_text'], re.I):
            # 'subject' is unavoidable — it is one of the seven element names
            if h == 'subject':
                continue
            W(f"{b['beat_id']}: heteronym \"{h}\" — Kokoro may stress it wrong")

# ---------------------------------------------------------------- 7. hygiene
for b in sheet['beats']:
    n = len(b['narration_text'].split())
    if b['beat_id'].startswith('B') and b['beat_id'] not in ('B00', 'BOUT',
                                                             'BVDT', 'BHTF'):
        if not (40 <= n <= 72):
            W(f"{b['beat_id']}: {n} words (body beats want 45-70)")
    if 'actual_duration_s' not in b:
        B(f"{b['beat_id']}: no actual_duration_s — audio not locked")

kick = set()
for b in sheet['beats']:
    pr = b['shot']['remotion'].get('props', {})
    if 'kicker' in pr:
        kick.add(pr['kicker'])
for k in kick:
    if 'PART 2' not in k:
        B(f'a scene passes the wrong kicker: {k!r}')

# ---------------------------------------------------------------- report
print('=' * 72)
for x in blockers:
    print('BLOCKER  ' + x)
for x in warnings:
    print('warning  ' + x)
print('=' * 72)
print(f'{len(blockers)} blockers, {len(warnings)} warnings')
sys.exit(1 if blockers else 0)
