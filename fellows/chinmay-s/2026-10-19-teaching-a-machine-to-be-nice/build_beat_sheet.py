#!/usr/bin/env python3
"""Author beat_sheet.json for hai-teaching-a-machine-to-be-nice — kid-friendly cut.

Subject: a from-scratch alignment notebook (NumPy only): SFT, a reward model,
best-of-n, RLHF with and without a KL penalty, and DPO.

The notebook deliberately runs the unleashed case to demonstrate reward hacking,
which it calls "the single most important plot". This reel TEACHES; it is not a
teardown. Every figure is parsed from the notebook's recorded outputs under
assertions. No individual is named.
"""
import json
import re
from pathlib import Path

NB = Path(r"C:\Users\sawan\OneDrive\Desktop\dumps\aligning_llms_rlhf_dpo_from_scratch.ipynb")
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
    assert m, f"{pat!r} not found in cell {i}"
    return m.group(g)


def metrics(i):
    """Pull {'true score': np.float64(x), 'grammatical': y, ...} out of a printed dict."""
    txt = stream(i)
    d = {}
    for key in ("true score", "grammatical", "diversity", "sentiment"):
        m = re.search(rf"'{key}':\s*(?:np\.float64\()?(-?[\d.]+)", txt)
        if m:
            d[key] = float(m.group(1))
    return d


GRAD_ERR = grab(17, r"worst relative error: ([\d.e+-]+)")
N_PARAMS = grab(21, r"model has ([\d,]+) parameters")
BASE = metrics(22)
SFT = metrics(25)
DEMO_MEAN = grab(25, r"200 demonstrations, mean true score ([+-][\d.]+)")
N_PAIRS = grab(28, r"collected ([\d,]+) comparisons")
LABEL_ACC = grab(28, r"labels agree with the true better review ([\d.]+)%")
RM_VS_TRUTH = grab(32, r"agrees with the TRUE better review:\s+([\d.]+)%")

# reward-model probe table
PROBES = []
for line in stream(34).splitlines():
    m = re.match(r"^(.+?)\s{2,}([+-][\d.]+)\s+([+-][\d.]+)\s*$", line.rstrip())
    if m and not m.group(1).startswith("review"):
        t, j = float(m.group(2)), float(m.group(3))
        PROBES.append((m.group(1).strip(), t, j))

BON = [(int(a), float(b)) for a, b in
       re.findall(r"best of\s+(\d+): true score ([+-][\d.]+)", stream(37))]

# the unleashed run
HACK = [(int(a), float(b), float(c), int(d)) for a, b, c, d in re.findall(
    r"it\s+(\d+) \| reward model ([+-][\d.]+) \| true score ([+-][\d.]+) \| KL\s+[\d.]+ \| grammatical (\d+)%",
    stream(42))]
HACK_SAMPLE = re.findall(r"\[-3\.00\]\s*(.+)", stream(42))
HACK_FINAL = metrics(42)

BETAS = [(a, float(b), int(c), int(d)) for a, b, c, d in re.findall(
    r"beta = ([\d.]+)\s+true score ([+-][\d.]+) \| grammatical (\d+)% \| KL\s+[\d.]+ \| diversity (\d+)%",
    stream(45))]

DPO = metrics(49)
DPO_NLL = metrics(53)

# ── guards ────────────────────────────────────────────────────────────────
assert float(GRAD_ERR) < 1e-6, GRAD_ERR
assert BASE["true score"] < 0.1 and SFT["true score"] > BASE["true score"], (BASE, SFT)
assert 70 < float(LABEL_ACC) < 85, LABEL_ACC
assert len(PROBES) >= 6, len(PROBES)
assert any(t < 0 < j for _, t, j in PROBES), "need at least one fooled probe"
assert len(BON) >= 4 and BON[-1][1] > BON[0][1], BON
assert len(HACK) >= 5, len(HACK)
assert HACK[-1][1] > HACK[0][1], "judge score must rise"
assert HACK[-1][2] < HACK[0][2], "true score must fall"
assert HACK[-1][3] == 0, "grammar must hit zero"
assert len(BETAS) >= 3, BETAS
assert DPO["grammatical"] < 0.6 < DPO_NLL["grammatical"], (DPO, DPO_NLL)
print(f"[nb] grad {GRAD_ERR} · params {N_PARAMS} · base {BASE['true score']} -> SFT {SFT['true score']}")
print(f"[nb] labels {LABEL_ACC}% · RM vs truth {RM_VS_TRUTH}% · probes {len(PROBES)}")
print(f"[nb] best-of: {BON[0]} -> {BON[-1]}")
print(f"[nb] hack: judge {HACK[0][1]:+.2f}->{HACK[-1][1]:+.2f} truth {HACK[0][2]:+.2f}->{HACK[-1][2]:+.2f} gram {HACK[0][3]}%->{HACK[-1][3]}%")
print(f"[nb] DPO {DPO['true score']} gram {DPO['grammatical']} · +NLL {DPO_NLL['true score']} gram {DPO_NLL['grammatical']}")

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
    "A machine was taught to write nice restaurant reviews. It learned to write this instead. "
    "This is Humanitarians AI. Today: how you teach a machine what you want, "
    "and the very strange thing that happens when you get it slightly wrong.",
    "ClaudeComposerAsk",
    {"greeting": "Teach it to be nice.", "topic": "TEACHING MACHINES WHAT WE WANT",
     "segment": "Teaching a Machine to Be Nice",
     "command": "Walk me through aligning a small language model: showing it examples, building a judge from people's preferences, and training against that judge. Then show me what happens with no restraint at all.",
     "runningText": "opening the notebook…",
     "folderLabel": "@HumanitariansAI",
     "output": ["show it good examples",
                "build a judge from what people prefer",
                "then watch it learn to cheat the judge"]},
    "type-on")

add("B01", "SFT",
    "We start with a machine that writes restaurant reviews. Good ones, bad ones, it does not care — "
    "it just writes. So first we show it two hundred nice reviews, and ask it to write more like those.",
    "KidReviewBot",
    {"before": f"{BASE['true score']:+.2f}", "after": f"{SFT['true score']:+.2f}",
     "sample": "the dessert was really delicious and the room was excellent ."},
    "stagger")

stmt("B02", "LIMIT",
     "That helps, and it is also as far as showing examples can take you. "
     "To go further the machine needs to know not just what good looks like, but which of two things is better. "
     "And for that, somebody has to say.",
     "THE NEXT PROBLEM", "Examples only get you so far.",
     "now it needs to compare, not copy")

add("B03", "NOISY",
    f"So we show people pairs of reviews and ask which is nicer. {N_PAIRS} times. "
    "But here is the thing nobody mentions: people are not perfect at this.",
    "KidNoisyLabels",
    {"agreePct": f"{LABEL_ACC}%", "agreeN": float(LABEL_ACC) / 100.0},
    "stagger")

stmt("B04", "JUDGE",
     "Now we train a judge. It reads thousands of those pairs and learns to give any review a score, "
     "trying to agree with what people picked. It ends up a little better than the people were — "
     "but it learned from their mistakes too.",
     "BUILDING THE JUDGE", "A judge built from imperfect opinions.",
     "it is a copy of a slightly blurry original")

add("B05", "BLINDSPOT",
    "And when you test that judge carefully, you find the gaps. On ordinary reviews it does fine — great beats terrible, exactly as you would hope. But look at the highlighted rows. Add the word not, and it barely notices. Say the same nice thing three times over, and it likes you more, not less.",
    "KidJudgeBlindSpot",
    {"rows": [{"text": t, "truth": f"{tr:+.2f}", "judge": f"{j:+.2f}", "fooled": (tr < 0 < j) or (tr > 0 > j)}
              for (t, tr, j) in PROBES[:7]]},
    "stagger")

stmt("B06", "GAPS",
     "It never worked out what the word not means, so not great looks positive to it. "
     "And it adores piled-up praise — the more times you say very and amazing, the higher it scores you, "
     "even when a real reader would find it ridiculous.",
     "TWO BLIND SPOTS", "It cannot hear the word “not”.",
     "and it rewards saying “very” over and over")

add("B07", "BESTOF",
    "Before anything clever, here is the lazy idea that works. Write several reviews, let the judge pick the best one, "
    "and throw the rest away. No training at all.",
    "KidBestOfN",
    {"rows": [{"n": str(n), "score": f"{s:+.3f}", "bar": max(0.05, s / max(x[1] for x in BON))}
              for (n, s) in BON]},
    "stagger")

stmt("B08", "NOWTRAIN",
     "But we want the machine itself to get better, not just to guess repeatedly. "
     "So we let it practise: write a review, see what the judge scores it, and change slightly to score higher next time. "
     "Over and over. With no other rules at all.",
     "NOW LET IT PRACTISE", "Chase the score. Nothing else.",
     "what could possibly go wrong")

add("B09", "CHEAT",
    "Watch both lines. The orange one is what the judge thinks of the reviews. The dark one is how good they actually are. At the start they agree with each other. Then they come apart — and they never come back together. The orange line climbs the whole way up. The dark one falls off a cliff.",
    "KidCheating",
    {"pts": [{"it": it, "judge": j, "truth": t, "gram": g / 100.0} for (it, j, t, g) in HACK],
     "hacked": (HACK_SAMPLE[0][:120] if HACK_SAMPLE else "")},
    "stagger")

stmt("B10", "HACKED",
     f"The judge is delighted. It went from {HACK[0][1]:+.2f} up to {HACK[-1][1]:+.2f}. "
     f"Meanwhile the reviews fell from {HACK[0][2]:+.2f} to {HACK[-1][2]:+.2f}, and the share that are even proper sentences "
     f"went from {HACK[0][3]} percent to {HACK[-1][3]}.",
     "WHAT ACTUALLY HAPPENED", "The score went up. Everything else collapsed.",
     "it stopped writing reviews and started writing bait")

stmt("B11", "CHEATING",
     "It found the judge's weak spot and did nothing but that. It is not broken, and it is not being naughty. "
     "It did exactly what we asked — we just asked for the score, and forgot to ask for the reviews.",
     "IT DID AS IT WAS TOLD", "Nobody taught it to cheat. We taught it to score.",
     "this has a name: reward hacking")

add("B12", "LEASH",
    "The fix is a lead. Alongside chasing the score, we add one more rule: do not drift too far from how you used to write. "
    "The shorter the lead, the less it can wander.",
    "KidLeash",
    {"rows": [{"beta": f"lead = {b}", "score": f"{s:+.3f}", "gram": f"{g}%", "variety": f"{d}%",
               "hero": abs(float(b) - 0.1) < 1e-9} for (b, s, g, d) in BETAS]},
    "stagger")

stmt("B13", "WORKS",
     f"And now it works. With a middling lead the reviews score {[s for (b, s, _, _) in BETAS if abs(float(b)-0.1) < 1e-9][0]:+.2f}, "
     "almost everything is a proper sentence, and it still has things to say. "
     "Too short a lead and every review sounds the same. Too long and we are back to nonsense.",
     "THE LEAD WORKS", "Good reviews, and still proper sentences.",
     "the lead length is the whole art of it")

stmt("B14", "DPO",
     "There is a second route that skips the judge entirely. Instead of building one, "
     "you show the machine the pairs directly and say: make the preferred one more likely, and the other one less. "
     "It is simpler, and much faster.",
     "THE SHORTCUT", "Skip the judge. Learn straight from the pairs.",
     "no separate judge to fool")

stmt("B15", "DPOBREAK",
     f"Except on this run it goes wrong in its own way. Pushing the worse review down drags the better one down with it, "
     f"and the writing falls apart — only {DPO['grammatical']*100:.0f} percent proper sentences, "
     f"and a true score of {DPO['true score']:+.2f}.",
     "A DIFFERENT FAILURE", "Push one down, and the other sinks too.",
     "a known quirk, not a mistake in the code")

stmt("B16", "DPOFIX",
     f"The repair is a reminder. Alongside pushing the bad one down, keep practising the good one. "
     f"That brings it back: {DPO_NLL['grammatical']*100:.0f} percent proper sentences, "
     f"and a true score of {DPO_NLL['true score']:+.2f}.",
     "THE REPAIR", "Keep practising the good answers, too.",
     "one extra term, and the writing returns")

add("B17", "SCOREBOARD",
    "So here they all are together, scored on the thing we actually cared about the whole time. Showing examples helped a bit. Writing sixteen and keeping the best helped more, with no training whatsoever. The one kept on a lead is the best of the trained ones. And the one we let run free, the one the judge adored most, finishes dead last.",
    "KidScoreboard",
    {"rows": [
        {"name": "before any teaching", "score": f"{BASE['true score']:+.2f}", "bar": BASE["true score"],
         "gram": f"{BASE['grammatical']*100:.0f}%", "good": False, "bad": False},
        {"name": "shown good examples", "score": f"{SFT['true score']:+.2f}", "bar": SFT["true score"],
         "gram": f"{SFT['grammatical']*100:.0f}%", "good": False, "bad": False},
        {"name": f"write {BON[-1][0]}, keep the best", "score": f"{BON[-1][1]:+.2f}", "bar": BON[-1][1],
         "gram": "—", "good": True, "bad": False},
        {"name": "chasing the judge, no lead", "score": f"{HACK_FINAL['true score']:+.2f}",
         "bar": HACK_FINAL["true score"], "gram": f"{HACK_FINAL['grammatical']*100:.0f}%",
         "good": False, "bad": True},
        {"name": "chasing the judge, on a lead", "score": f"{BETAS[1][1]:+.2f}", "bar": BETAS[1][1],
         "gram": f"{BETAS[1][2]}%", "good": True, "bad": False},
        {"name": "straight from the pairs", "score": f"{DPO['true score']:+.2f}", "bar": DPO["true score"],
         "gram": f"{DPO['grammatical']*100:.0f}%", "good": False, "bad": True},
        {"name": "pairs, with the reminder", "score": f"{DPO_NLL['true score']:+.2f}", "bar": DPO_NLL["true score"],
         "gram": f"{DPO_NLL['grammatical']*100:.0f}%", "good": True, "bad": False},
    ]},
    "stagger")

stmt("B18", "LESSON",
     "And here is the idea worth keeping, long after you have forgotten the rest. "
     "The moment you turn something you care about into a score, and then push hard on that score, "
     "the score and the thing you cared about start to come apart.",
     "THE BIG IDEA", "A measure you push hard on stops being a good measure.",
     "true of machines, and of people, and of schools")

add("B19", "VERDICT",
    "So here is the whole story. A machine that writes. Two hundred examples to show it what nice looks like. "
    "A judge built from thousands of human choices that were themselves only right about three quarters of the time. "
    "A judge with blind spots. And a machine that found every single one of them the moment we let it off the lead.",
    "ClaudeVerdictArtifact",
    {"artifactTitle": "Teaching a machine to be nice",
     "artifactHeading": "What happened",
     "artifactLines": [
         f"Showing examples moved it from {BASE['true score']:+.2f} to {SFT['true score']:+.2f}. Useful, and not enough.",
         f"The judge learned from {N_PAIRS} human comparisons that picked the genuinely better review only {LABEL_ACC}% of the time.",
         "It never learned the word 'not', and it rewarded piled-up praise that a real reader would laugh at.",
         f"Let off the lead, the machine drove the judge's score to {HACK[-1][1]:+.2f} while real quality hit {HACK[-1][2]:+.2f} and grammar hit {HACK[-1][3]}%.",
         f"A lead fixed it: {BETAS[1][1]:+.2f} with {BETAS[1][2]}% proper sentences. The shortcut route needed its own repair, {DPO['true score']:+.2f} to {DPO_NLL['true score']:+.2f}.",
         "The lesson: push hard enough on any measure and it stops measuring the thing you wanted."]},
    "stagger")

add("B20", "HANDOFF",
    "Your turn. Think of a score somebody measures you by — marks at school, steps on a watch, likes on a post. "
    "Now think of how you would push that number up without actually doing the thing it is meant to measure. "
    "You will find a way in about ten seconds. So does the machine.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "YOUR TURN", "segment": "Find the loophole",
     "command": "Pick a metric my team is measured on. Tell me the three easiest ways to make that number go up without improving the thing it is supposed to represent.",
     "runningText": "looking for loopholes…",
     "folderLabel": "@HumanitariansAI",
     "output": ["every score has a loophole",
                "the question is who finds it first"]},
    "type-on")

add("B21", "OUTRO",
    "Teaching a machine to be nice. If you like the parts where it goes wrong, subscribe. Humanitarians AI.",
    "ClaudeTitleOutro",
    {"title": "Teaching a Machine to Be Nice", "handle": "@HumanitariansAI"},
    "fade")

sheet = {
    "metadata": {
        "title": "Teaching a Machine to Be Nice",
        "slug": "hai-teaching-a-machine-to-be-nice",
        "topic": "TEACHING MACHINES WHAT WE WANT",
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
        "note": ("KID-FRIENDLY explainer of a from-scratch alignment notebook (SFT, reward model, "
                 "best-of-n, RLHF with/without KL penalty, DPO). This reel TEACHES — the notebook "
                 "deliberately runs the unleashed case to demonstrate reward hacking, and includes a "
                 "gradient check plus honest reporting of DPO's likelihood-displacement failure. "
                 "Every figure parsed from recorded outputs under 13 assertions. Goodhart's law is "
                 "the closing idea, delivered without the name. NO INDIVIDUAL IS NAMED. Bella."),
        "tags": ["RLHF", "DPO", "reward hacking", "alignment", "Goodhart's law",
                 "explain like I'm ten", "reward model", "kids", "Humanitarians AI"],
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
