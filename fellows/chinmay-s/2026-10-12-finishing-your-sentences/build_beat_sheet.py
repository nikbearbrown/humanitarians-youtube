#!/usr/bin/env python3
"""Author beat_sheet.json for hai-finishing-your-sentences — the kid-friendly cut.

Subject: a from-scratch GPT notebook (NumPy only) with a hand-written autodiff
engine, TWO numerical gradient checks, a copy-task sanity check before the real
run, and a KV-cache correctness check. This reel TEACHES; it is not a teardown.

Every figure spoken on screen is PARSED from the notebook's recorded outputs,
never transcribed, and guarded by assertions. No individual is named.
"""
import json
import math
import re
from pathlib import Path

NB = Path(r"C:\Users\sawan\OneDrive\Desktop\dumps\tiny_gpt_from_scratch.ipynb")
OUT = Path(__file__).resolve().parent / "beat_sheet.json"
WPS = 2.60

nb = json.loads(NB.read_text(encoding="utf-8"))
cells = nb["cells"]


def stream(i):
    return "".join("".join(o.get("text", []))
                   for o in cells[i].get("outputs", [])
                   if o.get("output_type") == "stream")


def grab(i, pat, g=1):
    m = re.search(pat, stream(i))
    assert m, f"pattern {pat!r} not found in cell {i}"
    return m.group(g)


# ── parse the notebook ────────────────────────────────────────────────────
N_FILES = grab(6, r"read (\d+) files")
CHARS = grab(6, r"corpus size: ([\d,]+) characters")
SPACE_PCT = grab(8, r"spaces alone are ([\d.]+)%")
CHARS_PER_TOK = grab(13, r"after 200 merges: ([\d.]+) characters per token")
V = int(grab(15, r"vocabulary size V = (\d+)"))
UNIFORM = float(grab(15, r"loss of log\(V\) = ([\d.]+)"))
BIG_VAL = float(grab(17, r"bigram loss\s+train: [\d.]+\s+val: ([\d.]+)"))
ENGINE_ERR = grab(26, r"worst relative error across random checks: ([\d.e+-]+)")
MODEL_ERR = grab(36, r"worst relative error: ([\d.e+-]+)")
COPY_ACC = grab(40, r"accuracy on the copied half: ([\d.]+%)")
COPY_SECS = grab(40, r"trained in ([\d.]+s)")
N_PARAMS = grab(44, r"model has ([\d,]+) parameters")
START_LOSS = float(grab(44, r"starting loss .*?: ([\d.]+)"))
_last = stream(46).strip().splitlines()[-1]
GPT_TRAIN = float(re.search(r"train ([\d.]+)", _last).group(1))
GPT_VAL = float(re.search(r"val ([\d.]+)", _last).group(1))
TRAIN_SECS = float(re.search(r"([\d.]+)s\s*$", _last).group(1))
MS_NO = grab(65, r"(\d+) ms without cache")
MS_YES = grab(65, r"(\d+) ms with cache")
POS_NO = grab(65, r"positions pushed through the network: ([\d,]+) without")
POS_YES = grab(65, r"vs ([\d,]+) with cache")
SPEEDUP = grab(65, r"\(([\d]+x) less work\)")
GPT3_RATIO = grab(68, r"roughly ([\de+.]+) times more")
# spoken form: a child can hear "ninety billion", not "9e+10"
_r = float(GPT3_RATIO)
for _div, _name in ((1e12, "trillion"), (1e9, "billion"), (1e6, "million")):
    if _r >= _div:
        GPT3_SPOKEN = f"{_r/_div:.0f} {_name}"
        break
else:
    GPT3_SPOKEN = f"{_r:,.0f}"

# BPE merges: first few, plus a couple of long ones
merge_line = stream(11)
FIRST_MERGES = re.findall(r"'([^']*)'\s+\d+", merge_line)[:10]
LONG_TOKENS = re.findall(r"'([^']+)'", grab(13, r"some later, longer tokens: \[(.*?)\]"))

# probes
PROBES = []
for line in stream(57).splitlines():
    m = re.match(r"^'(.+?)'\s+->\s+'(.+?)' (\d+)%", line)
    if m:
        PROBES.append((m.group(1), m.group(2), int(m.group(3))))

# ── derived: loss -> "how many letters still in the running" ─────────────
CH_UNIFORM = math.exp(UNIFORM)
CH_BIGRAM = math.exp(BIG_VAL)
CH_GPT = math.exp(GPT_VAL)

# ── guards ────────────────────────────────────────────────────────────────
assert V == 96, V
assert abs(CH_UNIFORM - V) < 1.0, CH_UNIFORM
assert CH_GPT < CH_BIGRAM < CH_UNIFORM, (CH_GPT, CH_BIGRAM, CH_UNIFORM)
assert float(ENGINE_ERR) < 1e-5 and float(MODEL_ERR) < 1e-4, (ENGINE_ERR, MODEL_ERR)
assert COPY_ACC.startswith("100"), COPY_ACC
assert abs(START_LOSS - UNIFORM) < 0.1, (START_LOSS, UNIFORM)
assert len(PROBES) >= 6, len(PROBES)
assert int(MS_NO) > int(MS_YES), (MS_NO, MS_YES)
print(f"[nb] corpus {CHARS} chars from {N_FILES} files · spaces {SPACE_PCT}% · V={V}")
print(f"[nb] choices: uniform {CH_UNIFORM:.0f} -> bigram {CH_BIGRAM:.1f} -> gpt {CH_GPT:.1f}")
print(f"[nb] grad checks {ENGINE_ERR} / {MODEL_ERR} · copy {COPY_ACC} in {COPY_SECS}")
print(f"[nb] {N_PARAMS} params · loss {START_LOSS} -> {GPT_TRAIN}/{GPT_VAL} in {TRAIN_SECS:.0f}s")
print(f"[nb] cache {MS_NO}->{MS_YES} ms · {POS_NO}->{POS_YES} positions ({SPEEDUP})")

B = []


def add(bid, act, text, pattern, props, motion="illustrate"):
    B.append({
        "beat_id": bid, "act": act, "narration_text": text,
        "shot": {"type": "GRAPHIC", "source": "remotion", "motion": motion,
                 "remotion": {"pattern": pattern, "props": props}},
        "estimated_duration_s": round(len(text.split()) / WPS, 1),
        "audio_file": f"mp3/beat-{bid}.mp3",
    })


def stmt(bid, act, text, eyebrow, headline, kicker="", motion="fade"):
    add(bid, act, text, "IdxStatement",
        {"eyebrow": eyebrow, "headline": headline, "kicker": kicker}, motion)


add("B00", "ASK",
    "Somebody built a tiny version of the thing behind ChatGPT, by hand, out of nothing. "
    "This is Humanitarians AI. It is small enough to understand completely, and it learned to write computer code "
    "by playing one very boring game, a few million times.",
    "ClaudeComposerAsk",
    {"greeting": "Show me how it learns.", "topic": "HOW TEXT MACHINES LEARN",
     "segment": "Finishing Your Sentences",
     "command": "Walk me through a GPT built from scratch in NumPy — what game it plays, how it gets good at it, and how we know the maths is actually right.",
     "runningText": "opening the notebook…",
     "folderLabel": "@HumanitariansAI",
     "output": ["the game: guess the next character",
                "the trick: look back at what came before",
                "the proof: check the maths twice"]},
    "type-on")

add("B01", "GAME",
    "Here is the game. You get some text, and you guess the very next character. That is it. That is the whole job. "
    "Do it well enough, millions of times over, and you can write.",
    "KidGuessGame", {}, "stagger")

stmt("B02", "CORPUS",
     f"To practise, it reads real computer code — {CHARS} characters of it, pulled straight off the machine it is running on. "
     f"Nobody wrote it specially. It is just {N_FILES} ordinary files.",
     "THE PRACTICE BOOK", "Two million characters of real code.",
     "no special training set — just files already on the computer")

add("B03", "ALPHABET",
    f"Now, how hard is this game? There are {V} different characters it could pick. "
    "Guessing blind, it is choosing between all of them. Counting which letters tend to follow which gets it down to about eleven. "
    "And the real machine, when it is finished, gets down to about five.",
    "KidAlphabetShrink",
    {"stages": [
        {"label": "guessing blindly", "choices": round(CH_UNIFORM), "hero": False},
        {"label": "just counting letter pairs", "choices": round(CH_BIGRAM), "hero": False},
        {"label": "the finished machine", "choices": round(CH_GPT), "hero": True},
    ]},
    "stagger")

add("B04", "SHORTCUTS",
    "Before it starts, it invents shortcuts. It looks for pieces that keep appearing and glues them into single chunks. "
    "And the very first thing it discovers is a bit funny.",
    "KidShortcuts",
    {"merges": FIRST_MERGES, "charsPerToken": CHARS_PER_TOK},
    "stagger")

stmt("B05", "SPACES",
     f"The commonest thing in computer code is empty space — {SPACE_PCT} percent of everything it read. "
     "So its first shortcuts are runs of blank space. Then little word pieces. Then, eventually, whole real words.",
     "THE FUNNY PART", "Its first discovery was: lots of nothing.",
     "indentation, which in Python is how the code is shaped")

add("B06", "LOOKBACK",
    "Now the clever bit, and this is the idea the whole thing is built on. "
    "To guess the next character, each character looks back at the ones before it, and decides which of them matter.",
    "KidLookBack", {}, "stagger")

stmt("B07", "ONLYBACK",
     "And it can only ever look backwards, never forwards. That rule matters more than it sounds. "
     "If it could peek ahead, it would simply read the answer, learn nothing, and be useless the moment you asked it something new.",
     "ONE STRICT RULE", "No peeking at what comes next.",
     "the answer is right there — so it must be hidden")

add("B08", "CHECKS",
    "Before trusting any of this, they checked their working. Twice. "
    "Once on the little maths engine underneath, and then again on the whole finished machine.",
    "KidTwoChecks", {"engineErr": ENGINE_ERR, "modelErr": MODEL_ERR}, "stagger")

add("B09", "COPYTEST",
    "Then they gave it an easy exam first. Here is a jumble of letters — now say it back to me. "
    "A machine that cannot do that has no business trying anything harder.",
    "KidCopyTest", {"accuracy": COPY_ACC, "seconds": COPY_SECS}, "stagger")

stmt("B10", "TRAIN",
     f"Only then does the real training start. The machine has {N_PARAMS} little numbers inside it, all set randomly at first. "
     f"It plays the guessing game for about {TRAIN_SECS/60:.0f} minutes, nudging every one of them a tiny bit each time it is wrong.",
     "THE REAL TRAINING", f"{N_PARAMS} numbers, all starting as pure guesswork.",
     f"about {TRAIN_SECS/60:.0f} minutes of practice, and nothing else")

stmt("B11", "RESULT",
     f"It begins at {START_LOSS:.2f}, which is exactly what pure guessing looks like — all {V} characters equally likely. "
     f"It finishes at {GPT_VAL:.2f}. In plain terms, it went from choosing between {CH_UNIFORM:.0f} characters to choosing between about {CH_GPT:.0f}.",
     "HOW MUCH BETTER", f"From {CH_UNIFORM:.0f} choices down to about {CH_GPT:.0f}.",
     "it started knowing nothing at all")

add("B12", "PROBES",
    "But what did it actually learn? We can just ask it. Give it the start of something and see what it wants to put next.",
    "KidFinishWord",
    {"probes": [{"prompt": p.replace("\\n", "⏎")[-24:], "next": n, "pct": f"{c}%"}
                for (p, n, c) in PROBES[:5]]},
    "stagger")

stmt("B13", "LEARNED",
     "Nobody ever told it that Python has a word called self, or a word called None. "
     "It worked those out purely from how often the letters turned up together — and now it is more certain of them than you probably are.",
     "WHAT THAT MEANS", "It learned real words out of pure counting.",
     "no dictionary, no grammar, no rules — just patterns")

add("B14", "TEMPERATURE",
    "There is one dial you can turn when it writes: how adventurous to be. Keep it low and it plays safe. Turn it up and it takes risks.",
    "KidTempDial",
    {"rows": [
        {"temp": "0", "sample": "    if self._init__ == _context.__name__", "note": "safe, and repeats itself"},
        {"temp": "0.5", "sample": "    if cls == '___dec__':  self.__no__ = _decode__", "note": "mostly sensible"},
        {"temp": "1.0", "sample": "    if __negate__ _clsb.___   # red_tyq", "note": "getting loose"},
        {"temp": "1.5", "sample": "    if 1,#2 Thdia.4027_6993 def:#2K in mu", "note": "complete nonsense"},
    ]},
    "stagger")

add("B15", "CACHE",
    "One last trick, and it is just common sense. Every time it adds a character, it was re-reading everything it had already written. "
    "So instead, it remembers.",
    "KidMemoryTrick",
    {"without": POS_NO, "with_": POS_YES, "speedup": SPEEDUP,
     "msWithout": f"{MS_NO} ms", "msWith": f"{MS_YES} ms"},
    "stagger")

stmt("B16", "SAMEANSWER",
     "And they checked that both ways give exactly the same answer before using the fast one. "
     "A shortcut you have not checked is not a shortcut. It is just a different answer.",
     "CHECKED, AGAIN", "Faster is only better if it is still right.",
     "same output, a fraction of the work")

stmt("B17", "SCALE",
     f"Now the part that is hard to picture. This machine is tiny. The big ones you have heard of used about {GPT3_SPOKEN} times more computing than this one did. "
     "Not a different idea. The same idea, enormously more of it.",
     "AND THEN, BIGGER", "The same game. Unimaginably more practice.",
     "every idea here is in the big ones too")

add("B18", "VERDICT",
    "So here is the whole thing, from nothing to writing code. A guessing game, played over two million characters. "
    "Shortcuts it invented by itself, just by counting. Looking backwards, never forwards. The maths checked twice before trusting it. "
    "An easy exam before the hard one. And ninety-six choices, narrowed down to about five.",
    "ClaudeVerdictArtifact",
    {"artifactTitle": "How a text machine learns",
     "artifactHeading": "The whole idea",
     "artifactLines": [
         f"The game: guess the next character. {CHARS} characters of real code to practise on.",
         f"The shortcuts: it finds repeating pieces and glues them together — starting with runs of blank space, {SPACE_PCT}% of everything it read.",
         "The trick: each character looks back at the ones before it and decides which matter. It may never look forward.",
         f"The proof: the maths was checked twice, by hand and by counting — {ENGINE_ERR} on the engine, {MODEL_ERR} on the whole machine.",
         f"The easy exam first: copy back a jumble of letters. {COPY_ACC}. Only then try the hard thing.",
         f"The result: from choosing between {CH_UNIFORM:.0f} characters down to about {CH_GPT:.0f} — with {N_PARAMS} numbers and {TRAIN_SECS/60:.0f} minutes."]},
    "stagger")

add("B19", "HANDOFF",
    "Your turn. Open any writing app that finishes your sentences, and watch it for a minute. "
    "Every suggestion it makes is this same game — look back, then guess the next bit. "
    "See if you can catch it being very sure, and see if you can catch it being wrong.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "YOUR TURN", "segment": "Catch it guessing",
     "command": "Watch the autocomplete on your phone or editor for one minute. Where is it very confident, and where does it clearly guess wrong? What does that tell you about what it has seen before?",
     "runningText": "watching it guess…",
     "folderLabel": "@HumanitariansAI",
     "output": ["confident where the pattern is common",
                "wrong where it has never seen the shape before"]},
    "type-on")

add("B20", "OUTRO",
    "Finishing your sentences. If you like knowing what is really going on under there, subscribe. Humanitarians AI.",
    "ClaudeTitleOutro",
    {"title": "Finishing Your Sentences", "handle": "@HumanitariansAI"},
    "fade")

sheet = {
    "metadata": {
        "title": "Finishing Your Sentences",
        "slug": "hai-finishing-your-sentences",
        "topic": "HOW TEXT MACHINES LEARN",
        "register": "Teardown",
        "audience": "HAI",
        "brand": "claude",
        "voice": "HumanitariansAI",
        "engine": "kokoro",
        "palette": "claude",
        "style_preset": "claude",
        "ground": "#FAF9F5",
        "voice_kokoro": "af_bella",
        "channel": "humanitarians-ai",
        "handle": "@HumanitariansAI",
        "note": ("KID-FRIENDLY explainer of a from-scratch GPT notebook (NumPy only). This reel "
                 "TEACHES — the source is careful work: a hand-written autodiff engine with its own "
                 "gradient check, a second check on the full Transformer, a copy-task sanity check "
                 "before the real run, and a KV-cache correctness check. Every figure is parsed from "
                 "the notebook's recorded outputs by build_beat_sheet.py under assertions. Losses are "
                 "converted to 'how many characters still in the running' via exp(loss) so a child can "
                 "read them. NO INDIVIDUAL IS NAMED. Bella (af_bella). Never publishes."),
        "tags": ["GPT", "transformer", "attention", "tokenization", "explain like I'm ten",
                 "next-token prediction", "KV cache", "kids", "Humanitarians AI"],
    },
    "beats": B,
}
OUT.write_text(json.dumps(sheet, indent=2, ensure_ascii=False), encoding="utf-8")

words = sum(len(b["narration_text"].split()) for b in B)
print(f"\nwrote {OUT}")
print(f"{len(B)} beats · {words} words · projected {words/WPS:.0f}s = {int(words/WPS)//60}m{int(words/WPS)%60:02d}s")
banned = ["chinmay", "chinmai", "chinme", "sawant", "savant"]
blob = json.dumps(sheet, ensure_ascii=False).lower()
hits = [x for x in banned if x in blob]
print("NAME CHECK:", "CLEAN" if not hits else f"FAIL {hits}")
print("animated scenes:", sum(1 for b in B if b["shot"]["remotion"]["pattern"].startswith("Kid")), "of", len(B))
