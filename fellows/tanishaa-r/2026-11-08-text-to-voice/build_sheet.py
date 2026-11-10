"""build_sheet.py — writes beat_sheet.json for "How a Computer Turns Text into a Voice"
from the approved SCRIPT.md (v2).

Same method as youtube/what-is-rag and youtube/learning-brutalist: reveal times are
fractions of the beat, taken from MEASURED word starts (mp3/words.json, faster-whisper
on Bella's audio) once the audio exists; before that, from word position.
B04/B05 data comes from demo/tts_output.json (demo/tts_demo.py, real Kokoro output).

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
TITLE = "How a Computer Turns Text into a Voice"
SHORT_TITLE = "Text into a Voice"

old = {b["beat_id"]: b for b in json.loads(SHEET.read_text())["beats"]} if SHEET.exists() else {}
timings = json.loads((HERE / "mp3/timings.json").read_text()) if (HERE / "mp3/timings.json").exists() else {}
MEASURED = json.loads((HERE / "mp3/words.json").read_text()) if (HERE / "mp3/words.json").exists() else {}
DEMO = json.loads((HERE / "demo/tts_output.json").read_text())
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


# Spoken text. Voice-only respellings: "red and reed" (B02, "read and read"; Kokoro
# would say "reed" twice) and "instead of red" (B05). B05's "I read it yesterday" is
# left as typed on purpose: Bella saying "reed" there is the demo.
N = {
 "B00": "Hi, I am Tanishaa, and this video is about how a computer turns text into a voice. The voice you're hearing is Bella, an AI narrator reading a script Claude drafted and I approved. So she's also the example.",
 "B01": "A computer doesn't read the way you do. It works out which sounds to make, plans how long and how high each one goes, and then builds the sound wave, number by number.",
 "B02": "Start with the problem. Writing is a shorthand for speech. The same letters can sound different: red and reed. The same abbreviation can mean two things: doctor and drive. And numbers aren't words at all until something decides how to say them.",
 "B03": "Most text-to-speech systems follow four steps. Clean up: spell out numbers and abbreviations. Sound it out: turn each word into phonemes, the small sounds speech is made of. Plan the delivery: how long, how high and how loud each sound should be. Then build the wave.",
 "B04": "Sound is just air pressure going up and down. Recorded digitally, it's a list of numbers, and Bella's audio uses twenty-four thousand of them every second. A neural network predicts those numbers. The voice itself is another list, two hundred fifty-six numbers. Swap that list, and the same words come out in a different voice.",
 "B05": "Here's what Bella's own system did with those tricky lines. For I read it yesterday, it said reed, the present tense, instead of red. Oak Drive became Oak Doctor. And five dollars became dollar five. A different voice made the exact same mistakes, because the voice only changes the style, not the sounds.",
 "B06": "So when is it useful? Reading text aloud for accessibility, drafting a narration, or hearing how a word sounds. Be careful with names and unusual words, which it often gets wrong, and with moments where tone matters. And because it sounds so human, always say it's an AI voice. Never copy a real person's voice without their permission.",
 "B07": "Three things to keep. It works out sounds; it doesn't read the way you do. A voice is just a set of numbers. And sounding human isn't the same as being right.",
 "B08": "Your turn. Take something you've written and try this prompt: find every word an AI voice might say wrong, explain why, and rewrite it so it's spoken correctly. Then listen to both versions. You'll hear the difference.",
 "B09": "How a computer turns text into a voice. At Humanitarians AI.",
}


def spoken_lines(bid, breaks, accent=()):
    """The narration as on-screen words, each cued to its MEASURED start (small lead).
    Display text is the script's own words (with punctuation); timing is faster-whisper's."""
    shown = N[bid].split()
    heard = [x for x in MEASURED.get(bid, []) if norm(x["w"])]
    if len(heard) != len(shown):
        raise SystemExit(f"{bid}: {len(shown)} script words vs {len(heard)} measured; align by hand")
    scene = timings[bid] + 0.4
    words_ = [{"w": w, "at": round(max(0.0, (h["s"] - 0.08) / scene), 4), "accent": i in accent}
              for i, (w, h) in enumerate(zip(shown, heard))]
    cuts = [0, *breaks, len(words_)]
    return [words_[a:b] for a, b in zip(cuts, cuts[1:])]

YOUR_TURN = ("Here's a paragraph I want read aloud by an AI voice. Find every word it might say wrong "
             "(numbers, abbreviations, names, and words like 'read' or 'lead' that change sound with meaning), "
             "explain why, and rewrite the paragraph so it's spoken correctly.")

S = DEMO["sentences"]   # 0 read/past, 1 read/future, 2 Dr., 3 $5
BELLA, OTHER = "af_bella", "am_michael"


def shots():
    return {
     "B00": ("ClaudeComposerAsk", {
        "greeting": "Hi, Tanishaa", "topic": "Irreducibly Human", "segment": SHORT_TITLE,
        "command": "How does a computer turn text into a voice?",
        "runningText": "thinking…",
        "output": ["Text-to-speech works out the sounds,", "plans timing and pitch,", "then builds the sound wave."],
        "folderLabel": HANDLE, "modelLabel": "Claude", "effortLabel": "AI narration: Bella", "largeText": True}),
     "B01": ("TtvSpokenLines", {"lines": spoken_lines("B01", breaks=[8, 15, 24, 30], accent={2, 3}), "fontSize": 84}),
    "B02": ("TtvTrickyLines", {
        "spark": "Writing is shorthand for speech.",
        "lines": [
          {"parts": ["I ", "read", " it yesterday. I'll ", "read", " it tomorrow."], "hot": [1, 3],
           "note": "red or reed?", "at": at("B02", "same letters")},
          {"parts": ["", "Dr.", " Lee lives on Oak ", "Dr."], "hot": [1, 3],
           "note": "doctor or drive?", "at": at("B02", "same abbreviation")},
          {"parts": ["It costs ", "$5", " in ", "2026", "."], "hot": [1, 3],
           "note": "not words yet", "at": at("B02", "numbers aren't")}]}),
     "B03": ("TtvPipeline", {
        "spark": "Four steps from text to sound.",
        "steps": [{"name": "Clean up", "detail": "spell out numbers and abbreviations", "example": "$5 → five dollars"},
                  {"name": "Sound it out", "detail": "words become phonemes", "example": "fˈaɪv dˈɑːlɚz"},
                  {"name": "Plan the delivery", "detail": "length, pitch and loudness", "example": "bars"},
                  {"name": "Build the wave", "detail": "a neural network outputs audio", "example": "wave"}],
        "stepAt": [at("B03", "Clean up"), at("B03", "Sound it out"), at("B03", "Plan the delivery"), at("B03", "build the wave")],
        "envelope": S[3]["voices"][BELLA]["envelope"]}),
     "B04": ("TtvWave", {
        "envelope": S[0]["voices"][BELLA]["envelope"],
        "samples": S[0]["voices"][BELLA]["raw_first12"],
        "sampleRate": S[0]["voices"][BELLA]["sample_rate"],
        "styleSize": DEMO["style_numbers_per_voice"],
        "bellaStyle": DEMO["bella_style_first8"], "otherStyle": DEMO["michael_style_first8"],
        "otherEnvelope": S[0]["voices"][OTHER]["envelope"],
        "bellaLabel": "Bella", "otherLabel": "Michael",
        "waveAt": at("B04", "Sound is"), "zoomAt": at("B04", "list of numbers"), "rateAt": at("B04", "uses"),
        "netAt": at("B04", "neural network"), "styleAt": at("B04", "voice itself"), "swapAt": at("B04", "Swap that list"),
        "footnote": "Real samples and style numbers from Kokoro (demo/tts_demo.py); first few of each shown.",
        "footnoteShort": "Real numbers from Kokoro."}),
     "B05": ("TtvDemo", {
        "spark": "Real output, real mistakes.",
        "rows": [
          {"text": "I read it yesterday.", "hot": "read", "phonemes": S[0]["phonemes"], "bad": "ɹˈiːd",
           "said": "said “reed”", "at": at("B05", "For I read")},
          {"text": "Dr. Lee lives on Oak Dr.", "hot": "Oak Dr.", "phonemes": S[2]["phonemes"], "bad": "ˈoʊk dˈɑːktɚ", "badShort": "dˈɑːktɚ",
           "said": "said “Oak Doctor”", "at": at("B05", "Oak Drive")},
          {"text": "It costs $5 in 2026.", "hot": "$5", "phonemes": S[3]["phonemes"], "bad": "dˈɑːlɚ fˈaɪv",
           "said": "said “dollar five”", "at": at("B05", "and 5 became")}],
        "bellaEnvelope": S[0]["voices"][BELLA]["envelope"], "otherEnvelope": S[0]["voices"][OTHER]["envelope"],
        "bellaLabel": "Bella", "otherLabel": "Michael",
        "chip": "different voice, same mistakes", "voicesAt": at("B05", "different voice"),
        "footnote": "Kokoro-82M via kokoro-onnx 0.6.1 · espeak-ng phonemes · demo/tts_demo.py",
        "footnoteShort": "Real Kokoro output."}),
     "B06": ("RagWhenToUse", {
        "useHeader": "Use it for", "skipHeader": "Be careful with",
        "useHeaderAt": at("B06", "when is it useful"), "skipHeaderAt": at("B06", "Be careful"),
        "useItems": [{"text": "reading text aloud", "at": at("B06", "Reading text")},
                     {"text": "drafting a narration", "at": at("B06", "drafting")},
                     {"text": "hearing how a word sounds", "at": at("B06", "hearing how")}],
        "skipItems": [{"text": "names and unusual words", "at": at("B06", "names and unusual")},
                      {"text": "moments where tone matters", "at": at("B06", "tone matters")}],
        "warning": "Sounds human ≠ is right. Say it's AI.", "warningAt": at("B06", "always say")}),
     "B07": ("ClaudeVerdictArtifact", {
        "artifactTitle": SHORT_TITLE, "artifactHeading": "Three things to keep",
        "artifactLines": ["1. It works out sounds; it doesn't read the way you do.",
                          "2. A voice is just a set of numbers.",
                          "3. Sounding human isn't the same as being right."],
        "lineAt": [at("B07", "It works out"), at("B07", "A voice is"), at("B07", "sounding human")],
        "lectureLayout": True,
        "lecturePageFrames": [0, round(at("B07", "sounding human") * (timings.get("B07", 11) + 0.4) * 30)]}),
     "B08": ("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "YOUR TURN · TEXT TO VOICE", "segment": SHORT_TITLE, "command": YOUR_TURN,
        "runningText": "paste this into Claude…", "output": [], "folderLabel": HANDLE,
        "modelLabel": "Claude", "effortLabel": "AI narration: Bella", "largeText": True}),
     "B09": ("HaiTitleOutro", {"title": SHORT_TITLE, "handle": HANDLE}),
    }


ACTS = {"B00": "ASK", "B01": "BLUF", "B02": "PROBLEM", "B03": "FRAMEWORK", "B04": "MECHANISM",
        "B05": "WORKED EXAMPLE", "B06": "WHEN NOT TO", "B07": "VERDICT", "B08": "YOUR TURN", "B09": "OUTRO"}
EST = {"B00": 14, "B01": 11, "B02": 18, "B03": 20, "B04": 22, "B05": 22, "B06": 26, "B07": 11, "B08": 22, "B09": 5}

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
  "title": TITLE, "slug": "text-to-voice", "topic": "Irreducibly Human", "brand": "claude-hai",
  "skill": "ai-explainer", "audience": "students new to AI", "register": "Plain",
  "engine": "kokoro", "voice_kokoro": VOICE, "palette": "claude", "channel": HANDLE,
  "greeting": "Hi, Tanishaa", "fellow": "Tanishaa",
  "fellow_intro": "Hi, I am Tanishaa and this video is about how a computer turns text into a voice (required fellow opening line, B00).",
  "ai_disclosure": "Narration is Kokoro af_bella, an AI voice, disclosed aloud in B00 and on the composer chip.",
  "decisions": [
   "Script v2 approved by Tanishaa in chat on 2026-11-08 (\"Approved, build it\").",
   "Same look as What Is RAG and Learning Brutalist: Claude cream palette, HAI corner mark, HaiTitleOutro.",
   "B04/B05 use real Kokoro output (demo/tts_demo.py). The engine mispronounced the tricky lines, so B05 shows the mistakes, the fallback planned in the script.",
   "B00 says 'a script Claude drafted and I approved' (matches Learning Brutalist's corrected disclosure)."],
 },
 "beats": beats,
}
SHEET.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
print(f"wrote {SHEET} — {len(beats)} beats, {sum(len(words(t)) for t in N.values())} words")
