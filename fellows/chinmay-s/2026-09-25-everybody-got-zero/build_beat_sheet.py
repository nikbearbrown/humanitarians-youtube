#!/usr/bin/env python3
"""Author beat_sheet.json for hai-everybody-got-zero — the kid-friendly cut.

Same subject as hai-your-eval-is-lying (a prompt-engineering notebook whose
scorer reports 0.0 for everything), retold so a child can follow it: two
characters, concrete props, no unexplained jargon.

The technical content is NOT softened — every number is still recomputed by
running the notebook's own scoring functions, copied verbatim below.
No individual is named anywhere in the output.
"""
import json
import re
import unicodedata
from pathlib import Path

OUT = Path(__file__).resolve().parent / "beat_sheet.json"
WPS = 2.60

# ── the notebook's scoring functions, copied verbatim ─────────────────────
def normalize_text(text):
    if text is None:
        return ""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s\.\-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def f1_tokens(pred, gold):
    p, g = normalize_text(pred).split(), normalize_text(gold).split()
    if not p or not g:
        return 0.0
    common = set(p) & set(g)
    num = sum(min(p.count(t), g.count(t)) for t in common)
    if num == 0:
        return 0.0
    precision, recall = num / len(p), num / len(g)
    return 2 * precision * recall / (precision + recall)


def exact_match(pred, gold):
    return float(normalize_text(pred) == normalize_text(gold))


# a mended normaliser: fold accents, drop trailing punctuation
def normalize_fixed(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = t.lower().strip()
    t = re.sub(r"[^a-z0-9\s\-]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


PAIRS = [("Paris", "Paris"), ("Tokyo", "Tokyo"), ("New Delhi", "New Delhi"),
         ("Ottawa.", "Ottawa"), ("Brasilia", "Brasília")]

EM_BROKEN = sum(exact_match(p, g) for p, g in PAIRS) / len(PAIRS)
EM_FIXED = sum(float(normalize_fixed(p) == normalize_fixed(g)) for p, g in PAIRS) / len(PAIRS)
F1_DELHI = f1_tokens("Delhi", "New Delhi")
F1_VERBOSE = f1_tokens("The capital of France is Paris.", "Paris")
NORM_ACCENT = normalize_text("Brasília")

# ── guards: the narration speaks these ────────────────────────────────────
assert abs(EM_BROKEN - 0.60) < 1e-9, EM_BROKEN
assert abs(EM_FIXED - 1.00) < 1e-9, EM_FIXED
assert abs(F1_DELHI - 2 / 3) < 0.01, F1_DELHI
assert F1_VERBOSE == 0.0, F1_VERBOSE
assert NORM_ACCENT == "bras lia", NORM_ACCENT
print(f"[repro] broken marker EM={EM_BROKEN:.2f}  mended EM={EM_FIXED:.2f}")
print(f"[repro] 'Delhi' vs 'New Delhi' F1={F1_DELHI:.2f}")
print(f"[repro] verbose-but-correct answer F1={F1_VERBOSE:.2f}")
print(f"[repro] normalize('Brasilia' with accent) -> {NORM_ACCENT!r}")

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
    "A robot sat a test with ten questions, and got every single one wrong. Zero out of ten. "
    "But here is the strange part — the robot was never switched on. This is Humanitarians AI. "
    "Today we find out who actually failed that test.",
    "ClaudeComposerAsk",
    {"greeting": "Who failed the test?", "topic": "A STORY ABOUT MARKING",
     "segment": "The Test Where Everybody Got Zero",
     "command": "A robot answered ten questions and scored zero on all of them. Before I blame the robot, check the test itself — the marking rules, the tidying step, and whether the robot was ever actually asked anything.",
     "runningText": "checking the test…",
     "folderLabel": "@HumanitariansAI",
     "output": ["the marking rule is stricter than it looks",
                "the tidying machine eats letters",
                "and the robot was fast asleep"]},
    "type-on")

add("B01", "MEET",
    "First, meet the robot. You ask it a question, and it gives you an answer. "
    "What is the capital of France? Paris. What is three plus four? Seven. So far, easy.",
    "KidRobotTest", {}, "stagger")

stmt("B02", "MARKER",
     "But somebody has to decide whether each answer counts as right. That is the marker's job. "
     "And this marker follows one very strict rule.",
     "THE MARKER", "Every test needs someone to say right or wrong.",
     "and this one has a rule it never bends")

add("B03", "RULE",
    "The rule is this: your answer has to match the correct word exactly. Say Paris, and you get a tick. "
    "Say, the capital of France is Paris, and you get a cross. Same city. Different mark.",
    "KidStampRule", {}, "stagger")

add("B04", "GUM",
    "And here is why. When the marker compares two answers, it chops them into words. "
    "But the full stop stays stuck to the last word, like chewing gum. "
    "So paris-with-a-dot and paris look like two completely different words. The answer was perfect. The score was zero.",
    "KidGumDot", {}, "illustrate")

stmt("B05", "NAMING",
     "Grown-ups call that strict rule exact match. It only says yes when every single letter lines up.",
     "WHAT IT IS CALLED", "Exact match: every letter, or nothing.",
     "one small dot is enough to fail")

add("B06", "PARTIAL",
    "There is a kinder way to mark. Instead of all or nothing, count how many words match. "
    "Answer Delhi when the right answer is New Delhi, and you got one word out of two. "
    "That earns about two thirds of a mark, instead of nothing at all.",
    "EvalTokenOverlap", {}, "stagger")

add("B07", "MONSTER",
    "Now the strangest problem of the lot. Before anything is marked, every answer goes through a cleaning machine. "
    "It is meant to tidy the words up. But it only keeps the letters a to z. "
    "Feed it Brasília, the capital of Brazil, and it eats the letter with the accent. What comes out is bras, space, lia.",
    "KidLetterMonster", {}, "stagger")

stmt("B08", "CONSEQUENCE",
     "The machine snapped the city in half. And it does this to the correct answer too. "
     "So no spelling of Brasília can ever match — not the fancy one, not the plain one, not even the right one.",
     "NOBODY CAN WIN", "It breaks the answer key as well.",
     "a question that is impossible to get right")

add("B09", "SLEEPY",
    "And then the big one. Look at what the robot actually said. Every answer, all ten of them, "
    "was the same two words: mock output. The robot was never switched on.",
    "KidSleepyRobot", {}, "illustrate")

stmt("B10", "WHY",
     "The test needed a special key to wake the robot up, and there was no key. "
     "So instead of stopping and saying so, the programme quietly pretended, and carried on as if nothing was wrong.",
     "WHY IT HAPPENED", "It did not crash. It pretended.",
     "a silent failure is worse than a loud one")

add("B11", "PARADE",
    "Ten questions. Ten identical answers. Ten zeros. "
    "And at the end, the computer drew a tidy chart of the results — four bars, all flat at nothing.",
    "KidZeroParade", {}, "stagger")

stmt("B12", "DANGER",
     "That chart is the dangerous bit. It has a title. It has labels. It has neat straight edges. "
     "It looks exactly like a finished piece of work. It simply does not mean anything at all.",
     "THE DANGEROUS PART", "It looks finished. That is the problem.",
     "a chart of nothing still looks like a chart")

stmt("B13", "LESSON",
     "So here is the big idea, and it is worth keeping. When every single answer comes back wrong, "
     "do not start by blaming whoever was answering. Check the test.",
     "THE BIG IDEA", "When everyone fails, check the test.",
     "zero out of ten is a clue, not a result")

add("B14", "CHECK",
    "You can check a marker the same way you check anything else. Hand it an answer you already know is right, "
    "and watch what it says. Paris, when the answer is Paris — fine. Paris with a full stop — wrong. "
    "Brasilia — wrong. Two out of three. The marker is broken.",
    "KidTestTheTeacher", {}, "stagger")

stmt("B15", "CHEAP",
     "That takes about a minute. One minute, and you would have caught every single problem in this story "
     "before anybody ever looked at a chart.",
     "IT IS CHEAP", "One minute of checking. Three bugs caught.",
     "the test for the test is the shortest code you will write")

add("B16", "FIXED",
    "So mend the marker. Teach it to ignore full stops, and to understand letters with accents. "
    "Then mark the very same answers again. Sixty percent becomes one hundred percent.",
    "KidFixedScores",
    {"before": round(EM_BROKEN, 2), "after": round(EM_FIXED, 2)},
    "stagger")

stmt("B17", "MEANING",
     "Nothing about the answers changed. Not one letter. Only the marking changed. "
     "And that is the whole point of the story.",
     "WHAT CHANGED", "The answers never moved. The marking did.",
     "the score was never really about the robot")

stmt("B18", "CLOSE",
     "A score tells you about two things at once: the thing being tested, and the thing doing the testing. "
     "If you only ever check one of them, you are reading half the answer.",
     "THE LAST THOUGHT", "Every score is really two scores.",
     "one for the student, one for the test")

add("B19", "VERDICT",
    "So here is what we found. Three separate problems, and not one of them was the robot's fault.",
    "ClaudeVerdictArtifact",
    {"artifactTitle": "The test where everybody got zero",
     "artifactHeading": "What we found",
     "artifactLines": [
         "The full stop: a correct answer ending in a dot scores nothing, because the dot stays stuck to the word.",
         "The cleaning machine: it keeps only a to z, so Brasilia with an accent becomes 'bras lia' — and the answer key breaks too.",
         "The sleeping robot: with no key to wake it, every answer was the words 'mock output', and the test carried on anyway.",
         "The chart still drew itself: four flat bars, a title, and no meaning.",
         "The fix took one minute: hand the marker an answer you know is right, and see if it agrees."]},
    "stagger")

add("B20", "HANDOFF",
    "Your turn. Next time something you built gives you a score, try this first. "
    "Feed it one answer you are certain is correct, and check that it says yes. "
    "If it says no, you have not found a bad result. You have found a bad ruler.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "YOUR TURN", "segment": "Check the ruler first",
     "command": "Here is my scoring function. Write me three tiny tests using answers I already know are right, and tell me honestly whether my scorer agrees with all of them.",
     "runningText": "checking your ruler…",
     "folderLabel": "@HumanitariansAI",
     "output": ["a scorer is code, and code has bugs",
                "test it before you trust a single number"]},
    "type-on")

add("B21", "OUTRO",
    "The test where everybody got zero. If you like stories where the machine is innocent, subscribe. Humanitarians AI.",
    "ClaudeTitleOutro",
    {"title": "The Test Where Everybody Got Zero", "handle": "@HumanitariansAI"},
    "fade")

sheet = {
    "metadata": {
        "title": "The Test Where Everybody Got Zero",
        "slug": "hai-everybody-got-zero",
        "topic": "A STORY ABOUT MARKING",
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
        "note": ("KID-FRIENDLY cut of the eval-harness teardown. Same three findings as "
                 "hai-your-eval-is-lying, retold with two cartoon characters (the Grader and Robo) "
                 "and concrete props: chewing gum for the full stop, a letter-eating machine for the "
                 "unicode strip, a sleeping robot for mock mode. Narration uses plain words and names "
                 "the real term once. All figures still recomputed from the notebook's own scoring "
                 "functions. NO INDIVIDUAL IS NAMED. Bella (af_bella). Never publishes."),
        "tags": ["explain like I'm ten", "evaluation", "testing", "exact match",
                 "unicode", "silent failure", "kids", "Humanitarians AI"],
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
cartoon = sum(1 for b in B if b["shot"]["remotion"]["pattern"].startswith("Kid"))
print(f"cartoon scenes: {cartoon} of {len(B)} beats")
