"""Authors beat_sheet.json and cues.json for "How Spatial Audio Works" (run once; later edits go in the sheet).

RENDERER: B00, B07 and B08 are the channel's standard Remotion cards. B01-B06 are HyperFrames compositions with
three.js scenes (hyperframes/), rendered at 4K into media/<beat>.mp4 (16:9) and pantry/<beat>-916.mp4 (9:16).
Their shot.remotion holds props only, so remotion_scenes.py skips them and sync_cues.py still writes the cues.

Numbers spoken are from evidence/run.log (spatial.py: a textbook spherical head, not Apple's code) or from
week-12/_research/facts-spatial.md. B04 ends with the run's own binaural clip (evidence/circle.wav), headphones on."""
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
        "Hi, I am Row-Haan and this video is about how spatial audio works: how headphones make a sound seem to come "
        "from beside you, behind you, or across the room. I built a small version to see how.",
        "ClaudeComposerAsk",
        {"greeting": "Hi, Rohan", "topic": EYE, "segment": "How Spatial Audio Works",
         "command": "How do my headphones make sound come from behind me?",
         "runningText": "working it out…", "folderLabel": "@HumanitariansAI", "modelLabel": "Claude",
         "effortLabel": "Desktop",
         "output": ["time the gap between your ears", "shade the far ear", "keep the sound still when you turn"],
         "disclosure": "Narration: AI voice (Kokoro af_bella), script by Rohan V."}, 14),
    hf("B01", "TIMING",
       "Your brain finds a sound with two ears. A sound on your right reaches your right ear first. In my head model, "
       "straight out to one side, the gap is about two thirds of a millisecond, and it shrinks to nothing as the sound "
       "moves in front of you.",
       "itd", {"title": "Two Ears, a Tiny Delay"}, 17),
    hf("B02", "LEVEL",
       "Your head also casts a shadow. High sounds can't bend around it, so the far ear hears them quieter: fourteen "
       "decibels quieter in my model. Low sounds bend around, so only two. Timing for low sounds, loudness for high "
       "ones. Lord Rayleigh worked that out in nineteen-oh-seven.",
       "ild", {"title": "Your Head Casts a Shadow"}, 18),
    hf("B03", "FRONT OR BACK",
       "But a sound in front of you and its mirror behind you give your ears the same timing and the same loudness. "
       "In my model, exactly the same. Your outer ears break the tie: their folds change the high notes depending on "
       "where a sound comes from.",
       "frontback", {"title": "Front or Behind?"}, 16),
    hf("B04", "THE FILTERS",
       "Researchers measure all of this with microphones inside a dummy head's ears, from more than seven hundred "
       "directions. Those measurements are called head-related transfer functions. Run a sound through the pair for "
       "one direction, and headphones play it from there. Put your headphones on, and listen.",
       "hrtf", {"title": "A Filter for Every Direction"}, 19),
    hf("B05", "HEAD TRACKING",
       "Then there's head tracking. Turn your head, and an ordinary headphone mix turns with you. Spatial audio uses "
       "motion sensors to turn the sound the other way, so it stays put in the room. Apple added this to AirPods in "
       "twenty twenty.",
       "tracking", {"title": "The Sound Stays Put"}, 16),
    hf("B06", "YOUR EARS",
       "Everyone's ears are different, so filters from a dummy head can mix up front and back. Apple's Personalized "
       "Spatial Audio scans your ears with the iPhone's camera to build a profile for you.",
       "personal", {"title": "Tuned to Your Ears"}, 12),
    rem("B07", "WHAT TO DO",
        "To try it: use headphones with head tracking, set up the personalized profile, and pick music mixed in Dolby "
        "Atmos.",
        "HaiApplyCard",
        {"title": "Try Spatial Audio",
         "lede": "Timing, shadow and your ears, rebuilt in your headphones.",
         "steps": ["Use headphones with head tracking.",
                   "Set up the personalized profile.",
                   "Pick music mixed in Dolby Atmos."],
         "sparkLine": "Two ears, and a little maths."}, 9),
    rem("B08", "OUTRO",
        "A tiny delay, a shadow, and the shape of your ears. I'm Row-Haan, for Humanitarians AI.",
        "HaiTitleOutro", {"title": "How Spatial Audio Works", "handle": "@HumanitariansAI", "subline": "Rohan V."}, 7),
]

sheet = {
    "metadata": {
        "title": "How Spatial Audio Works", "slug": "spatial-audio-explainer", "topic": EYE,
        "register": "Pragmatist", "audience": "Humanitarians AI", "brand": "claude", "engine": "kokoro",
        "voice_kokoro": "af_bella", "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "aspect_ratio": "16:9", "fps": 30, "presenter": "Rohan V.", "channel": "@HumanitariansAI",
        "channel_title": "@HumanitariansAI", "handoff_name": "SpatialAudio_RohanV",
        "renderer": "B01-B06 HyperFrames + three.js (hyperframes/), the rest Remotion",
        "ai_disclosure": "Narration is an AI voice (Kokoro af_bella, Rohan V.'s persistent choice for the series); "
                         "script and decisions by Rohan V.",
        "note": "Audio explainer: how headphones place sound around you. EXECUTABLE EVIDENCE: spatial.py renders a "
                "plucked-string melody through a textbook spherical head (Woodworth timing, Brown-Duda head shadow, "
                "a simple outer-ear filter) and measures ITD, ILD and the front/back ambiguity; B04 ends with the run's "
                "own binaural clip (evidence/circle.wav). Not Apple's code. Facts: week-12/_research/facts-spatial.md. "
                "NAME: 'Row-Haan' in narration; 'Rohan V.' on screen. LOGO LAW: Apple's mark beside its name. "
                "WORD-CLOCK via cues.json.",
        "tags": ["Humanitarians AI", "spatial audio", "AirPods", "HRTF", "binaural", "psychoacoustics", "beginner",
                 "Lyrical Literacy"],
    },
    "beats": beats,
}
json.dump(sheet, open("beat_sheet.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

cues = {
    "_comment": "Cue name -> anchor phrase spoken in that beat's narration. sync_cues.py resolves each against "
                "mp3/words.json and writes the measured fraction into beat_sheet.json at shot.remotion.props.cues.",
    "B00": {"spatial": "how spatial audio works", "behind": "behind you", "room": "across the room", "built": "I built"},
    "B01": {"ears": "two ears", "right": "on your right", "first": "right ear first", "model": "In my head model",
            "gap": "the gap is", "front": "in front of you"},
    "B02": {"shadow": "casts a shadow", "high": "High sounds", "fourteen": "fourteen", "low": "Low sounds",
            "two": "only two", "rule": "Timing for low", "rayleigh": "Lord Rayleigh"},
    "B03": {"mirror": "its mirror", "same": "same timing", "exactly": "exactly the same", "outer": "outer ears",
            "folds": "their folds"},
    "B04": {"dummy": "inside a dummy", "seven": "seven hundred", "hrtf": "head-related", "pair": "the pair",
            "there": "play it from there", "listen": "and listen"},
    "B05": {"tracking": "head tracking", "turn": "Turn your head", "with": "turns with you", "sensors": "motion sensors",
            "stays": "stays put", "apple": "Apple added"},
    "B06": {"different": "ears are different", "mixup": "mix up front", "scan": "scans your ears", "profile": "a profile"},
    "B07": {"headphones": "head tracking", "profile": "personalized profile", "atmos": "Dolby"},
    "B08": {"close": "shape of your ears"},
}
json.dump(cues, open("cues.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("beat_sheet.json + cues.json written")
