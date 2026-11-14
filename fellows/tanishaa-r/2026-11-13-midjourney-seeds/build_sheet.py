"""build_sheet.py — writes beat_sheet.json for "Why the Same Prompt Gives Four Different
Images" (Midjourney seeds) from the approved SCRIPT.md v1 (approved by Tanishaa 2026-11-13).

Same method as how-gps-works: reveal times are fractions of the beat, taken from
MEASURED word starts (mp3/words.json, faster-whisper on Bella's audio) once the audio
exists; before that, from word position. Nothing on screen runs on its own clock.
B06 numbers and pictures come from demo/seed_output.json (demo/seed_demo.py, a toy, not Midjourney).

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
TITLE = "Why the Same Prompt Gives Four Different Images"
SHORT_TITLE = "Midjourney Seeds"

old = {b["beat_id"]: b for b in json.loads(SHEET.read_text())["beats"]} if SHEET.exists() else {}
timings = json.loads((HERE / "mp3/timings.json").read_text()) if (HERE / "mp3/timings.json").exists() else {}
MEASURED = json.loads((HERE / "mp3/words.json").read_text()) if (HERE / "mp3/words.json").exists() else {}
DEMO = json.loads((HERE / "demo/seed_output.json").read_text())
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
 "B00": "Hi, I am Tanishaa, and this video is about why the same Midjourney prompt gives you four different images. The voice you're hearing is Bella, an AI narrator reading a script Claude drafted and I approved.",
 "B01": "Type one prompt into Midjourney and you get four images, and none of them match. Type the exact same prompt again, and you get four more. So where does the difference come from?",
 "B02": "Every image starts as random noise, like static on an old TV. Midjourney's own guide describes it exactly that way. The model then cleans that noise up, step by step, into a picture that matches your prompt.",
 "B03": "Think of it like this. The prompt decides what the picture is about. The noise nudges where things land: the shapes and the layout. Different noise, different picture, even with the same words.",
 "B04": "That's why one prompt gives you four images. Each one starts from a different patch of noise. And if you don't choose, Midjourney picks new random noise every time.",
 "B05": "The seed is the number that picks which noise you start from. It can be any whole number up to about four billion. Add dash dash seed and a number to the end of your prompt, and you lock in the starting noise.",
 "B06": "I tested this with a tiny toy generator, not Midjourney itself, but it works the same way. With no seed, four random seeds gave four different landscapes. With seed twelve thirty-four, twice, the two pictures matched pixel for pixel. Then I kept the seed and changed one word, sunset to forest. The hills stayed put. Only the colours changed.",
 "B07": "In Midjourney, the same seed and the same prompt bring back almost the same image. Its own guide says about ninety-nine percent identical. To find an image's seed, open it, use the options button, and copy the seed.",
 "B08": "So what is a seed good for? It's a control in an experiment: keep the seed, change one word, and you see exactly what that word did. But a seed can't carry a style or a character across different prompts, and it isn't reliable in Turbo mode. For a consistent look across assets, Midjourney recommends style references, moodboards, and personalization instead.",
 "B09": "Three things to keep. Every image starts as random noise. The seed picks the noise, so the same seed brings back the same image. And for the same look across different prompts, use references, not seeds.",
 "B10": "Your turn. Ask Claude to plan a seed experiment with you: one prompt, no seed, then a fixed seed twice, then one word changed. Then run it yourself and see what stays and what moves.",
 "B11": "Why the same prompt gives four different images. At Humanitarians AI.",
}

YOUR_TURN = ("Act as my tutor. Help me plan a Midjourney seed test: one prompt with no seed, a fixed seed twice, "
             "then the same seed with one word changed. Tell me what to look for, then help me explain what I see.")
IMG = "midjourney-seeds/"


def shots():
    D = DEMO
    four = [IMG + f"four_{i}.png" for i in range(4)]
    return {
     "B00": ("ClaudeComposerAsk", {
        "greeting": "Hi, Tanishaa", "topic": "Irreducibly Human", "segment": SHORT_TITLE,
        "command": "Why does the same Midjourney prompt give me four different images?",
        "runningText": "thinking…",
        "output": ["Every image starts from random noise,", "and each of the four gets different noise.",
                   "A seed picks which noise you start from."],
        "folderLabel": HANDLE, "modelLabel": "Claude", "effortLabel": "AI narration: Bella", "largeText": True}),
     "B01": ("MjPuzzle", {
        "prompt": D["prompt"], "images": four, "more": [IMG + f"more_{i}.png" for i in range(4)],
        "promptAt": at("B01", "Type 1 prompt"), "imagesAt": at("B01", "you get four images"),
        "againAt": at("B01", "Type the exact"), "moreAt": at("B01", "you get four more"),
        "label": "same prompt · four different images", "labelAt": at("B01", "none of them match"),
        "questionAt": at("B01", "where does")}),
     "B02": ("MjNoise", {
        "noise": IMG + "noise_42.png", "noiseAt": at("B02", "random noise"),
        "label": "every image starts here: random noise", "labelAt": at("B02", "Every image"),
        "quote": "Midjourney: a seed is “the random noise you see on a TV screen”", "quoteAt": at("B02", "own guide"),
        "cleanAt": at("B02", "cleans that noise"), "picture": IMG + "four_0.png"}),
     "B03": ("MjSteps", {
        "noise": IMG + "noise_42.png", "picture": IMG + "four_0.png", "prompt": D["prompt"],
        "promptAt": at("B03", "The prompt decides"), "noiseAt": at("B03", "The noise nudges"),
        "shapesAt": at("B03", "the shapes"), "diffAt": at("B03", "Different noise"),
        "caption": "schematic: the real model takes many steps"}),
     "B04": ("MjFour", {
        "noises": [IMG + f"noise_four_{i}.png" for i in range(4)], "images": four, "fourAt": at("B04", "four images"),
        "eachAt": at("B04", "Each one"), "randomAt": at("B04", "if you don't"),
        "label": "4 images = 4 different starting noises", "randomLabel": "no seed chosen → new random noise every time"}),
     "B05": ("MjSeed", {
        "seed": 1234, "prompt": D["prompt"], "noise": IMG + "noise_42.png",
        "seedAt": at("B05", "The seed is"), "rangeAt": at("B05", "any whole"), "flagAt": at("B05", "Add dash"),
        "lockAt": at("B05", "lock in"), "range": "any whole number from 0 to 4,294,967,295"}),
     "B06": ("MjDemo", {
        "four": four, "a": IMG + "seed1234_a.png", "b": IMG + "seed1234_b.png", "forest": IMG + "seed1234_forest.png",
        "prompt": D["prompt"], "prompt2": D["prompt2"],
        "toyAt": at("B06", "toy generator"), "fourAt": at("B06", "With no seed"),
        "sameAt": at("B06", "With seed"), "matchAt": at("B06", "pixel for pixel"),
        "wordAt": at("B06", "changed one word"), "stayAt": at("B06", "hills stayed"),
        "identical": D["seed1234_twice_identical_pixels"],
        "toyLabel": "toy generator (demo/seed_demo.py), not Midjourney"}),
     "B07": ("MjInMidjourney", {
        "sameAt": at("B07", "the same seed"), "pctAt": at("B07", "Its own guide"), "findAt": at("B07", "To find"),
        "same": "same seed + same prompt → almost the same image", "pct": "Midjourney: “99% identical in V8”",
        "find": "find a seed: open the image → options → Copy → Seed",
        "stepAt": [at("B07", "open it"), at("B07", "options"), at("B07", "copy"), at("B07", "the seed")]}),
     "B08": ("RagWhenToUse", {
        "useHeader": "Use a seed to", "skipHeader": "Don't use a seed to",
        "useHeaderAt": at("B08", "So what"), "skipHeaderAt": at("B08", "But a seed"),
        "useItems": [{"text": "run a controlled experiment", "at": at("B08", "control in")},
                     {"text": "keep the seed, change one word", "at": at("B08", "Keep the seed")}],
        "skipItems": [{"text": "carry a style across prompts", "at": at("B08", "carry a style")},
                      {"text": "rely on it in Turbo mode", "at": at("B08", "isn't reliable")}],
        "warning": "Same look? Style references, moodboards, personalization.", "warningAt": at("B08", "style references")}),
     "B09": ("GpsTakeaway", {
        "artifactTitle": SHORT_TITLE, "artifactHeading": "Three things to keep",
        "artifactLines": ["1. Every image starts as random noise.",
                          "2. The seed picks the noise; same seed, same image.",
                          "3. Same look across prompts? Use references, not seeds."],
        "lineAt": [at("B09", "Every image"), at("B09", "The seed picks"), at("B09", "And for the same")]}),
     "B10": ("MjYourTurn", {
        "prompt": YOUR_TURN, "askAt": at("B10", "Ask Claude"),
        "steps": [{"text": "one prompt, no seed", "at": at("B10", "One prompt")},
                  {"text": "a fixed seed, twice", "at": at("B10", "then a fixed")},
                  {"text": "same seed, one word changed", "at": at("B10", "then one word")}],
        "runAt": at("B10", "Then run"), "runText": "Run it: what stays, what moves?"}),
     "B11": ("HaiTitleOutro", {"title": SHORT_TITLE, "handle": HANDLE}),
    }


ACTS = {"B00": "ASK", "B01": "BLUF", "B02": "MECHANISM", "B03": "MECHANISM", "B04": "MECHANISM", "B05": "FRAMEWORK",
        "B06": "WORKED EXAMPLE", "B07": "SURPRISE", "B08": "WHEN NOT TO", "B09": "VERDICT", "B10": "YOUR TURN", "B11": "OUTRO"}
EST = {"B00": 13, "B01": 12, "B02": 15, "B03": 15, "B04": 12, "B05": 16, "B06": 22, "B07": 15, "B08": 24,
       "B09": 11, "B10": 16, "B11": 4}

# The toy pictures (sky gradients, hills, sun) read as low-contrast "text blobs" to GATE T §8.3b, so
# these beats declare where their real text is and contrast is measured there (landscape layout).
_REASON = "Toy-generator pictures (demo/seed_demo.py) are image content, not typography; contrast is checked on the text areas."
QC = {
 "B01": {"contrast_reason": _REASON, "contrast_regions": [
    {"label": "prompt bar", "box": [0.08, 0.05, 0.5, 0.16]},
    {"label": "label + question", "box": [0.04, 0.65, 0.8, 0.86]}]},
 "B02": {"contrast_reason": _REASON, "contrast_regions": [
    {"label": "label, quote, step line", "box": [0.53, 0.14, 0.95, 0.6]}]},
 "B03": {"contrast_reason": _REASON, "contrast_regions": [
    {"label": "prompt / noise lines", "box": [0.04, 0.04, 0.7, 0.2]},
    {"label": "result + caption", "box": [0.04, 0.74, 0.7, 0.9]}]},
 "B04": {"contrast_reason": _REASON, "contrast_regions": [
    {"label": "labels", "box": [0.06, 0.78, 0.8, 0.95]}]},
 "B05": {"contrast_reason": _REASON, "contrast_regions": [
    {"label": "seed card", "box": [0.06, 0.1, 0.25, 0.34]},
    {"label": "range + prompt", "box": [0.06, 0.67, 0.7, 0.86]}]},
 "B06": {"contrast_reason": _REASON, "contrast_regions": [
    {"label": "toy label + column heads", "box": [0.04, 0.04, 0.97, 0.19]},
    {"label": "result notes", "box": [0.36, 0.67, 0.97, 0.8]}]},
}
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
    if bid in QC:
        b["qc"] = QC[bid]
    for k in ("audio_file", "actual_duration_s"):
        if k in o:
            b[k] = o[k]
    if bid in timings:
        b["actual_duration_s"] = timings[bid]
    beats.append(b)

sheet = {
 "metadata": {
  "title": TITLE, "slug": "midjourney-seeds", "topic": "Irreducibly Human", "brand": "claude-hai",
  "skill": "ai-explainer", "audience": "students new to the topic", "register": "Plain",
  "engine": "kokoro", "voice_kokoro": VOICE, "palette": "claude", "channel": HANDLE,
  "greeting": "Hi, Tanishaa", "fellow": "Tanishaa",
  "fellow_intro": "Hi, I am Tanishaa and this video is about why the same Midjourney prompt gives you four different images (required fellow opening line, B00).",
  "ai_disclosure": "Narration is Kokoro af_bella, an AI voice, disclosed aloud in B00 and on the composer chip.",
  "decisions": [
   "Topic from Tanishaa's team assignment (Midjourney), given 2026-11-13: why one prompt gives four images; seeds. Script v1 approved in chat 2026-11-13 (\"Approved, build it\").",
   "Correction chosen by Tanishaa: Midjourney's Seeds page says seeds are 'Not for Saving Styles', so the video says seed = same image, references = same look.",
   "No Midjourney screenshots (Tanishaa's choice). B06 is a real toy program (demo/seed_demo.py), labeled 'toy generator, not Midjourney' on screen.",
   "Sync rule: key points cued to measured words; the screen is never left empty while Bella talks."],
 },
 "beats": beats,
}
if (HERE / "beat_sheet.json").exists():
    prev = json.loads(SHEET.read_text())["metadata"]
    if "build" in prev:
        sheet["metadata"]["build"] = prev["build"]
SHEET.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
print(f"wrote {SHEET} — {len(beats)} beats, {sum(len(words(t)) for t in N.values())} words")
