# How Your Phone Types Japanese

**Creator:** Keya G. · **Project:** Humanitarians AI / Brutalist Videos
**Reporting period:** Week 4

The folder is named for Week 4, the week this work counts toward.

[Script](SCRIPT.md) · [Beat sheet](beat_sheet.json) · [Portrait beat sheet](vertical/beat_sheet.json) · [Manim scenes](scenes.py) · [Portrait scenes](vertical/scenes.py) · [Fact check](FACTCHECK.md) · [Shot list](SHOTLIST.md) · [Prompts](PROMPTS.md) · [Frictional log](FRICTIONAL.md)

## This week's contribution

- **Question:** when I type "hashi" on a Japanese keyboard, how does it know whether I mean bridge, chopsticks or edge?
- **Prediction:** I thought the keyboard simply converted letters into characters.
- **What I built:** a 14-beat, 3:25 Brutalist explainer. It covers Japanese's three writing systems, how romaji becomes kana, homophones like hashi, hana, ame and shiro, how an IME scores word splits and kanji by how common they are and how often they appear together, the "footwear or kimono" sentence with no spaces, the 1978 Toshiba word processor, today's Transformer-based IMEs, and where it fails on names and new words.
- **Result:** the keyboard is predicting, not converting. A Japanese IME is a small language model, and Japanese keyboards were doing this decades before chatbots.
- **Next:** the Week 4 progress video.

## Human and AI work

**My decisions:**
- Topic from my interest in Japanese and over a year of learning it on Duolingo; my own homophone examples (hana, ame, shiro) come from that learning.
- Story order, hook, overview correction, verdict, Your Turn prompt and takeaway.
- Pronunciations chosen by ear from test clips for "hashi", "はし" and "ame", plus "AWS"-style letter spelling for H-A-S-H-I; my name in katakana as ケヤ.
- The design of beat 9: the sentence in kana, split two ways, with kanji and English for each meaning.
- I reviewed the audio, previews with audio, both review cuts and both masters.

**AI tools and voices:**
- Claude (chat) guided my research, corrected my notes, and drafted an example script from my story plan, which I approved.
- Claude Code wrote the beat sheets, Manim scenes, fact check, shot list and prompts, and ran the builds and gate fixes with my approval.
- Narration is AI-generated (Kokoro `af_bella`) and says so in its first beat.

**What I rejected or corrected:**
- A search-engine answer claimed typing "zoomu" gives 頭部 (cranium). That is false (頭部 is read tōbu), so it was not used.
- Beat 10 originally said researchers test "large language models"; my source is about Transformer-based IMEs, so the line was corrected.
- Beat 10's "learned which homophones its user chose" was softened to what the sources say: it chose using sentence context and frequency.
- Beat 11's "that's why names are typed in katakana" was removed because no source supports it.
- Source labels were corrected (the Mozc link is an unofficial package; the ACL paper is not about LLMs), and ame, shiro, はきもの and きもの were checked on jisho.org.

**What remains unverified or open:**
- See [FACTCHECK.md](FACTCHECK.md): most claims are supported; some are simplified or illustrative (the probability bars carry no real numbers; the 毛/矢 wrong split in beat 11 is an illustration, not a measured result).
- Beat 3 (the typing card) is marked "sparse by design" in the beat sheet, with a written reason.
- In portrait, two toolkit-controlled handles (`@HumanitariansAI` on the intro and outro) sit lower than my own 86% rule; Gate T passes them.

## Watch

| Format | File | Link |
|---|---|---|
| 16:9 landscape, 3840×2160, 3:25 | `JapaneseTyping_KeyaG.mp4` | [Watch on Drive](https://drive.google.com/file/d/1kSMnype8KNIbuQ0KvjX2vBn1XGncokpl/view?usp=drive_link) |
| 9:16 vertical, 2160×3840, 3:25 | `JapaneseTyping_KeyaG.mp4` | [Watch on Drive](https://drive.google.com/file/d/1KiAWKSzygeT90Yi1ZBgu1B-4M-PnCxoi/view?usp=drive_link) |

## Reproduce

Same toolkit and commands as the [Week 1 explainer](../2026-10-13-how-ai-draws-anime-frames/README.md#reproduce), on this folder.

## Sources

See the Sources list in [SCRIPT.md](SCRIPT.md#sources) and the claim-by-claim evidence in [FACTCHECK.md](FACTCHECK.md).
