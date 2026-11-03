"""Authors beat_sheet.json and cues.json for "How Noise-Cancelling Headphones Work" (run once; later edits go in
the sheet). Every number spoken here is from evidence/run.log (anc.py). Facts: week-09/_research/facts-anc.md."""
import json

EYE = "HUMANITARIANS AI · AUDIO CONCEPTS"


def beat(bid, act, text, pattern, props, est):
    return {"beat_id": bid, "act": act, "narration_text": text,
            "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "choreographed",
                     "remotion": {"pattern": pattern, "props": {**props, "eyebrow": EYE}}},
            "estimated_duration_s": est}


beats = [
    beat("B00", "ASK",
         "Hi, I am Row-Haan and this video is about how noise-cancelling headphones work: how they can make an "
         "engine's hum nearly disappear, but still let you hear someone talking. The trick is to add more sound, "
         "not less.",
         "ClaudeComposerAsk",
         {"greeting": "Hi, Rohan", "topic": EYE, "segment": "How Noise-Cancelling Headphones Work",
          "command": "How do noise-cancelling headphones make noise disappear?",
          "runningText": "working it out…", "folderLabel": "@HumanitariansAI", "modelLabel": "Claude",
          "effortLabel": "Desktop",
          "output": ["play the noise back upside down", "keep adjusting, thousands of times a second",
                     "low steady sounds cancel best"],
          "disclosure": "Narration: AI voice (Kokoro af_bella), script by Rohan V."}, 15),
    beat("B01", "BACKGROUND",
         "Sound is a wave of pressure. Add the same wave flipped upside down, and the two cancel: every high meets a "
         "low. That flipped copy is called anti-noise. Here's an engine hum at the ear, the anti-noise my simulated "
         "headphone made for it, and what's left.",
         "AncWaves", {"title": "Add the Wave, Upside Down",
                      "sparkLine": "Noise plus anti-noise: almost nothing."}, 17),
    beat("B02", "MECHANISM",
         "A microphone on the outside of the ear cup hears the noise first. A chip turns it into anti-noise and plays "
         "it through the speaker. Many headphones also have a microphone inside, listening to what's left. My simulated "
         "one uses it to keep adjusting its filter, forty-eight thousand times a second. The noise takes eighty-three "
         "microseconds to reach the ear, and the electronics take a hundred and twenty-five. So the chip has to predict "
         "a little of the future.",
         "AncSystem", {"title": "Listen, Flip, Check, Adjust",
                       "sparkLine": "The chip has to stay ahead of the noise."}, 26),
    beat("B03", "MATH",
         "Being a little late matters more at high pitch. A timing error of a tenth of a millisecond is a tiny slice "
         "of a hundred-hertz wave: three point six degrees, and the hum still drops twenty-four decibels. At two "
         "thousand hertz, the same delay is seventy-two degrees, and the anti-noise now adds to the noise. Past sixty "
         "degrees, there's no cancellation at all.",
         "AncPhase", {"title": "Late Matters More at High Pitch",
                      "sparkLine": "Same delay, bigger mistake at high pitch."}, 24),
    beat("B04", "MEASURED",
         "I ran four kinds of noise through my simulated headphone. Engine hum: twenty-five decibels quieter. Low "
         "rumble: thirty-one. Voices: only eleven. Clatter: none at all, in fact slightly louder. Steady, low sounds "
         "are predictable, so the chip can stay ahead of them. Sudden sounds aren't. Listen: the hum without it, then "
         "with it.",
         "AncTypes", {"title": "What It Cancels, and What It Can't",
                      "sparkLine": "Steady and low: gone. Sudden: still there."}, 26),
    beat("B05", "THE CURVE",
         "Across every pitch at once, the pattern is clear. At least ten decibels quieter up to about three hundred "
         "hertz, a little quieter up to three thousand, and above that, slightly louder. Real headphones handle those "
         "high sounds the old way: the ear cups and tips simply block them.",
         "AncCurve", {"title": "Quiet Lows, Untouched Highs",
                      "sparkLine": "The cups block the highs; the chip cancels the lows."}, 20),
    beat("B06", "WHAT TO DO",
         "So use noise-cancelling for steady noise: planes, trains, air conditioning. Get a good seal, because the "
         "cups and tips do the high frequencies. And with the hum gone, turn your music down: you don't have to play "
         "over it.",
         "HaiApplyCard",
         {"title": "Getting the Most From Noise-Cancelling",
          "lede": "It cancels steady, low noise. The seal blocks the rest.",
          "steps": ["Use it for steady noise: planes, trains, air conditioning.",
                    "Get a good seal: the cups and tips block the high sounds.",
                    "With the hum gone, turn your music down."],
          "sparkLine": "Cancel the hum, then lower the volume."}, 15),
    beat("B07", "OUTRO",
         "Flip the wave, stay ahead of it, and let the cups do the rest. I'm Row-Haan, for Humanitarians AI.",
         "HaiTitleOutro", {"title": "How Noise-Cancelling Headphones Work", "handle": "@HumanitariansAI",
                           "subline": "Rohan V."}, 7),
]

sheet = {
    "metadata": {
        "title": "How Noise-Cancelling Headphones Work", "slug": "noise-cancelling-explainer", "topic": EYE,
        "register": "Pragmatist", "audience": "Humanitarians AI", "brand": "claude", "engine": "kokoro",
        "voice_kokoro": "af_bella", "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "aspect_ratio": "16:9", "fps": 30, "presenter": "Rohan V.", "channel": "@HumanitariansAI",
        "channel_title": "@HumanitariansAI", "handoff_name": "NoiseCancelling_RohanV",
        "ai_disclosure": "Narration is an AI voice (Kokoro af_bella, Rohan V.'s persistent choice for the series); "
                         "script and decisions by Rohan V.",
        "note": "Audio-concept explainer: how active noise cancellation works. EXECUTABLE EVIDENCE: anc.py simulates a "
                "feedforward headphone (outside mic, 83 us acoustic lead, 125 us electronic latency, 128-tap filtered-x "
                "LMS adaptive filter, in-ear error mic) at 48 kHz on synthetic noise (engine hum, rumble, voice babble, "
                "clatter, pink noise; no recordings), and checks the phase-error rule against a simulated late copy; "
                "every picture and number in B01-B05 comes from that run (evidence/run.log, evidence/scene.json). B04 "
                "ends with the hum, off then on (evidence/engine_off_then_on.wav), appended by mix_listen.py. MATH: "
                "B03's phase rule is typeset through runtime/scripts/typeset_math.py. FACTS: "
                "week-09/_research/facts-anc.md. Opening line follows docs/FELLOWS-SUBMISSION.md verbatim. NAME: "
                "narration spells 'Row-Haan'; on-screen 'Rohan V.'. No person icons. WORD-CLOCK via cues.json.",
        "tags": ["Humanitarians AI", "audio", "noise cancelling", "ANC", "headphones", "acoustics", "beginner",
                 "Lyrical Literacy"],
    },
    "beats": beats,
}
json.dump(sheet, open("beat_sheet.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

cues = {
    "_comment": "Cue name -> anchor phrase spoken in that beat's narration. sync_cues.py resolves each against "
                "mp3/words.json and writes the measured fraction into beat_sheet.json at shot.remotion.props.cues.",
    "B00": {"hum": "engine's hum", "talk": "someone talking", "more": "add more sound"},
    "B01": {"wave": "a wave of pressure", "flip": "flipped upside down", "cancel": "the two cancel", "anti": "called anti-noise",
            "hum": "Here's an engine hum", "made": "the anti-noise my simulated", "left": "what's left"},
    "B02": {"outside": "on the outside", "chip": "A chip turns it", "speaker": "through the speaker", "inside": "a microphone inside",
            "adjust": "keep adjusting", "rate": "forty-eight thousand", "noise": "The noise takes", "elec": "the electronics take",
            "predict": "predict a little"},
    "B03": {"late": "a little late", "error": "a tenth of a millisecond", "hundred": "a hundred-hertz wave", "drops": "still drops",
            "two": "At two thousand", "adds": "adds to the noise", "sixty": "Past sixty"},
    "B04": {"four": "four kinds of noise", "engine": "Engine hum", "rumble": "Low rumble", "voices": "Voices", "clatter": "Clatter",
            "steady": "Steady, low sounds", "sudden": "Sudden sounds", "listen": "Listen"},
    "B05": {"every": "Across every pitch", "ten": "At least ten", "little": "a little quieter", "louder": "slightly louder",
            "cups": "the ear cups and tips"},
    "B06": {"steady": "steady noise", "seal": "good seal", "down": "turn your music down"},
    "B07": {"close": "do the rest"},
}
json.dump(cues, open("cues.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("beat_sheet.json + cues.json written")
