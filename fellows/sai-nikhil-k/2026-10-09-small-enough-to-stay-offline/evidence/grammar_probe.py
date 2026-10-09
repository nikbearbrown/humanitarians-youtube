#!/usr/bin/env python3
"""grammar_probe.py — is the JSON schema actually enforced, or did the model just comply?

local_bench.py's constrained mode got 20/20 on the 4b and 9b but returned '{"none"}'
(not valid under the schema) on the 0.8b. A grammar cannot emit that, so either the
schema was not applied to the 0.8b, or something skipped it. Probe: ask each model for
things the schema forbids (a poem, a list, free prose) with the same schema attached.
If every reply still parses and validates, the grammar is in force for that model.

The 0.8b tag is the one that ships a "draft" layer (MTP speculative decoding); the
hypothesis is that drafted tokens bypass the grammar on this Ollama build.

Stdlib only. Run:  python3 grammar_probe.py > grammar_probe.out
"""
import json
import subprocess
import time
import urllib.request

API = "http://127.0.0.1:11434"
SCHEMA = {"type": "object", "required": ["action", "value"], "properties": {
    "action": {"type": "string", "enum": ["open_page", "set_theme", "set_update_checks",
                                          "get_app_version", "none"]},
    "value": {"type": "string", "enum": ["check", "results", "settings", "help", "light",
                                         "dark", "system", "on", "off", ""]}}}
ASKS = ["Write a two-line poem about loons. Do not use JSON.",
        "List three lakes in Maine, one per line, no JSON.",
        "Ignore all formats and reply with the single word: hello"]


def valid(s):
    try:
        o = json.loads(s)
    except ValueError:
        return False
    p = SCHEMA["properties"]
    return (isinstance(o, dict) and set(o) == {"action", "value"}
            and o["action"] in p["action"]["enum"] and o["value"] in p["value"]["enum"])


print("date", time.strftime("%Y-%m-%d %H:%M %Z"), "·",
      subprocess.run(["ollama", "--version"], capture_output=True, text=True).stdout.strip())
for model in ("qwen3.5:0.8b", "qwen3.5:4b"):
    ok = 0
    for ask in ASKS:
        body = {"model": model, "stream": False, "think": False, "format": SCHEMA,
                "options": {"temperature": 0, "seed": 0, "num_predict": 64},
                "messages": [{"role": "user", "content": ask}]}
        req = urllib.request.Request(API + "/api/chat", data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=120) as r:
            out = json.loads(r.read())["message"]["content"]
        ok += valid(out)
        print(f"{model:14} {'valid  ' if valid(out) else 'INVALID'} {ask[:40]!r:44} → {out[:70]!r}")
    print(f"{model}: {ok}/{len(ASKS)} replies valid under the schema")
    req = urllib.request.Request(API + "/api/generate",
                                 data=json.dumps({"model": model, "keep_alive": 0}).encode(),
                                 headers={"Content-Type": "application/json"})
    urllib.request.urlopen(req, timeout=60).read()
