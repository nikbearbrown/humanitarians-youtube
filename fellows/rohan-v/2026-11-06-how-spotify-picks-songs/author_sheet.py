"""Authors beat_sheet.json and cues.json for "How Spotify Picks Songs" (run once; later edits go in the sheet).
Every number spoken here is from evidence/run.log (recs.py, a made-up service, not Spotify's data).
Facts about Spotify: week-11/_research/facts-recs.md ("Safe to say")."""
import json

EYE = "HUMANITARIANS AI · TECH CONCEPTS"


def beat(bid, act, text, pattern, props, est):
    return {"beat_id": bid, "act": act, "narration_text": text,
            "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "choreographed",
                     "remotion": {"pattern": pattern, "props": {**props, "eyebrow": EYE}}},
            "estimated_duration_s": est}


beats = [
    beat("B00", "ASK",
         "Hi, I am Row-Haan and this video is about how Spotify picks songs: how an app guesses what you'll want to "
         "hear next. Spotify doesn't publish its recipe, so I built a small recommender to see how the idea works.",
         "ClaudeComposerAsk",
         {"greeting": "Hi, Rohan", "topic": EYE, "segment": "How Spotify Picks Songs",
          "command": "How does Spotify know what I want to hear next?",
          "runningText": "working it out…", "folderLabel": "@HumanitariansAI", "modelLabel": "Claude",
          "effortLabel": "Desktop",
          "output": ["learn from what people play, skip and save", "turn listeners and songs into taste numbers",
                     "recommend the closest matches"],
          "disclosure": "Narration: AI voice (Kokoro af_bella), script by Rohan V."}, 14),
    beat("B01", "SIGNALS",
         "Spotify says the most important input is your taste profile: what you search, play, skip and save. There "
         "are no star ratings, so it learns from what you do. It also looks at people with similar taste. That idea "
         "is called collaborative filtering.",
         "RecsSignals", {"title": "It Learns From What You Do",
                         "sparkLine": "No ratings. Just plays, skips and saves."}, 17),
    beat("B02", "THE GRID",
         "Picture a giant grid: listeners down the side, songs across the top, and most boxes empty. I made one up: "
         "three thousand listeners and sixteen hundred songs. Matrix factorisation fills it in by giving every "
         "listener and every song twenty-four hidden taste numbers. A song's score is how well the two lists match.",
         "RecsGrid", {"title": "A Grid That's Mostly Empty",
                      "sparkLine": "Two short lists of numbers, one score."}, 22),
    beat("B03", "WHAT IT LEARNED",
         "It was never told a single genre. Still, a song's five closest songs were the same genre eighty-four "
         "percent of the time, because the same people play them. Close means the two lists of numbers point the "
         "same way. That's cosine similarity.",
         "RecsNeighbours", {"title": "It Found the Genres Itself",
                            "sparkLine": "Played by the same people, so close together."}, 18),
    beat("B04", "THE TEST",
         "Then I hid a fifth of each listener's songs and asked for ten picks. Seventy-four percent of listeners got "
         "at least one hidden song back. Just recommending the hits did nearly as well, sixty-five percent. Random "
         "picks: six.",
         "RecsAccuracy", {"title": "Better Than the Charts, Just",
                          "sparkLine": "Seventy-four against sixty-five."}, 17),
    beat("B05", "THE CATCH",
         "But look at what it picks. Only six percent of its picks came from the less popular half of the songs, "
         "though a quarter of all listening happens there. And a brand-new song, with no plays yet, appeared in "
         "nobody's list. That's the cold-start problem.",
         "RecsPopularity", {"title": "It Leans on the Hits",
                            "sparkLine": "No plays, no picks."}, 18),
    beat("B06", "EXPLORE",
         "So I gave two of every ten slots to songs few people had heard. Almost the whole catalogue came into "
         "play, and the biggest hits' share of the slots fell from seventy-six to sixty-three percent. Spotify "
         "experiments with exploration too.",
         "RecsExplore", {"title": "Leave Room to Explore",
                         "sparkLine": "Two slots in ten for the unknown."}, 17),
    beat("B07", "WHAT TO DO",
         "What can you do? Play, skip and save on purpose: those are its signals. Exclude playlists like sleep "
         "sounds from your taste profile. And go looking for new music yourself.",
         "HaiApplyCard",
         {"title": "Steer Your Recommendations",
          "lede": "It learns from what you do, so do it on purpose.",
          "steps": ["Play, skip and save on purpose.",
                    "Exclude sleep and kids' playlists from your taste profile.",
                    "Search for music it hasn't shown you."],
          "sparkLine": "Your listening is the input."}, 13),
    beat("B08", "OUTRO",
         "What you do goes in, taste numbers come out, with a lean toward the hits. I'm Row-Haan, for Humanitarians AI.",
         "HaiTitleOutro", {"title": "How Spotify Picks Songs", "handle": "@HumanitariansAI",
                           "subline": "Rohan V."}, 7),
]

sheet = {
    "metadata": {
        "title": "How Spotify Picks Songs", "slug": "spotify-recs-explainer", "topic": EYE,
        "register": "Pragmatist", "audience": "Humanitarians AI", "brand": "claude", "engine": "kokoro",
        "voice_kokoro": "af_bella", "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "aspect_ratio": "16:9", "fps": 30, "presenter": "Rohan V.", "channel": "@HumanitariansAI",
        "channel_title": "@HumanitariansAI", "handoff_name": "SpotifyRecs_RohanV",
        "ai_disclosure": "Narration is an AI voice (Kokoro af_bella, Rohan V.'s persistent choice for the series); "
                         "script and decisions by Rohan V.",
        "note": "Tech explainer: how a music app recommends songs. EXECUTABLE EVIDENCE: recs.py builds a made-up "
                "service (1,600 songs in 8 Western genres, 3,000 listeners, play counts with a popularity pull) and "
                "fits implicit-feedback ALS (Hu, Koren & Volinsky 2008); every number in B02-B06 comes from that run "
                "(evidence/run.log, results.json, scene.json). Nothing is Spotify's data or code; Spotify facts are "
                "from week-11/_research/facts-recs.md. Opening line follows docs/FELLOWS-SUBMISSION.md verbatim. "
                "NAME: 'Row-Haan' in narration; 'Rohan V.' on screen. LOGO LAW: Spotify's mark beside its name. "
                "WORD-CLOCK via cues.json.",
        "tags": ["Humanitarians AI", "recommendation systems", "Spotify", "collaborative filtering",
                 "matrix factorization", "beginner", "Lyrical Literacy"],
    },
    "beats": beats,
}
json.dump(sheet, open("beat_sheet.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

cues = {
    "_comment": "Cue name -> anchor phrase spoken in that beat's narration. sync_cues.py resolves each against "
                "mp3/words.json and writes the measured fraction into beat_sheet.json at shot.remotion.props.cues.",
    "B00": {"picks": "how Spotify picks songs", "guesses": "guesses what", "recipe": "doesn't publish", "built": "I built"},
    "B01": {"profile": "taste profile", "search": "what you search", "skip": "skip and save", "stars": "no star ratings",
            "similar": "similar taste", "cf": "collaborative filtering"},
    "B02": {"grid": "a giant grid", "empty": "most boxes empty", "made": "I made one up", "fills": "fills it in",
            "numbers": "twenty-four", "score": "A song's score"},
    "B03": {"never": "never told", "five": "five closest", "eighty": "eighty-four", "same": "same people",
            "point": "point the", "cosine": "cosine similarity"},
    "B04": {"hid": "I hid a fifth", "ten": "ten picks", "seventy": "Seventy-four percent", "hits": "recommending the hits",
            "random": "Random"},
    "B05": {"look": "look at what it picks", "six": "Only six percent", "quarter": "a quarter", "new": "brand-new song",
            "nobody": "nobody's list", "cold": "cold-start"},
    "B06": {"two": "two of every ten", "whole": "whole catalogue", "share": "share of the slots", "fell": "seventy-six to",
            "spotify": "Spotify experiments"},
    "B07": {"purpose": "on purpose", "exclude": "Exclude playlists", "looking": "go looking"},
    "B08": {"close": "lean toward the hits"},
}
json.dump(cues, open("cues.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("beat_sheet.json + cues.json written")
