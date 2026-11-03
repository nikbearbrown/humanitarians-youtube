"""Authors beat_sheet.json and cues.json for "How AI Voices Read a Script" (run once; later edits go in the sheet).
Every number spoken here is from evidence/run.log (voice.py). Facts: week-10/_research/facts-tts.md."""
import json

EYE = "HUMANITARIANS AI · AUDIO CONCEPTS"


def beat(bid, act, text, pattern, props, est):
    return {"beat_id": bid, "act": act, "narration_text": text,
            "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "choreographed",
                     "remotion": {"pattern": pattern, "props": {**props, "eyebrow": EYE}}},
            "estimated_duration_s": est}


beats = [
    beat("B00", "ASK",
         "Hi, I am Row-Haan and this video is about how an AI voice reads a script, including the one reading this "
         "to you. It doesn't read letters the way you do. First it turns the words into sounds, and that step is "
         "where most of its mistakes happen.",
         "ClaudeComposerAsk",
         {"greeting": "Hi, Rohan", "topic": EYE, "segment": "How AI Voices Read a Script",
          "command": "How does an AI voice turn my script into speech?",
          "runningText": "working it out…", "folderLabel": "@HumanitariansAI", "modelLabel": "Claude",
          "effortLabel": "Desktop",
          "output": ["write out numbers and short forms", "turn every word into sounds",
                     "turn the sounds into a voice"],
          "disclosure": "Narration: AI voice (Kokoro af_bella), script by Rohan V."}, 16),
    beat("B01", "BACKGROUND",
         "A text-to-speech voice works in three steps. First it cleans up the text: doctor, not D R dot. Then it "
         "turns every word into phonemes, the small sounds speech is built from; English has about forty-four, "
         "depending on accent. Only then does the voice model turn those sounds into audio. This voice, Kokoro, "
         "never sees the spelling at all. It only gets the sounds.",
         "VoicePipeline", {"title": "Text, Then Sounds, Then a Voice",
                           "sparkLine": "The voice only hears the sounds."}, 24),
    beat("B02", "MECHANISM",
         "The middle step is called G to P: graphemes, the letters, to phonemes, the sounds. Ours uses a program "
         "called e-speak. It looks a word up in a dictionary, and if the word isn't there, it guesses from rules "
         "about how English letters usually sound. That works for most words. It goes wrong when the same letters "
         "make two different words.",
         "VoiceG2P", {"title": "Letters to Sounds",
                      "sparkLine": "A dictionary first, then rules."}, 22),
    beat("B03", "MEASURED",
         "I tested eight of them, like read, which can be reed or red, each in a sentence "
         "that makes its meaning clear. Sixteen sentences, ten right. Only two words came out right both ways. Last "
         "night I read a book comes out with reed, not red. There's no grammar check behind it, only a few clues "
         "from the word just before.",
         "VoiceHeteronyms", {"title": "Same Spelling, Two Words",
                             "sparkLine": "Sixteen sentences, ten right."}, 26),
    beat("B04", "NUMBERS",
         "The clean-up step does better. Doctor, street, one thousand twenty-four, the fifth of May: all right. "
         "But a price trips it up. It costs three dollars fifty comes out as dollar, three, fifty. Listen.",
         "VoiceNumbers", {"title": "Numbers and Short Forms",
                          "sparkLine": "Six of seven right. Prices aren't."}, 16),
    beat("B05", "THE FIX",
         "The fix is to spell a word the way it sounds. This voice got my name wrong, so every script spells it Row "
         "dash Haan. It read the drum, the dhole, as dee haal, and the sitaar as sitter, until I respelled them. "
         "Here's my name as the pronunciation step reads it, then respelled.",
         "VoiceRespell", {"title": "Spell It the Way It Sounds",
                          "sparkLine": "Respell it, then listen again."}, 20),
    beat("B06", "WHAT TO DO",
         "So when you write for an AI voice, write numbers and prices out as words. Respell names until they sound "
         "right. And listen for words with two meanings, then reword the line if it picks the wrong one.",
         "HaiApplyCard",
         {"title": "Writing for an AI Voice",
          "lede": "The voice says what the sounds say, not what you meant.",
          "steps": ["Write numbers and prices out as words.",
                    "Respell names until they sound right.",
                    "Listen for words with two meanings, and reword."],
          "sparkLine": "Write it the way it should sound."}, 15),
    beat("B07", "OUTRO",
         "Clean the text, turn it into sounds, and check the sounds. I'm Row-Haan, for Humanitarians AI.",
         "HaiTitleOutro", {"title": "How AI Voices Read a Script", "handle": "@HumanitariansAI",
                           "subline": "Rohan V."}, 7),
]

sheet = {
    "metadata": {
        "title": "How AI Voices Read a Script", "slug": "ai-voice-explainer", "topic": EYE,
        "register": "Pragmatist", "audience": "Humanitarians AI", "brand": "claude", "engine": "kokoro",
        "voice_kokoro": "af_bella", "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "aspect_ratio": "16:9", "fps": 30, "presenter": "Rohan V.", "channel": "@HumanitariansAI",
        "channel_title": "@HumanitariansAI", "handoff_name": "AIVoices_RohanV",
        "ai_disclosure": "Narration is an AI voice (Kokoro af_bella, Rohan V.'s persistent choice for the series); "
                         "script and decisions by Rohan V. The video is about that voice.",
        "note": "Audio-concept explainer: how text-to-speech reads a script. EXECUTABLE EVIDENCE: voice.py runs the "
                "narrator's own G2P step (generate_audio_kokoro.phonemize: espeak-ng via kokoro-onnx) on 8 heteronym "
                "pairs, 7 normalisation cases and 4 of our own past mispronunciations, and synthesises the "
                "interesting cases with Kokoro af_bella, checked by faster-whisper base. Every IPA string and count "
                "in B01-B05 comes from that run (evidence/run.log, results.json). B04 and B05 end with the run's own "
                "clips (price.wav; name_default.wav, name_fixed.wav) appended by mix_listen.py. FACTS: "
                "week-10/_research/facts-tts.md. Opening line follows docs/FELLOWS-SUBMISSION.md verbatim. NAME: "
                "narration spells 'Row-Haan'; on-screen 'Rohan V.'; B05 plays the default reading of the name on "
                "purpose, as the evidence. No person icons. WORD-CLOCK via cues.json + sync_cues.py.",
        "tags": ["Humanitarians AI", "text to speech", "AI voice", "pronunciation", "phonemes", "beginner",
                 "Lyrical Literacy"],
    },
    "beats": beats,
}
json.dump(sheet, open("beat_sheet.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

cues = {
    "_comment": "Cue name -> anchor phrase spoken in that beat's narration. sync_cues.py resolves each against "
                "mp3/words.json and writes the measured fraction into beat_sheet.json at shot.remotion.props.cues.",
    "B00": {"reads": "reads a script", "letters": "doesn't read letters", "sounds": "into sounds", "mistakes": "most of its mistakes"},
    "B01": {"three": "three steps", "clean": "cleans up the text", "phonemes": "into phonemes", "fortyfour": "about forty-four",
            "model": "the voice model", "never": "never sees the spelling", "only": "only gets the sounds"},
    "B02": {"g2p": "G to P", "letters": "the letters", "espeak": "called e-speak", "dict": "in a dictionary",
            "rules": "guesses from rules", "works": "That works", "wrong": "goes wrong"},
    "B03": {"eight": "eight of them", "sixteen": "Sixteen sentences", "ten": "ten right", "two": "Only two words",
            "last": "Last night I read", "reed": "with reed", "clues": "a few clues"},
    "B04": {"better": "does better", "list": "Doctor, street", "price": "a price trips", "dollar": "dollar, three",
            "listen": "Listen"},
    "B05": {"fix": "The fix", "name": "got my name wrong", "dhol": "the drum", "sitar": "as sitter",
            "here": "Here's my name"},
    "B06": {"numbers": "numbers and prices", "names": "Respell names", "two": "two meanings"},
    "B07": {"close": "check the sounds"},
}
json.dump(cues, open("cues.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("beat_sheet.json + cues.json written")
