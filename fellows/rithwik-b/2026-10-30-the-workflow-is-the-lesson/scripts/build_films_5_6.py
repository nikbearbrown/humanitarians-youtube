#!/usr/bin/env python3
"""Author beat sheets + paperwork for films 5-6 of the AI Fluency x Brutalist series.

Reuses build_films.py's spine helpers, with the lessons from films 2-4 baked in
(BUILD-LOG.md #7-#10): fast B01 typing, no commas in corrections, short tab labels,
an explicit language on every code card.
"""
import json
from build_films import CHIP, HERE, film, paperwork, rows

FILMS = []

# ── Film 5 ────────────────────────────────────────────────────────────────────
FILMS.append(("hai-show-what-broke", film(
    "hai-show-what-broke", "Show What Broke", 5,
    "Write a four-line failure-log entry (broke, noticed, changed, checked) and explain why it is stronger evidence than a polished demo",
    "Hola, HAI",
    ('claude "list everything that broke while building this series"',
     ["BUILD-LOG.md · 11 failures", "caught by the toolkit · 4", "caught by a person · 7"],
     "Hola, I'm Bella, for Humanitarians A I. Four films into this series, here's something most portfolios "
     "never show. Everything that broke while making them. Eleven failures, all written down. They're the "
     "best evidence in the whole project."),
    ("Here's the whole idea.\nA good portfolio shows\nonly what worked.", "only what worked", "what broke and why",
     "Here's the whole idea. A good portfolio doesn't only show what worked. It shows what broke, and why. "
     "That's what Brutalist means by showing your real work. A failure log is a receipt you can't fake."),
    [
     ("Anyone can post a polished demo. A polished demo proves something worked once. It doesn't prove you "
      "understand it. What does is the record of what broke, how you noticed, and what you changed.",
      [{"at": "what broke", "event": "the word BROKE fills the frame"}],
      {"kind": "masked", "word": "Broke", "heading": "The receipt", "sub": "failures are evidence"}),
     ("Put them side by side. The demo says it works, it looks finished, and the process is invisible. The "
      "log says what broke, how I noticed, and what I changed. Only one of those lets someone else judge "
      "your thinking.",
      [{"at": "start", "event": "tab: what the demo says"}, {"at": "The log", "event": "tabs switch: what the log says"}],
      {"kind": "tabs", "labels": ["Demo says", "Log says"],
       "items": [{"label": "It works"}, {"label": "Looks finished"}, {"label": "Process hidden"}],
       "items2": [{"label": "What broke"}, {"label": "How I noticed"}, {"label": "What I changed"}],
       "cues": [0.45]}),
     ("Here's this series' actual log, by stage. One failure in the test build. Five in film one. Four more "
      "across films two to four. One in the card previews. Eleven in all, and every one of them is written "
      "down.",
      [{"at": "by stage", "event": "line chart draws failures per stage"}],
      {"kind": "chart", "heading": "Failures logged, by stage", "sub": "11 in all",
       "labels": ["Test build", "Film 1", "Films 2–4", "Previews"], "values": [1, 5, 4, 1]}),
     ("And look at who caught them. The toolkit caught four. A refused final cut, a missing series name, "
      "empty canvas, a crashed preview. A person caught the other seven, just by watching. That split is the "
      "A I fluency lesson, written down as data.",
      [{"at": "toolkit caught", "event": "lens walks the toolkit rows"}, {"at": "A person", "event": "lens lands on the person row"}],
      {"kind": "focus", "heading": "Who caught it",
       "items": rows(("Final cut refused", "the toolkit"), ("Missing series name", "the toolkit"),
                     ("Empty canvas", "the toolkit"), ("Preview crashed", "the toolkit"),
                     ("Correction too late", "a person")),
       "focus": 4, "cues": [0.18, 0.26, 0.34, 0.5]}),
     ("Every entry has the same shape. What broke. How it was noticed. What changed. How the change was "
      "checked. Then it's logged, so the next build, and the next person, starts smarter.",
      [{"at": "same shape", "event": "path lights Broke → Noticed → Changed → Checked → Logged"}],
      {"kind": "paths", "heading": "One shape per entry",
       "items": [{"label": "Broke"}, {"label": "Noticed"}, {"label": "Changed"}, {"label": "Checked"}, {"label": "Logged"}],
       "focus": 4, "cues": [0.14, 0.26, 0.38, 0.5, 0.64]}),
    ],
    ("The Comma Bug", 'claude "why does film 2\'s correction stop at the whole job?"',
     ['replacementWords: "the whole job, described"', "split on the comma → 2 replacements",
      'fix: "a complete description"'],
     "Here's one real entry. Film two's opening correction came out wrong. It read, a good prompt is the "
     "whole job. The tool splits replacements on commas, so my phrase was cut in half. No error, no warning. "
     "Just a sentence that quietly meant less."),
    ("BUILD-LOG.md · entry 8",
     "## 8 · film 2 · comma split the fix\nbroke:   correction read \"the whole job.\"\n"
     "         replacement split on its comma\nnoticed: a person, frame at 90%\n"
     "changed: replacement → \"a complete description\"\nchecked: re-rendered, frame re-read",
     "Four lines.",
     "So it went in the log. What broke, how it was noticed, what changed, how the change was checked. Four "
     "lines. Anyone reading it can see exactly where the machine went wrong, and exactly where a person "
     "stepped in."),
    ("how much do I log?",
     [("Typo in a draft", "skip it"), ("Fix that taught nothing", "skip it"),
      ("A failure that surprised you", "log it"), ("One others will hit", "log it")],
     "Where this bites. Logging everything turns into noise. Skip the typos and the fixes that taught you "
     "nothing. Log the failures that surprised you, and the ones someone else is likely to hit next."),
    ("Logged", "Polished isn't proof", "broke · noticed · changed",
     "So, the verdict. A polished demo shows the result. A failure log shows the thinking. If you want proof "
     "that you can work with A I, show what broke."),
    ("Write the Entry",
     "Here's what I built this week with AI: [describe it]. Interview me: what broke, how did I notice, what "
     "did I change, and how did I check it? Then write it up as a four-line log entry.",
     "Your turn. Paste this into Claude. Here's what I built this week with A I, and then describe it. "
     "Interview me. What broke, how did I notice, what did I change, and how did I check it? Then write it up "
     "as a four line log entry. Notice that it asks you the questions instead of answering them. Only you "
     "know how you noticed. Run it at the end of every week."),
), [
    ("B00/B03/B04", "11 failures logged while building films 1–4: 1 test build, 5 film 1, 4 films 2–4, 1 previews",
     "TRUE (log)", "ai-fluency/youtube/BUILD-LOG.md"),
    ("B05", "Toolkit caught 4 (GATE F, preview crash, GATE L, GATE V); a person caught 7", "TRUE (log)", "BUILD-LOG.md"),
    ("B07/B08", "Film 2's replacement was split on its comma; fixed with 'a complete description'", "TRUE (log)",
     "BUILD-LOG.md entry 8; hai-beat-sheet-is-the-prompt/beat_sheet.json"),
    ("B02", "A polished demo doesn't prove understanding", "JUDGMENT", "the brief's Brutalist framing; HOW-TO.md §1"),
    ("B09", "Log surprising failures, skip trivial ones", "JUDGMENT", "framed as advice"),
]))

# ── Film 6 ────────────────────────────────────────────────────────────────────
FILMS.append(("hai-workflow-is-the-lesson", film(
    "hai-workflow-is-the-lesson", "The Workflow Is the Lesson", 6,
    "Map an AI-assisted workflow as steps and mark which the machine runs and where a person must check",
    "Jambo, HAI",
    ('claude "make three more films, built the same way as film 1"',
     ["build_films.py · 3 beat sheets", "39 scenes rendered · 4K", "3 review cuts · checked"],
     "Jambo, I'm Bella, for Humanitarians A I. After film one, Claude was asked for three more films, built "
     "the same way. One script wrote all three. That speed only works because of where the workflow makes "
     "a person stop."),
    ("Here's the whole idea.\nA good AI workflow\nremoves the human.", "removes the human", "places your checkpoints",
     "Here's the whole idea. A good A I workflow doesn't remove you. It places your checkpoints. Brutalist is "
     "that kind of workflow, built for video. The machine runs the steps. You stand at the checks."),
    [
     ("This A I fluency skill isn't about any single prompt. It's about the workflow, the repeatable sequence "
      "that turns one good result into many. Done well, the machine does more each time, and you think in the "
      "same places every time.",
      [{"at": "workflow", "event": "the word WORKFLOW fills the frame"}],
      {"kind": "masked", "word": "Workflow", "heading": "The skill", "sub": "repeatable, not one-off"}),
     ("Here's the Brutalist loop. Author the beat sheet. Generate the audio. Render the scenes. Check the "
      "frames. Sign the final. Five stages. The machine runs three of them almost alone. The other two are "
      "built around a person.",
      [{"at": "loop", "event": "path lights Author → Audio → Render → Check → Sign"}],
      {"kind": "paths", "heading": "The loop",
       "items": [{"label": "Author"}, {"label": "Audio"}, {"label": "Render"}, {"label": "Check"}, {"label": "Sign"}],
       "focus": 3, "cues": [0.12, 0.2, 0.28, 0.36, 0.44]}),
     ("Sort them. Generating the audio, rendering thirty nine scenes, compiling the cuts. The machine does "
      "those, fast and without complaint. Deciding what each film argues, reading what the frames actually "
      "show, and choosing whether to sign. Those stay with you.",
      [{"at": "start", "event": "tab: what the machine does"}, {"at": "Deciding", "event": "tabs switch: what you decide"}],
      {"kind": "tabs", "labels": ["Machine", "You"],
       "items": [{"label": "Generate the audio"}, {"label": "Render 39 scenes"}, {"label": "Compile the cuts"}],
       "items2": [{"label": "What each film argues"}, {"label": "What the frames show"}, {"label": "Whether to sign"}],
       "cues": [0.45]}),
     ("What made it repeatable? One script wrote three beat sheets. Every film shares the same thirteen beat "
      "spine. Cards that passed review in film one were reused. The receipts came from the real build. And the "
      "same checks ran on every film.",
      [{"at": "One script", "event": "lens walks the rows"}, {"at": "same checks", "event": "lens lands on the checks row"}],
      {"kind": "focus", "heading": "What made it repeatable",
       "items": rows(("One script", "3 beat sheets"), ("Same spine", "13 beats each"), ("Proven cards", "reused"),
                     ("Real receipts", "from the build"), ("Same checks", "every film")),
       "focus": 4, "cues": [0.14, 0.3, 0.46, 0.62]}),
     ("And the workflow got cheaper. Film one took four compiles to reach a clean cut. Film two took three. "
      "Films three and four took two each. Not because the machine got smarter, but because every failure in "
      "film one became a rule for the next three.",
      [{"at": "four compiles", "event": "line chart draws compiles per film falling"}],
      {"kind": "chart", "heading": "Compiles to a clean cut", "sub": "it got cheaper",
       "labels": ["Film 1", "Film 2", "Film 3", "Film 4"], "values": [4, 3, 2, 2]}),
    ],
    ("One Loop, Three Films", 'claude "audio, render and compile films 2 to 4"',
     ["film 2 · 170.1s · gate-v MAJOR=0", "film 3 · 167.7s · gate-v MAJOR=1", "film 4 · 167.2s · gate-v MAJOR=1"],
     "Here's the real run. One loop, three films. Audio, render, compile, check. Two fifty, two forty eight, "
     "two forty seven. The gate flagged one defect each in films three and four. Machine speed, with the "
     "checks still on."),
    ("build_films.py",
     '"""Author beat sheets + paperwork for films 2-4 of the\nAI Fluency x Brutalist series.\n\n'
     "Same spine as film 1: composer cold open -> hesitant-writer\nBLUF -> five body cards -> ask/result receipt "
     "->\nwhen-not-to -> verdict -> Your Turn -> title layout outro.\n"
     'Every receipt is a real artifact from this series\' own build.\n"""',
     "The shape repeats.",
     "Here's the script itself. What it automates is the shape. The same spine, the same bookends, the same "
     "paperwork. What it can't automate is everything inside. Every line of narration and every receipt was "
     "still written and checked, film by film."),
    ("should I automate this?",
     [("Done once", "do it by hand"), ("Still figuring it out", "do it by hand"),
      ("Done every week", "build the workflow"), ("Others will repeat it", "build the workflow")],
     "Where this bites. Building a workflow too early locks in your mistakes. Do the work by hand while you're "
     "still figuring it out. Build the workflow once you've done it enough to know where the checkpoints belong."),
    ("Placed", "You, not removed", "automate · check · repeat",
     "So, the verdict. A good A I workflow doesn't remove you. It moves you to the places only you can stand, "
     "and makes everything else cheaper every time you run it."),
    ("Map Your Workflow",
     "Here's a task I do with AI every week: [describe it]. Map it as steps, mark which ones you could run "
     "alone and which need my judgment, and tell me where one check would catch the most mistakes.",
     "Your turn. Paste this into Claude. Here's a task I do with A I every week, and then describe it. Map it "
     "as steps, mark which ones you could run alone and which need my judgment, and tell me where one check "
     "would catch the most mistakes. That last answer is your first checkpoint. Run it on the task that eats "
     "most of your week."),
), [
    ("B00/B05", "One script (build_films.py) wrote the beat sheets for films 2–4", "TRUE", "ai-fluency/youtube/build_films.py"),
    ("B00/B04", "39 scenes rendered at 4K for films 2–4", "TRUE (log)", "remotion_scenes.py runs, 13 × 3"),
    ("B03", "Loop: author → audio → render → check → sign", "TRUE", "HOW-TO.md §4; CLAUDE.md rules 2, 4, 5"),
    ("B06", "Compiles to a clean cut: film 1 = 4, film 2 = 3, films 3 & 4 = 2", "TRUE (log)", "GATE V runs; BUILD-LOG.md"),
    ("B07", "First loop run: 170.1 s / 167.7 s / 167.2 s; MAJOR 0 / 1 / 1", "TRUE (log)", "films 2–4 pipeline output"),
    ("B08", "build_films.py docstring shown on screen", "TRUE (trimmed + re-wrapped to fit the card)", "build_films.py module docstring"),
    ("B09", "Automate only after doing it by hand enough", "JUDGMENT", "framed as advice"),
]))


if __name__ == "__main__":
    langs = {"hai-show-what-broke": "markdown", "hai-workflow-is-the-lesson": "python"}
    for slug, sheet, facts in FILMS:
        b01 = sheet["beats"][1]["shot"]["remotion"]["props"]
        b01.update(charMs=20, hesitateBetween=6, hesitateWithin=1, mistakeRate=2)
        assert "," not in b01["triggerWords"] + b01["replacementWords"], slug
        sheet["beats"][8]["shot"]["remotion"]["props"]["language"] = langs[slug]
        folder = HERE / slug
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
        paperwork(folder, sheet, facts)
        words = sum(len(b["narration_text"].split()) for b in sheet["beats"])
        print(f"{slug}: {len(sheet['beats'])} beats, {words} words")
