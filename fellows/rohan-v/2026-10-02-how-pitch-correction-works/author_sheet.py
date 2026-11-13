"""Authors beat_sheet.json and cues.json for "How Pitch Correction Works" (run once; later edits go in the sheet)."""
import json

EYE = "HUMANITARIANS AI · AUDIO CONCEPTS"


def beat(bid, act, text, pattern, props, est):
    return {"beat_id": bid, "act": act, "narration_text": text,
            "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "choreographed",
                     "remotion": {"pattern": pattern, "props": {**props, "eyebrow": EYE}}},
            "estimated_duration_s": est}


beats = [
    beat("B00", "ASK",
         "Hi, I am Row-Haan and this video is about how pitch correction works: how a tool like Auto-Tune hears a note "
         "that's slightly off, and pulls it into tune. Every singer drifts a little, even good ones. The software can't "
         "hear the song the way you do. All it can do is measure, and it measures very fast.",
         "ClaudeComposerAsk",
         {"greeting": "Hi, Rohan", "topic": EYE, "segment": "How Pitch Correction Works",
          "command": "How does Auto-Tune know a note is off, and how does it fix it?",
          "runningText": "working it out…", "folderLabel": "@HumanitariansAI", "modelLabel": "Claude",
          "effortLabel": "Desktop",
          "output": ["measure the pitch, many times a second", "snap it to the nearest allowed note",
                     "pull it there, as fast as you choose"],
          "disclosure": "Narration: AI voice (Kokoro af_bella), script by Rohan V."}, 20),
    beat("B01", "BACKGROUND",
         "A sung note is air vibrating. The faster the vibration repeats, the higher the note sounds. The A above middle C "
         "repeats four hundred and forty times every second: four hundred and forty hertz. Double that, and you're an "
         "octave higher. Between two neighbouring piano keys, musicians count a hundred tiny steps, called cents. Pitch "
         "correction works in cents.",
         "PitchCycles", {"title": "A Note Is a Vibration That Repeats",
                         "sparkLine": "Faster repeats, higher note. Correction works in cents."}, 21),
    beat("B02", "MECHANISM",
         "To measure the pitch, the software slides a copy of the sound along itself. When the copy has moved by exactly "
         "one cycle, the two line up, and the difference between them drops almost to zero. That shift is one period. "
         "Here it's two point three milliseconds, so the note is four hundred and thirty hertz. The first Auto-Tune found "
         "pitch with this same idea, called autocorrelation.",
         "PitchFindPeriod", {"title": "Slide the Sound Along Itself",
                             "sparkLine": "Where the copy lines up, you have one period."}, 22),
    beat("B03", "MATH",
         "Next it turns that number into a note. Four hundred and thirty hertz sits just below A, which is four hundred "
         "and forty. How far below? Twelve hundred, times the base-two logarithm of the ratio between them: minus "
         "thirty-nine and a half cents. So the target is A, and the job is to raise this note by almost forty cents.",
         "PitchSnapCents", {"title": "From Hertz to Cents", "sparkLine": "The nearest note becomes the target."}, 20),
    beat("B04", "MEASURED",
         "So I wrote one. I synthesised seven sung notes, each a little off, with a scoop up into every note and vibrato "
         "on the long ones. On average, forty cents out. My detector measured the pitch every six milliseconds, "
         "and the corrector pulled each note to its target. Measured again afterwards, it's under three cents out. "
         "Listen: first as sung, then corrected.",
         "PitchMelodyFix", {"title": "I Built One and Measured It",
                            "sparkLine": "Forty cents out, then under three."}, 34),
    beat("B05", "RETUNE SPEED",
         "The setting that matters most is speed: how quickly the pitch is pulled to the target. Pull it instantly, and "
         "the slides and the vibrato vanish, leaving flat steps. That's the robotic sound Cher's song Believe made famous "
         "in 1998. Pull it slowly, over a quarter of a second, and the vibrato survives. It's eighteen cents from "
         "perfect, but it still moves like a voice. Instant, then slow.",
         "PitchRetuneSpeed", {"title": "Speed Decides How Human It Sounds",
                              "sparkLine": "Instant is robotic. Slow keeps the voice."}, 34),
    beat("B06", "THE CATCH",
         "Here's what it can't do: know which note you meant. My last note is seventy-five cents below G, which puts it "
         "closer to F sharp. Let the corrector pick from every note, and it lands, perfectly in tune, on F sharp. The "
         "wrong note. Tell it the song is in C major, where F sharp isn't allowed, and it goes to G.",
         "PitchWrongNote", {"title": "In Tune Isn't the Same as Right",
                            "sparkLine": "It picks the nearest note, not the one you meant."}, 20),
    beat("B07", "WHAT TO DO",
         "So if you tune a vocal for a Lyrical Literacy track, set the key and scale first. Keep the speed slow for a "
         "natural voice, and go fast only when you want the effect. Then listen all the way through. A corrector can put "
         "every note in tune. It can't make them the right notes.",
         "HaiApplyCard",
         {"title": "Set the Key, Then Choose the Speed",
          "lede": "Pitch correction measures and snaps. Choosing the note is still your job.",
          "steps": ["Set the key and scale before anything else.",
                    "Slow speed for a natural voice. Fast or instant only for the effect.",
                    "Listen all the way through: in tune is not the same as the right note."],
          "sparkLine": "Key first, speed second, ears last."}, 18),
    beat("B08", "OUTRO",
         "Pitch correction measures, snaps and pulls. You decide which note, and how fast. I'm Row-Haan, for "
         "Humanitarians AI.",
         "HaiTitleOutro", {"title": "How Pitch Correction Works", "handle": "@HumanitariansAI", "subline": "Rohan V."}, 8),
]

sheet = {
    "metadata": {
        "title": "How Pitch Correction Works", "slug": "pitch-correction-explainer", "topic": EYE,
        "register": "Pragmatist", "audience": "Humanitarians AI", "brand": "claude", "engine": "kokoro",
        "voice_kokoro": "af_bella", "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "aspect_ratio": "16:9", "fps": 30, "presenter": "Rohan V.", "channel": "@HumanitariansAI",
        "channel_title": "@HumanitariansAI", "handoff_name": "PitchCorrection_RohanV",
        "ai_disclosure": "Narration is an AI voice (Kokoro af_bella, Rohan V.'s persistent choice for the series); "
                         "script and decisions by Rohan V.",
        "note": "Audio-concept explainer: how pitch correction (Auto-Tune style) detects pitch, snaps it to a note and "
                "glides it there. EXECUTABLE EVIDENCE: pitch_demo.py synthesises a 7-note sung melody, detects pitch "
                "with YIN, snaps (chromatic or C major), glides with a retune time constant, shifts the audio with "
                "TD-PSOLA, then RE-MEASURES the result; every curve and number in B02-B06 comes from that run "
                "(evidence/pitch_demo.json). B04 and B05 end with listening clips from the same run (sung.wav, "
                "corrected_*.wav) appended to the narration track by mix_listen.py. MATH: B03's cents equation is "
                "typeset through runtime/scripts/typeset_math.py, no text fallback. The synthetic voice is labelled a "
                "test signal, never a real singer. Opening line follows docs/FELLOWS-SUBMISSION.md verbatim. NAME: "
                "narration spells 'Row-Haan'; on-screen text says 'Rohan V.'. WORD-CLOCK choreographed via cues.json "
                "+ sync_cues.py.",
        "tags": ["Humanitarians AI", "audio", "pitch correction", "Auto-Tune", "singing", "beginner",
                 "Lyrical Literacy"],
    },
    "beats": beats,
}
json.dump(sheet, open("beat_sheet.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

cues = {
    "_comment": "Cue name -> anchor phrase spoken in that beat's narration. sync_cues.py resolves each against "
                "mp3/words.json and writes the measured fraction into beat_sheet.json at shot.remotion.props.cues. "
                "Re-run align.py then sync_cues.py after ANY narration edit.",
    "B00": {"drift": "Every singer drifts", "measure": "All it can do is measure", "fast": "measures very fast"},
    "B01": {"air": "air vibrating", "faster": "faster the vibration repeats", "a440": "four hundred and forty times",
            "double": "Double that", "cents": "called cents", "works": "Pitch correction works in cents"},
    "B02": {"slides": "slides a copy of the sound", "lineup": "the two line up", "zero": "drops almost to zero",
            "period": "That shift is one period", "hz": "four hundred and thirty hertz", "first": "The first Auto-Tune"},
    "B03": {"note": "turns that number into a note", "below": "just below A", "how": "How far below",
            "log": "base-two logarithm", "minus": "minus thirty-nine", "target": "the target is A"},
    "B04": {"wrote": "So I wrote one", "seven": "seven sung notes", "scoop": "scoop up into every note",
            "average": "On average", "measured": "detector measured the pitch", "pulled": "pulled each note",
            "again": "Measured again afterwards", "listen": "Listen: first as sung"},
    "B05": {"speed": "matters most is speed", "instantly": "Pull it instantly", "vanish": "vibrato vanish",
            "robotic": "robotic sound", "slowly": "Pull it slowly", "survives": "the vibrato survives",
            "eighteen": "eighteen cents from perfect", "listen": "Instant, then slow"},
    "B06": {"cant": "what it can't do", "sixtytwo": "sixty-two cents below G", "closer": "closer to F sharp",
            "every": "pick from every note", "wrong": "The wrong note", "major": "in C major", "g": "it goes to G"},
    "B07": {"key": "set the key and scale", "slow": "Keep the speed slow", "listen": "listen all the way through",
            "right": "the right notes"},
    "B08": {"close": "You decide which note"},
}
json.dump(cues, open("cues.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok", sum(len(b["narration_text"].split()) for b in beats), "words")
