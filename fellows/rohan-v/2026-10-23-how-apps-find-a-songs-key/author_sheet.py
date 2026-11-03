"""Authors beat_sheet.json and cues.json for "How Apps Find a Song's Key" (run once; later edits go in the sheet).
Every number spoken here is from evidence/run.log (key.py). Facts: week-09/_research/facts-key.md."""
import json

EYE = "HUMANITARIANS AI · AUDIO CONCEPTS"


def beat(bid, act, text, pattern, props, est):
    return {"beat_id": bid, "act": act, "narration_text": text,
            "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "choreographed",
                     "remotion": {"pattern": pattern, "props": {**props, "eyebrow": EYE}}},
            "estimated_duration_s": est}


beats = [
    beat("B00", "ASK",
         "Hi, I am Row-Haan and this video is about how apps find a song's key: the label, like A minor or C major, "
         "that a DJ app shows next to a track. Last week it was the tempo. This time the app has to work out which "
         "note the song keeps coming home to.",
         "ClaudeComposerAsk",
         {"greeting": "Hi, Rohan", "topic": EYE, "segment": "How Apps Find a Song's Key",
          "command": "How does an app work out what key a song is in?",
          "runningText": "working it out…", "folderLabel": "@HumanitariansAI", "modelLabel": "Claude",
          "effortLabel": "Desktop",
          "output": ["count which notes the song uses", "compare them with every key's shape",
                     "keep the closest match"],
          "disclosure": "Narration: AI voice (Kokoro af_bella), script by Rohan V."}, 17),
    beat("B01", "BACKGROUND",
         "A key is a set of seven notes with one of them as home. C major uses the white keys of a piano, and C is "
         "home. A minor uses the very same seven notes, but its home is A. Hold on to that, because that's exactly "
         "where apps go wrong.",
         "KeyNotes", {"title": "Seven Notes and a Home",
                      "sparkLine": "Same notes, different home."}, 16),
    beat("B02", "MECHANISM",
         "Step one: hear which notes are sounding. Every frequency is folded into one of twelve note names, whatever "
         "the octave. That's called chroma. Added up over the whole song, it gives twelve bars: how much of each note "
         "the song uses. In my C major pop song, C, G and E stand tallest. Here's how it sounds.",
         "KeyChroma", {"title": "Step One: Count the Notes",
                       "sparkLine": "Twelve bars: the song's note profile."}, 22),
    beat("B03", "MATH",
         "Step two: compare it with a template. In 1982, psychologists asked listeners how well each note fits a key, "
         "and those ratings give every one of the twenty-four keys a shape. The app slides the song's bars against all "
         "twenty-four shapes, and keeps the best match, measured by correlation. C major scores zero point nine eight. "
         "The next best, G major, only zero point seven two.",
         "KeyProfiles", {"title": "Step Two: Match a Key's Shape",
                         "sparkLine": "The closest shape names the key."}, 26),
    beat("B04", "MEASURED",
         "I built a detector this way, and tested it on sixty songs I generated: pop, rock, blues, and two kinds of "
         "minor ballad, each in all twelve keys. It named the key right on fifty of sixty. Pop, rock and blues: every "
         "single one.",
         "KeyGrid", {"title": "Sixty Songs, Fifty Right",
                     "sparkLine": "Pop, rock and blues: all right."}, 18),
    beat("B05", "THE CATCH",
         "The ten misses were all in one place: minor ballads that only use the notes of the natural minor scale. Ten "
         "of twelve came out as the major key with the same seven notes. For A minor, the match was zero point eight "
         "eight six, against zero point eight nine one for C major. Raise one note, the seventh, and all twelve come "
         "out right. The standard test gives this mistake partial credit.",
         "KeyRelative", {"title": "Same Notes, Wrong Home",
                         "sparkLine": "A minor and C major share every note."}, 28),
    beat("B06", "KEY CHANGE",
         "One label has a second problem: songs change key. This one moves up a semitone halfway, the classic pop key "
         "change. Asked for one key, my detector said C minor: neither of them. Listening in eight-second windows, it "
         "hears C major, then C sharp major.",
         "KeyChange", {"title": "When the Key Changes",
                       "sparkLine": "One label can't follow a key change."}, 20),
    beat("B07", "WHAT TO DO",
         "So when an app's key looks wrong, check the relative key first: A minor and C major share every note, and "
         "harmonic-mixing charts put them side by side. And on a song with a key change, check each section, not one "
         "label.",
         "HaiApplyCard",
         {"title": "When the Key Looks Wrong",
          "lede": "Most wrong keys share the right key's notes.",
          "steps": ["Check the relative key: A minor and C major share every note.",
                    "Expect neighbours: relative keys sit side by side on mixing charts.",
                    "On a song with a key change, check each section."],
          "sparkLine": "Same notes first, then the home note."}, 15),
    beat("B08", "OUTRO",
         "Count the notes, match a shape, then check the home note. I'm Row-Haan, for Humanitarians AI.",
         "HaiTitleOutro", {"title": "How Apps Find a Song's Key", "handle": "@HumanitariansAI",
                           "subline": "Rohan V."}, 7),
]

sheet = {
    "metadata": {
        "title": "How Apps Find a Song's Key", "slug": "song-key-explainer", "topic": EYE,
        "register": "Pragmatist", "audience": "Humanitarians AI", "brand": "claude", "engine": "kokoro",
        "voice_kokoro": "af_bella", "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "aspect_ratio": "16:9", "fps": 30, "presenter": "Rohan V.", "channel": "@HumanitariansAI",
        "channel_title": "@HumanitariansAI", "handoff_name": "KeyDetection_RohanV",
        "ai_disclosure": "Narration is an AI voice (Kokoro af_bella, Rohan V.'s persistent choice for the series); "
                         "script and decisions by Rohan V.",
        "note": "Audio-concept explainer: how key detection works. EXECUTABLE EVIDENCE: key.py builds a detector the "
                "classic way (STFT chroma, Krumhansl-Kessler profiles, Krumhansl-Schmuckler correlation over 24 keys) "
                "and tests it on 60 synthetic Western songs (songs.py; pop, minor ballad, minor with raised 7th, rock "
                "with a flat 7th, 12-bar blues, each in 12 keys; no recordings), scored with the MIREX weights; every "
                "picture and number in B01-B06 comes from that run (evidence/run.log, evidence/scene.json). B02 ends "
                "with the example song (evidence/song_c_major_pop.wav) appended by mix_listen.py. MATH: B03's "
                "correlation is typeset through runtime/scripts/typeset_math.py. FACTS: week-09/_research/facts-key.md. "
                "Opening line follows docs/FELLOWS-SUBMISSION.md verbatim. NAME: narration spells 'Row-Haan'; "
                "on-screen text says 'Rohan V.'. No person icons. WORD-CLOCK choreographed via cues.json + sync_cues.py.",
        "tags": ["Humanitarians AI", "audio", "music key", "key detection", "chroma", "music technology", "beginner",
                 "Lyrical Literacy"],
    },
    "beats": beats,
}
json.dump(sheet, open("beat_sheet.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

cues = {
    "_comment": "Cue name -> anchor phrase spoken in that beat's narration. sync_cues.py resolves each against "
                "mp3/words.json and writes the measured fraction into beat_sheet.json at shot.remotion.props.cues.",
    "B00": {"label": "the label", "tempo": "it was the tempo", "home": "coming home to"},
    "B01": {"seven": "set of seven notes", "white": "the white keys", "chome": "and C is", "aminor": "A minor uses",
            "ahome": "its home is A", "wrong": "where apps go wrong"},
    "B02": {"one": "Step one", "fold": "folded into one of twelve", "octave": "whatever the octave", "chroma": "called chroma",
            "added": "Added up", "bars": "twelve bars", "tallest": "stand tallest", "listen": "Here's how it sounds"},
    "B03": {"two": "Step two", "template": "with a template", "listeners": "asked listeners", "shape": "a shape",
            "slides": "slides the song's bars", "corr": "measured by correlation", "cmaj": "C major scores",
            "rival": "The next best"},
    "B04": {"built": "I built a detector", "sixty": "sixty songs", "styles": "pop, rock, blues", "fifty": "fifty of sixty",
            "every": "every single one"},
    "B05": {"misses": "The ten misses", "natural": "natural minor scale", "ten": "Ten of twelve", "amin": "For A minor",
            "cmaj": "for C major", "raise": "Raise one note", "credit": "partial credit"},
    "B06": {"second": "a second problem", "semitone": "up a semitone", "one": "Asked for one key", "neither": "neither of them",
            "windows": "eight-second windows", "sharp": "C sharp major"},
    "B07": {"wrong": "looks wrong", "relative": "relative key first", "charts": "harmonic-mixing charts",
            "section": "check each section"},
    "B08": {"close": "the home note"},
}
json.dump(cues, open("cues.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("beat_sheet.json + cues.json written")
