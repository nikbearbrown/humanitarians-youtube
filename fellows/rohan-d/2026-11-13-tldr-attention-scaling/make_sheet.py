#!/usr/bin/env python3
"""Builds beat_sheet.json for tldr-attention-scaling. Re-running keeps audio_file /
actual_duration_s from an existing sheet (audio is the clock)."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "beat_sheet.json")
SLUG = "tldr-attention-scaling"
TITLE = "Why Attention Divides By The Square Root"
VOICE = dict(voice="am_onyx", engine="kokoro")

def rem(pattern, props, show):
    return {"type": "REMOTION", "source": "own", "show": show,
            "remotion": {"pattern": pattern, "props": props}}

def bookend(bid, act, narr, est, shot, proof="SHOW", qc=None, **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": proof,
         "narration_text": narr, "estimated_duration_s": est, **VOICE, "shot": shot}
    b.update(extra)
    if qc:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": qc}
    return b

def learn(bid, role, narr, est, q, a, o, i, nxt, intent, show, cls, claim, **extra):
    b = {"beat_id": bid, "act": "learn 1", "section": 1, "role": role, "lane": "manim",
         "proof_gate": "SHOW",
         "learn": {"question": q, "action": a, "observation": o, "inference": i,
                   "next_question": nxt},
         "narration_text": narr, "estimated_duration_s": est, **VOICE,
         "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": intent,
                  "show": show, "manim": {"class": cls}},
         "motion_claim": claim}
    b.update(extra)
    return b

FOLDER = "@NikBearBrown"
beats = []

beats.append(bookend("B00", "tldr · what",
    "Hola. This is Liam, in for Bear. This film is about one small piece of the attention formula: why the scores are divided by the square root of the vector length. Longer vectors make wider scores, and wide scores make the softmax pick a single winner. Dividing by the square root keeps the spread the same at any length. The trap is calling it a detail.",
    24,
    rem("ClaudeTldrWhat", {
        "eyebrow": "TL;DR", "greeting": "Hola, Liam", "topic": "Attention · Machine Learning",
        "question": "Why does attention divide its scores by the square root of the vector length?",
        "lines": ["Longer vectors make wider scores, and wide scores make the softmax pick one winner.",
                  "Dividing by the square root of the length keeps the spread the same at every size.",
                  "The trap: calling it a detail. Without it, almost no learning signal gets through."],
        "cues": [1.2, 7.0, 12.5, 18.0], "durationSeconds": 24, "folderLabel": "",
        "heading": "What This Film Is About"},
        [{"at": 0.0, "event": "'TL;DR.' wordmark lands; 'Hola, Liam' + topic"},
         {"at": 0.06, "event": "the question writes on, word by word"},
         {"at": 0.3, "event": "line 1 lands, terracotta numeral"},
         {"at": 0.55, "event": "line 2 lands; line 1 settles"},
         {"at": 0.78, "event": "line 3 lands"}]),
    qc="TL;DR card one — lines land on the spoken clauses by design; waives only underfill."))

beats.append(bookend("B01", "tldr · why",
    "Why should you care? Every attention layer scores words against each other, and scores that run too wide break it. Nearly all the weight lands on one word. The softmax passes back almost no learning signal. One short division keeps attention a weighted average instead of a vote.",
    20,
    rem("ClaudeTldrWhy", {
        "eyebrow": "TL;DR", "heading": "Why You Should Care", "topic": "Attention · Machine Learning",
        "lead": "Every attention layer scores words against each other, and scores that run too wide break it.",
        "lines": ["Nearly all the weight lands on one word.",
                  "The softmax passes back almost no learning signal.",
                  "One short division keeps attention a weighted average instead of a vote."],
        "cues": [1.0, 7.0, 11.0, 14.5], "durationSeconds": 20, "folderLabel": ""},
        [{"at": 0.0, "event": "page turn: same header, heading 'Why You Should Care'"},
         {"at": 0.08, "event": "the stake writes on"},
         {"at": 0.4, "event": "dash 1 lands"}, {"at": 0.6, "event": "dash 2 lands"},
         {"at": 0.78, "event": "dash 3 lands"}]),
    qc="TL;DR card two — text lands on cues by design."))

beats.append(bookend("B02", "the question",
    "The question this film is really asking: why does attention divide by the square root of the vector length? Not why it divides at all. Why that number, and not one you could simply pick.",
    13,
    rem("BrutalistHesitantWriter", {
        "text": "Why does attention divide its scores\nby a number you could pick by hand?",
        "triggerWords": "a number you could pick by hand",
        "replacementWords": "the square root of the vector length",
        "fontSize": 68, "charMs": 26, "hesitateBetween": 8, "hesitateWithin": 1,
        "mistakeRate": 5, "jitter": 20, "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types the naive question"},
         {"at": 0.4, "event": "backspaces 'a number you could pick by hand' → 'the square root of the vector length' on the spoken correction"},
         {"at": 0.85, "event": "caret holds on the corrected question"}]),
    lead_silence_s=0.8,
    motion_claim="The writer types the naive question and replaces the phrase that makes it the wrong question, on the spoken word.",
    qc="Hesitant-writer bookend: the correction is the motion."))

beats.append(bookend("B03", "terms",
    "Three terms before we start. A dot product multiplies two vectors entry by entry and adds the results into one number. Softmax turns a list of scores into weights that add up to one. Variance measures how spread out numbers are around their average.",
    17,
    rem("ClaudeDefinitions", {
        "title": "Terms In This Film",
        "terms": [
            {"term": "dot product", "meaning": "multiply two vectors entry by entry, then add: one number"},
            {"term": "softmax", "meaning": "turns a list of scores into weights that add up to one"},
            {"term": "variance", "meaning": "how far numbers spread around their average"}],
        "durationSeconds": 17, "folderLabel": ""},
        [{"at": 0.15, "event": "row 1 'dot product' lands, terracotta"},
         {"at": 0.45, "event": "row 2 'softmax' lands; row 1 settles"},
         {"at": 0.75, "event": "row 3 'variance' lands; row 2 settles"}]),
    proof="CARD",
    qc="TERMS card: prerequisites only; the film earns 'scaling' and the square root itself."))

# ---------------- LEARN section 1 (pure Manim) ----------------
beats.append(learn("B10", "HOOK",
    "One word asks a question of six others. Each gets a score, and softmax turns the scores into weights. With short vectors, the weights look sensible. Now keep the recipe and make the vectors five hundred and twelve numbers long. One key takes ninety-nine point six percent.",
    19,
    "Same recipe, longer vectors: why does one key take everything?",
    "Show 6 key bars at length 4, then at length 512.",
    "Sensible weights at 4; one bar at 99.6% at 512.",
    "Something about vector length breaks the softmax.",
    "What is changing as the vectors get longer?",
    "Six bars (keys) with weights from the seeded run; a length readout sweeps 4 → 512 and the bars snap to one-hot.",
    [{"at": 0.1, "event": "six bars at length 4 (0.022 0.054 0.042 0.469 0.105 0.309)"},
     {"at": 0.45, "event": "length readout sweeps to 512 on 'five hundred and twelve'"},
     {"at": 0.85, "event": "bars collapse to one tall bar, '99.6%' lands"}],
    "B10_SixBars",
    "The bars snapping to one winner as the length counter climbs is the claim; the same six bars return in B18."))

beats.append(learn("B11", "INSTANCE",
    "Look at the scores themselves. At four numbers per vector they huddle near zero. At sixteen they spread. At sixty-four, wider. At five hundred and twelve, they run for dozens of units. On average, the biggest weight climbs from fifty-seven percent to ninety-six.",
    19,
    "Is it the spread of the scores?",
    "Sweep the length 4, 16, 64, 512 and plot the six scores as dots on a line.",
    "The dots spread wider each step; the average largest weight climbs 0.574 → 0.961.",
    "Wider scores, more one-sided softmax.",
    "Why does one-sided matter?",
    "Number line with six dots (seeded instance); a length readout steps through four values; a counter shows the average largest weight.",
    [{"at": 0.1, "event": "dots at length 4 huddle near zero"},
     {"at": 0.35, "event": "length steps to 16, 64: dots spread"},
     {"at": 0.65, "event": "length 512: dots span about −17 to 41"},
     {"at": 0.85, "event": "counter reads 0.574 → 0.961"}],
    "B11_ScoresSpread",
    "The dots spreading as length steps up is the claim."))

beats.append(learn("B12", "INSTANCE",
    "Why does a winner-take-all softmax matter? Training needs slope. Where the curve is flat, nudging a score changes nothing. Our rough measure of that slope, the biggest p times one minus p, falls from about point two to under point oh three.",
    17,
    "What does a one-sided softmax cost?",
    "Draw the softmax curve; park the scores on it at each length; read the slope.",
    "Wide scores sit on the flat ends; slope falls 0.203 → 0.0276.",
    "A saturated softmax passes back almost nothing.",
    "Can a simple fix cure it?",
    "Softmax curve with dots parked at length 4, then 512 on its flat ends; a slope readout labelled 'our measure'.",
    [{"at": 0.1, "event": "softmax curve draws"},
     {"at": 0.4, "event": "length-4 dots sit on the steep middle; slope reads 0.203"},
     {"at": 0.7, "event": "length-512 dots slide onto the flat ends; slope reads 0.028"}],
    "B12_FlatEnds",
    "The dots sliding off the slope onto the flat ends is the claim."))

beats.append(learn("B13", "NAIVE",
    "The obvious patch: divide every score by ten. Around sixty-four it looks fine. But at four, the bars go nearly flat. At two thousand and forty-eight, one winner takes most of the weight again. A fixed number fits one vector length.",
    17,
    "Can we just divide by a constant?",
    "Apply a fixed divisor of 10 at lengths 4, 64, 2048.",
    "Largest weight 0.209, 0.368, 0.809 — flat, fine, collapsed.",
    "A constant fits one length only.",
    "What divisor tracks the length?",
    "Three panels of six bars (lengths 4, 64, 2048) after dividing by 10, with the uniform line at 0.167.",
    [{"at": 0.15, "event": "length 4 panel: bars nearly flat, 0.209"},
     {"at": 0.45, "event": "length 64 panel: reasonable, 0.368"},
     {"at": 0.75, "event": "length 2048 panel: one bar tall again, 0.809"}],
    "B13_FixedTen",
    "The same fix landing flat, fine, then collapsed across three lengths is the claim."))

beats.append(learn("B14", "SHIFT",
    "Stop watching the bars. Watch the width of the cloud of scores instead. Length four, the width is two. Sixteen, four. Sixty-four, eight. Every time the length quadruples, the width doubles. Before it moves, commit: what should we divide by?",
    20,
    "How does the spread depend on the length?",
    "Plot the width (standard deviation) against length; hold for the prediction.",
    "Widths 2, 4, 8, 16, 22.6, 45.3 fall on a square-root curve.",
    "The width grows as the square root of the length.",
    "What happens if we divide by that width?",
    "Plot of score-cloud width versus length with six measured points landing on a square-root curve; a HOLD on 'commit'.",
    [{"at": 0.1, "event": "axes: length vs width"},
     {"at": 0.4, "event": "points land at 4,16,64: 2, 4, 8 on the spoken values"},
     {"at": 0.65, "event": "points at 256, 512, 2048 land; the curve draws through all"},
     {"at": 0.85, "event": "HOLD — nothing moves on 'commit'"}],
    "B14_WidthVsLength",
    "The points landing on the curve and then the held frame is the predict-before-reveal beat.",
    predict=True))

beats.append(learn("B15", "TRANSFORM",
    "Divide by the square root, and the wide cloud folds back to the width it had at four. The bars recover.",
    12,
    "What happens when we divide by the width?",
    "Scale the length-512 dot cloud by 1/√512 in place; bars beneath morph.",
    "Cloud width becomes 1; bars go from one-hot to a healthy spread.",
    "Dividing by the square root makes the spread the same at every length.",
    "Why exactly the square root?",
    "The length-512 dots shrink in place onto a width-1 band (same dots, same labels); the six bars beneath morph from one-hot to [0.027 0.356 0.278 0.085 0.103 0.151].",
    [{"at": 0.1, "event": "wide cloud and one-hot bars on stage"},
     {"at": 0.35, "event": "cloud shrinks by 1/√512, dots keep identity"},
     {"at": 0.65, "event": "bars morph to the healthy spread"}],
    "B15_Fold",
    "One continuous morph of the same dots and bars: the section's single aha."))

beats.append(learn("B16", "ABSTRACTION",
    "Now the idea deserves a name. Each score is a sum of d products. Each product has variance one. The variances of independent terms add, so the score has variance d. Divide by the square root of d, and the variance is one again.",
    19,
    "Why is the width exactly the square root of the length?",
    "Write the sum of d products; add their variances; divide.",
    "Var(q·k) = d_k, then Var(q·k / √d_k) = 1.",
    "The square root is what turns variance d back into 1.",
    "What does each symbol stand for?",
    "The width band from B15 turns into the equation: Var(q·k)=d_k, then the divided form; both typeset as MathText SVG, revealed one line at a time.",
    [{"at": 0.15, "event": "'sum of d products' writes under the cloud"},
     {"at": 0.45, "event": "Var(q·k) = d_k lands"},
     {"at": 0.75, "event": "Var(q·k/√d_k) = 1 lands"}],
    "B16_NameIt",
    "The equation arrives as the name for the band just watched."))

beats.append(learn("B17", "TANGENT",
    "Read it as a claim. The left side is how wide the score cloud is, squared. The equals sign says: exactly d, when the entries are independent with variance one. Q and k are random; d is a fixed count. Check at five hundred and twelve: measured variance, about five hundred and thirteen; divided, one.",
    24,
    "What does each symbol mean?",
    "Five-zone tangent: left side as a sentence, the sign as a claim, Role glossary, worked check at 512.",
    "Measured variance 512.65 → 1.00 after dividing.",
    "The relation holds under its stated assumption.",
    "Does it fix our original six bars?",
    "Split stage: equation persists on the main side; side band writes the sentence, the claim, the Role glossary (q, k random variables; d a fixed count) and the d=512 check.",
    [{"at": 0.1, "event": "left-side sentence writes"},
     {"at": 0.35, "event": "'=' read as a claim: 'exactly d, under independence'"},
     {"at": 0.6, "event": "Role glossary rows land, spotlight moving"},
     {"at": 0.85, "event": "check: 512.65 → 1.00"}],
    "B17_ReadIt",
    "The spotlight walking through symbols and the measured check carry the tangent."))

beats.append(learn("B18", "PAYOFF",
    "Back to the six keys at five hundred and twelve. Raw, one key held ninety-nine point six percent. Scaled, the weights spread, from three percent to thirty-six. Attention is a weighted average again, not a vote.",
    17,
    "Did it fix the original six bars?",
    "Return the hook's six bars; show raw beside scaled.",
    "Raw [0, 0.996, 0.004, 0, 0, 0]; scaled [0.027 0.356 0.278 0.085 0.103 0.151].",
    "Scaling restores a weighted average.",
    "",
    "The same six bars as B10: raw one-hot beside the scaled spread, same objects, same labels.",
    [{"at": 0.15, "event": "the hook's six bars return (raw)"},
     {"at": 0.5, "event": "scaled bars grow beside them"},
     {"at": 0.85, "event": "'weighted average' label lands"}],
    "B18_SixBarsBack",
    "The hook's own bars returning resolved closes the loop."))

beats.append(bookend("BVDT", "verdict",
    "Let's recap with Claude. Dot products of longer vectors spread wider. Wide scores saturate the softmax, and a saturated softmax passes back almost no signal. A fixed divisor fits one length only. For random vectors the spread grows as the square root of the length, so dividing by it holds the spread constant.",
    26,
    rem("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": TITLE,
        "artifactLines": [
            "Dot products of longer vectors spread wider.",
            "Wide scores saturate the softmax and starve learning.",
            "A fixed divisor fits one length only.",
            "Dividing by the square root holds the spread constant."]},
        [{"at": 0.0, "event": "artifact page opens"},
         {"at": 0.2, "event": "four verdict lines land in narration order"}]),
    lead_silence_s=0.5, qc="Mandated ClaudeVerdictArtifact bookend."))

PROMPT = ("Write a short Python script that draws random queries and keys with variance 4 instead of 1, "
          "computes the variance of their dot products at vector length 64, and checks whether dividing by "
          "the square root of 64 still gives variance 1. Predict the number before you run it, then say what "
          "divisor would fix it.")
beats.append(bookend("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + PROMPT +
    " Look for two things: did you commit to a number before running it, and is the divisor you named the one that brings the variance back to one.",
    40,
    rem("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "ATTENTION · YOUR TURN",
        "segment": "What If The Entries Are Bigger?", "command": PROMPT,
        "runningText": "paste this into Claude…",
        "output": ["Check: you committed to a number before running the script.",
                   "Check: the divisor you named brings the variance back to 1."],
        "folderLabel": FOLDER, "modelLabel": "Fable 5", "effortLabel": "High"},
        [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
         {"at": 0.1, "event": "the prompt types in full"},
         {"at": 0.78, "event": "two check lines land"}])))

beats.append(bookend("BOUT", "outro", TITLE + ". At Nik Bear Brown.", 6,
    rem("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": FOLDER, "subline": ""},
        [{"at": 0.0, "event": "title restates; handle; slug-seeded mascot; Liam reads the title then 'At Nik Bear Brown'"}]),
    kind="outro_voice", tail_silence_s=1.0,
    hold_note="spoken outro + 1.0 s silent tail (apad); no jingle (OUTRO-LOCK §Voice)"))

meta = {
    "slug": SLUG, "title": TITLE, "topic": "TL;DR · MACHINE LEARNING",
    "skill": "tldr", "style_preset": "tldr", "channel": "claude-liam",
    "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx",
    "engine": "kokoro", "clock": "narration", "palette": "claude", "learn_canvas": "cream",
    "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none",
    "audience": "a smart reader who has heard of Transformers and wants to know why one small division is in the formula",
    "source_doc": "SOURCES.md",
    "sections": [{"n": 1, "title": "Why Divide By The Square Root",
                  "key_case": "one query scored against six keys at vector length 4 versus 512"}],
    "greeting_language": "Spanish (Hola)",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "outro_policy": "OUTRO-LOCK §Voice: spoken title + 'At Nik Bear Brown', 1.0 s silent tail, no jingle.",
    "bookloop_policy": "The film teaches the idea standalone; the source paper is credited in SOURCES.md and in the verdict, not narrated as a lesson reference.",
    "math_route": "MathText SVG (typeset_math.py); Manim MathTex unavailable (no dvisvgm)",
    "tags": ["attention", "transformer", "softmax", "scaling", "3Blue1Brown style", "Claude", "Nik Bear Brown"],
}

# carry audio forward on re-runs
if os.path.exists(OUT):
    old = {b["beat_id"]: b for b in json.load(open(OUT))["beats"]}
    for b in beats:
        o = old.get(b["beat_id"], {})
        for k in ("audio_file", "actual_duration_s"):
            if k in o:
                b[k] = o[k]

# conform Remotion card timing to the measured audio (audio is the clock)
for b in beats:
    act, est = b.get("actual_duration_s"), b["estimated_duration_s"]
    props = (b["shot"].get("remotion") or {}).get("props")
    if act and props is not None:
        if "durationSeconds" in props:
            props["durationSeconds"] = round(act, 2)
        if "cues" in props:
            props["cues"] = [round(c * act / est, 2) for c in props["cues"]]

json.dump({"metadata": meta, "beats": beats}, open(OUT, "w"), indent=1, ensure_ascii=False)
words = {b["beat_id"]: len(b["narration_text"].split()) for b in beats}
print("wrote", OUT, "| beats:", len(beats))
print("words:", words)
