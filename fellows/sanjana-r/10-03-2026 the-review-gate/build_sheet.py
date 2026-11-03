# -*- coding: utf-8 -*-
"""Authoring script for "The Review Gate" ai-explainer PROGRESS-RECORD reel.

ai-explainer (claude-explainer) spine, @HumanitariansAI channel, af_bella (female)
voice, narrated first-person as Sanjana Rao. Register: Plain (HAI) / Teardown-warm.

This is a PROGRESS RECORD, not a concept explainer: the data is Sanjana's own
video-review tracker, window = the LAST TWO WEEKS OF SEPTEMBER 2026 (Sep 16-30).
Every number on screen is verified from that tracker -- no fabrication (PROOF).

The teachable framework (shown BEFORE the examples) is THE REVIEW GATE -- the
three checks every fellow video clears before it reaches a professor:
  1. 4K ON BOTH CUTS?   true 4K for the 16:9 AND the 9:16 short
  2. RIGHT BRANDING?     @HumanitariansAI, not a leftover @NikBearBrown
  3. CODE ON GITHUB?     committed + correct dimensions
  3 pass -> APPROVED -> Prof. Nina.   Any fail -> back to the fellow with an email.

Verified aggregates (Sep 16-30, "September Videos" sheet):
  88 videos reviewed | 22 fellows | 8 projects
  78 approved / 10 needs-modifications | 71 on GitHub (of 88)
  projects: Brutalist 41, Madison 18, AI+1 14, Lyrical Literacy 4,
            Causal Couture 4, Raman Effect 3, Relocation Engine 2, Walker 2
  worked (green) example: Jainil - Brutalist (4), approved
  fail->fix->re-approve loop: Deepa (16), Harshitha (8), Neelabh (1)

Graphics are a NEW visual language vs prior films (gate/conveyor stations, stat
tiles, lollipop ranking, segmented approval bar, compliance arc, fix-loop) -- the
Claude fidelity palette throughout. Rendered prop strings stay ASCII (Remotion).
"""
import json, pathlib

TOPIC = "Irreducibly Human"            # claude-hai branding kicker is LOCKED to this
SEG = "The Review Gate"
FOLDER = "@HumanitariansAI"


def composer(greeting, command, runningText, segment, output=None):
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


def manim(scene_class):
    return {"scene_class": scene_class, "file": "scenes.py"}


def beat(bid, act, role, narration, shot, est, extra=None):
    b = {
        "beat_id": bid,
        "act": act,
        "role_note": role,
        "narration_text": narration,
        "shot": shot,
        "estimated_duration_s": est,
        "voice": "af_bella",
        "engine": "kokoro",
        "voice_kokoro": "af_bella",
    }
    if extra:
        b.update(extra)
    return b


beats = []

# ---- T00 COLD OPEN (ClaudeComposerAsk, ask answered) ------------------------
beats.append(beat(
    "T00", "INTRO",
    "COLD OPEN LAW -- ClaudeComposerAsk, ask answered; first-person Sanjana",
    "Hi, I'm Sanjana, a project manager at Humanitarians AI. Over the last two "
    "weeks of September, eighty-eight fellow videos landed on my desk for review. "
    "This isn't a highlights reel. It's the record -- what I actually did, how I "
    "checked each one, and what made it through. Because reviewing isn't watching "
    "and clicking approve. Every video runs a gate first. Let me show you the "
    "gate, and the two weeks it sorted.",
    {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
     "remotion": composer(
         "Hi, Sanjana",
         "Here are my fellow-video review logs for the last two weeks of "
         "September. Walk through what I did -- how many, how I checked them, and "
         "what got approved.",
         "sorting two weeks of reviews...",
         "The Review Gate",
         ["88 videos reviewed across 22 fellows",
          "each one runs a 3-check quality gate",
          "78 approved, 10 sent back to fix"])},
    25.0))

# ---- T01 OVERVIEW / BLUF (BrutalistHesitantWriter) --------------------------
beats.append(beat(
    "T01", "OVERVIEW",
    "EXECUTIVE-SUMMARY LAW -- hesitant-writer BLUF; corrects the reel's real misconception",
    "Here's the whole thing in one breath. It's easy to picture video review as "
    "hitting play and clicking approve. It isn't. Every one of these eighty-eight "
    "videos went through the same three-check gate before it reached a professor "
    "-- and a lot of them bounced back first.",
    {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
     "remotion": {
         "pattern": "BrutalistHesitantWriter",
         "props": {
             "text": "Reviewing fellow videos is just\nwatching them and clicking approve.",
             "face": "serif",
             "fontSize": 50,
             "lineSpacing": 1.3,
             "align": "center",
             "triggerWords": "watching them and clicking approve",
             "replacementWords": "running each through a 3-check gate",
             "mistakeRate": 6,
             "hesitateWithin": 3,
             "hesitateBetween": 22,
             "charMs": 55,
             "jitter": 28,
             "seed": "review-gate-bluf-01",
             "showCaret": True,
             "brandLabel": "@HumanitariansAI",
             "contextTitle": "The two weeks in one breath",
             "contextItems": [
                 {"label": "The job", "detail": "88 videos, 22 fellows -- checked, not just watched"},
                 {"label": "The gate", "detail": "4K? branding? GitHub? -- pass = approved, fail = back"},
             ],
         },
         "rendered": {"out": "", "at": ""}}},
    15.0, {"lead_silence_s": 0.8}))

# ---- T02 FRAMEWORK -- The Review Gate (shown before examples) ---------------
beats.append(beat(
    "T02", "FRAMEWORK",
    "framework-first (PROOF): the 3-check gate, BEFORE any example",
    "So here's the gate every video has to clear. Check one: is it rendered in "
    "true 4K -- both the wide cut and the vertical short, not just one. Check two: "
    "is the branding right -- the Humanitarians AI handle, not a leftover "
    "NikBearBrown. Check three: is the code on GitHub, with the dimensions "
    "correct. Three passes, it's approved and goes to the professor. Any fail, it "
    "goes back to the fellow with an email saying exactly what to fix.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "Three check-stations stacked; a video card travels through "
     "each: 1 4K ON BOTH CUTS? 2 RIGHT BRANDING (@HumanitariansAI not @NikBearBrown)? "
     "3 CODE ON GITHUB? Each station has a PASS test (green) and a FAIL reason (red). "
     "Footer rule: 3 PASS -> APPROVED -> Prof. Nina | any FAIL -> back to the fellow. "
     "Terracotta on the footer rule.",
     "manim": manim("T02_Gate")},
    37.0))

# ---- T03 ASK (composer -> generates the scoreboard) -------------------------
beats.append(beat(
    "T03", "ASK",
    "ASK->RESULT LAW -- composer ask that generates the T04 scoreboard",
    "Two weeks of notes is a spreadsheet, not a picture. So I did what I'd tell "
    "any fellow to do. I handed the raw tracker to Claude and asked it to turn the "
    "mess into a scoreboard. Not to judge anything -- just to count it, and lay it "
    "out honestly.",
    {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
     "remotion": composer(
         "The scoreboard,",
         "Here's my raw two-week review tracker -- dates, fellows, counts, "
         "approve or modify, GitHub yes/no. Total it up and lay out a scoreboard: "
         "how many reviewed, approved vs sent back, and how many had code on "
         "GitHub. Don't rename or re-judge anything.",
         "counting two weeks of reviews...",
         "Build the scoreboard")},
    16.0))

# ---- T04 RESULT -- the scoreboard -------------------------------------------
beats.append(beat(
    "T04", "RESULT",
    "ASK->RESULT result; sources-on-screen (the real tracker numbers)",
    "And here's the scoreboard. Eighty-eight videos reviewed in two weeks, from "
    "twenty-two different fellows. Of those, seventy-eight cleared the gate and "
    "went up for approval -- ten came back needing fixes. And seventy-one already "
    "had their code on GitHub, where the work can actually be checked. That's the "
    "two weeks, counted honestly -- the good and the sent-back.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "Dashboard: top row three big stat tiles -- 88 VIDEOS "
     "REVIEWED, 22 FELLOWS, 2 WEEKS. Middle: a segmented approval bar 78 APPROVED "
     "(green) | 10 SENT BACK (red). Bottom: a GitHub compliance arc/meter filling "
     "to 71 of 88 (~81%). Small source caption 'Source: September review tracker'. "
     "Terracotta accent on the headline 88.",
     "manim": manim("T04_Scoreboard")},
    28.0))

# ---- T05 BREAKDOWN -- project ranking ---------------------------------------
beats.append(beat(
    "T05", "BREAKDOWN",
    "where the 88 went -- real project split from the tracker",
    "Where did the eighty-eight go? Not evenly. Almost half were Brutalist-toolkit "
    "videos -- forty-one of them -- as that project scaled up. Madison was next at "
    "eighteen, then the AI-plus-one teams at fourteen. The rest spread thin across "
    "Lyrical Literacy, Causal Couture, the Raman Effect, Relocation Engine, and "
    "Walker. Eight projects, one reviewer.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "Horizontal lollipop/bar ranking, 8 rows sorted descending: "
     "Brutalist 41 (terracotta, highlighted), Madison 18, AI+1 14, Lyrical Literacy "
     "4, Causal Couture 4, Raman Effect 3, Relocation Engine 2, Walker 2. Bars grow "
     "to value; counts at the end of each. Title 'Where the 88 went'.",
     "manim": manim("T05_Breakdown")},
    27.0))

# ---- T06 WORKED EXAMPLE -- one video, 3 green -> approved --------------------
beats.append(beat(
    "T06", "WORKED EXAMPLE",
    "worked example -- one real submission walked through the gate, all green",
    "Here's the gate doing its job on a good one. Jainil's Brutalist batch -- four "
    "videos. Rendered in 4K, both cuts? Pass. Branding on the Humanitarians AI "
    "handle? Pass. Code on GitHub? Pass. Three green. So it's approved and uploaded "
    "straight to YouTube for the professors. No email, no back-and-forth -- this is "
    "exactly what a clean submission looks like.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "The gate frame from T02, one video card 'Jainil - Brutalist "
     "(4)' travels through: 4K ON BOTH CUTS check, RIGHT BRANDING check, CODE ON "
     "GITHUB check -- each lights green in turn -> a green APPROVED verdict -> 'to "
     "Prof. Nina for review'. Clean, no fail branch. Green is the accent here.",
     "manim": manim("T06_GreenPass")},
    26.0))

# ---- T07 FALSIFIABILITY -- the fail -> fix -> re-approve loop ----------------
beats.append(beat(
    "T07", "FALSIFIABILITY",
    "falsifiability/edge -- the videos that FAIL the gate, and the fix loop that proves it's real",
    "But most of the work is in the ones that fail. Deepa's batch -- sixteen "
    "videos -- good content, but it needed changes, so it went back with notes. "
    "The next day she fixed them and re-uploaded. Approved. Same story for "
    "Harshitha's eight, and Neelabh's. That's the point of a gate -- not to reject "
    "people, but to catch it, say exactly what's wrong, and let them fix it before "
    "a professor ever sees it.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "A circular fix-loop: SUBMIT -> [GATE: FAIL] -> EMAIL (what "
     "to fix) -> FELLOW FIXES -> RE-SUBMIT -> [GATE: PASS] -> APPROVED. Three real "
     "chips cycle on the loop: Deepa (16), Harshitha (8), Neelabh (1). Terracotta "
     "on the FAIL->EMAIL->FIX arc; green on the final APPROVED. Caption: '10 of 88 "
     "sent back -- these three came back fixed'.",
     "manim": manim("T07_FixLoop")},
    38.0))

# ---- T08 HANDOFF (composer 'Your turn.') ------------------------------------
beats.append(beat(
    "T08", "NEXT STEPS",
    "HANDOFF LAW -- ClaudeComposerAsk 'Your turn.'; prompt read aloud + discussed",
    "Your turn. If you review anyone's work -- or your own -- build a gate instead "
    "of a gut call. Here's the prompt I'd run: paste your log, and have Claude turn "
    "it into a scoreboard and a checklist you apply to every item, the same way "
    "every time. Read what it hands back -- the checklist is the real output. A "
    "good answer gives you three or four checks you can actually run. A vague one "
    "just says 'looks good' -- which is the gut call you're trying to replace.",
    {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
     "remotion": composer(
         "Your turn.",
         "Here's a log of work I review regularly.\n[PASTE YOUR LOG]\n\n"
         "1. SCOREBOARD: total it -- how many, how many passed vs sent back, and\n"
         "   any compliance column (e.g. code committed).\n"
         "2. BUILD THE GATE: from the reasons things got sent back, draft a\n"
         "   3-check gate I can apply to EVERY item the same way.\n"
         "3. For each check give me the PASS test and the FAIL action.\n"
         "Don't re-judge my past calls -- just build the repeatable gate.",
         "paste your own review log into Claude...",
         "Build your own gate")},
    36.0))

# ---- T09 OUTRO -- custom @HumanitariansAI card ------------------------------
beats.append(beat(
    "T09", "OUTRO",
    "OUTRO LAW -- title restate 'The Review Gate'; @HumanitariansAI card (house outro is @NikBearBrown-locked)",
    "The Review Gate -- my two weeks at Humanitarians AI, with Sanjana Rao. Don't "
    "just watch the work. Run it through the gate. Thanks for watching.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "manim": manim("T09_Outro")},
    11.0))


sheet = {
    "metadata": {
        "title": "The Review Gate: My Two Weeks at Humanitarians AI",
        "slug": "the-review-gate",
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
        "approvals": {
            "voice": {
                "status": "approved",
                "reviewer_type": "human",
                "reviewed_by": "Sanjana Rao",
                "reviewed_at": "2026-10-08T12:00:00+00:00",
                "subject_sha256": "d3486a7ac5d092a1899e7d5610728c96d03bf769ed2c423635e04dbd98e04bf4"
            }
        },
        "aspect_ratio": "16:9",
        "note": "ai-explainer PROGRESS RECORD for @HumanitariansAI, narrated "
                "first-person by Sanjana Rao (af_bella). Data = Sanjana's own "
                "video-review tracker, window Sep 16-30 2026. Framework = THE "
                "REVIEW GATE (4K on both cuts? / right branding? / code on "
                "GitHub?) -> 3 pass = approved to Prof. Nina, any fail = back to "
                "the fellow. Every number verified from the tracker.",
        "tags": [
            "Humanitarians AI", "Sanjana Rao", "progress report",
            "video review", "quality gate", "fellows", "Brutalist",
            "project management", "Claude", "two week review"
        ],
        "total_estimated_duration_seconds": int(sum(b["estimated_duration_s"] for b in beats)),
    },
    "beats": beats,
}

out = pathlib.Path(__file__).resolve().parent / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2), encoding="utf-8")
print(f"wrote {out}  ({len(beats)} beats, est {sheet['metadata']['total_estimated_duration_seconds']}s)")
