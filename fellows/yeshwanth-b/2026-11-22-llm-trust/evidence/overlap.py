"""Unigram-overlap score (ROUGE-1 F1) of two candidate answers against one reference.

    python3 overlap.py > overlap.txt

ROUGE-1 counts the words a candidate shares with a reference (clipped counts), then takes the
harmonic mean of precision (shared / candidate words) and recall (shared / reference words).
Tokens: lower-case letters, digits and the degree sign; punctuation dropped.
"""
import json
import re
from collections import Counter

REFERENCE = 'Water boils at about 70 °C at the top of Mount Everest.'
CANDIDATES = {
    'wrong': 'Water boils at 100 °C at the top of Mount Everest.',
    'right': "On Everest's summit, the boiling point drops to roughly 70 degrees Celsius.",
}


def tokens(s):
    return re.findall(r"[a-z0-9°]+", s.lower().replace("'s", ''))


def rouge1(cand, ref):
    c, r = Counter(tokens(cand)), Counter(tokens(ref))
    shared = sum((c & r).values())
    p, rec = shared / sum(c.values()), shared / sum(r.values())
    f = 0 if shared == 0 else 2 * p * rec / (p + rec)
    return {'shared': shared, 'candidate_words': sum(c.values()), 'reference_words': sum(r.values()),
            'precision': round(p, 3), 'recall': round(rec, 3), 'f1': round(f, 3),
            'matched': sorted((c & r).elements())}


out = {'reference': REFERENCE, 'reference_tokens': tokens(REFERENCE),
       'results': {k: dict(text=v, tokens=tokens(v), **rouge1(v, REFERENCE)) for k, v in CANDIDATES.items()}}
print(json.dumps(out, indent=1, ensure_ascii=False))
