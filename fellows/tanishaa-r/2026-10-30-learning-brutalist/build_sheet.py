"""build_sheet.py — writes beat_sheet.json for "Learning Brutalist" from the approved SCRIPT.md (v2).

Same method as youtube/what-is-rag/build_sheet.py: reveal times are fractions of
the beat, taken from MEASURED word starts (mp3/words.json, faster-whisper on
Bella's audio) once the audio exists; before that, from word position.
Re-run after regenerating audio.

Run:  python3 build_sheet.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHEET = HERE / "beat_sheet.json"
VOICE = "af_bella"
SPEED = 0.95
HANDLE = "@HumanitariansAI"
TITLE = "Learning Brutalist"

old = {b["beat_id"]: b for b in json.loads(SHEET.read_text())["beats"]} if SHEET.exists() else {}
timings = json.loads((HERE / "mp3/timings.json").read_text()) if (HERE / "mp3/timings.json").exists() else {}
MEASURED = json.loads((HERE / "mp3/words.json").read_text()) if (HERE / "mp3/words.json").exists() else {}
LEAD_S = 0.2


def words(s):
    return re.findall(r"[A-Za-z0-9'’-]+", s)


def norm(s):
    return re.sub(r"[^a-z0-9']", "", s.lower().replace("’", "'"))


def at(bid, cue, nudge_s=0.0):
    """Fraction of beat `bid`'s scene at which `cue` is spoken (minus LEAD_S, plus nudge)."""
    c = [norm(x) for x in words(cue)]
    if bid in MEASURED and bid in timings:
        ws = [(norm(x["w"]), x["s"]) for x in MEASURED[bid]]
        ws = [(w, s) for w, s in ws if w]
        for i in range(len(ws) - len(c) + 1):
            if [w for w, _ in ws[i:i + len(c)]] == c:
                scene = timings[bid] + 0.4
                return round(max(0.0, min(0.95, (ws[i][1] - LEAD_S + nudge_s) / scene)), 4)
        raise SystemExit(f"cue {cue!r} not found in measured words for {bid}: {[w for w, _ in ws]}")
    w = [norm(x) for x in words(N[bid])]
    for i in range(len(w) - len(c) + 1):
        if w[i:i + len(c)] == c:
            return round(max(0.0, min(0.95, i / len(w))), 3)
    raise SystemExit(f"cue {cue!r} not found in: {N[bid]}")


# Spoken text. Respellings for the voice only: "eff eff em peg" (ffmpeg), "lay-tek" (LaTeX).
N = {
 "B00": "Hi, I am Tanishaa, and this video is about learning Brutalist, the toolkit Humanitarians AI fellows use to make videos, and the tools that come with it. The voice you're hearing is Bella, an AI narrator reading a script Claude drafted and I approved.",
 "B01": "Brutalist builds a video in steps. Every video starts as a beat sheet, one entry for each moment. The narration is generated first, and its measured length becomes the clock that every picture is timed to.",
 "B02": "Setting it up was my first lesson. My Mac didn't have the usual developer tools, so Claude Code installed everything into one self-contained environment. The setup check came back ready, except lay-tek, which only matters for math equations.",
 "B03": "Then I learned what each piece does. Claude Code runs the commands and writes the scene code. Kokoro makes the voice, on my own laptop, for free. Remotion and Manim draw every graphic from code, and eff eff em peg stitches the beats into one film.",
 "B04": "A video isn't done until it passes two automatic checks. One measures the text: is it big enough, readable, not overlapping. The other looks at every frame for layout problems.",
 "B05": "My first real test was a two-and-a-half-minute explainer called What Is RAG. One surprise: the vertical version isn't a crop. Each scene needed its own portrait layout with fewer words, so the text stays readable on a phone.",
 "B06": "The biggest lesson: the checks passed, but when I watched the preview, the list appeared after Bella said each item. Claude can't watch a video, so catching that was my job. We fixed it by timing each reveal to the measured word.",
 "B07": "If you're learning a toolkit like this, start with the setup check, push one small project all the way to the end, and watch every preview yourself. A passing check doesn't mean it works.",
 "B08": "Learning Brutalist. At Humanitarians AI.",
}


def shots():
    return {
     "B00": ("ClaudeComposerAsk", {
        "greeting": "Hi, Tanishaa", "topic": "Irreducibly Human", "segment": TITLE,
        "command": "How does Brutalist actually make a video?",
        "runningText": "thinking…",
        "output": ["Beat sheet → audio → visuals → checks.", "The narration sets the clock.", "You watch; the machine builds."],
        "folderLabel": HANDLE, "modelLabel": "Claude", "effortLabel": "AI narration: Bella", "largeText": True}),
     "B01": ("LbPipeline", {
        "spark": "One video, five steps.",
        "steps": [{"name": "Beat sheet", "sub": "one entry per moment"},
                  {"name": "Audio", "sub": "the clock"},
                  {"name": "Visuals", "sub": "timed to the audio"},
                  {"name": "Checks", "sub": "automatic gates"},
                  {"name": "Video", "sub": "4K master"}],
        "stepAt": [at("B01", "beat sheet"), at("B01", "narration is generated"), at("B01", "every picture"),
                   at("B01", "timed to"), at("B01", "timed to", 0.6)],
        "clockIndex": 1, "clockAt": at("B01", "becomes the clock")}),
     "B02": ("LbChecklist", {
        "spark": "First lesson: setup.",
        "title": "./setup",
        "items": [{"label": "Python", "logo": "python", "ok": True, "at": at("B02", "installed everything")},
                  {"label": "Node", "logo": "nodejs", "ok": True, "at": at("B02", "installed everything", 0.35)},
                  {"label": "ffmpeg", "logo": "ffmpeg", "ok": True, "at": at("B02", "installed everything", 0.7)},
                  {"label": "Bella and Onyx voices", "short": "Voices", "logo": "", "ok": True, "at": at("B02", "came back ready")},
                  {"label": "LaTeX", "logo": "latex", "ok": False, "note": "only needed for math equations", "noteShort": "math only",
                   "at": at("B02", "except")}],
        "footnote": "No Homebrew: everything lives in one micromamba environment.",
        "footnoteShort": "One micromamba environment",
        "footnoteAt": at("B02", "self")}),
     "B03": ("LbToolCards", {
        "spark": "What each piece does.",
        "cards": [{"name": "Claude Code", "role": "runs the build", "logos": ["claude-code"], "at": at("B03", "Claude Code runs")},
                  {"name": "Kokoro", "role": "local AI voices", "logos": [], "glyph": "wave", "at": at("B03", "makes the voice", -0.6)},
                  {"name": "Remotion + Manim", "role": "scenes written as code", "logos": ["remotion"], "at": at("B03", "draw every graphic", -0.9)},
                  {"name": "ffmpeg", "role": "joins the beats", "logos": ["ffmpeg"], "at": at("B03", "stitches", -0.9)}]}),
     "B04": ("LbGates", {
        "spark": "Two automatic checks.",
        "gates": [{"name": "GATE T", "desc": "type size, contrast, overlap", "result": "PASS", "at": at("B04", "One measures")},
                  {"name": "GATE V", "desc": "every frame reviewed", "result": "0 blockers", "at": at("B04", "The other looks")}],
        "footnote": "Results from the What Is RAG build, 2026-11-06.",
        "footnoteShort": "From the What Is RAG build"}),
     "B05": ("LbTwoFrames", {
        "spark": "First test: What Is RAG?",
        "landscape": "learning-brutalist/rag-land-57.png", "vertical": "learning-brutalist/rag-vert-57.png",
        "landTag": "3840×2160", "vertTag": "2160×3840",
        "landAt": at("B05", "My first"), "vertAt": at("B05", "the vertical"),
        "callout": "Own layout, fewer words. Not a crop.", "calloutShort": "Not a crop.", "calloutAt": at("B05", "Each scene needed"),
        "footnote": "Real frames from What Is RAG?, same moment in both versions.",
        "footnoteShort": "Real frames, same moment"}),
     "B06": ("LbSyncFix", {
        "spark": "What only I could catch.",
        "frame": "learning-brutalist/rag-land-118.png",
        "badge": "Checks: PASS", "badgeAt": at("B06", "checks passed"),
        "words": ["answer lives", "facts change", "cite a source"],
        "lagAt": at("B06", "the list appeared"),
        "fixAt": at("B06", "We fixed it"),
        "caption": "Claude can't watch a video. I can.", "captionAt": at("B06", "Claude can't watch"),
        "spokenLabel": "Bella says", "shownLabel": "On screen"}),
     "B07": ("ClaudeVerdictArtifact", {
        "artifactTitle": TITLE, "artifactHeading": "Learning a new toolkit?",
        "artifactLines": ["1. Run the setup check first.",
                          "2. Push one small video all the way through.",
                          "3. Watch every preview yourself."],
        "lineAt": [at("B07", "setup check"), at("B07", "push one"), at("B07", "watch every preview")],
        "lectureLayout": True,
        "lecturePageFrames": [0, round(at("B07", "watch every preview") * (timings.get("B07", 11) + 0.4) * 30)]}),
     "B08": ("HaiTitleOutro", {"title": TITLE, "handle": HANDLE}),
    }


ACTS = {"B00": "ASK", "B01": "FRAMEWORK", "B02": "SETUP", "B03": "TOOLS", "B04": "CHECKS",
        "B05": "WORKED EXAMPLE", "B06": "HUMAN JUDGEMENT", "B07": "TAKEAWAY", "B08": "OUTRO"}
EST = {"B00": 13, "B01": 16, "B02": 17, "B03": 20, "B04": 15, "B05": 18, "B06": 19, "B07": 14, "B08": 4}

SHOTS = shots()
beats = []
for bid, text in N.items():
    pattern, props = SHOTS[bid]
    o = old.get(bid, {})
    d = timings.get(bid) or o.get("actual_duration_s") or EST[bid]
    props = {**props, "durationSeconds": round(float(d) + 0.4, 2)}
    b = {"beat_id": bid, "act": ACTS[bid], "narration_text": text, "voice": VOICE, "engine": "kokoro",
         "speed": SPEED, "estimated_duration_s": EST[bid],
         "shot": {"type": "REMOTION", "source": "own", "remotion": {"pattern": pattern, "props": props}}}
    for k in ("audio_file", "actual_duration_s"):
        if k in o:
            b[k] = o[k]
    if bid in timings:
        b["actual_duration_s"] = timings[bid]
    beats.append(b)

sheet = {
 "metadata": {
  "title": TITLE, "slug": "learning-brutalist", "topic": "Irreducibly Human", "brand": "claude-hai",
  "skill": "ai-explainer", "audience": "new fellows and students", "register": "Plain",
  "engine": "kokoro", "voice_kokoro": VOICE, "palette": "claude", "channel": HANDLE,
  "greeting": "Hi, Tanishaa", "fellow": "Tanishaa",
  "fellow_intro": "Hi, I am Tanishaa and this video is about learning Brutalist (required fellow opening line, B00).",
  "ai_disclosure": "Narration is Kokoro af_bella, an AI voice, disclosed aloud in B00 and on the composer chip.",
  "decisions": [
   "Script v2 approved by Tanishaa in chat on 2026-11-06 (topic changed from weeks 1-2 to learning Brutalist).",
   "Same look as What Is RAG: Claude cream palette, HAI corner mark, HaiTitleOutro.",
   "LOGO LAW: tool logos shown where the toolkit has them (Claude Code, Remotion, ffmpeg, Python, Node, LaTeX). Kokoro and Manim have no logo in icons/logos, so Kokoro gets a drawn waveform and Manim is named beside the Remotion mark.",
   "B05/B06 use real frames from the What Is RAG masters (landscape and vertical at 57 s; landscape at 118 s)."],
 },
 "beats": beats,
}
SHEET.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
print(f"wrote {SHEET} — {len(beats)} beats, {sum(len(words(t)) for t in N.values())} words")
