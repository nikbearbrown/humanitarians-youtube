# How Your Phone Types Japanese — Script

**Fellow:** Keya G. · **Week 4** · **Voice:** Kokoro `af_bella` · **Pronounce:** Keya = kˈeɪjɛə ("Kay-yeah")

Story plan, topic, research and decisions: Keya. Example script drafted with Claude from Keya's story plan and research notes; Keya approved and edited it.
Visuals: simple illustrative graphics only (kana, kanji, candidate lists, probability bars, word-split paths). No real product logos or screenshots of commercial apps.

## 1. Intro
Hi, I am Keya and this video is about how your phone types Japanese, and why every Japanese sentence you type is a guess. The voice you're hearing is an AI voice reading my script.

## 2. Hook
I've been learning Japanese on Duolingo for over a year, and hana still trips me up: flower or nose? Now my keyboard has the same problem. I type hashi. Bridge, chopsticks, or edge? It has to guess.

## 3. Overview
On screen, typed then corrected: "Autocomplete is a new AI trick." → "Japanese keyboards were predicting words long before chatbots."

Autocomplete feels like a new AI trick. But Japanese keyboards were predicting words long before chatbots. Let's see how they guess which word you mean.

## 4. About Japanese
Japanese is spoken by more than a hundred and twenty million people, mostly in Japan. And it's written without spaces between words.
`[Wikipedia: Japanese language]`

## 5. Three scripts
Japanese has three ways of writing, often mixed in a single sentence. Hiragana carries the grammar. Katakana is for foreign words, like my own name, Keya. And kanji carry meaning: two different kanji can share one sound, like flower and nose, both read hana.
`[Glossika]`

## 6. Typing
On a keyboard, I type Latin letters. H-A-S-H-I becomes はし in hiragana. A simple kana keyboard stops right there. But はし could be three different words, so a real Japanese keyboard, called an IME, has one more job: choosing the kanji.
`[Keya's own test: InputKing kana keyboard]`

## 7. Homophones
Japanese has many words like that. Hashi is bridge, chopsticks or edge. Hana is flower or nose. Ame is rain or candy. Shiro is white or castle. Same sounds, different kanji.
`[Robertson; TUFS; jisho.org; Keya's Duolingo learning]`

## 8. How the IME chooses
So how does it choose? The IME lists every way to split my kana into words, and every kanji for each piece. It scores each option by how common the word is, and how often those words appear together in real Japanese text. Then it picks the highest-scoring path.
`[Mori et al.; Mozc]`

## 9. No spaces
Without spaces, even splitting is a guess. This sentence can mean "take off your shoes here" or "take off your kimono here." A person uses the situation: at the front door, it's shoes. The IME only has statistics: which split appears more often in text.
`[Japanese Stack Exchange; word segmentation slides; jisho.org]`

On screen: ここではきものをぬぐ large in kana with romaji underneath, then split two ways, one above the other, with は highlighted where it moves: ここで/はきもの/を/ぬぐ → ここで履物を脱ぐ → "Take off your footwear here" (shoe outline), and ここでは/きもの/を/ぬぐ → ここでは着物を脱ぐ → "Take off your kimono here" (kimono outline). Then side by side: "You: where you are" (front-door outline, points to footwear) and "IME: which split is more common in text" (two bars, footwear longer, labelled illustrative, no numbers).

"A person uses the situation: at the front door, it's shoes" is Keya's own illustrative explanation, not a sourced claim.

## 10. Old vs. new
This isn't new. In 1978, Toshiba unveiled the first Japanese word processor. It converted kana to kanji with a dictionary and grammar rules, and chose between homophones using sentence context and how often words are used. Later keyboards counted words in huge amounts of text. Today, neural networks called Transformers, the same design behind ChatGPT, are helping keyboards convert as you type.
`[IEEE Milestone; IPSJ museum; ACL Findings]`

## 11. Where it fails
It still makes mistakes. Names and brand-new words may not be in its dictionary, so it can split them in the wrong place or pick the wrong kanji.
`[Wikipedia: Japanese input method]` — partly confirmed (see FACTCHECK.md)

## 12. Verdict
Kanji confused me at first, but they're the reason hana can mean flower or nose without confusion. The keyboard just has to guess which one I mean, and so do I, every lesson. Every time your phone suggests a word, it's doing what ChatGPT does: predicting what comes next. Japanese keyboards were doing it decades earlier.

## 13. Your turn
Your turn. Paste this into Claude: Show me how predictive typing works in Japanese, English and Korean. What's the same, and what's hardest in each? Look at how each language splits words, and where guessing gets hard. And next time you type, watch the suggestion bar. It's a tiny language model guessing for you.

Prompt shown on screen: "Show me how predictive typing works in Japanese, English and Korean. What's the same, and what's hardest in each?"

## 14. Outro
How Your Phone Types Japanese. Built with Claude, for Humanitarians AI.

## Notes for the fact check
- Hana (花/鼻) and ame (雨/飴) differ slightly in pitch accent when spoken, but are written identically in kana, which is what matters for typing.
- The InputKing test showed romaji → kana only; no kanji candidates. Keep any IME candidate list as an illustrative animation, not a screenshot of a real product.
- A Google search answer claimed typing "zoomu" produces 頭部; that is false (頭部 is read tōbu). Not used.

## Sources
- Wikipedia, "Japanese language" — https://en.wikipedia.org/wiki/Japanese_language
- Wikipedia, "Japanese input method" — https://en.wikipedia.org/wiki/Japanese_input_method
- Glossika, "Hiragana, Katakana, Kanji" — https://ai.glossika.com/blog/hiragana-katakana-kanji
- Wesley C. Robertson, "A guide to words with multiple kanji" — https://wesleycrobertson.wordpress.com/2025/08/05/a-guide-to-words-with-multiple-kanji/
- TUFS Japanese language module — https://www.coelang.tufs.ac.jp/ja/en/pmod/practical/01-08-01.php
- Shinsuke Mori et al., kana-kanji conversion research (Kyoto University) — https://www.lsta.media.kyoto-u.ac.jp/mori/research/public/WTIM11.pdf
- Kana-kanji conversion paper (COLING 2000) — https://aclanthology.org/C00-1050.pdf
- mozcpy, an unofficial Python package built on the Mozc dictionary (the author has no affiliation with Google) — https://pypi.org/project/mozcpy
- Japanese Stack Exchange, "How does someone know when one word ends and the next one starts?" — https://japanese.stackexchange.com/questions/21145/how-does-someone-know-when-one-word-ends-and-the-next-one-starts
- "Word segmentation and lexical normalization for unsegmented languages" (slides) — https://speakerdeck.com/shigashiyama/word-segmentation-and-lexical-normalization-for-unsegmented-languages
- IEEE Milestone, "The First Word Processor for the Japanese Language, 1971–1978" — https://ethw.org/Milestones:The_First_Word_Processor_for_the_Japanese_Language,_1971-1978
- IPSJ Computer Museum, JW-10 — https://museum.ipsj.or.jp/en/heritage/jw_10.html
- ACL Findings, "Alignment-Based Decoding Policy for Low-Latency and Anticipation-Free Neural Japanese Input Method Editors" (Transformer-based IMEs, not LLMs) — https://aclanthology.org/2024.findings-acl.479.pdf
- jisho.org, entries for あめ, しろ, はきもの, きもの, はし, はな and ぬぐ — https://jisho.org
