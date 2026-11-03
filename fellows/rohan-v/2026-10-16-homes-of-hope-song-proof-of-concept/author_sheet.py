"""Authors beat_sheet.json and cues.json for "Homes of Hope Songs: Proof of Concept Progress" (weekly progress).

Source: Rohan V.'s project summary, Lyrical_Literacy_Hindi_PoC_Summary.pdf (week of 12-16 Oct 2026), copied
to SOURCE-brief.md. Under 90 s by request. Safeguards: no girl, home, school or staff member is named or
shown; no person icons; the two lyric lines shown are the songs' own chorus/chant lines, marked as pending
native Hindi review. Team members are not named (standing instruction: no one but the presenter).
"""
import json

EYE = "HUMANITARIANS AI · WEEKLY PROGRESS"


def beat(bid, act, text, pattern, props, est):
    return {"beat_id": bid, "act": act, "narration_text": text,
            "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "choreographed",
                     "remotion": {"pattern": pattern, "props": {**props, "eyebrow": EYE}}},
            "estimated_duration_s": est}


beats = [
    beat("B00", "ASK",
         "Hi, I am Row-Haan and this video is about the proof of concept we're building for Homes of Hope: songs in "
         "a girl's own language that build real English as she sings. This round is one pairing, English and Hindi.",
         "ClaudeComposerAsk",
         {"greeting": "Hi, Rohan", "topic": EYE, "segment": "Homes of Hope Songs: Proof of Concept",
          "command": "Build a small proof of concept: English and Hindi songs at two levels.",
          "runningText": "drafting…", "folderLabel": "@HumanitariansAI", "modelLabel": "Claude",
          "effortLabel": "Desktop",
          "output": ["call and response in two languages", "two tiers, one melody", "safe for girls in care"],
          "disclosure": "Narration: AI voice (Kokoro af_bella), script by Rohan V."}, 12),
    beat("B01", "THE METHOD",
         "The method is call and response. The lead sings a line in Hindi, and the group answers with the same line "
         "in English. So every English phrase arrives with its meaning.",
         "HohCallResponse",
         {"title": "Call and Response",
          "pairs": [{"lead": "Saath saath, hum saath saath", "group": "Side by side", "song": "SISTERS SIDE BY SIDE"},
                    {"lead": "Nayi naari, naya Bharat", "group": "New women, new India", "song": "I WILL BE"}],
          "leadLabel": "LEAD · HINDI", "groupLabel": "GROUP · ENGLISH",
          "note": "Hindi in Roman script · native review pending",
          "sparkLine": "Each English line is cued by its meaning."}, 11),
    beat("B02", "TWO TIERS",
         "Each song comes in two tiers. Tier one is half Hindi, half English. Tier two is mostly English, with Hindi "
         "as a warm thread. The melody stays the same, so a girl can move up without leaving her song behind.",
         "HohTiers",
         {"title": "Two Tiers, One Melody",
          "tiers": [{"name": "TIER 1 · FOUNDATION", "english": 50, "line": "Half Hindi, half English"},
                    {"name": "TIER 2 · BRIDGE", "english": 80, "line": "Mostly English, Hindi as a thread"}],
          "melody": "SAME MELODY, SAME MESSAGE",
          "sparkLine": "Move up a tier, keep the song."}, 13),
    beat("B03", "THE SOUND",
         "Two themes, four songs, drafted with Claude and generated in Suno. The first versions leaned on violin and "
         "felt too soft. I rebuilt I Will Be around dhole, tubla and sitaar, a little faster, with a strong lead and a "
         "big group answer.",
         "HaiProgressOverturned",
         {"title": "What the Sound Revision Changed", "leftHeader": "first version", "rightHeader": "revision",
          "rows": [{"was": "Acoustic guitar and violin swells", "now": "Dhol, tabla and sitar lead"},
                   {"was": "Violin in every chorus", "now": "Light strings, in the background only"},
                   {"was": "102 to 106 BPM", "now": "108 BPM (Tier 1), 110 BPM (Tier 2)"},
                   {"was": "Strong lead with group", "now": "Powerful lead, big group answers"}],
          "sparkLine": "Same songs, far more energy."}, 15),
    beat("B04", "SAFEGUARDS",
         "These are girls in care, so the songs sing about dreams and daily routines, never names, places or "
         "backstories. No real girl's voice or likeness is used. Lines about home life go to staff review first.",
         "HaiVerdictSplit",
         {"title": "Written to Protect the Girls", "goodHeader": "THE SONGS USE", "notYetHeader": "NEVER USED",
          "good": ["Dreams and careers", "Daily routines of a home", "Values: honesty, hard work"],
          "notYet": ["Names, schools or stories", "A real girl's voice or likeness"],
          "pendingLabel": "BEFORE PRODUCTION", "pending": "Staff review the lines about home life",
          "baseline": True,
          "sparkLine": "Interests and dreams, never identities."}, 13),
    beat("B05", "NEXT",
         "The team is now choosing the strongest versions. Next: a native Hindi review, then a short proof of concept "
         "video for the pitch. If you speak Hindi fluently, I'd welcome your review.",
         "HaiProgressRoadmap",
         {"title": "Done, and What Is Next",
          "shipped": [{"label": "Four songs, two tiers", "sub": "lyrics, styles and tags for each"},
                      {"label": "Song versions generated", "sub": "shared with the team to pick"}],
          "next": [{"label": "Native Hindi review", "sub": "pronunciation, meaning and tone", "due": "NEXT"},
                   {"label": "Proof of concept video", "sub": "for the Homes of Hope pitch", "due": "AFTER THE PICKS"}],
          "phoneType": True, "accentText": True,
          "sparkLine": "Pick, review, then pitch."}, 13),
    beat("B06", "OUTRO",
         "One song, two languages, two levels. I'm Row-Haan, for Humanitarians AI.",
         "HaiTitleOutro", {"title": "Homes of Hope Songs: Proof of Concept", "handle": "@HumanitariansAI",
                           "subline": "Rohan V."}, 5),
]

sheet = {
    "metadata": {
        "title": "Homes of Hope Songs: Proof of Concept Progress", "slug": "homes-of-hope-poc-progress",
        "topic": EYE, "register": "Pragmatist", "audience": "Humanitarians AI", "brand": "claude",
        "engine": "kokoro", "voice_kokoro": "af_bella", "palette": "claude", "style_preset": "claude",
        "ground": "#FAF9F5", "aspect_ratio": "16:9", "fps": 30, "presenter": "Rohan V.",
        "channel": "@HumanitariansAI", "channel_title": "@HumanitariansAI", "handoff_name": "HomesOfHopePoC_RohanV",
        "ai_disclosure": "Narration is an AI voice (Kokoro af_bella, Rohan V.'s persistent choice for the series); "
                         "script and decisions by Rohan V. The lyrics were drafted with Claude and the songs "
                         "generated in Suno; Rohan V. chose, revised and directed both.",
        "note": "Weekly progress, week of 2026-10-12: the Lyrical Literacy x Homes of Hope English + Hindi proof of "
                "concept. Under 90 s by request. SOURCE: Rohan V.'s project summary (SOURCE-brief.md). EVIDENCE: the "
                "two lyric lines in B01 and every number in B03 are from that summary. No song audio is included "
                "(Rohan V.'s choice: visuals only). SAFEGUARDS: no girl, home, school or staff member is named or "
                "shown; no person icons; team members are not named. Opening line follows "
                "docs/FELLOWS-SUBMISSION.md verbatim. NAME: narration spells 'Row-Haan'; on-screen 'Rohan V.'.",
        "tags": ["Humanitarians AI", "Lyrical Literacy", "Homes of Hope", "Hindi", "English learning",
                 "weekly progress"],
    },
    "beats": beats,
}
json.dump(sheet, open("beat_sheet.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

cues = {
    "_comment": "Cue name -> anchor phrase spoken in that beat's narration. sync_cues.py resolves each against "
                "mp3/words.json and writes the measured fraction into beat_sheet.json at shot.remotion.props.cues.",
    "B00": {"songs": "songs in", "english": "build real English", "pair": "one pairing"},
    "B01": {"method": "call and response", "lead": "The lead sings", "group": "the group answers",
            "meaning": "arrives with its meaning"},
    "B02": {"two": "two tiers", "t1": "Tier one", "t2": "Tier two", "thread": "warm thread",
            "melody": "The melody stays the same", "up": "move up"},
    "B03": {"r0": "leaned on violin", "r1": "felt too soft", "r2": "a little faster", "r3": "strong lead"},
    "B04": {"showed": "girls in care", "good": "dreams and daily", "visuals": "never names", "fourk": "No real girl's voice",
            "pending": "staff review"},
    "B05": {"choosing": "choosing the strongest", "review": "native Hindi review", "video": "proof of concept video",
            "you": "If you speak Hindi"},
    "B06": {"close": "two levels"},
}
json.dump(cues, open("cues.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("beat_sheet.json + cues.json written")
