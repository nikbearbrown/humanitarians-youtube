#!/usr/bin/env python3
"""Builds beat_sheet.json for claude-liam-convolution (ai-explainer spine, Liam in for Bear)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "beat_sheet.json")
SLUG = "claude-liam-convolution"
TITLE = "Convolution, One Window at a Time"
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
    "Hi, this is Liam, in for Bear. The ask: how does a convolution find an edge in an image, and why share one small kernel across the whole picture? Show me with real numbers. A kernel is a tiny grid of weights. Slide it over the image, multiply and add. Nine weights find the same pattern everywhere.",
    24,
    rem("ClaudeComposerAsk", {
        "greeting": "Hi, Liam", "topic": "MACHINE LEARNING · CONVOLUTION",
        "segment": TITLE,
        "command": "How does a convolution find an edge in an image, and why share one small kernel across the whole picture? Show me with real numbers.",
        "runningText": "working through the math…", "folderLabel": FOLDER,
        "output": ["Working through the math…",
                   "the trick: slide a small grid of weights over the image, multiply and add at every spot",
                   "worked example: a 3 by 3 edge kernel on a 6 by 6 image gives 0, 27, 27, 0 across the edge",
                   "where it bites: the output shrinks, 6 to 4 to 2, so a third layer will not fit without padding"]},
        [{"at": 0.0, "event": "the ask types into the composer"},
         {"at": 0.45, "event": "result lines land one by one"}]),
    qc="Cold-open composer: the ask and its result lines are the motion."))

beats.append(card("B01", "overview",
    "A convolution slides a small window. It never reads the whole image at once. It looks at one small patch, writes down a single number, and moves over. Then it does that again, everywhere.",
    13,
    rem("BrutalistHesitantWriter", {
        "text": "A convolution\nreads the whole image.",
        "triggerWords": "reads the whole image",
        "replacementWords": "slides a small window",
        "fontSize": 140, "charMs": 26, "hesitateBetween": 8, "hesitateWithin": 1,
        "mistakeRate": 5, "jitter": 20, "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types the naive framing"},
         {"at": 0.45, "event": "backspaces 'reads the whole image' and writes 'slides a small window'"}]),
    lead_silence_s=0.8,
    motion_claim="The writer types the naive framing and corrects it on the spoken word.",
    qc="Hesitant-writer overview: the correction is the motion."))

beats.append(man("B02", "the image",
    "Here is a six by six image. Dark on the left, bright on the right. The edge sits between the third column and the fourth. How would a computer find it? Give it a small grid of weights, a kernel, and slide it across.",
    17, "A six by six image with one vertical edge.",
    [{"at": 0.1, "event": "6x6 grid of pixel values: 0 0 0 9 9 9 in every row"},
     {"at": 0.5, "event": "the edge between column 3 and 4 is marked"},
     {"at": 0.75, "event": "the 3x3 kernel appears: -1 0 1 in every row"}],
    "B02_Image", "The grid and the kernel appearing is the claim."))

beats.append(man("B03", "one window",
    "The kernel is three by three. Left column, minus one. Middle, zero. Right, plus one. Place it on the top left. Multiply each weight by the pixel beneath, and add. The window covers a flat dark patch. The sum is zero.",
    17, "One window: multiply pixel by weight, add.",
    [{"at": 0.1, "event": "kernel weights highlighted column by column"},
     {"at": 0.45, "event": "window lands on the top left of the image"},
     {"at": 0.8, "event": "readout: sum = 0"}],
    "B03_Window", "The window landing on a flat patch and reading zero is the claim."))

beats.append(man("B04", "slide it",
    "Slide it one step right. Now the right column lands on bright pixels. Three nines, twenty-seven. One more step, twenty-seven again. And one more: bright on both sides, nine minus nine, so zero. Zero, twenty-seven, twenty-seven, zero.",
    18, "Sliding the window along the top row fills the output with 0, 27, 27, 0.",
    [{"at": 0.1, "event": "window moves to position 2: sum 27"},
     {"at": 0.4, "event": "position 3: sum 27"},
     {"at": 0.7, "event": "position 4: sum 0; output row 0 27 27 0"}],
    "B04_Slide", "The window moving and the output row filling is the claim."))

beats.append(man("B05", "the map",
    "Do that for every row and you get a four by four map. Zero, twenty-seven, twenty-seven, zero, in every row. The big numbers sit exactly on the edge. The kernel found it.",
    14, "The whole output map lights up along the edge.",
    [{"at": 0.15, "event": "4x4 output grid appears with 0 and 27"},
     {"at": 0.7, "event": "the two columns of 27 turn terracotta"}],
    "B05_Map", "The two bright columns on the edge are the claim."))

beats.append(man("B06", "shared weights",
    "Why share one kernel? Count the weights. To make this four by four map, a layer that connects every input to every output needs thirty-six times sixteen: five hundred seventy-six weights. The convolution uses nine. And move the edge one column left, and the same nine weights find it one place over.",
    22, "Nine shared weights against 576.",
    [{"at": 0.1, "event": "two bars: connect everything 576, one kernel 9"},
     {"at": 0.45, "event": "the 9-weight bar is tiny against 576"},
     {"at": 0.8, "event": "readout: edge moved left, output 27 0 0 0"}],
    "B06_Share", "The tiny bar beside the huge one is the claim."))

beats.append(man("B07", "where it bites",
    "Where it bites. The map is smaller than the image. Six becomes four, four becomes two, and a third three by three kernel no longer fits. Pad the border with zeros and the size stays six.",
    16, "Each unpadded 3x3 layer shrinks the map by two.",
    [{"at": 0.1, "event": "6 by 6 grid"},
     {"at": 0.4, "event": "morphs to 4 by 4, then 2 by 2"},
     {"at": 0.85, "event": "readout: a third kernel does not fit; padding keeps 6"}],
    "B07_Shrink", "The grid shrinking twice is the claim."))

beats.append(card("BVDT", "verdict",
    "Let's recap with Claude. A kernel is a small grid of weights slid across the image. At each spot, multiply and add. The edge kernel gives zero, twenty-seven, twenty-seven, zero across the edge. One kernel of nine weights replaces five hundred seventy-six, and finds the pattern wherever it sits. But each layer shrinks the map by two, so padding keeps the size.",
    34,
    rem("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": "Convolution, in six lines",
        "artifactLines": [
            "A kernel is a small grid of weights slid across the image.",
            "At each spot, multiply each weight by its pixel and add.",
            "The edge kernel gives 0, 27, 27, 0 across the edge.",
            "One kernel of 9 weights replaces 576, and finds the pattern anywhere.",
            "Move the edge and the output moves with it.",
            "Each 3 by 3 layer shrinks the map by 2; zero padding keeps the size."]},
        [{"at": 0.0, "event": "artifact page opens"},
         {"at": 0.2, "event": "six verdict lines land in narration order"}]),
    lead_silence_s=0.5, qc="Mandated ClaudeVerdictArtifact bookend."))

PROMPT = ("Write a short Python script, no ML libraries, that slides the 3 by 3 kernel with columns of minus 1, 0 and 1 "
          "over a 6 by 6 image whose rows are 0, 0, 0, 9, 9, 9, and prints the 4 by 4 output. Predict the output "
          "before you run it. Then move the edge one column left and print the output again. Finally, pad the image "
          "with a border of zeros and print the output size.")
beats.append(card("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + PROMPT +
    " Here's what to check. Every row of the first output should read zero, twenty-seven, twenty-seven, zero. With the edge moved left, it should read twenty-seven, zero, zero, zero. With padding, the output should be six by six. And see whether Claude explains why the edge shows up as two columns of twenty-seven, not one.",
    58,
    rem("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "CONVOLUTION · YOUR TURN",
        "segment": "Slide The Kernel", "command": PROMPT,
        "runningText": "paste this into Claude…", "folderLabel": FOLDER,
        "modelLabel": "Fable 5", "effortLabel": "High",
        "output": ["Check: every output row reads 0, 27, 27, 0.",
                   "Check: with the edge moved left it reads 27, 0, 0, 0.",
                   "Check: with zero padding the output is 6 by 6."]},
        [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
         {"at": 0.1, "event": "the prompt types in full"},
         {"at": 0.78, "event": "three check lines land"}])))

beats.append(card("BOUT", "outro", TITLE + ". At Nik Bear Brown.", 6,
    rem("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": FOLDER, "subline": ""},
        [{"at": 0.0, "event": "title restates; handle; slug-seeded mascot; Liam reads the title then 'At Nik Bear Brown'"}]),
    kind="outro_voice", tail_silence_s=1.0,
    hold_note="spoken outro + 1.0 s silent tail (apad); no jingle (OUTRO-LOCK §Voice)"))

meta = {
    "slug": SLUG, "title": TITLE, "topic": "MACHINE LEARNING · CONVOLUTION",
    "skill": "ai-explainer", "style_preset": "claude", "brand": "claude-liam", "channel": "claude-liam",
    "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160, "caption_policy": "none",
    "audience": "a smart reader who wants to know how a convolution finds an edge and why its kernel is shared",
    "greeting": "Hi, Liam", "greeting_note": "hello lexicon: Hindi. Wagwan is Bear's.",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "math_route": "no typeset equations in this film",
    "note": "Series film 3 of 6 after claude-liam-cross-entropy: same ai-explainer spine, numbers from experiment.py.",
    "tags": ["convolution", "generalization", "machine learning", "Claude", "Nik Bear Brown"],
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
