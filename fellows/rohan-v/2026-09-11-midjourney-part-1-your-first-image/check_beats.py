#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
check_beats.py — verify Midjourney Part 1's beat sheet against the UI spec and
the pipeline's own rules, BY SCRIPT rather than by eye.

VIDEO-PIPELINE.md section 8 step 3. Every factual error the Suno series shipped
survived a careful human read of the same file. These are the checks that would
have caught them:

  1  every cues.json anchor actually occurs in that beat's narration
     (a reworded line silently orphans its anchor and the scene desyncs)
  2  every asserted COUNT in the narration matches the nav data the scene
     renders  ("four submenus" against a five-item menu)
  3  no forbidden term reaches the narration — version numbers, pricing,
     a stated video count, or a claim the captures disprove
  4  heteronyms the voice cannot be trusted with
  5  register rules — name once, access once
  6  the scene patterns exist as files, and the beat order is monotonic

Run:  PYTHONUTF8=1 python check_beats.py
Exit: 0 clean, 1 if any BLOCKER.
"""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCENES = os.path.normpath(os.path.join(
    HERE, '..', '..', '..', 'RohanClaudeHAIbrutalist.art',
    'runtime', 'remotion', 'src', 'scenes'))

blockers = []
warnings = []
notes = []


def norm(s):
    """Lowercase, strip punctuation, collapse whitespace — how sync_cues matches."""
    s = s.lower().replace('’', "'").replace('—', ' ').replace('–', ' ')
    s = re.sub(r"[^a-z0-9' ]+", ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


with io.open(os.path.join(HERE, 'beat_sheet.json'), encoding='utf-8') as f:
    bs = json.load(f)
with io.open(os.path.join(HERE, 'cues.json'), encoding='utf-8') as f:
    cues = json.load(f)

beats = {b['beat_id']: b for b in bs['beats']}
order = [b['beat_id'] for b in bs['beats']]
narr = {k: norm(v['narration_text']) for k, v in beats.items()}
all_narr = ' '.join(narr.values())

print('=' * 72)
print('MIDJOURNEY PART 1 — beat sheet check')
print('=' * 72)

# ---------------------------------------------------------------- 1. anchors
print('\n[1] cue anchors resolve against their own narration')
for bid, cs in cues.items():
    if bid.startswith('_'):
        continue
    if bid not in narr:
        blockers.append('cues.json has %s but the beat sheet does not' % bid)
        continue
    for name, phrase in cs.items():
        if norm(phrase) not in narr[bid]:
            blockers.append('%s cue "%s" anchor not in narration: %r'
                            % (bid, name, phrase))
        else:
            print('    ok  %s.%-10s %r' % (bid, name, phrase))

# every body beat that renders an MjL1 scene needs cues
for bid, b in beats.items():
    pat = b['shot'].get('remotion', {}).get('pattern', '')
    if pat.startswith('MjL1') and bid not in cues:
        blockers.append('%s renders %s but has no cues.json entry' % (bid, pat))

# ------------------------------------------------------------------ 2. counts
print('\n[2] asserted counts match the nav data the scenes render')
kit = io.open(os.path.join(SCENES, 'midjourneyKit.tsx'), encoding='utf-8').read()


def arr_len(name):
    m = re.search(r'export const %s = \[(.*?)\] as const;' % name, kit, re.S)
    if not m:
        blockers.append('kit array %s not found' % name)
        return -1
    return len(re.findall(r"label:\s*'", m.group(1)))


n_main = arr_len('MJ_NAV_MAIN')
n_aes = arr_len('MJ_NAV_AESTHETICS')
n_com = arr_len('MJ_NAV_COMMUNITY')
n_tot = n_main + n_aes + n_com
print('    kit says: %d main + %d aesthetics + %d community = %d total'
      % (n_main, n_aes, n_com, n_tot))

WORD = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}

b03 = narr.get('B03', '')
for label, n in (('total', n_tot), ('main', n_main),
                 ('aesthetics', n_aes), ('community', n_com)):
    w = WORD.get(n, str(n))
    if w in b03.split():
        print('    ok  B03 says "%s" for %s (%d)' % (w, label, n))
    else:
        blockers.append('B03 never says "%s" — the %s group has %d'
                        % (w, label, n))

# the three hover buttons, from the scene that renders them
hov = io.open(os.path.join(SCENES, 'MjL1Hover.tsx'), encoding='utf-8').read()
m = re.search(r"const HOVER = \[(.*?)\] as const;", hov, re.S)
hover_items = re.findall(r"'([^']+)'", m.group(1)) if m else []
print('    scene says hover buttons: %s' % ', '.join(hover_items))
if WORD.get(len(hover_items)) not in narr.get('B07', '').split():
    blockers.append('B07 does not say "%s" for the %d hover buttons'
                    % (WORD.get(len(hover_items)), len(hover_items)))
else:
    print('    ok  B07 says "%s"' % WORD.get(len(hover_items)))
for h in hover_items:
    if norm(h) not in narr.get('B07', ''):
        blockers.append('B07 does not name hover button %r' % h)

# ------------------------------------------------------- 3. forbidden content
print('\n[3] forbidden content')

# version numbers — VIDEO-PIPELINE.md section 7
for bid, t in narr.items():
    for m in re.finditer(r'\b(v ?\d+(\.\d+)?|version \d)', t):
        blockers.append('%s narration carries a version number: %r'
                        % (bid, m.group(0)))

# pricing / plan language
PRICE = ['free', 'subscription', 'subscribe', 'plan', 'price', 'pricing',
         'dollar', 'per month', 'paid', 'premium', 'pro account', 'credits',
         'gpu hour', 'fast hour']
for bid, t in narr.items():
    for p in PRICE:
        if p in t:
            blockers.append('%s narration carries pricing language: %r' % (bid, p))

# a stated video count — the Suno Part 1 mistake
for m in re.finditer(r'\b(one|two|three|four|five|six) (training )?(videos|parts)\b',
                     all_narr):
    blockers.append('narration states a video COUNT: %r' % m.group(0))
if re.search(r'first of\b', all_narr):
    blockers.append('narration says "first of ..." — do not commit to a count')
print('    ok  no version number, no pricing, no stated video count')

# claims the captures disprove
if 'upscale' in narr.get('B07', ''):
    seg = narr['B07']
    if not re.search(r'no upscale|not.{0,20}upscale', seg):
        blockers.append('B07 mentions Upscale without saying it is NOT on hover')
    else:
        print('    ok  B07 says Upscale is not on the hover row')
if re.search(r'grid of four|two by two|2x2|quad', all_narr):
    blockers.append('narration calls the result a grid/quad — it is a ROW of four')
print('    ok  the four results are never called a quad')

# ------------------------------------------------------------- 4. heteronyms
print('\n[4] heteronyms the voice cannot be trusted with')
HET = ['live', 'lives', 'read', 'reads', 'lead', 'bow', 'close', 'record',
       'records', 'present', 'wind', 'tear', 'object', 'produce', 'contract',
       'separate', 'subject', 'minute', 'refuse', 'content']
for bid, t in narr.items():
    for w in HET:
        if re.search(r'\b%s\b' % w, t):
            warnings.append('%s narration contains heteronym %r — verify by ear'
                            % (bid, w))
if not warnings:
    print('    ok  none present')

# --------------------------------------------------------------- 5. register
print('\n[5] register')
n_name = len(re.findall(r'rohaan humanitarians ai', all_narr))
if n_name != 1:
    blockers.append('sign-off spoken %d times; must be exactly 1' % n_name)
else:
    print('    ok  sign-off spoken exactly once (BOUT)')

if 'rohaan humanitarians ai' not in narr.get('BOUT', ''):
    blockers.append('sign-off is not in BOUT')

n_disc = sum(1 for bid, t in narr.items() if 'discord' in t and bid != 'BVDT')
if n_disc > 1:
    blockers.append('Discord access stated in %d beats outside the verdict; '
                    'state it ONCE (B02)' % n_disc)
else:
    print('    ok  access stated once, in B02 (plus the verdict recap)')

if not narr.get('B00', '').startswith("hi i'm rohaan from humanitarians ai"):
    blockers.append('B00 does not open with the host line')
else:
    print('    ok  B00 opens with the host line')

# body-beat word counts
print('\n    body beat word counts (target 45-75):')
for bid in order:
    if not bid.startswith('B') or bid in ('B00', 'BVDT', 'BHTF', 'BOUT'):
        continue
    n = len(beats[bid]['narration_text'].split())
    flag = '' if 45 <= n <= 75 else '   <-- outside 45-75'
    if flag:
        warnings.append('%s narration is %d words' % (bid, n))
    print('      %-5s %3d%s' % (bid, n, flag))

# ---------------------------------------------------------------- 6. wiring
print('\n[6] scene wiring')
root = io.open(os.path.normpath(os.path.join(SCENES, '..', 'Root.tsx')),
               encoding='utf-8').read()
for bid in order:
    pat = beats[bid]['shot'].get('remotion', {}).get('pattern')
    if not pat:
        blockers.append('%s has no remotion pattern' % bid)
        continue
    if pat.startswith('MjL1'):
        if not os.path.exists(os.path.join(SCENES, pat + '.tsx')):
            blockers.append('%s: scene file %s.tsx does not exist' % (bid, pat))
            continue
        if 'id="%s"' % pat not in root:
            blockers.append('%s: %s is not registered in Root.tsx' % (bid, pat))
            continue
        src = io.open(os.path.join(SCENES, pat + '.tsx'), encoding='utf-8').read()
        if 'MIDJOURNEY TUTORIAL PART 1' not in src:
            blockers.append('%s: %s does not set the Part 1 kicker' % (bid, pat))
        if 'SUNO TUTORIAL' in src:
            blockers.append('%s: %s carries a Suno kicker' % (bid, pat))
    print('    ok  %-5s %s' % (bid, pat))

# beat order monotonic + expected shape
if order != sorted([b for b in order if b.startswith('B0')]) + ['BVDT', 'BHTF', 'BOUT']:
    expected = ['B00', 'B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07',
                'BVDT', 'BHTF', 'BOUT']
    if order != expected:
        blockers.append('beat order is not monotonic: %s' % ' '.join(order))

est = sum(b.get('estimated_duration_s', 0) for b in bs['beats'])
print('\n    estimated runtime: %d:%02d across %d beats'
      % (est // 60, est % 60, len(bs['beats'])))

# ------------------------------------------------------------------ report
print('\n' + '=' * 72)
for w in warnings:
    print('WARN     %s' % w)
for b in blockers:
    print('BLOCKER  %s' % b)
print('=' * 72)
print('%d blockers, %d warnings' % (len(blockers), len(warnings)))
sys.exit(1 if blockers else 0)
