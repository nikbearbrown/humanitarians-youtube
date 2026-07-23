#!/usr/bin/env python3
"""make_audio.py — generate the Bear-clone narration for ch01-angiogenesis, on your Mac.
Stdlib only (no pip). Same ElevenLabs call as riff_audio.py. Reads the key from your
unreal-reels/.env automatically. Writes audio/<id>.mp3 for every slide.

Slug: cancer-medicine-ch01-angiogenesis

Run:  python3 make_audio.py
Then tell Claude "audio done" — it stages the mp3s back and renders the voiced MP4.
"""
import json, os, re, sys, urllib.request, urllib.error
from pathlib import Path

HERE = Path(__file__).resolve().parent
# key: env first, then your repo .env (adjust if your path differs)
ENV_CANDIDATES = [
    Path.home() / "Documents/CoWork/bear-textbooks/books/unreal-reels/.env",
    HERE / ".env",
]

def load_key():
    k = os.getenv("ELEVENLABS_API_KEY")
    if k: return k
    for env in ENV_CANDIDATES:
        if env.exists():
            for line in env.read_text().splitlines():
                m = re.match(r"\s*ELEVENLABS_API_KEY\s*=\s*(.+)", line)
                if m: return m.group(1).strip().strip("'\"")
    sys.exit("[err] no ELEVENLABS_API_KEY in env or .env — set it and re-run")

SUB = {"—": ", ", "–": ", ", "…": "...", "%": " percent",
       "VEGF-A": "VEGF A", "VEGFR-2": "VEGFR 2", "HIF-1α": "HIF one alpha", "HIF-1-alpha": "HIF one alpha",
       "VHL": "V-H-L", "TSP-1": "TSP 1", "DLL4": "D-L-L-4", "PDGF": "P-D-G-F", "FGF": "F-G-F",
       "AV": "arteriovenous", "IFP": "interstitial fluid pressure",
       "PI3K": "P-I-3-K", "Bcl-2": "B-C-L-2", "AKT": "A K T", "APC": "A P C",
       "KRAS": "K-RAS", "p53": "p 53", "TP53": "T-P-53", "BAX": "backs", "C-D-Ks": "C D Ks"}

def spoken(t):
    for a, b in SUB.items(): t = t.replace(a, b)
    return re.sub(r"\s+", " ", t).strip()

def gen(text, voice, key, out):
    payload = {"text": text, "model_id": "eleven_multilingual_v2", "output_format": "mp3_44100_128",
               "voice_settings": {"stability": 0.80, "similarity_boost": 0.75, "style": 0.0,
                                  "use_speaker_boost": True, "speed": 0.94}}
    req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{voice}",
        data=json.dumps(payload).encode(), method="POST",
        headers={"Accept": "audio/mpeg", "Content-Type": "application/json", "xi-api-key": key})
    with urllib.request.urlopen(req, timeout=180) as r:
        out.write_bytes(r.read())

def measure(path):
    """real duration via ffprobe (ffmpeg is already on this Mac for the riff pipeline)."""
    import subprocess
    try:
        r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                            "-of", "default=nk=1:nw=1", str(path)], capture_output=True, text=True)
        return round(float(r.stdout.strip()), 2)
    except Exception:
        return None

def main():
    key = load_key()
    sheet = json.loads((HERE / "beat_sheet.json").read_text())
    voice = os.getenv("ELEVENLABS_VOICE_NIKBEARBROWN") or sheet["voice_id"]
    adir = HERE / "audio"; adir.mkdir(exist_ok=True)
    total = 0.0
    for s in sheet["segments"]:
        out = adir / f"{s['id']}.mp3"
        txt = spoken(s["beats"][0]["text"])
        try:
            gen(txt, voice, key, out)
        except urllib.error.HTTPError as e:
            sys.exit(f"[err] {s['id']} HTTP {e.code}: {e.read().decode('utf-8','ignore')[:300]}")
        dur = measure(out)
        s["beats"][0]["audio_file"] = f"audio/{s['id']}.mp3"
        s["beats"][0]["actual_duration_s"] = dur
        if dur: total += dur
        print(f"  [{s['id']}] {out.name}  {dur if dur else '?'}s  ({out.stat().st_size//1024} KB)")
    (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False))
    print(f"\n[ok] {len(sheet['segments'])} mp3s in {adir} · {total:.0f}s · durations written back to beat_sheet.json")
    print("[next] run:  python3 brutalist-art/runtime/scripts/build_deck.py <folder> && python3 brutalist-art/runtime/scripts/render.py <folder>")

if __name__ == "__main__":
    main()
