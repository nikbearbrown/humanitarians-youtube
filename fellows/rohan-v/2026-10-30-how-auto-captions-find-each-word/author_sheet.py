"""Authors beat_sheet.json and cues.json for "How Auto-Captions Find Each Word" (run once; later edits go in the sheet).
Every number spoken here is from evidence/run.log (captions.py) or, for B05's two examples, the voice reel's
evidence/run.log (voice.py, AUDIO CHECK). Facts: week-10/_research/facts-asr.md."""
import json

EYE = "HUMANITARIANS AI · AUDIO CONCEPTS"


def beat(bid, act, text, pattern, props, est):
    return {"beat_id": bid, "act": act, "narration_text": text,
            "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "choreographed",
                     "remotion": {"pattern": pattern, "props": {**props, "eyebrow": EYE}}},
            "estimated_duration_s": est}


beats = [
    beat("B00", "ASK",
         "Hi, I am Row-Haan and this video is about how auto-captions find each word: how an app turns speech into "
         "text, and works out when each word was said. Our own videos depend on it. Every animation you see here is "
         "timed by it.",
         "ClaudeComposerAsk",
         {"greeting": "Hi, Rohan", "topic": EYE, "segment": "How Auto-Captions Find Each Word",
          "command": "How do auto-captions know what was said, and when?",
          "runningText": "working it out…", "folderLabel": "@HumanitariansAI", "modelLabel": "Claude",
          "effortLabel": "Desktop",
          "output": ["turn the sound into a picture", "predict the words, one piece at a time",
                     "line each word up with the sound"],
          "disclosure": "Narration: AI voice (Kokoro af_bella), script by Rohan V."}, 15),
    beat("B01", "BACKGROUND",
         "First, the sound becomes a picture: a spectrogram with eighty frequency bands, read in thirty-second "
         "chunks. The model our videos use is Whisper, an open model first trained on six hundred and eighty "
         "thousand hours of audio from the web. It looks at the picture and predicts the text, one small piece at "
         "a time.",
         "CapSpectro", {"title": "Sound Becomes a Picture",
                        "sparkLine": "A picture of sound, read like a page."}, 20),
    beat("B02", "MECHANISM",
         "To find when each word was said, it checks where in the sound it was looking while it wrote each word, "
         "then lines those moments up in order. That method is called dynamic time warping. Here's one sentence: "
         "when each word really starts, and when Whisper says it starts.",
         "CapTiming", {"title": "When Was Each Word Said?",
                       "sparkLine": "Where it looked, lined up in order."}, 19),
    beat("B03", "MEASURED",
         "I built twenty-four sentences from this narrator's voice, word by word, so I know exactly when each word "
         "starts. Whisper's base model, the one our pipeline uses, got two hundred and thirty-four of the two "
         "hundred and thirty-eight words right. Its word starts came about a quarter of a second early, and nine in "
         "ten were within three tenths of a second.",
         "CapAccuracy", {"title": "Words Right, Slightly Early",
                         "sparkLine": "Almost every word, a quarter second early."}, 24),
    beat("B04", "NOISE",
         "Then I added noise. With the speech ten decibels louder than the noise, it still got ninety-seven percent "
         "of the words. At five decibels, eighty-nine percent. With noise as loud as the speech, it fell apart: an "
         "error rate of over seventy percent. Listen to that sentence, and what it wrote.",
         "CapNoise", {"title": "How Much Noise It Takes",
                      "sparkLine": "Five decibels of headroom matters."}, 22),
    beat("B05", "THE CATCH",
         "Louder noise didn't make it stop. It wrote words that were never said: over three hundred words for two "
         "hundred and thirty-eight, with phrases repeated over and over. And even on clean speech it writes what it "
         "expects. My narrator says Row-Haan, and it writes Rohan. It hears dollar, three, fifty, and writes a neat "
         "price with a dollar sign.",
         "CapCatch", {"title": "It Writes What It Expects",
                      "sparkLine": "Confident text isn't proof it was said."}, 24),
    beat("B06", "WHAT TO DO",
         "So read auto-captions before you publish, especially names and numbers. YouTube itself says automatic "
         "captions can get words wrong. And record somewhere quiet: a few decibels of noise make a big difference.",
         "HaiApplyCard",
         {"title": "Before You Trust Auto-Captions",
          "lede": "They're a first draft, not a transcript.",
          "steps": ["Read them before you publish.",
                    "Check names and numbers first.",
                    "Record somewhere quiet."],
          "sparkLine": "Read the captions, then publish."}, 14),
    beat("B07", "OUTRO",
         "Picture the sound, predict the words, line them up, and then check them. I'm Row-Haan, for Humanitarians AI.",
         "HaiTitleOutro", {"title": "How Auto-Captions Find Each Word", "handle": "@HumanitariansAI",
                           "subline": "Rohan V."}, 7),
]

sheet = {
    "metadata": {
        "title": "How Auto-Captions Find Each Word", "slug": "auto-captions-explainer", "topic": EYE,
        "register": "Pragmatist", "audience": "Humanitarians AI", "brand": "claude", "engine": "kokoro",
        "voice_kokoro": "af_bella", "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "aspect_ratio": "16:9", "fps": 30, "presenter": "Rohan V.", "channel": "@HumanitariansAI",
        "channel_title": "@HumanitariansAI", "handoff_name": "AutoCaptions_RohanV",
        "ai_disclosure": "Narration is an AI voice (Kokoro af_bella, Rohan V.'s persistent choice for the series); "
                         "script and decisions by Rohan V.",
        "note": "Audio-concept explainer: how speech recognition writes captions and times each word. EXECUTABLE "
                "EVIDENCE: captions.py builds 24 sentences word by word from the narrator's voice (true word starts "
                "known) and runs faster-whisper base (the model our align.py uses) clean and with pink noise at 20 to "
                "-5 dB SNR; every number and picture in B01-B05 comes from that run (evidence/run.log, results.json, "
                "scene.json), except B05's two clean-speech examples, which are the voice reel's own audio check. B04 "
                "ends with the run's own 0 dB sentence (evidence/sentence_1_0db.wav) appended by mix_listen.py. "
                "FACTS: week-10/_research/facts-asr.md. Opening line follows docs/FELLOWS-SUBMISSION.md verbatim. NAME: "
                "'Row-Haan' in narration; 'Rohan V.' on screen. No person icons. WORD-CLOCK via cues.json.",
        "tags": ["Humanitarians AI", "speech recognition", "captions", "Whisper", "accessibility", "beginner",
                 "Lyrical Literacy"],
    },
    "beats": beats,
}
json.dump(sheet, open("beat_sheet.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

cues = {
    "_comment": "Cue name -> anchor phrase spoken in that beat's narration. sync_cues.py resolves each against "
                "mp3/words.json and writes the measured fraction into beat_sheet.json at shot.remotion.props.cues.",
    "B00": {"text": "speech into text", "when": "when each word was said", "ours": "Our own videos", "timed": "timed by it"},
    "B01": {"picture": "becomes a picture", "eighty": "eighty frequency bands", "chunks": "thirty-second", "whisper": "is Whisper",
            "hours": "six hundred and eighty", "predicts": "predicts the text", "piece": "one small piece"},
    "B02": {"find": "To find when", "looking": "where in the sound", "order": "lines those moments", "dtw": "dynamic time warping",
            "one": "Here's one sentence", "really": "really starts", "says": "Whisper says"},
    "B03": {"built": "I built twenty-four", "know": "I know exactly", "base": "base model", "words": "two hundred and thirty-four",
            "early": "a quarter of a second early", "nine": "nine in ten"},
    "B04": {"noise": "added noise", "ten": "ten decibels louder", "five": "At five decibels", "equal": "as loud as the speech",
            "rate": "an error rate", "listen": "Listen to that sentence"},
    "B05": {"stop": "didn't make it stop", "never": "never said", "count": "over three hundred", "repeat": "repeated over and over",
            "expects": "writes what it expects", "name": "My narrator says", "price": "dollar, three, fifty"},
    "B06": {"read": "read auto-captions", "names": "names and numbers", "youtube": "YouTube itself", "quiet": "somewhere quiet"},
    "B07": {"close": "check them"},
}
json.dump(cues, open("cues.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("beat_sheet.json + cues.json written")
