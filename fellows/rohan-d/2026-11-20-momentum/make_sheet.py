#!/usr/bin/env python3
"""Builds beat_sheet.json for claude-liam-momentum (ai-explainer spine, Liam in for Bear)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "beat_sheet.json")
SLUG = "claude-liam-momentum"
TITLE = "Momentum, One Remembered Step at a Time"
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
    "Hi, this is Liam, in for Bear. The ask: why does adding momentum make gradient descent faster? Show me with real numbers. Momentum keeps a running memory of past slopes. The zigzags cancel, and the steady direction builds. A little more than halves the steps. Too much overshoots.",
    24,
    rem("ClaudeComposerAsk", {
        "greeting": "Hi, Liam", "topic": "MACHINE LEARNING · MOMENTUM",
        "segment": TITLE,
        "command": "Why does adding momentum make gradient descent faster? Show me with real numbers.",
        "runningText": "working through the math…", "folderLabel": FOLDER,
        "output": ["Working through the math…",
                   "the trick: keep a running memory of past slopes so zigzags cancel and the steady direction builds",
                   "worked example: a narrow valley from (4, 1): plain descent 47 steps, momentum 0.5 takes 20",
                   "where it bites: too much memory overshoots, 0.9 takes 53 steps and 0.99 never settles"]},
        [{"at": 0.0, "event": "the ask types into the composer"},
         {"at": 0.45, "event": "result lines land one by one"}]),
    qc="Cold-open composer: the ask and its result lines are the motion."))

beats.append(card("B01", "overview",
    "Momentum cancels the zigzag. It doesn't just add speed. It remembers where the slopes pointed, so the steps that disagree cancel, and the steps that agree add up.",
    13,
    rem("BrutalistHesitantWriter", {
        "text": "Momentum\njust adds speed.",
        "triggerWords": "just adds speed",
        "replacementWords": "cancels the zigzag",
        "fontSize": 140, "charMs": 26, "hesitateBetween": 8, "hesitateWithin": 1,
        "mistakeRate": 5, "jitter": 20, "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types the naive framing"},
         {"at": 0.45, "event": "backspaces 'just adds speed' and writes 'cancels the zigzag'"}]),
    lead_silence_s=0.8,
    motion_claim="The writer types the naive framing and corrects it on the spoken word.",
    qc="Hesitant-writer overview: the correction is the motion."))

beats.append(man("B02", "the valley",
    "Here is a narrow valley. Start at four, one. Plain gradient descent steps against the slope. Across the valley the slope is steep, so it overshoots and bounces from side to side, while creeping along the floor. Forty-seven steps to get the loss under point oh one.",
    20, "Plain descent bounces across a narrow valley and crawls along it.",
    [{"at": 0.1, "event": "elliptical valley contours"},
     {"at": 0.3, "event": "start point (4, 1); the zigzag path appears step by step"},
     {"at": 0.8, "event": "readout: plain 47 steps"}],
    "B02_Valley", "The path bouncing from side to side is the claim."))

beats.append(man("B03", "the memory",
    "Momentum keeps a memory. Call it v. Each step, v becomes beta times the old v, plus the new slope. Then move against v, not against the slope. Beta zero is plain descent. Beta point eight remembers roughly the last five slopes.",
    18, "Two lines define momentum.",
    [{"at": 0.15, "event": "v update equation writes in"},
     {"at": 0.45, "event": "position update equation writes in"},
     {"at": 0.75, "event": "beta 0 = plain descent; beta 0.8 = last 5 slopes"}],
    "B03_Rule", "The two equations landing in order is the claim."))

beats.append(man("B04", "same start",
    "Same start, same step size, beta point five. The first steps still zigzag, but the sideways motion fades while the forward motion builds. Twenty steps, instead of forty-seven.",
    13, "Momentum reaches the bottom in 20 steps instead of 47.",
    [{"at": 0.1, "event": "valley with the plain path faint"},
     {"at": 0.3, "event": "momentum path draws from the same start"},
     {"at": 0.8, "event": "readout: plain 47 · momentum 20"}],
    "B04_Faster", "Two paths from one start is the claim."))

beats.append(man("B05", "why it works",
    "Why does it work? Look at the numbers. Across the valley, the slope swings: twenty-five, minus nineteen, minus eight, eleven. The velocity swings less. Along the valley the slope keeps its sign, so the velocity grows, from four to over six.",
    22, "Swings cancel across the valley; steady slopes add up along it.",
    [{"at": 0.1, "event": "two panels: across the valley / along the valley"},
     {"at": 0.35, "event": "slope bars (grey) then velocity bars (ink), steps 1-5, across"},
     {"at": 0.7, "event": "same for along: velocity grows"}],
    "B05_Cancel", "Smaller swing bars across, taller bars along, is the claim."))

beats.append(man("B06", "how much memory",
    "How much memory is right? Count the steps to get the loss under point oh one. Beta zero, forty-seven. Point five, twenty. Point eight, twenty-nine. Point nine, fifty-three. Point nine five, ninety-nine. Point nine nine never gets there in two hundred steps.",
    21, "More memory is not always faster.",
    [{"at": 0.1, "event": "six rows, one per beta"},
     {"at": 0.3, "event": "bars grow row by row: 47, 20, 29, 53, 99, 200+"},
     {"at": 0.85, "event": "beta 0.5 turns terracotta"}],
    "B06_Sweep", "A bar that shrinks then grows again is the claim."))

beats.append(man("B07", "where it bites",
    "Where it bites. Too much memory and the ball overshoots. With beta point nine, x swings to minus two point two at step eleven, before coming back. With point nine nine, it is still swinging at step two hundred, with a loss of one point one.",
    21, "A heavy ball overshoots; the 0.99 run is still swinging at step 200.",
    [{"at": 0.1, "event": "x against step for beta 0.5 (grey) and 0.9 (ink)"},
     {"at": 0.5, "event": "dip to -2.17 at step 11 marked"},
     {"at": 0.8, "event": "readout: beta 0.99, loss 1.1 at step 200"}],
    "B07_Overshoot", "The curve crossing below zero is the claim."))

beats.append(card("BVDT", "verdict",
    "Let's recap with Claude. Momentum keeps a running memory of past slopes. Each step v becomes beta times the old v plus the new slope, and the move goes against v. Zigzags cancel and steady directions add up. With beta point five the valley takes twenty steps, plain descent takes forty-seven. More memory is not better: point nine takes fifty-three. And at point nine nine, it is still swinging after two hundred steps.",
    36,
    rem("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": "Momentum, in six lines",
        "artifactLines": [
            "Momentum keeps a running memory v of past slopes.",
            "v becomes beta times the old v plus the new slope; move against v.",
            "Zigzags cancel and steady directions add up.",
            "Beta 0.5 reaches loss 0.01 in 20 steps; plain descent needs 47.",
            "More memory is not better: beta 0.9 needs 53 steps.",
            "At beta 0.99 it is still swinging after 200 steps (loss 1.1)."]},
        [{"at": 0.0, "event": "artifact page opens"},
         {"at": 0.2, "event": "six verdict lines land in narration order"}]),
    lead_silence_s=0.5, qc="Mandated ClaudeVerdictArtifact bookend."))

PROMPT = ("Write a short Python script, no ML libraries, that runs gradient descent with momentum on loss = 0.5 * "
          "(x squared + 25 y squared), starting at x = 4 and y = 1, with step size 0.07. Each step, set v = beta * v + "
          "gradient, then subtract step size times v. Try beta = 0, 0.5, 0.9 and 0.99, and print how many steps each "
          "needs to get the loss below 0.01. Before running it, predict which beta wins.")
beats.append(card("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + PROMPT +
    " Here's what to check. Beta zero should take forty-seven steps and beta point five twenty. Beta point nine should take fifty-three, and point nine nine should not finish in two hundred. And see whether Claude explains why more momentum is not always faster, rather than just printing the counts.",
    58,
    rem("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "MOMENTUM · YOUR TURN",
        "segment": "Race The Betas", "command": PROMPT,
        "runningText": "paste this into Claude…", "folderLabel": FOLDER,
        "modelLabel": "Fable 5", "effortLabel": "High",
        "output": ["Check: beta 0 takes 47 steps and beta 0.5 takes 20.",
                   "Check: beta 0.9 takes 53 steps; beta 0.99 does not finish in 200.",
                   "Check: Claude explains why more momentum is not always faster."]},
        [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
         {"at": 0.1, "event": "the prompt types in full"},
         {"at": 0.78, "event": "three check lines land"}])))

beats.append(card("BOUT", "outro", TITLE + ". At Nik Bear Brown.", 6,
    rem("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": FOLDER, "subline": ""},
        [{"at": 0.0, "event": "title restates; handle; slug-seeded mascot; Liam reads the title then 'At Nik Bear Brown'"}]),
    kind="outro_voice", tail_silence_s=1.0,
    hold_note="spoken outro + 1.0 s silent tail (apad); no jingle (OUTRO-LOCK §Voice)"))

meta = {
    "slug": SLUG, "title": TITLE, "topic": "MACHINE LEARNING · MOMENTUM",
    "skill": "ai-explainer", "style_preset": "claude", "brand": "claude-liam", "channel": "claude-liam",
    "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160, "caption_policy": "none",
    "audience": "a smart reader who has seen gradient descent and wants to know why momentum helps",
    "greeting": "Hi, Liam", "greeting_note": "hello lexicon: Hindi. Wagwan is Bear's.",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "math_route": "MathText SVG (typeset_math.py); Manim MathTex unavailable (no dvisvgm)",
    "note": "Series film 2 of 6 after claude-liam-cross-entropy: same ai-explainer spine, numbers from experiment.py.",
    "tags": ["momentum", "generalization", "machine learning", "Claude", "Nik Bear Brown"],
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
