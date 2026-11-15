"""build_sheet.py — writes beat_sheet.json for "What Is RAG?" from the approved SCRIPT.md.

Reveal times inside each scene are fractions of the beat. They are computed from
where the cue word sits in that beat's narration (word index / word count), and
each beat's duration comes from mp3/timings.json once Bella's audio exists. Re-run
this after regenerating audio; it preserves audio_file / actual_duration_s.

Run:  python3 build_sheet.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHEET = HERE / "beat_sheet.json"
VOICE = "af_bella"
SPEED = 0.95
HANDLE = "@HumanitariansAI"
TITLE = "What Is RAG?"

old = {b["beat_id"]: b for b in json.loads(SHEET.read_text())["beats"]} if SHEET.exists() else {}
timings = json.loads((HERE / "mp3/timings.json").read_text()) if (HERE / "mp3/timings.json").exists() else {}
demo = json.loads((HERE / "demo/retrieval_output.json").read_text())


def words(s):
    return re.findall(r"[A-Za-z0-9'’-]+", s)


MEASURED = json.loads((HERE / "mp3/words.json").read_text()) if (HERE / "mp3/words.json").exists() else {}
LEAD_S = 0.2   # reveal starts this far before the word, so it is fully on screen as it is said


def norm(s):
    return re.sub(r"[^a-z0-9']", "", s.lower().replace("’", "'"))


def at(text, cue, nudge_s=0.0):
    """Fraction of the beat (of its scene duration) at which `cue` is spoken.

    Uses the MEASURED word start from mp3/words.json (faster-whisper on Bella's
    audio). Falls back to word position only before audio exists.
    """
    bid = next(k for k, v in N.items() if v == text)
    c = [norm(x) for x in words(cue)]
    if bid in MEASURED and bid in timings:
        ws = [(norm(x["w"]), x["s"]) for x in MEASURED[bid]]
        for i in range(len(ws) - len(c) + 1):
            if [w for w, _ in ws[i:i + len(c)]] == c:
                scene = timings[bid] + 0.4
                return round(max(0.0, min(0.95, (ws[i][1] - LEAD_S + nudge_s) / scene)), 4)
        raise SystemExit(f"cue {cue!r} not found in measured words for {bid}")
    w = [norm(x) for x in words(text)]
    for i in range(len(w) - len(c) + 1):
        if w[i:i + len(c)] == c:
            return round(max(0.0, min(0.95, i / len(w))), 3)
    raise SystemExit(f"cue {cue!r} not found in: {text}")


N = {
 "B00": "Hi, I am Tanishaa, and this video is about RAG, retrieval-augmented generation, and when it actually helps. The voice you're hearing is Bella, an AI narrator reading a script I wrote.",
 "B01": "RAG lets an AI look things up before it answers. It doesn't make the model any smarter. It hands the model the right pages, so the answer can point back to a source.",
 "B02": "Start with the problem. A language model answers from patterns it absorbed during training. It has never seen your syllabus, your company handbook, or a policy that changed last month. Ask anyway, and it may still answer, fluently and wrong. Fluent isn't the same as correct.",
 "B03": "RAG adds a step before the answer. Retrieve: search your documents for the few passages that best match the question. Augment: paste those passages into the prompt. Generate: the model writes from that text, and it can say where each part came from.",
 "B04": "How does the search know which passages match? First, the documents are cut into short chunks. Each chunk is turned into a list of numbers, called an embedding, that captures what it means. The question gets one too. Chunks with similar meaning land close together, so a question about late work can find a passage about an extension.",
 "B05": "Here it is on that same question. The search pulls three passages from the syllabus. The top one says labs can be submitted up to forty-eight hours late, with a ten percent penalty. Now the answer quotes it and names the section it came from, so you can check it yourself.",
 "B06": "So when should you use it? When the answer lives in documents you can point to, like a syllabus, a manual or last week's meeting notes, especially when those facts change. When shouldn't you? If the document is short, just paste it in. If you need reasoning or writing, not lookup, retrieval won't help much. And watch the search: if it grabs the wrong passage, you get a wrong answer that looks sourced.",
 "B07": "Three things to keep. RAG looks things up; it doesn't learn. A citation is something to check, not a guarantee. And the answer is only as good as what was retrieved.",
 "B08": "Your turn. Paste in a document you actually use and try this prompt: Here's a document I use for school or work. Split it into short passages, show me the three you'd retrieve for my question, then answer using only those passages, quote them, and tell me what the document doesn't say. That last part is the real test. A good answer admits what isn't there.",
 "B09": "What is RAG? At Humanitarians AI.",
}

YOUR_TURN = ("Here's a document I use for school or work. Split it into short passages, show me the three "
             "you'd retrieve for this question: [my question]. Then answer using only those passages, "
             "quote them, and tell me what the document doesn't say.")

top = demo["top3"][0]
SHOTS = {
 "B00": ("ClaudeComposerAsk", {
    "greeting": "Hi, Tanishaa", "topic": "Irreducibly Human", "segment": TITLE,
    "command": "What is RAG, and when should I actually use it?",
    "runningText": "thinking…",
    "output": ["RAG = retrieval-augmented generation.", "It searches your documents first,", "then answers from what it found."],
    "folderLabel": HANDLE, "modelLabel": "Claude", "effortLabel": "AI narration: Bella", "largeText": True}),
 "B01": ("BrutalistHesitantWriter", {
    "text": "RAG makes the AI smarter.\nIt hands the model the right pages.",
    "triggerWords": "makes the AI smarter", "replacementWords": "lets the AI look things up before it answers",
    "fontSize": 88, "lineSpacing": 1.5, "yOffset": -170, "seed": "what-is-rag-b01", "mistakeRate": 4, "charMs": 45}),
 "B02": ("RagTwoAnswers", {
    "question": "Can I submit Lab 3 late?", "spark": "Fluent isn't correct.",
    "leftLabel": "From memory", "leftAnswer": "Yes. Late labs are accepted for up to one week with no penalty.",
    "stamp": "no source", "stampAt": at(N["B02"], "fluently"), "rightLabel": "With retrieval",
    "footnote": "The “from memory” answer is invented on purpose, to show the failure.",
    "footnoteShort": "Invented answer, on purpose."}),
 "B03": ("RagPipeline", {
    "spark": "One step before the answer.",
    "stages": [{"name": "Retrieve", "detail": "search your documents for the best-matching passages"},
               {"name": "Augment", "detail": "paste those passages into the prompt"},
               {"name": "Generate", "detail": "answer from that text, with citations"}],
    "stageAt": [at(N["B03"], "Retrieve"), at(N["B03"], "Augment"), at(N["B03"], "Generate")]}),
 "B04": ("RagEmbeddingMap", {
    "spark": "Close in meaning, close on the map.",
    "chunks": [{"label": "office hours", "x": 0.12, "y": 0.22}, {"label": "grading", "x": 0.80, "y": 0.18},
               {"label": "late labs", "x": 0.40, "y": 0.42}, {"label": "extensions", "x": 0.30, "y": 0.70},
               {"label": "final project", "x": 0.82, "y": 0.62}, {"label": "integrity", "x": 0.62, "y": 0.86},
               {"label": "attendance", "x": 0.58, "y": 0.30}],
    "question": {"label": "Can I submit Lab 3 late?", "x": 0.24, "y": 0.50},
    "nearest": ["late labs", "extensions", "attendance"], "highlight": "extensions",
    "chunks916": [{"label": "office hours", "x": 0.05, "y": 0.0}, {"label": "grading", "x": 0.95, "y": 0.14}, {"label": "attendance", "x": 0.62, "y": 0.3}, {"label": "late labs", "x": 0.45, "y": 0.44}, {"label": "extensions", "x": 0.3, "y": 0.72}, {"label": "final project", "x": 0.95, "y": 0.86}, {"label": "integrity", "x": 0.4, "y": 1.0}], "question916": {"x": 0.12, "y": 0.58},
    "cutAt": at(N["B04"], "cut into"), "flyAt": at(N["B04"], "Each chunk is turned"),
    "questionAt": at(N["B04"], "The question gets"), "linkAt": at(N["B04"], "Chunks with similar"),
    "footnote": "Schematic: dot positions illustrate the idea; they are not computed embeddings.",
    "footnoteShort": "Schematic, not computed."}),
 "B05": ("RagRetrievalDemo", {
    "spark": "Real search, real output.", "question": demo["question"],
    "method": f'{demo["method"]} over {demo["chunks_searched"]} chunks',
    "results": [{"section": r["section"], "text": r["text"], "score": r["score"]} for r in demo["top3"]],
    "resultsAt": at(N["B05"], "pulls three"),
    "answer": "Yes, within 48 hours of the deadline, with a 10 percent penalty. After 48 hours it gets no credit.",
    "citation": f'Source: {top["section"]} of the syllabus', "answerAt": at(N["B05"], "Now the answer"),
    "footnote": "Example syllabus made up for this demo · scores from demo/rag_demo.py",
    "footnoteShort": "Made-up syllabus · real scores"}),
 "B06": ("RagWhenToUse", {
    "useHeader": "Use it when", "skipHeader": "Skip it when",
    "useHeaderAt": at(N["B06"], "should you use"), "skipHeaderAt": at(N["B06"], "shouldn't you"),
    "useItems": [{"text": "the answer lives in your documents", "at": at(N["B06"], "answer lives")},
                 {"text": "the facts change", "at": at(N["B06"], "facts change")},
                 {"text": "you need to cite a source", "at": at(N["B06"], "facts change", 0.8)}],
    "skipItems": [{"text": "the document is short: paste it", "at": at(N["B06"], "document is short")},
                  {"text": "the task is reasoning or writing", "at": at(N["B06"], "reasoning or writing")}],
    "warning": "Wrong passage → a wrong answer that looks sourced.", "warningAt": at(N["B06"], "watch the search")}),
 "B07": ("ClaudeVerdictArtifact", {
    "artifactTitle": TITLE, "artifactHeading": "Three things to keep",
    "artifactLines": ["RAG looks things up; it doesn't learn.",
                      "A citation is something to check, not a guarantee.",
                      "The answer is only as good as the retrieval."],
    "lectureLayout": True, "lecturePageFrames": [0, round(at(N["B07"], "And the answer") * (timings.get("B07", 11) + 0.4) * 30)]}),
 "B08": ("ClaudeComposerAsk", {
    "greeting": "Your turn.", "topic": "YOUR TURN · RAG", "segment": TITLE, "command": YOUR_TURN,
    "runningText": "paste this into Claude…", "output": [], "folderLabel": HANDLE,
    "modelLabel": "Claude", "effortLabel": "AI narration: Bella", "largeText": True}),
 "B09": ("HaiTitleOutro", {"title": TITLE, "handle": HANDLE}),
}

ACTS = {"B00": "ASK", "B01": "BLUF", "B02": "PROBLEM", "B03": "FRAMEWORK", "B04": "MECHANISM",
        "B05": "WORKED EXAMPLE", "B06": "WHEN NOT TO", "B07": "VERDICT", "B08": "YOUR TURN", "B09": "OUTRO"}
EST = {"B00": 12, "B01": 11, "B02": 17, "B03": 16, "B04": 21, "B05": 18, "B06": 26, "B07": 11, "B08": 24, "B09": 4}

beats = []
for bid, text in N.items():
    pattern, props = SHOTS[bid]
    o = old.get(bid, {})
    d = timings.get(bid) or o.get("actual_duration_s") or EST[bid]
    props = {**props, "durationSeconds": round(float(d) + 0.4, 2)}
    b = {"beat_id": bid, "act": ACTS[bid], "narration_text": text, "voice": VOICE, "engine": "kokoro",
         "speed": SPEED, "estimated_duration_s": EST[bid],
         "shot": {"type": "REMOTION", "source": "own", "remotion": {"pattern": pattern, "props": props}}}
    for k in ("audio_file", "actual_duration_s"):
        if k in o:
            b[k] = o[k]
    if bid in timings:
        b["actual_duration_s"] = timings[bid]
    beats.append(b)

sheet = {
 "metadata": {
  "title": TITLE, "slug": "what-is-rag", "topic": "Irreducibly Human", "brand": "claude-hai",
  "skill": "ai-explainer", "audience": "students new to AI", "register": "Plain",
  "engine": "kokoro", "voice_kokoro": VOICE, "palette": "claude", "channel": HANDLE,
  "greeting": "Hi, Tanishaa", "fellow": "Tanishaa",
  "fellow_intro": "Hi, I am Tanishaa and this video is about RAG (required fellow opening line, B00).",
  "ai_disclosure": "Narration is Kokoro af_bella, an AI voice, disclosed aloud in B00 and on the composer chip.",
  "decisions": [
   "Voice af_bella chosen by the fellow in chat on 2026-11-05 (Plain register; overrides claude-hai's am_onyx default).",
   "Body graphics use the Claude fidelity palette (cream/ink/terracotta) for one consistent look; HAI mark as the corner bug.",
   "Outro is HaiTitleOutro (HAI mark full-size, title restate, handle): ClaudeTitleOutro is locked to @NikBearBrown.",
   "B05 uses keyword search (TF-IDF) so the output is real and runnable without a model; B04 explains embeddings schematically and is captioned as such."],
 },
 "beats": beats,
}
SHEET.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
print(f"wrote {SHEET} — {len(beats)} beats, {sum(len(words(t)) for t in N.values())} words")
