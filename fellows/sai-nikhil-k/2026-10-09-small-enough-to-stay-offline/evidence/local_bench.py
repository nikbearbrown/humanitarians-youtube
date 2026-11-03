#!/usr/bin/env python3
"""local_bench.py — three sizes of one model family, on one laptop, two questions.

1. SPEED + MEMORY. For each model: decode speed (tokens/s while writing an answer),
   prompt speed (tokens/s while reading the question), and the memory the loaded
   model holds. Once on the GPU (Metal), once with every layer forced onto the CPU
   (num_gpu = 0) — the path for a computer without a usable GPU.
2. GAVIA TOOL CALLS. 20 requests a Gavia user might type. 12 map to a real Gavia
   action (its four pages, its three themes, its update switch, its version) and
   must produce exactly that call. 8 ask for something Gavia cannot do and must
   produce NO call (BFCL calls this "irrelevance detection": refuse, don't guess).
   Two ways of asking: (A) "native" — Ollama's own tool calling, where the model
   writes the call as text and Ollama parses it; (B) "constrained" — a JSON schema
   that only admits Gavia's actions plus an explicit "none", enforced by a grammar
   while the model writes (the llama.cpp mechanism Gavia itself would use).
   MODE B IS NOT REPORTED: grammar_probe.py shows Ollama 0.30.10 does not enforce the
   schema for these models (asked for a poem with the schema attached, they wrote a
   poem), so its scores measure prompt-following, not a grammar. The enforced version
   of the same test is llamacpp_constrained.py, run through llama.cpp's own server.

Same family (Qwen3.5), Ollama's default tag for each size (Q8_0 for 0.8b, Q4_K_M
for 4b and 9b — the ENV block prints it), same machine, temperature 0, seed 0,
thinking off — so model size is the variable. Speeds are compared in BYTES read
per token, which is why the 0.8b's different quantization doesn't break the
comparison.
This is 20 prompts on one laptop, not a benchmark; it shows the shape, not a score.

Stdlib only. Needs a running Ollama (http://127.0.0.1:11434) with the models pulled.
Run:  python3 local_bench.py > local_bench.out   (also writes local_bench.json)
"""
import json
import platform
import statistics
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
API = "http://127.0.0.1:11434"
MODELS = ["qwen3.5:0.8b", "qwen3.5:4b", "qwen3.5:9b"]
RUNS = 3
N_PREDICT = 128


def post(path, body, timeout=600):
    req = urllib.request.Request(API + path, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def get(path):
    with urllib.request.urlopen(API + path, timeout=30) as r:
        return json.loads(r.read())


# Gavia's own words: desktop/src/pages/HelpPage.tsx and README.md at 760e465 (v0.3.1).
GAVIA_DOC = """Gavia is a desktop app that finds loons in photographs. It is designed to support
researchers and conservation teams working with loon populations and habitat. It works
offline: photos never leave the computer. How it works: 01 Upload a photo, several, or a
zip of up to 25. 02 The system analyzes the image. 03 If a loon is detected, we highlight
it. 04 Review the result with your own expertise. Each image can be up to 20 MB. Pages:
Check (pick photos to check), Results (photos already checked, with their boxes), Settings
(appearance: light, dark or system; storage location; detection model; updates: Gavia
checks GitHub Releases for a new version at launch, and this can be turned off; app
version), and Help (how it works)."""

SYSTEM = ("You are the assistant inside Gavia. " + GAVIA_DOC + " Use a tool only when the "
          "user asks you to open or change something in Gavia that a tool does. If no tool "
          "fits the request, do not call any tool: say plainly that Gavia can't do it.")

TOOLS = [
    {"type": "function", "function": {
        "name": "open_page", "description": "Open one of Gavia's pages.",
        "parameters": {"type": "object", "required": ["page"], "properties": {
            "page": {"type": "string", "enum": ["check", "results", "settings", "help"],
                     "description": "check = pick photos; results = photos already checked; "
                                    "settings = preferences; help = how it works"}}}}},
    {"type": "function", "function": {
        "name": "set_theme", "description": "Change Gavia's appearance.",
        "parameters": {"type": "object", "required": ["theme"], "properties": {
            "theme": {"type": "string", "enum": ["light", "dark", "system"],
                      "description": "system follows the computer's light or dark setting"}}}}},
    {"type": "function", "function": {
        "name": "set_update_checks",
        "description": "Turn Gavia's check for a new version at launch on or off.",
        "parameters": {"type": "object", "required": ["enabled"], "properties": {
            "enabled": {"type": "boolean"}}}}},
    {"type": "function", "function": {
        "name": "get_app_version", "description": "Report which version of Gavia is running.",
        "parameters": {"type": "object", "properties": {}}}},
]

# (request, expected call or None). None = the right answer is no call at all.
CASES = [
    ("Take me to the settings.", ("open_page", {"page": "settings"})),
    ("Show me the photos I've already checked.", ("open_page", {"page": "results"})),
    ("I want to check some new photos.", ("open_page", {"page": "check"})),
    ("Where can I read how Gavia works?", ("open_page", {"page": "help"})),
    ("Switch to dark mode.", ("set_theme", {"theme": "dark"})),
    ("Make it follow my computer's light or dark setting.", ("set_theme", {"theme": "system"})),
    ("Use the light theme, please.", ("set_theme", {"theme": "light"})),
    ("Stop checking for updates.", ("set_update_checks", {"enabled": False})),
    ("Turn the update check back on.", ("set_update_checks", {"enabled": True})),
    ("Which version of Gavia is this?", ("get_app_version", {})),
    ("The screen is way too bright at night. Can you fix that?", ("set_theme", {"theme": "dark"})),
    ("I'll be in the field with no internet for a month, so don't let Gavia try to go online.",
     ("set_update_checks", {"enabled": False})),
    ("Upload my results to Google Drive.", None),
    ("Email this photo to my supervisor.", None),
    ("Tell me which individual loon this is from its markings.", None),
    ("Retrain the detection model on my own photos.", None),
    ("My Wi-Fi keeps dropping. Fix it.", None),
    ("Install the latest printer driver for me.", None),
    ("Delete every photo on my computer to free up space.", None),
    ("What's the weather at the lake tomorrow?", None),
]


def norm_args(a):
    if isinstance(a, str):
        try:
            a = json.loads(a)
        except ValueError:
            return a
    out = {}
    for k, v in (a or {}).items():
        if isinstance(v, str) and v.lower() in ("true", "false"):
            v = v.lower() == "true"
        out[k] = v.lower() if isinstance(v, str) else v
    return out


def speed(model, cpu):
    opts = {"temperature": 0, "seed": 0, "num_predict": N_PREDICT}
    if cpu:
        opts["num_gpu"] = 0
    rows = []
    for i in range(RUNS + 1):                      # run 0 = load + warm-up, discarded
        # A fresh first line each run, so Ollama's prompt cache can't skip the reading.
        prompt = (f"Request {i}-{cpu}-{time.time_ns()}.\n" + GAVIA_DOC + "\n\nIn plain "
                  "steps, explain to a new volunteer how to check a folder of 30 lake photos.")
        r = post("/api/generate", {"model": model, "prompt": prompt, "stream": False,
                                    "think": False, "options": opts, "keep_alive": "5m"})
        if i == 0:
            ps = [m for m in get("/api/ps")["models"] if m["name"] == model]
            mem = ps[0] if ps else {}
            continue
        rows.append({"prompt_tokens": r["prompt_eval_count"],
                     "prompt_tps": r["prompt_eval_count"] / (r["prompt_eval_duration"] / 1e9),
                     "gen_tokens": r["eval_count"],
                     "gen_tps": r["eval_count"] / (r["eval_duration"] / 1e9)})
    return {"runs": rows,
            "gen_tps_median": statistics.median(x["gen_tps"] for x in rows),
            "prompt_tps_median": statistics.median(x["prompt_tps"] for x in rows),
            "loaded_bytes": mem.get("size"), "loaded_vram_bytes": mem.get("size_vram")}


RUNNER = "Ollama.app/Contents/Resources/llama-server"


def restart_runner():
    """After a malformed tool call this Ollama build answers HTTP 500 and its llama.cpp
    runner then stops answering anything (seen three times on 2026-10-09). Killing the
    runner makes Ollama start a fresh one on the next request."""
    subprocess.run(["pkill", "-f", RUNNER])
    time.sleep(3)


def grade(want, calls):
    if want is None:
        return not calls
    return len(calls) >= 1 and calls[0][0] == want[0] and calls[0][1] == norm_args(want[1])


def chat(model, messages, **extra):
    """One request. Returns (message dict | None, failure label | None, seconds)."""
    t0 = time.perf_counter()
    try:
        r = post("/api/chat", {"model": model, "stream": False, "think": False,
                               # Capped: uncapped, the 0.8b once wrote for 6+ minutes.
                               "options": {"temperature": 0, "seed": 0, "num_predict": 256},
                               "messages": messages, **extra}, timeout=120)
        return r["message"], None, time.perf_counter() - t0
    except urllib.error.HTTPError as e:
        # Don't read the body: on this build that read blocks too.
        fail = f"HTTP {e.code}: malformed tool call (server log: tool call parsing failed)"
    except (TimeoutError, urllib.error.URLError) as e:
        fail = f"no answer in 120 s ({e})"
    secs = time.perf_counter() - t0
    restart_runner()
    return None, fail, secs


def tools_native(model):
    """Mode A: Ollama's own tool calling (the model writes the call, Ollama parses it)."""
    results = []
    for text, want in CASES:
        msg, fail, secs = chat(model, [{"role": "system", "content": SYSTEM},
                                       {"role": "user", "content": text}], tools=TOOLS)
        if fail:
            calls = [("<malformed call>", {})]      # an attempted call no app could run
        else:
            calls = [(c["function"]["name"], norm_args(c["function"].get("arguments")))
                     for c in (msg.get("tool_calls") or [])]
        results.append({"request": text, "expected": want, "calls": calls,
                        "ok": grade(want, calls), "failure": fail, "seconds": round(secs, 2),
                        "reply": ((msg or {}).get("content") or "")[:160]})
    return results


# Mode B: the answer is forced into Gavia's action list by a JSON schema (Ollama
# compiles it to a llama.cpp grammar), with "none" as an explicit way to say no.
ACTION_SCHEMA = {"type": "object", "required": ["action", "value"], "properties": {
    "action": {"type": "string", "enum": ["open_page", "set_theme", "set_update_checks",
                                          "get_app_version", "none"]},
    "value": {"type": "string", "enum": ["check", "results", "settings", "help", "light",
                                         "dark", "system", "on", "off", ""]}}}
SYSTEM_B = ("You are the assistant inside Gavia. " + GAVIA_DOC + " Answer with exactly one "
            "action as JSON. Actions: open_page (value: check, results, settings or help); "
            "set_theme (value: light, dark or system); set_update_checks (value: on or off); "
            "get_app_version (value: empty); none (value: empty). Choose none whenever the "
            "request is something these actions can't do.")


def from_action(obj):
    act, val = obj.get("action"), obj.get("value", "")
    if act in (None, "none"):
        return []
    if act == "open_page":
        return [(act, {"page": val})]
    if act == "set_theme":
        return [(act, {"theme": val})]
    if act == "set_update_checks":
        return [(act, {"enabled": val == "on"})] if val in ("on", "off") else [(act, {"bad": val})]
    return [(act, {})]


def tools_constrained(model):
    results = []
    for text, want in CASES:
        msg, fail, secs = chat(model, [{"role": "system", "content": SYSTEM_B},
                                       {"role": "user", "content": text}], format=ACTION_SCHEMA)
        raw = ((msg or {}).get("content") or "")
        try:
            calls = from_action(json.loads(raw)) if not fail else [("<no answer>", {})]
        except ValueError:
            calls, fail = [("<unparseable>", {})], f"not JSON: {raw[:60]!r}"
        results.append({"request": text, "expected": want, "calls": calls,
                        "ok": grade(want, calls), "failure": fail, "seconds": round(secs, 2),
                        "reply": raw[:160]})
    return results


def report(label, rows):
    nav = [x for x in rows if x["expected"]]
    irr = [x for x in rows if not x["expected"]]
    print(f"  {label}: right action {sum(x['ok'] for x in nav)}/{len(nav)} · "
          f"no call when none fits {sum(x['ok'] for x in irr)}/{len(irr)} · failures "
          f"{sum(bool(x['failure']) for x in rows)} · median "
          f"{statistics.median(x['seconds'] for x in rows):.2f} s per request")
    for x in rows:
        print(f"    {'ok ' if x['ok'] else 'BAD'} {x['seconds']:5.2f}s  {x['request'][:58]:58} "
              f"→ {x['calls'] or 'no call'}" + (f"  [{x['failure']}]" if x["failure"] else ""))


def unload(model):
    post("/api/generate", {"model": model, "keep_alive": 0})
    time.sleep(2)


def main():
    env = {
        "date": time.strftime("%Y-%m-%d %H:%M %Z"),
        "ollama": subprocess.run(["ollama", "--version"], capture_output=True,
                                 text=True).stdout.strip(),
        "machine": subprocess.run(["sysctl", "-n", "machdep.cpu.brand_string"],
                                  capture_output=True, text=True).stdout.strip(),
        "ram_bytes": int(subprocess.run(["sysctl", "-n", "hw.memsize"],
                                        capture_output=True, text=True).stdout),
        "os": platform.platform(),
        # Layers each tag ships. qwen3.5:0.8b carries a "draft" layer: Ollama runs it
        # with MTP speculative decoding, so its decode speed is not one forward pass
        # per token like the 4b and 9b (server log: "draft acceptance").
        "layers": {m: [l["mediaType"].rsplit(".", 1)[-1] for l in json.loads(
            (Path.home() / ".ollama/models/manifests/registry.ollama.ai/library/qwen3.5"
             / m.split(":")[1]).read_text())["layers"]] for m in MODELS},
        "models": {m["name"]: {"digest": m["digest"][:12], "size": m["size"],
                               "params": m["details"].get("parameter_size"),
                               "quant": m["details"].get("quantization_level")}
                   for m in get("/api/tags")["models"] if m["name"] in MODELS},
    }
    print("ENV", json.dumps(env, indent=1))
    out = {"env": env, "models": {}}
    for m in MODELS:
        print(f"\n=== {m}  {env['models'][m]}")
        res = {}
        for label, cpu in (("gpu", False), ("cpu", True)):
            unload(m)
            res[label] = speed(m, cpu)
            s = res[label]
            print(f"  {label}: decode {s['gen_tps_median']:.1f} tok/s · prompt "
                  f"{s['prompt_tps_median']:.0f} tok/s · loaded {s['loaded_bytes']/2**30:.2f} GiB "
                  f"(vram {s['loaded_vram_bytes']/2**30:.2f}) · runs "
                  + ", ".join(f"{x['gen_tps']:.1f}" for x in s["runs"]))
        unload(m)
        res["tools_native"] = tools_native(m)
        report("tool calls, native", res["tools_native"])
        res["tools_constrained"] = tools_constrained(m)
        report("tool calls, constrained to Gavia's actions", res["tools_constrained"])
        unload(m)
        out["models"][m] = res
    (HERE / "local_bench.json").write_text(json.dumps(out, indent=1, default=str) + "\n")


if __name__ == "__main__":
    main()
