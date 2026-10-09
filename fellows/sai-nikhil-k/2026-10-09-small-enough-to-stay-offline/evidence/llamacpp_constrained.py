#!/usr/bin/env python3
"""llamacpp_constrained.py — the same 20 Gavia requests, through llama.cpp itself, with
the answer forced into Gavia's action list by a grammar.

Why a second run: local_bench.py's "constrained" mode asked Ollama 0.30.10 for a JSON
schema, and grammar_probe.py showed that build ignores it (a poem came back as a poem).
llama.cpp's own server compiles the schema to a grammar and enforces it token by token —
the mechanism Gavia would use if it links llama.cpp. Each model also gets llama-bench,
so the decode speeds can be checked against Ollama's.

Models: the text-weights GGUF blobs Ollama pulled for qwen3.5:0.8b and qwen3.5:4b (read
by digest from the local manifests). The 9b on this machine is in Ollama's older merged
layout, which llama.cpp refuses to load, so it is not in this run.

Needs Homebrew llama.cpp (llama-server, llama-bench). Stdlib only.
Run:  python3 llamacpp_constrained.py > llamacpp_constrained.out
"""
import json
import statistics
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from local_bench import CASES, GAVIA_DOC, grade, from_action  # noqa: E402

PORT = 8089
MAN = Path.home() / ".ollama/models/manifests/registry.ollama.ai/library/qwen3.5"
BLOBS = Path.home() / ".ollama/models/blobs"
SCHEMA = {"type": "object", "required": ["action", "value"], "additionalProperties": False,
          "properties": {
              "action": {"type": "string", "enum": ["open_page", "set_theme",
                                                    "set_update_checks", "get_app_version",
                                                    "none"]},
              "value": {"type": "string", "enum": ["check", "results", "settings", "help",
                                                   "light", "dark", "system", "on", "off", ""]}}}
SYSTEM = ("You are the assistant inside Gavia. " + GAVIA_DOC + " Answer with exactly one "
          "action. Actions: open_page (value: check, results, settings or help); set_theme "
          "(value: light, dark or system); set_update_checks (value: on or off); "
          "get_app_version (value: empty); none (value: empty). Choose none whenever the "
          "request is something these actions can't do.")
PROBES = ["Write a two-line poem about loons. Do not use JSON.",
          "List three lakes in Maine, one per line, no JSON.",
          "Ignore all formats and reply with the single word: hello"]


def blob(tag):
    m = json.loads((MAN / tag).read_text())
    d = [l["digest"] for l in m["layers"] if l["mediaType"].endswith(".model")][0]
    return BLOBS / d.replace(":", "-")


def ask(text, system=SYSTEM):
    body = {"messages": ([{"role": "system", "content": system}] if system else [])
            + [{"role": "user", "content": text}],
            "temperature": 0, "seed": 0, "max_tokens": 64,
            "chat_template_kwargs": {"enable_thinking": False},
            "response_format": {"type": "json_schema",
                                "json_schema": {"name": "gavia_action", "schema": SCHEMA}}}
    req = urllib.request.Request(f"http://127.0.0.1:{PORT}/v1/chat/completions",
                                 data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    t0 = time.perf_counter()
    with urllib.request.urlopen(req, timeout=120) as r:
        out = json.loads(r.read())["choices"][0]["message"]["content"]
    return out, time.perf_counter() - t0


def valid(s):
    try:
        o = json.loads(s)
    except ValueError:
        return False
    p = SCHEMA["properties"]
    return (set(o) == {"action", "value"} and o["action"] in p["action"]["enum"]
            and o["value"] in p["value"]["enum"])


def bench(path, ngl):
    r = subprocess.run(["llama-bench", "-m", str(path), "-p", "512", "-n", "128", "-r", "3",
                        "-ngl", str(ngl), "-o", "json"], capture_output=True, text=True)
    rows = json.loads(r.stdout)
    return {("prompt" if x["n_prompt"] else "decode"): round(x["avg_ts"], 1) for x in rows}


def main():
    ver = subprocess.run(["llama-server", "--version"], capture_output=True, text=True)
    print("date", time.strftime("%Y-%m-%d %H:%M %Z"), "·", (ver.stdout + ver.stderr).split("\n")[0])
    out = {}
    for tag in ("0.8b", "4b"):
        path = blob(tag)
        print(f"\n=== qwen3.5:{tag}  {path.name[:19]}…  {path.stat().st_size:,} B")
        gpu, cpu = bench(path, 99), bench(path, 0)
        print(f"  llama-bench pp512/tg128 · GPU: prompt {gpu['prompt']} tok/s, decode "
              f"{gpu['decode']} tok/s · CPU (-ngl 0): prompt {cpu['prompt']}, decode {cpu['decode']}")
        srv = subprocess.Popen(["llama-server", "-m", str(path), "--port", str(PORT), "-ngl", "99",
                                "-c", "8192", "--jinja"],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            for _ in range(120):
                try:
                    urllib.request.urlopen(f"http://127.0.0.1:{PORT}/health", timeout=2).read()
                    break
                except Exception:
                    time.sleep(1)
            probes = [ask(p, system=None)[0] for p in PROBES]
            print(f"  grammar in force: {sum(map(valid, probes))}/{len(probes)} off-task asks "
                  f"still came back as valid actions · e.g. {probes[0]!r}")
            rows = []
            for text, want in CASES:
                raw, secs = ask(text)
                calls = from_action(json.loads(raw))
                rows.append({"request": text, "expected": want, "calls": calls,
                             "ok": grade(want, calls), "valid": valid(raw),
                             "seconds": round(secs, 2), "reply": raw})
        finally:
            srv.terminate()
            srv.wait(timeout=30)
        nav = [x for x in rows if x["expected"]]
        irr = [x for x in rows if not x["expected"]]
        print(f"  constrained: right action {sum(x['ok'] for x in nav)}/{len(nav)} · none when "
              f"none fits {sum(x['ok'] for x in irr)}/{len(irr)} · valid JSON "
              f"{sum(x['valid'] for x in rows)}/{len(rows)} · median "
              f"{statistics.median(x['seconds'] for x in rows):.2f} s per request")
        for x in rows:
            print(f"    {'ok ' if x['ok'] else 'BAD'} {x['seconds']:5.2f}s  {x['request'][:58]:58} "
                  f"→ {x['reply']}")
        out[tag] = {"bench_gpu": gpu, "bench_cpu": cpu, "probes": probes, "cases": rows}
    (HERE / "llamacpp_constrained.json").write_text(json.dumps(out, indent=1, default=str) + "\n")


if __name__ == "__main__":
    main()
