"""Authors beat_sheet.json and cues.json for "How Google Maps Works" (run once; later edits go in the sheet).

RENDERER: B00, B08 and B09 are the channel's standard Remotion cards. B01-B07 are HyperFrames compositions
(hyperframes/ in this folder), rendered at 4K into media/<beat>.mp4 (16:9) and pantry/<beat>-916.mp4 (9:16),
which the Brutalist compiler picks up like any other beat clip. Their shot.remotion holds props only (no
pattern), so remotion_scenes.py skips them and sync_cues.py still writes the word-clock cues there; the
HyperFrames render reads those cues.

Every number spoken is from evidence/run.log (maps.py: a simulated city and sky, not Google's data) or from
week-11/_research/facts-maps.md ("Safe to say")."""
import json

EYE = "HUMANITARIANS AI · TECH CONCEPTS"


def rem(bid, act, text, pattern, props, est):
    return {"beat_id": bid, "act": act, "narration_text": text,
            "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "choreographed",
                     "remotion": {"pattern": pattern, "props": {**props, "eyebrow": EYE}}},
            "estimated_duration_s": est}


def hf(bid, act, text, comp, props, est):
    return {"beat_id": bid, "act": act, "narration_text": text,
            "shot": {"type": "GRAPHIC", "source": "hyperframes", "motion": "choreographed",
                     "hyperframes": {"composition": comp, "project": "hyperframes"},
                     "remotion": {"props": {**props, "eyebrow": EYE}}},
            "estimated_duration_s": est}


beats = [
    rem("B00", "ASK",
        "Hi, I am Row-Haan and this video is about how Google Maps works: how it finds you, picks a route, sees "
        "traffic, and knows how busy a cafe or a bus will be. I built a small version of each part to see how.",
        "ClaudeComposerAsk",
        {"greeting": "Hi, Rohan", "topic": EYE, "segment": "How Google Maps Works",
         "command": "How does Google Maps know where I am, the fastest way, and how busy it is?",
         "runningText": "working it out…", "folderLabel": "@HumanitariansAI", "modelLabel": "Claude",
         "effortLabel": "Desktop",
         "output": ["find you from satellite timing", "search the road graph for a route",
                    "pool phones for traffic, crowds and buses"],
         "disclosure": "Narration: AI voice (Kokoro af_bella), script by Rohan V."}, 15),
    hf("B01", "WHERE AM I",
       "First, where are you. Your phone times signals from at least four satellites. Three pin down where you "
       "are, and the fourth corrects your phone's clock, which matters: one millisecond off is three hundred "
       "kilometres. In my simulation, open sky gave about five metres. Between tall buildings, about seventy. That's "
       "the blue circle: how unsure it is.",
       "gps", {"title": "Four Satellites and a Clock"}, 24),
    hf("B02", "THE MAP",
       "The map itself is built from Street View cars, satellite and aerial photos, data partners and people's "
       "edits, with AI reading signs and house numbers in the images. More than two billion people use it every "
       "month.",
       "build", {"title": "Built From Photos and People"}, 14),
    hf("B03", "THE ROUTE",
       "To find a route, the roads become a graph: corners joined by streets, each with a travel time. I built a "
       "city with nine hundred corners. Dijkstra's algorithm checked eight hundred and twenty-six of them. A-star, "
       "which aims at the destination, checked five hundred and forty-seven, and found the same route. Google "
       "doesn't publish its exact recipe.",
       "route", {"title": "Roads Become a Graph"}, 24),
    hf("B04", "TRAFFIC",
       "Traffic comes from phones. Since two thousand nine, phones with location on have sent anonymous speeds, "
       "compared with how each road usually behaves. In my city, history alone coloured eighty-seven percent of "
       "roads right, but missed a crash. Five hundred phones were enough to turn it red.",
       "traffic", {"title": "Traffic From Phones"}, 20),
    hf("B05", "ARRIVAL TIME",
       "Arrival times use both. From speed limits alone, my estimates were off by nineteen percent. History plus "
       "live phones: three percent. Google says its arrival times are accurate for over ninety-seven percent of "
       "trips.",
       "eta", {"title": "History Plus Live"}, 15),
    hf("B06", "HOW BUSY",
       "Popular times come from people who opted in, pooled and privacy-protected, and shown only when enough people "
       "visit. I counted a quarter of one cafe's visitors and added privacy noise. The bars still matched the real "
       "crowd, busiest at one o'clock. A quiet shop had too little data, so it got no chart.",
       "busy", {"title": "How Busy, Without Names"}, 21),
    hf("B07", "HOW CROWDED",
       "For buses and trains, agencies publish timetables and live vehicle data in an open format called GTFS. "
       "Crowding comes from riders answering a quick question. With three in a hundred riders answering, my "
       "predictions were right for eighty-one percent of trips.",
       "bus", {"title": "How Full the Bus Is"}, 18),
    rem("B08", "WHAT TO DO",
        "So: when the blue circle is big, trust your eyes. Report crashes and closures. And answer the crowding "
        "question. That's how the next rider knows.",
        "HaiApplyCard",
        {"title": "Help the Map Help You",
         "lede": "Much of what Maps knows comes from people like you.",
         "steps": ["When the blue circle is big, trust your eyes.",
                   "Report crashes and closures.",
                   "Answer the crowding question."],
         "sparkLine": "Your phone is one of the sensors."}, 11),
    rem("B09", "OUTRO",
        "Satellites find you, a graph finds the route, and millions of phones fill in the rest. I'm Row-Haan, for "
        "Humanitarians AI.",
        "HaiTitleOutro", {"title": "How Google Maps Works", "handle": "@HumanitariansAI", "subline": "Rohan V."}, 8),
]

sheet = {
    "metadata": {
        "title": "How Google Maps Works", "slug": "google-maps-explainer", "topic": EYE,
        "register": "Pragmatist", "audience": "Humanitarians AI", "brand": "claude", "engine": "kokoro",
        "voice_kokoro": "af_bella", "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "aspect_ratio": "16:9", "fps": 30, "presenter": "Rohan V.", "channel": "@HumanitariansAI",
        "channel_title": "@HumanitariansAI", "handoff_name": "GoogleMaps_RohanV",
        "renderer": "B01-B07 HyperFrames (hyperframes/), the rest Remotion",
        "ai_disclosure": "Narration is an AI voice (Kokoro af_bella, Rohan V.'s persistent choice for the series); "
                         "script and decisions by Rohan V.",
        "note": "Tech explainer: how a maps app finds you, routes you, sees traffic and predicts crowds. EXECUTABLE "
                "EVIDENCE: maps.py simulates GPS ranging, a 30 x 30 grid city (Dijkstra and A*), rush-hour traffic "
                "from phone speeds, arrival-time prediction, opted-in visit counts with Laplace noise, and rider "
                "crowding reports; every measured number in B01 and B03-B07 comes from that run. Facts about Google "
                "Maps: week-11/_research/facts-maps.md. Opening line follows docs/FELLOWS-SUBMISSION.md verbatim. "
                "NAME: 'Row-Haan' in narration; 'Rohan V.' on screen. LOGO LAW: Google Maps' mark beside its name. "
                "WORD-CLOCK via cues.json.",
        "tags": ["Humanitarians AI", "Google Maps", "GPS", "routing", "traffic", "algorithms", "beginner",
                 "Lyrical Literacy"],
    },
    "beats": beats,
}
json.dump(sheet, open("beat_sheet.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

cues = {
    "_comment": "Cue name -> anchor phrase spoken in that beat's narration. sync_cues.py resolves each against "
                "mp3/words.json and writes the measured fraction into beat_sheet.json at shot.remotion.props.cues.",
    "B00": {"finds": "how it finds you", "route": "picks a route", "busy": "how busy", "built": "I built"},
    "B01": {"where": "where are you", "four": "at least four", "three": "Three pin down", "clock": "corrects your",
            "milli": "one millisecond", "open": "open sky", "tall": "tall buildings", "circle": "the blue circle"},
    "B02": {"street": "Street View cars", "photos": "aerial photos", "edits": "edits", "ai": "with AI reading",
            "billion": "two billion"},
    "B03": {"graph": "become a graph", "corners": "corners joined", "built": "I built a", "dijkstra": "Dijkstra's",
            "astar": "A-star", "same": "same route", "recipe": "exact recipe"},
    "B04": {"phones": "Traffic comes from phones", "since": "Since two thousand nine", "usually": "usually behaves",
            "history": "history alone", "crash": "missed a crash", "five": "Five hundred phones", "red": "turn it red"},
    "B05": {"both": "use both", "limits": "speed limits", "live": "History plus", "google": "Google says"},
    "B06": {"opted": "opted in", "enough": "enough people", "quarter": "a quarter", "noise": "privacy noise",
            "matched": "still matched", "one": "one o'clock", "shop": "quiet shop"},
    "B07": {"agencies": "agencies publish", "gtfs": "GTFS", "riders": "riders answering", "three": "three in a hundred",
            "eighty": "eighty-one"},
    "B08": {"circle": "blue circle", "report": "Report crashes", "answer": "answer the crowding"},
    "B09": {"close": "millions of phones"},
}
json.dump(cues, open("cues.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("beat_sheet.json + cues.json written")
