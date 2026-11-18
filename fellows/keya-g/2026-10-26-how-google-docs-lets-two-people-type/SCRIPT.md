# How Google Docs Lets Two People Type in the Same Sentence — Script

**Fellow:** Keya G. · **Week 3** · **Voice:** Kokoro `af_bella` · **Pronounce:** Keya = kˈeɪjɛə ("Kay-yeah")

Story plan, topic, research and decisions: Keya. Example script drafted with Claude from Keya's story plan, research notes and her own test; Keya approved and edited it.
Visuals: simple illustrative graphics only (two browser windows, the letters a b c, operations moving to a server, a revision log, cursors, characters with ID tags). No Google logo, Docs interface screenshots or other branding.

## 1. Intro
Hi, I am Keya, and this video is about how Google Docs lets two people type in the same sentence. The voice you're hearing is an AI voice reading my script.

## 2. Hook
I've worked with shared documents. Sometimes two people type in the same line, and the text overlaps for a moment. So I wondered: if I press Control Z, will I undo my teammate's work too? I tested it in two windows. It only undid mine. How does Google Docs keep track?
`[Keya's experience and test]`

## 3. Overview
On screen, typed then corrected: "The last person to type wins." → "Every keystroke gets merged."

Google Docs doesn't let the last person win. It merges every change, so everyone ends up with the same document. Let's see how, step by step.

## 4. The problem
Here's why this is hard. Say the document says a, b, c. At the same moment, I add an x at the start, and my teammate deletes the third letter, c. My x pushes everything one place to the right, so the third letter is now b. If my teammate's change is applied exactly as it was sent, the wrong letter gets deleted.
`[Illustrative example; Wikipedia: Operational transformation]`

## 5. Two copies
When you open a Google Doc, it runs in two places: in your browser, and on Google's server. As you type, your browser doesn't send the whole document. It sends only your changes to the server, and receives everyone else's changes back.
`[Google Drive blog, 2010]`

## 6. Operational transformation
Google's engineers explained that Docs solves this with a technique called operational transformation. Each edit is an operation, like "insert x at the start" or "delete the third letter." When two operations clash, one is transformed to fit the other. My teammate's delete is shifted from the third letter to the fourth, so the c is deleted, just as they meant.
`[Google Drive blog, 2010; Wikipedia: Operational transformation]`

## 7. The collaboration protocol
But transforming isn't enough. Every copy also needs the same changes, in the same order. That's the second part, the collaboration protocol. The server processes changes in the order they arrive. It sends an acknowledgement back to the person who made the change, passes the change on to everyone else, and keeps every change in a revision log: the complete history of the document.
`[Google Drive blog, 2010]`

## 8. Cursors and delay
In my test, Control Z only undid my own typing, so the document must keep track of who made each change. I can also see where my teammate's cursor is. And sometimes their text shows up a moment late, because each change has to travel to the server and back.
`[Keya's experience and test]`

## 9. Another way: CRDTs
There's another approach I'm just starting to learn about, called CRDTs, short for conflict-free replicated data types. Each copy can be changed on its own, at the same time, without coordinating with the others, and the copies still end up the same.
`[Wikipedia: Conflict-free replicated data type]`

## 10. Where it gets messy
It isn't perfect. In my experience, on a slow connection, text can appear late, or overlap for a moment before it settles. And if two people rewrite the same sentence in different ways, the system can merge both edits, but it can't decide which wording the team actually wanted.
`[Keya's experience]`

## 11. Verdict
So how does Google Docs let two people type in the same sentence? It doesn't avoid conflicts. It fixes them so fast that we almost never notice. Behind every keystroke, changes are shifted, ordered and shared. And when I pressed Control Z, only my words disappeared.

## 12. Your turn
Your turn. Paste this into Claude: Explain operational transformation using the word cat, when one person inserts a letter and another deletes one at the same time. And next time you edit a shared document, ask: whose change just moved my text?

Prompt shown on screen: "Explain operational transformation using the word 'cat', when one person inserts a letter and another deletes one at the same time."

## 13. Outro
How Google Docs Lets Two People Type in the Same Sentence. Built with Claude, for Humanitarians AI.

## Notes for the fact check
- Beats 2, 8 and 10 are Keya's own experience and test (Ctrl+Z in two windows undid only her own changes).
- Beat 8: "the document must keep track of who made each change" is Keya's inference from her test, not a claim about Google's internals.
- Beat 4 and 6: the a-b-c example is illustrative; check that it matches how operational transformation is described (positions shift, the clashing operation is transformed).
- Beat 5: Keya found the blog's list of what each client and the server keep track of: clients hold local changes not yet sent, and changes sent but not yet acknowledged; the server holds received changes, the revision log and the current document. So only changes are sent, not the whole document.
- Beat 7: the blog's example says the server "got Luiz's change before John's so it processed that change first. An acknowledgement of the change was sent to Luiz. The change itself was sent to John, where his client transformed it against his still pending" change. The revision log is "the complete history of all processed changes."
- Beat 6 and 7: Keya's notes say Google's blog splits the problem into operational transformation and a collaboration protocol, with a revision log; check the wording.
- Beat 9: CRDT wording follows Wikipedia only: replicas updated "independently, concurrently and without coordinating with other replicas", and they converge. The earlier "permanent ID" and "merge in any order" lines were removed because the cited source doesn't state them. Keya flags she hasn't studied CRDTs deeply, and the narration says so.
- Beat 3: "everyone ends up with the same document" replaces "nobody's words get lost", which the sources don't state.
- Beat 6: attributed to Google's engineers, because the sources are 2010 blog posts and don't say how Docs works today.
- Beat 7: the acknowledgement goes only to the person who made the change, as in the blog's Luiz and John example.
- Beat 10: "can merge both edits but can't decide which wording was wanted" is framing, not a measured claim.
- "Control Z" is spoken; the on-screen text can show Ctrl+Z.

## Sources
- Google Drive blog, "What's different about the new Google Docs: Making collaboration fast" — https://drive.googleblog.com/2010/09/whats-different-about-new-google-docs.html
- Google Drive blog, "What's different about the new Google Docs: Conflict resolution" — https://drive.googleblog.com/2010/09/whats-different-about-new-google-docs_22.html
- Wikipedia, "Operational transformation" — https://en.wikipedia.org/wiki/Operational_transformation
- Wikipedia, "Conflict-free replicated data type" — https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type
- Keya's own test: one Google Doc open in two windows, typing in both, then Ctrl+Z in one
