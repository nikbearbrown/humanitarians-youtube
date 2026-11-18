# FACTCHECK — How Google Docs Lets Two People Type in the Same Sentence

Narration is `SCRIPT.md` verbatim. Nothing in the script or the beat sheet was changed by this check. Where a claim is
weaker than the sentence that carries it, the row says so and suggests a wording for you to decide on.

## How this was checked

Every web source listed in `SCRIPT.md` was fetched and read. Each verdict names the source it rests on. A claim is
SUPPORTED only where a fetched page says it.

| Source (as listed in `SCRIPT.md`) | What was actually read |
|---|---|
| Google Drive blog, "Making collaboration fast" (the `whats-different-about-new-google-docs.html` URL) | Whole post text, read from the page's own HTML. The first fetch tool returned only the site chrome, so the post body was downloaded directly and the text extracted. This is the post with the client/server lists, the Luiz and John walkthrough, the revision log and the collaboration protocol. |
| Google Drive blog, "Conflict resolution" (the `..._22.html` URL) | Whole post text, read the same way. This is the post that names operational transformation and shows the "EASY AS 123" shift example. |
| Wikipedia, "Operational transformation" | Page read, plus the page's wikitext searched for the example. The `Insert[0, "x"]` and `Delete[2, "c"]` example on the string "abc" is in the Basics section. |
| Wikipedia, "Conflict-free replicated data type" | Page read, plus the wikitext searched for "identifier", "unique", "permanent", "any order" and "central server". |
| Your own test | Not checkable. Taken as you describe it in `SCRIPT.md`. |

Two limits you should know about:

- **Age of the Google sources.** Both Google posts are old blog posts about "the new Google Docs" at the time they were
  written. Nothing read here says how Google Docs works today. The script speaks in the present tense. Wikipedia's lead
  says OT was adopted as a core technique behind Google Docs, but that is also a statement about the past. Beat 6 now
  attributes the explanation to Google's engineers for this reason (row 14).
- **Names.** "Luiz" and "John" are the blog's example editors. The narration does not use either name, so there is
  nothing to listen-check for them. The scenes use "me" and "teammate".

**Verdicts:** SUPPORTED (a fetched source says it) · PARTLY (some of it, or it joins two things the source keeps apart) ·
SIMPLIFIED (true in outline) · NOT STATED (no fetched source says it) · EXEMPT (your own experience or view, so it is not
a sourced claim) · PROCESS (a statement about this video).

**Tally (34 live claims; row 28 was removed):** 14 SUPPORTED · 7 SIMPLIFIED · 9 EXEMPT · 4 PROCESS · 0 PARTLY · 0 NOT STATED.
No row needs your decision. The earlier four (7, 20, 27, 28) are resolved by your edits to beats 3, 7 and 9. See "What needs your decision" below.

## Claims by beat

| # | Beat | Claim | Verdict | Evidence |
|---|---|---|---|---|
| 1 | 1 | "Hi, I am Keya, and this video is about…" opens the video | PROCESS | Matches the required opening line in `docs/FELLOWS-SUBMISSION.md`. |
| 2 | 1 | "The voice you're hearing is an AI voice reading my script." | PROCESS | True: Kokoro `af_bella`. Required disclosure in `docs/FELLOWS-SUBMISSION.md`. |
| 3 | 2 | "I've worked with shared documents." | EXEMPT | Your own experience. |
| 4 | 2 | "Sometimes two people type in the same line, and the text overlaps for a moment." | EXEMPT | Your own experience. |
| 5 | 2 | "I tested it in two windows. It only undid mine." | EXEMPT | Your own test (one document open in two windows, Ctrl+Z in one). Not independently repeatable here. The video says "I tested it", not "Google guarantees it". |
| 6 | 3 | "Google Docs doesn't let the last person win." | SIMPLIFIED | The blog says the old approach compared versions and the new one uses OT, and that "there are no more collaboration conflicts". It never uses "last person wins" about either. The line is a contrast with the viewer's likely belief, which is how the on-screen overview uses it. It is not a claim about how an older Docs behaved. |
| 7 | 3 | "It merges every change, so everyone ends up with the same document." | SUPPORTED | Replaces "nobody's words get lost", which no source states. The conflict-resolution post: "If OT is implemented correctly, it guarantees that once all editors have received all changes, everyone will be looking at the same version of the document." The protocol post: "At this point the server and both editors are looking at the same document". "Merges every change" fits "each change is merged properly with each other changes". |
| 8 | 3 (on screen) | "The last person to type wins." → "Every keystroke gets merged." | SIMPLIFIED | The first line is the viewer's misconception, not a claim. "Every keystroke" is close to the blog's "character-by-character" but is a paraphrase. |
| 9 | 4 | With the document a, b, c, one person adds x at the start while another deletes the third letter, c. | SUPPORTED | Wikipedia's Basics section uses the same shape: string "abc", O1 = Insert at position 0 of "x", O2 = Delete at position 2 of "c". Wikipedia counts from zero, so "position 2" is the third letter, as in your script. |
| 10 | 4 | "My x pushes everything one place to the right, so the third letter is now b." | SUPPORTED | After the insert the document is "xabc"; the third character is b. Checked by hand and matches Wikipedia: "if O2 is executed without transformation, it incorrectly deletes character b rather than c". |
| 11 | 4 | "If my teammate's change is applied exactly as it was sent, the wrong letter gets deleted." | SUPPORTED | Same Wikipedia passage. The blog's "EASY AS 123" example makes the same point: "He deleted the wrong characters!" |
| 12 | 5 | "When you open a Google Doc, it runs in two places: in your browser, and on Google's server." | SIMPLIFIED | The blog: "you need code running in two places: your browser and our servers". The post says "servers", plural. "Server" is a fair simplification and the blog itself switches to "the server" afterwards. |
| 13 | 5 | "Your browser doesn't send the whole document. It sends only your changes to the server, and receives everyone else's changes back." | SUPPORTED | The blog: the client "sends them [your edits] to the server, and processes other editors' changes when it receives them from the server", and "the information that is sent over the network is always the bare minimum needed to describe what changed". The "what each side keeps" lists in your notes match the post (the client also keeps its last revision number and its current view; the server keeps unprocessed changes, the revision log and the current document). |
| 14 | 6 | "Google's engineers explained that Docs solves this with a technique called operational transformation." | SUPPORTED | The conflict-resolution post, by a Google software engineer: "The algorithm that we use to handle these shifts is called operational transformation (OT)." The new attribution and past tense claim only what the post said, not how Docs works today. |
| 15 | 6 | "Each edit is an operation, like 'insert x at the start' or 'delete the third letter.'" | SIMPLIFIED | The blog says edits "boil down to three basic types of changes: inserting text, deleting text, and applying styles". It says "change", not "operation"; "operation" is Wikipedia's word. The two examples are insert and delete, which are two of the three types. |
| 16 | 6 | "When two operations clash, one is transformed to fit the other." | SUPPORTED | The blog: "Luiz must transform John's changes and make them relative to his local document", and some pairs of changes need no transform at all. "Clash" is a plain-language word for a pair that does. |
| 17 | 6 | "My teammate's delete is shifted from the third letter to the fourth, so the c is deleted, just as they meant." | SUPPORTED | Wikipedia: "O2' = Delete[3, 'c']... incremented by one due to the insertion", and executing it on "xabc" "deletes the correct character 'c'". The blog describes the same shift ("shift the changes over by two characters"). |
| 18 | 7 | "Transforming isn't enough. Every copy also needs the same changes, in the same order. That's the second part, the collaboration protocol." | SIMPLIFIED | The blog's split: the first problem (editing the same area) "is handled by operational transformation and the second problem is handled by the collaboration protocol". Its second problem is "when many changes happen at the same time, each change is merged properly with each other changes". "Same changes in the same order" is your reading of that, and it matches the walkthrough, where the server decides the order. |
| 19 | 7 | "The server processes changes in the order they arrive." | SUPPORTED | The blog: "The server got Luiz's change before John's so it processed that change first." |
| 20 | 7 | "It sends an acknowledgement back to the person who made the change, passes the change on to everyone else…" | SUPPORTED | The protocol post: "An acknowledgement of the change was sent to Luiz. The change itself was sent to John." The acknowledgement goes to the author only, as the narration now says. |
| 21 | 7 | "…and keeps every change in a revision log: the complete history of the document." | SUPPORTED | The blog: "The complete history of all processed changes (called the revision log)." The other post adds "we save your document as a revision log". |
| 22 | 8 | "Control Z only undid my own typing." | EXEMPT | Your own test. |
| 23 | 8 | "…so the document must keep track of who made each change." | EXEMPT (inference) | Your inference, and your notes already say so. Neither Google post mentions who made a change, or undo. "Must" states the inference as certain. Suggested: "so the document seems to keep track of who made each change". The scene marks this layer "my guess". |
| 24 | 8 | "I can also see where my teammate's cursor is." | EXEMPT | Your own observation. Not covered by the blog. |
| 25 | 8 | "Sometimes their text shows up a moment late, because each change has to travel to the server and back." | SIMPLIFIED | The "late" is your experience. The "because" follows from the blog's design (a change goes to the server, then is passed on to the others) but the blog never discusses delay for other people's text. It says the opposite for your own typing: "the speed or reliability of your network connection doesn't influence how fast you can type", because each editor applies their own changes locally first. The script only says other people's text arrives late, so the two do not conflict. |
| 26 | 9 | "CRDTs, short for conflict-free replicated data types." | SUPPORTED | Wikipedia, lead: "a conflict-free replicated data type (CRDT)". |
| 27 | 9 | "Each copy can be changed on its own, at the same time, without coordinating with the others, and the copies still end up the same." | SUPPORTED | Replaces the permanent-ID line. Wikipedia, lead: "The application can update any replica independently, concurrently and without coordinating with other replicas", and "they are guaranteed to eventually converge". "End up the same" drops the word "eventually", a fair plain-language simplification. The page does not describe how sequence CRDTs do this, and the narration no longer says. |
| 28 | 9 | (Removed.) "So changes can merge in any order, even without one central server." | REMOVED | No longer in the narration. Nothing to check. |
| 29 | 10 | "On a slow connection, text can appear late, or overlap for a moment before it settles." | EXEMPT | Your own experience ("in my experience"). |
| 30 | 10 | "If two people rewrite the same sentence in different ways, the system can merge both edits, but it can't decide which wording the team actually wanted." | EXEMPT (framing) | Your framing, and your notes say it is not a measured claim. It is consistent with the sources: OT only shifts positions so that all copies agree; nothing in either post says it judges intent. |
| 31 | 11 | "It doesn't avoid conflicts. It fixes them so fast that we almost never notice." | SIMPLIFIED | The blog says "there are no more collaboration conflicts" and that editors "can see each other's changes as they happen". "Doesn't avoid, fixes" is your reading of the mechanism. "So fast that we almost never notice" is an experience claim, not a measured one. |
| 32 | 11 | "Behind every keystroke, changes are shifted, ordered and shared." | SUPPORTED | Shifted (transformed), ordered (server order, revision log) and shared (passed to the others): all three are in the blog. |
| 33 | 11 | "When I pressed Control Z, only my words disappeared." | EXEMPT | Your own test, repeated from beat 2. |
| 34 | 12 | The prompt: explain operational transformation using the word "cat", when one person inserts a letter and another deletes one at the same time. | PROCESS | A prompt for the viewer. It is checkable by running it. It uses the same insert-and-delete case as beats 4 and 6, so Claude's answer should show the delete shifting by one place. "Whose change just moved my text?" is a question for the viewer, not a claim. |
| 35 | 13 | "Built with Claude, for Humanitarians AI." | PROCESS | Describes this video. |

## Changes since the last check (beats 3, 6, 7, 9)

`SCRIPT.md` was edited after the first check. Each change was re-checked against the sources.

| Beat | What changed | Result |
|---|---|---|
| 3 | "nobody's words get lost" is now "everyone ends up with the same document". | Resolved. Row 7 is SUPPORTED. |
| 6 | Now opens "Google's engineers explained that Docs solves this with…". | Resolved. Row 14 is SUPPORTED, and the claim is now about what the posts said, not how Docs works today. |
| 7 | "sends each person an acknowledgement" is now "sends an acknowledgement back to the person who made the change". | Resolved. Row 20 is SUPPORTED. |
| 9 | The permanent-ID and "merge in any order" sentences are replaced by one: each copy can be changed on its own, at the same time, without coordinating, and the copies still end up the same. | Resolved. Row 27 is SUPPORTED by Wikipedia; row 28 is removed. The Yjs file is no longer relied on. |

## Notes for the fact check: your list, answered

- **Beats 2, 8 and 10 (your own experience and test):** EXEMPT, rows 3 to 5, 22 to 25, 29 and 30.
- **Beat 8, "must keep track of who made each change":** your inference, not stated by Google. Row 23.
- **Beats 4 and 6, the a-b-c example:** matches how OT is described. Wikipedia's example is the same shape (insert at the start, delete the third character, delete shifted by one). Rows 9, 10, 11 and 17.
- **Beat 5, what each side keeps:** matches the blog. Only changes are sent, not the whole document. Row 13.
- **Beat 7, the Luiz and John example:** the quote in your notes is accurate; the blog continues "...where his client transformed it against his still pending {InsertText '!' @1} change". The revision log definition is "The complete history of all processed changes (called the revision log)". Rows 19 to 21.
- **Beat 3, beat 6 and beat 7 edits:** resolved, rows 7, 14 and 20.
- **Beats 6 and 7, the split into OT and the collaboration protocol:** the wording is in the blog's opening paragraph, quoted in row 18.
- **Beat 9, CRDT wording:** now follows Wikipedia only (independently, concurrently, without coordinating, converge). Rows 26 to 28. Your "I'm just starting to learn about" line is honest and stays.
- **Beat 10, framing:** row 30.
- **"Control Z" spoken, Ctrl+Z on screen:** done. The scenes and key chips show Ctrl+Z; the verdict page keeps "Control Z" so it matches the narration word for word.

## Visuals

- No Google logo, no Docs interface or screenshots, no Google colours used as branding. The windows are plain drawn rectangles.
- Every example (a-b-c, packets, the log, the ID tags) is an illustration. The a-b-c row and its numbers match the Wikipedia example; nothing else on screen is a data value.
- No dates on screen or in these files.
