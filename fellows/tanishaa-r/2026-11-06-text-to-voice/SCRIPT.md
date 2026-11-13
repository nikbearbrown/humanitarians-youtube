# How a Computer Turns Text into a Voice (script v2, approved 2026-11-08; B04/B05 updated to the real demo output)

**Fellow:** Tanishaa · **Channel:** @HumanitariansAI · **Narrator:** Bella (Kokoro `af_bella`, an AI voice; disclosed on screen and aloud)
**Target length:** ~2½ minutes (about 430 spoken words), inside the 2–3 minute range · **Exports:** 16:9 at 3840×2160, plus a native 9:16 at 2160×3840
**Audience:** students who are new to AI. The channel's recurring question is when to use AI and when not to.
**Hook:** the narrator *is* the example. Every step is shown on Bella's own voice.

Each beat lists what's **on screen** first, then what Bella **says**.

---

### B00 · Cold open: the ask (~14 s)
**On screen:** The Claude app opens with the greeting "Hi, Tanishaa". The composer types: *"How does a computer turn text into a voice?"* The first lines of the answer appear. A small label reads "AI narration: Bella".
**Says:** "Hi, I am Tanishaa, and this video is about how a computer turns text into a voice. The voice you're hearing is Bella, an AI narrator reading a script I wrote. So she's also the example."

### B01 · The one-line summary (~11 s)
**On screen:** A writer types *"The computer reads the words out loud."*, hesitates, deletes **"reads the words out loud"** and retypes it as **"works out the sounds, then builds the wave."**
**Says:** "A computer doesn't read the way you do. It works out which sounds to make, plans how long and how high each one goes, and then builds the sound wave, number by number."

### B02 · The problem: writing isn't speech (~18 s)
**On screen:** Three tricky lines appear one at a time, each with the hard part highlighted:
*"I **read** it yesterday. I'll **read** it tomorrow."* · *"**Dr.** Lee lives on Oak **Dr.**"* · *"It costs **$5** in **2026**."*
**Says:** "Start with the problem. Writing is a shorthand for speech. The same letters can sound different: read and read. The same abbreviation can mean two things: doctor and drive. And numbers aren't words at all until something decides how to say them."

### B03 · How it works: four steps (~20 s)
**On screen:** A four-stage flow lights up as each step is named. **Clean up**: "$5" becomes "five dollars". **Sound it out**: words become phonemes, the symbols for speech sounds. **Plan the delivery**: timing, pitch and loudness for each sound. **Build the wave**: a neural network outputs the audio.
**Says:** "Most text-to-speech systems follow four steps. Clean up: spell out numbers and abbreviations. Sound it out: turn each word into phonemes, the small sounds speech is made of. Plan the delivery: how long, how high and how loud each sound should be. Then build the wave."

### B04 · What "build the wave" means (~22 s)
**On screen:** A sound wave zooms in until it becomes a row of dots, each one a number. A counter ticks up: **24,000 numbers per second**. Then a small panel labeled **"Bella"** shows a short list of numbers, the voice's style. It swaps to a different voice's numbers and the same sentence's wave changes shape.
**Says:** "Sound is just air pressure going up and down. Recorded digitally, it's a list of numbers, and Bella's audio uses twenty-four thousand of them every second. A neural network predicts those numbers. The voice itself is another list, two hundred fifty-six numbers. Swap that list, and the same words come out in a different voice."

### B05 · Worked example, run for real (~22 s)
**On screen:** Real output from the Kokoro engine that voices this video (`demo/tts_demo.py`), on the B02 lines. Each line shows the text, then the phonemes it chose, with the wrong part marked: *"I **read** it yesterday"* → `ɹˈiːd` ("reed", present tense) ✕ · *"Oak **Dr.**"* → `dˈɑːktɚ` ("doctor") ✕ · *"**$5**"* → `dˈɑːlɚ fˈaɪv` ("dollar five") ✕. Then two waveforms, Bella and Michael (another built-in voice), with one chip: "different voice, same mistakes".
**Says:** "Here's what Bella's own system did with those tricky lines. I read it yesterday came out as reed, the present tense. Oak Drive became Oak Doctor. And five dollars became dollar five. A different voice made the exact same mistakes, because the voice only changes the style, not the sounds."

### B06 · When to use it, and when not to (~26 s)
**On screen:** Two columns sort themselves as each item is spoken.
**Use it when:** you want to hear text read aloud · you're drafting narration · you're practicing pronunciation.
**Be careful when:** names and rare words show up · the tone really matters.
At the end, a third card drops in: **"A voice that sounds human can still be wrong. Say it's AI."**
**Says:** "So when is it useful? Reading text aloud for accessibility, drafting a narration, or hearing how a word sounds. Be careful with names and unusual words, which it often gets wrong, and with moments where tone matters. And because it sounds so human, always say it's an AI voice. Never copy a real person's voice without their permission."

### B07 · Verdict (~11 s)
**On screen:** A Claude artifact page titled "How a Computer Turns Text into a Voice" with three key findings:
1. It works out sounds; it doesn't understand the words the way you do.
2. A voice is a set of numbers you can swap.
3. Sounding human isn't the same as being right.
**Says:** "Three things to keep. It works out sounds; it doesn't read the way you do. A voice is just a set of numbers. And sounding human isn't the same as being right."

### B08 · Your turn (~22 s)
**On screen:** The Claude composer, greeting "Your turn.", with this prompt typed in:
> *"Here's a paragraph I want read aloud by an AI voice. Find every word it might say wrong (numbers, abbreviations, names, and words like 'read' or 'lead' that change sound with meaning), explain why, and rewrite the paragraph so it's spoken correctly."*

**Says:** "Your turn. Take something you've written and try this prompt: find every word an AI voice might say wrong, explain why, and rewrite it so it's spoken correctly. Then listen to both versions. You'll hear the difference."

### B09 · Outro (~5 s)
**On screen:** The title "Text into a Voice." in serif with a terracotta period, and @HumanitariansAI below it.
**Says:** "How a computer turns text into a voice. At Humanitarians AI."

---

## Build notes
- **Fact-check, done 2026-11-08 (`demo/tts_demo.py` → `demo/tts_output.json`):** the engine here is Kokoro-82M v1.0 through kokoro-onnx 0.6.1, which uses the **espeak-ng** phonemizer (not `misaki`, as v1 of these notes guessed). Output is 24,000 samples per second. A voice style is 256 numbers (`af_bella` is a 510×256 table, one row picked by text length).
- **The demo got the tricky lines wrong**, so B05 shows the mistakes (the fallback planned in v1): "read" → "reed" in both tenses, both "Dr." → "doctor", "$5" → "dollar five", identical in Bella and am_michael.
- The ONNX model returns audio only, no per-sound durations, so B05 no longer claims to show a length bar per sound.
- **B03 wording** says "most systems" on purpose: Kokoro plans timing and pitch inside one network, so the four steps are the general picture, not one exact architecture.
