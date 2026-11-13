"""Authors beat_sheet.json and cues.json for "How AI Music Generators Turn Text Into Audio"
(run once; later edits go in the sheet). Every number spoken is from evidence/run.log (codec.py) or
from the verified sources in week-07/_research/facts.md."""
import json

EYE = "HUMANITARIANS AI · AUDIO CONCEPTS"


def beat(bid, act, text, pattern, props, est):
    return {"beat_id": bid, "act": act, "narration_text": text,
            "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "choreographed",
                     "remotion": {"pattern": pattern, "props": {**props, "eyebrow": EYE}}},
            "estimated_duration_s": est}


beats = [
    beat("B00", "ASK",
         "Hi, I am Row-Haan and this video is about how AI music generators turn text into audio. You type a few "
         "words, and a minute later there's a song. Suno hasn't published how its own model works. But many published "
         "music generators share one idea: turn sound into tokens, and predict them one at a time, the way a chatbot "
         "writes words.",
         "ClaudeComposerAsk",
         {"greeting": "Hi, Rohan", "topic": EYE, "segment": "How AI Music Generators Turn Text Into Audio",
          "command": "How does an AI music generator turn a text prompt into a song?",
          "runningText": "working it out…", "folderLabel": "@HumanitariansAI", "modelLabel": "Claude",
          "effortLabel": "Desktop",
          "output": ["squeeze the sound into tokens", "predict the next token, again and again",
                     "let the words tilt each prediction"],
          "disclosure": "Narration: AI voice (Kokoro af_bella), script by Rohan V."}, 20),
    beat("B01", "BACKGROUND",
         "Here's the problem. Digital audio is a long list of numbers, one for every tiny moment. A CD stores forty-four "
         "thousand one hundred of them every second, for each ear. A three-minute song is almost sixteen million "
         "numbers. That's far too many to predict one by one. So first, the sound has to be squeezed into a much "
         "shorter list.",
         "TokSampleCount", {"title": "Audio Is a Lot of Numbers",
                            "sparkLine": "Sixteen million numbers is too many to predict."}, 20),
    beat("B02", "MECHANISM",
         "That's the job of a codec. It cuts the sound into short frames, about a hundredth of a second each. It "
         "compares each frame with a codebook: a list of one thousand and twenty-four typical sound shapes, learned "
         "from music. Then it writes down only the number of the closest one. That number is a token. A whole frame "
         "of sound becomes one number between zero and one thousand and twenty-three.",
         "TokCodebook", {"title": "A Frame Becomes a Token",
                         "sparkLine": "Find the closest shape. Keep its number."}, 24),
    beat("B03", "MATH",
         "One guess is rough, so a second codebook codes what the first one missed, and a third codes what's still "
         "left. Add the pieces together, and you get closer each time. My codec makes about ninety-four frames a "
         "second. With four codebooks, that's three hundred and seventy-five tokens a second: nearly four hundred "
         "times less data than a CD.",
         "TokResidual", {"title": "Each Codebook Fixes the Last One's Error",
                         "sparkLine": "Add the pieces. Get closer each time."}, 22),
    beat("B04", "MEASURED",
         "So I built one, and trained its codebooks on thirty-six short pieces of music I generated. Then I coded a "
         "piece it had never heard. With one codebook, it's dull and smeared: the treble is down by seventeen "
         "decibels. With four, clearer. With twelve, the treble is down by less than six. Listen: one codebook, four, "
         "twelve, then the original.",
         "TokCodecQuality", {"title": "I Built a Codec and Measured It",
                             "sparkLine": "More tokens, closer sound. The treble goes first."}, 34),
    beat("B05", "PREDICT",
         "Now the model. A music model reads tokens and guesses the next one. Mine is tiny: it just counts which token "
         "tends to follow each pair. On music it had never heard, it guessed the next token right sixteen and a half "
         "percent of the time. A blind guess would be right one time in a thousand. That's the whole trick, at a vastly "
         "bigger scale: learn what comes next.",
         "TokNextGuess", {"title": "Guess the Next Token",
                          "sparkLine": "Learning music is learning what comes next."}, 22),
    beat("B06", "THE TEXT",
         "And the text? In published systems, a text encoder turns your prompt into numbers that tilt every "
         "prediction. Meta's MusicGen does this: four codebooks, fifty frames a second, and a text encoder called T5 "
         "steering the model. In my toy, the words only pick which music it learned from. Calm piano, then busy drums. "
         "Neither is copied: the longest stretch it repeats from its training music is a quarter of a second.",
         "TokTextSteer", {"title": "The Words Tilt the Odds",
                          "sparkLine": "The prompt steers. It doesn't write the notes."}, 34),
    beat("B07", "WHAT TO DO",
         "So when you prompt Suno for a Lyrical Literacy track, remember: the words shift the odds, they don't write "
         "the notes. Generate a few versions and choose. Name the instruments, the mood and the tempo, because those "
         "are what the text can steer. And check the treble on headphones: when sound is squeezed into tokens, the "
         "high end is the first thing to go.",
         "HaiApplyCard",
         {"title": "Prompting Shifts the Odds",
          "lede": "The model predicts sound one token at a time. Your words steer the guesses.",
          "steps": ["Generate a few versions, then choose.",
                    "Name the instruments, the mood and the tempo.",
                    "Check the treble on headphones."],
          "sparkLine": "Steer, generate, listen, choose."}, 20),
    beat("B08", "OUTRO",
         "Sound becomes tokens, a model predicts the next one, and the words tilt the odds. I'm Row-Haan, for "
         "Humanitarians AI.",
         "HaiTitleOutro", {"title": "How AI Music Generators Turn Text Into Audio", "handle": "@HumanitariansAI",
                           "subline": "Rohan V."}, 8),
]

sheet = {
    "metadata": {
        "title": "How AI Music Generators Turn Text Into Audio", "slug": "ai-music-tokens-explainer", "topic": EYE,
        "register": "Pragmatist", "audience": "Humanitarians AI", "brand": "claude", "engine": "kokoro",
        "voice_kokoro": "af_bella", "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "aspect_ratio": "16:9", "fps": 30, "presenter": "Rohan V.", "channel": "@HumanitariansAI",
        "channel_title": "@HumanitariansAI", "handoff_name": "AIMusicTokens_RohanV",
        "ai_disclosure": "Narration is an AI voice (Kokoro af_bella, Rohan V.'s persistent choice for the series); "
                         "script and decisions by Rohan V.",
        "note": "Audio/AI explainer: how published music generators work on audio TOKENS. EXECUTABLE EVIDENCE: "
                "codec.py builds a residual-vector-quantization codec (MDCT frames, 12 k-means codebooks of 1,024) "
                "and a trigram next-token model on synthetic music (synth.py; no copyrighted audio), measures both on "
                "unseen music, and generates 6 s per prompt (coarse token predicted, finer tokens filled in); every "
                "number and picture in B01-B06 comes from that run (evidence/codec.json, evidence/run.log). B04 and "
                "B06 end with listening clips from the same run appended by mix_listen.py. MATH: B03's residual sum "
                "and token-rate arithmetic are typeset through runtime/scripts/typeset_math.py. FACTS: "
                "week-07/_research/facts.md (Suno's method is UNPUBLISHED and is never described; MusicGen numbers "
                "verified against its paper). Opening line follows docs/FELLOWS-SUBMISSION.md verbatim. NAME: "
                "narration spells 'Row-Haan'; on-screen text says 'Rohan V.'. No person icons. WORD-CLOCK via "
                "cues.json + sync_cues.py; props.durationSeconds written after audio.",
        "tags": ["Humanitarians AI", "AI music", "audio tokens", "Suno", "MusicGen", "codec", "beginner",
                 "Lyrical Literacy"],
    },
    "beats": beats,
}
json.dump(sheet, open("beat_sheet.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

cues = {
    "_comment": "Cue name -> anchor phrase spoken in that beat's narration. sync_cues.py resolves each against "
                "mp3/words.json and writes the measured fraction into beat_sheet.json at shot.remotion.props.cues. "
                "Re-run align.py then sync_cues.py after ANY narration edit.",
    "B00": {"type": "You type a few words", "suno": "Suno hasn't published", "tokens": "turn sound into tokens",
            "predict": "predict them one at a time"},
    "B01": {"problem": "Here's the problem", "list": "long list of numbers", "cd": "A CD stores", "song": "A three-minute song",
            "many": "far too many", "squeezed": "squeezed into a much shorter list"},
    "B02": {"codec": "the job of a codec", "frames": "short frames", "codebook": "compares each frame with a codebook",
            "learned": "learned from music", "closest": "number of the closest one", "token": "That number is a token",
            "range": "between zero and one thousand"},
    "B03": {"rough": "One guess is rough", "second": "a second codebook", "third": "a third codes", "add": "Add the pieces",
            "frames": "ninety-four frames", "four": "With four codebooks", "cd": "nearly four hundred times"},
    "B04": {"built": "So I built one", "never": "never heard", "one": "With one codebook", "treble": "the treble is down",
            "four": "With four, clearer", "twelve": "With twelve", "listen": "Listen: one codebook"},
    "B05": {"model": "Now the model", "reads": "reads tokens", "tiny": "Mine is tiny", "right": "guessed the next token right",
            "blind": "A blind guess", "trick": "That's the whole trick"},
    "B06": {"text": "And the text", "encoder": "a text encoder turns your prompt", "musicgen": "Meta's MusicGen",
            "t5": "called T5", "toy": "In my toy", "calm": "Calm piano", "copied": "Neither is copied"},
    "B07": {"odds": "the words shift the odds", "versions": "Generate a few versions", "name": "Name the instruments",
            "treble": "check the treble"},
    "B08": {"close": "the words tilt the odds"},
}
json.dump(cues, open("cues.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok", sum(len(b["narration_text"].split()) for b in beats), "words")
