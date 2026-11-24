#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-how-rag-works (film #7 of the STEM/AI series).

SHOW-TELL (Bear, 2026-09-26): one isometric drawing per beat, labels of one to three words,
and Liam's narration carrying the explanation. Spine: BIDEA, BDEFS, B00 hero arrives, B01 it
opens, one step per beat on the same cast, where it fails (executed numbers), why now
(attributed number), BHTF composer, BOUT spoken outro.

The cast, kept for the whole film: a kraft BOX of documents (the handbook), its three PAGES,
paper SLIPS (chunks), the checkpoint SCANNER that stamps each slip with a strip of grey BARS
(its embedding), a DRAWER cabinet (the vector store), a PROMPT sheet, a dark MODEL block, and
an ANSWER card.

Every number on screen or in the narration comes from demo/evidence.json, written by
demo/rag_demo.py (deterministic TF-IDF cosine retrieval in numpy; no models, no APIs). The one
outside number (21 million passages) is attributed aloud and on screen to Lewis et al. 2020.
The answer step is ILLUSTRATED: the demo's "reader" is a regex stand-in, not a language model.
"""
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "show-tell-how-rag-works"
TITLE = "How RAG Works"
WPS = 2.9                       # planning rate (STEM-VIDEO-GUIDE §10); audio is the real clock

EV = json.loads((HERE / "demo" / "evidence.json").read_text(encoding="utf-8"))
F = EV["film"]
A_RANK, B_RANK = EV["runs"]["A"]["ranking"], EV["runs"]["B"]["ranking"]

_WORDS = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
          "6": "six", "7": "seven", "8": "eight", "9": "nine"}


def spoken(x):
    """0.5774 -> 'zero point five eight' (two decimals, read digit by digit)."""
    s = f"{x:.2f}"
    whole, frac = s.split(".")
    return f"{_WORDS[whole]} point " + " ".join(_WORDS[d] for d in frac)


def num(n):
    return {6: "six", 29: "twenty-nine", 30: "thirty", 14: "fourteen", 3: "three"}[n]


def two(x):
    return f"{x:.2f}"


# ── evidence-derived values (asserted, so a changed demo cannot silently change the film) ──
assert F["n_docs"] == 3 and F["n_chunks"] == 6
assert F["A_top"]["id"] == "returns#1" and F["A_second"]["id"] == "warranty#1"
assert F["B_top"]["id"] == "faq-2019#1" and F["B_second"]["id"] == "returns#1"
assert F["A_answer"] == "30 days" and F["B_answer"] == "14 days"
assert EV["runs"]["C"]["ranking"] == A_RANK
DIMS = F["dims"]                                   # 29
A1, A2 = F["A_top"]["score"], F["A_second"]["score"]       # 0.5774, 0.2494
B1, B2 = F["B_stale_score"], F["B_right_score"]            # 0.6204, 0.3846
B3 = B_RANK[2]["score"]                                    # 0.1660
A3 = A_RANK[2]["score"]                                    # 0.0
QUESTION = F["question"]

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, minimal "
                 "labels, the voice carrying the explanation. The negative space is the style, so only underfill and "
                 "clustered are waived; edge-bleed, empty-frame and contrast still apply.")


def est(narration):
    return round(len(narration.split()) / WPS, 1)


def beat(bid, role, narration, cls, image, show, labels, ctype="mechanism", sparse=True):
    b = {"beat_id": bid, "act": "show-tell", "role": role, "lane": "manim", "proof_gate": "SHOW",
         "content_type": ctype, "narration_text": narration, "estimated_duration_s": est(narration),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show,
                  "manim": {"class": cls}, "motion_claim": image, "labels": labels}}
    if sparse:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}
    return b


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", lane="bookend", **extra):
    b = {"beat_id": bid, "act": act, "lane": lane, "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": est(narration),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


def card(bid, role, narration, props, claim, why_card):
    props = {**props, "durationSeconds": max(2.0, est(narration))}   # rewrite from actual_duration_s after audio
    return remotion(bid, "show-tell", narration, "ShowTellCard", props,
                    [{"at": 0.0, "event": f"{props['kind']} card, shot on twos"}], lane="card",
                    role=role, content_type="mechanism", motion_claim=claim, why_card=why_card)


def cue_at(narration, phrase, lo=0.56, hi=0.62):
    """Card move time from the spoken phrase, kept clear of GATE T's 45–55% sample window."""
    f = narration.index(phrase) / len(narration)
    return round(min(hi, max(lo, f - 0.03)), 3)


# ═════════════════════════════════ bookends: open ═════════════════════════════════
OPEN = [
 remotion("BIDEA", "the question",
    "Hallo. This is Liam, in for Bear. A chatbot has never read your own documents. "
    "So the question isn't how the model memorizes your files. It's how it looks them up.",
    "BrutalistHesitantWriter",
    {"text": "How does the model\nmemorize my files?", "triggerWords": "memorize my files", "replacementWords": "look them up",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How does the model'"}, {"at": 0.62, "event": "'memorize my files' → 'look them up' on the spoken correction"}],
    lead_silence_s=0.8, role="IDEA", content_type="title",
    motion_claim="The writer types the naive question (does the model memorize my files?) and corrects it to the real one: it looks them up.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Four terms. RAG, retrieval-augmented generation: look things up first, then write the answer. "
    "A chunk: a short piece cut from a document. An embedding: a list of numbers that stands for a piece of text. "
    "And a vector store: a database that finds the nearest lists of numbers.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "RAG", "meaning": "retrieval-augmented generation: look things up, then answer"},
               {"term": "chunk", "meaning": "a short piece cut from a document"},
               {"term": "embedding", "meaning": "a list of numbers that stands for a piece of text"},
               {"term": "vector store", "meaning": "a database that finds the nearest lists of numbers"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'RAG' lands"}, {"at": 0.38, "event": "'chunk' lands"}, {"at": 0.55, "event": "'embedding' lands"},
     {"at": 0.78, "event": "'vector store' lands"}], gate="CARD", role="TERMS", content_type="structure",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

# ═════════════════════════════════ body: one step per beat ═════════════════════════════════
N_B06 = (f"Step four: the store compares the question's numbers with every chunk's, and returns the closest. "
         f"The returns chunk scores {spoken(A1)}. The warranty chunk shares only the word laptop, so it scores {spoken(A2)}. "
         f"The other four share no words, and score {spoken(A3).replace(' point zero zero', '')}.")
N_B09 = (f"Here's where it fails. Same question, but someone has added an old FAQ page that says {num(14)} days. "
         f"It repeats the question almost word for word, so it now scores {spoken(B1)}, "
         f"and the right chunk drops to second, at {spoken(B2)}.")

BODY = [
 beat("B00", "HERO", "Start with a box of your own documents. Here, it's a small shop's handbook. "
      "The model never saw these pages in training, so on its own, it can only guess what they say.",
      "B00_Handbook", "A taped kraft box drops onto the stage and lands with a floor shadow; 'handbook' beside it. "
      "A faint dashed thought-line from a dark model block at right stops short of the box, ending in a small grey '?' tick.",
      [{"at": 0.1, "event": "box drops in, shadow lands"}, {"at": 0.35, "event": "'handbook' label"},
       {"at": 0.7, "event": "model block slides in at right; dashed line stops short of the box"}],
      ["handbook", "model"], ctype="title"),
 beat("B01", "OPEN", "Open the box, and there are three documents: returns, shipping, and warranty. "
      "RAG doesn't teach the model these pages. It hands the model the right page, at the moment it answers.",
      "B01_ThreePages", "The tape splits and the lid flaps lift; three white pages rise out and fan into a row, one label each.",
      [{"at": 0.08, "event": "tape splits, flaps lift"}, {"at": 0.22, "event": "page 1 rises: 'returns'"},
       {"at": 0.32, "event": "page 2: 'shipping'"}, {"at": 0.42, "event": "page 3: 'warranty'"},
       {"at": 0.75, "event": "one page lifts slightly toward the right edge (the page handed over)"}],
      ["returns", "shipping", "warranty"], ctype="structure"),
 beat("B02", "STEP", f"Step one: cut every document into chunks, short pieces the system can fetch one at a time. "
      f"Each of these documents has two sentences, so each becomes two chunks. {num(6).capitalize()} chunks in all.",
      "B02_Chunks", "A terracotta cut line sweeps across each page in turn; each page separates into two paper slips; "
      "the six slips settle in a row; '6 chunks' beside them.",
      [{"at": 0.15, "event": "cut line sweeps page 1, it splits"}, {"at": 0.3, "event": "pages 2 and 3 split"},
       {"at": 0.62, "event": "six slips line up"}, {"at": 0.85, "event": "'6 chunks' label"}],
      [f"{F['n_chunks']} chunks"]),
 beat("B03", "STEP", f"Step two: turn each chunk into an embedding, a list of numbers. Our toy version counts words, "
      f"with one slot for each of the handbook's {num(DIMS)} key words. Real systems use a trained model, "
      f"so chunks that mean the same thing land close together.",
      "B03_Scanner", "The slips ride a conveyor through a checkpoint scanner; a scan line sweeps each; each slip exits trailing "
      "a strip of grey bars of different heights (its embedding). '29 numbers' beside the strips.",
      [{"at": 0.1, "event": "conveyor + scanner"}, {"at": 0.25, "event": "first slip scanned, bar strip appears"},
       {"at": 0.4, "event": "the rest follow"}, {"at": 0.62, "event": "'29 numbers' label"},
       {"at": 0.8, "event": "two strips with similar bars slide together"}],
      ["embedding", f"{DIMS} numbers"]),
 beat("B04", "STEP", "Step three: file every embedding in a vector store, a database built to find the closest lists "
      "of numbers, fast. This happens once, ahead of time, before anyone asks a thing.",
      "B04_Drawers", "A drawer cabinet stands at right; each bar strip slides into its own drawer, which closes; "
      "one terracotta light per drawer comes on. 'vector store' beside it.",
      [{"at": 0.1, "event": "cabinet appears"}, {"at": 0.25, "event": "strips file into drawers one by one"},
       {"at": 0.7, "event": "drawer lights on; 'vector store'"}],
      ["vector store"]),
 beat("B05", "STEP", f"Now a question arrives. {QUESTION} It goes through the same scanner, so it becomes a list of "
      "numbers too, in the same space as the chunks.",
      "B05_Question", "A slip with a scribbled line and a large ink question mark enters from left, passes the same scanner, "
      "and exits with its own bar strip, edged with a terracotta dot. 'question' beside it.",
      [{"at": 0.1, "event": "question slip enters"}, {"at": 0.45, "event": "scanner sweeps it"},
       {"at": 0.7, "event": "its bar strip appears; 'question'"}],
      ["question"]),
 beat("B06", "STEP", N_B06,
      "B06_Ranking", "The question's bar strip sits on top, the three best chunks' strips below it; dashed guides drop from the "
      "question's two non-zero slots; score bars grow beside each chunk with its executed score (0.58, 0.25, 0.00); "
      "the vector-store cabinet stands at right; a check lands on the top row.",
      [{"at": 0.02, "event": "question strip + 'question'; three chunk strips drop in"},
       {"at": 0.07, "event": "dashed guides from the question's slots (compares)"},
       {"at": 0.31, "event": "returns bar grows: 'within 30 days' 0.58"},
       {"at": 0.56, "event": "warranty bar: 'one year warranty' 0.25"},
       {"at": 0.80, "event": "stub bar: 'receipt and charger' 0.00"},
       {"at": 0.90, "event": "check on the top row"}],
      ["question", "within 30 days", "one year warranty", "receipt and charger", two(A1), two(A2), two(A3)]),
      # 2026-11-23: was a ShowTellCard `search`; GATE T §8.6b read its bordered result rows as text runs
      # enclosing the labels (100% overlap), so B06 is drawn (open bars, no closed rectangles around text).
 beat("B07", "STEP", "Step five: paste the top two chunks into the prompt, above the question, with one instruction: "
      "answer only from these notes, and say so if they don't cover it. Now the facts sit right in front of the model.",
      "B07_Prompt", "Two drawers open; their slips lift out and land on a large prompt sheet, above the question slip; "
      "an instruction scribble draws at the top. 'prompt' beside the sheet.",
      [{"at": 0.1, "event": "two drawers open"}, {"at": 0.25, "event": "slips land on the prompt sheet"},
       {"at": 0.4, "event": "question slip lands below them"}, {"at": 0.7, "event": "instruction scribble draws; 'prompt'"}],
      ["prompt"]),
 beat("B08", "STEP", f"The model reads the prompt and writes a grounded answer: {num(30)} days, from the returns chunk. "
      "Because you know which chunks went in, the answer can point back to its source, and you can check it.",
      "B08_Answer", "The prompt sheet slides into the dark model block; an answer card slides out with a large '30 days'; "
      "a kraft thread draws from the card back to the returns slip; an ink check lands. Small 'illustrated' tag.",
      [{"at": 0.1, "event": "sheet into model"}, {"at": 0.3, "event": "answer card out: '30 days'"},
       {"at": 0.6, "event": "thread back to the returns slip"}, {"at": 0.8, "event": "check lands"}],
      [F["A_answer"], "source", "illustrated"]),
 card("B09", "FAILS", N_B09,
      {"kind": "tabs", "labels": ["Before", "After"], "cues": [cue_at(N_B09, "so it now scores")],
       "items": [{"label": "Returned within 30 days", "value": two(A1)},
                 {"label": "One year warranty", "value": two(A2)},
                 {"label": "Receipt and charger", "value": two(A3)}],
       "items2": [{"label": "2019 FAQ: 14 days", "value": two(B1)},
                  {"label": "Returned within 30 days", "value": two(B2)},
                  {"label": "One year warranty", "value": two(B3)}]},
      "The tab pill slides from Before to After; the ranking is replaced, and the stale FAQ chunk now sits on top.",
      "Card test: (1) the idea is two sets of real executed scores; (2) the tab switch flipping the ranking IS "
      "'one added page changes what ranks first'; (3) the drawers cannot show two rankings side by side with numbers."),
 beat("B10", "FAILS", f"Now the prompt leads with the old chunk. A model told to trust its notes can answer {num(14)} days, "
      "fluently and confidently. Nothing in the writing looks wrong. The mistake happened earlier, at retrieval.",
      "B10_WrongAnswer", "An old, dog-eared page drops into the box; its slip rides the scanner into a drawer; that drawer opens, "
      "the slip lands on top of the prompt sheet; the model pushes out an answer card '14 days'; the thread runs back to the "
      "old slip, and a terracotta ring circles that drawer. Small 'illustrated' tag.",
      [{"at": 0.1, "event": "old page drops in"}, {"at": 0.3, "event": "its slip on top of the prompt"},
       {"at": 0.4, "event": "answer card: '14 days'"}, {"at": 0.72, "event": "ring circles the drawer: 'retrieval'"}],
      [F["B_answer"], "retrieval", "illustrated"]),
 beat("B11", "FIX", f"The fix is in the store, not the model. Take the old page out, and the returns chunk is back on top, "
      f"at {spoken(A1)}. Nobody retrained anything. You changed the pages.",
      "B11_Fix", "The old slip lifts out of its drawer and off the stage; the returns slip rises to the top of the prompt sheet; "
      "the answer card flips back to '30 days'; an ink check lands. The model block never moves.",
      [{"at": 0.12, "event": "old slip lifted out"}, {"at": 0.4, "event": "returns slip back on top"},
       {"at": 0.62, "event": "answer card: '30 days', check"}],
      [F["A_answer"], "store"]),
 beat("B12", "WHY_NOW", "That's the idea behind RAG. In the 2020 paper that named it, Lewis and colleagues gave a model "
      "twenty-one million Wikipedia passages to search, and updated what the model knew by swapping in a newer copy of Wikipedia.",
      "B12_Scale", "The one drawer cabinet multiplies into a long wall of grey cabinets receding in isometric rows; a counter "
      "climbs to '21M'; caption 'per Lewis et al. 2020'; one cabinet slides out and a newer one slides in.",
      [{"at": 0.15, "event": "cabinets multiply"}, {"at": 0.4, "event": "counter climbs to 21M"},
       {"at": 0.55, "event": "caption 'per Lewis et al. 2020'"}, {"at": 0.75, "event": "old cabinet out, newer one in"}],
      ["21M", "per Lewis et al. 2020"]),
]

# ═════════════════════════════════ bookends: close ═════════════════════════════════
YT_PROMPT = ("Here are three short passages from my own notes: [paste them]. And here is my question: [your question]. "
             "Before you answer, rank the passages by how relevant each one is to the question, and say why. "
             "Then answer using only the top passage, and quote the sentence you used.")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things yourself. Does the quoted sentence "
    "really say the answer? And would a newer passage say something different? If it would, the retrieval picked wrong.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Retrieve, Then Answer", "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: the quoted sentence really says the answer.", "Check: no newer passage would change it."],
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"},
     {"at": 0.8, "event": "two check lines land"}],
    role="YOUR_TURN", content_type="structure",
    rubric=["The quoted sentence states the answer itself, not something near it.",
            "No newer or more specific passage in your notes contradicts it; if one does, retrieval picked wrong."])

BOUT = {"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW", "role": "OUTRO",
        "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
        "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                 "remotion": {"pattern": "ClaudeTitleOutro",
                              "props": {"title": TITLE + ".", "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
        "kind": "outro_voice", "tail_silence_s": 1.0}

BEATS = OPEN + BODY + [YOURTURN, BOUT]

# Carry audio forward if make_sheet.py is re-run after GATE 0 (SKILL card-trap 4). Never re-run after `final`.
# It also carries pad_silence.py's `audio_pad` hash, so padded mp3s are not padded twice. It does NOT carry the
# align-derived B09 `cues` (it recomputes them from character share); re-derive from mp3/words.json after a re-run.
_old = HERE / "beat_sheet.json"
if _old.exists():
    try:
        prev = {b["beat_id"]: b for b in json.loads(_old.read_text(encoding="utf-8"))["beats"]}
        for b in BEATS:
            p = prev.get(b["beat_id"], {})
            if p.get("narration_text") == b["narration_text"]:
                for k in ("actual_duration_s", "audio_file", "audio_pad"):
                    if k in p:
                        b[k] = p[k]
                if "actual_duration_s" in b and b["shot"].get("remotion", {}).get("pattern") == "ShowTellCard":
                    b["shot"]["remotion"]["props"]["durationSeconds"] = b["actual_duration_s"]
    except Exception:
        pass

# ── guards: show-tell content rules ──
body = [b for b in BEATS if b["beat_id"].startswith("B") and b["beat_id"][1:].isdigit()]
cards = [b for b in body if b["lane"] == "card"]
assert len(cards) * 3 <= len(body), "at most a third of body beats are cards"
for b in body:
    for lab in b["shot"].get("labels", []):
        assert len(lab.split()) <= 3 or lab.startswith("per "), f"label too long: {b['beat_id']} {lab!r}"
assert YOURTURN["shot"]["remotion"]["props"]["command"] in YOURTURN["narration_text"]

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "AI · RAG", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9",
    "width": 3840, "height": 2160, "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": ("show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear: 'add hesitant "
                              "writer as the first beat and key terms like tldr uses as the second'), no composer cold open and no "
                              "verdict card; Your Turn is the Claude.ai composer; the spoken @NikBearBrown outro stays."),
    "audience": "curious non-specialists and early builders who have heard 'RAG' and want the mechanism",
    "source_doc": ("Lewis et al. 2020, 'Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks' (arXiv:2005.11401, "
                   "NeurIPS 2020); executed toy pipeline demo/rag_demo.py → demo/evidence.json"),
    "evidence": {"script": "demo/rag_demo.py", "evidence": "demo/evidence.json", "run_log": "demo/RUN-LOG.txt",
                 "script_sha256": EV["script_sha256"], "inputs_sha256": EV["inputs_sha256"]},
    "pronounce": {"RAG": "ɹˈæɡ"},
    "pronounce_note": ("--phonemize 2026-11-22: 'RAG' alone → ɹˈæɡ, but IN CONTEXT espeak spells it R-A-G (ˌɑːɹɹˌeɪdʒˈiː); "
                       "whisper heard 'R.A.G.' in B12/BOUT and 'Ragee' in B01. Pinned to ɹˈæɡ ('rag'), as BDEFS already says it. "
                       "'embedding' ɛmbˈɛdɪŋ, 'FAQ' ˌɛfˌeɪkjˈuː, 'Hallo' hˈæloʊ need no override."),
    "playlist": "Claude & Agentic AI", "chapter_number": 0, "series": "STEM/AI explainers", "series_number": 7,
    "tags": ["RAG", "retrieval-augmented generation", "embeddings", "vector database", "vector store",
             "LLM", "hallucination", "Claude", "Nik Bear Brown"]},
    "beats": BEATS}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

tot_w = sum(len(b["narration_text"].split()) for b in BEATS)
print(f"{len(BEATS)} beats ({len(body)} body, {len(cards)} cards); {tot_w} words; "
      f"est {tot_w / 3.5:.0f} s @3.5 w/s, {sum(b['estimated_duration_s'] for b in BEATS):.0f} s @{WPS} w/s")
for b in BEATS:
    print(f"  {b['beat_id']:<6} {len(b['narration_text'].split()):>3}w  {b['narration_text'][:70]}")
