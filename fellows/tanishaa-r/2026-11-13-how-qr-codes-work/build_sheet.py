"""build_sheet.py — writes beat_sheet.json for "How a QR Code Works" from the approved
SCRIPT.md (v2, fact-checked; approved by Tanishaa 2026-11-13).

Same method as how-gps-works: reveal times are fractions of the beat, taken from
MEASURED word starts (mp3/words.json, faster-whisper on Bella's audio) once the audio
exists; before that, from word position. Nothing on screen runs on its own clock.
QR grids and B06/B07 numbers come from demo/qr_output.json (demo/qr_demo.py).

Run:  python3 build_sheet.py      (re-run after regenerating audio)
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHEET = HERE / "beat_sheet.json"
VOICE = "af_bella"
SPEED = 0.95
HANDLE = "@HumanitariansAI"
TITLE = "How a QR Code Works"
SHORT_TITLE = "How QR Codes Work"

old = {b["beat_id"]: b for b in json.loads(SHEET.read_text())["beats"]} if SHEET.exists() else {}
timings = json.loads((HERE / "mp3/timings.json").read_text()) if (HERE / "mp3/timings.json").exists() else {}
MEASURED = json.loads((HERE / "mp3/words.json").read_text()) if (HERE / "mp3/words.json").exists() else {}
DEMO = json.loads((HERE / "demo/qr_output.json").read_text())
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


N = {
 "B00": "Hi, I am Tanishaa, and this video is about how a QR code works. The voice you're hearing is Bella, an AI narrator reading a script Claude drafted and I approved.",
 "B01": "You can cover part of a QR code, and your phone still reads it. The missing piece isn't guessed. It's rebuilt from the rest of the code.",
 "B02": "A QR code is a grid of tiny squares. Each one is a single bit: dark means one, light means zero. It was invented in Japan in nineteen ninety-four, to track car parts on a factory line, which is why it's called Quick Response.",
 "B03": "First your camera has to find it. Those three big squares in the corners are finder patterns. They tell the phone where the code is, and which way up it's turned, even at an angle. The dotted lines between them count out the grid, so the phone knows where every square sits.",
 "B04": "Then it reads the data, starting at the bottom-right corner and snaking up and down, two columns at a time. Every eight bits make a byte, and the bytes spell out the link. A mask pattern is flipped over the top, so there are no big blank patches to confuse the camera.",
 "B05": "Here's the trick. A QR code carries more than your message. It also carries extra recovery data, worked out with a bit of math called Reed-Solomon, the same idea that lets a scratched CD keep playing. There are four levels. The lowest can recover about seven percent of the code. The highest, about thirty.",
 "B06": "Here it is for real. I made the same link at the lowest level and the highest, and covered the middle of each with a growing sticker. The low one broke once a seven by seven patch was gone. The high one still read with about a fifth of the whole code covered.",
 "B07": "That's why some QR codes have a logo in the middle. The logo is just damage, and the recovery data fills it in. The cost is a bigger code with more squares.",
 "B08": "So when can you trust it? A QR code is great at surviving smudges, scratches, and logos, and reading at an angle. But it has no idea whether the link inside is safe, and a scammer can just stick a new code over the real one. So always check the link your phone shows you before you open it.",
 "B09": "Three things to keep. A QR code is a grid of bits. The corner squares find it, and spare data repairs it. And it checks the code, not the link.",
 "B10": "Your turn. Ask Claude to be your tutor: send a message with one spare bit, flip a bit, and catch the error yourself. That's the first step toward how a QR code repairs itself.",
 "B11": "How a QR code works. At Humanitarians AI.",
}

YOUR_TURN = ("Act as my tutor. Give me a short message as bits, add one extra parity bit, then flip a bit and let me "
             "find the error. Then show me how QR codes go further and fix errors, not just find them.")


def shots():
    D = DEMO
    L, H = D["matrix"]["L"], D["matrix"]["H"]
    lv = D["levels"]
    return {
     "B00": ("ClaudeComposerAsk", {
        "greeting": "Hi, Tanishaa", "topic": "Irreducibly Human", "segment": SHORT_TITLE,
        "command": "How does my phone read a QR code?",
        "runningText": "thinking…",
        "output": ["Your camera finds the three corner squares,", "reads the grid of bits,",
                   "and repairs anything missing."],
        "folderLabel": HANDLE, "modelLabel": "Claude", "effortLabel": "AI narration: Bella", "largeText": True}),
     "B01": ("QrHook", {
        "matrix": H, "cover": lv["H"]["largest_centre_cover_modules"] - 4,
        "points": [{"text": "cover part of it", "at": at("B01", "cover part")},
                   {"text": "still reads", "at": at("B01", "still reads"), "accent": True},
                   {"text": "rebuilt from the rest", "at": at("B01", "rebuilt")}],
        "coverAt": at("B01", "cover part"), "readAt": at("B01", "still reads")}),
     "B02": ("QrGrid", {
        "matrix": L, "sizeLabel": f"{len(L)} × {len(L)} squares",
        "gridAt": at("B02", "grid of tiny"), "bitAt": at("B02", "single bit"), "darkAt": at("B02", "dark means"),
        "lightAt": at("B02", "light means"), "historyAt": at("B02", "invented"), "nameAt": at("B02", "Quick Response"),
        "history": "Japan · 1994 · tracking car parts", "name": "QR = Quick Response"}),
     "B03": ("QrFinders", {
        "matrix": L, "findAt": at("B03", "find it"), "findersAt": at("B03", "three big squares"),
        "angleAt": at("B03", "at an angle"), "timingAt": at("B03", "dotted lines")}),
     "B04": ("QrReadPath", {
        "matrix": L, "text": D["text"].replace("https://", "https://"),
        "startAt": at("B04", "bottom right"), "byteAt": at("B04", "8 bits"), "spellAt": at("B04", "spell out"),
        "maskAt": at("B04", "mask pattern")}),
     "B05": ("QrRecovery", {
        "low": D["codewords"]["L"], "high": D["codewords"]["H"],
        "msgAt": at("B05", "more than your message"), "recAt": at("B05", "extra recovery"),
        "rsAt": at("B05", "called Reed"), "levelsAt": at("B05", "four levels"),
        "lowAt": at("B05", "lowest"), "highAt": at("B05", "highest"),
        "levels": [{"name": "L", "pct": 7}, {"name": "M", "pct": 15}, {"name": "Q", "pct": 25}, {"name": "H", "pct": 30}]}),
     "B06": ("QrDemo", {
        "low": L, "high": H, "lowFail": lv["L"]["fails_at_modules"], "lowOk": lv["L"]["largest_centre_cover_modules"],
        "highOk": lv["H"]["largest_centre_cover_modules"], "highPct": lv["H"]["largest_centre_cover_pct_of_area"],
        "setupAt": at("B06", "same link"), "growAt": at("B06", "growing sticker"),
        "lowAt": at("B06", "low one"), "highAt": at("B06", "high one"),
        "footnote": "Real result: demo/qr_demo.py (segno encoder, OpenCV reader).",
        "footnoteShort": "Real test: OpenCV reader."}),
     "B07": ("QrLogo", {
        "matrix": H, "small": L, "logoModules": 13,
        "logoAt": at("B07", "logo in the middle"), "damageAt": at("B07", "just damage"),
        "fillAt": at("B07", "fills it in"), "costAt": at("B07", "bigger code")}),
     "B08": ("RagWhenToUse", {
        "useHeader": "It's good at", "skipHeader": "It can't tell you",
        "useHeaderAt": at("B08", "So when"), "skipHeaderAt": at("B08", "no idea"),
        "useItems": [{"text": "smudges, scratches, a logo", "at": at("B08", "smudges")},
                     {"text": "reading at an angle", "at": at("B08", "reading at")}],
        "skipItems": [{"text": "whether the link is safe", "at": at("B08", "no idea")},
                      {"text": "a sticker over the real code", "at": at("B08", "a scammer")}],
        "warning": "Check the link before you open it.", "warningAt": at("B08", "always check")}),
     "B09": ("GpsTakeaway", {
        "artifactTitle": SHORT_TITLE, "artifactHeading": "Three things to keep",
        "artifactLines": ["1. A QR code is a grid of bits.",
                          "2. Corner squares find it; spare data repairs it.",
                          "3. It checks the code, not the link."],
        "lineAt": [at("B09", "A QR code is"), at("B09", "the corner squares"), at("B09", "and it checks")]}),
     "B10": ("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "YOUR TURN · QR", "segment": SHORT_TITLE, "command": YOUR_TURN,
        "runningText": "paste this into Claude…", "output": [], "folderLabel": HANDLE,
        "modelLabel": "Claude", "effortLabel": "AI narration: Bella", "largeText": True}),
     "B11": ("HaiTitleOutro", {"title": "How QR Works", "handle": HANDLE}),  # "How QR Codes Work" wrapped past the safe area (GATE V)
    }


ACTS = {"B00": "ASK", "B01": "BLUF", "B02": "PROBLEM", "B03": "MECHANISM", "B04": "MECHANISM", "B05": "FRAMEWORK",
        "B06": "WORKED EXAMPLE", "B07": "SURPRISE", "B08": "WHEN NOT TO", "B09": "VERDICT", "B10": "YOUR TURN", "B11": "OUTRO"}
EST = {"B00": 13, "B01": 12, "B02": 16, "B03": 18, "B04": 18, "B05": 20, "B06": 20, "B07": 12, "B08": 22,
       "B09": 10, "B10": 18, "B11": 4}

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
  "title": TITLE, "slug": "how-qr-codes-work", "topic": "Irreducibly Human", "brand": "claude-hai",
  "skill": "ai-explainer", "audience": "students new to the topic", "register": "Plain",
  "engine": "kokoro", "voice_kokoro": VOICE, "palette": "claude", "channel": HANDLE,
  "greeting": "Hi, Tanishaa", "fellow": "Tanishaa",
  "fellow_intro": "Hi, I am Tanishaa and this video is about how a QR code works (required fellow opening line, B00).",
  "ai_disclosure": "Narration is Kokoro af_bella, an AI voice, disclosed aloud in B00 and on the composer chip.",
  "decisions": [
   "Topic chosen by Tanishaa on 2026-11-10 (QR codes, from four options). Script v2 (fact-checked) approved in chat on 2026-11-13 (\"Approved, build it\").",
   "Sync rule (Tanishaa): on-screen text never runs on its own clock; long narration shows key points only, each cued to its measured word. No BrutalistHesitantWriter.",
   "Same look as the earlier videos: Claude cream palette, HAI corner mark, HaiTitleOutro.",
   "Every QR grid on screen is the real module matrix from demo/qr_demo.py; B06/B07 numbers are its measured results."],
 },
 "beats": beats,
}
if (HERE / "beat_sheet.json").exists():
    prev = json.loads(SHEET.read_text())["metadata"]
    if "build" in prev:
        sheet["metadata"]["build"] = prev["build"]
SHEET.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
print(f"wrote {SHEET} — {len(beats)} beats, {sum(len(words(t)) for t in N.values())} words")
