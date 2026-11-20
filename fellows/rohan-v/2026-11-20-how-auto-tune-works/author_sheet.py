"""Authors beat_sheet.json and cues.json for "How Auto-Tune Works" (run once; later edits go in the sheet).

RENDERER: B00, B07 and B08 are the channel's standard Remotion cards. B01-B06 are HyperFrames compositions with
three.js scenes (hyperframes/), rendered at 4K into media/<beat>.mp4 (16:9) and pantry/<beat>-916.mp4 (9:16).
Their shot.remotion holds props only, so remotion_scenes.py skips them and sync_cues.py still writes the cues.

Numbers spoken are from evidence/run.log (autotune.py: a synthetic singer, a YIN detector and a PSOLA corrector, not
Antares' code) or from week-13/_research/facts-autotune.md. B05 plays the run's own three takes: as sung, gentle
correction, retune speed zero."""
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
        "Hi, I am Row-Haan and this video is about how Auto-Tune works: how software finds the note you sang, and "
        "moves it to the right one. I built a small version to see how.",
        "ClaudeComposerAsk",
        {"greeting": "Hi, Rohan", "topic": EYE, "segment": "How Auto-Tune Works",
         "command": "How does Auto-Tune fix a singer's notes?",
         "runningText": "working it out…", "folderLabel": "@HumanitariansAI", "modelLabel": "Claude",
         "effortLabel": "Desktop",
         "output": ["find the pitch", "pick the nearest note", "move it without a chipmunk voice"],
         "disclosure": "Narration: AI voice (Kokoro af_bella), script by Rohan V."}, 11),
    hf("B01", "PITCH",
       "A sung note is a wave that repeats. How often it repeats is its pitch: the A above middle C repeats four "
       "hundred and forty times a second. To find it, the software slides a copy of the wave along itself until the "
       "two line up. My detector was within five cents, about the smallest change most people can hear, ninety-three "
       "percent of the time.",
       "pitch", {"title": "Finding the Repeat"}, 19),
    hf("B02", "OFF KEY",
       "A semitone, one step on a piano, is a hundred cents. My synthetic singer, singing a short tune in C major, "
       "was off by about twenty-nine cents on average: never a wrong note, just a little sharp or flat.",
       "offkey", {"title": "A Little Sharp, a Little Flat"}, 13),
    hf("B03", "SNAP",
       "Auto-Tune moves each moment toward the nearest note in the key you choose. A setting called retune speed "
       "decides how fast. At a gentle sixty milliseconds, my singer averaged under seven cents off, and the vibrato "
       "survived. At zero, it snaps instantly: the voice sat within five cents of a note ninety-one percent of the "
       "time. That's the robotic sound, made famous by Cher's Believe in nineteen ninety-eight.",
       "snap", {"title": "Snap to the Note"}, 22),
    hf("B04", "SHIFTING",
       "To raise a pitch, you could speed the recording up, but it gets shorter. Auto-Tune's patent keeps the length "
       "by repeating whole cycles. For a big shift, both move the vowel too: in my test, up by over a quarter, a "
       "chipmunk. My version re-spaces single cycles instead, a method called PSOLA. The vowel moved under one "
       "percent.",
       "shift", {"title": "No Chipmunks"}, 20),
    hf("B05", "LISTEN",
       "Here's my singer: as sung, then gentle, then retune speed zero.",
       "listen", {"title": "Hear the Difference"}, 5),
    hf("B06", "THEN AND NOW",
       "Auto-Tune came out in nineteen ninety-seven, from an engineer who had used similar maths to read seismic "
       "data for oil. Today, pitch correction is a standard studio tool, often too subtle to notice.",
       "history", {"title": "From Oil to Pop"}, 12),
    rem("B07", "WHAT TO DO",
        "To try it: set your song's key first, start with a slow retune speed for a natural sound, and turn it to "
        "zero for the effect.",
        "HaiApplyCard",
        {"title": "Try Pitch Correction",
         "lede": "Find the repeat, pick the note, move it.",
         "steps": ["Set your song's key first.",
                   "Slow retune speed: natural.",
                   "Zero: the robot effect."],
         "sparkLine": "A little maths between you and the note."}, 9),
    rem("B08", "OUTRO",
        "Find the repeat, pick the note, and shift the pitch. I'm Row-Haan, for Humanitarians AI.",
        "HaiTitleOutro", {"title": "How Auto-Tune Works", "handle": "@HumanitariansAI", "subline": "Rohan V."}, 7),
]

sheet = {
    "metadata": {
        "title": "How Auto-Tune Works", "slug": "auto-tune-explainer", "topic": EYE,
        "register": "Pragmatist", "audience": "Humanitarians AI", "brand": "claude", "engine": "kokoro",
        "voice_kokoro": "af_bella", "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "aspect_ratio": "16:9", "fps": 30, "presenter": "Rohan V.", "channel": "@HumanitariansAI",
        "channel_title": "@HumanitariansAI", "handoff_name": "AutoTune_RohanV",
        "renderer": "B01-B06 HyperFrames + three.js (hyperframes/), the rest Remotion",
        "ai_disclosure": "Narration is an AI voice (Kokoro af_bella, Rohan V.'s persistent choice for the series); "
                         "script and decisions by Rohan V.",
        "note": "Audio explainer: how pitch correction works. EXECUTABLE EVIDENCE: autotune.py synthesises a singer "
                "(source-filter 'ah', an original 7-note phrase in C major, sung off-key on purpose), detects pitch "
                "with YIN, corrects it at two retune speeds with TD-PSOLA (using the detected pitch only), measures "
                "the corrected audio again, and shifts a held note by resampling, by the patent's resample + repeat "
                "cycles, and by PSOLA. B05 plays the three takes. Not Antares' code. Facts: "
                "week-13/_research/facts-autotune.md (inventor and producers unnamed). "
                "NAME: 'Row-Haan' in narration; 'Rohan V.' on screen. WORD-CLOCK via cues.json.",
        "tags": ["Humanitarians AI", "Auto-Tune", "pitch correction", "pitch detection", "PSOLA", "music technology",
                 "beginner", "Lyrical Literacy"],
    },
    "beats": beats,
}
json.dump(sheet, open("beat_sheet.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

cues = {
    "_comment": "Cue name -> anchor phrase spoken in that beat's narration. sync_cues.py resolves each against "
                "mp3/words.json and writes the measured fraction into beat_sheet.json at shot.remotion.props.cues.",
    "B00": {"at": "how Auto-Tune works", "finds": "finds the note", "moves": "moves it", "built": "I built"},
    "B01": {"wave": "a wave that repeats", "pitch": "is its pitch", "a": "the A above", "four": "four hundred",
            "slides": "slides a copy", "line": "line up", "detector": "My detector", "five": "within five cents",
            "ninety": "ninety-three"},
    "B02": {"semitone": "A semitone", "hundred": "a hundred cents", "singer": "synthetic singer", "cmajor": "C major",
            "twenty": "twenty-nine", "never": "never a wrong note", "sharp": "a little sharp"},
    "B03": {"nearest": "nearest note", "speed": "retune speed", "gentle": "a gentle sixty", "seven": "under seven",
            "vibrato": "the vibrato", "zero": "At zero", "ninety": "ninety-one", "robotic": "the robotic sound",
            "believe": "Believe"},
    "B04": {"speed": "speed the recording", "shorter": "gets shorter", "patent": "Auto-Tune's patent",
            "cycles": "whole cycles", "vowel": "move the vowel", "quarter": "over a quarter", "chipmunk": "a chipmunk",
            "respace": "re-spaces", "psola": "called PSOLA", "one": "under one"},
    "B05": {"sung": "as sung", "gentle": "then gentle", "zero": "speed zero"},
    "B06": {"came": "came out", "oil": "seismic", "today": "Today", "standard": "standard studio tool",
            "subtle": "too subtle"},
    "B07": {"key": "song's key", "slow": "slow retune", "zero": "to zero"},
    "B08": {"close": "shift the pitch"},
}
json.dump(cues, open("cues.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("beat_sheet.json + cues.json written")
