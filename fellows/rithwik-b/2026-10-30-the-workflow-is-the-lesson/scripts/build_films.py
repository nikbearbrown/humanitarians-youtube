#!/usr/bin/env python3
"""Author beat sheets + paperwork for films 2-4 of the AI Fluency x Brutalist series.

Same spine as film 1 (hai-fluent-isnt-finished): composer cold open -> hesitant-writer
BLUF -> five body cards -> ask/result receipt -> when-not-to -> verdict -> Your Turn ->
title layout outro. Every receipt is a real artifact from this series' own build.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHIP = "@HumanitariansAI"


def composer(bid, act, narr, show, **props):
    props.setdefault("folderLabel", CHIP)
    return {"beat_id": bid, "act": act, "narration_text": narr,
            "shot": {"scene_type": "remotion", "show": show,
                     "remotion": {"pattern": "ClaudeComposerAsk", "props": props}}}


def card(bid, act, narr, show, pattern="ShowTellCard", **props):
    return {"beat_id": bid, "act": act, "narration_text": narr,
            "shot": {"scene_type": "remotion", "show": show,
                     "remotion": {"pattern": pattern, "props": props}}}


def rows(*pairs, key="value"):
    return [{"label": a, key: b} for a, b in pairs]


def film(slug, title, n, outcome, hello, b00, b01, body, b07, b08, b09, b10, b11):
    """body = five (narration, show, props) beats B02-B06."""
    cmd, out, narr00 = b00
    text, trig, repl, narr01 = b01
    beats = [
        composer("B00", "cold open", narr00,
                 [{"at": "start", "event": "composer types the ask"},
                  {"at": "end", "event": "result lines land"}],
                 greeting=hello, topic="IRREDUCIBLY HUMAN", segment=title,
                 command=cmd, runningText="working…", output=out),
        card("B01", "overview", narr01,
             [{"at": "start", "event": "writer types the misconception"},
              {"at": "correction", "event": "phrase struck and retyped"}],
             pattern="BrutalistHesitantWriter", text=text, triggerWords=trig,
             replacementWords=repl, fontSize=140, charMs=35, mistakeRate=4,
             seed=slug, brandLabel=CHIP),
    ]
    beats[1]["lead_silence_s"] = 0.8
    for i, (narr, show, props) in enumerate(body, start=2):
        pattern = props.pop("pattern", "ShowTellCard")
        beats.append(card(f"B{i:02d}", "body", narr, show, pattern=pattern, **props))
    seg, cmd7, out7, narr7 = b07
    beats.append(composer("B07", "worked example", narr7,
                          [{"at": "start", "event": "the real ask"},
                           {"at": "end", "event": "the real log lines land"}],
                          greeting="A real build.", topic="FILM 1 BUILD", segment=seg,
                          command=cmd7, runningText="running…", output=out7,
                          animateTyping=False))
    t8, code8, spark8, narr8 = b08
    beats.append(card("B08", "worked example", narr8,
                      [{"at": "start", "event": "real file lines land"}],
                      pattern="ClaudeCodeBeat", title=t8, code=code8, sparkLine=spark8,
                      brandLabel=CHIP, largeText=True))
    q9, items9, narr9 = b09
    beats.append(card("B09", "when not to", narr9,
                      [{"at": "start", "event": "search types the question"},
                       {"at": "end", "event": "four answers resolve"}],
                      kind="search", heading=q9, items=rows(*items9, key="sub"), focus=2))
    word10, head10, sub10, narr10 = b10
    beats.append(card("B10", "verdict", narr10,
                      [{"at": "start", "event": "the verdict word stretches in"}],
                      kind="elastic", word=word10, heading=head10, sub=sub10))
    seg11, cmd11, narr11 = b11
    beats.append(composer("B11", "your turn", narr11,
                          [{"at": "start", "event": "composer types the viewer's prompt"}],
                          greeting="Your turn.", topic="TRY THIS", segment=seg11,
                          command=cmd11, runningText="paste this into Claude…"))
    beats.append(card("B12", "outro", f"{title.rstrip('.')}. At Humanitarians A I.",
                      [{"at": "start", "event": "title-restate layout with the handle"}],
                      kind="layout", heading=title.rstrip('.') + ".", sub=CHIP,
                      items=[{"label": f"AI Fluency × Brutalist · film {n}"}]))
    sheet = {"metadata": {
        "title": title, "slug": slug, "series": f"AI Fluency × Brutalist (film {n} of 4)",
        "audience": "Humanitarians AI fellows who use Claude daily but have never built with the Brutalist toolkit",
        "outcome": outcome, "channel": "claude-hai", "folderLabel": CHIP,
        "topic": "Irreducibly Human", "engine": "kokoro", "voice_kokoro": "af_bella",
        "palette": "claude", "register": "Plain", "aspect": "16:9"}, "beats": beats}
    return sheet


def paperwork(folder, sheet, facts):
    rows_ = "\n".join(f"| {b['beat_id']} | {b['shot']['remotion']['pattern']}"
                      f"{' · ' + b['shot']['remotion']['props']['kind'] if 'kind' in b['shot']['remotion']['props'] else ''}"
                      f" | media/{b['beat_id']}.mp4 |" for b in sheet["beats"])
    (folder / "SHOTLIST.md").write_text(
        f"# SHOTLIST — {sheet['metadata']['slug']}\n\nAll 13 slots are machine-rendered "
        f"Remotion scenes. No pantry media requested.\n\n| Beat | Composition | Slot |\n|---|---|---|\n{rows_}\n")
    yt = sheet["beats"][11]["shot"]["remotion"]["props"]["command"]
    (folder / "PROMPTS.md").write_text(
        f"# PROMPTS — {sheet['metadata']['slug']}\n\nNo open slots — every beat is a rendered "
        f"Remotion composition.\n\nB11 (viewer handoff prompt, read aloud in the film):\n> {yt}\n")
    table = "\n".join(f"| {b} | {c} | {v} | {s} |" for b, c, v, s in facts)
    (folder / "FACTCHECK-DRAFT.md").write_text(
        f"# FACTCHECK — {sheet['metadata']['slug']} (DRAFT — NOT SIGNED)\n\n"
        "Status: **drafted by Claude, awaiting human review.** GATE F stays closed until a\n"
        "person checks every row and renames this file to `FACTCHECK.md`.\n\n"
        f"| Beat | Claim (as narrated) | Verdict | Source |\n|---|---|---|---|\n{table}\n\n"
        "Reviewed by: ________  Date: ________\n")


FILMS = []

# ── Film 2 ────────────────────────────────────────────────────────────────────
FILMS.append(("hai-beat-sheet-is-the-prompt", film(
    "hai-beat-sheet-is-the-prompt", "The Beat Sheet Is the Prompt", 2,
    "Name a beat's parts (narration, show, scene) and explain why Brutalist generates audio first",
    "Ola, HAI",
    ('claude "build film 1 of the AI fluency series"',
     ["beat_sheet.json · 13 beats", "every beat: said · shown · rendered", "audio · measured first"],
     "Ola, I'm Bella, for Humanitarians A I. Last time, Claude built a whole video from one request. "
     "But the request wasn't really one sentence. It was a file. And that file is the most important "
     "prompt in the whole toolkit."),
    ("Here's the whole idea.\nA good prompt is\na clever sentence.", "a clever sentence",
     "a complete description",
     "Here's the whole idea. A good prompt isn't a clever sentence. It's the whole job, described. "
     "In Brutalist, that description has a name. The beat sheet."),
    [
     ("Of all the A I fluency skills, this is the one people underrate. Not tricks, not magic words. "
      "Description. Telling the machine what the product is, how it should be made, and how it should "
      "sound. Brutalist makes you write all three down.",
      [{"at": "Description", "event": "the word DESCRIBE fills the frame"}],
      {"kind": "masked", "word": "Describe", "heading": "The skill", "sub": "the whole job, on paper"}),
     ("Here's one real beat from film one. The narration is what Bella says. The show block is what "
      "you watch, and when. The pattern is the scene that renders it. Every beat in the film is this "
      "explicit. Nothing is left for the machine to guess.",
      [{"at": "start", "event": "the real B03 beat from film 1 lands line by line"}],
      {"pattern": "ClaudeCodeBeat", "title": "beat_sheet.json · film 1, B03", "language": "json",
       "largeText": True, "brandLabel": CHIP, "sparkLine": "Nothing to guess.",
       "code": '{\n  "beat_id": "B03",\n  "narration_text": "But the whole toolkit rests on one asymmetry…",\n'
               '  "shot": {\n    "show": [{"at": "cannot watch",\n              "event": "the word WATCH fills the frame"}],\n'
               '    "remotion": {"pattern": "ShowTellCard",\n                 "props": {"kind": "masked", "word": "Watch"}}\n  }\n}'}),
     ("Read it like a spec. What is said. What you see. What renders it, with the exact details. And one "
      "field Claude fills in afterward, the audio file, measured to the hundredth of a second. That last "
      "one changes everything.",
      [{"at": "said", "event": "lens snaps row by row"}, {"at": "afterward", "event": "lens lands on audio_file"}],
      {"kind": "focus", "heading": "Read it like a spec",
       "items": rows(("narration_text", "what is said"), ("show", "what you see"), ("pattern", "what renders it"),
                     ("props", "the exact details"), ("audio_file", "the measured clock")),
       "focus": 4, "cues": [0.12, 0.22, 0.32, 0.5]}),
     ("Because Brutalist is audio first. Kokoro, a free local voice, speaks the narration, and every clip "
      "is measured. Those real durations become the clock. Every scene is built to fit the voice, never "
      "the other way around.",
      [{"at": "audio first", "event": "path lights Narration → Audio → Clock → Scenes → Cut"}],
      {"kind": "paths", "heading": "Audio first",
       "items": [{"label": "Narration"}, {"label": "Audio"}, {"label": "Clock"}, {"label": "Scenes"}, {"label": "Cut"}],
       "focus": 2, "cues": [0.14, 0.24, 0.34, 0.44, 0.54]}),
     ("This is film one's actual clock. The cold open ran thirteen and a half seconds. The your turn beat, "
      "eighteen. The outro, under three. Nobody guessed those numbers. And if the timing feels wrong, you "
      "don't nudge it by hand. You rewrite the words and regenerate.",
      [{"at": "actual clock", "event": "line chart draws film 1's measured beat lengths"}],
      {"kind": "chart", "heading": "Film 1, seconds per beat", "sub": "measured, not guessed",
       "labels": ["B00", "B03", "B06", "B09", "B11", "B12"], "values": [13.5, 15.1, 16.0, 11.1, 18.0, 2.9]}),
    ],
    ("A Missing Line", 'claude "compile film 1 for the Humanitarians AI channel"',
     ["[beat-lint] topic is None; channel claude-hai", "  must use fixed kicker 'Irreducibly Human'",
      "[run] GATE L FAILED … Nothing rendered."],
     "Here's what happens when the description is incomplete. Building film one, my beat sheet left out "
     "a single field, the channel's series name. The toolkit refused to render anything until it was there."),
    ("beat_sheet.json · the fix",
     '"metadata": {\n  "channel": "claude-hai",\n- "topic": null\n+ "topic": "Irreducibly Human"\n}\n\n'
     "$ ./art run hai-fluent-isnt-finished\n[beat-lint] clean — beat mix OK",
     "One line fixed it.",
     "One line fixed it. That's the point of a written description. The gap was visible, it had a name, "
     "and the fix was a single line. A vague prompt fails quietly. A complete one fails loudly, early, and cheaply."),
    ("how much do I write down?",
     [("One-off question", "a sentence is fine"), ("Quick personal draft", "a sentence is fine"),
      ("Work you'll repeat", "write the spec"), ("Work others rely on", "write the spec")],
     "Where this bites. Writing a full spec takes time. For a one-off question or a quick personal draft, "
     "a good sentence is plenty. Write the whole description when you'll repeat the work, or when someone "
     "else depends on it."),
    ("Described", "The best prompt is", "said · shown · timed",
     "So, the verdict. The best prompt isn't the cleverest. It's the most complete. Say what's said, "
     "what's shown, and how long it takes, and the machine has nothing left to guess."),
    ("Write the Spec",
     "Here's a task I keep giving AI: [your task]. Turn it into a written spec: what goes in, what comes "
     "out, the steps, and what I must check myself.",
     "Your turn. Paste this into Claude. Here's a task I keep giving A I, and then your task. Turn it into "
     "a written spec. What goes in, what comes out, the steps, and what I must check myself. Look hardest "
     "at that last part. Whatever lands there is still your job. Run it on a task you repeat every week."),
), [
    ("B00/B03", "Brutalist builds every video from a beat_sheet.json", "TRUE", "HOW-TO.md §1; film 1 build"),
    ("B03", "Film 1 B03 beat shown on screen", "TRUE (verbatim, trimmed)", "hai-fluent-isnt-finished/beat_sheet.json"),
    ("B04", "audio_file filled in after generation, measured to 0.01 s", "TRUE (log)", "generate_audio_kokoro.py output"),
    ("B05", "Audio-first: measured durations are the master clock", "TRUE", "CLAUDE.md rule 2; HOW-TO §1"),
    ("B05", "Kokoro is a free local voice", "TRUE", "HOW-TO §2 (model ships locally, no key)"),
    ("B06", "Film 1 beat lengths 13.5 / 15.1 / 16.0 / 11.1 / 18.0 / 2.9 s", "TRUE (log)", "film 1 audio run"),
    ("B06", "Fix timing by rewriting + regenerating, not by hand", "TRUE", "CLAUDE.md rule 2"),
    ("B07/B08", "GATE L refused film 1 over a missing topic; one line fixed it", "TRUE (log)", "film 1 ./art run output"),
    ("B09", "A sentence is enough for one-off work", "JUDGMENT", "framed as advice"),
]))

# ── Film 3 ────────────────────────────────────────────────────────────────────
FILMS.append(("hai-look-at-the-frames", film(
    "hai-look-at-the-frames", "Look at the Frames", 3,
    "Read a QC report and contact sheet and classify a defect as blocker, major, or fine",
    "Hej, HAI",
    ('claude "render all 13 scenes for film 1"',
     ["[remotion] B00 … B12: ok", "slots: 13/13 filled", "review cut · 172.0s"],
     "Hej, I'm Bella, for Humanitarians A I. Film one rendered all thirteen of its scenes on the first try. "
     "No errors, no crashes. It still wasn't good enough to show you. Here's how we found out."),
    ("Here's the whole idea.\nIf it rendered,\nit's finished.", "it's finished", "someone still has to look",
     "Here's the whole idea. If it rendered, someone still has to look. Evaluating output is the A I fluency "
     "skill no prompt can replace, and Brutalist builds it into every cut."),
    [
     ("A rendered video feels finished. It plays. It has sound. It has a progress bar. But rendering only "
      "proves the code ran. It says nothing about whether a viewer can read the screen, or whether a "
      "picture means anything at all.",
      [{"at": "plays", "event": "player opens and scrubs through film 1"}],
      {"kind": "player", "heading": "Film 1 review cut", "sub": "13 scenes · rendered", "values": [172, 172]}),
     ("So the toolkit looks first. Its visual gate samples every beat at three moments and checks the "
      "frames. Text bleeding off the edge, crowded margins, overflowing boxes, type too small to read, and "
      "big empty canvas. Any major defect, and the cut fails.",
      [{"at": "bleeding", "event": "lens snaps down the rubric rows"}, {"at": "empty canvas", "event": "lens lands on canvas fill"}],
      {"kind": "focus", "heading": "What the gate checks",
       "items": rows(("Edge bleed", "clipping"), ("Title-safe", "margins"), ("Overflow", "boxes"),
                     ("Legibility", "type size"), ("Canvas fill", "dead space")),
       "focus": 4, "cues": [0.3, 0.4, 0.5, 0.62]}),
     ("Film one's first cut failed. Eight major defects, all the same kind. Empty canvas. The outro filled "
      "just eight percent of the frame. The overview, thirty six. The minimum is fifty five. Real numbers, "
      "from the real report.",
      [{"at": "eight percent", "event": "line chart draws the four failing fill values"}],
      {"kind": "chart", "heading": "Canvas fill, first cut", "sub": "minimum 55%",
       "labels": ["B12", "B01", "B09", "B06"], "values": [8, 36, 42, 51]}),
     ("But the gate isn't the whole review. It caught the empty canvas. It did not notice that one card "
      "showed meaningless placeholder pictures, or that a correction landed too late to read. Those I "
      "caught by looking at the frames myself.",
      [{"at": "start", "event": "tab: what the gate caught"}, {"at": "did not notice", "event": "tabs switch: what only eyes caught"}],
      {"kind": "tabs", "labels": ["The gate caught", "Only eyes caught"],
       "items": [{"label": "Empty canvas, 4 beats"}, {"label": "Outro at 8% fill"}, {"label": "Overview too small"}],
       "items2": [{"label": "Placeholder pictures"}, {"label": "Correction typed late"}, {"label": "A missing heading"}],
       "cues": [0.4]}),
     ("And when the machine honestly can't make a visual, Brutalist doesn't fake one. It renders a slate, "
      "a labeled card that says exactly what's missing. You drop the real thing into the pantry folder, "
      "rebuild, and only that slot changes.",
      [{"at": "slate", "event": "path lights Gap → Slate → You → pantry → Rebuild"}],
      {"kind": "paths", "heading": "Honest gaps",
       "items": [{"label": "Gap"}, {"label": "Slate"}, {"label": "You"}, {"label": "pantry/"}, {"label": "Rebuild"}],
       "focus": 1, "cues": [0.14, 0.26, 0.4, 0.52, 0.62]}),
    ],
    ("The First Verdict", 'claude "compile film 1 and run the visual check"',
     ["[gate-v] frames=26 BLOCKER=0 MAJOR=8", "[gate-v] FAILED — 8 blocking defect(s)", "Reel not clean; fix and re-render."],
     "Here's the receipt. Twenty six frames sampled. Zero blockers, eight majors. Failed. The machine "
     "built every piece correctly, and the result still wasn't ready for a viewer."),
    ("film 1 · four compiles",
     "B01  type 84 → 140 px, typing 50 → 35 ms\nB06  stack card → focus card\nB09  2 rows → 4 rows\n"
     "B12  OutroCTA → title layout\n\n[gate-v] compile 1  MAJOR=8\n[gate-v] compile 2  MAJOR=1\n"
     "[gate-v] compile 3  MAJOR=2\n[gate-v] compile 4  MAJOR=0",
     "Look, change, look.",
     "It took four compiles to get to zero. Bigger type, faster typing, a different card, a real outro. "
     "Notice compile three got worse before it got better. That's normal. You look, you change one thing, "
     "you look again."),
    ("how closely do I look?",
     [("Private draft", "skim it once"), ("Practice video", "skim it once"),
      ("Shared with fellows", "check every beat"), ("Public video", "check every frame")],
     "Where this bites. Frame by frame review is slow. For a private draft, one honest skim is enough. "
     "When other people will watch it, check every beat. The more people who'll trust it, the closer you look."),
    ("Looked", "Rendered isn't", "sampled · read · fixed",
     "So, the verdict. Rendered isn't reviewed. A machine can measure the canvas. Only a person can tell "
     "whether the picture means anything."),
    ("Where Do I Look?",
     "Here's something an AI made for me: [paste it]. Before I use it, list what a person must inspect "
     "that you can't verify yourself, and which parts you're least sure about.",
     "Your turn. Paste this into Claude. Here's something an A I made for me, and then paste it in. Before "
     "I use it, list what a person must inspect that you can't verify yourself, and which parts you're "
     "least sure about. That second question matters most. Where it's least sure is where your eyes go "
     "first. Run it on the next thing an A I makes for you."),
), [
    ("B00", "Film 1 rendered all 13 scenes on the first pass", "TRUE (log)", "film 1 remotion_scenes.py output"),
    ("B03", "GATE V samples each beat at ~15/50/85% and checks edge, margins, overflow, legibility, fill", "TRUE",
     "ai-explainer SKILL.md VISUAL QC LAW; _qc/REPORT.md"),
    ("B04", "First cut: 8 MAJOR underfill; B12 8%, B01 36%, B09 42%, B06 51%; min 55%", "TRUE (log)",
     "film 1 _qc/REPORT.md, compile 1"),
    ("B05", "Gate missed placeholder images, late correction, missing heading", "TRUE (observed)", "manual frame review of film 1"),
    ("B06", "Slates name what's missing; pantry/ swap rebuilds only that slot", "TRUE", "HOW-TO.md §1"),
    ("B08", "Four compiles: MAJOR 8 → 1 → 2 → 0", "TRUE (log)", "film 1 GATE V runs"),
    ("B09", "Review depth should scale with audience", "JUDGMENT", "framed as advice"),
]))

# ── Film 4 ────────────────────────────────────────────────────────────────────
FILMS.append(("hai-trust-then-verify", film(
    "hai-trust-then-verify", "Trust, Then Verify", 4,
    "Decide which claims in a script need a source before the final cut, and who signs for them",
    "Ciao, HAI",
    ('claude "make a video series from this brief on AI fluency"',
     ["brief · 5 claims found", "2 sourced · 2 unverified · 1 contradicted", "FACTCHECK-DRAFT.md · awaiting review"],
     "Ciao, I'm Bella, for Humanitarians A I. When this series started, Claude was handed a brief. It was "
     "clear, confident, and it came with citations. Some of it didn't hold up. Here's how the toolkit kept "
     "that from reaching you."),
    ("Here's the whole idea.\nIf it sounds polished,\nit's probably true.", "it's probably true",
     "check it before you share",
     "Here's the whole idea. Polished isn't true. Knowing when to trust A I output and when to check it is "
     "the last A I fluency skill, and in Brutalist it's a gate you can't skip."),
    [
     ("Fluent text is persuasive. It reads like someone careful wrote it, whether or not anyone did. That's "
      "exactly why verification is its own skill. You don't check the writing. You check each claim, one at "
      "a time, against a source.",
      [{"at": "verification", "event": "the word VERIFY fills the frame"}],
      {"kind": "masked", "word": "Verify", "heading": "The skill", "sub": "trust, then check"}),
     ("Here's the brief, claim by claim. The definition of A I fluency held up. Showing your real work "
      "matched the toolkit's own docs. But two claims, a named course and a university credit, had no public "
      "source Claude could find. And one contradicted the toolkit outright.",
      [{"at": "claim by claim", "event": "lens walks the five claims"}, {"at": "no public source", "event": "lens rests on the unsourced rows"}],
      {"kind": "focus", "heading": "The brief, claim by claim",
       "items": rows(("AI fluency definition", "consistent"), ("Show the real work", "matches toolkit"),
                     ("Taught via Botspeak", "no source found"), ("Credited to Stanford", "no source found"),
                     ("Upload every week", "contradicts toolkit")),
       "focus": 3, "cues": [0.18, 0.32, 0.5]}),
     ("So they split. Sourced claims went into the films. Unsourced ones were held out until someone finds "
      "a source. And the contradiction, that Brutalist means uploading videos every week, got corrected. "
      "Nothing in the toolkit ever publishes.",
      [{"at": "start", "event": "tab: kept"}, {"at": "held out", "event": "tabs switch: held out"}],
      {"kind": "tabs", "labels": ["Kept", "Held out"],
       "items": [{"label": "Fluency definition"}, {"label": "Show the real work"}],
       "items2": [{"label": "Botspeak course"}, {"label": "Stanford credit"}, {"label": "Upload every week"}],
       "cues": [0.3]}),
     ("Every film ships with a fact check file. Each row is one claim, its source, a verdict, and the fix. "
      "And at the bottom, a line for a person to sign. The toolkit won't export a final master without it.",
      [{"at": "Each row", "event": "path lights Claim → Source → Verdict → Fix → Signed"}],
      {"kind": "paths", "heading": "One row per claim",
       "items": [{"label": "Claim"}, {"label": "Source"}, {"label": "Verdict"}, {"label": "Fix"}, {"label": "Signed"}],
       "focus": 4, "cues": [0.2, 0.3, 0.38, 0.46, 0.62]}),
     ("But look at what the gate actually checks. Only that the file exists and isn't empty. If Claude "
      "wrote that file itself, the gate would open, and nobody would have checked anything. The code can't "
      "tell a real signature from a fake one.",
      [{"at": "start", "event": "the real gate function lands line by line"}],
      {"pattern": "ClaudeCodeBeat", "title": "build_safety.py", "language": "python", "largeText": True,
       "brandLabel": CHIP, "sparkLine": "It only checks a file.",
       "code": "def require_paperwork(folder):\n    for name in ('FACTCHECK.md', 'SHOTLIST.md', 'PROMPTS.md'):\n"
               "        p = Path(folder) / name\n        if not p.is_file() or not p.read_text().strip():\n"
               "            raise BuildError(f'GATE F: missing or empty {name}; '\n"
               "                             'review is allowed, final is blocked')"}),
    ],
    ("Draft, Don't Sign", 'claude "draft the fact check for film 1, but don\'t sign it"',
     ["FACTCHECK-DRAFT.md · 10 claims", "Reviewed by: ________", "GATE F: still closed"],
     "So here's what Claude did instead. It drafted every row, and saved the file under a different name. "
     "The gate stays closed. Ten claims, checked by the machine, waiting for a person."),
    ("FACTCHECK-DRAFT.md",
     "# FACTCHECK — hai-fluent-isnt-finished (DRAFT — NOT SIGNED)\n\n"
     "Status: drafted by Claude, awaiting human review.\nGATE F stays closed until a person checks every row\n"
     "and renames this file to FACTCHECK.md.\n\nReviewed by: ________  Date: ________",
     "Waiting for you.",
     "This is the real file, right now. Drafted by Claude. Awaiting human review. That blank line is the "
     "whole lesson. The machine can find the claims and look for sources. Deciding they're good enough to "
     "carry your name is yours."),
    ("when can I skip checking?",
     [("Brainstorm for yourself", "trust, lightly"), ("Private notes", "trust, lightly"),
      ("Anything you'll share", "check each claim"), ("Anything with your name", "check, then sign")],
     "Where this bites. Checking every claim is real work. For a brainstorm or private notes, light trust "
     "is fine. The moment something carries your name to other people, every claim gets a source."),
    ("Checked", "Polished isn't", "sourced · signed · yours",
     "So, the verdict. Polished isn't checked. And nothing in Brutalist publishes. The master stays with "
     "you. Putting it in front of an audience is always your call."),
    ("Check the Claims",
     "Here's a paragraph I'm about to share: [paste it]. List every factual claim, mark which ones you "
     "can't verify, and tell me what source I'd need for each.",
     "Your turn. Paste this into Claude. Here's a paragraph I'm about to share, and then paste it in. List "
     "every factual claim, mark which ones you can't verify, and tell me what source I'd need for each. The "
     "list of claims it can't verify is your to do list. Run it on the next thing you post."),
), [
    ("B00/B03", "The series brief contained 5 claims: 2 sourced, 2 unverified, 1 contradicted", "TRUE (session record)",
     "SERIES-PLAN.md fact-check table"),
    ("B03", "No public source found for 'Botspeak' or the Stanford HAI credit", "TRUE (as of 2026-10-29 searches)",
     "web searches logged in session; re-check before signing"),
    ("B04", "Nothing in the toolkit publishes", "TRUE", "CLAUDE.md rule 5; HOW-TO.md §1"),
    ("B05", "FACTCHECK rows: claim | verdict | source | fix; final blocked without it", "TRUE", "HOW-TO.md §5; build_safety.py"),
    ("B06", "GATE F checks only that the file exists and is non-empty", "TRUE (verbatim code)", "runtime/scripts/build_safety.py require_paperwork"),
    ("B07/B08", "Film 1's draft has 10 claims, unsigned, saved as FACTCHECK-DRAFT.md", "TRUE", "hai-fluent-isnt-finished/FACTCHECK-DRAFT.md"),
    ("B09", "Verification depth should scale with who relies on it", "JUDGMENT", "framed as advice"),
]))


if __name__ == "__main__":
    for slug, sheet, facts in FILMS:
        folder = HERE / slug
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
        paperwork(folder, sheet, facts)
        words = sum(len(b["narration_text"].split()) for b in sheet["beats"])
        print(f"{slug}: {len(sheet['beats'])} beats, {words} words")
