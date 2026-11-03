# -*- coding: utf-8 -*-
"""Authoring script for "AI Status Reports: Trust, but Verify" ai-explainer.

ai-explainer (claude-explainer) CONCEPT explainer, @HumanitariansAI channel,
af_bella (female) voice, narrated first-person as Sanjana Rao. Register: Plain
(HAI students) / Teardown-warm.

Topic: the AI in project tools now auto-writes your status reports. The reusable
framework the film teaches is THE SIGN-OFF -- AI drafts the status; YOU sign it.
Before an AI-written status goes to a stakeholder, verify three things:
  1. SOURCED?   every claim points to a real ticket/date, not confident filler
  2. CURRENT?   the board behind it isn't stale
  3. COMPLETE?  you added the off-board truth the AI can't see
Three pass -> sign & send. Any fail -> fix it first.
Worked example (T05): a clean draft verified + one off-board risk line added -> signed.
Falsifiability (T06): an "all green, on track" report that fails all three
(unsourced guess / 10-day-stale board / invisible blocker) -> do not send.

Graphics are a NEW visual language vs prior films (status-report cards with
verification stamps, a traffic light the AI sets vs the truth, a sign-off gate) in
the Claude fidelity palette. Rendered prop strings stay ASCII (Remotion).
"""
import json, pathlib

TOPIC = "Irreducibly Human"            # claude-hai branding kicker is LOCKED
SEG = "AI Status Reports"
FOLDER = "@HumanitariansAI"


def composer(greeting, command, runningText, segment, output=None):
    return {"pattern": "ClaudeComposerAsk",
            "props": {"greeting": greeting, "topic": TOPIC, "segment": segment,
                      "command": command, "runningText": runningText,
                      "folderLabel": FOLDER, "modelLabel": "Claude",
                      "effortLabel": "High", "output": output or []},
            "rendered": {"out": "", "at": ""}}


def manim(scene_class):
    return {"scene_class": scene_class, "file": "scenes.py"}


def beat(bid, act, role, narration, shot, est, extra=None):
    b = {"beat_id": bid, "act": act, "role_note": role, "narration_text": narration,
         "shot": shot, "estimated_duration_s": est, "voice": "af_bella",
         "engine": "kokoro", "voice_kokoro": "af_bella"}
    if extra:
        b.update(extra)
    return b


beats = []

beats.append(beat(
    "T00", "INTRO",
    "COLD OPEN LAW -- ClaudeComposerAsk, ask answered; first-person Sanjana",
    "Hi, I'm Sanjana, a project manager at Humanitarians AI. Here's something "
    "that's quietly become normal: the AI in your project tools will now write "
    "your status report for you. One click, and out comes a clean paragraph you "
    "can send to your boss or your client. It sounds great. But a status report "
    "has your name on it. So the real question isn't whether the AI can write it. "
    "It's whether you can trust what it wrote -- before you hit send.",
    {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
     "remotion": composer(
         "Hi, Sanjana",
         "The AI in my project tools can auto-write a status report for my "
         "stakeholders. How do I know I can trust it before I send it?",
         "drafting the status report...",
         "AI Status Reports",
         ["AI can draft the status -- it reads your board fast",
          "but it's only as true as the board behind it",
          "verify three things before you sign and send"])},
    25.0))

beats.append(beat(
    "T01", "OVERVIEW",
    "EXECUTIVE-SUMMARY LAW -- hesitant-writer BLUF; corrects the reel's real misconception",
    "Here's the whole idea in one breath. It's tempting to treat the AI's status "
    "report as the status itself. It isn't. It's a draft built only from what's on "
    "your board -- and a confident paragraph can hide an empty or stale one. Your "
    "job is to verify it before you sign it.",
    {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
     "remotion": {
         "pattern": "BrutalistHesitantWriter",
         "props": {
             "text": "The AI's status report is the status.\nIf it says on track, we're on track.",
             "face": "serif", "fontSize": 50, "lineSpacing": 1.3, "align": "center",
             "triggerWords": "is the status, If it says on track, we're on track",
             "replacementWords": "is a draft, It's only as true as the board behind it",
             "mistakeRate": 6, "hesitateWithin": 3, "hesitateBetween": 22,
             "charMs": 55, "jitter": 28, "seed": "status-bluf-01",
             "showCaret": True, "brandLabel": "@HumanitariansAI",
             "contextTitle": "The whole idea in one breath",
             "contextItems": [
                 {"label": "AI", "detail": "drafts the status fast -- reads the board, writes the prose"},
                 {"label": "You", "detail": "sign it -- verify it's sourced, current, complete first"},
             ],
         }, "rendered": {"out": "", "at": ""}}},
    15.0, {"lead_silence_s": 0.8}))

beats.append(beat(
    "T02", "PROBLEM",
    "SHOW-DON'T-TELL: the AI writes a confident green status; green is a judgment, not a fact",
    "So here's the situation. Every tool now has a summarize-this-sprint button, "
    "and the paragraph it gives you is genuinely good writing -- clear, confident, "
    "ready to send. That's the trap. The AI sets the status to green by counting "
    "closed tickets. But green isn't a fact -- it's a judgment about whether you'll "
    "actually make it. The AI can't see the vendor who's gone quiet, the engineer "
    "who's out, the call that moved the deadline. As a time-saver, it's a gift. As "
    "the truth, it's a liability.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "AI generates a status card with a green ON TRACK badge + "
     "smooth prose lines; a traffic light the AI has set to GREEN. Then the real "
     "signal is revealed as AMBER behind it (hidden: vendor quiet, engineer out, "
     "deadline moved). Reframe: time-saver (gift) vs the truth (liability). "
     "Terracotta on the reframe.",
     "manim": manim("T02_GreenByDefault")},
    32.0))

beats.append(beat(
    "T03", "FRAMEWORK",
    "framework-first (PROOF): the 3 checks, shown BEFORE any example",
    "So before you forward anything the AI wrote, verify three things. One: is it "
    "sourced? Every claim should point to something real on the board -- a closed "
    "ticket, an actual date -- not smooth prose filling a gap. Two: is it current? "
    "A status is only as true as the board behind it, and the AI will happily "
    "summarize a board nobody's touched in two weeks. Three: is it complete? The "
    "most important line is usually the one that isn't logged anywhere -- the "
    "blocker in a Slack thread, the risk from a call. Three checks pass, you sign "
    "it. Any check fails, you fix it first.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "Three checks stacked: 1 SOURCED? (points to a real ticket vs "
     "confident filler) 2 CURRENT? (board fresh vs stale) 3 COMPLETE? (off-board "
     "truth added vs missing). Each with a green pass test and a red failure. Footer "
     "rule: 3 PASS -> SIGN & SEND | any FAIL -> fix first. Terracotta on the footer.",
     "manim": manim("T03_SignOff")},
    34.0))

beats.append(beat(
    "T04", "ASK",
    "ASK->RESULT LAW -- composer ask that generates the T05 draft",
    "Let's run a real one. Here's the end of a sprint. Watch me ask the AI to "
    "draft the status -- but only to draft it. Pull what's on the board into a "
    "clean update. Don't decide if we're on track, and don't invent anything.",
    {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
     "remotion": composer(
         "The draft,",
         "Draft a sprint status update from my board for the client. Pull straight "
         "from the tickets -- what's done, in progress, and blocked. Don't declare "
         "on-track or at-risk, and don't add anything that isn't on the board. Mark "
         "anything you're unsure about.",
         "drafting from the board...",
         "Worked example: draft the status")},
    15.0))

beats.append(beat(
    "T05", "RESULT",
    "worked example walked through the framework -- verified, then the human adds COMPLETE",
    "And there's the draft -- eight of ten tickets closed, two in progress, written "
    "up cleanly. Now verify it. Sourced? Yes, every line matches a real ticket. "
    "Current? Yes, I updated the board this morning. Complete? Almost -- and this is "
    "the part only I can do. The export feature depends on a vendor API that's been "
    "flaky all week, and that's on no card anywhere. I add one line flagging it as "
    "a risk. Now it's sourced, current, and complete. I sign it, and I send it.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "Left: the AI draft status card (8/10 closed, 2 in progress). "
     "Apply stamps: SOURCED check, CURRENT check. Then the HUMAN adds one line -- "
     "'Risk: export depends on a flaky vendor API' -- and COMPLETE check lands -> a "
     "green SIGNED & SENT verdict. Green accent on the sign-off.",
     "manim": manim("T05_VerifyGreen")},
    27.0))

beats.append(beat(
    "T06", "FALSIFIABILITY",
    "falsifiability -- the confident all-green report that fails all three checks",
    "Now the trap -- because a clean green report is so easy to forward. Same "
    "button, different sprint. The AI writes: project on track, all green. Looks "
    "perfect. Verify it. Sourced? No -- on track is the AI's guess from counting "
    "tickets; the board never says it. Current? No -- nobody's touched this board "
    "in ten days, because the team quietly moved to a hotfix. So the AI is "
    "summarizing a fossil. Complete? No -- the real blocker, a key engineer out "
    "sick, is nowhere on it. Three fails. Forward that, and you've told your client "
    "a confident lie. The test is what catches it before you do.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "A confident 'ON TRACK - all green' status card, then three "
     "RED stamps land: UNSOURCED (the AI's guess, not on the board), STALE (board "
     "untouched 10 days -> a fossil), INCOMPLETE (key engineer out, not logged) -> "
     "a red DO NOT SEND verdict. Terracotta/red on the failures.",
     "manim": manim("T06_GreenLie")},
    37.0))

beats.append(beat(
    "T07", "SUMMARY",
    "reusable rubric restated -- AI DRAFTS, you SIGN (sourced/current/complete)",
    "So here's the rule you can carry to any tool. Let the AI draft -- it reads the "
    "board and writes the prose faster than you ever will. But you sign it. And "
    "your signature means you checked three things: that every claim is sourced, "
    "that the board is current, and that you added what the AI couldn't see. The AI "
    "writes the paragraph. You write the one line that actually matters.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "A clean router: LEFT 'AI DRAFTS -- reads the board, writes "
     "the prose'. A center gate = the three checks SOURCED / CURRENT / COMPLETE. "
     "RIGHT 'YOU SIGN -- send it to the stakeholder'. High negative space, "
     "terracotta accent on the signature gate.",
     "manim": manim("T07_Router")},
    27.0))

beats.append(beat(
    "T08", "NEXT STEPS",
    "HANDOFF LAW -- ClaudeComposerAsk 'Your turn.'; prompt read aloud + discussed",
    "Your turn. Next time your tool offers to write your status, don't just copy it "
    "out. Run this prompt: have the AI draft the update, but make it tag every "
    "single claim with the exact ticket or date it came from -- and separately list "
    "everything it could not verify from the board alone. Read that second list "
    "closely. That's your verification checklist, handed to you. A good answer gives "
    "you a sourced draft plus an honest here's-what-I-couldn't-see. A bad one gives "
    "a confident paragraph with no sources -- and now you know that's the one never "
    "to forward.",
    {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
     "remotion": composer(
         "Your turn.",
         "Draft my sprint/project status from the board below.\n[PASTE YOUR BOARD]\n\n"
         "1. SOURCED: tag every claim with the exact ticket ID or date it came from.\n"
         "2. SEPARATE: list everything you canNOT verify from the board alone\n"
         "   (on-track / at-risk judgments, off-board risks, anything stale).\n"
         "3. Do NOT declare on-track or at-risk yourself -- leave that to me.\n"
         "Give me (a) the sourced draft and (b) the 'could not verify' list.",
         "paste your own board into Claude...",
         "Run it on your own status")},
    35.0))

beats.append(beat(
    "T09", "OUTRO",
    "OUTRO LAW -- title restate; @HumanitariansAI card (house outro is @NikBearBrown-locked)",
    "AI status reports -- trust, but verify. With Sanjana Rao, for Humanitarians "
    "AI. Let the AI draft it. You sign it. Thanks for watching.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "manim": manim("T09_Outro")},
    12.0))


sheet = {
    "metadata": {
        "title": "AI Status Reports: Trust, but Verify",
        "slug": "ai-status-reports",
        "topic": TOPIC, "register": "Plain / Teardown-warm",
        "audience": "Humanitarians AI", "brand": "claude-hai",
        "channel_title": "@HumanitariansAI", "creator": "Sanjana Rao",
        "engine": "kokoro", "palette": "claude", "style_preset": "claude",
        "style": "claude-explainer", "voice_kokoro": "af_bella",
        "voice_policy": "persistent-fellow-selected", "voice_approval": "APPROVED",
        "approvals": {"voice": {"status": "approved", "reviewer_type": "human",
                                "reviewed_by": "Sanjana Rao",
                                "reviewed_at": "2026-10-08T12:00:00+00:00",
                                "subject_sha256": "d3486a7ac5d092a1899e7d5610728c96d03bf769ed2c423635e04dbd98e04bf4"}},
        "aspect_ratio": "16:9",
        "note": "ai-explainer CONCEPT explainer for @HumanitariansAI, first-person "
                "Sanjana Rao (af_bella). Topic: trusting AI-generated project status "
                "reports. Framework = THE SIGN-OFF: AI drafts, you sign; verify "
                "SOURCED / CURRENT / COMPLETE before it reaches a stakeholder.",
        "tags": ["Humanitarians AI", "Sanjana Rao", "project management",
                 "AI status report", "project status", "Jira", "Asana", "Notion AI",
                 "when to use AI", "Claude", "stakeholder update"],
        "total_estimated_duration_seconds": int(sum(b["estimated_duration_s"] for b in beats)),
    },
    "beats": beats,
}
out = pathlib.Path(__file__).resolve().parent / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2), encoding="utf-8")
print(f"wrote {out}  ({len(beats)} beats, est {sheet['metadata']['total_estimated_duration_seconds']}s)")
