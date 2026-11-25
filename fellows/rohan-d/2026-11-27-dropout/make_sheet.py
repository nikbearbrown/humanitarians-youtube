#!/usr/bin/env python3
"""Builds beat_sheet.json for claude-liam-dropout (ai-explainer spine, Liam in for Bear)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "beat_sheet.json")
SLUG = "claude-liam-dropout"
TITLE = "Dropout, One Silenced Unit at a Time"
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
    "Hi, this is Liam, in for Bear. The ask: why does randomly switching off neurons during training help, and why scale the ones that survive? Show me with real numbers. Silence each unit with some probability. Scale the survivors up. The average output stays put, and no unit can lean on a neighbor.",
    24,
    rem("ClaudeComposerAsk", {
        "greeting": "Hi, Liam", "topic": "MACHINE LEARNING · DROPOUT",
        "segment": TITLE,
        "command": "Why does randomly switching off neurons during training help, and why scale the ones that survive? Show me with real numbers.",
        "runningText": "working through the math…", "folderLabel": FOLDER,
        "output": ["Working through the math…",
                   "the trick: silence each unit at random and scale the survivors by 1 over (1 minus p)",
                   "worked example: 8 units summing to 36: one mask gives 38, 10,000 masks average 35.98",
                   "where it bites: at p = 0.9 the output wobbles by 43 instead of 14"]},
        [{"at": 0.0, "event": "the ask types into the composer"},
         {"at": 0.45, "event": "result lines land one by one"}]),
    qc="Cold-open composer: the ask and its result lines are the motion."))

beats.append(card("B01", "overview",
    "Dropout trains many networks. Each random mask picks a thinned copy that shares the same weights. Training on all of them at once is what keeps any one unit from being relied on.",
    14,
    rem("BrutalistHesitantWriter", {
        "text": "Dropout\nbreaks the network.",
        "triggerWords": "breaks the network",
        "replacementWords": "trains many networks",
        "fontSize": 140, "charMs": 26, "hesitateBetween": 8, "hesitateWithin": 1,
        "mistakeRate": 5, "jitter": 20, "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types the naive framing"},
         {"at": 0.45, "event": "backspaces 'breaks the network' and writes 'trains many networks'"}]),
    lead_silence_s=0.8,
    motion_claim="The writer types the naive framing and corrects it on the spoken word.",
    qc="Hesitant-writer overview: the correction is the motion."))

beats.append(man("B02", "one mask",
    "Eight units, with activations one to eight. They add up to thirty-six. Now flip a coin for each unit. Heads, keep it. Tails, silence it. This mask keeps units one, five, six and seven. Their sum is nineteen.",
    17, "A random mask silences four of eight units.",
    [{"at": 0.1, "event": "eight bars, values 1 to 8"},
     {"at": 0.5, "event": "units 2, 3, 4, 8 become hollow"},
     {"at": 0.8, "event": "readout: kept 1 + 5 + 6 + 7 = 19"}],
    "B02_Mask", "Bars turning hollow is the claim."))

beats.append(man("B03", "scale up",
    "Silencing half the units cuts the sum in half. So scale the survivors up by two. Nineteen becomes thirty-eight. One mask, one answer, near the thirty-six we would get with every unit.",
    15, "Survivors double; the output is 38.",
    [{"at": 0.15, "event": "the four kept bars double in height"},
     {"at": 0.7, "event": "readout: 19 x 2 = 38"}],
    "B03_Scale", "The kept bars doubling is the claim."))

beats.append(man("B04", "many masks",
    "Draw five more masks. The outputs jump around: eighteen, forty, forty-four, twenty-two, twenty-eight. Any single mask is noisy. Now draw ten thousand. The average is thirty-five point nine eight. The noise averages away.",
    19, "Five noisy outputs around 36; 10,000 average 35.98.",
    [{"at": 0.1, "event": "five bars grow: 18, 40, 44, 22, 28"},
     {"at": 0.4, "event": "dashed line at 36"},
     {"at": 0.8, "event": "readout: 10,000 masks: 35.98"}],
    "B04_Average", "Bars scattering around a dashed line is the claim."))

beats.append(man("B05", "why scale",
    "Why scale? Without it, the average output is eighteen, half the truth. With the factor of two, it's thirty-six, the same as with no dropout. Scaling is what keeps the expected output unchanged.",
    15, "Unscaled average 18; scaled average 36.",
    [{"at": 0.15, "event": "two bars: no scaling 18.0, scaled 36.0"},
     {"at": 0.5, "event": "dashed line at 36"}],
    "B05_WhyScale", "A short bar beside a tall bar is the claim."))

beats.append(man("B06", "256 networks",
    "Count the masks. Eight units, two choices each: two to the eighth, two hundred fifty-six thinned networks, all sharing one set of weights. For a plain sum like this one, averaging all two hundred fifty-six gives exactly thirty-six. At test time, you skip the masks and use the full network. That is the average.",
    24, "256 masks, one set of weights.",
    [{"at": 0.1, "event": "16 by 16 grid of masks appears"},
     {"at": 0.5, "event": "readouts: 256 masks, one set of weights"},
     {"at": 0.8, "event": "readout: average 36.0"}],
    "B06_Crowd", "The 256-cell grid is the claim."))

beats.append(man("B07", "where it bites",
    "Where it bites. Dropout adds noise. At drop probability point one, the output wobbles by about five. At point five, fourteen. At point nine, forty-three, more than the answer itself. And forget to switch it off at test time, and the same input gives a different answer every run.",
    22, "Noise grows with the drop probability.",
    [{"at": 0.1, "event": "three bars: p 0.1 -> 4.76, p 0.5 -> 14.28, p 0.9 -> 42.85"},
     {"at": 0.75, "event": "reminder: no dropout at test time"}],
    "B07_Noise", "Bars growing with p is the claim."))

beats.append(card("BVDT", "verdict",
    "Let's recap with Claude. Dropout silences each unit with probability p during training. Survivors are scaled by one over one minus p, so the average output stays at thirty-six. One mask gives thirty-eight, and ten thousand average thirty-five point nine eight. Eight units give two hundred fifty-six thinned networks that share one set of weights. Noise grows with p. And at test time, dropout is switched off.",
    32,
    rem("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": "Dropout, in six lines",
        "artifactLines": [
            "Dropout silences each unit with probability p during training.",
            "Survivors are scaled by 1/(1 − p), so the average output stays at 36.",
            "One mask gives 38; 10,000 masks average 35.98.",
            "8 units give 256 thinned networks that share one set of weights.",
            "Noise grows with p: the output wobbles by 4.8, 14.3 and 42.9 at p = 0.1, 0.5, 0.9.",
            "At test time dropout is switched off, or answers change from run to run."]},
        [{"at": 0.0, "event": "artifact page opens"},
         {"at": 0.2, "event": "six verdict lines land in narration order"}]),
    lead_silence_s=0.5, qc="Mandated ClaudeVerdictArtifact bookend."))

PROMPT = ("Write a short Python script, numpy only, that applies dropout to the activations 1 through 8: keep each unit "
          "with probability 1 minus p, scale the survivors by 1 over 1 minus p, then sum. Run it on 10,000 random masks "
          "and print the mean and the standard deviation of the sum, for p = 0.1, 0.5 and 0.9. Predict the means before "
          "you run it.")
beats.append(card("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + PROMPT +
    " Here's what to check. The mean should be about thirty-six for every p. The standard deviation should be about four point eight, fourteen point three, and forty-three. And see whether Claude explains why the mean does not move while the noise grows.",
    52,
    rem("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "DROPOUT · YOUR TURN",
        "segment": "Silence The Units", "command": PROMPT,
        "runningText": "paste this into Claude…", "folderLabel": FOLDER,
        "modelLabel": "Fable 5", "effortLabel": "High",
        "output": ["Check: the mean is about 36 for every p.",
                   "Check: the standard deviation is about 4.8, 14.3 and 42.9.",
                   "Check: Claude explains why the mean holds while the noise grows."]},
        [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
         {"at": 0.1, "event": "the prompt types in full"},
         {"at": 0.78, "event": "three check lines land"}])))

beats.append(card("BOUT", "outro", TITLE + ". At Nik Bear Brown.", 6,
    rem("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": FOLDER, "subline": ""},
        [{"at": 0.0, "event": "title restates; handle; slug-seeded mascot; Liam reads the title then 'At Nik Bear Brown'"}]),
    kind="outro_voice", tail_silence_s=1.0,
    hold_note="spoken outro + 1.0 s silent tail (apad); no jingle (OUTRO-LOCK §Voice)"))

meta = {
    "slug": SLUG, "title": TITLE, "topic": "MACHINE LEARNING · DROPOUT",
    "skill": "ai-explainer", "style_preset": "claude", "brand": "claude-liam", "channel": "claude-liam",
    "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160, "caption_policy": "none",
    "audience": "a smart reader who wants to know how dropout finds groups and why its start matters",
    "greeting": "Hi, Liam", "greeting_note": "hello lexicon: Hindi. Wagwan is Bear's.",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "math_route": "no typeset equations in this film",
    "note": "Extra film after the series of six after claude-liam-cross-entropy: same ai-explainer spine, numbers from experiment.py.",
    "tags": ["dropout", "generalization", "machine learning", "Claude", "Nik Bear Brown"],
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
