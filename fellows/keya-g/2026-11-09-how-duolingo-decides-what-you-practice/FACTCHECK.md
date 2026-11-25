# FACTCHECK — How Duolingo Decides What You Practice Next

Narration is `SCRIPT.md` verbatim. Nothing in the script or the beat sheet was changed by this check. Where a claim
is weaker than the sentence that carries it, the row says so and suggests a wording for you to decide on.

## How this was checked

Every web source listed in `SCRIPT.md` was fetched and read. Each verdict names the source it rests on. A claim is
SUPPORTED only where a fetched page or paper says it. File access stayed inside `brutalist.art` and
`humanitarians-youtube`.

| Source (as listed in `SCRIPT.md`) | What was actually read |
|---|---|
| Duolingo blog, "How we learn how you learn" | Whole page. |
| Settles and Meeder, "A Trainable Spaced Repetition Model for Language Learning" | The 6-page PDF, text extracted and read: abstract, the Leitner section, the half-life section, the feature list, Tables 2 and 4, and the two user experiments. The ACL abstract page alone gave only metadata, so the PDF was needed. |
| Duolingo, half-life regression code and data (GitHub) | The README and `experiment.py`. Code only: used to cross-check the paper's formula and inputs. Not cited for any claim. |
| Duolingo blog, "Introducing Birdbrain" | Whole page. |
| Wikipedia, "Forgetting curve" | Whole page. |
| Ebbinghaus, *Memory* (York Classics) | The index page and the preface. |
| Birmingham City University, "Spaced repetition" | Whole page. |
| University of York, "Leitner system" | Whole page. |
| jisho.org (not in your source list; used only for the Japanese words) | Entry for 見る. The search did not return entries for します or みます as polite forms. |

Method note: the paper PDF could not be read through the fetch tool, so its text was extracted with a throwaway
PDF reader installed in a scratch folder outside the project. Nothing was added to the project.

**Verdicts:** SUPPORTED (a fetched source says it) · PARTLY (some of it, or it joins two things the source keeps apart) ·
SIMPLIFIED (true in outline) · NOT STATED (no fetched source says it) · EXEMPT (your own experience or view, so it is not
a sourced claim) · PROCESS (a statement about this video).

**Tally (38 claims):** 22 SUPPORTED · 6 SIMPLIFIED · 6 EXEMPT · 4 PROCESS. No PARTLY or NOT STATED claims remain.

## Changes since the last check (beats 7, 9, 10, 13)

`SCRIPT.md` was edited after the first check. Each change was re-checked against the sources and the script's
"Notes for the fact check". The earlier concerns on these beats are resolved by your edits, except the note under beat 9.

| Beat | What changed | Result |
|---|---|---|
| 7 | The last sentence is now "And once a skill's strength meter slips to half-full, it's time to practice." | Resolved. It uses the blog's wording and makes the meter a per-skill thing, which matches the paper (the meter is the average over a skill's words). No longer joined to one word's 50% point. |
| 9 | The 12% is dropped. The beat now says Duolingo's "prediction error was nearly half that of the Leitner system" and that "tests with real learners were more mixed". | Resolved. "Mixed" matches Table 4. The error line now says "prediction error", which is what the sources measure (see row 24). |
| 10 | "It doesn't predict when you'll forget" is gone. | Resolved. Every remaining claim is in the Birdbrain post. |
| 13 | "Use example numbers" added to the prompt, on screen and spoken. | Resolved. It tells viewers the half-life Claude gives is illustrative. |

## Claims by beat

| # | Beat | Claim | Verdict | Evidence |
|---|---|---|---|---|
| 1 | 1 | "Hi, I am Keya, and this video is about…" opens the video | PROCESS | Matches the required opening line in `docs/FELLOWS-SUBMISSION.md`. |
| 2 | 1 | "The voice you're hearing is an AI voice reading my script." | PROCESS | True: Kokoro `af_bella`. Required disclosure in `docs/FELLOWS-SUBMISSION.md`. |
| 3 | 2 | "I've been learning Japanese on Duolingo for over a year." | EXEMPT | Your own experience. |
| 4 | 2 | "Shimasu" means do; "mimasu" means look | SIMPLIFIED | Your own note. jisho.org's 見る gives "to see, to look, to watch…", so mimasu = look is consistent. する ("do") was not pulled up, and the polite forms します and みます were not returned by the search, so those two forms are not source-checked. Both are standard Japanese. |
| 5 | 2 | "I kept mixing up two words… And Duolingo kept bringing them back, until I finally got them right." | EXEMPT | Your own experience. |
| 6 | 3 | "Duolingo doesn't review words at random. It predicts when you'll forget each word, and brings it back just in time." | SIMPLIFIED | Paper: practice sessions use "words (lexeme tags) due for practice according to student model". Blog: the model predicts each word's half-life, and "the best time to practice is when you are on the verge of forgetting". "Just in time" is your plain-English shorthand: the blog's footnote notes the prediction is approximate. |
| 7 | 4 | "In 1885, Hermann Ebbinghaus studied his own memory and described the forgetting curve" | SIMPLIFIED | Blog: "These ideas go back to 1885, when… Ebbinghaus pioneered the concept of the forgetting curve." Wikipedia: he ran the study on himself over several years and published in 1885. Preface to *Memory*: "The tests were all made upon myself". 1885 is the publication. |
| 8 | 4 | The forgetting curve: "without any effort to keep it, what we learn fades away over time" | SUPPORTED | Wikipedia: "measures the decline of memory retention across time, showing how information is lost when there is no attempt to retain it." |
| 9 | 5 | "Short practices spread out over time work better than cramming" | SUPPORTED | Blog: "short practices spaced out over time is better for learning than 'cramming.'" Paper intro; BCU says the same. |
| 10 | 5 | "Gradually increasing the gaps between practices works even better" | SUPPORTED | Blog (lag effect): "You can learn even better if you gradually increase the spacing between practices." Paper intro; BCU: "increasingly longer intervals". |
| 11 | 5 | "The best time to review is just before you're likely to forget" | SUPPORTED | Blog: "the best time to practice is when you are on the verge of forgetting". BCU: "just before you're most likely to forget it". |
| 12 | 5 | "This is called spaced repetition." | SUPPORTED | Blog, paper and BCU all use the term for this. |
| 13 | 6 | "A simple version uses flashcards in boxes. This is the Leitner system." | SUPPORTED | York: "Cards are sorted into boxes based on how well the material is known." Paper: Leitner "intended for use with flashcards". |
| 14 | 6 | "Get a card right, and it moves to a box you review less often." | SUPPORTED | York: "Correctly answered cards progress to boxes that you don't need to review as often." |
| 15 | 6 | "Get it wrong, and it moves to a box you review more often." | SIMPLIFIED | York: wrong cards go "back to the first box for more frequent review". Paper: the card is "demoted to a shorter interval box". In York's version it goes all the way back to box 1, not just one box. Your wording fits the paper's. The B06 scene shows it moving one box left, so it matches the script. |
| 16 | 6 | "Every card follows the same fixed rules." | SIMPLIFIED | Paper: Leitner and Pimsleur "can be interpreted as special cases of (2) using a few fixed, hand-picked weights", so one fixed rule set for all words. York: you assign each box a frequency, with an example schedule. The rules are fixed, but you choose them, and York's schedule is only an example. |
| 17 | 7 | "It gives every word its own half-life" | SUPPORTED | Blog: "we can learn to predict the half-life for each word in your long-term memory". Paper: one estimate per word (lexeme tag). |
| 18 | 7 | Half-life: "the time it takes for your memory strength to decrease by half" | SUPPORTED | Blog, verbatim. |
| 19 | 7 | "When the time since you last practiced a word equals its half-life, you have about a fifty-fifty chance of remembering it." | SUPPORTED | Paper formula p = 2^(−Δ/h): when Δ = h, p = 2^(−1) = 0.5, "on the verge of being unable to remember". Blog: "only a 50% chance you'll remember". The blog's footnote says a predicted 0.5 means the real rate is about 37 to 63%, which supports "about". |
| 20 | 7 | "And once a skill's strength meter slips to half-full, it's time to practice." | SUPPORTED | Blog: "Once the meter slips to half-full, though, you know it's time to practice." Paper: the meter shows "the average probability that the student can… correctly recall a random target word from the lessons in this skill", so it is per skill, not per word. The scene draws the meter as its own labelled illustration, apart from the single word's curve. |
| 21 | 8 | "…combined machine learning and data science into a new statistical model, called half-life regression." | SUPPORTED | Blog: "combining modern machine learning and data science techniques… we invented a new statistical model we call half-life regression (HLR)". The paper's abstract says "novel model" and "modern machine learning techniques" but does not say "data science": that phrase is the blog's. |
| 22 | 8 | "It looks at your history with each word: how many times you've seen it, and how often you got it right or wrong." | SUPPORTED | Paper, interaction features: "the total number of times a student has seen the word", "the number of times it was correctly recalled", "the number of times incorrect". The paper also uses word (lexeme) tags. The script names only the counts, which is true as far as it goes. |
| 23 | 8 | "From that, it predicts how long each word will last in your memory." | SUPPORTED | Paper: HLR "indirectly estimat[es] the 'half-life' of a word… in a student's long-term memory". |
| 24 | 9 | "Duolingo reported that its prediction error was nearly half that of the Leitner system." | SUPPORTED | Blog: "the HLR error rate is nearly half that of the Leitner system method". Paper: "cutting MAE nearly in half"; "reduce MAE compared to Leitner by at least 45%"; Table 2 has HLR 0.128 and Leitner 0.235 (HLR's error is a little over half of Leitner's, a cut of about 45%). The measure is error in predicting whether a learner recalls a word, which "prediction error" says plainly. For context, on AUC, a ranking measure, Leitner scored slightly higher (0.542 against 0.538); the paper says so, and the script makes no accuracy claim beyond the error figure. |
| 25 | 9 | "But tests with real learners were more mixed." | SUPPORTED | Paper, Table 4, HLR against Leitner: +0.3% for overall activity, +0.3% for new lessons, −7.3% for practice sessions. The authors deployed HLR anyway, citing anecdotal praise for the strength meters. A later test of a simpler HLR against the full HLR was clearly positive, but that is not the comparison the script describes. No engagement percentage is used, as your note says. |
| 26 | 10 | "Later, Duolingo added another model, called Birdbrain." | SUPPORTED | The Birdbrain post says it "complements our other personalization system" (the half-life work) and does not say it replaced it, so "added" is right. Per your note, nothing implies a replacement. |
| 27 | 10 | "It makes an educated guess about whether you'll get an exercise right." | SUPPORTED | Birdbrain post: "Birdbrain makes an educated guess about whether a learner will get a given exercise right." |
| 28 | 10 | "It helps pick exercises at just the right difficulty: not so hard that you're frustrated, and not so easy that you've already mastered them." | SUPPORTED | Birdbrain post: exercises "at just the right difficulty level for this specific learner"; "if the material is too challenging, it's easy to get frustrated"; avoiding "material that you've already mastered". |
| 29 | 11 | "In my view, the model only sees what I do inside the app." | EXEMPT | Your view, and it says so. It fits the sources: the paper's inputs are practice counters and word tags. The sources describe the models as published, and the current app may use more. |
| 30 | 11 | "It doesn't know my interests, when I use Japanese somewhere else, or when I make a mistake while speaking." | EXEMPT | Your view. No fetched source says what the current app does or does not know, so it stays a view. The on-screen "In my view" keeps it that way. |
| 31 | 12 | "The idea behind spaced repetition is over a hundred years old." | SUPPORTED | Paper: the spacing effect was "first documented by Ebbinghaus (1885)". Blog: "These ideas go back to 1885." |
| 32 | 12 | "Duolingo's AI didn't invent it." | SUPPORTED | Blog and paper credit Ebbinghaus, Leitner (Leitner was Duolingo's first approach) and Pimsleur. |
| 33 | 12 | "It made it personal, one word at a time." | SIMPLIFIED | A half-life per word, estimated from your own history with that word (paper, interaction features). Some of the model's weights are shared across all learners (the word-tag weights), so "personal" refers to the history inputs. |
| 34 | 12 | "The best review isn't more practice. It's the right word, just before I forget it." | EXEMPT | Your conclusion. It restates the blog's "on the verge of forgetting" point. |
| 35 | 12 | "That's how shimasu and mimasu finally stuck." | EXEMPT | Your own experience. Careful: it implies the algorithm is why they stuck. That is your belief, not something the sources test. It is phrased as your story, so it is fine. |
| 36 | 13 | Prompt: "Explain Duolingo's half-life regression using one word I'm learning. Show what its half-life means, and when I should practice it next. Use example numbers." | PROCESS | Not a claim. "Use example numbers" tells Claude, and the viewer, that the half-life is illustrative: the sources do not publish any learner's real per-word half-lives. |
| 37 | 13 | "…ask: was I just about to forget it?" | SUPPORTED | Matches the blog's "on the verge of forgetting" criterion. |
| 38 | 14 | "Built with Claude, for Humanitarians AI." | PROCESS | True: Claude helped draft and build, and the channel is Humanitarians AI. See the README for the human and AI split. |

## What you were right about

- Beat 8: the paper does not say right answers always lengthen a half-life, and the script does not say so. For the
  record, the blog does say it while walking through its example ("each time you remember correctly, h increases").
  The script does not use that, so nothing changes.
- Beat 10: the Birdbrain post never says it replaced half-life regression, and the script does not claim that.
- Beat 7: the fifty-fifty line comes from the paper's formula, as your note says.
- Beat 9: the blog's 9.5% and 12% do come from the table comparing two versions of HLR, and so does the abstract's 12%.
  Your edit drops the figure and says "mixed", which is what the first comparison (against Leitner) showed.
- Beat 12: "over a hundred years" rests on Ebbinghaus, as your note says.

## On-screen claims to check again at render

These are in the shot list and need a look at the real frames, not the source:

- B07 and B09 show a meter and bars. They must carry the label "illustrative" and no numbers at all. B09 no longer
  shows a 12%. Its second panel shows "mixed" with a flat line for overall activity and a down arrow for practice sessions.
- B07's strength meter is a separate drawing for a skill, apart from the single word's curve.
- B09's Leitner and half-life regression bars should have lengths in about the paper's ratio (0.235 to 0.128), with
  no axis numbers.
- B11 shows "my interests", "Japanese I use somewhere else" and "a mistake while speaking" as things the model
  does not see. The "In my view" label must stay on screen so it reads as your view.
- B02's kana, します and みます, must render as real glyphs, not boxes.
- No Duolingo logo, owl, colours-as-branding or app screenshot in any frame.
