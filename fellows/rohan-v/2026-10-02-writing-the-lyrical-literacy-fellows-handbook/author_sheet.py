"""Authors beat_sheet.json and cues.json for "Writing the Lyrical Literacy Fellows Handbook" (weekly progress).

No person other than the presenter is named in narration or on screen (standing instruction), and
no handbook page with contact details or the shared login is shown (crops.json lists what is).
"""
import json

EYE = "HUMANITARIANS AI · WEEKLY PROGRESS"


def beat(bid, act, text, pattern, props, est):
    return {"beat_id": bid, "act": act, "narration_text": text,
            "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "choreographed",
                     "remotion": {"pattern": pattern, "props": {**props, "eyebrow": EYE}}},
            "estimated_duration_s": est}


PAGES = [
    {"src": "fellows-handbook/title.png", "label": "Title page", "cue": "here"},
    {"src": "fellows-handbook/contents.png", "label": "Contents · 12 sections", "cue": "pages"},
    {"src": "fellows-handbook/suno.png", "label": "5.4 · Suno, your first song", "cue": "guides"},
    {"src": "fellows-handbook/midjourney.png", "label": "6.4 · Midjourney prompts", "cue": "mj"},
    {"src": "fellows-handbook/workflow.png", "label": "8.1 · Who does what", "cue": "workflow"},
    {"src": "fellows-handbook/checklist.png", "label": "1.2 · First-week checklist", "cue": "checklist"},
]

beats = [
    beat("B00", "ASK",
         "Hi, I am Row-Haan and this video is about the handbook I wrote for new Lyrical Literacy fellows. Until now, "
         "getting started meant asking around: which account, which link, who approves what. This week, all of it went "
         "into one document.",
         "ClaudeComposerAsk",
         {"greeting": "Hi, Rohan", "topic": EYE, "segment": "Writing the Lyrical Literacy Fellows Handbook",
          "command": "Put everything a new Lyrical Literacy fellow needs into one handbook.",
          "runningText": "drafting…", "folderLabel": "@HumanitariansAI", "modelLabel": "Claude",
          "effortLabel": "Desktop",
          "output": ["getting access, step by step", "Suno and Midjourney, in depth",
                     "weekly reporting and renewals"],
          "disclosure": "Narration: AI voice (Kokoro af_bella), script by Rohan V."}, 15),
    beat("B01", "THE HANDBOOK",
         "Here it is: forty-six pages in twelve sections. Claude drafted it from the program's own pages and from our "
         "nine tutorials, and I reviewed and corrected it. It covers getting into every tool, full guides to Suno and "
         "Midjourney, the weekly reporting rules, the whole video workflow, and how renewals work. And it opens with a "
         "first-week checklist.",
         "HaiDocPages",
         {"title": "The Fellows Handbook, Version 1.0", "pages": PAGES,
          "stats": [{"value": "46", "label": "PAGES"}, {"value": "12", "label": "SECTIONS"},
                    {"value": "v1.0", "label": "EDITABLE WORD FILE"}],
          "credit": "Drafted by Claude from the program's pages and our tutorials · reviewed by Rohan V.",
          "sparkLine": "One document instead of asking around."}, 24),
    beat("B02", "ACCESS",
         "The part new fellows ask about most is access. Discord comes first, because Suno and Midjourney both sign in "
         "through it. Then Canva for design, and Adobe for editing. A month ago, this chain lived in people's heads. "
         "Now each link is a numbered set of steps.",
         "HaiProgressSignupChain",
         {"title": "The Access Chain, Written Down",
          "tools": [{"name": "Discord", "purpose": "the key to Suno and Midjourney", "hue": "#5865F2"},
                    {"name": "Suno", "purpose": "music", "hue": "#E5197F"},
                    {"name": "Midjourney", "purpose": "images", "hue": "#2F2A26"},
                    {"name": "Canva", "purpose": "design", "hue": "#00A3B4"},
                    {"name": "Adobe CC", "purpose": "editing", "hue": "#DA1F26"}],
          "docLabel": "FELLOWS HANDBOOK · SECTION 4", "docStatus": "WRITTEN · v1.0",
          "sparkLine": "From people's heads to numbered steps."}, 17),
    beat("B03", "WHAT REVIEW CHANGED",
         "It didn't come out right first time. The first draft followed a navy and cream palette that looked heavy, so "
         "it was rebuilt to match our website. My review comments in Word removed a step nobody needs, and handed the "
         "hours and logs to Claude. And when the program's rules changed mid-week, the handbook changed with them: "
         "build files on GitHub, and every video to one reviewer.",
         "HaiProgressOverturned",
         {"title": "What Review Changed", "leftHeader": "first draft", "rightHeader": "after review",
          "rows": [{"was": "Navy and cream palette", "now": "The website's look: white, Inter, deep red"},
                   {"was": "Email your GitHub username to the PM", "now": "Removed: nobody needs it"},
                   {"was": "Fellows keep hours and logs by hand", "now": "Claude keeps them from what you tell it"},
                   {"was": "No video files of any kind on GitHub", "now": "Build inputs on GitHub, renders on Drive"},
                   {"was": "Videos go to your PM", "now": "Every video to one reviewer"}],
          "sparkLine": "The draft was the start, not the deliverable."}, 24),
    beat("B04", "WHAT IT DOES",
         "What it does now: one place for access, tools, reporting and renewals, in an editable Word file with a version "
         "history, so whoever runs onboarding next can keep it current. What it hasn't done yet is meet a new fellow. "
         "The real test is someone following it from page one, without asking anyone.",
         "HaiVerdictSplit",
         {"title": "What It Does, and What It Hasn't Done Yet", "goodHeader": "DOES NOW", "notYetHeader": "NOT YET",
          "good": ["One place: access, tools, reporting, renewals", "Editable Word file with a version history",
                   "Shared privately with the team"],
          "notYet": ["Used by a new fellow"],
          "pendingLabel": "THE REAL TEST", "pending": "A new fellow following it from page one, without asking anyone",
          "sparkLine": "Written is not the same as tested."}, 19),
    beat("B05", "NEXT",
         "It also closes the first item on my renewal plan, which has now been approved, almost a month ahead of the "
         "thirty October target. Next is automating our video editing: testing two more tools on the same footage in "
         "November, then building the best one into a pipeline for Lyrical Literacy by mid-December.",
         "HaiProgressRoadmap",
         {"title": "Shipped, and What Is Next",
          "shipped": [{"label": "Renewal approved", "sub": "Oct 2026 – Jan 2027"},
                      {"label": "Fellows Handbook v1.0", "sub": "due 30 Oct · done 30 Sep"}],
          "next": [{"label": "Test OpenReel and DaVinci Resolve", "sub": "same footage as the HyperFrames test", "due": "2–20 NOV"},
                   {"label": "Editing pipeline for LL", "sub": "build in the tool that wins", "due": "BY 11 DEC"}],
          "sparkLine": "One plan item done. Next: video editing."}, 17),
    beat("B06", "WHAT TO DO",
         "If you're joining Lyrical Literacy: ask your project manager for the handbook, start with the first-week "
         "checklist, and come to the team meeting on Wednesdays at twelve, Eastern time. If anything in it is unclear "
         "or out of date, tell me, and it goes into the next version.",
         "HaiApplyCard",
         {"title": "New to Lyrical Literacy? Start Here", "lede": "One document, so nobody has to ask twice.",
          "steps": ["Ask your project manager for the handbook link.",
                    "Start with the first-week checklist in Section 1.",
                    "Join the team meeting: Wednesdays, 12:00 pm ET.",
                    "Something unclear? Tell me, and it goes into the next version."],
          "sparkLine": "Checklist first. Questions second."}, 17),
    beat("B07", "OUTRO",
         "One handbook, so nobody has to ask twice. I'm Row-Haan, for Humanitarians AI.",
         "HaiTitleOutro", {"title": "Writing the Lyrical Literacy Fellows Handbook", "handle": "@HumanitariansAI",
                           "subline": "Rohan V."}, 6),
]

sheet = {
    "metadata": {
        "title": "Writing the Lyrical Literacy Fellows Handbook", "slug": "fellows-handbook-progress", "topic": EYE,
        "register": "Pragmatist", "audience": "Humanitarians AI", "brand": "claude", "engine": "kokoro",
        "voice_kokoro": "af_bella", "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "aspect_ratio": "16:9", "fps": 30, "presenter": "Rohan V.", "channel": "@HumanitariansAI",
        "channel_title": "@HumanitariansAI", "handoff_name": "FellowsHandbookUpdate_RohanV",
        "ai_disclosure": "Narration is an AI voice (Kokoro af_bella, Rohan V.'s persistent choice for the series); "
                         "script and decisions by Rohan V. The handbook itself was drafted by Claude from cited sources "
                         "and reviewed and corrected by Rohan V.",
        "note": "Weekly progress, week of 2026-09-28 (built and submitted late, 2026-10-05). The deliverable: the "
                "Lyrical Literacy Fellows Handbook v1.0 (46 pages, editable .docx). EVIDENCE: B01 shows six crops of "
                "the real v1.0 PDF (pantry/handbook/, listed with page numbers and SHA-256 in crops.json); no page "
                "with contact details or the shared login is shown. The handbook file itself is NOT committed (it "
                "holds a shared login). No person other than the presenter is named. Opening line follows "
                "docs/FELLOWS-SUBMISSION.md verbatim. NAME: narration spells 'Row-Haan'; on-screen 'Rohan V.'.",
        "tags": ["Humanitarians AI", "Lyrical Literacy", "onboarding", "documentation", "weekly progress"],
    },
    "beats": beats,
}
json.dump(sheet, open("beat_sheet.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

cues = {
    "_comment": "Cue name -> anchor phrase spoken in that beat's narration. sync_cues.py resolves each against "
                "mp3/words.json and writes the measured fraction into beat_sheet.json at shot.remotion.props.cues.",
    "B00": {"asking": "meant asking around", "one": "into one document"},
    "B01": {"here": "Here it is", "pages": "forty-six pages", "drafted": "Claude drafted it", "reviewed": "I reviewed",
            "tools": "getting into every tool", "guides": "full guides to Suno", "mj": "and Midjourney",
            "reporting": "weekly reporting rules", "workflow": "whole video workflow", "renewals": "how renewals work",
            "checklist": "first-week checklist"},
    "B02": {"doc": "ask about most is access", "t0": "Discord comes first", "t1": "because Suno",
            "t2": "Midjourney both sign in", "t3": "Then Canva", "t4": "Adobe for editing",
            "each": "numbered set of steps"},
    "B03": {"r0": "navy and cream", "r1": "removed a step", "r2": "handed the hours", "r3": "build files on GitHub",
            "r4": "every video to one reviewer"},
    "B04": {"showed": "What it does now", "good": "one place for access", "visuals": "hasn't done yet",
            "pending": "The real test"},
    "B05": {"plan": "first item on my renewal plan", "next": "Next is automating"},
    "B06": {"ask": "ask your project manager", "checklist": "first-week checklist", "meeting": "the team meeting",
            "tell": "tell me"},
    "B07": {"close": "nobody has to ask twice"},
}
json.dump(cues, open("cues.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok", sum(len(b["narration_text"].split()) for b in beats), "words")
