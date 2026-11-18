# FACTCHECK — How Your Phone Types Japanese

## How this was checked

Keya allowed the web sources in `SCRIPT.md` to be fetched; local file access stayed inside `brutalist.art`
and `humanitarians-youtube`. Each verdict names the source it rests on. A claim is marked SUPPORTED only where
a fetched page or paper says it. Everything else says what is missing.

| Source (as listed in `SCRIPT.md`) | What was actually read |
|---|---|
| Wikipedia, Japanese language | Infobox and the first part of the article verbatim. The rest came through a summary only. |
| Wikipedia, Japanese input method | Whole article body, verbatim. |
| Glossika | Whole page. |
| Robertson, words with multiple kanji | Whole body text verbatim; only the last few thousand characters came through a summary. **It lists none of hashi, hana, ame or shiro.** |
| TUFS module | Whole page. It is about pitch accent and uses hashi and hana as examples. |
| Mori et al. (Kyoto) | The PDF was downloaded to a scratch folder outside the project and its text extracted. It is the paper "Discriminative Method for Japanese Kana-Kanji Input Method" (Tokunaga, Okanohara, Mori). The sections on the conversion graph, costs and features were read. |
| COLING kana-kanji paper | The Anthology page gives the title "Kana-Kanji Conversion System with Input Support Based on Prediction" and no abstract. The PDF is a scan with no text layer. **Not read.** |
| mozcpy (PyPI) | The PyPI metadata. It is an *unofficial* package ("no affiliation with Google"), and says nothing about how conversion works. `SCRIPT.md`'s label has been corrected to say so. Nothing in the narration relies on it. |
| Japanese Stack Exchange | **Blocked.** The fetch tool refuses that site. Not worked around. |
| Word segmentation slides | Slides 1 to 37 verbatim, the rest through a summary. They do not use the ここではきものをぬぐ example. |
| jisho.org (added by Keya) | JSON entries for あめ, しろ, はきもの, きもの, はし, はな and ぬぐ, all read in full. |
| IEEE Milestone (ETHW) | Whole page. |
| IPSJ Computer Museum, JW-10 | Whole page. |
| ACL Findings paper | The paper's abstract page. The title is "Alignment-Based Decoding Policy for Low-Latency and Anticipation-Free Neural Japanese Input Method Editors" (Transformer-based, not LLMs). The PDF would not extract, so only the abstract was read. |

**Verdicts:** SUPPORTED (a fetched source says it) · PARTLY (some of it) · NOT IN SOURCES (none of the fetched
sources contain it) · SIMPLIFIED (true in outline) · ILLUSTRATIVE (Keya's own illustrative explanation, not a sourced
claim) · UNCONFIRMED · OWN TEST / OWN FILES (Keya's test or this project's files) · EXEMPT (personal account).

**Tally (47 claims):** 25 SUPPORTED · 7 PARTLY · 6 SIMPLIFIED · 1 ILLUSTRATIVE · 2 OWN TEST · 2 OWN FILES · 4 EXEMPT.

## What changed since the last check

- **Beat 10** now says Transformers help keyboards convert as you type, and that the first word processor chose
  homophones by sentence context and frequency. The second is SUPPORTED. The first is PARTLY: the paper does apply
  Transformer networks to converting as you type, but it is a research paper, and "the same design behind ChatGPT" is
  not in it (see row 37 for the caveats). Nothing is contradicted any more.
- **Beat 11** lost its last sentence. What remains (mistakes, names and new words missing from the dictionary, wrong
  split or wrong kanji) is supported in outline; the missing-dictionary link is an inference, flagged in its row.
- **Beat 7** words (ame, shiro, and "edge" for hashi) are now SUPPORTED by jisho.org.
- **Beat 9**: "A person uses the situation" is marked ILLUSTRATIVE. The words in the example are verified on jisho.org;
  the example sentence itself is not in a fetched source (Stack Exchange is blocked).

## Still open

1. The ここではきものをぬぐ example has no fetched source (row 30).
2. The COLING paper's text could not be read, so beat 8 rests on the Mori et al. paper alone.
3. Robertson, which `SCRIPT.md` still lists for the homophones, does not contain them. jisho.org now covers them.

## Claims, beat by beat

| # | Beat | Claim (as spoken or shown) | Verdict | Basis |
|---|---|---|---|---|
| 1 | B01 | The video is about how a phone types Japanese | OWN TEST | Keya's story plan in `SCRIPT.md`. |
| 2 | B01 | The voice is an AI voice reading Keya's script | OWN FILES | `beat_sheet.json`: Kokoro `af_bella`; narration is `SCRIPT.md` verbatim. |
| 3 | B02 | Keya has learned Japanese on Duolingo for over a year | EXEMPT | Personal account. |
| 4 | B02 | hana trips her up: flower or nose | SUPPORTED | Glossika: "花 (flower) and 鼻 (nose), both words are pronounced the same—はな (hana)". |
| 5 | B02 | Typing hashi gives bridge, chopsticks or edge | SUPPORTED | jisho.org: 橋【はし】 "bridge", 箸【はし】 "chopsticks", 端【はし】 "end, tip, point, edge, margin", all common. TUFS also lists bridge and chopsticks. |
| 6 | B02 | The keyboard "has to guess" | SIMPLIFIED | Wikipedia (Japanese input method): "the converter attempts to guess the correct division of words." Fair shorthand for choosing among candidates. |
| 7 | B03 | Autocomplete feels like a new AI trick (the framing the film corrects) | EXEMPT | Opinion used as the misconception the film argues against. |
| 8 | B03 | Japanese keyboards were predicting words long before chatbots | PARTLY | Supported: kana-kanji conversion has been statistical and data-driven for decades (Tokunaga, Okanohara, Mori paper); Wikipedia describes predictive input; the COLING paper's title is "Kana-Kanji Conversion System with Input Support Based on Prediction" (its text could not be read). Caveat: converting a typed sound to the right word is not the same task as predicting the next word. Defensible as a teaching comparison. |
| 9 | B04 | Japanese is spoken by more than a hundred and twenty million people | SUPPORTED | Wikipedia (Japanese language) infobox: 123 million native speakers. The page says native speakers; the narration says "spoken by". |
| 10 | B04 | ...mostly in Japan | SUPPORTED | Wikipedia infobox: native to Japan. Partly rests on the fetch tool's summary of the page. |
| 11 | B04 | It is written without spaces between words | SUPPORTED | Glossika: "there's basically no space between words and sentences within a text". The part of the Wikipedia page that came through verbatim does not say it. |
| 12 | B05 | Japanese has three ways of writing, often mixed in one sentence | SUPPORTED | Glossika: "it's common to see single sentences which include all three systems." |
| 13 | B05 | Hiragana carries the grammar | SUPPORTED | Glossika: "Hiragana show grammatical information within a sentence". |
| 14 | B05 | Katakana is for foreign words, like Keya's name | PARTLY | Glossika: "Katakana are used for foreign loanwords, and sometimes for emphasis". Writing a foreign-origin personal name in katakana is a convention that none of the fetched pages states. |
| 15 | B05 | Kanji carry meaning; two kanji can share one sound, flower and nose, both hana | SUPPORTED | Glossika: "Kanji show the meaning of words" and the 花 / 鼻 hana example. TUFS also lists 鼻 and 花 as hana. |
| 16 | B06 | H-A-S-H-I typed in Latin letters becomes はし | SUPPORTED | Wikipedia (Japanese input method): text is entered in rōmaji, "which can then be converted to kana or kanji". |
| 17 | B06 | A simple kana keyboard stops there | OWN TEST | Keya's InputKing test: romaji to kana only, no kanji candidates. |
| 18 | B06 | はし could be three different words | SUPPORTED | jisho.org lists 橋 (bridge), 箸 (chopsticks) and 端 (edge) as はし. |
| 19 | B06 | A real Japanese keyboard, called an IME, has one more job: choosing the kanji | SUPPORTED | Wikipedia (Japanese input method): kana to kanji "is often a one-to-many process"; "offers a list of candidate kanji writings". |
| 20 | B07 | Hashi: bridge, chopsticks or edge | SUPPORTED | As the hashi row above (jisho.org, TUFS). |
| 21 | B07 | Hana: flower or nose | SUPPORTED | Glossika, TUFS and jisho.org (花【はな】 "flower", 鼻【はな】 "nose"). |
| 22 | B07 | Ame: rain or candy | SUPPORTED | jisho.org: 雨【あめ】 "rain" and 飴【あめ】 "(hard) candy, toffee", both common. |
| 23 | B07 | Shiro: white or castle | SUPPORTED | jisho.org: 白【しろ】 "white" and 城【しろ】 "castle", both common. |
| 24 | B07 | "Same sounds, different kanji" | SIMPLIFIED | TUFS shows pitch differs for hashi (bridge: low-high; chopsticks: high-low) and hana (nose unaccented; flower accented). That supports Keya's note. In kana the words are spelled identically, which is what a keyboard sees. |
| 25 | B08 | The IME lists every way to split the kana into words, and every kanji for each piece | SUPPORTED | Tokunaga, Okanohara, Mori: "a graph that represents all possible conversions", built "in order to use a dictionary". The COLING paper is a scan with no text layer and could not be read. |
| 26 | B08 | It scores each option by how common the word is | SUPPORTED | Same paper: word unigram probabilities and features, and a cost on each vertex and edge. |
| 27 | B08 | ...and how often those words appear together in real Japanese text | SUPPORTED | Same paper: word bigram and class (part-of-speech) bigram features, learned from data. Slightly simplified: part-of-speech pairs are scored too, not only word pairs. |
| 28 | B08 | It picks the highest-scoring path | SUPPORTED | Same paper: "select the most likely path in the graph", using the Viterbi algorithm. |
| 29 | B09 | Without spaces, even splitting is a guess | SUPPORTED | Glossika (no spaces) and Wikipedia (Japanese input method): the converter "attempts to guess the correct division of words". |
| 30 | B09 | ここではきものをぬぐ can mean "take off your shoes here" or "take off your kimono here" | PARTLY | jisho.org confirms the words: 履物【はきもの】 "footwear, shoes" (also written 履き物), 着物【きもの】 "kimono, clothing" and 脱ぐ【ぬぐ】 "to take off (clothes, shoes, etc.)". So ここで履物を脱ぐ and ここでは着物を脱ぐ are both real readings. The Stack Exchange page that is supposed to use this example could not be fetched (blocked, not circumvented), and the segmentation slides use a different example. The two-way split itself is therefore not shown in any fetched source. |
| 31 | B09 | A person uses the situation: at the front door, it's shoes | ILLUSTRATIVE | Keya's own illustrative explanation, not a sourced claim. Marked as such here and in `SCRIPT.md`. |
| 32 | B09 | The IME only has statistics: which split appears more often in text | SIMPLIFIED | The models are statistical (Tokunaga, Okanohara, Mori). Wikipedia adds that IMEs also learn the user's choices and recently selected words. "Only statistics" leaves those out. |
| 33 | B10 | Toshiba unveiled the first Japanese word processor, in the year the narration gives | SUPPORTED | Both IEEE Milestone (ETHW) and IPSJ museum give the narration's year. ETHW says publicly unveiled that October; IPSJ says announced that September and first shipped the following year. "Unveiled" is safe either way. |
| 34 | B10 | It converted kana to kanji with a dictionary and grammar rules | SUPPORTED | ETHW: "a practical kana-to-kanji conversion system with a machine-readable dictionary and grammatical analysis". |
| 35 | B10 | ...and chose between homophones using sentence context and how often words are used | SUPPORTED | IPSJ museum: homophone selection "based on factors such as the sentence context and use frequency". (ETHW separately mentions a "learning mechanism for homophone selection"; the narration no longer claims it learned the user's choices.) |
| 36 | B10 | Later keyboards counted words in huge amounts of text | PARTLY | Tokunaga, Okanohara, Mori: data-driven statistical models, with probability language models described as long established. "Huge amounts of text" is not stated in the parts read. |
| 37 | B10 | Today, neural networks called Transformers, the same design behind ChatGPT, are helping keyboards convert as you type | PARTLY | The cited Findings of ACL paper (abstract page read), "Alignment-Based Decoding Policy for Low-Latency and Anticipation-Free Neural Japanese Input Method Editors", applies attention-based encoder-decoder networks "such as Transformer" to "simultaneous kana-kanji conversion", which is converting as you type. Caveats: (1) it is a research paper showing a better quality-versus-delay trade-off; it does not say shipped keyboards use it, so "are helping" is a mild stretch. (2) "The same design behind ChatGPT" is not in the paper. Both are Transformers in the broad sense, but the paper uses an encoder-decoder and ChatGPT-style models are decoder-only. Only the abstract could be read (the PDF would not extract). |
| 38 | B11 | It still makes mistakes | SUPPORTED | Wikipedia (Japanese input method): "If the selected word boundaries are incorrect, the word boundaries can be moved"; conversion "is often a one-to-many process". |
| 39 | B11 | Names and brand-new words may not be in its dictionary | PARTLY | Tokunaga, Okanohara, Mori say the conversion graph is built from a dictionary, so a word missing from it cannot be offered. That is an inference. Wikipedia does not mention names or new words. "May" keeps the claim honest. |
| 40 | B11 | ...so it can split them in the wrong place or pick the wrong kanji | PARTLY | Wrong splits and one-to-many kanji choices are both in Wikipedia. That missing words cause them is in no fetched source. |
| 41 | B12 | Kanji confused Keya at first | EXEMPT | Personal account. |
| 42 | B12 | Kanji are why hana can mean flower or nose without confusion (in writing) | SUPPORTED | Glossika: kanji "show the meaning of words"; the hana example. |
| 43 | B12 | The keyboard has to guess which one Keya means, and so does Keya, every lesson | EXEMPT | Personal account. |
| 44 | B12 | When your phone suggests a word, it's doing what ChatGPT does: predicting what comes next | SIMPLIFIED | Wikipedia (Japanese input method) describes predictive suggestion on phones, "usually based on words sent in previous messages". Same broad task as a chatbot at a very different scale. Not "the same model". |
| 45 | B12 | Japanese keyboards were doing it decades earlier | SIMPLIFIED | Consistent with the first word processor and the statistical models. Same caveat as row 8: conversion versus next-word prediction. |
| 46 | B13 | The suggestion bar is "a tiny language model guessing for you" | SIMPLIFIED | A teaching metaphor. Some suggestion bars use small models, some use frequency counts. |
| 47 | B14 | Built with Claude, for Humanitarians AI | OWN FILES | `SCRIPT.md`: drafted with Claude from Keya's plan and edited by Keya. |

## Notes

1. **hashi, hana, ame, shiro.** All four are confirmed on jisho.org, which `SCRIPT.md` now lists for beats 7 and 9.
   TUFS adds that the pitch differs for hashi and hana.
2. **Conversion versus prediction.** The film's thesis equates kana-kanji conversion with predicting words.
   The sources show both are statistical and both are old, but they are different steps. Applies to rows
   6, 8, 44, 45 and 46.
3. **On-screen candidates.** No on-screen candidate list is a screenshot. Keya's InputKing test showed romaji to
   kana only, so every candidate list is an illustrative animation, as her script requires.
4. **Beat 8 and beat 11 examples.** The three paths in B08 (橋を渡る, 箸を渡る, 端を渡る) and the mis-cut けや with 毛 and 矢 in B11
   are illustrations. jisho.org confirms each word and reading (毛 け "hair", 矢 や "arrow", 渡る わたる "to cross over"), but not the phrases,
   and no source supports the example failure. They are labelled illustrative on screen where numbers or results appear.
5. **Beat 9 bars.** The two bars are drawn illustrative, with no numbers, and say so on screen. No source gives
   frequencies for the two splits, so none are shown.
6. **"zoomu" and 頭部.** `SCRIPT.md` records that a search answer claiming "zoomu" gives 頭部 is false. It is not used.
7. **Dates.** The narration contains one year, in beat 10, kept as Keya wrote it. No date was added to any file.
