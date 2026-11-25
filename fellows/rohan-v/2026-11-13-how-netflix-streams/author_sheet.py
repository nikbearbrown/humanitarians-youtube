"""Authors beat_sheet.json and cues.json for "How Netflix Streams" (run once; later edits go in the sheet).

RENDERER: B00, B07 and B08 are the channel's standard Remotion cards. B01-B06 are HyperFrames compositions with
three.js scenes (hyperframes/), rendered at 4K into media/<beat>.mp4 and pantry/<beat>-916.mp4.

Numbers spoken are from evidence/run.log (stream.py: real libx264 encodes scored with VMAF, and a simulated player
and network; not Netflix's code or video) or from week-12/_research/facts-netflix.md."""
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
        "Hi, I am Row-Haan and this video is about how Netflix streams: how a show reaches your screen without "
        "stopping to load, even when your internet slows down. I built a small version of each part to see how.",
        "ClaudeComposerAsk",
        {"greeting": "Hi, Rohan", "topic": EYE, "segment": "How Netflix Streams",
         "command": "How does Netflix keep playing when my internet slows down?",
         "runningText": "working it out…", "folderLabel": "@HumanitariansAI", "modelLabel": "Claude",
         "effortLabel": "Desktop",
         "output": ["store every show at many qualities", "pick the next few seconds to fit your connection",
                    "serve it from a box near you"],
         "disclosure": "Narration: AI voice (Kokoro af_bella), script by Rohan V."}, 14),
    hf("B01", "THE LADDER",
       "First, every show is stored many times over, at different qualities: a ladder from a few hundred kilobits a "
       "second to several megabits. I made two test clips, a clean test card and a grainy, detailed zoom, and encoded "
       "each one at six rungs.",
       "ladder", {"title": "Many Copies of Every Show"}, 15),
    hf("B02", "VMAF",
       "To judge the quality, Netflix built a score called VMAF, from zero to a hundred, and gave it away in twenty "
       "sixteen. On my test card, the lowest rung scored thirty-eight, and the top rung ninety-six. The grainy clip "
       "topped out at seventy-five.",
       "vmaf", {"title": "A Score for How It Looks"}, 16),
    hf("B03", "PER TITLE",
       "So one ladder doesn't fit every show. My test card reached a score of ninety-three at about four megabits. "
       "The grainy clip never got there, even at five point eight. Since twenty fifteen, Netflix has built a ladder "
       "for each title.",
       "pertitle", {"title": "A Ladder for Each Show"}, 15),
    hf("B04", "THE PLAYER",
       "Then the show is cut into chunks a few seconds long, and before each one the player picks a rung. I streamed "
       "ten minutes over a connection that sags and drops. Always picking the best quality stalled for seven seconds. "
       "Picking by how full the buffer was never stalled, and streamed at a higher quality than picking by speed.",
       "player", {"title": "Choose Before Every Chunk"}, 21),
    hf("B05", "CLOSE BY",
       "Distance matters too. Netflix's network, Open Connect, puts its own servers inside internet providers, filled "
       "with popular shows overnight. In my model, a chunk from a far server took one and a half seconds. From one "
       "inside your provider, half a second.",
       "cdn", {"title": "A Server Near You"}, 17),
    hf("B06", "SCALE",
       "By twenty twenty-two, that network had about eighteen thousand servers in a hundred and seventy-five countries. Today it serves more than "
       "three hundred and twenty-five million memberships. And newer codecs like A-V-1, now about thirty percent of "
       "viewing, fit the same picture into fewer bits.",
       "scale", {"title": "The Whole System"}, 15),
    rem("B07", "WHAT TO DO",
        "For a sharp picture, Netflix suggests five megabits a second for full HD, and fifteen for 4K. A steady "
        "connection matters as much as a fast one.",
        "HaiApplyCard",
        {"title": "Get the Best Picture",
         "lede": "The player adapts, but it can't beat your connection.",
         "steps": ["Full HD: about 5 Mbit/s.",
                   "4K: about 15 Mbit/s.",
                   "A steady connection matters too."],
         "sparkLine": "Many copies, chosen chunk by chunk."}, 10),
    rem("B08", "OUTRO",
        "Many copies, chosen chunk by chunk, from a box near you. I'm Row-Haan, for Humanitarians AI.",
        "HaiTitleOutro", {"title": "How Netflix Streams", "handle": "@HumanitariansAI", "subline": "Rohan V."}, 7),
]

sheet = {
    "metadata": {
        "title": "How Netflix Streams", "slug": "netflix-streaming-explainer", "topic": EYE,
        "register": "Pragmatist", "audience": "Humanitarians AI", "brand": "claude", "engine": "kokoro",
        "voice_kokoro": "af_bella", "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "aspect_ratio": "16:9", "fps": 30, "presenter": "Rohan V.", "channel": "@HumanitariansAI",
        "channel_title": "@HumanitariansAI", "handoff_name": "NetflixStreaming_RohanV",
        "renderer": "B01-B06 HyperFrames + three.js (hyperframes/), the rest Remotion",
        "ai_disclosure": "Narration is an AI voice (Kokoro af_bella, Rohan V.'s persistent choice for the series); "
                         "script and decisions by Rohan V.",
        "note": "Tech explainer: how a streaming service keeps playing. EXECUTABLE EVIDENCE: stream.py encodes two "
                "test clips made with ffmpeg at a six-rung libx264 ladder, scores each with VMAF (libvmaf), simulates "
                "three players over a sagging home connection, and models segment download time from far and near "
                "servers. Not Netflix's code or video. Facts: week-12/_research/facts-netflix.md. NAME: 'Row-Haan' "
                "in narration; 'Rohan V.' on screen. LOGO LAW: Netflix's mark beside its name. WORD-CLOCK via cues.json.",
        "tags": ["Humanitarians AI", "Netflix", "streaming", "adaptive bitrate", "VMAF", "CDN", "beginner",
                 "Lyrical Literacy"],
    },
    "beats": beats,
}
json.dump(sheet, open("beat_sheet.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

cues = {
    "_comment": "Cue name -> anchor phrase spoken in that beat's narration. sync_cues.py resolves each against "
                "mp3/words.json and writes the measured fraction into beat_sheet.json at shot.remotion.props.cues.",
    "B00": {"streams": "how Netflix streams", "stopping": "without stopping", "slows": "slows down", "built": "I built"},
    "B01": {"stored": "stored many times", "ladder": "a ladder", "two": "two test clips", "card": "test card",
            "grainy": "grainy", "six": "six rungs"},
    "B02": {"score": "a score called", "range": "zero to a hundred", "away": "gave it away", "lowest": "lowest rung",
            "top": "top rung", "grain": "grainy clip"},
    "B03": {"fit": "doesn't fit", "card": "reached a score", "never": "never got there", "since": "Since twenty fifteen"},
    "B04": {"chunks": "cut into chunks", "picks": "picks a rung", "streamed": "I streamed", "best": "Always picking",
            "buffer": "Picking by how full", "speed": "picking by speed"},
    "B05": {"distance": "Distance matters", "open": "Open Connect", "inside": "inside internet providers",
            "overnight": "overnight", "far": "far server", "near": "inside your provider"},
    "B06": {"servers": "eighteen thousand", "countries": "seventy-five countries", "members": "twenty-five million",
            "av1": "A-V-1", "fewer": "fewer bits"},
    "B07": {"hd": "full HD", "fourk": "fifteen", "steady": "A steady connection"},
    "B08": {"close": "a box near you"},
}
json.dump(cues, open("cues.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("beat_sheet.json + cues.json written")
