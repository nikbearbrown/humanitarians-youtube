# -*- coding: utf-8 -*-
"""Authoring script for the "AI in Project Management Tools" ai-explainer reel.
Emits beat_sheet.json in the ai-explainer (claude-explainer) spine:
  cold open (ClaudeComposerAsk) -> hesitant-writer BLUF (BrutalistHesitantWriter)
  -> concept-illustration body (Manim) -> Your-Turn handoff -> title outro.

Claude skin, @HumanitariansAI channel, af_bella (female) voice, narrated
first-person as Sanjana Rao. Register: Plain (HAI students) / Teardown-warm.

Topic: AI is now inside Jira, Trello, Asana, ClickUp, Notion. The reusable
framework the film teaches is THE TICKET TEST -- three questions to ask before
you let AI DO a task on your board:
  1. MECHANICAL?  reshaping info that exists  vs  making a call
  2. REVERSIBLE?  cheap to check & undo       vs  teammates commit on it
  3. IN THE TOOL? the truth is written down    vs  it lives in someone's head
Three greens -> let AI DRAFT it. Any red -> AI suggests, a human DECIDES.
The Manim beats visualise the same rubric the narration argues; nothing is
invented -- the worked ticket and the trap case are both scored on those axes.
"""
import json, pathlib

TOPIC = "Irreducibly Human"
SEG = "AI in Project Management Tools"
FOLDER = "@HumanitariansAI"

def composer(greeting, command, runningText, output=None, segment=SEG):
    return {
        "pattern": "ClaudeComposerAsk",
        "props": {
            "greeting": greeting,
            "topic": TOPIC,
            "segment": segment,
            "command": command,
            "runningText": runningText,
            "folderLabel": FOLDER,
            "modelLabel": "Claude",
            "effortLabel": "High",
            "output": output or [],
        },
        "rendered": {"out": "", "at": ""},
    }

def hesitant(text, triggers, replacements, seed):
    return {
        "pattern": "BrutalistHesitantWriter",
        "props": {
            "text": text,
            "face": "serif",
            "fontSize": 58,
            "lineSpacing": 1.3,
            "align": "center",
            "triggerWords": triggers,
            "replacementWords": replacements,
            "mistakeRate": 6,
            "hesitateWithin": 3,
            "hesitateBetween": 22,
            "charMs": 55,
            "jitter": 28,
            "seed": seed,
            "showCaret": True,
            "brandLabel": FOLDER,
            "contextTitle": "The whole idea in one breath",
            "contextItems": [
                {"label": "AI", "detail": "drafts & surfaces the busywork -- tickets, summaries, first passes"},
                {"label": "You", "detail": "decide & commit -- what matters, what date, who's doing what"},
            ],
        },
        "rendered": {"out": "", "at": ""},
    }

# The viewer's suggested prompt (READ ALOUD + discussed per HANDOFF LAW).
HANDOFF_CMD = (
    "Here is a paste from my Jira / Trello board -- raw notes, half-written cards,\n"
    "and a stand-up transcript.\n"
    "[PASTE YOUR BOARD + NOTES]\n\n"
    "1. DRAFT: turn the loose notes into clean tickets -- title, type, a short\n"
    "   description, and a rough size. Group duplicates.\n"
    "2. SURFACE: flag stale cards, missing owners, and anything blocked.\n"
    "3. STOP at judgment: do NOT pick the sprint, commit dates, or rank priority.\n"
    "   For each of those, ask me the one question you'd need answered to decide.\n"
    "4. Mark any card whose real context is NOT on the board -- I'll fill it in."
)

beats = [
    # T00 INTRO -- COLD OPEN LAW: Claude UI, ask lands answered; first-person Sanjana
    {"beat_id": "T00", "act": "INTRO",
     "role_note": "COLD OPEN LAW -- ClaudeComposerAsk, ask answered; first-person Sanjana greeting",
     "narration_text": (
        "Hi, I'm Sanjana, a project manager at Humanitarians AI, and this video is about the AI "
        "that just showed up inside your project tools -- Jira, Trello, Asana, Notion. It can write "
        "your tickets, summarize your stand-up, even suggest what to do next. So the real question "
        "isn't whether it's smart. It's which of your project work you should actually hand to it -- "
        "and which you should keep. I'll give you a three-question test for exactly that."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer(
                  "Hi, Sanjana",
                  "AI is now inside Jira, Trello, and Asana. Help me decide which project work "
                  "to hand to it -- and which to keep for a human.",
                  "sorting the board work...",
                  ["AI is great at reshaping what's already written down",
                   "it should DRAFT and SURFACE, never DECIDE and COMMIT",
                   "one test tells you which side a task is on"])},
     "estimated_duration_s": 20},

    # T01 BLUF -- EXECUTIVE-SUMMARY LAW: the hesitant writer, misconception corrected
    {"beat_id": "T01", "act": "OVERVIEW",
     "role_note": "BrutalistHesitantWriter -- BLUF; corrects the reel's actual misconception",
     "narration_text": (
        "Here's the whole idea in one breath. It's tempting to think the AI in these tools will run "
        "the project for you. It won't. What it's genuinely good at is the busywork -- turning notes "
        "into tickets, summarizing, tidying. The judgment stays yours."),
     "lead_silence_s": 0.8,
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": hesitant(
                  "AI in Jira and Trello will run the whole project for you.\n"
                  "Your job is just to watch it work.",
                  "run the whole project for you, just to watch it work",
                  "do the busywork fast, to make the judgment calls",
                  seed="ai-pm-bluf-01")},
     "estimated_duration_s": 13},

    # T02 PROBLEM -- the landscape + the hope vs the reality (stakes before the framework)
    {"beat_id": "T02", "act": "PROBLEM",
     "role_note": "SHOW-DON'T-TELL: AI is in every tool now; the hope (autopilot) vs the reality (a fast intern)",
     "narration_text": (
        "So here's the situation. Almost every board you open now has an AI button. And the pitch is "
        "always the same: point it at your project and it'll basically manage it. But watch what "
        "happens when you actually lean on it. Ask it to run the sprint and it will confidently "
        "commit dates it has no way to know, off a board that's half out of date. It doesn't fail "
        "loudly -- it fails politely, with a clean-looking answer. Treated like an autopilot, it's a "
        "liability. Treated like a very fast intern, it's a gift."),
     "visual_intent": (
        "Top: a row of PM-tool chips (Jira, Trello, Asana, Notion, ClickUp) each sprouting a small "
        "AI spark. Below, a split: LEFT 'the hope' -- an AUTOPILOT badge over a project that steers "
        "itself (muted); RIGHT 'the reality' -- a FAST INTERN badge: quick, tireless, but needs "
        "checking. Terracotta on the reframe autopilot -> intern."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "T02_Landscape", "file": "scenes.py"}},
     "estimated_duration_s": 24},

    # T03 FRAMEWORK -- THE TICKET TEST, shown BEFORE the examples (framework-first)
    {"beat_id": "T03", "act": "FRAMEWORK",
     "role_note": "framework-first (PROOF): the 3-question Ticket Test before any worked example",
     "narration_text": (
        "So before you hand anything to the AI, run it through one test. Three questions. One: is it "
        "mechanical? Reshaping information that already exists -- summarizing, drafting, sorting -- "
        "or is it a call, like choosing what matters. Two: is it reversible? Can you check it in "
        "seconds and undo it, or do teammates act on it the moment it's posted. Three: is the truth "
        "actually in the tool? Or does it live in someone's head, a client call, a Slack thread the "
        "AI can't see. Three greens, let the AI draft it. Any red, the AI can suggest -- but a human "
        "decides."),
     "visual_intent": (
        "Three big stacked question rows, each lighting up in turn: 1 MECHANICAL? (reshape vs decide) "
        "2 REVERSIBLE? (check & undo vs others commit) 3 IN THE TOOL? (written down vs in a head). "
        "Each row shows a green check side and a red side. Footer rule: '3 greens -> AI DRAFTS | any "
        "red -> a HUMAN DECIDES'. Terracotta accent on the footer rule."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "T03_TicketTest", "file": "scenes.py"}},
     "estimated_duration_s": 26},

    # T04 ASK -- ClaudeComposerAsk: the drafting ask (ASK->RESULT pair with T05)
    {"beat_id": "T04", "act": "ASK",
     "role_note": "ASK->RESULT LAW -- the composer ask that generates the T05 result; SPARK 'The green case,'",
     "narration_text": (
        "Let's run a real one. Here's a stand-up note -- the kind of half-sentence mess we all paste "
        "into a board. Watch me hand it to the AI, but only for the mechanical part: turn this into "
        "clean tickets. Don't decide anything, don't set dates -- just draft."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer(
                  "The green case,",
                  "Turn this stand-up note into clean Trello cards -- title, type, one-line "
                  "description, rough size. Don't set priority or dates. Notes: \"login still flaky "
                  "on Safari, Priya looking; export button 500s on big files; need copy for the "
                  "empty dashboard state; someone bumped the staging DB again\"",
                  "drafting cards from the note...",
                  segment="Worked Example: draft the tickets")},
     "estimated_duration_s": 16},

    # T05 RESULT -- the tickets, scored GREEN on the Ticket Test (worked example)
    {"beat_id": "T05", "act": "RESULT",
     "role_note": "worked example walked through the framework -- three greens, so AI drafts",
     "narration_text": (
        "And there it is. Four messy lines became four clean cards -- a bug, a bug, a content task, "
        "an ops note -- each with a type and a rough size. Now score it on the test. Mechanical? "
        "Yes, it just reshaped what I already wrote. Reversible? Completely -- I can read all four in "
        "ten seconds and fix any of them. In the tool? Yes, everything it used was right there in my "
        "note. Three greens. This is exactly the work to hand over -- and it just saved me the "
        "boring ten minutes."),
     "visual_intent": (
        "Left: the raw 4-line stand-up note. Arrow. Right: four structured ticket cards (title / type "
        "chip / size), typing in one by one. Below, THE TICKET TEST scorecard for this task: "
        "MECHANICAL check, REVERSIBLE check, IN THE TOOL check -> a green 'AI DRAFTS' verdict."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "T05_DraftGreen", "file": "scenes.py"}},
     "estimated_duration_s": 24},

    # T06 FALSIFIABILITY -- the trap: same tool, same AI, RED verdict (edge case shown)
    {"beat_id": "T06", "act": "FALSIFIABILITY",
     "role_note": "the falsifiability case -- a task that LOOKS like AI work but scores red; the stale-board trap",
     "narration_text": (
        "Now the trap -- because 'AI is helpful on my board' is too easy to believe. Same tool, same "
        "AI, one step further: pick this sprint and commit the dates. Score it. Mechanical? No -- "
        "that's a judgment call about what matters. Reversible? No -- the moment it's posted, five "
        "people plan around it. In the tool? No -- the reason we're doing the export work first is a "
        "customer call that never made it onto any card. Three reds. And here's the sneaky one: even "
        "'just summarize our progress' turns red if the board is stale, because now the AI is "
        "confidently reporting fiction. The test is what tells them apart."),
     "visual_intent": (
        "Same scorecard frame as T05 for continuity, now the task 'PICK THE SPRINT + COMMIT DATES': "
        "MECHANICAL x, REVERSIBLE x, IN THE TOOL x -> red 'HUMAN DECIDES'. Then a second mini-row "
        "'SUMMARIZE PROGRESS' flips from a hopeful green to red with a 'STALE BOARD' stamp -- in the "
        "tool? fails. Terracotta on the red verdicts."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "T06_DecideRed", "file": "scenes.py"}},
     "estimated_duration_s": 27},

    # T07 SUMMARY -- the routing rule as the reusable takeaway (verdict card)
    {"beat_id": "T07", "act": "SUMMARY",
     "role_note": "reusable rubric restated -- DRAFT & SURFACE (AI) vs DECIDE & COMMIT (you)",
     "narration_text": (
        "So here's the rule you can carry to any tool. Give the AI the two verbs it's built for: "
        "draft and surface. Draft the tickets, the summaries, the first pass. Surface what's stale, "
        "unowned, or blocked. Keep the two verbs that need a human: decide and commit. What we do "
        "this sprint, what date we promise, how someone's doing. Run the three-question test when "
        "you're not sure which side a task is on. That's the whole skill -- not 'use AI' or 'don't,' "
        "but knowing where the line is."),
     "visual_intent": (
        "A clean two-column router. LEFT 'HAND TO AI -> DRAFT & SURFACE' with its verbs (draft "
        "tickets, summarize, tidy, flag stale/blocked). RIGHT 'KEEP FOR A HUMAN -> DECIDE & COMMIT' "
        "(pick scope, commit dates, judge people, own the call). Between them a vertical rule = THE "
        "TICKET TEST. High negative space, terracotta accent on the dividing test."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "T07_Router", "file": "scenes.py"}},
     "estimated_duration_s": 22},

    # T08 HANDOFF -- HANDOFF LAW: prompt READ ALOUD and discussed; greeting 'Your turn.'
    {"beat_id": "T08", "act": "NEXT STEPS",
     "role_note": "HANDOFF LAW -- ClaudeComposerAsk 'Your turn.'; prompt read aloud + discussed",
     "narration_text": (
        "Your turn. Open your own board and paste a real mess into Claude -- loose notes, half-"
        "written cards, a stand-up transcript. This prompt tells it exactly where the line is: draft "
        "the tickets and surface what's stale, but stop at judgment -- don't pick the sprint or "
        "commit dates. And this is the important line: for every call it can't make, it has to ask "
        "you the one question it would need answered. A good answer comes back with clean drafts and "
        "a short list of questions. A bad one quietly makes the decisions for you -- and now you "
        "know that's the exact thing to catch."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer(
                  "Your turn.", HANDOFF_CMD,
                  "paste your own board into Claude...",
                  segment="Run the test on your own board")},
     "estimated_duration_s": 24},

    # T09 OUTRO -- OUTRO LAW: title restate, HAI channel
    {"beat_id": "T09", "act": "OUTRO",
     "role_note": "OUTRO LAW -- title restate; @HumanitariansAI card",
     "narration_text": (
        "AI in project management tools -- with Sanjana Rao, for Humanitarians AI. Let it draft and "
        "surface. You decide and commit. Thanks for watching."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "T09_Outro", "file": "scenes.py"}},
     "estimated_duration_s": 10},
]

# Remotion mangles non-ASCII props on this Windows setup. Keep every RENDERED
# prop string ASCII; narration_text (TTS only) keeps unicode.
_ASCII = {"·": " | ", "…": "...", "—": " - ", "–": "-",
          "’": "'", "‘": "'", "“": '"', "”": '"',
          "×": "x", "−": "-", "→": "->"}
def _san(x):
    if isinstance(x, str):
        for a, b in _ASCII.items():
            x = x.replace(a, b)
        return x
    if isinstance(x, list):
        return [_san(i) for i in x]
    if isinstance(x, dict):
        return {k: _san(v) for k, v in x.items()}
    return x

for b in beats:
    rem = b.get("shot", {}).get("remotion")
    if rem and "props" in rem:
        rem["props"] = _san(rem["props"])
    b.setdefault("voice", "af_bella")
    b["engine"] = "kokoro"
    b["voice_kokoro"] = "af_bella"
    b.setdefault("build", {"status": "SLATE"})

sheet = {
    "metadata": {
        "title": "AI in Your Project Management Tools: What to Hand Over, What to Keep",
        "slug": "ai-project-management-tools",
        "topic": TOPIC,
        "register": "Plain / Teardown-warm",
        "audience": "Humanitarians AI",
        "brand": "claude-hai",
        "channel_title": "@HumanitariansAI",
        "creator": "Sanjana Rao",
        "engine": "kokoro",
        "palette": "claude",
        "style_preset": "claude",
        "style": "claude-explainer",
        "voice_kokoro": "af_bella",
        "voice_policy": "persistent-fellow-selected",
        "voice_approval": "APPROVED",
        # Sanjana Rao selected + approved af_bella as her persistent fellow voice
        # (this reel + all three prior HAI films), authorized in chat 2026-09-29.
        # subject_sha256 = digest of {engine: kokoro, voice: af_bella}.
        "approvals": {
            "voice": {
                "status": "approved",
                "reviewer_type": "human",
                "reviewed_by": "Sanjana Rao",
                "reviewed_at": "2026-09-29T12:00:00+00:00",
                "subject_sha256": "d3486a7ac5d092a1899e7d5610728c96d03bf769ed2c423635e04dbd98e04bf4",
            }
        },
        "aspect_ratio": "16:9",
        "note": ("ai-explainer (claude-explainer) for @HumanitariansAI, narrated first-person by "
                 "Sanjana Rao (af_bella). Claude skin bookends + hesitant-writer BLUF; concept-"
                 "illustration Manim body in the Claude palette. Framework: The Ticket Test "
                 "(mechanical? reversible? in the tool?) -> AI drafts & surfaces, humans decide & commit."),
        "tags": ["project management", "AI project management", "Jira", "Trello", "Asana",
                 "Atlassian Intelligence", "Notion AI", "when to use AI", "AI ticketing",
                 "Humanitarians AI", "Sanjana Rao", "Claude"],
        "total_estimated_duration_seconds": sum(b["estimated_duration_s"] for b in beats),
    },
    "beats": beats,
}

out = pathlib.Path(__file__).parent / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=1, ensure_ascii=False), encoding="utf-8")
print("wrote", out, "with", len(beats), "beats;",
      "est", sheet["metadata"]["total_estimated_duration_seconds"], "s")
