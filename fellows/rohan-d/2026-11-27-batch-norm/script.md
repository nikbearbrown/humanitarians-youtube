# Batch Normalization, One Rescale at a Time — script (final, as shot)

Channel claude-liam · Persona Liam (in for Bear) · Register Teardown · Voice Kokoro `am_onyx` (AI narration)
16:9 long cut: 3:00 (179.6s) · 9:16 cut: same length

Timestamps come from the measured audio and are approximate. This is what is spoken in the final render; on-screen props live in `beat_sheet.json`.

Opening line required by the weekly guide (not yet spoken in this video): "Hi, I am Rohan, and this video is about machine learning."

## 16:9 — long cut

### B00 · ask (0:00–0:14)
> Hi, this is Liam, in for Bear. The ask: why does normalizing the numbers inside a network make it train faster? Show me with real numbers. Subtract the batch mean, divide by the spread. Every feature lands on one scale. The loss valley stops being a ravine.

### B01 · overview (0:14–0:26)
> Normalization reshapes the landscape. It isn't just tidying. When features live on wildly different scales, the loss is a long narrow ravine. Put them on one scale and the ravine becomes a bowl.

### B02 · two scales (0:26–0:38)
> Two features, one batch of four. Feature A reads two, four, six, eight. Feature B reads two hundred, four hundred, six hundred, eight hundred. Same shape, a hundred times the scale. Whatever the network does next, B will shout over A.

### B03 · normalize A (0:38–0:53)
> Normalize. Take A. The mean is five. The spread, the standard deviation, is two point two four. Subtract the mean: minus three, minus one, one, three. Divide by the spread: minus one point three four, minus point four five, point four five, one point three four.

### B04 · normalize B (0:53–1:03)
> Now B. The mean is five hundred. The spread, two hundred twenty-four. Subtract, divide, and the same four numbers come out. Feature A and feature B now speak at the same volume.

### B05 · the valley (1:03–1:22)
> Why does that speed up training? The loss is a valley, like the one in the momentum film. With raw features, its steepest and flattest directions differ by a factor of three million. With normalized features, one point four. Normalized, gradient descent lands within a thousandth of the best loss in four steps. The raw run hasn't arrived after a hundred thousand.

### B06 · gamma and beta (1:22–1:40)
> One more piece. Forcing every feature to mean zero and spread one might throw away something useful. So batch norm adds two learnable numbers, gamma and beta. Scale by gamma, shift by beta. With gamma two and beta one, those four numbers become minus one point six eight, point one one, one point eight nine, three point six eight.

### B07 · where it bites (1:40–1:53)
> Where it bites. The mean and spread come from the batch. With a batch of one, the batch mean wobbles with a standard deviation of one. At thirty-two, point one eight. And a batch of one has no spread at all: subtract its own mean, and every output is zero.

### BVDT · verdict (1:53–2:15)
> Let's recap with Claude. Normalize each feature: subtract the batch mean, divide by the spread. A and B, a hundred times apart, become the same four numbers. The raw valley has a condition number of three million, the normalized one, one point four. Normalized, gradient descent is near the best loss in four steps. Gamma and beta let the network undo the rescale. And a batch of one has no spread: every output is zero.

### BHTF · your turn (2:15–2:54)
> Your turn. Paste this into Claude: Write a short Python script, numpy only, that normalizes the batches [2, 4, 6, 8] and [200, 400, 600, 800] by subtracting the mean and dividing by the standard deviation, and prints both. Then apply gamma = 2 and beta = 1 to the first result. Finally, normalize a batch containing one number and print it. Predict each output before you run it. Here's what to check. Both batches should print minus one point three four, minus point four five, point four five, one point three four. Gamma two and beta one should give minus one point six eight, point one one, one point eight nine, three point six eight. And the batch of one should print zero. See whether Claude explains why.

### BOUT · outro (2:54–3:00)
> Batch Normalization, One Rescale at a Time. At Nik Bear Brown.
