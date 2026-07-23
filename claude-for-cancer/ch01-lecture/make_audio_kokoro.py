#!/usr/bin/env python3
"""make_audio_kokoro.py — Kokoro TTS for lecture segments (free, local, no API key).

Reads segments from beat_sheet and generates audio/<id>.mp3 using the
Kokoro-82M ONNX model. Voice is taken from metadata.voice_kokoro (default: af_heart).
Writes actual_duration_s back to the beat sheet.

Usage:
  python3 make_audio_kokoro.py <lecture_folder>
  python3 make_audio_kokoro.py <lecture_folder> beat_sheet.hai.json
  python3 make_audio_kokoro.py <lecture_folder> beat_sheet.medhavy.json --only S03 S07

Model files (one-time, ~330 MB, no account needed):
  mkdir -p ../../brutalist-art/runtime/models/kokoro && cd ../../brutalist-art/runtime/models/kokoro
  curl -LO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
  curl -LO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
Install: pip install kokoro-onnx
"""
import argparse, json, os, re, shutil, struct, subprocess, sys, wave
from pathlib import Path

HERE_SCRIPT = Path(__file__).resolve().parent
FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
FFPROBE = shutil.which("ffprobe") or "ffprobe"
DEFAULT_VOICE = "af_heart"

# abbreviation expansions for TTS pronunciation
SUBS = {
    "—": ", ", "–": ", ", "…": "...", "%": " percent",
    "VEGF-A": "VEGF A", "VEGFR-2": "VEGFR 2",
    "HIF-1α": "HIF one alpha", "HIF-1-alpha": "HIF one alpha",
    "VHL": "V-H-L", "TSP-1": "TSP 1", "DLL4": "D-L-L-4",
    "PDGF": "P-D-G-F", "FGF": "F-G-F",
    "AV": "arteriovenous", "IFP": "interstitial fluid pressure",
    "ccRCC": "clear cell renal cell carcinoma",
    "PI3K": "P-I-3-K", "Bcl-2": "B-C-L-2", "AKT": "A K T",
    "KRAS": "K-RAS", "p53": "p 53", "TP53": "T-P-53",
    "VEGF": "V-E-G-F", "HAI": "Humanitarians AI",
}


def spoken(t):
    for a, b in SUBS.items():
        t = t.replace(a, b)
    return re.sub(r"\s+", " ", t).strip()


def model_paths():
    # walk up from the script's directory looking for brutalist-art/runtime/models/kokoro
    env_model = os.environ.get("KOKORO_MODEL")
    env_voices = os.environ.get("KOKORO_VOICES")
    if env_model and env_voices:
        return Path(env_model), Path(env_voices)

    art_home = os.environ.get("ART_HOME")
    search_roots = ([Path(art_home)] if art_home else []) + list(HERE_SCRIPT.parents)
    for root in search_roots:
        candidate = root / "brutalist-art" / "runtime" / "models" / "kokoro"
        m = candidate / "kokoro-v1.0.onnx"
        v = candidate / "voices-v1.0.bin"
        if m.exists() and v.exists():
            return m, v
    sys.exit(
        "[kokoro] model files not found. One-time download (~330 MB):\n"
        "  See make_audio_kokoro.py header for curl commands."
    )


def load_engine():
    model, voices = model_paths()
    try:
        from kokoro_onnx import Kokoro
    except ImportError:
        sys.exit("[kokoro] pip install kokoro-onnx")
    return Kokoro(str(model), str(voices))


LANG_BY_PREFIX = {
    "a": "en-us", "b": "en-gb", "j": "ja", "z": "cmn",
    "e": "es", "f": "fr-fr", "h": "hi", "i": "it", "p": "pt-br",
}


def lang_for(voice: str) -> str:
    return LANG_BY_PREFIX.get(voice[:1], "en-us")


def write_mp3(samples, sample_rate, out_mp3: Path):
    tmp = out_mp3.with_suffix(".tmp.wav")
    ints = [max(-32768, min(32767, int(s * 32767))) for s in samples]
    with wave.open(str(tmp), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sample_rate)
        w.writeframes(struct.pack(f"<{len(ints)}h", *ints))
    subprocess.run([FFMPEG, "-y", "-v", "error", "-i", str(tmp),
                    "-c:a", "libmp3lame", "-q:a", "2", str(out_mp3)], check=True)
    tmp.unlink()


def measure(path: Path) -> float:
    out = subprocess.run(
        [FFPROBE, "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True,
    )
    return round(float(out.stdout.strip()), 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", type=Path)
    ap.add_argument("beat_sheet", nargs="?", default="beat_sheet.json",
                    help="beat sheet filename inside folder (default: beat_sheet.json)")
    ap.add_argument("--only", nargs="*", default=None, help="segment IDs to (re)generate, e.g. S03 S07")
    ap.add_argument("--speed", type=float, default=1.0)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    folder = a.folder.resolve()
    sheet_path = folder / a.beat_sheet
    if not sheet_path.exists():
        sys.exit(f"[kokoro] beat sheet not found: {sheet_path}")
    sheet = json.loads(sheet_path.read_text())
    meta = sheet.get("metadata", {})
    voice = meta.get("voice_kokoro", DEFAULT_VOICE)
    lang = lang_for(voice)

    adir = folder / "audio"
    adir.mkdir(exist_ok=True)

    if not a.dry_run:
        engine = load_engine()
    else:
        engine = None

    total_s = 0.0
    generated = 0
    for seg in sheet.get("segments", []):
        sid = seg["id"]
        if a.only and sid not in a.only:
            continue
        beat = seg["beats"][0]
        raw_text = beat.get("text") or beat.get("narration_text", "")
        text = spoken(raw_text)
        out_mp3 = adir / f"{sid}.mp3"
        print(f"  [{sid}] {len(text.split())} words  voice={voice}  lang={lang}  → {out_mp3.name}")
        if a.dry_run:
            continue
        samples, sr = engine.create(text, voice=voice, speed=a.speed, lang=lang)
        write_mp3(samples, sr, out_mp3)
        dur = measure(out_mp3)
        beat["actual_duration_s"] = dur
        beat["audio_file"] = f"audio/{sid}.mp3"
        total_s += dur
        generated += 1
        print(f"         {dur:.2f}s  ({out_mp3.stat().st_size // 1024} KB)")

    if not a.dry_run:
        sheet_path.write_text(json.dumps(sheet, indent=2, ensure_ascii=False))
        print(f"\n[ok] {generated} mp3s in {adir}  total={total_s:.0f}s  durations written to {a.beat_sheet}")
        print("[next] python3 brutalist-art/runtime/scripts/build_deck.py <folder> <beat_sheet>  &&  python3 brutalist-art/runtime/scripts/render.py <folder> <beat_sheet>")
    else:
        print(f"\n[dry-run] would generate {sum(1 for s in sheet.get('segments', []) if not a.only or s['id'] in a.only)} mp3s")


if __name__ == "__main__":
    main()
