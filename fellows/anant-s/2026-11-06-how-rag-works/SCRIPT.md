# SCRIPT — How RAG Works

Narration as built, from `beat_sheet.json`. On 2026-11-24 the film was converted from the show-tell format to ai-explainer, and Anant approved the new narration. Durations are the measured audio, lead silence included. The pre-conversion script is in `_superseded/format-show-tell/docs/SCRIPT.md`.

## B00 · ASK · ClaudeComposerAsk

*33 words · 9.5 s*

Hello, this is Liam, in for Bear. The ask: how can a chatbot answer questions about my own documents, when it has never read them? Show me how RAG works, step by step.

*On screen:* composer card fades in on cream → greeting 'Hello, Liam' types above the composer → the ask types in → runningText 'working through the math…' appears → three result lines cascade in

## B01 · BLUF · BrutalistHesitantWriter

*33 words · 12.1 s*

With RAG, a chatbot answers from what it just looked up. It searches your documents for the closest pieces, pastes them into the prompt, and writes from them. RAG stands for retrieval-augmented generation.

*On screen:* cream page holds; caret blinks → types 'With RAG, a chatbot answers / from what it memorized.' → 'from what it memorized' turns terracotta, hesitates, backspaces → types 'from what it just looked up' → final lines settle

## B10 · SHOW-TELL · B10_Handbook

*33 words · 9.1 s*

Start with a box of your own documents. Here, it's a small shop's handbook. The model never saw these pages in training, so on its own, it can only guess what they say.

*On screen:* box drops in, shadow lands → 'handbook' label → model block slides in at right; dashed line stops short of the box

## B11 · SHOW-TELL · B11_ThreePages

*31 words · 10.2 s*

Open the box, and there are three documents: returns, shipping, and warranty. RAG doesn't teach the model these pages. It hands the model the right page, at the moment it answers.

*On screen:* tape splits, flaps lift → page 1 rises: 'returns' → page 2: 'shipping' → page 3: 'warranty' → one page lifts slightly toward the right edge (the page handed over)

## B12 · SHOW-TELL · B12_Chunks

*33 words · 10.9 s*

Step one: cut every document into chunks, short pieces the system can fetch one at a time. Each of these documents has two sentences, so each becomes two chunks. Six chunks in all.

*On screen:* cut line sweeps page 1, it splits → pages 2 and 3 split → six slips line up → '6 chunks' label

## B13 · SHOW-TELL · B13_Scanner

*44 words · 13.9 s*

Step two: turn each chunk into an embedding, a list of numbers. Our toy version counts words, with one slot for each of the handbook's twenty-nine key words. Real systems use a trained model, so chunks that mean the same thing land close together.

*On screen:* conveyor + scanner → first slip scanned, bar strip appears → the rest follow → '29 numbers' label → two strips with similar bars slide together

## B14 · SHOW-TELL · B14_Drawers

*31 words · 10.1 s*

Step three: file every embedding in a vector store, a database built to find the closest lists of numbers, fast. This happens once, ahead of time, before anyone asks a thing.

*On screen:* cabinet appears → strips file into drawers one by one → drawer lights on; 'vector store'

## B15 · SHOW-TELL · B15_Question

*34 words · 9.3 s*

Now a question arrives. How long do I have to return a laptop? It goes through the same scanner, so it becomes a list of numbers too, in the same space as the chunks.

*On screen:* question slip enters → scanner sweeps it → its bar strip appears; 'question'

## B16 · SHOW-TELL · B16_Ranking

*47 words · 15.3 s*

Step four: the store compares the question's numbers with every chunk's, and returns the closest. The returns chunk scores zero point five eight. The warranty chunk shares only the word laptop, so it scores zero point two five. The other four share no words, and score zero.

*On screen:* question strip + 'question'; three chunk strips drop in → dashed guides from the question's slots (compares) → returns bar grows: 'within 30 days' 0.58 → warranty bar: 'one year warranty' 0.25 → stub bar: 'receipt and charger' 0.00 → check on the top row

## B17 · SHOW-TELL · B17_Prompt

*39 words · 10.9 s*

Step five: paste the top two chunks into the prompt, above the question, with one instruction: answer only from these notes, and say so if they don't cover it. Now the facts sit right in front of the model.

*On screen:* two drawers open → slips land on the prompt sheet → question slip lands below them → instruction scribble draws; 'prompt'

## B18 · SHOW-TELL · B18_Answer

*36 words · 10.3 s*

The model reads the prompt and writes a grounded answer: thirty days, from the returns chunk. Because you know which chunks went in, the answer can point back to its source, and you can check it.

*On screen:* sheet into model → answer card out: '30 days' → thread back to the returns slip → check lands

## B19 · SHOW-TELL · ShowTellCard

*46 words · 14.4 s*

Here's where it fails. Same question, but someone has added an old FAQ page that says fourteen days. It repeats the question almost word for word, so it now scores zero point six eight, and the right chunk drops to second, at zero point three eight.

*On screen:* tabs card, shot on twos

## B20 · SHOW-TELL · B20_WrongAnswer

*34 words · 11.6 s*

Now the prompt leads with the old chunk. A model told to trust its notes can answer fourteen days, fluently and confidently. Nothing in the writing looks wrong. The mistake happened earlier, at retrieval.

*On screen:* old page drops in → its slip on top of the prompt → answer card: '14 days' → ring circles the drawer: 'retrieval'

## B21 · SHOW-TELL · B21_Fix

*34 words · 10.3 s*

The fix is in the store, not the model. Take the old page out, and the returns chunk is back on top, at zero point five eight. Nobody retrained anything. You changed the pages.

*On screen:* old slip lifted out → returns slip back on top → answer card: '30 days', check

## B22 · SHOW-TELL · B22_Scale

*38 words · 13.4 s*

That's the idea behind RAG. In the 2020 paper that named it, Lewis and colleagues gave a model twenty-one million Wikipedia passages to search, and updated what the model knew by swapping in a newer copy of Wikipedia.

*On screen:* cabinets multiply → counter climbs to 21M → caption 'per Lewis et al. 2020' → old cabinet out, newer one in

## BVDT · VERDICT · ClaudeVerdictArtifact

*69 words · 18.6 s*

Let's recap with Claude. Cut your documents into chunks, and turn each chunk into an embedding, a list of numbers. File them in a vector store. When a question arrives, embed it too, and fetch the closest chunks. Paste them into the prompt, and the model answers from them. And if the store holds an old page, the answer goes old with it. Fix the store, not the model.

## BHTF · YOUR TURN · ClaudeComposerAsk

*85 words · 21.9 s*

Your turn. Paste this into Claude: Here are three short passages from my own notes: [paste them]. And here is my question: [your question]. Before you answer, rank the passages by how relevant each one is to the question, and say why. Then answer using only the top passage, and quote the sentence you used. Then check two things yourself. Does the quoted sentence really say the answer? And would a newer passage say something different? If it would, the retrieval picked wrong.

*On screen:* Composer opens — 'Your turn.' → the prompt types in full → two check lines land

## BOUT · OUTRO · ClaudeTitleOutro

*7 words · 3.9 s*

How RAG Works. At Nik Bear Brown.

*On screen:* title restates; handle; mascot

**Total: 707 words · 215.6 s (3:35).**
