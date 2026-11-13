"""build_sheet.py — writes beat_sheet.json for "How GPS Knows Where You Are" from the
approved SCRIPT.md (v1, with the key-points sync rule).

Same method as youtube/text-to-voice: reveal times are fractions of the beat, taken
from MEASURED word starts (mp3/words.json, faster-whisper on Bella's audio) once the
audio exists; before that, from word position. Nothing on screen runs on its own
clock. B06 data comes from demo/gps_output.json (demo/gps_demo.py).

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
TITLE = "How GPS Knows Where You Are"
SHORT_TITLE = "How GPS Works"

old = {b["beat_id"]: b for b in json.loads(SHEET.read_text())["beats"]} if SHEET.exists() else {}
timings = json.loads((HERE / "mp3/timings.json").read_text()) if (HERE / "mp3/timings.json").exists() else {}
MEASURED = json.loads((HERE / "mp3/words.json").read_text()) if (HERE / "mp3/words.json").exists() else {}
DEMO = json.loads((HERE / "demo/gps_output.json").read_text())
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
 "B00": "Hi, I am Tanishaa, and this video is about how GPS knows where you are. The voice you're hearing is Bella, an AI narrator reading a script Claude drafted and I approved.",
 "B01": "Your phone never sends anything to a GPS satellite. It only listens. It times how long each signal takes to arrive, and works out the one place you could be.",
 "B02": "Start with the problem. Your phone has no idea where it is, and no way to ask. All it can do is listen to radio signals from about thirty satellites, twenty thousand kilometers up.",
 "B03": "Each satellite broadcasts two things, over and over: where it is, and exactly what time it is, from an atomic clock on board. Your phone notes when each signal arrives. Multiply that delay by the speed of light, and you get the distance. Seven hundredths of a second means about twenty-one thousand kilometers.",
 "B04": "One distance tells you you're somewhere on a giant sphere around that satellite. A second sphere narrows it to a circle. A third narrows it to just two points, and one of them is out in space. Here it's flattened into circles, but the idea is the same: you're where they all meet.",
 "B05": "But there's a catch. Your phone's clock is cheap. If it's off by just one millionth of a second, every distance is off by three hundred meters. So your phone uses a fourth satellite to work out its own clock error. Three for where, one for when.",
 "B06": "Here it is on real numbers. I gave a solver four satellites above Boston Common and a phone clock that's off by one millionth of a second. Ignore the clock, and the answer lands three hundred ninety meters away. Solve for it, and it lands right on the spot, and finds the clock error too.",
 "B07": "One more surprise. Because of Einstein's relativity, the satellite clocks run fast by about thirty-eight millionths of a second a day. Left alone, your position would drift about eleven kilometers every day. So the clocks are set to tick slightly slow before launch.",
 "B08": "So when can you trust it? Outdoors under open sky, a phone is usually accurate to within about five meters. Between tall buildings, signals bounce, and your dot can jump across the street. Indoors and underground, the signal barely gets through, so your phone guesses from Wi-Fi and cell towers. And remember, GPS only listens. The satellites never know where you are, but your apps might.",
 "B09": "Three things to keep. GPS turns time into distance. Three satellites for where, one for when. And GPS only listens; your apps are what share your location.",
 "B10": "Your turn. Ask Claude to be your tutor: have it give you three circles, find where they meet yourself, then see what happens when every distance is off by the same amount. That's the clock problem, by hand.",
 "B11": "How GPS knows where you are. At Humanitarians AI.",
}

YOUR_TURN = ("Act as my tutor. Draw three circles on a simple map, give me each center and radius, and let me "
             "find where they meet. Then check my answer, and show me what happens if every radius is off by "
             "the same amount.")


def shots():
    D = DEMO
    return {
     "B00": ("ClaudeComposerAsk", {
        "greeting": "Hi, Tanishaa", "topic": "Irreducibly Human", "segment": SHORT_TITLE,
        "command": "How does GPS know where I am?",
        "runningText": "thinking…",
        "output": ["Your phone listens to satellites,", "times their signals,", "and works out where it must be."],
        "folderLabel": HANDLE, "modelLabel": "Claude", "effortLabel": "AI narration: Bella", "largeText": True}),
     "B01": ("GpsKeyPoints", {
        "points": [{"text": "never sends", "at": at("B01", "never sends")},
                   {"text": "only listens", "at": at("B01", "only listens"), "accent": True},
                   {"text": "times the signals → finds you", "at": at("B01", "It times")}]}),
     "B02": ("GpsSky", {
        "altitudeLabel": "~20,000 km up", "count": 30,
        "phoneAt": at("B02", "no idea"), "satsAt": at("B02", "about 30"), "altAt": at("B02", "20 000")}),
     "B03": ("GpsTimeDistance", {
        "where": "I'm here: (x, y, z)", "when": "It's exactly 12:00:00.000000",
        "travelS": D["travel_ms"][0] / 1000, "rangeKm": D["range_km"][0],
        "broadcastAt": at("B03", "broadcasts"), "clockAt": at("B03", "atomic clock"),
        "arriveAt": at("B03", "notes when"), "mathAt": at("B03", "Multiply"), "resultAt": at("B03", "700ths")}),
     "B04": ("GpsCircles", {
        "c1At": at("B04", "One distance"), "c2At": at("B04", "A second"), "c3At": at("B04", "A third"),
        "captionAt": at("B04", "flattened"), "meetAt": at("B04", "where they all meet"),
        "caption": "Flattened to circles. In 3D they're spheres."}),
     "B05": ("GpsClockError", {
        "errorLabel": "phone clock off by 0.000001 s", "meters": round(D["clock_error_m"]),
        "clockAt": at("B05", "clock is cheap"), "swellAt": at("B05", "every distance"),
        "fourthAt": at("B05", "fourth satellite"), "whereAt": at("B05", "Three for where"), "whenAt": at("B05", "one for when")}),
     "B06": ("GpsDemo", {
        "place": "Boston Common", "ranges": D["range_km"], "travelMs": D["travel_ms"],
        "clockUs": D["clock_error_us"], "ignoreM": D["ignore_clock_error_m"], "solvedUs": D["solved_clock_us"],
        "setupAt": at("B06", "four satellites"), "ignoreAt": at("B06", "Ignore the clock"),
        "solveAt": at("B06", "Solve for it"), "foundAt": at("B06", "finds the clock"),
        "footnote": "Satellite positions chosen for illustration; the solver and physics are real (demo/gps_demo.py).",
        "footnoteShort": "Real solver, example sky."}),
     "B07": ("GpsRelativity", {
        "net": 38, "gravity": 45, "speed": 7, "driftKm": round(D["relativity_drift_km_per_day"]),
        "clocksAt": at("B07", "satellite clocks run fast"), "whyAt": at("B07", "relativity"),
        "driftAt": at("B07", "Left alone"), "fixAt": at("B07", "set to tick")}),
     "B08": ("RagWhenToUse", {
        "useHeader": "Trust it", "skipHeader": "Expect it to slip",
        "useHeaderAt": at("B08", "can you trust"), "skipHeaderAt": at("B08", "Between tall"),
        "useItems": [{"text": "outdoors, open sky", "at": at("B08", "Outdoors")},
                     {"text": "within about 5 m", "at": at("B08", "within about")}],
        "skipItems": [{"text": "between tall buildings", "at": at("B08", "Between tall")},
                      {"text": "indoors: Wi-Fi and cell towers", "at": at("B08", "In doors")}],
        "warning": "GPS only listens. Your apps might share.", "warningAt": at("B08", "GPS only listens")}),
     "B09": ("GpsTakeaway", {
        "artifactTitle": SHORT_TITLE, "artifactHeading": "Three things to keep",
        "artifactLines": ["1. GPS turns time into distance.",
                          "2. Three satellites for where, one for when.",
                          "3. GPS only listens; your apps are what share."],
        "lineAt": [at("B09", "GPS turns"), at("B09", "three satellites"), at("B09", "and GPS only")]}),
     "B10": ("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "YOUR TURN · GPS", "segment": SHORT_TITLE, "command": YOUR_TURN,
        "runningText": "paste this into Claude…", "output": [], "folderLabel": HANDLE,
        "modelLabel": "Claude", "effortLabel": "AI narration: Bella", "largeText": True}),
     "B11": ("HaiTitleOutro", {"title": SHORT_TITLE, "handle": HANDLE}),
    }


ACTS = {"B00": "ASK", "B01": "BLUF", "B02": "PROBLEM", "B03": "MECHANISM", "B04": "FRAMEWORK", "B05": "CATCH",
        "B06": "WORKED EXAMPLE", "B07": "SURPRISE", "B08": "WHEN NOT TO", "B09": "VERDICT", "B10": "YOUR TURN", "B11": "OUTRO"}
EST = {"B00": 13, "B01": 12, "B02": 15, "B03": 20, "B04": 22, "B05": 16, "B06": 19, "B07": 17, "B08": 24,
       "B09": 10, "B10": 20, "B11": 4}

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
  "title": TITLE, "slug": "how-gps-works", "topic": "Irreducibly Human", "brand": "claude-hai",
  "skill": "ai-explainer", "audience": "students new to the topic", "register": "Plain",
  "engine": "kokoro", "voice_kokoro": VOICE, "palette": "claude", "channel": HANDLE,
  "greeting": "Hi, Tanishaa", "fellow": "Tanishaa",
  "fellow_intro": "Hi, I am Tanishaa and this video is about how GPS knows where you are (required fellow opening line, B00).",
  "ai_disclosure": "Narration is Kokoro af_bella, an AI voice, disclosed aloud in B00 and on the composer chip.",
  "decisions": [
   "Script v1 approved by Tanishaa in chat on 2026-11-08 (\"Approved, build it\").",
   "Sync rule (Tanishaa): on-screen text never runs on its own clock; long narration shows key points only, each cued to its measured word. No BrutalistHesitantWriter.",
   "Same look as the earlier videos: Claude cream palette, HAI corner mark, HaiTitleOutro.",
   "B06 numbers are real output of demo/gps_demo.py; satellite positions are illustrative and labeled so."],
 },
 "beats": beats,
}
SHEET.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
print(f"wrote {SHEET} — {len(beats)} beats, {sum(len(words(t)) for t in N.values())} words")
