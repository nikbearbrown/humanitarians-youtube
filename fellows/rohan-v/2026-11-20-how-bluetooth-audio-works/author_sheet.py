"""Authors beat_sheet.json and cues.json for "How Bluetooth Audio Works" (run once; later edits go in the sheet).

RENDERER: B00, B07 and B08 are the channel's standard Remotion cards. B01-B06 are HyperFrames compositions with
three.js scenes (hyperframes/), rendered at 4K into media/<beat>.mp4 (16:9) and pantry/<beat>-916.mp4 (9:16).
Their shot.remotion holds props only, so remotion_scenes.py skips them and sync_cues.py still writes the cues.

Numbers spoken are from evidence/run.log (bluetooth.py: ffmpeg's real codecs + a simulated A2DP link, not any
company's code) or from week-13/_research/facts-bluetooth.md. B04 ends with two clips of the run's own track played
through the simulated link: a small buffer (one dropout) and a big one (none)."""
import json

EYE = "HUMANITARIANS AI · AUDIO CONCEPTS"


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
        "Hi, I am Row-Haan and this video is about how Bluetooth audio works: how music gets from your phone to "
        "wireless earbuds, and why it sometimes lags or cuts out. I built a small version to see how.",
        "ClaudeComposerAsk",
        {"greeting": "Hi, Rohan", "topic": EYE, "segment": "How Bluetooth Audio Works",
         "command": "How does music get to my wireless earbuds?",
         "runningText": "working it out…", "folderLabel": "@HumanitariansAI", "modelLabel": "Claude",
         "effortLabel": "Desktop",
         "output": ["squeeze the music to a quarter", "hop between radio channels", "keep a little music in reserve"],
         "disclosure": "Narration: AI voice (Kokoro af_bella), script by Rohan V."}, 13),
    hf("B01", "TOO MUCH DATA",
       "CD-quality stereo is about fourteen hundred kilobits a second: more than Bluetooth's audio link can reliably "
       "carry. So your phone squeezes the music first, with a codec. The one every device must support is SBC. On my "
       "test track, it used about three hundred and thirty kilobits: under a quarter.",
       "data", {"title": "Too Much Data to Send"}, 17),
    hf("B02", "THE RADIO",
       "Then the radio. Classic Bluetooth hops between seventy-nine channels, up to sixteen hundred times a second, "
       "and shares them with Wi-Fi. In my simulation, a busy Wi-Fi network made seventeen percent of tries fail. "
       "Adaptive hopping skips the busy channels: about one percent.",
       "hopping", {"title": "Seventy-Nine Channels"}, 19),
    hf("B03", "CODECS",
       "Your phone and headphones agree on a codec. SBC is the baseline. Apple's devices prefer AAC. Many Android "
       "phones also offer aptX, at about three hundred and fifty kilobits, or LDAC, at up to nine hundred and "
       "ninety. More data can sound better, but it's harder to send without gaps.",
       "codecs", {"title": "Picking a Codec"}, 16),
    hf("B04", "THE BUFFER",
       "Lost packets, from Wi-Fi or your own body, get sent again, so the earbuds keep a little music in reserve: a "
       "buffer. In two minutes of my simulation, a fifty millisecond buffer glitched thirty times; two hundred, "
       "three times; three hundred, never. That reserve is the main reason Bluetooth lags. Listen: small, then big.",
       "buffer", {"title": "Music in Reserve"}, 20),
    hf("B05", "LIP SYNC",
       "Real earbuds are often a couple of hundred milliseconds behind. For videos, the headphones can report that "
       "delay, and the phone holds the picture back to match. A game can't hold back your button presses, so games "
       "can feel laggy.",
       "lipsync", {"title": "Holding the Picture Back"}, 14),
    hf("B06", "LE AUDIO",
       "Bluetooth's next generation, LE Audio, brings a new codec called LC3. The Bluetooth SIG says it beats SBC even at "
       "half the bit rate. Its broadcast feature, Auracast, lets one phone or TV stream to any number of earbuds "
       "nearby.",
       "leaudio", {"title": "What Comes Next"}, 13),
    rem("B07", "WHAT TO DO",
        "For the best Bluetooth sound: keep your phone close, pick a better codec if your phone offers one, and use "
        "your earbuds' game mode for games.",
        "HaiApplyCard",
        {"title": "Better Bluetooth Sound",
         "lede": "Squeezed, hopped and buffered, every time you press play.",
         "steps": ["Keep your phone close.",
                   "Pick a better codec if offered.",
                   "Use game mode for games."],
         "sparkLine": "A quarter of the data, a little delay."}, 9),
    rem("B08", "OUTRO",
        "Squeeze it, hop around the noise, and keep a little in reserve. I'm Row-Haan, for Humanitarians AI.",
        "HaiTitleOutro", {"title": "How Bluetooth Audio Works", "handle": "@HumanitariansAI", "subline": "Rohan V."}, 7),
]

sheet = {
    "metadata": {
        "title": "How Bluetooth Audio Works", "slug": "bluetooth-audio-explainer", "topic": EYE,
        "register": "Pragmatist", "audience": "Humanitarians AI", "brand": "claude", "engine": "kokoro",
        "voice_kokoro": "af_bella", "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "aspect_ratio": "16:9", "fps": 30, "presenter": "Rohan V.", "channel": "@HumanitariansAI",
        "channel_title": "@HumanitariansAI", "handoff_name": "BluetoothAudio_RohanV",
        "renderer": "B01-B06 HyperFrames + three.js (hyperframes/), the rest Remotion",
        "ai_disclosure": "Narration is an AI voice (Kokoro af_bella, Rohan V.'s persistent choice for the series); "
                         "script and decisions by Rohan V.",
        "note": "Audio explainer: how wireless earbuds get their music. EXECUTABLE EVIDENCE: bluetooth.py encodes a "
                "synthetic pop track with ffmpeg's SBC, aptX, aptX HD and AAC encoders (data rates measured from the "
                "bytes) and simulates an A2DP link: 79 hopping channels, a busy Wi-Fi network, body blocking, "
                "re-sends and the headphone buffer. B04 ends with the track played through that link (small and "
                "big buffer). Not any company's code. Facts: week-13/_research/facts-bluetooth.md. "
                "NAME: 'Row-Haan' in narration; 'Rohan V.' on screen. WORD-CLOCK via cues.json.",
        "tags": ["Humanitarians AI", "Bluetooth", "wireless earbuds", "SBC", "AAC", "aptX", "LDAC", "LE Audio",
                 "latency", "beginner", "Lyrical Literacy"],
    },
    "beats": beats,
}
json.dump(sheet, open("beat_sheet.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

cues = {
    "_comment": "Cue name -> anchor phrase spoken in that beat's narration. sync_cues.py resolves each against "
                "mp3/words.json and writes the measured fraction into beat_sheet.json at shot.remotion.props.cues.",
    "B00": {"bt": "how Bluetooth audio works", "earbuds": "wireless earbuds", "lags": "lags or cuts out", "built": "I built"},
    "B01": {"cd": "CD-quality", "fourteen": "fourteen hundred", "more": "more than", "squeeze": "squeezes",
            "sbc": "is SBC", "test": "my test track", "three": "three hundred", "quarter": "under a quarter"},
    "B02": {"radio": "Then the radio", "seventy": "seventy-nine", "hops": "hops between", "sixteen": "sixteen hundred",
            "wifi": "with Wi-Fi", "sim": "In my simulation", "seventeen": "seventeen", "afh": "Adaptive hopping",
            "one": "about one"},
    "B03": {"agree": "agree on a codec", "sbc": "SBC is the baseline", "aac": "prefer AAC", "aptx": "offer aptX",
            "ldac": "or LDAC", "more": "More data", "gaps": "without gaps"},
    "B04": {"lost": "Lost packets", "body": "your own body", "reserve": "in reserve", "sim": "In two",
            "fifty": "fifty millisecond", "two": "two hundred,", "never": "three hundred, never",
            "lag": "reason Bluetooth lags", "listen": "Listen:"},
    "B05": {"behind": "a couple of hundred", "videos": "for videos", "report": "report that", "holds": "holds the picture",
            "game": "A game", "laggy": "feel laggy"},
    "B06": {"le": "next generation", "lc3": "called LC3", "sig": "Bluetooth SIG", "half": "half the bit rate",
            "auracast": "Auracast", "any": "any number"},
    "B07": {"close": "phone close", "codec": "better codec", "game": "game mode"},
    "B08": {"close": "keep a little in reserve"},
}
json.dump(cues, open("cues.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("beat_sheet.json + cues.json written")
