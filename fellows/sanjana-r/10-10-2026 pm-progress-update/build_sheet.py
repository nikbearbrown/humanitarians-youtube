# -*- coding: utf-8 -*-
"""Authoring script for "The Last Mile" ai-explainer (16:9).

ai-explainer (claude-explainer) PROGRESS RECORD, @HumanitariansAI channel,
af_bella (female) voice, narrated first-person as Sanjana Rao. Register: Plain
(HAI students) / Teardown-warm.

Progress window: the week of Oct 4-10, 2026 (Sanjana's own review log).
Verified numbers (October Videos sheet):
  85 videos reviewed | 13 fellows | 1 project (Mycroft) | 100% on GitHub (14/14)
  12 sent for approval / 2 "Needs Modifications"
  2 rejections (the film's falsifiability cases):
    Onkar Bhujbal -- 8 videos -- stray toolkit (Remotion) footer baked in -> mailed
    Ameya        -- 8 videos -- 9:16 had overlapping text / bad UX (16:9 was nice) -> mailed
  Also: Oct 6 planning calls (Akshay, Jainil); Oct 8 created 4 of her own videos.

The reusable framework the film teaches is THE LAST MILE -- the craft check between
a FINISHED video and a SHIPPED one. Before a fellow video reaches the professors,
verify three things about how the FILE plays:
  1. CLEAN FINISH?  no leftover toolkit footer/watermark baked into the render
  2. PORTRAIT HOLDS?  the 9:16 is its own layout, not a squeezed 16:9 -- no overlap
  3. ON GITHUB?  code + assets committed
Three pass -> upload for the profs. Any fail -> back to the fellow with a mail.

NEW visual language vs prior films (gate-stations/stat-tiles/stamps/routers):
a film-strip throughput counter, an export-style progress checklist, and literal
16:9-vs-9:16 screen PANES that show the portrait defect. Claude fidelity palette.
Rendered prop strings stay ASCII (Remotion mangles non-ASCII on this box).
"""
import json, pathlib

TOPIC = "Irreducibly Human"            # claude-hai branding kicker is LOCKED
SEG = "The Last Mile"
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
    "Hi, I'm Sanjana, a project manager at Humanitarians AI. This week I reviewed "
    "eighty-five fellow videos for the Mycroft project -- thirteen fellows, and every "
    "single one with its code already on GitHub. The old checklist was basically "
    "automatic. So only two came back. And here's the strange part: not for their "
    "content. For the last mile -- the part of a video that's easy to finish, and "
    "easy to miss.",
    {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
     "remotion": composer(
         "Hi, Sanjana",
         "I reviewed 85 fellow videos this week for the Mycroft project, and almost "
         "all of them passed. So what actually sends a finished video back?",
         "reviewing the Mycroft queue...",
         "The Last Mile",
         ["code on GitHub + clean branding -- basically automatic now",
          "what's left is the last mile: how the file actually plays",
          "two went back -- a stray footer, and a broken 9:16"])},
    26.0))

beats.append(beat(
    "T01", "OVERVIEW",
    "EXECUTIVE-SUMMARY LAW -- hesitant-writer BLUF; corrects the reel's real misconception",
    "Here's the whole idea in one breath. It's tempting to think a finished video is a "
    "shipped video. It isn't. The content can be done -- the explainer, the code, the "
    "branding all correct -- and the file still isn't ready. The last mile is how it "
    "actually plays, and that's exactly what I check before a professor ever sees it.",
    {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
     "remotion": {
         "pattern": "BrutalistHesitantWriter",
         "props": {
             "text": "A finished video is ready to upload.\nIf the content is done, it ships.",
             "face": "serif", "fontSize": 50, "lineSpacing": 1.3, "align": "center",
             "triggerWords": "is ready to upload, If the content is done, it ships",
             "replacementWords": "still has a last mile, Done is not shipped -- you check it first",
             "mistakeRate": 6, "hesitateWithin": 3, "hesitateBetween": 22,
             "charMs": 55, "jitter": 28, "seed": "lastmile-bluf-01",
             "showCaret": True, "brandLabel": "@HumanitariansAI",
             "contextTitle": "The whole idea in one breath",
             "contextItems": [
                 {"label": "Content", "detail": "the easy 95% -- the explainer, the code, the branding"},
                 {"label": "Last mile", "detail": "how the file plays -- the part that sent two back"},
             ],
         }, "rendered": {"out": "", "at": ""}}},
    16.0, {"lead_silence_s": 0.8}))

beats.append(beat(
    "T02", "PROBLEM",
    "SHOW-DON'T-TELL: the week's throughput; the old gate is now automatic, so what's left?",
    "Here's the week. Eighty-five videos, thirteen fellows, all on one project -- "
    "Mycroft. A year ago, what sent videos back was process: wrong resolution, wrong "
    "branding, no code committed. This week every one had its code on GitHub and clean "
    "branding. That gate is basically automatic now. So only two came back -- and both "
    "of them looked finished. The problem was never the content. It was the last mile.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "A film-strip of fellow-video frames with a throughput counter "
     "filling to 85; chips: 13 fellows | 1 project (Mycroft) | 100% on GitHub. Then the "
     "'old gate' (resolution/branding/GitHub) lights all-green and reads AUTOMATIC; a "
     "terracotta question lands: 'so what sent 2 back?' -> THE LAST MILE.",
     "manim": manim("T02_WeekThroughput")},
    33.0))

beats.append(beat(
    "T03", "FRAMEWORK",
    "framework-first (PROOF): the 3 last-mile checks, shown BEFORE any example",
    "So before a fellow video goes to the professors, I check the last mile -- three "
    "things. One: clean finish? No leftover toolkit footer or watermark baked into the "
    "render; the tool's chrome should never ship. Two: does the portrait hold? The "
    "nine-by-sixteen is its own layout, not a squeezed landscape -- no overlapping "
    "text. Three: is it on GitHub? Code and assets committed. Three pass, it goes up "
    "for the profs. Any fail, it goes back to the fellow with a mail.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "An export-style checklist (progress-bar rows, not badges): "
     "1 CLEAN FINISH? (no baked-in footer vs a stray footer strip) 2 PORTRAIT HOLDS? "
     "(9:16 laid out on its own vs overlapping text) 3 ON GITHUB? (committed vs nothing "
     "pushed). Each row a green pass test + a red fail. Footer rule: 3 PASS -> UPLOAD "
     "FOR PROFS | any FAIL -> mail the fellow. Terracotta on the footer.",
     "manim": manim("T03_LastMile")},
    35.0))

beats.append(beat(
    "T04", "ASK",
    "ASK->RESULT LAW -- composer ask that runs this week's queue (-> T05 result)",
    "Let's run this week's real queue. Fourteen reviews came in. Watch me take one "
    "through the last mile -- not the content this time, just how the file ships.",
    {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
     "remotion": composer(
         "The queue,",
         "Here's this week's Mycroft queue -- 14 fellow reviews. Take each finished "
         "video through the last-mile check: clean finish, portrait holds, on GitHub. "
         "Flag anything that isn't upload-ready for the professors.",
         "running the last-mile check...",
         "Worked example: this week's queue")},
    13.0))

beats.append(beat(
    "T05", "RESULT",
    "worked example walked through the framework -- a clean submission clears all three",
    "Take the first submission -- eight videos. Clean finish? Yes -- nothing baked into "
    "the frame that shouldn't be there. Portrait holds? Yes -- the nine-by-sixteen is "
    "laid out on its own, text clear. On GitHub? Yes. Three greens, so that one goes "
    "straight up for the professors to review. And most of the queue looked exactly "
    "like this -- twelve of the fourteen cleared on the first pass.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "A submission card 'Aishwariya Patil -- Mycroft -- 8 videos' with "
     "a small 16:9 screen pane. Three checks land green in order (CLEAN FINISH / PORTRAIT "
     "HOLDS / ON GITHUB), then a green verdict 'UPLOADED FOR PROFS TO REVIEW'. A quiet "
     "counter: 12 of 14 cleared first pass. Green accent on the verdict.",
     "manim": manim("T05_CleanPass")},
    27.0))

beats.append(beat(
    "T06", "FALSIFIABILITY",
    "falsifiability -- two finished-looking videos that fail DIFFERENT last-mile checks",
    "Now the two that went back -- and here's the catch: both looked done. The first: "
    "eight videos, the content was solid, but a leftover toolkit footer was baked into "
    "the end of the render. Fails clean finish. The second: eight videos, the landscape "
    "cuts were genuinely nice -- but the nine-by-sixteen had text overlapping itself, "
    "hard to actually watch. Fails portrait holds. Neither failed on content. Both "
    "passed the old gate. The last mile is the only thing that caught them. So each gets "
    "a mail, a fix, and a second pass.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "Two submission cards side by side. LEFT 'Onkar Bhujbal -- 8' with "
     "a 16:9 pane showing a stray footer strip at the bottom, struck red -> red stamp "
     "FAILS CLEAN FINISH. RIGHT 'Ameya -- 8' with a clean 16:9 pane + a 9:16 pane whose "
     "caption text overlaps itself, struck red -> red stamp FAILS PORTRAIT HOLDS. Both "
     "note 'content OK | old gate OK'. Verdict strip: NEEDS MODIFICATIONS -- mailed. "
     "Terracotta/red on the two failures.",
     "manim": manim("T06_TwoSentBack")},
    38.0))

beats.append(beat(
    "T07", "SUMMARY",
    "reusable rubric restated -- CONTENT DONE -> last-mile gate -> UPLOADED",
    "So here's the rule I carry into every review. Content done is not the same as "
    "shipped. The explainer can be finished, the code committed, the branding perfect "
    "-- and the file still fails at the last mile. The last mile is small, it's boring, "
    "and it's exactly where a good video gets caught before anyone important sees it.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "A clean router: LEFT 'CONTENT DONE -- explainer, code, branding'. "
     "A center gate = the three last-mile checks CLEAN FINISH / PORTRAIT HOLDS / ON "
     "GITHUB. RIGHT 'UPLOADED -- for the profs'. Footer punch: 'Done isn't shipped. The "
     "last mile is.' High negative space, terracotta accent on the gate.",
     "manim": manim("T07_DoneVsShipped")},
    24.0))

beats.append(beat(
    "T08", "NEXT STEPS",
    "HANDOFF LAW -- ClaudeComposerAsk 'Your turn.'; prompt read aloud + discussed",
    "Your turn -- and this one's for the fellows. Before you submit your next video, "
    "run your own last mile. Paste this: ask Claude to build you a two-minute "
    "pre-submission checklist -- watch the final ten seconds for any stray footer or "
    "watermark, open the nine-by-sixteen on an actual phone and read every caption for "
    "overlap, and confirm the code and assets are pushed. A good answer gives you a "
    "short list you can tick before you hit send. Catch it yourself, and it never comes "
    "back with a mail.",
    {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
     "remotion": composer(
         "Your turn.",
         "Act as my pre-submission reviewer for a fellow explainer video.\n"
         "Build me a 2-minute LAST-MILE checklist to run on my OWN export:\n"
         "1. CLEAN FINISH: scan the final 10s for any toolkit footer/watermark baked in.\n"
         "2. PORTRAIT HOLDS: open the 9:16 on a phone; flag overlapping or clipped text.\n"
         "3. ON GITHUB: confirm code + assets are committed and the link works.\n"
         "Give me a tickable list + the 3 things that most often get a video sent back.",
         "build my pre-submission checklist...",
         "Run it before you submit")},
    35.0))

beats.append(beat(
    "T09", "OUTRO",
    "OUTRO LAW -- title restate; @HumanitariansAI card (house outro is @NikBearBrown-locked)",
    "The last mile -- the check between finished and shipped. With Sanjana Rao, for "
    "Humanitarians AI. Done isn't shipped. Thanks for watching.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "manim": manim("T09_Outro")},
    12.0))


sheet = {
    "metadata": {
        "title": "The Last Mile",
        "slug": "the-last-mile",
        "topic": TOPIC, "register": "Plain / Teardown-warm",
        "audience": "Humanitarians AI", "brand": "claude-hai",
        "channel_title": "@HumanitariansAI", "creator": "Sanjana Rao",
        "engine": "kokoro", "palette": "claude", "style_preset": "claude",
        "style": "claude-explainer", "voice_kokoro": "af_bella",
        "voice_policy": "persistent-fellow-selected", "voice_approval": "APPROVED",
        "approvals": {"voice": {"status": "approved", "reviewer_type": "human",
                                "reviewed_by": "Sanjana Rao",
                                "reviewed_at": "2026-10-11T12:00:00+00:00",
                                "subject_sha256": "d3486a7ac5d092a1899e7d5610728c96d03bf769ed2c423635e04dbd98e04bf4"}},
        "aspect_ratio": "16:9",
        "note": "ai-explainer PROGRESS RECORD for @HumanitariansAI, first-person Sanjana "
                "Rao (af_bella). Week of Oct 4-10, 2026: 85 videos / 13 fellows / Mycroft "
                "/ 100% GitHub / 12 approved, 2 needs-mods. Framework = THE LAST MILE: "
                "clean finish / portrait holds / on GitHub -- the check between finished "
                "and shipped.",
        "tags": ["Humanitarians AI", "Sanjana Rao", "project management", "video review",
                 "quality control", "Mycroft", "fellows", "weekly progress", "Claude",
                 "YouTube Shorts", "9:16"],
        "total_estimated_duration_seconds": int(sum(b["estimated_duration_s"] for b in beats)),
    },
    "beats": beats,
}
out = pathlib.Path(__file__).resolve().parent / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2), encoding="utf-8")
print(f"wrote {out}  ({len(beats)} beats, est {sheet['metadata']['total_estimated_duration_seconds']}s)")
