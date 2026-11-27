# FACTCHECK — How AI Reads Words: Tokenization

Every on-screen and spoken claim, traced to its source. Medhavy paths are relative to `~/Desktop/medhavy/medhavi-hub`. Code outputs are copied verbatim from `code/*.out.txt`.

## B00 · ASK
- Source: bookend (no factual claim beyond the film summary)
- Narration: Hi, I am Shubham L. and this video is about how language models break text into tokens, using a tiny byte-pair encoding I ran myself. The voice you're hearing is Liam, an A I narrator, reading my script. It's the first step every language model takes, and almost nobody sees it.

## B01 · BLUF
- Source: bookend (no factual claim beyond the film summary)
- Narration: It's natural to think A I models read words. They read pieces: tokens, learned from how often letter combinations appear. That one fact explains spelling quirks, costs, and context limits.

## B02 · FRAMEWORK
- Source: standard BPE algorithm (Sennrich et al., 2016); my bpe.py
- Narration: The method most models use is called byte-pair encoding, and it's one rule repeated. Split every word into letters. Count which neighbouring pairs appear most often across the text. Merge the winner into a single new symbol. Then do it again, and again, until you have as many tokens as you want.

## B03 · WORKED_EXAMPLE
- Source: stem-ai-1-tokenization/code/bpe.py (run locally)
- Narration: Here's a version I ran on four words: low, lower, newest, widest. First merge: e and s, seen nine times. Then e s plus t. Then est at the end of a word. Only then l and o. After four merges, newest is n, e, w, and one token, est. The ending everyone shares became a single piece first.

## B04 · MECHANISM
- Source: stem-ai-1-tokenization/code/bpe.out.txt
- Narration: These are the counts behind each merge. Nine for each step of est, because newest appears six times and widest three. Seven for l and o, from low and lower. Nothing here knows grammar or meaning. Frequency alone decides what becomes a token. Common endings get cheap. Rare words get chopped into several pieces.

## B05 · FALSIFIABILITY
- Source: general consequence of subword tokenization
- Narration: And that explains things people find strange. Ask a model to count letters in a word and it can stumble, because it never saw the letters, only pieces. Prices and context limits are counted in tokens. And languages that were rarer in the training text get split into more pieces, so they cost more to process.

## B06 · VERDICT
- Source: bookend (no factual claim beyond the film summary)
- Narration: So: models read tokens, not words. Byte-pair encoding builds them by merging the most frequent pair, again and again. In my small run, est became a token before anything else. And once you see tokens, the quirks stop being mysterious.

## B07 · YOUR_TURN
- Source: bookend (no factual claim beyond the film summary)
- Narration: Your turn. Ask Claude for a byte-pair encoder you can run on a paragraph of your own writing, printing each merge and its count, then tokenizing three of your sentences. Look at which words split into the most pieces. Usually it's names and rare words. That's exactly where models struggle most.

## B08 · OUTRO
- Source: bookend (no factual claim beyond the film summary)
- Narration: That was How AI Reads Words: Tokenization. Shubham L., for Humanitarians A I. Thanks for watching.

