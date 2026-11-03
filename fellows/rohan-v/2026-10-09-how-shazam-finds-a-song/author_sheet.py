"""Authors beat_sheet.json and cues.json for "How Shazam Finds a Song" (run once; later edits go in the sheet).
Every number spoken here is from evidence/run.log (fingerprint.py)."""
import json

EYE = "HUMANITARIANS AI · AUDIO CONCEPTS"


def beat(bid, act, text, pattern, props, est):
    return {"beat_id": bid, "act": act, "narration_text": text,
            "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "choreographed",
                     "remotion": {"pattern": pattern, "props": {**props, "eyebrow": EYE}}},
            "estimated_duration_s": est}


beats = [
    beat("B00", "ASK",
         "Hi, I am Row-Haan and this video is about how Shazam finds a song: how an app can hear five seconds of "
         "music in a noisy room, and name the exact recording. It doesn't listen the way you do. It doesn't know the "
         "melody or the words. It looks for a handful of loud points, and the timing between them.",
         "ClaudeComposerAsk",
         {"greeting": "Hi, Rohan", "topic": EYE, "segment": "How Shazam Finds a Song",
          "command": "How does Shazam name a song from a few seconds of noisy audio?",
          "runningText": "working it out…", "folderLabel": "@HumanitariansAI", "modelLabel": "Claude",
          "effortLabel": "Desktop",
          "output": ["keep only the loudest points of the sound", "pair them up into short codes",
                     "let the codes vote on the song and the moment"],
          "disclosure": "Narration: AI voice (Kokoro af_bella), script by Rohan V."}, 20),
    beat("B01", "BACKGROUND",
         "First, the sound becomes a spectrogram. Time runs left to right, pitch runs bottom to top, and darker means "
         "louder. Then almost all of it is thrown away. Only the points that are louder than everything around them "
         "are kept: about twelve every second. The 2003 paper that described Shazam's method calls this a "
         "constellation map. In my test, with noise as loud as the music, twenty-four of these forty points "
         "survived. That's enough to work with.",
         "ShazamPeaks", {"title": "Keep Only the Loudest Points",
                         "sparkLine": "Thousands of numbers become a few stars."}, 24),
    beat("B02", "MECHANISM",
         "One point on its own says very little. So each point becomes an anchor, and is paired with a few points "
         "just after it. Each pair gives three numbers: the first frequency, the second frequency, and the time between "
         "them. Here: seven hundred and eighty-six hertz, then eleven hundred and seventy-four hertz, five hundredths "
         "of a second later. Those three numbers are packed into one code, called a hash. My version makes about "
         "fifty-seven of them every second.",
         "ShazamHashPairs", {"title": "Pair the Points Into Codes",
                             "sparkLine": "Two frequencies and a gap: one hash."}, 25),
    beat("B03", "MATH",
         "To search, the app makes hashes from your clip and looks each one up. Plenty of songs share a few hashes by "
         "chance. The trick is timing. For every match, take the time in the song and subtract the time in your clip. "
         "If the clip really comes from that song, the answers agree: they all point to the same moment. A real match "
         "is one tall spike. Chance matches are scattered.",
         "ShazamOffsetVote", {"title": "Let the Timing Vote",
                              "sparkLine": "A real match lines up. Chance doesn't."}, 22),
    beat("B04", "MEASURED",
         "So I built one. I made six songs from scratch, forty seconds each, and indexed them: about fourteen thousand "
         "hashes. Then I took five seconds of Song C, starting at twelve seconds, and buried it in cafe noise as loud "
         "as the music, through a phone-quality filter. Song C got thirty-three votes, at exactly twelve seconds. The "
         "next best song got two. Listen: the noisy clip, then the original.",
         "ShazamMatch", {"title": "I Built One and Tested It",
                         "sparkLine": "Thirty-three votes against two."}, 34),
    beat("B05", "NOISE",
         "How much noise can it take? I ran thirty random clips at each noise level. With the music ten decibels "
         "louder than the noise, all thirty were found. With noise as loud as the music, twenty-nine. With the noise "
         "five decibels louder, twenty-two. Ten decibels louder, nine. And when it failed, it said no match. It never "
         "named the wrong song.",
         "ShazamNoiseSweep", {"title": "How Much Noise It Takes",
                              "sparkLine": "When it can't tell, it says so."}, 22),
    beat("B06", "THE CATCH",
         "Here's what this kind of fingerprint can't do: it matches one exact recording, not the song. I played the "
         "same song again, one semitone higher: one vote. Six percent faster: four. The melody alone, hummed: one. To "
         "the fingerprint, those are different recordings, because every frequency and every gap has moved. Apps that "
         "recognise humming use a different kind of fingerprint, built on the melody.",
         "ShazamVersions", {"title": "It Matches a Recording, Not a Song",
                            "sparkLine": "Change the key or the speed, and the codes change."}, 24),
    beat("B07", "WHAT TO DO",
         "So for your Lyrical Literacy videos: a recording playing under your voice can still be matched, even under "
         "loud talking. Upload checks like YouTube's Content ID compare your audio with files that copyright owners "
         "submit. And not being matched isn't the same as being allowed. Use music you made, or music you're licensed "
         "to use.",
         "HaiApplyCard",
         {"title": "Music in Your Videos Can Be Recognised",
          "lede": "Fingerprinting hears through noise. Permission is a separate question.",
          "steps": ["A song under your voice can still be matched.",
                    "Upload checks compare your audio with copyright owners' files.",
                    "Not matched doesn't mean allowed: use music you made or licensed."],
          "sparkLine": "Recognised through noise. Allowed only with permission."}, 18),
    beat("B08", "OUTRO",
         "Shazam keeps the loudest points, turns pairs of them into codes, and lets the timing vote. I'm Row-Haan, for "
         "Humanitarians AI.",
         "HaiTitleOutro", {"title": "How Shazam Finds a Song", "handle": "@HumanitariansAI", "subline": "Rohan V."}, 8),
]

sheet = {
    "metadata": {
        "title": "How Shazam Finds a Song", "slug": "shazam-fingerprint-explainer", "topic": EYE,
        "register": "Pragmatist", "audience": "Humanitarians AI", "brand": "claude", "engine": "kokoro",
        "voice_kokoro": "af_bella", "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "aspect_ratio": "16:9", "fps": 30, "presenter": "Rohan V.", "channel": "@HumanitariansAI",
        "channel_title": "@HumanitariansAI", "handoff_name": "SongFingerprinting_RohanV",
        "ai_disclosure": "Narration is an AI voice (Kokoro af_bella, Rohan V.'s persistent choice for the series); "
                         "script and decisions by Rohan V.",
        "note": "Audio-concept explainer: how audio fingerprinting (Shazam's published method) identifies a "
                "recording. EXECUTABLE EVIDENCE: fingerprint.py builds the fingerprinter (spectrogram peaks, "
                "anchor/target-zone hashes, offset voting) on six synthetic songs (synth.py; no copyrighted audio) "
                "and tests it with noisy, band-limited clips; every picture and number in B01-B06 comes from that run "
                "(evidence/fingerprint.json, evidence/run.log). B04 ends with listening clips from the same run "
                "(clip_cafe.wav, original_segment.wav) appended by mix_listen.py. MATH: B03's offset rule is typeset "
                "through runtime/scripts/typeset_math.py. FACTS: _research/facts.md (week-07). Opening line follows "
                "docs/FELLOWS-SUBMISSION.md verbatim. NAME: narration spells 'Row-Haan'; on-screen text says "
                "'Rohan V.'. No person icons (PROFESSOR BEAR LAW not triggered). WORD-CLOCK choreographed via "
                "cues.json + sync_cues.py; props.durationSeconds written after audio.",
        "tags": ["Humanitarians AI", "audio", "Shazam", "audio fingerprinting", "music recognition", "beginner",
                 "Lyrical Literacy"],
    },
    "beats": beats,
}
json.dump(sheet, open("beat_sheet.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

cues = {
    "_comment": "Cue name -> anchor phrase spoken in that beat's narration. sync_cues.py resolves each against "
                "mp3/words.json and writes the measured fraction into beat_sheet.json at shot.remotion.props.cues. "
                "Re-run align.py then sync_cues.py after ANY narration edit.",
    "B00": {"listen": "doesn't listen the way you do", "points": "handful of loud points", "timing": "the timing between them"},
    "B01": {"spec": "becomes a spectrogram", "time": "Time runs left to right", "pitch": "pitch runs bottom to top",
            "darker": "darker means louder", "thrown": "thrown away", "kept": "are kept", "twelve": "about twelve",
            "constellation": "constellation map", "noise": "with noise as loud", "survive": "twenty-four of these forty"},
    "B02": {"one": "One point on its own", "anchor": "becomes an anchor", "paired": "paired with a few points",
            "three": "three numbers", "here": "Here:", "packed": "packed into one code", "hash": "called a hash",
            "rate": "fifty-seven of them"},
    "B03": {"search": "To search", "chance": "by chance", "timing": "The trick is timing", "subtract": "subtract the time",
            "agree": "the answers agree", "spike": "one tall spike", "scattered": "Chance matches are scattered"},
    "B04": {"built": "So I built one", "six": "six songs from scratch", "indexed": "indexed them", "took": "five seconds of Song C",
            "buried": "buried it in cafe noise", "votes": "thirty-three votes", "next": "The next best song",
            "listen": "Listen: the noisy clip"},
    "B05": {"how": "How much noise", "ran": "thirty random clips", "ten": "ten decibels louder than the noise",
            "zero": "noise as loud as the music", "five": "five decibels louder, twenty-two", "tenl": "Ten decibels louder, nine",
            "failed": "when it failed", "never": "It never named"},
    "B06": {"cant": "can't do", "exact": "one exact recording", "semitone": "one semitone higher", "faster": "Six percent faster",
            "hummed": "The melody alone, hummed", "moved": "every gap has moved", "apps": "Apps that recognise humming"},
    "B07": {"under": "under your voice", "upload": "Upload checks", "allowed": "isn't the same as being allowed",
            "licensed": "licensed to use"},
    "B08": {"close": "lets the timing vote"},
}
json.dump(cues, open("cues.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok", sum(len(b["narration_text"].split()) for b in beats), "words")
