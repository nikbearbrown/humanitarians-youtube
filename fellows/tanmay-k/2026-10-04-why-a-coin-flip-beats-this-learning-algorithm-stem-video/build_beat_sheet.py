#!/usr/bin/env python3
"""Writes beat_sheet.json for the Week 25 topic video: A WEIGHTED COIN (draft 1).

The film's structure is the corridor itself (Sutton & Barto, Example 13.1). Each chapter is one
answer to the puzzle, tried in order of how sensible it sounds, and each one walks the same four
squares on screen. Every factual line cites the FACTCHECK.md row that backs it (A1-A19).

Edit this script, not the JSON. Every Remotion prop is set explicitly (PLAYBOOK §2/§10): no
component default may reach the frame. Corridor and CoinCurve are NEW components, specified here
and built in the component phase (see BEATS-DRAFT.md → Components).
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
VOICE = "am_onyx"
TITLE = "Why a Coin Flip Beats This Learning Algorithm"
SIGNOFF = "Tanmay Kulkarni, in for Humanitarians AI"
WPS = 3.3  # planning rate (W23/W24 am_onyx). Measured Kokoro audio replaces it

MP3 = HERE / "mp3"
MEASURED = json.loads((MP3 / "timings.json").read_text()) if (MP3 / "timings.json").exists() else {}
sys.path.insert(0, str(HERE))
from cue_align import spoken_at, spoken_at_whisper  # noqa: E402

RESULTS = json.loads((HERE / "experiment" / "results.json").read_text())
CURVE = [[p, round(v, 2)] for p, v in RESULTS["curve"]]

SRC_BOOK = "Sutton & Barto, Reinforcement Learning: An Introduction, 2nd ed. (2018), Example 13.1, p. 323"
SRC_OURS = "Our runs: experiment/corridor.py, 30 seeds"
SRC_EXACT = "Exact value, our calculation (experiment/corridor.py)"

# Squares 0, 1, 2 and the goal (3). Square 1 is the swapped one.
ALWAYS_RIGHT = [0, 1, 0, 1, 0, 1, 0, 1, 0]       # loops end where they start, so the replay is seamless
ALWAYS_LEFT = [0, 0, 0, 0, 0, 0]
FAIR_WALK = [0, 0, 0, 1, 0, 0, 0, 0, 1, 2, 1, 2, 3]       # seeded sample (seed 2), 12 steps = the mean
SEEING_WALK = [0, 1, 2, 3]


def corridor(heading, view, rule, path, caption, source, p_right=None, show_swap=True,
             counter="steps", cue=None, caption_cue=None, loop=False, scoreline=None, step_cues=None):
    """Corridor props. view: 'viewer' (we see the swap) | 'blind' (every square drawn alike, the
    learner's reading) | 'sees' (each square labelled, the learner can see where it is).
    path: the token's squares in order, animated one step per `stepSeconds` from `walkAt`.
    scoreline: the B02 framework line as a strip under the corridor (no curve, markers only), so
    each answer visibly drops its point onto the same line the moment its score is spoken."""
    return {"type": "GRAPHIC", "status": "PROPS SET (component planned)", "motion": "illustrate",
            "remotion": {"pattern": "Corridor", "props": {
                "heading": heading, "view": view, "showSwap": show_swap, "rule": rule,
                "pRight": p_right, "path": path, "loopPath": loop, "stepSeconds": 0.45,
                "counter": counter, "caption": caption, "source": source,
                "walkAtCue": cue, "captionAtCue": caption_cue,
                **({"stepAtCues": step_cues} if step_cues else {}),
                "scoreline": scoreline}}}


def strip(markers):
    """Scoreline inset: markers placed so far (state carries beat to beat), the newest on its cue."""
    return {"xLabel": "chance of pressing right", "endsLabel": "never finishes", "markers": markers}


def dial(heading, markers, caption, source, peak=False, peak_cue=None, caption_cue=None,
         curve=True, curve_cue=None, peak_label="best: 58.6% → −11.66", equation=None):
    """CoinCurve props: value of the start state for every P(right) (our exact curve), with labelled
    markers that appear on their cue phrase. Both ends of the axis are drawn as 'never finishes'."""
    return {"type": "GRAPHIC", "status": "PROPS SET (component planned)", "motion": "illustrate",
            "remotion": {"pattern": "CoinCurve", "props": {
                "heading": heading, "curve": CURVE, "showCurve": curve, "curveAtCue": curve_cue,
                "xLabel": "chance of pressing right",
                "yLabel": "score (steps, negative)", "endsLabel": "never finishes",
                "markers": markers, "showPeak": peak, "peakLabel": peak_label,
                "peakAtCue": peak_cue, "caption": caption, "source": source,
                # typeset result (MATH-TYPESETTING.md); algebra checked in FACTCHECK A7
                "equation": equation or {"lhs": "", "lhsSup": "", "whole": "", "radicand": "",
                                         "approx": "", "note": ""},
                "captionAtCue": caption_cue}}}


def marker(p, v, label, cue):
    return {"p": p, "v": v, "label": label, "atCue": cue}


def card(title, heading, lines, spark, cue=None):
    return {"type": "GRAPHIC", "status": "PROPS SET", "motion": "illustrate", "remotion": {
        "pattern": "ClaudeArtifactCardFull",
        "props": {"chrome": "artifact", "artifactTitle": title, "artifactHeading": heading,
                  "artifactLines": lines, "sparkLine": spark}}}


BEATS = []


def beat(bid, act, tone, text, shot, refs):
    BEATS.append((bid, act, tone, text, shot, refs))


# ── COLD OPEN: the puzzle, before anything else ───────────────────────────────────────────
beat("B01", "THE PUZZLE", "curious, playful",
     "Here's a puzzle from a textbook. Four squares in a row. Start on the left, reach the goal on "
     "the right, and every step costs a point. Two buttons, left and right. Easy. "
     "Except in the second square, the buttons are swapped. And you're blindfolded. Every square "
     "gives you the same reading, and you can't keep count of your steps. So whatever you do in "
     "one square, you do in all three. "
     "Which button do you press?",
     corridor("Four squares. One is swapped.", "viewer", "", [0],
              "Same reading in every square. No counting steps.", SRC_BOOK + " · Ch. 9 opening, p. 197",
              counter="none", caption_cue="And you're blindfolded."),
     ["A1", "A2", "A3", "A22"])

# ── PRESENTER + SUBJECT IN PLAIN WORDS (PLAYBOOK §1c) ─────────────────────────────────────
beat("B02", "THE PLAN", "warm, clear",
     "Hi, this is Tanmay Kulkarni, in for Humanitarians AI. This video is about one example from "
     "Sutton and Barto's Reinforcement Learning: An Introduction, a textbook about machines that "
     "learn by trial and error. Here's the key to the puzzle. Any rule you could pick is really a "
     "coin: how often it presses right, from never to always. So every answer gets a spot on this "
     "line, and a score. We'll try them one at a time. By the end you'll know the best answer. "
     "It isn't a button. It's a biased coin, set to one exact number.",
     dial("Every rule is a coin", [],
          "Any rule for this corridor = one chance of pressing right. Each answer gets a spot and a score.",
          SRC_BOOK, curve=False, caption_cue="Any rule you could pick"),
     ["A1", "A3", "A20", "A25"])

# ── ANSWER 1 AND 2: commit to a button ────────────────────────────────────────────────────
beat("B03", "ALWAYS RIGHT", "brisk",
     "First answer: always press right. Square one, right, you move to square two. Square two, "
     "right. But it's swapped, so you slide back to square one. Right. Square two. Back again. You "
     "never reach the goal. Your score doesn't just get bad. It never stops counting.",
     corridor("Rule: always right", "viewer", "always right", ALWAYS_RIGHT,
              "Never reaches the goal.", "From the rules of Example 13.1",
              p_right=1.0, loop=True, cue="Square one, right", caption_cue="You never reach",
              step_cues=["you move to square two", "you slide back", "Square two. Back", "Back again"],
              scoreline=strip([marker(1.0, None, "always right: never finishes", "You never reach")])),
     ["A2", "A13"])

beat("B04", "ALWAYS LEFT", "dry",
     "Always press left? In the first square, left walks you into the wall. You stand there. Forever.",
     corridor("Rule: always left", "viewer", "always left", ALWAYS_LEFT,
              "Never leaves square one.", "From the rules of Example 13.1",
              p_right=0.0, loop=True, cue="left walks you", caption_cue="You stand there",
              scoreline=strip([marker(1.0, None, "always right: never finishes", None),
                               marker(0.0, None, "always left: never finishes", "Forever.")])),
     ["A2", "A13"])

# ── ANSWER 3: hand it to a learner that scores buttons ────────────────────────────────────
beat("B05", "THE BUTTON LEARNER", "explanatory",
     "So no fixed button works. Let's give the problem to a learning algorithm, a classic from the "
     "earlier chapters of the book, called Sarsa. It learns a score for each button from "
     "experience. Just one score per button, since every square reads the same. Then it mostly "
     "presses the higher one. One time in ten it presses a random button, "
     "just to keep exploring. That's what gets it out of the loops. I ran it thirty times. All "
     "thirty settled on the same thing. Mostly right.",
     card("Sarsa · ε = 0.1 · 30 runs", "Where the button learner settled",
          ["Scores each button, presses the higher one 95% of the time",
           "30 of 30 runs: mostly right",
           "0 of 30 runs: mostly left"],
          SRC_OURS + " (ε = 0.1, α = 0.01, 1,000 episodes)"),
     ["A4", "A16"])

beat("B06", "MINUS FORTY-FOUR", "deflated",
     "And mostly right is worth about minus forty-four. The book reports the same number. The only "
     "other place this learner can land, mostly left, is worse: about minus eighty-two. Those are "
     "its two options. It's built to find a best button, and in this corridor there isn't one.",
     dial("Where a button learner can land",
          [marker(0.95, -44.21, "mostly right ≈ −44", "about minus forty-four"),
           marker(0.05, -82.11, "mostly left ≈ −82", "about minus eighty-two")],
          "ε-greedy can only be mostly right or mostly left.", SRC_BOOK + " · values: " + SRC_EXACT,
          curve=False, caption_cue="Those are its two options"),
     ["A4", "A5"])

# ── ANSWER 4: the turn ────────────────────────────────────────────────────────────────────
beat("B07", "THE COIN", "surprised",
     "Then I tried something that felt almost insulting. No learning at all. Flip a fair coin "
     "every step. Heads, right. Tails, left. Minus twelve. A coin beat the learning algorithm by "
     "more than three and a half times. And that's not a lucky run. It's the exact value.",
     corridor("Rule: flip a fair coin", "viewer", "50% right", FAIR_WALK,
              "Fair coin: −12.00 (exact) · learner: −44.21", SRC_EXACT + " · walk shown: one seeded sample",
              p_right=0.5, cue="Flip a fair coin", caption_cue="Minus twelve.",
              scoreline=strip([marker(1.0, None, "never finishes", None),
                               marker(0.0, None, "never finishes", None),
                               marker(0.95, -44.21, "−44", None), marker(0.05, -82.11, "−82", None),
                               marker(0.5, -12.0, "fair coin −12", "Minus twelve.")])),
     ["A14", "A15"])

beat("B08", "WHY THE COIN WINS", "pulling back, careful",
     "Now, the coin isn't clever. It wins for a plain reason. The swapped square punishes "
     "commitment. Lean hard on either button and you pay for it, bouncing or stuck. The coin "
     "doesn't commit at all. Which raises a question. Is fifty-fifty actually the best you can do?",
     dial("Commit hard, and you pay for it",
          [marker(0.95, -44.21, "mostly right −44", None),
           marker(0.05, -82.11, "mostly left −82", None),
           marker(0.5, -12.0, "fair coin −12", "The coin")],
          "Is 50% the best setting?", SRC_EXACT, caption_cue="Is fifty-fifty", curve=False),
     ["A13", "A14"])

# ── THE DIAL ──────────────────────────────────────────────────────────────────────────────
beat("B09", "WEIGHT THE COIN", "curious, building",
     "So let's bias the coin. At one end it never says right. At the other, it always does. "
     "And here's the score for every setting in between. Both ends never finish. The learner's "
     "two options sit way down here. The fair coin is near the top. But it isn't the top. The "
     "best setting leans a little toward right.",
     dial("Every setting of the coin",
          # all three carried from B08; the curve drawing through them is the only new element
          [marker(0.05, -82.11, "mostly left", None),
           marker(0.95, -44.21, "mostly right", None),
           marker(0.5, -12.0, "fair coin", None)],
          "The best setting is not 50%.", SRC_EXACT, caption_cue="best setting",
          curve_cue="here's the score for every"),
     ["A13", "A14", "A5"])

beat("B10", "TWO MINUS ROOT TWO", "quiet wonder",
     "The best setting works out to two minus the square root of two. About fifty-eight point six "
     "percent right, for a score of minus eleven point six six. The book rounds it to "
     "fifty-nine percent and leaves the exact form as an exercise for the reader. And that exact "
     "form is irrational. The best way through this corridor is a coin no one could ever mint "
     "exactly.",
     dial("The best setting",
          [marker(0.5, -12.0, "fair coin −12", None)],
          "The book: \u201cabout 0.59\u201d, \u201cabout −11.6\u201d. The exact form is left as Exercise 13.1.",
          SRC_BOOK + " · exact form: Exercise 13.1, p. 324", peak=True,
          peak_cue="two minus the square root", caption_cue="The book rounds",
          equation={"lhs": "p", "lhsSup": "*", "whole": "2", "radicand": "2", "approx": "0.586",
                    "note": "chance of pressing right"}),
     ["A6", "A7"])

# ── ANSWER 5: the learner the chapter is about ────────────────────────────────────────────
beat("B11", "SOMETHING NEW", "explanatory, satisfying",
     "And this is what the book is really getting at. Almost everything before chapter thirteen "
     "learns the way Sarsa did, by scoring actions. Chapter thirteen opens with, quote, in this "
     "chapter we consider something new. Learners that don't score buttons at all. They learn "
     "the coin's bias directly, shifting the odds toward whatever the runs reward.",
     card("Chapter 13 · Policy Gradient Methods", "“In this chapter we consider something new.”",
          ["Before: score each action, then pick the best (almost all methods)",
           "Chapter 13: learn the probabilities directly"],
          "Sutton & Barto (2018), p. 321. One earlier exception: gradient bandits, Sec. 2.8"),
     ["A10", "A8"])

beat("B12", "THE COIN LEARNER", "building to payoff",
     "The simplest one is called REINFORCE. I started it at the worst setting I had, mostly left, "
     "minus eighty-two. Within four hundred episodes it was averaging about minus thirteen. Across "
     "thirty runs, the average setting it settled on was fifty-eight point six percent. It found "
     "two minus root two on its own.",
     dial("REINFORCE, started at mostly left",
          [marker(0.05, -82.11, "start: −82", "I started it")],
          "Runs ranged 53%–65%; the average landed on the best setting.",
          SRC_OURS + " (α = 2⁻¹², 2,000 episodes)", peak=True, peak_cue="the average setting",
          caption_cue="the average setting", peak_label="average 58.6% → −11.70"),
     ["A12", "A17"])

beat("B13", "WHY IT SITS HERE", "reflective",
     "The book says it plainly. Methods that score actions have no natural way of finding the best "
     "random policy. Methods that learn the probabilities can. But that leaves a fair question. "
     "Why did the best answer have to be random at all?",
     card("Section 13.1", "Why learn probabilities?",
          ["Action-value methods: no natural way to find stochastic optimal policies",
           "Policy methods can, as Example 13.1 shows"],
          "Sutton & Barto (2018), Sec. 13.1, p. 323 (paraphrased)"),
     ["A8"])

# ── THE TEST, OUTCOME ONE: the randomness disappears ──────────────────────────────────────
beat("B14", "TAKE OFF THE BLINDFOLD", "still, honest",
     "Here's how to find out. Take off the blindfold. Same Sarsa learner as before, but now it keeps "
     "a separate score for each square. Thirty runs out of thirty, it learned right, left, right. "
     "Three steps. Minus three. Nearly four times better than the best coin. And the book says that's "
     "no accident. When the player knows exactly where it is, there's always a fixed rule that's "
     "best. The coin was covering for what it couldn't see.",
     corridor("Same learner, one score per square", "sees", "right · left · right", SEEING_WALK,
              "30 of 30 runs: right, left, right → −3 (best coin −11.66). Book: with full state, "
              "a deterministic optimal policy always exists.",
              SRC_OURS + " (sarsa_sees_state) · Sutton & Barto (2018), Sec. 17.3, p. 465",
              cue="right, left, right", caption_cue="When the player knows"),
     ["A18", "A19", "A21", "A22"])

# ── THE TEST, OUTCOME TWO: the randomness survives (falsifiability case) ──────────────────
beat("B15", "THE OTHER OUTCOME", "curious, then firm",
     "But randomness doesn't always disappear. The book's own example is poker, where the best play "
     "is often to bluff with a specific probability. Here's a simpler one I ran. Rock, paper, "
     "scissors, against an opponent that learns your habits. Nothing is hidden. Always rock lost "
     "essentially every round. Leaning toward rock still came out behind. The even three-way split "
     "broke even. Now swap in an opponent that just plays at random, and always rock does as well "
     "as anything. That randomness is there because someone is watching for a pattern.",
     card("Rock, paper, scissors · 30 runs × 1,000 rounds", "Against an opponent that learns your habits",
          ["Always rock: −0.999 per round (lost essentially every round)",
           "Lean rock 50/30/20: −0.29 per round",
           "Even 1/3 each: ≈ 0 (broke even)",
           "Opponent that plays at random: all three ≈ 0"],
          "Our runs: experiment/rps.py · Poker: Sutton & Barto (2018), Sec. 13.1, p. 323"),
     ["A9", "A23", "A24"])

# ── THE TEST ITSELF: the reusable rubric, stated once, both outcomes on screen ────────────
beat("B16", "THE BLINDFOLD TEST", "clear, confident",
     "So that's the test, and you can carry it to other problems. When the best move is random, give the player more "
     "information. If the randomness disappears, it was covering for what the player couldn't see. "
     "If it survives, look for someone who'd exploit a pattern. The corridor is the first kind. "
     "Rock, paper, scissors is the second.",
     card("The blindfold test", "When the best move is random, give the player more information.",
          ["Randomness disappears → it was covering for what the player couldn't see "
           "(corridor: −11.66 → −3)",
           "Randomness survives → someone would exploit a pattern "
           "(rock-paper-scissors: always rock −0.999 / round)"],
          "Corridor: experiment/corridor.py · RPS: experiment/rps.py · Sutton & Barto (2018), Sec. 17.3"),
     ["A21", "A18", "A23"])

# ── THE TASK: a new case, with what a strong and a weak answer look like ──────────────────
beat("B17", "THE GOALKEEPER", "direct, inviting",
     "Now try it on a goalkeeper facing a penalty, choosing which way to dive. Run the test. Does "
     "more information make the randomness disappear, or does it survive? Put your answer in the "
     "comments. A strong answer names the missing information, or the person who'd exploit the "
     "pattern. Saying it's random because it's uncertain doesn't count. And if you code, the corridor "
     "script is linked below. Run it, and watch the blindfold come off.",
     card("Run the blindfold test: a goalkeeper at a penalty", "Does more information remove the randomness?",
          ["Strong answer: names the missing information, or who would exploit a pattern",
           "Weak answer: \u201cit's random because it's uncertain\u201d",
           "Code: experiment/corridor.py · stdlib Python · runs in under a second"],
          "Answer in the comments"),
     [])

beat("B18", "OUTRO", "warm",
     "Two minus root two. Tanmay Kulkarni, in for Humanitarians AI, signing off.",
     {"type": "GRAPHIC", "status": "PROPS SET", "motion": "fade", "remotion": {
         "pattern": "ClaudeTitleOutroFull",
         "props": {"title": "The best move was a weighted coin.", "handle": "@HumanitariansAI",
                   "subline": SIGNOFF}}},
     [])


def main():
    beats = []

    def at(text, cue):
        # Whisper clock once audio exists (cue_align: Whisper's words snapped to the audio's own pauses),
        # pause clock as fallback, planning rate before audio. W24: fixed-rate cues drifted up to 1.2 s.
        if cue not in text:
            sys.exit(f"cue not in narration: {cue!r}")
        mp3 = MP3 / f"beat-{CUR['bid']}.mp3"
        if CUR["bid"] in MEASURED and mp3.exists():
            w = spoken_at_whisper(text, mp3, cue)
            return w if w is not None else spoken_at(text, mp3, cue)
        return round(len(text[:text.index(cue)].split()) / WPS, 2)

    def resolve(d, text):
        # "<key>Cue": narration phrase → "<key>": absolute seconds (PLAYBOOK §2: never fractions)
        if isinstance(d, dict):
            if isinstance(d.get("stepAtCues"), list):
                d["stepAt"] = [at(text, c) for c in d.pop("stepAtCues")]
            for k in [k for k in d if k.endswith("Cue")]:
                v = d.pop(k)
                # a marker with no cue is carried from the previous beat: on screen from frame 0
                # (None), never popped in at 0.6 s, which also made two carried markers both "newest"
                # curveAtCue None = the curve carried over from the previous beat: drawn from frame 0
                # (it re-drew itself at every cut in the first compile, B10/B12)
                d[k[:-3]] = at(text, v) if isinstance(v, str) else (None if k == "atCue" else -10.0 if k == "curveAtCue" else 0.6)
            for v in d.values():
                resolve(v, text)
        elif isinstance(d, list):
            for v in d:
                resolve(v, text)

    CUR = {}
    ids = [b[0] for b in BEATS]
    assert len(ids) == len(set(ids)), "duplicate beat_id"
    for bid, act, tone, text, shot, refs in BEATS:
        words = len(text.split())
        CUR["bid"] = bid
        rem = shot.get("remotion")
        if rem:
            rem["pattern"] += "OFL"   # open-licence fonts only, as W24
            resolve(rem["props"], text)
            if bid in MEASURED and rem["pattern"].startswith(("Corridor", "CoinCurve")):
                # render length = measured audio, or the composition's registered length is used
                rem["props"]["durationSeconds"] = round(MEASURED[bid] + 0.1, 2)
        beats.append({"beat_id": bid, "act": act, "tone": tone, "narration_text": text,
                      "shot": shot, "estimated_duration_s": round(words / WPS, 1),
                      "word_count": words, "audio_file": f"mp3/beat-{bid}.mp3",
                      **({"actual_duration_s": MEASURED[bid]} if bid in MEASURED else {}),
                      "engine": "kokoro", "voice": VOICE,
                      "factcheck_ref": [f"FACTCHECK.md {r}" for r in refs] or None})
    sheet = {"metadata": {
        "title": TITLE, "title_status": "WORKING", "structure": "THE CORRIDOR (one answer per chapter)",
        "slug": "why-a-coin-flip-beats-this-learning-algorithm",
        "topic": "REINFORCEMENT LEARNING", "register": "Pragmatist", "audience": "hai",
        "brand": "claude-liam", "channel": "hai", "chip": "@HumanitariansAI",
        "voice": VOICE, "engine": "kokoro", "voice_kokoro": VOICE,
        "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "thesis": ("In Sutton & Barto's short corridor, every fixed button fails and a button-scoring "
                   "learner lands at about -44. The optimum is a coin weighted 2 - sqrt(2) toward right "
                   "(-11.66), which a probability-tuning learner finds on its own, but only because the "
                   "learner cannot see which square it is in. Give it that and right-left-right wins."),
        "source_project": "claude-for-education/reinforcement-learning-an-introduction (10-beat auto-conversion of Nik Bear Brown's book review; base topic, template discarded)",
        "note": "DRAFT 1 (THE CORRIDOR). Generated by build_beat_sheet.py. Edit that, not this file. Runtime is a words/sec estimate until Kokoro audio exists. Corridor + CoinCurve are planned components.",
    }, "beats": beats}
    (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
    total = sum(b["word_count"] for b in beats)
    est = sum(b["estimated_duration_s"] for b in beats)
    print(f"{len(beats)} beats · {total} words · ~{int(est // 60)}:{int(est % 60):02d} estimated")
    for b in beats:
        print(f"  {b['beat_id']:4} {b['act']:24} {b['word_count']:3}w ~{b['estimated_duration_s']:5}s  {b['tone']}")


if __name__ == "__main__":
    import sys
    main()
