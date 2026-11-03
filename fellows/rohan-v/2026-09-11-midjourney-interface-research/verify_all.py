# -*- coding: utf-8 -*-
"""Cross-part final check for the Midjourney series.

Runs the checks that only make sense across parts, which no per-reel script
can see:

  1. Every beat of every part is 3840x2160 and frame-accurate to its own audio.
  2. Every master is 3840x2160.
  3. No `_ext_` leftovers anywhere (a leftover means a failed shutil.move).
  4. Each part's kicker says the right part number.
  5. **Continuity**: what each part's BHTF promises is what the next part
     actually delivers. This is the check that caught Part 1 teasing a Part 2
     that no longer existed.
  6. The sign-off is spoken exactly once per part.
  7. No part states the series count.

Usage:  python verify_all.py
"""
import io, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
# DISCOVERED, not listed. A hardcoded list meant Part 4 was authored, rendered
# and compiled while this script still reported "0 problems across 3 parts" -
# a green result that had simply not looked at it.
PARTS = sorted(
    (d for d in os.listdir(HERE)
     if d.startswith('midjourney-part-')
     and os.path.isdir(os.path.join(HERE, d))
     and os.path.exists(os.path.join(HERE, d, 'beat_sheet.json'))),
    key=lambda d: int(d.rsplit('-', 1)[1]),
)

problems, notes = [], []
P = problems.append
N = notes.append


def probe(path, entries):
    out = subprocess.run(
        ['ffprobe', '-v', 'error', '-select_streams', 'v:0',
         '-show_entries', 'stream=' + entries, '-of', 'csv=p=0', path],
        capture_output=True, text=True).stdout.strip()
    return out.split(',')


sheets = {}
for part in PARTS:
    d = os.path.join(HERE, part)
    sp = os.path.join(d, 'beat_sheet.json')
    if not os.path.exists(sp):
        P('%s: no beat_sheet.json' % part)
        continue
    sheet = json.load(io.open(sp, encoding='utf-8'))
    sheets[part] = sheet
    num = part[-1]

    # ---- beats ----
    total = 0.0
    for b in sheet['beats']:
        bid = b['beat_id']
        dur = b.get('actual_duration_s')
        if dur is None:
            P('%s %s: audio not locked' % (part, bid))
            continue
        total += dur
        f = os.path.join(d, 'media', '%s.mp4' % bid)
        if not os.path.exists(f):
            P('%s %s: media missing' % (part, bid))
            continue
        w, h, n = probe(f, 'width,height,nb_frames')
        if (w, h) != ('3840', '2160'):
            P('%s %s: %sx%s not 4K' % (part, bid, w, h))
        exp = round(dur * 30)
        if abs(int(n) - exp) > 2:
            P('%s %s: %s frames vs %d expected' % (part, bid, n, exp))

    # ---- leftovers ----
    md = os.path.join(d, 'media')
    if os.path.isdir(md):
        junk = [x for x in os.listdir(md) if x.startswith('_')]
        if junk:
            P('%s: leftover temp files in media/: %s' % (part, junk))

    # ---- master ----
    m = os.path.join(d, '%s.mp4' % part)
    if not os.path.exists(m):
        P('%s: no master' % part)
    else:
        w, h = probe(m, 'width,height')
        if (w, h) != ('3840', '2160'):
            P('%s master: %sx%s not 4K' % (part, w, h))
        N('%s  %5.1fs = %d:%02d  %sx%s  %.1f MB'
          % (part, total, total // 60, total % 60, w, h,
             os.path.getsize(m) / 1e6))

    # ---- kicker ----
    for b in sheet['beats']:
        k = b['shot']['remotion'].get('props', {}).get('kicker')
        if k and ('PART %s' % num) not in k:
            P('%s %s: kicker says %r' % (part, b['beat_id'], k))

    # ---- name once ----
    allnar = ' '.join(b['narration_text'] for b in sheet['beats'])
    c = len(re.findall(r'Rohaan, Humanitarians AI', allnar))
    if c != 1:
        P('%s: sign-off spoken %dx, must be once' % (part, c))

    # ---- no series count ----
    for pat in [r'\bfirst of (?:three|four|five|six)\b',
                r'\b(?:three|four|five|six) (?:part|video)s?\b']:
        mm = re.search(pat, allnar, re.I)
        if mm:
            P('%s: states a series count: "%s"' % (part, mm.group(0)))

# ---------------------------------------------------------------- continuity
# What part N's BHTF promises must be what part N+1 delivers. Part 1 shipped a
# tease for a Part 2 that was later replaced; nothing caught it but a frame.
EXPECT = {
    'midjourney-part-1': (
        'midjourney-part-2',
        ['seven', 'prompt'],
        'Part 2 is the seven documented prompt elements',
    ),
    'midjourney-part-2': (
        'midjourney-part-3',
        ['vary', 'upscale', 'rerun'],
        'Part 3 is the opened-image action rail',
    ),
    'midjourney-part-3': (
        'midjourney-part-4',
        ['aspect', 'dial'],
        'Part 4 is the settings panel',
    ),
    'midjourney-part-4': (
        'midjourney-part-5',
        ['moodboard', 'personalize'],
        'Part 5 is the consistency systems',
    ),
}
for part, (nxt, words, what) in EXPECT.items():
    if part not in sheets or nxt not in sheets:
        continue
    bhtf = [b for b in sheets[part]['beats'] if b['beat_id'] == 'BHTF']
    if not bhtf:
        P('%s: no BHTF beat' % part)
        continue
    tease = bhtf[0]['narration_text'].lower()
    props = json.dumps(bhtf[0]['shot']['remotion'].get('props', {})).lower()
    blob = tease + ' ' + props
    missing = [w for w in words if w not in blob]
    if missing:
        P('%s BHTF does not tease %s - missing %s.\n'
          '      Tease reads: %r' % (part, what, missing, tease[:150]))
    # and the next part must actually contain those words
    nxt_nar = ' '.join(b['narration_text']
                       for b in sheets[nxt]['beats']).lower()
    absent = [w for w in words if w not in nxt_nar]
    if absent:
        P('%s promises %s but %s never says %s'
          % (part, words, nxt, absent))

# ---------------------------------------------------------------- report
print('=' * 72)
for n in notes:
    print('  ' + n)
print('=' * 72)
for x in problems:
    print('PROBLEM  ' + x)
print('=' * 72)
print('%d problem(s) across %d part(s)' % (len(problems), len(sheets)))
sys.exit(1 if problems else 0)
