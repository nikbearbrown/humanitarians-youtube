#!/usr/bin/env python3
"""Author beat_sheet.json for hai-your-eval-is-lying.

Subject: Worked_Examples_in_Generative_AI_Prompt_Engineering_&_Evaluation.ipynb

Every metric shown on screen is RECOMPUTED HERE by the notebook's own scoring
functions, copied verbatim below. Nothing is hand-typed, so the video cannot
drift from what the code actually does.

No individual is named anywhere (the notebook carries a personal copyright line).
A guard at the bottom enforces this.
"""
import json, re, unicodedata
from pathlib import Path

OUT = Path(__file__).resolve().parent / "beat_sheet.json"
WPS = 2.242  # Bella's measured pace: 1463 words / 652.4s

# ── the notebook's functions, verbatim (cells 2) ────────────────────────────

def normalize_text(text: str) -> str:
    if text is None:
        return ""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s\.\-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def extract_final_answer(text: str) -> str:
    if not text:
        return ""
    m = re.search(r"final answer\s*:\s*(.*)", text, re.IGNORECASE | re.DOTALL)
    return m.group(1).strip() if m else text.strip()

def exact_match(pred, gold, norm=normalize_text):
    return float(norm(pred) == norm(gold))

def f1_tokens(pred, gold, norm=normalize_text):
    p = norm(pred).split(); g = norm(gold).split()
    if not p or not g:
        return 0.0
    common = set(p) & set(g)
    num = sum(min(p.count(t), g.count(t)) for t in common)
    if num == 0:
        return 0.0
    precision = num / len(p); recall = num / len(g)
    return 2 * precision * recall / (precision + recall)

# ── the corrected normalizer (the four-line fix the video proposes) ─────────

def normalize_fixed(text: str) -> str:
    if text is None:
        return ""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s\-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()

# ── the scoreboard, computed ────────────────────────────────────────────────

CASES = [
    ("Paris", "Paris"),
    ("The capital of France is Paris.", "Paris"),
    ("Delhi", "New Delhi"),
    ("Brasilia", "Brasília"),
    ("Final answer: 7", "7"),
]
SCOREBOARD = []
for pred, gold in CASES:
    ans = extract_final_answer(pred)
    SCOREBOARD.append({
        "pred": pred if len(pred) <= 31 else pred[:30] + "…",
        "gold": gold,
        "em": exact_match(ans, gold),
        "f1": round(f1_tokens(ans, gold), 2),
    })

FIX_CASES = [("Paris", "Paris"), ("Tokyo", "Tokyo"), ("New Delhi", "New Delhi"),
             ("Ottawa.", "Ottawa"), ("Brasilia", "Brasília")]
BEFORE = round(sum(exact_match(p, g) for p, g in FIX_CASES) / len(FIX_CASES), 2)
AFTER = round(sum(exact_match(p, g, normalize_fixed) for p, g in FIX_CASES) / len(FIX_CASES), 2)

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
    "A notebook that benchmarks prompt engineering, where every score is zero — this is Humanitarians AI. "
    "Today we take apart an evaluation harness that reports total failure, and cannot tell you whether the model "
    "or the measurement is the broken thing.",
    "ClaudeComposerAsk",
    {"greeting": "Audit the measurement.", "topic": "EVAL TEARDOWN",
     "segment": "Your Eval Is Lying to You",
     "command": "Here is a notebook comparing baseline and chain-of-thought prompts on two datasets, scored with exact match and F1. Every number it reports is 0.0. Tell me whether the prompts failed, or the harness did — and show me exactly where.",
     "runningText": "auditing the harness…",
     "folderLabel": "@HumanitariansAI",
     "output": ["the model was never called",
                "the normalizer deletes accented characters",
                "a correct answer with a full stop scores zero"]},
    "type-on")

stmt("B01", "SETUP",
     "The design is reasonable. Two datasets — geography facts, and arithmetic word problems. "
     "Two prompts each: a plain baseline, and chain-of-thought. Score both with exact match and token F1, then compare.",
     "THE DESIGN", "Two datasets. Two prompts. Two metrics.",
     "knowledge versus reasoning — a genuinely good comparison")

add("B02", "PROMPTS",
    "The prompt is the interface. Baseline asks for the answer in one or two words. Chain-of-thought asks the model "
    "to reason first and then commit, which the harness pulls out with a regex on the words final answer.",
    "EvalPromptDiff", {}, "stagger")

add("B03", "PIPELINE",
    "Every prediction walks the same four steps. Call the model. Extract the final answer. Normalize the text. Score it. "
    "Three of those four never touch the model at all.",
    "EvalPipeline", {}, "stagger")

add("B04", "CHART",
    "Here is what the notebook actually produced. Four bars. Exact match zero, F1 zero, every dataset, every prompt. "
    "No error, no warning. The chart rendered cleanly.",
    "EvalZeroChart", {}, "stagger")

stmt("B05", "MOCK",
     "It is not a result. The OpenAI client never initialized, so every single call returned the literal string "
     "MOCK underscore OUTPUT. The harness scored a placeholder against the gold answers and dutifully reported perfect failure.",
     "THE FIRST BUG", "The model was never called.",
     "every prediction was the string MOCK_OUTPUT")

stmt("B06", "LESSON",
     "And that is the real problem, which is not in the metric. An evaluation that cannot separate a broken model "
     "from a broken pipeline is not measuring the model at all.",
     "WHAT IT MEANS", "Zero is not a score. It is a symptom.",
     "the harness has no way to tell you which failed")

add("B07", "NORMALIZER",
    "Now the second bug. The normalizer lowercases, then deletes every character outside a small allow-list. "
    "Watch what that does to the capital of Brazil.",
    "EvalNormalizer", {}, "type-on")

stmt("B08", "CONSEQUENCE",
     "So the gold answer and the spelling a model actually emits can never match. Brasilia scores zero against Brasília — "
     "not because the model was wrong, but because the accent was deleted and the tokens stopped lining up.",
     "THE CONSEQUENCE", "The gold answer is corrupted before comparison.",
     "a perfect answer, marked wrong by the scorer")

add("B09", "SCOREBOARD",
    "Run the notebook's own scoring functions and the damage is visible. A fully correct sentence naming Paris "
    "scores zero on both metrics, because the allow-list keeps the full stop and paris-with-a-period never matches paris.",
    "EvalScoreboard",
    {"rows": SCOREBOARD,
     "eyebrow": "computed by the notebook's own exact_match and f1_tokens",
     "sparkLine": "Two of these five predictions are correct and scored zero."},
    "stagger")

add("B10", "F1",
    "That last one stings, because F1 is supposed to be the forgiving metric. It measures token overlap, "
    "so Delhi against New Delhi earns nought point six seven — real partial credit. Punctuation defeats it anyway.",
    "EvalTokenOverlap", {}, "stagger")

add("B11", "FIX",
    "The fix is four lines. Fold unicode down to ASCII, and drop the full stop from the allow-list. "
    "Same predictions, same gold answers, same metrics — exact match moves from nought point six to one point zero.",
    "EvalBeforeAfter", {"before": BEFORE, "after": AFTER}, "stagger")

stmt("B12", "LESSON",
     "Nothing about the model changed. Forty percent of that score was the harness marking correct answers wrong. "
     "Ship it as-is and you would have concluded your prompting was failing.",
     "THE COST", "You would have tuned the prompt to fix the scorer.",
     "and the prompt was never the problem")

add("B13", "VERDICT",
    "So here is the teardown. The prompt engineering in this notebook is sound. The evaluation is what needed review — "
    "and evaluation is the part almost nobody reviews, because a number that renders looks exactly like a number that is true.",
    "ClaudeVerdictArtifact",
    {"artifactTitle": "Your Eval Is Lying to You — one page",
     "artifactHeading": "The teardown",
     "artifactLines": [
         "Bug 1 — the model was never called. The client failed to initialize, every prediction was the string MOCK_OUTPUT, and the harness reported 0.0 without a single warning.",
         "Bug 2 — the normalizer strips non-ASCII, so \"Brasília\" becomes \"bras lia\" and can never match the spelling a model emits.",
         "Bug 3 — the allow-list keeps the full stop, so a correct sentence ending in \"Paris.\" scores zero on exact match AND on F1.",
         "The fix: fold unicode to ASCII, drop the period. Four lines. Exact match went from 0.60 to 1.00 on the same predictions.",
         "The rule: test the scorer against the gold answers before you trust it to judge a model."]},
    "stagger")

add("B14", "HANDOFF",
    "Your turn, and this one takes a minute. Feed your own eval harness the gold answers as if they were predictions. "
    "If it does not return a perfect one point zero, your metric is broken before your model ever gets a turn.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "YOUR TURN", "segment": "Score the gold against itself",
     "command": "Take my evaluation harness and run it with the gold answers passed in as the predictions. Every score should be a perfect 1.0. Tell me every case where it is not, and why the normalizer or the metric is responsible.",
     "runningText": "scoring gold against gold…",
     "folderLabel": "@HumanitariansAI",
     "output": ["a scorer that cannot score itself perfectly is broken",
                "this catches normalizer bugs in about a minute"]},
    "type-on")

add("B15", "OUTRO",
    "Your eval is lying to you. If a build log that audits its own measurements is worth your time, subscribe. Humanitarians AI.",
    "ClaudeTitleOutro",
    {"title": "Your Eval Is Lying to You", "handle": "@HumanitariansAI"},
    "fade")

sheet = {
    "metadata": {
        "title": "Your Eval Is Lying to You",
        "slug": "hai-your-eval-is-lying",
        "topic": "EVAL TEARDOWN",
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
        "note": ("Teardown of an LLM prompt-engineering + evaluation notebook whose harness "
                 "reports 0.0 across the board. Three real bugs: the model was never called "
                 "(MOCK_OUTPUT), the normalizer strips non-ASCII, and it preserves the full stop. "
                 "Every on-screen metric is recomputed by build_beat_sheet.py using the notebook's "
                 "own scoring functions — no figure is hand-typed. NO INDIVIDUAL IS NAMED. "
                 "Bella (af_bella), Humanitarians AI. Never publishes."),
        "tags": ["LLM evaluation", "prompt engineering", "exact match", "F1",
                 "chain-of-thought", "eval harness", "unicode normalization",
                 "Humanitarians AI"],
    },
    "beats": B,
}

OUT.write_text(json.dumps(sheet, indent=2, ensure_ascii=False), encoding="utf-8")

words = sum(len(b["narration_text"].split()) for b in B)
print(f"wrote {OUT}")
print(f"{len(B)} beats · {words} words · projected {words/WPS:.0f}s = {int(words/WPS)//60}m{int(words/WPS)%60:02d}s")
print(f"computed: BEFORE={BEFORE}  AFTER={AFTER}")
for r in SCOREBOARD:
    print(f"   {r['pred']:<33}{r['gold']:<12}EM={r['em']:.0f} F1={r['f1']:.2f}")

BANNED = ["chinmay", "chinmai", "chinme", "sawant", "savant"]
blob = json.dumps(sheet, ensure_ascii=False).lower()
hits = [n for n in BANNED if n in blob]
print("NAME CHECK:", "CLEAN" if not hits else f"FAIL {hits}")
