# FACTCHECK — agents-use-tools

Verified 2026-10-02. DOUBLE-CHECK LAW: every number on screen is traced to its
source here, and anything that could not be verified was cut rather than softened.

| # | Claim (as it appears) | Verdict | Source | Fix applied |
|---|---|---|---|---|
| 1 | `153.6 KB  type_check.py` and the four other file sizes (B04) | **TRUE** | Live run of `ls -l runtime/scripts/*.py \| awk … \| sort -rn \| head -5` in `<home>/brutalist.art`, 2026-10-02 | none — verbatim output |
| 2 | type_check.py is the largest, ~3.5× the runner-up (B04 narration + bar) | **TRUE** | 153.6 / 43.5 = 3.53 | none |
| 3 | `P(clean) = pⁿ` (B07) | **TRUE** | Independent events: the probability that all n succeed is the product of the per-step probabilities | none |
| 4 | "one step works ninety-six percent … seventy-four in a row work five percent" (B07 narration) | **TRUE** | 0.96^74 = e^(74·ln 0.96) = e^(−3.021) = 0.0488 → 5% | none |
| 5 | "p = 71/74 tool calls succeeded, measured over one real session" (B07 on-screen) | **IMPRECISE — CORRECTED** | 71/74 was true at the 74-call mark. By the end of the same session: 162 calls, 4 errors, p = 0.9753 | Line changed to name the window: **"p = 71/74 over the first 74 tool calls of this film's own build session"** |
| 6 | "The model never opened a folder" (B05) | **TRUE** | Architectural: the model emits a `tool_use` block; the harness executes and returns a `tool_result`. The model receives text, never a file handle | none |
| 7 | Tool categories: shell, filesystem, browser, API, database, code execution (B03) | **TRUE** | Standard categories; all six are ordinary agent tool types, none invented | none |

## Note on claim 5 — the drift is interesting, not embarrassing

p *rose* from 0.9595 to 0.9753 as the session went on, because the early errors
were clustered in environment setup (a venv without pip, the `_smoke` slug, the
`npx` lookup). Once the environment was correct the failure rate fell. That is
the film's own thesis behaving as described: the loop observed failures and
recovered. The on-screen figure is anchored to the first-74 window so it matches
the spoken numbers exactly and remains independently checkable.

## Reproduce

```bash
# claim 1
cd <home>/brutalist.art
ls -l runtime/scripts/*.py | awk '{printf "%8.1f KB  %s\n", $5/1024, $9}' | sort -rn | head -5

# claims 4-5 (count tool_use / tool_result blocks in the session transcript)
python - <<'PY'
import json
f=r'<path to the Claude Code session transcript>.jsonl'
u=r_=e=0
for line in open(f,encoding='utf8'):
    try: d=json.loads(line)
    except: continue
    c=(d.get('message') or {}).get('content')
    if isinstance(c,list):
        for b in c:
            if isinstance(b,dict):
                if b.get('type')=='tool_use': u+=1
                if b.get('type')=='tool_result':
                    r_+=1
                    if b.get('is_error'): e+=1
print(u,r_,e,(r_-e)/r_)
PY
```

## Dated material stripped

No model version numbers, no pricing, no vendor counts that drift. "Claude" appears
only as the interface in the bookend beats, never as a claim about a product's
capabilities.
