# Momentum, One Remembered Step at a Time — script (final, as shot)

Channel claude-liam · Persona Liam (in for Bear) · Register Teardown · Voice Kokoro `am_onyx` (AI narration)
16:9 long cut: 3:00 (179.8s) · 9:16 cut: same length

Timestamps come from the measured audio and are approximate. This is what is spoken in the final render; on-screen props live in `beat_sheet.json`.

Opening line required by the weekly guide (not yet spoken in this video): "Hi, I am Rohan, and this video is about machine learning."

## 16:9 — long cut

### B00 · ask (0:00–0:15)
> Hi, this is Liam, in for Bear. The ask: why does adding momentum make gradient descent faster? Show me with real numbers. Momentum keeps a running memory of past slopes. The zigzags cancel, and the steady direction builds. A little more than halves the steps. Too much overshoots.

### B01 · overview (0:15–0:24)
> Momentum cancels the zigzag. It doesn't just add speed. It remembers where the slopes pointed, so the steps that disagree cancel, and the steps that agree add up.

### B02 · the valley (0:24–0:38)
> Here is a narrow valley. Start at four, one. Plain gradient descent steps against the slope. Across the valley the slope is steep, so it overshoots and bounces from side to side, while creeping along the floor. Forty-seven steps to get the loss under point oh one.

### B03 · the memory (0:38–0:52)
> Momentum keeps a memory. Call it v. Each step, v becomes beta times the old v, plus the new slope. Then move against v, not against the slope. Beta zero is plain descent. Beta point eight remembers roughly the last five slopes.

### B04 · same start (0:52–1:02)
> Same start, same step size, beta point five. The first steps still zigzag, but the sideways motion fades while the forward motion builds. Twenty steps, instead of forty-seven.

### B05 · why it works (1:02–1:15)
> Why does it work? Look at the numbers. Across the valley, the slope swings: twenty-five, minus nineteen, minus eight, eleven. The velocity swings less. Along the valley the slope keeps its sign, so the velocity grows, from four to over six.

### B06 · how much memory (1:15–1:29)
> How much memory is right? Count the steps to get the loss under point oh one. Beta zero, forty-seven. Point five, twenty. Point eight, twenty-nine. Point nine, fifty-three. Point nine five, ninety-nine. Point nine nine never gets there in two hundred steps.

### B07 · where it bites (1:29–1:42)
> Where it bites. Too much memory and the ball overshoots. With beta point nine, x swings to minus two point two at step eleven, before coming back. With point nine nine, it is still swinging at step two hundred, with a loss of one point one.

### BVDT · verdict (1:42–2:04)
> Let's recap with Claude. Momentum keeps a running memory of past slopes. Each step v becomes beta times the old v plus the new slope, and the move goes against v. Zigzags cancel and steady directions add up. With beta point five the valley takes twenty steps, plain descent takes forty-seven. More memory is not better: point nine takes fifty-three. And at point nine nine, it is still swinging after two hundred steps.

### BHTF · your turn (2:04–2:55)
> Your turn. Paste this into Claude: Write a short Python script, no ML libraries, that runs gradient descent with momentum on loss = 0.5 * (x squared + 25 y squared), starting at x = 4 and y = 1, with step size 0.07. Each step, set v = beta * v + gradient, then subtract step size times v. Try beta = 0, 0.5, 0.9 and 0.99, and print how many steps each needs to get the loss below 0.01. Before running it, predict which beta wins. Here's what to check. Beta zero should take forty-seven steps and beta point five twenty. Beta point nine should take fifty-three, and point nine nine should not finish in two hundred. And see whether Claude explains why more momentum is not always faster, rather than just printing the counts.

### BOUT · outro (2:55–3:00)
> Momentum, One Remembered Step at a Time. At Nik Bear Brown.
