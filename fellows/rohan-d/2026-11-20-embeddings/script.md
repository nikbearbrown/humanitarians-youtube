# Embeddings, One Angle at a Time — script (final, as shot)

Channel claude-liam · Persona Liam (in for Bear) · Register Teardown · Voice Kokoro `am_onyx` (AI narration)
16:9 long cut: 2:44 (164.4s) · 9:16 cut: same length

Timestamps come from the measured audio and are approximate. This is what is spoken in the final render; on-screen props live in `beat_sheet.json`.

Opening line required by the weekly guide (not yet spoken in this video): "Hi, I am Rohan, and this video is about machine learning."

## 16:9 — long cut

### B00 · ask (0:00–0:13)
> Hi, this is Liam, in for Bear. The ask: how does a model tell that two words mean similar things? Show me with real numbers. Turn each word into a list of numbers, a vector, then compare the angle between them. Length can fool you. Direction doesn't.

### B01 · overview (0:13–0:27)
> Similar words have similar directions. Not similar sizes, and not similar spellings. Two vectors that point the same way mean the same kind of thing, however long they are. Then the model can compare any two words by the angle between them.

### B02 · words as arrows (0:27–0:39)
> Give every word a list of numbers. Here is a toy plane with two numbers per word. Furry along the bottom, vehicle up the side. Cat is four, one. Dog is three, two. Car is one, four. Similar words land near each other.

### B03 · distance fails (0:39–0:54)
> The obvious way to compare is distance. Cat to car, four point two. Now say a document uses cat three times as often. Cat times three is twelve, three. Its distance to cat is eight point two, farther than the car. Distance says a cat is less like a cat than a car is.

### B04 · direction (0:54–1:06)
> Compare direction instead. Cat points up at fourteen degrees, dog at thirty-four, car at seventy-six. Cat to dog, twenty degrees. Cat to car, sixty-two. And cat times three points exactly where cat points. Zero degrees.

### B05 · cosine (1:06–1:20)
> The score for that angle is its cosine. Dot product, over the two lengths. Cat dot dog is fourteen. The lengths are four point one two and three point six one. Fourteen over fourteen point nine is point nine four. Same direction scores one.

### B06 · every pair (1:20–1:32)
> Score every pair. Cat and dog, point nine four. Dog and car, point seven four. Cat and car, point four seven. And cat against three cats, one point oh oh. Direction decides. Length doesn't.

### B07 · where it bites (1:32–1:44)
> Where it bites. Cosine says near, not same. Cat and dog score point nine four, but they aren't interchangeable. And a vector of zeros has no direction at all. Its cosine is zero divided by zero. Undefined.

### BVDT · verdict (1:44–2:05)
> Let's recap with Claude. An embedding turns a word into a list of numbers. Distance is fooled by length: cat to three cats is eight point two, farther than cat to car. Cosine compares direction, dot product over the two lengths. Cat and dog score point nine four, cat and car point four seven, cat and three cats one. Near is not the same. And a zero vector has no direction, so its cosine is undefined.

### BHTF · your turn (2:05–2:40)
> Your turn. Paste this into Claude: Write a short Python script, no ML libraries, that computes the distance and the cosine between cat = (4, 1) and each of dog = (3, 2), car = (1, 4) and cat times 3 = (12, 3). Before running it, predict which of the three each measure ranks closest to cat. Here's what to check. Distance should rank dog, then car, then cat times three: one point four one, four point two four, eight point two five. Cosine should rank cat times three, then dog, then car: one, point nine four, point four seven. And see whether Claude explains why the two measures disagree about cat times three.

### BOUT · outro (2:40–2:44)
> Embeddings, One Angle at a Time. At Nik Bear Brown.
