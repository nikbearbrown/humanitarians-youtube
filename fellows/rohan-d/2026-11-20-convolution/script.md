# Convolution, One Window at a Time — script (final, as shot)

Channel claude-liam · Persona Liam (in for Bear) · Register Teardown · Voice Kokoro `am_onyx` (AI narration)
16:9 long cut: 2:43 (163.0s) · 9:16 cut: same length

Timestamps come from the measured audio and are approximate. This is what is spoken in the final render; on-screen props live in `beat_sheet.json`.

Opening line required by the weekly guide (not yet spoken in this video): "Hi, I am Rohan, and this video is about machine learning."

## 16:9 — long cut

### B00 · ask (0:00–0:16)
> Hi, this is Liam, in for Bear. The ask: how does a convolution find an edge in an image, and why share one small kernel across the whole picture? Show me with real numbers. A kernel is a tiny grid of weights. Slide it over the image, multiply and add. Nine weights find the same pattern everywhere.

### B01 · overview (0:16–0:26)
> A convolution slides a small window. It never reads the whole image at once. It looks at one small patch, writes down a single number, and moves over. Then it does that again, everywhere.

### B02 · the image (0:26–0:37)
> Here is a six by six image. Dark on the left, bright on the right. The edge sits between the third column and the fourth. How would a computer find it? Give it a small grid of weights, a kernel, and slide it across.

### B03 · one window (0:37–0:49)
> The kernel is three by three. Left column, minus one. Middle, zero. Right, plus one. Place it on the top left. Multiply each weight by the pixel beneath, and add. The window covers a flat dark patch. The sum is zero.

### B04 · slide it (0:49–1:03)
> Slide it one step right. Now the right column lands on bright pixels. Three nines, twenty-seven. One more step, twenty-seven again. And one more: bright on both sides, nine minus nine, so zero. Zero, twenty-seven, twenty-seven, zero.

### B05 · the map (1:03–1:13)
> Do that for every row and you get a four by four map. Zero, twenty-seven, twenty-seven, zero, in every row. The big numbers sit exactly on the edge. The kernel found it.

### B06 · shared weights (1:13–1:29)
> Why share one kernel? Count the weights. To make this four by four map, a layer that connects every input to every output needs thirty-six times sixteen: five hundred seventy-six weights. The convolution uses nine. And move the edge one column left, and the same nine weights find it one place over.

### B07 · where it bites (1:29–1:40)
> Where it bites. The map is smaller than the image. Six becomes four, four becomes two, and a third three by three kernel no longer fits. Pad the border with zeros and the size stays six.

### BVDT · verdict (1:40–1:59)
> Let's recap with Claude. A kernel is a small grid of weights slid across the image. At each spot, multiply and add. The edge kernel gives zero, twenty-seven, twenty-seven, zero across the edge. One kernel of nine weights replaces five hundred seventy-six, and finds the pattern wherever it sits. But each layer shrinks the map by two, so padding keeps the size.

### BHTF · your turn (1:59–2:38)
> Your turn. Paste this into Claude: Write a short Python script, no ML libraries, that slides the 3 by 3 kernel with columns of minus 1, 0 and 1 over a 6 by 6 image whose rows are 0, 0, 0, 9, 9, 9, and prints the 4 by 4 output. Predict the output before you run it. Then move the edge one column left and print the output again. Finally, pad the image with a border of zeros and print the output size. Here's what to check. Every row of the first output should read zero, twenty-seven, twenty-seven, zero. With the edge moved left, it should read twenty-seven, zero, zero, zero. With padding, the output should be six by six. And see whether Claude explains why the edge shows up as two columns of twenty-seven, not one.

### BOUT · outro (2:38–2:43)
> Convolution, One Window at a Time. At Nik Bear Brown.
