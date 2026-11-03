"""Authors beat_sheet.json and cues.json for "How Apps Find a Song's Tempo" (run once; later edits go in the sheet).
Every number spoken here is from evidence/run.log (tempo.py). Facts: week-08/_research/facts.md."""
import json

EYE = "HUMANITARIANS AI · AUDIO CONCEPTS"


def beat(bid, act, text, pattern, props, est):
    return {"beat_id": bid, "act": act, "narration_text": text,
            "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "choreographed",
                     "remotion": {"pattern": pattern, "props": {**props, "eyebrow": EYE}}},
            "estimated_duration_s": est}


beats = [
    beat("B00", "ASK",
         "Hi, I am Row-Haan and this video is about how apps find a song's tempo: the B-P-M number a DJ app or a "
         "music library shows next to a track. Nobody tells the app where the beats are. It has to hear them. And "
         "the hard part turns out not to be finding a beat. It's choosing which one.",
         "ClaudeComposerAsk",
         {"greeting": "Hi, Rohan", "topic": EYE, "segment": "How Apps Find a Song's Tempo",
          "command": "How does an app work out a song's BPM?",
          "runningText": "working it out…", "folderLabel": "@HumanitariansAI", "modelLabel": "Claude",
          "effortLabel": "Desktop",
          "output": ["find where new sounds start", "find the gap that keeps repeating",
                     "choose which repeat is the beat"],
          "disclosure": "Narration: AI voice (Kokoro af_bella), script by Rohan V."}, 18),
    beat("B01", "BACKGROUND",
         "Tempo is counted in beats per minute. At a hundred and twenty B-P-M, a beat lands every half second: the "
         "place you'd tap your foot. This is four seconds of a rock groove I generated, with its beats marked. The app "
         "gets only the sound, never the marks. Here's how it sounds.",
         "TempoBeats", {"title": "A Beat Every Half Second",
                        "sparkLine": "The app hears the sound, not the marks."}, 18),
    beat("B02", "MECHANISM",
         "Step one: find where new sounds start. The sound is split into forty frequency bands, and at every moment "
         "the app asks how much louder each band just got. Add those jumps up, and you get the onset curve. A drum hit "
         "makes a spike. A held chord adds almost nothing. This is called spectral flux.",
         "TempoOnsets", {"title": "Step One: Where New Sounds Start",
                         "sparkLine": "Every hit becomes a spike."}, 20),
    beat("B03", "MATH",
         "Step two: slide the curve against a copy of itself. At most shifts, spikes miss spikes. At some, they land "
         "on top of each other, and the match jumps. This is called autocorrelation. Here, it matches at half a second, "
         "and even better at one second. Sixty divided by half a second is a hundred and twenty beats per minute. But "
         "sixty divided by one second is sixty. Both are real repeats. So which one is the beat?",
         "TempoAutocorr", {"title": "Step Two: Find the Repeat",
                           "sparkLine": "Two real repeats. One beat."}, 26),
    beat("B04", "MEASURED",
         "I built a detector this way and tested it on forty grooves: rock, funk, house, hip hop, slow ballads, drum "
         "and bass, waltzes and jazz swing, five tempos each. Picking the strongest repeat, it got the tempo right on "
         "thirteen of forty. Most misses were exactly half: it locked onto the kick and snare pattern, which repeats "
         "every two beats. So, like the free library librosa, it adds a preference: tempos near a hundred and twenty "
         "count for more, roughly where people tend to tap. Now the rock grooves come out right, five of five.",
         "TempoPrior", {"title": "Step Three: Choose the Beat",
                        "sparkLine": "A preference near 120 picks the beat."}, 30),
    beat("B05", "THE CATCH",
         "But that preference cuts both ways. Every slow ballad came out double: sixty became a hundred and twenty. "
         "Every drum and bass groove came out half: a hundred and seventy became eighty-five. And funk's off-beat kicks "
         "pulled it to a different repeat altogether. In all: seventeen of forty exactly right, and thirty-three of "
         "forty either right or exactly double or half. librosa, run on the same forty, gave the same verdict on "
         "thirty-four. The mistake is so common it has a name, the octave error, and the standard tests score it "
         "separately.",
         "TempoGrid", {"title": "Right, Double or Half",
                       "sparkLine": "Off by exactly double or half: an octave error."}, 30),
    beat("B06", "DRIFT",
         "A single number has a second problem: real drummers drift. This groove starts at a hundred and twenty and "
         "ends near a hundred and twenty-three. A beat grid at one fixed tempo is more than fifty milliseconds off "
         "within six seconds, and up to a hundred and forty. A beat tracker places each beat on a strong hit while "
         "keeping the spacing steady. That's the method librosa uses, from a 2007 research paper. Half its beats "
         "land within six milliseconds.",
         "TempoDrift", {"title": "Real Drummers Drift",
                        "sparkLine": "Follow the hits, not a fixed grid."}, 28),
    beat("B07", "WHAT TO DO",
         "So when your app shows a tempo that feels wrong, check whether it's exactly half or double what you'd tap. "
         "DJ apps let you halve or double the number, or set a B-P-M range so it can't happen. And for a live "
         "recording, check the beat grid, not just the number.",
         "HaiApplyCard",
         {"title": "When the BPM Looks Wrong",
          "lede": "Most wrong tempos are exactly double or half.",
          "steps": ["Tap along: is the number double or half what you tap?",
                    "Halve or double it, or set a BPM range.",
                    "On a live recording, check the beat grid, not just the number."],
          "sparkLine": "Trust your foot, then fix the number."}, 16),
    beat("B08", "OUTRO",
         "Find the hits, find the repeat, then choose the beat. I'm Row-Haan, for Humanitarians AI.",
         "HaiTitleOutro", {"title": "How Apps Find a Song's Tempo", "handle": "@HumanitariansAI",
                           "subline": "Rohan V."}, 7),
]

sheet = {
    "metadata": {
        "title": "How Apps Find a Song's Tempo", "slug": "song-tempo-explainer", "topic": EYE,
        "register": "Pragmatist", "audience": "Humanitarians AI", "brand": "claude", "engine": "kokoro",
        "voice_kokoro": "af_bella", "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "aspect_ratio": "16:9", "fps": 30, "presenter": "Rohan V.", "channel": "@HumanitariansAI",
        "channel_title": "@HumanitariansAI", "handoff_name": "TempoDetection_RohanV",
        "ai_disclosure": "Narration is an AI voice (Kokoro af_bella, Rohan V.'s persistent choice for the series); "
                         "script and decisions by Rohan V.",
        "note": "Audio-concept explainer: how tempo (BPM) detection works. EXECUTABLE EVIDENCE: tempo.py builds a "
                "detector the classic way (mel-band spectral flux, 8-s windowed autocorrelation, a log-normal "
                "preference centred at 120 BPM as librosa's default, Ellis 2007 dynamic-programming beat tracker) "
                "and tests it on 40 synthetic Western drum grooves (grooves.py; no recordings), cross-checked "
                "against librosa 0.11.0; every picture and number in B01-B06 comes from that run (evidence/run.log, "
                "evidence/scene.json). B01 ends with the example groove (evidence/groove_rock_120.wav) appended by "
                "mix_listen.py. MATH: B03's autocorrelation and BPM rule are typeset through "
                "runtime/scripts/typeset_math.py. FACTS: week-08/_research/facts.md. Opening line follows "
                "docs/FELLOWS-SUBMISSION.md verbatim. NAME: narration spells 'Row-Haan'; on-screen text says "
                "'Rohan V.'. No person icons (PROFESSOR BEAR LAW not triggered). WORD-CLOCK choreographed via "
                "cues.json + sync_cues.py; props.durationSeconds written after audio.",
        "tags": ["Humanitarians AI", "audio", "tempo", "BPM", "beat tracking", "music technology", "beginner",
                 "Lyrical Literacy"],
    },
    "beats": beats,
}
json.dump(sheet, open("beat_sheet.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

cues = {
    "_comment": "Cue name -> anchor phrase spoken in that beat's narration. sync_cues.py resolves each against "
                "mp3/words.json and writes the measured fraction into beat_sheet.json at shot.remotion.props.cues. "
                "Re-run align.py then sync_cues.py after ANY narration edit.",
    "B00": {"tells": "Nobody tells the app", "hear": "It has to hear them", "choose": "choosing which one"},
    "B01": {"counted": "counted in beats per minute", "half": "every half second", "tap": "tap your foot",
            "groove": "four seconds of a rock groove", "marked": "with its beats marked", "only": "gets only the sound",
            "listen": "Here's how it sounds"},
    "B02": {"one": "Step one", "bands": "forty frequency bands", "louder": "how much louder", "add": "Add those jumps up",
            "curve": "the onset curve", "spike": "makes a spike", "chord": "A held chord", "flux": "spectral flux"},
    "B03": {"two": "Step two", "miss": "spikes miss spikes", "land": "land on top", "auto": "called autocorrelation",
            "half": "matches at half a second", "one": "even better at one second", "div": "Sixty divided by half",
            "sixty": "divided by one second is sixty", "which": "which one is the beat"},
    "B04": {"built": "I built a detector", "forty": "forty grooves", "strongest": "Picking the strongest repeat",
            "thirteen": "thirteen of forty", "halfmiss": "exactly half", "pattern": "kick and snare pattern",
            "pref": "adds a preference", "tap": "people tend to tap", "rock": "five of five"},
    "B05": {"cuts": "cuts both ways", "ballad": "Every slow ballad", "dnb": "Every drum and bass", "funk": "funk's off-beat",
            "all": "In all", "octave": "thirty-three of forty", "librosa": "run on the same forty",
            "name": "the octave error", "tests": "score it separately"},
    "B06": {"drift": "real drummers drift", "starts": "starts at a hundred and twenty", "grid": "A beat grid",
            "fifty": "within six seconds", "max": "up to a hundred and forty", "tracker": "A beat tracker",
            "ellis": "2007 research paper", "within": "within six milliseconds"},
    "B07": {"wrong": "feels wrong", "halve": "halve or double", "range": "B-P-M range", "live": "live recording"},
    "B08": {"close": "choose the beat"},
}
json.dump(cues, open("cues.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("beat_sheet.json + cues.json written")
