"""Builds beat_sheet.json (and SCRIPT.md) for "Attention, One Head at a Time" (tldr-attention).

On-screen numbers are read from demo/evidence.json (produced by demo/attention_demo.py), never typed.
Spoken numbers are written as words and checked against the same file by the asserts below.
Re-running this OVERWRITES beat_sheet.json (drops measured audio fields) — rerun audio after.
Durations and B00/B01 cues are PRE-AUDIO ESTIMATES at 3.5 words/s; re-cue from mp3/words.json
after GATE 0.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ev = json.loads((HERE / "demo" / "evidence.json").read_text(encoding="utf-8"))

TITLE = "Attention, One Head at a Time"
SLUG = "tldr-attention"
TOPIC_LINE = "Machine Learning · Transformers"      # on-card course/topic line (Title Case)
WPS = 3.5                                           # Kokoro am_onyx pace measured on film 1

W = ev["words"]                                     # ["cats", "chase", "small", "dogs"]
V = ev["V"]
A2 = ev["weights2"]
O2 = ev["outputs2"]
WK = ev["worked"]
SW = ev["swap"]
SH = ev["shuffle"]
WP = ev["with_position"]
NV = ev["naive_equal"]["outputs"][0]
B2 = ev["blend_two"]["sweep"]
B4 = ev["blend_four"]


def g(x):
    """Number for on-screen text: 2 decimals max, true minus sign."""
    s = f"{x:.2f}".rstrip("0").rstrip(".") if isinstance(x, float) else str(x)
    return s.replace("-", "−")


def vec(v):
    return "(" + ", ".join(g(float(x)) for x in v) + ")"


def row(v):
    return "[" + " ".join(g(x) for x in v) + "]"


# ---- spoken numbers must match the evidence ------------------------------------------
assert WK["query"] == [1, 0, 1, 0]                                   # "one, zero, one, zero"
assert [d["score"] for d in WK["dots"]] == [3, 2, -1, -1]            # "three ... two ... minus one each"
assert A2[1][:2] == [0.53, 0.32] and A2[1][2:] == [0.07, 0.07]       # "zero point five three ..."
assert B2[0]["point"] == [0.0, 0.0] and B2[1]["w"] == 0.8            # "half and half ... zero point eight"
assert ev["match_small"]["scores"] == [0, -3, 2, -1]
assert NV == [0.5, 0.75]
assert SW["kids_key"] == [0, 1, -1, 0] and SW["chase_scores"][0] == -1   # "only minus one against kids'"
assert SW["chase_weights2"][1] == 0.6                                # "mostly back onto chase itself"
assert SH["outputs_permuted_identically"] and SH["max_abs_diff"] < 1e-12
assert WP["cats_moved_by"] > 0.5
assert ev["sizes"]["sqrt_d_k"] == 2.0                                 # "divide each score by two"


def est(narr, lead=0.0):
    return round(len(narr.split()) / WPS + lead + 0.6, 1)


def cue_at(narr, phrase, lead=0.0):
    """Estimated seconds at which `phrase` starts (word index / WPS)."""
    toks = narr.split()
    want = phrase.split()
    for i in range(len(toks) - len(want) + 1):
        if [t.strip(".,:;!?") for t in toks[i:i + len(want)]] == want:
            return round(lead + i / WPS, 1)
    raise KeyError(phrase)


def bookend(bid, act, pattern, props, narration, show, proof="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": proof,
         "narration_text": narration, "estimated_duration_s": est(narration, extra.get("lead_silence_s", 0.0)),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


def learn(bid, role, cls, content_type, lrn, narration, show, visual_intent, motion_claim, **extra):
    b = {"beat_id": bid, "act": "learn 1", "section": 1, "role": role, "lane": "manim",
         "content_type": content_type, "proof_gate": "SHOW", "learn": lrn,
         "narration_text": narration, "estimated_duration_s": est(narration),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": visual_intent, "show": show,
                  "manim": {"class": cls, "file": "scenes.py"}},
         "motion_claim": motion_claim}
    b.update(extra)
    return b


beats = []

# =============================================================== B00 TL;DR · WHAT
n00 = ("Konnichiwa. This is Liam, in for Bear. This film is about attention, the step inside a "
       "transformer where words read each other. Each word's new meaning is a weighted average of what "
       "all the words carry. The weights come from how well two words match. You'll watch one head do it, "
       "with real numbers. The trap: attention blends rather than picks, and on its own it can't see word order.")
d00 = est(n00)
beats.append(bookend("B00", "tldr · what", "ClaudeTldrWhat", {
    "eyebrow": "TL;DR", "heading": "What This Film Is About", "greeting": "Konnichiwa, Liam",
    "topic": TOPIC_LINE,
    "question": "How does a transformer let each word use the words around it?",
    "lines": ["Each word's new meaning is a weighted average of what every word carries.",
              "The weights come from how well two words match. You'll watch one head do it, with real numbers.",
              "The trap: attention blends rather than picks, and on its own it can't see word order."],
    "cues": [cue_at(n00, "This film is about"), cue_at(n00, "Each word's new meaning"),
             cue_at(n00, "The weights come from"), cue_at(n00, "The trap")],
    "durationSeconds": d00, "folderLabel": "@NikBearBrown"},
    n00,
    [{"at": 0.0, "event": "'TL;DR.' wordmark lands (terracotta period); 'Konnichiwa, Liam' + topic line"},
     {"at": 0.12, "event": "the question writes on, word by word, on 'This film is about'"},
     {"at": 0.32, "event": "line 1 lands on 'Each word's new meaning' — numeral 1 terracotta"},
     {"at": 0.53, "event": "line 2 lands on 'The weights come from'; line 1 settles to ink"},
     {"at": 0.78, "event": "line 3 (the trap) lands on 'The trap'"}],
    role_note="TL;DR card one — the point first; Liam signs in (IN-FOR-BEAR)."))

# =============================================================== B01 TL;DR · WHY
n01 = ("Why should you care? Every transformer language model runs this one step, across many heads, "
       "layer after layer. Misread it and you'll picture the model looking up the one right word. "
       "It's actually blending all of them. Work the arithmetic once, and every transformer diagram "
       "stops being boxes. It becomes four moves you can do by hand.")
beats.append(bookend("B01", "tldr · why", "ClaudeTldrWhy", {
    "eyebrow": "TL;DR", "heading": "Why You Should Care", "topic": TOPIC_LINE,
    "lead": "Every transformer language model runs this one step, across many heads, layer after layer.",
    "lines": ["Misread it and you picture a lookup of the one right word. It's a blend of all of them.",
              "Work the arithmetic once and the diagram becomes four moves you can do by hand: project, score, softmax, sum."],
    "cues": [cue_at(n01, "Every transformer"), cue_at(n01, "Misread it"), cue_at(n01, "Work the arithmetic")],
    "durationSeconds": est(n01), "folderLabel": "@NikBearBrown"},
    n01,
    [{"at": 0.0, "event": "page turn: same header, heading 'Why You Should Care'"},
     {"at": 0.08, "event": "the stake writes on, word by word"},
     {"at": 0.36, "event": "dash 1 lands on 'Misread it'"},
     {"at": 0.65, "event": "dash 2 lands on 'Work the arithmetic'"}],
    qc={"sparse_by_design": True, "sparse_reason": "TL;DR card two — text lands on cues by design."}))

# =============================================================== B02 THE QUESTION
n02 = ("The question this film is really asking: how does each word blend the words around it? "
       "Not how it picks the right one. Attention doesn't pick. It mixes, and the mix is the new meaning.")
beats.append(bookend("B02", "the question", "BrutalistHesitantWriter", {
    "text": "How does each word\npick the word it needs?",
    "triggerWords": "pick the word it needs", "replacementWords": "blend the words around it",
    "face": "serif", "fontSize": 72, "charMs": 26, "hesitateBetween": 7, "hesitateWithin": 1,
    "mistakeRate": 5, "jitter": 20, "seed": SLUG, "banner": ""},
    n02,
    [{"at": 0.0, "event": "cream page; caret blinks through the 0.8 s lead silence"},
     {"at": 0.08, "event": "types 'How does each word / pick the word it needs?'"},
     {"at": 0.40, "event": "'pick the word it needs' backspaces → 'blend the words around it' on the spoken correction"},
     {"at": 0.80, "event": "caret holds on the corrected question"}],
    lead_silence_s=0.8,
    motion_claim="The writer types the naive question (a lookup) and replaces the phrase that makes it wrong (a blend), on the spoken word.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}))

# =============================================================== B03 TERMS
n03 = ("Three words you'll hear. An embedding: a list of numbers standing in for a word. A dot product: "
       "multiply matching entries and add them up. It's big when two lists point the same way. Softmax: it "
       "turns a row of scores into positive weights that add up to one.")
beats.append(bookend("B03", "terms", "ClaudeDefinitions", {
    "title": "Terms In This Film",
    "terms": [{"term": "embedding", "meaning": "a list of numbers that stands in for a word"},
              {"term": "dot product", "meaning": "multiply matching entries and add; big when two lists point the same way"},
              {"term": "softmax", "meaning": "turns a row of scores into positive weights that add up to one"}],
    "durationSeconds": est(n03), "folderLabel": "@NikBearBrown"},
    n03,
    [{"at": 0.12, "event": "row 1 'embedding' lands, terracotta"},
     {"at": 0.35, "event": "row 2 'dot product' lands; row 1 settles to ink"},
     {"at": 0.68, "event": "row 3 'softmax' lands; row 2 settles"}],
    proof="CARD",
    qc={"sparse_by_design": True,
        "sparse_reason": "TERMS card: prerequisites only. Query, key, value and attention itself are EARNED in B16, not defined here."}))

# =============================================================== LEARN section 1 (B10–B19)
hook_out, kids_out = O2[1], SW["chase_output2"]
beats.append(learn("B10", "HOOK", "B10_ChaseMoves", "mechanism", {
    "question": "Same word, same numbers in: why does chase come out somewhere else when a neighbour changes?",
    "action": "Run the sentence through one head and follow chase's output; swap cats for kids and run it again.",
    "observation": "Chase's own input row never changes, but its output point moves.",
    "inference": "The output is built from the neighbours, not from chase alone.",
    "next_question": "How do you build one point out of several?"},
    "Four words: cats chase small dogs. Each one goes into an attention head as a list of four numbers. "
    "Follow chase. It comes out as a point, right here. Now swap cats for kids. Chase's own numbers haven't "
    "changed, yet it lands somewhere else. The head only sees these four words. So how do the neighbours get inside chase?",
    [{"at": 0.03, "event": "sentence 'cats chase small dogs' writes across the top; each word's embedding row (mono) lands beneath it: "
                           + "; ".join(f"{w} {row(x)}" for w, x in zip(W, ev['X']))},
     {"at": 0.22, "event": "a plain ink box 'one attention head' draws between the rows and a light value plane on the right"},
     {"at": 0.36, "event": f"chase's row passes through the box; a terracotta dot lands at {vec(hook_out)} on 'right here'"},
     {"at": 0.52, "event": f"'cats' morphs into 'kids'; its row ticks to {row(SW['kids_embedding'])}; chase's row stays put (brief dim box on it)"},
     {"at": 0.66, "event": f"chase's dot glides from {vec(hook_out)} to {vec(kids_out)}; a ghost stays at the first landing"},
     {"at": 0.88, "event": "HOLD on the two landings; dim caption 'toy numbers, not a trained model'"}],
    "Top: the four words with their integer embeddings. Middle: one ink box for the head. Right: a light value plane "
    "(x −2…3, y −3…3) where chase's output lands. The cats→kids swap moves the dot while chase's input stays fixed.",
    "Same input row, two different landings: the gap between what chase's own numbers predict and where it lands IS the section.",
    simplification_caption="toy numbers, not a trained model"))

beats.append(learn("B11", "INSTANCE", "B11_MixingPoints", "mechanism", {
    "question": "How do you build one point out of several?",
    "action": "Give each word a point (a third fixed grid of weights); blend two points with a sweeping weight, then all four.",
    "observation": "The blend slides toward the heavier point and never leaves the shape the points make.",
    "inference": "A weighted average with positive weights that sum to one is a pull toward the heavy points.",
    "next_question": "Who decides the weights?"},
    "Run each word's numbers through a fixed grid of weights, giving each word a point. "
    "Mix two points: some of one, the rest of the other. Half and half lands in the middle. Put zero point "
    "eight on cats, and the mix slides toward cats. With all four, weights adding to one, the mix glides "
    "but never leaves the shape.",
    [{"at": 0.04, "event": "each embedding row slides through a small ink grid labelled 'fixed weights'; four labelled points drop onto the plane: "
                           + "; ".join(f"{w} {vec(v)}" for w, v in zip(W, V))},
     {"at": 0.30, "event": f"segment cats–small draws; blend dot at {vec(B2[0]['point'])} with MathTex label 0.5·cats + 0.5·small"},
     {"at": 0.50, "event": f"weight sweeps to 0.8: the dot slides to {vec(B2[1]['point'])}; label morphs to 0.8·cats + 0.2·small"},
     {"at": 0.68, "event": "ghost quadrilateral outline through the four points; four weight bars appear beside the plane"},
     {"at": 0.78, "event": "bars re-balance three times; the dot glides " + " → ".join(vec(b['point']) for b in B4) + ", staying inside the outline (terracotta dot)"}],
    "Value plane only. One blend dot is the dominant mover; the weight label and four bars are subordinate. Points keep their word labels.",
    "Parametrized instance one: vary the weights, replay the blend; the dot's path stays inside the shape.",
    simplification_caption="two numbers per point so we can draw it; real heads use 64"))

beats.append(learn("B12", "INSTANCE", "B12_RequestMeetsOffer", "mechanism", {
    "question": "Who decides the weights?",
    "action": "Give each word a request and an offer (two more fixed grids); dot chase's request with each offer; then ask from small.",
    "observation": f"Chase's request {row(WK['query'])} scores 3, 2, −1, −1 against the four offers; small's request scores a different row.",
    "inference": "A dot product measures how well one word's request matches another word's offer.",
    "next_question": "Why not skip the scores and weigh everyone equally?"},
    "Who sets the weights? Two more grids give each word two more lists: a request, what it's looking for, and an "
    "offer, what it has. Chase requests one, zero, one, zero. Against cats' offer, multiply matching entries and add: "
    "three. Against its own offer, two. Small and dogs, minus one each. Ask from small instead, and the scores reshuffle.",
    [{"at": 0.05, "event": "two small ink grids; each word gains a 'request' row and an 'offer' row (mono integers)"},
     {"at": 0.30, "event": f"chase's request {row(WK['query'])} lifts out in terracotta"},
     {"at": 0.40, "event": f"it slides beside cats' offer {row(WK['dots'][0]['key'])}; products {row(WK['dots'][0]['products'])} pop out and sum into the chip '3'"},
     {"at": 0.58, "event": "the request slides down the column: chips '2', '−1', '−1' land beside chase, small, dogs"},
     {"at": 0.82, "event": f"small's request {row(ev['match_small']['query'])} replaces chase's; the four chips tick to {row(ev['match_small']['scores'])}"}],
    "Left: the four offer rows stacked. The asking word's request is one moving row that docks against each offer in turn; products fly into a sum chip.",
    "Parametrized instance two: the same dot product replayed down the column, then replayed with a different asker.",
    ))

beats.append(learn("B13", "NAIVE", "B13_EqualWeights", "mechanism", {
    "question": "Why not skip the scores and weigh everyone equally?",
    "action": "Give every word weights of a quarter each and blend all four words at once.",
    "observation": f"All four blends land on one point, {vec(NV)}, the middle of the shape.",
    "inference": "Weights must differ from word to word, or every word means the same thing; the scores have to set them.",
    "next_question": "How do we turn a row of scores into weights?"},
    "Here's the obvious shortcut: skip the scores and weigh every word equally, a quarter each. Watch all four words mix. "
    "Cats, chase, small, dogs: every one lands on the same point, the middle of the shape. Four words, one meaning. "
    "Equal weights erase exactly what made each word itself.",
    [{"at": 0.05, "event": "a 4×4 grid of equal bars '0.25' (one row per word) lands left of the plane"},
     {"at": 0.32, "event": "four blend dots, one per word, start at their own points"},
     {"at": 0.45, "event": f"all four slide together and stack at {vec(NV)} as each word is named"},
     {"at": 0.70, "event": "terracotta box around the single stacked point on 'one meaning'"},
     {"at": 0.88, "event": "dim caption 'equal weights → every word identical'"}],
    "Value plane with four word dots; four moving blend dots that collapse onto the centroid.",
    "The natural wrong turn walked to where it breaks: four movers converge on one point.",
    ))

beats.append(learn("B14", "SHIFT", "B14_HeatMap", "equation", {
    "question": "How do we turn a row of scores into weights?",
    "action": "Score every request against every offer into a 4×4 grid; divide by two; softmax each row. Then ask the viewer to commit.",
    "observation": f"The grid becomes a heat map whose rows are positive and sum to one; chase's row reads {row(A2[1])}.",
    "inference": "The representation is the heat map: row i is exactly the set of blend weights for word i.",
    "next_question": "Where does chase's blend land with those weights?"},
    "So let the scores decide. Put every request against every offer, and you get a grid. Divide each score by two. "
    "Then softmax each row, so it turns positive and adds to one. That's the heat map: who listens to whom. Chase's row "
    "puts zero point five three on cats. Before anything moves, where does chase land?",
    [{"at": 0.04, "event": "4×4 score grid fills (rows = who asks, columns = who offers): "
                           + " / ".join(row(rw) for rw in ev['scores'])},
     {"at": 0.28, "event": "every cell divides by two (MathTex ÷2 chip; cells re-typeset as halves)"},
     {"at": 0.42, "event": "softmax sweeps row by row: cells become weights and shade by size — the heat map: "
                           + " / ".join(row(rw) for rw in A2)},
     {"at": 0.58, "event": "dim caption 'rounded; every row sums to 1'"},
     {"at": 0.72, "event": "chase's row gets a terracotta box; the value plane with the four word points slides in on the right"},
     {"at": 0.85, "event": "HOLD ≥ 2 s: nothing moves on 'where does chase land?'"}],
    "Left: the score grid morphing into the heat map (persistent object, reused in B15/B16/B19). Right: the value plane, waiting.",
    "The representation arrives as a morph of the scores; the beat ends on a still frame for the prediction.",
    predict=True))

beats.append(learn("B15", "TRANSFORM", "B15_LetTheMatchMix", "mechanism", {
    "question": "Where does chase's blend land with those weights?",
    "action": "Chase's heat-map row flies onto the four value points as masses; the blend dot slides into place; then the other three rows fire.",
    "observation": f"Chase lands at {vec(hook_out)} — exactly the HOOK's landing; the other words land at four different points.",
    "inference": "The head's output is the heat-map row used as blend weights: query·key similarity decides the mix.",
    "next_question": "Can we write the whole head down in one line?"},
    "Let the heat map set the mix. Zero point five three toward cats, zero point three two toward itself, a little toward "
    "the rest. There. Exactly where the head put chase. And every other row lands somewhere of its own.",
    [{"at": 0.03, "event": "chase's heat-map row lifts off the grid; its four cells fly to cats, chase, small, dogs and become dot masses (radius ∝ weight)"},
     {"at": 0.30, "event": "four pull lines from a blend dot to the points; the dot slides from the centre toward cats"},
     {"at": 0.52, "event": f"the dot settles at {vec(hook_out)} — onto the HOOK's ghost landing, which flashes terracotta on 'There'"},
     {"at": 0.75, "event": "rows cats, small, dogs fire in quick succession; dots land at "
                           + ", ".join(vec(O2[i]) for i in (0, 2, 3)) + " (contrast: NAIVE's single stack, ghosted)"}],
    "One continuous morph: heat-map cells → masses on the value points → blend dot lands on B10's ghost. Short narration; the motion takes the time.",
    "The collision: the matching thread (heat map) meets the blending thread (value plane) as one morph, landing on the HOOK's point."))

beats.append(learn("B16", "ABSTRACTION", "B16_NameIt", "equation", {
    "question": "Can we write the whole head down in one line?",
    "action": "Name the three lists, stack them into Q, K, V, and morph the score grid and heat map into the equation.",
    "observation": "Each object on screen becomes one symbol: requests → Q, offers → K, points → V, heat map → softmax(·).",
    "inference": "Attention is softmax(QKᵀ/√d_k)V: weights from query·key, applied to values.",
    "next_question": "What does each symbol mean, and why divide by two?"},
    "This thing we keep pointing at deserves a name. The request is the query. The offer is the key. The point a word hands "
    "over is its value. Stack them into grids, Q, K and V, and the whole head is one line: softmax of Q times K transposed, "
    "over root d, times V. That's attention.",
    [{"at": 0.05, "event": "the request rows slide together into a 4×4 grid labelled Q ('query'), terracotta label on 'query'"},
     {"at": 0.20, "event": "offer rows → K ('key'); the word points → a 4×2 grid V ('value')"},
     {"at": 0.45, "event": "Q and K slot into QKᵀ; the ÷2 chip becomes the √d_k denominator; the heat map collapses into softmax( )"},
     {"at": 0.62, "event": "MathTex assembles: Attention(Q, K, V) = softmax(QKᵀ / √d_k) V"},
     {"at": 0.88, "event": "the word 'attention' names it, serif, terracotta"}],
    "Objects morph INTO the notation (not the reverse): Q, K, V are the very grids from B12/B11; the equation is set with MathTex.",
    "The abstraction arrives as an endpoint: every symbol is born from an object the viewer already watched.",
    equation_tex=r"\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\!\left(\frac{QK^{\top}}{\sqrt{d_k}}\right)V"))

e = WK
beats.append(learn("B17", "TANGENT", "B17_Tangent", "equation", {
    "question": "What does each symbol mean, and why divide by two?",
    "action": "Equation persists on the MAIN side; the SIDE band writes LHS/RHS sentences, the '=' claim, a role glossary, chase's worked row, and the values claim.",
    "observation": f"Chase's scores 3, 2, −1, −1 → halved → softmax {row(A2[1])}: the same row the heat map showed.",
    "inference": "The notation is a description of what was watched; √d_k is a design choice that keeps softmax blending.",
    "next_question": "So — why did chase move when cats became kids?"},
    "Read it in words. The left side: what the head hands each word. The right side: score every query against every key, "
    "shrink the scores, turn each row into weights, and blend the values. The equals sign is a promise: same thing, row for row. "
    "Q holds the queries, K the keys, V the values. d k is the length of a key, four here, so we divide by two. For chase: three, two, "
    "minus one, minus one. Halved and softmaxed: zero point five three, zero point three two, zero point zero seven, zero point zero seven. "
    "The division is a design choice: without it, long keys make huge scores, and softmax stops blending and starts picking. Back to chase.",
    [{"at": 0.02, "event": "split stage: the equation holds on the MAIN side; eyebrow 'Equation · tangent' over the SIDE band"},
     {"at": 0.06, "event": "LHS sentence writes; terracotta box around Attention(Q,K,V)"},
     {"at": 0.12, "event": "RHS sentence writes; box moves to softmax(QKᵀ/√d_k)V"},
     {"at": 0.24, "event": "'= : the same thing, row for row' writes; box on '=' (a box, never an underline)"},
     {"at": 0.32, "event": "glossary rows land: Q · matrix · one query per word · 4×4 | K · matrix · one key per word · 4×4 | "
                           "V · matrix · one value per word · 4×2 | d_k · fixed size · key length · 4 | softmax · operator · row → weights · (0,1)"},
     {"at": 0.52, "event": f"worked row (mono): scores {row([d['score'] for d in e['dots']])} → ÷2 {row([d['scaled'] for d in e['dots']])} → weights {row(A2[1])}"},
     {"at": 0.78, "event": f"values claim (tinted box): '÷√d_k is a design choice'; mini-row: without it chase gets {row([round(x, 2) for x in ev['unscaled_focus_row']])}"},
     {"at": 0.95, "event": "re-entry: the side band clears; the equation holds"}],
    "EQUATIONS.md five zones on the split stage; one terracotta box spotlight moves across equation, sentence and glossary row together.",
    "One moving spotlight walks symbol, sentence and number in narration order — the equation tangent template.",
    equation_tex=r"\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\!\left(\frac{QK^{\top}}{\sqrt{d_k}}\right)V",
    tangent_zones={
        "symbolic": "Attention(Q,K,V) = softmax(QKᵀ/√d_k) V",
        "lhs": "What the head hands each word.",
        "rhs": "Score every query against every key, shrink, turn each row into weights, blend the values.",
        "claim": "= : the same thing, row for row.",
        "glossary": [
            {"sym": "Q", "role": "matrix (data)", "mean": "one query per word", "dom": "4×4 here"},
            {"sym": "K", "role": "matrix (data)", "mean": "one key per word", "dom": "4×4 here"},
            {"sym": "V", "role": "matrix (data)", "mean": "one value per word", "dom": "4×2 here"},
            {"sym": "d_k", "role": "fixed size", "mean": "length of a key", "dom": "4 here, so √d_k = 2"},
            {"sym": "softmax", "role": "operator, row by row", "mean": "scores → positive weights summing to 1", "dom": "(0, 1)"}],
        "example": {"scores": [d["score"] for d in e["dots"]], "scaled": [d["scaled"] for d in e["dots"]],
                    "weights": e["weights"], "output": e["output"]},
        "values_claim": "Dividing by √d_k is a design choice: it keeps scores from growing with key length, so softmax keeps blending.",
        "reentry": "Back to chase."}))

beats.append(learn("B18", "PAYOFF", "B18_Payoff", "mechanism", {
    "question": "So — why did chase move when cats became kids?",
    "action": "Bring back the HOOK's dot with pull lines labelled by weight; swap cats for kids again; chase's row re-weights and the dot slides.",
    "observation": f"Chase's request scored 3 against cats' offer but −1 against kids'; the weight drains back onto chase (0.32 → {g(SW['chase_weights2'][1])}).",
    "inference": "The HOOK is resolved: a neighbour changes the output by changing the weights and the values being blended.",
    "next_question": "What can't attention tell, on its own?"},
    "Chase's point is no mystery now: zero point five three of cats, zero point three two of itself, a little "
    "of small and dogs. Swap cats for kids again. Chase's request scored three against cats' offer, but only minus one against kids'. "
    "The weight drains away, mostly back onto chase itself, and the point slides. That was the move.",
    [{"at": 0.04, "event": f"the HOOK's sentence and chase's dot at {vec(hook_out)} return (same objects); four pull lines labelled {row(A2[1])}"},
     {"at": 0.36, "event": f"'cats' → 'kids' again; kids' point appears at {vec(SW['kids_value'])}; cats' point fades to ghost"},
     {"at": 0.55, "event": f"score chip 3 → −1 beside the first column; chase's heat-map row re-shades to {row(SW['chase_weights2'])}"},
     {"at": 0.75, "event": f"the terracotta dot slides to {vec(kids_out)}, onto the HOOK's second ghost landing"}],
    "The HOOK's persistent objects (sentence, dot, ghost landings) resolved with the heat-map row and pull lines.",
    "The mystery replays with its mechanism visible: the same slide as B10, now with the weights that cause it."))

beats.append(learn("B19", "BOUNDARY", "B19_OrderBlind", "mechanism", {
    "question": "What can't attention tell, on its own?",
    "action": "Reorder the sentence to 'dogs chase small cats'; watch the heat map permute and the output points; then add a position signal.",
    "observation": "Rows and columns swap; every word lands on exactly the same point. With position added, cats moves.",
    "inference": "Attention alone is blind to order; position must be added (positional encoding — not taught here).",
    "next_question": ""},
    "Here's what attention can't do on its own. Reorder the sentence: dogs chase small cats. The heat map's rows and columns "
    "swap places, and every word lands on exactly the same point. Attention alone can't tell who chased whom. The original "
    "transformer fixes this by adding a position signal to each word's numbers. With it, cats lands somewhere new.",
    [{"at": 0.06, "event": "'cats' and 'dogs' swap places in the sentence: 'dogs chase small cats'"},
     {"at": 0.25, "event": "the heat map's first and last rows and columns physically swap (cells travel, values unchanged)"},
     {"at": 0.45, "event": f"output dots stay put; terracotta box on cats' dot at {vec(SH['cats_output_before'])} on 'exactly the same point'"},
     {"at": 0.70, "event": "a small dim '+ position' chip slides into each embedding row"},
     {"at": 0.85, "event": f"cats' dot jumps (moved {g(WP['cats_moved_by'])}); dim caption 'positional encoding — not taught here'"}],
    "Sentence + heat map + value plane; the permutation is shown as moving cells, the stillness of the output dots is the claim.",
    "Falsifiability: the shuffle is a real change of meaning that leaves every output point unmoved (executed, max diff 2e−16).",
    ))

# =============================================================== BVDT VERDICT
vl = ["Each word gets a query, a key and a value from three learned grids.",
      "A query dotted with a key scores how well two words match.",
      "Divide by √d_k, softmax each row: that is the heat map.",
      "Each word's output is a weighted average of every value.",
      "Equal weights would make every word the same.",
      "Attention alone can't see order; position has to be added."]
beats.append(bookend("BVDT", "verdict", "ClaudeVerdictArtifact", {
    "artifactTitle": "Verdict", "artifactHeading": TITLE, "artifactLines": vl},
    "Let's recap with Claude. Every word gets a query, a key and a value, from three learned grids. A query against a key, by dot "
    "product, scores how well two words match. Divide by root d k and softmax each row, and you have the heat map. Each word's "
    "output is a weighted average of every value. Weigh them all equally and every word means the same. And attention alone can't "
    "see order, so position has to be added.",
    [{"at": 0.0, "event": "artifact page opens on cream"},
     {"at": 0.12, "event": "heading types"},
     {"at": 0.2, "event": "six verdict lines land in narration order"}],
    lead_silence_s=0.5,
    qc={"sparse_by_design": True, "sparse_reason": "Mandated ClaudeVerdictArtifact bookend."}))

# =============================================================== BHTF YOUR TURN
prompt = ("Write a short Python script, numpy only, for one attention head on a three-word sentence. Use small integer "
          "queries, keys and values that you choose. Before running it, predict which word each word will weight most. "
          "Then print the scores, the softmax weights, and the outputs. Finally, reverse the word order, run it again, "
          "and explain what changed and what didn't.")
beats.append(bookend("BHTF", "your turn", "ClaudeComposerAsk", {
    "greeting": "Your turn.", "topic": "TRANSFORMERS · YOUR TURN", "segment": "Run one head yourself",
    "command": prompt, "runningText": "paste this into Claude…",
    "output": ["check: every row of weights adds up to one",
               "check: the scores are divided by the square root of the key length",
               "check: reversing the words only reorders the outputs, and it says why"],
    "folderLabel": "@NikBearBrown", "modelLabel": "Claude"},
    "Your turn. Paste this into Claude: " + prompt + " Here's what to check. Every row of weights should add up to one. The scores "
    "should be divided by the square root of the key length. And reversing the words should only reorder the outputs. If Claude "
    "says the outputs change, ask it where the position information would come from.",
    [{"at": 0.0, "event": "composer opens — 'Your turn.'"},
     {"at": 0.08, "event": "the prompt types in full as Liam reads it"},
     {"at": 0.62, "event": "runningText 'paste this into Claude…'"},
     {"at": 0.70, "event": "three check lines cascade in as each is spoken"}],
    role_note="HANDOFF — prompt read aloud verbatim (props.command is a substring of narration_text), then a 3-point rubric. "
              "The transfer exercise is the BOUNDARY (order-blindness) on a changed instance."))

# =============================================================== BOUT OUTRO
beats.append(bookend("BOUT", "outro", "ClaudeTitleOutro",
    {"title": TITLE + ".", "handle": "@NikBearBrown", "slug": SLUG, "subline": ""},
    f"{TITLE}. At Nik Bear Brown.",
    [{"at": 0.0, "event": "title restates; handle; slug-seeded mascot. Liam reads the title, then 'At Nik Bear Brown'."}],
    kind="outro_voice", tail_silence_s=1.0,
    hold_note="spoken outro + 1.0 s silent tail; no jingle (OUTRO-LOCK §Voice)"))

# ---- structural asserts -------------------------------------------------------------
ids = [b["beat_id"] for b in beats]
assert ids[:4] == ["B00", "B01", "B02", "B03"] and ids[-3:] == ["BVDT", "BHTF", "BOUT"]
roles = [b.get("role") for b in beats if b.get("section") == 1]
assert roles == ["HOOK", "INSTANCE", "INSTANCE", "NAIVE", "SHIFT", "TRANSFORM", "ABSTRACTION", "TANGENT", "PAYOFF", "BOUNDARY"]
assert all(b["beat_id"] == f"B1{i}" for i, b in enumerate(beats[4:14]))
assert any(b.get("predict") for b in beats[4:9]), "predict beat must precede the TRANSFORM"
assert all(b["learn"]["next_question"] for b in beats[4:13]) and beats[13]["learn"]["next_question"] == ""
assert 20 <= len(n02.split()) <= 35
assert prompt in beats[-2]["narration_text"]
assert beats[-1]["narration_text"] == f"{TITLE}. At Nik Bear Brown."

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "TL;DR · TRANSFORMERS",
    "skill": "tldr", "style_preset": "tldr", "channel": "claude-liam", "brand": "claude-liam",
    "persona": "Liam (in for Bear)", "in_for_bear": True,
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro", "clock": "narration",
    "palette": "claude", "learn_canvas": "cream", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160, "caption_policy": "none",
    "folderLabel": "@NikBearBrown",
    "audience": "a smart learner who has heard 'attention' and 'transformer' and wants the mechanism, with numbers",
    "source_doc": "SOURCE.md (our written source on scaled dot-product attention, after Vaswani et al. 2017); see SOURCES.md",
    "sections_file": "tldr-sections-attention.md",
    "sections": [{"n": 1, "title": "One Head, by Hand",
                  "key_case": "chase in 'cats chase small dogs' lands somewhere new when cats becomes kids"}],
    "greeting": "Konnichiwa, Liam", "greeting_language": "Japanese (Konnichiwa)",
    "evidence": "demo/attention_demo.py -> demo/evidence.json, demo/RUN-LOG.txt (seed 290537)",
    "pronounce": {"Konnichiwa": "kˌoʊniːtʃˈiːwɑː", "numpy": "nˈʌmpaɪ"},
    "outro_policy": "OUTRO-LOCK §Voice: spoken title + 'At Nik Bear Brown', 1.0 s silent tail, no jingle.",
    "bookloop_policy": "The film teaches the idea standalone; no book, chapter or course is named on screen or in narration.",
    "estimate_wps": WPS,
    "tags": ["attention", "transformers", "self-attention", "softmax", "query key value",
             "machine learning", "3Blue1Brown style", "Claude", "Nik Bear Brown"]},
    "beats": beats}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False), encoding="utf-8")

# ---- SCRIPT.md (for the human at the narration gate) --------------------------------
out = [f"# SCRIPT — {TITLE}", "",
       "Narration for review (narration gate), generated from beat_sheet.json by make_sheet.py. "
       f"Durations are estimates at {WPS} words/s (Kokoro am_onyx on film 1); audio has NOT been generated.", ""]
tot_w = tot_s = 0
for b in beats:
    n = len(b["narration_text"].split())
    tot_w += n
    tot_s += b["estimated_duration_s"]
    pat = b["shot"].get("remotion", {}).get("pattern") or b["shot"].get("manim", {}).get("class")
    role = b.get("role") or b["act"].upper()
    flag = "  · PREDICT" if b.get("predict") else ""
    out += [f"## {b['beat_id']} · {role} · {pat}{flag}", "", f"*{n} words · ~{b['estimated_duration_s']} s*", "",
            b["narration_text"], "",
            "*On screen:* " + " → ".join(s["event"] for s in b["shot"]["show"]), ""]
out += [f"**Total: {tot_w} words · ~{tot_s / 60:.1f} min** (sum of per-beat estimates, incl. lead silences and ~0.6 s per beat of sentence pauses).", ""]
(HERE / "SCRIPT.md").write_text("\n".join(out), encoding="utf-8")

for b in beats:
    n = len(b["narration_text"].split())
    print(f"{b['beat_id']:5} {(b.get('role') or b['act']):13} {n:4} words  ~{b['estimated_duration_s']:5.1f}s")
print(f"total {tot_w} words  ~{tot_s:.0f}s = {tot_s / 60:.1f} min ({WPS} w/s)")
