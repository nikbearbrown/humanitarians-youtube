#!/usr/bin/env python3
"""Builds beat_sheet.json for claude-liam-overfitting (ai-explainer spine, Liam in for Bear)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "beat_sheet.json")
SLUG = "claude-liam-overfitting"
TITLE = "Overfitting, One Memorized Point at a Time"
VOICE = dict(voice="am_onyx", engine="kokoro")
FOLDER = "@NikBearBrown"

def rem(pattern, props, show):
    return {"type": "REMOTION", "source": "own", "show": show,
            "remotion": {"pattern": pattern, "props": props}}

def card(bid, act, narr, est, shot, proof="SHOW", qc=None, **extra):
    b = {"beat_id": bid, "act": act, "proof_gate": proof, "narration_text": narr,
         "estimated_duration_s": est, **VOICE, "shot": shot}
    b.update(extra)
    if qc:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": qc}
    return b

def man(bid, act, narr, est, intent, show, cls, claim):
    return {"beat_id": bid, "act": act, "proof_gate": "SHOW", "narration_text": narr,
            "estimated_duration_s": est, **VOICE,
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": intent,
                     "show": show, "manim": {"class": cls}},
            "motion_claim": claim}

beats = []
beats.append(card("B00", "ask",
    "Hi, this is Liam, in for Bear. The ask: why can a model score perfectly on its training data and still fail on new data? Show me with real numbers. A flexible model can memorize the noise in its examples. So judge it on points it has never seen. A perfect training score can hide a worse model.",
    24,
    rem("ClaudeComposerAsk", {
        "greeting": "Hi, Liam", "topic": "MACHINE LEARNING · OVERFITTING",
        "segment": TITLE,
        "command": "Why can a model score perfectly on its training data and still fail on new data? Show me with real numbers.",
        "runningText": "working through the math…", "folderLabel": FOLDER,
        "output": ["Working through the math…",
                   "the trick: a flexible model memorizes the noise, so judge it on points it has never seen",
                   "worked example: 8 points, a line scores 0.099 train and 0.074 test; a degree 7 curve scores 0.000 and 0.221",
                   "where it bites: training error always falls with flexibility, test error turns around"]},
        [{"at": 0.0, "event": "the ask types into the composer"},
         {"at": 0.45, "event": "result lines land one by one"}]),
    qc="Cold-open composer: the ask and its result lines are the motion."))

beats.append(card("B01", "overview",
    "A perfect fit means it memorized. Not that the model learned the pattern, but that it learned the noise along with it. That is why a perfect training score proves very little.",
    13,
    rem("BrutalistHesitantWriter", {
        "text": "A perfect fit\nproves it learned.",
        "triggerWords": "proves it learned",
        "replacementWords": "means it memorized",
        "fontSize": 140, "charMs": 26, "hesitateBetween": 8, "hesitateWithin": 1,
        "mistakeRate": 5, "jitter": 20, "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types the naive framing"},
         {"at": 0.45, "event": "backspaces 'proves it learned' and writes 'means it memorized'"}]),
    lead_silence_s=0.8,
    motion_claim="The writer types the naive framing and corrects it on the spoken word.",
    qc="Hesitant-writer overview: the correction is the motion."))

beats.append(man("B02", "a straight line",
    "Eight points, scattered around a rising line. Fit a straight line and it misses every point a little. The training error is point oh nine nine. Now bring fresh points the model has never seen. The test error is point oh seven four. About the same. That is what learning looks like.",
    19, "A simple fit scores about the same on training and fresh points.",
    [{"at": 0.1, "event": "eight points and the fitted line"},
     {"at": 0.4, "event": "readout: train error 0.099"},
     {"at": 0.6, "event": "fresh hollow points appear; readout: test error 0.074"}],
    "B02_Line", "Fresh points landing near the same line is the claim."))

beats.append(man("B03", "full freedom",
    "Now give the model more freedom. A degree seven curve. It bends through every single point. Training error: zero. A perfect score.",
    12, "A flexible curve passes through every training point.",
    [{"at": 0.15, "event": "line morphs into the degree 7 curve through all 8 points"},
     {"at": 0.7, "event": "readout: train error 0.000"}],
    "B03_Memorize", "The line bending into a curve through every dot is the claim."))

beats.append(man("B04", "fresh points",
    "But look at the fresh points. The curve swings between its memorized dots and misses them. Test error, point two two one. Three times the straight line's. The perfect model is the worse model.",
    16, "The memorizing curve misses fresh points that the line nearly hits.",
    [{"at": 0.1, "event": "degree 7 curve with fresh points and their misses"},
     {"at": 0.55, "event": "readout: test error 0.221"},
     {"at": 0.8, "event": "curve morphs back to the line; test error 0.074"}],
    "B04_Fresh", "Same fresh points, two models, two error readouts."))

beats.append(man("B05", "every degree",
    "Try every degree from one to seven. Training error only falls, from point oh nine nine to zero. Test error doesn't. It sits near point oh eight through degree three, then jumps to point one three nine, and climbs to point two two one. The gap between the two lines is the memorizing.",
    21, "Training error falls forever; test error turns around.",
    [{"at": 0.1, "event": "axes: degree 1 to 7"},
     {"at": 0.3, "event": "train line descends to 0.000"},
     {"at": 0.55, "event": "test line stays flat then climbs to 0.221"},
     {"at": 0.85, "event": "the gap at degree 7 is marked"}],
    "B05_Sweep", "Two lines parting is the claim."))

beats.append(man("B06", "more data",
    "The fix is not always a simpler model. Give the degree seven curve forty points instead of eight. Training error becomes point oh three five. Test error drops from point two two one to point oh six six. More data starves the memorizing.",
    19, "More data shrinks the gap for the same flexible model.",
    [{"at": 0.15, "event": "8-point bars: train 0.000, test 0.221"},
     {"at": 0.55, "event": "bars morph to 40 points: train 0.035, test 0.066"}],
    "B06_MoreData", "Bars morphing as the data grows is the claim."))

beats.append(man("B07", "where it bites",
    "Where it bites. Even a perfect model can't beat the noise in the data. Here, about point oh six two five. Degree one's test error is point oh seven four. Degree seven's is point two two one. A training error of zero sits below that floor. That should worry you, not please you.",
    21, "Noise sets a floor; zero training error sits below it.",
    [{"at": 0.1, "event": "three test-error bars: degree 1, 3, 7"},
     {"at": 0.5, "event": "noise floor line at 0.0625"},
     {"at": 0.8, "event": "degree 7 bar turns terracotta"}],
    "B07_Floor", "A tall bar against a low floor line is the claim."))

beats.append(card("BVDT", "verdict",
    "Let's recap with Claude. Training error always falls as the model gets more flexible. Test error falls, then rises: a line scores point oh seven four, degree seven scores point two two one. A perfect training score can mean memorized noise, and the gap between the two errors is the memorizing. More data shrinks the gap. And noise sets a floor, so a training error below it is a warning.",
    36,
    rem("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": "Overfitting, in six lines",
        "artifactLines": [
            "Training error always falls as the model gets more flexible.",
            "Test error falls, then rises: 0.074 at degree 1, 0.221 at degree 7.",
            "A perfect training score can mean memorized noise.",
            "The gap between training and test error is the memorizing.",
            "More data shrinks the gap: 8 to 40 points cut test error 0.221 to 0.066.",
            "Noise sets a floor (about 0.0625); a training error below it is a warning."]},
        [{"at": 0.0, "event": "artifact page opens"},
         {"at": 0.2, "event": "six verdict lines land in narration order"}]),
    lead_silence_s=0.5, qc="Mandated ClaudeVerdictArtifact bookend."))

PROMPT = ("Write a short Python script, numpy only, that draws 8 noisy points from y = 2x with noise standard "
          "deviation 0.25, fits polynomials of degree 1 to 7, and prints the training error and the test error "
          "on 200 fresh points for each degree. Before running it, predict which degree has the lowest test error "
          "and why. Then repeat with 40 training points.")
beats.append(card("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + PROMPT +
    " Here's what to check. Training error should fall to nearly zero by degree seven, while test error ends up several times larger. The lowest test error should sit at a low degree, since the true pattern is a straight line. With forty points, the degree seven test error should come down close to the noise floor. And see whether Claude explains why, rather than just printing the table.",
    58,
    rem("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "OVERFITTING · YOUR TURN",
        "segment": "Catch The Memorizer", "command": PROMPT,
        "runningText": "paste this into Claude…", "folderLabel": FOLDER,
        "modelLabel": "Fable 5", "effortLabel": "High",
        "output": ["Check: training error is about 0 at degree 7; test error is several times larger.",
                   "Check: the lowest test error sits at a low degree.",
                   "Check: with 40 points the degree 7 test error falls near the noise floor."]},
        [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
         {"at": 0.1, "event": "the prompt types in full"},
         {"at": 0.78, "event": "three check lines land"}])))

beats.append(card("BOUT", "outro", TITLE + ". At Nik Bear Brown.", 6,
    rem("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": FOLDER, "subline": ""},
        [{"at": 0.0, "event": "title restates; handle; slug-seeded mascot; Liam reads the title then 'At Nik Bear Brown'"}]),
    kind="outro_voice", tail_silence_s=1.0,
    hold_note="spoken outro + 1.0 s silent tail (apad); no jingle (OUTRO-LOCK §Voice)"))

meta = {
    "slug": SLUG, "title": TITLE, "topic": "MACHINE LEARNING · OVERFITTING",
    "skill": "ai-explainer", "style_preset": "claude", "brand": "claude-liam", "channel": "claude-liam",
    "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160, "caption_policy": "none",
    "audience": "a smart reader who wants to know why a perfect training score can hide a worse model",
    "greeting": "Hi, Liam", "greeting_note": "hello lexicon: Hindi. Wagwan is Bear's.",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "math_route": "no typeset equations in this film",
    "note": "Series film 1 of 6 after claude-liam-cross-entropy: same ai-explainer spine, numbers from experiment.py.",
    "tags": ["overfitting", "generalization", "machine learning", "Claude", "Nik Bear Brown"],
}

if os.path.exists(OUT):
    old = {b["beat_id"]: b for b in json.load(open(OUT))["beats"]}
    for b in beats:
        for k in ("audio_file", "actual_duration_s"):
            if k in old.get(b["beat_id"], {}):
                b[k] = old[b["beat_id"]][k]
for b in beats:
    act, est = b.get("actual_duration_s"), b["estimated_duration_s"]
    props = (b["shot"].get("remotion") or {}).get("props")
    if act and props is not None and "durationSeconds" in props:
        props["durationSeconds"] = round(act, 2)
json.dump({"metadata": meta, "beats": beats}, open(OUT, "w"), indent=1, ensure_ascii=False)
print("wrote", OUT, {b["beat_id"]: len(b["narration_text"].split()) for b in beats})
