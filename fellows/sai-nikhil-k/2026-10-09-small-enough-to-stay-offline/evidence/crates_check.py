import json, sys, time, urllib.request
print(f"crates.io API, read {time.strftime('%Y-%m-%d %H:%M %Z')} — Rust bindings for the two engines in B05 (and ort, which Gavia ships).")
for name in ("llama-cpp-2", "onnx-genai", "ort"):
    req = urllib.request.Request(f"https://crates.io/api/v1/crates/{name}", headers={"User-Agent": "claude-factcheck"})
    d = json.loads(urllib.request.urlopen(req, timeout=30).read())
    c, v = d["crate"], d["versions"][0]
    print(f"{name}: max {c['max_version']} ({v['created_at'][:10]}, licence {v['license']}) · all-time downloads "
          f"{c['downloads']:,} · first published {c['created_at'][:10]} · repo {c.get('repository')}")
print('onnxruntime-genai README (main): API row = "Python <br/>C# <br/>C/C++ <br/> Java ^ | Objective-C" — no Rust.')
print("Neither Rust binding is published by its engine's own project: llama-cpp-2 is utilityai's, onnx-genai is justinchuby's.")
