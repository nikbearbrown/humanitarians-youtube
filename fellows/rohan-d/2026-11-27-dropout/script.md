# Dropout, One Silenced Unit at a Time — script (final, as shot)

Channel claude-liam · Persona Liam (in for Bear) · Register Teardown · Voice Kokoro `am_onyx` (AI narration)
16:9 long cut: 2:46 (166.3s) · 9:16 cut: same length

Timestamps come from the measured audio and are approximate. This is what is spoken in the final render; on-screen props live in `beat_sheet.json`.

Opening line required by the weekly guide (not yet spoken in this video): "Hi, I am Rohan, and this video is about machine learning."

## 16:9 — long cut

### B00 · ask (0:00–0:16)
> Hi, this is Liam, in for Bear. The ask: why does randomly switching off neurons during training help, and why scale the ones that survive? Show me with real numbers. Silence each unit with some probability. Scale the survivors up. The average output stays put, and no unit can lean on a neighbor.

### B01 · overview (0:16–0:26)
> Dropout trains many networks. Each random mask picks a thinned copy that shares the same weights. Training on all of them at once is what keeps any one unit from being relied on.

### B02 · one mask (0:26–0:38)
> Eight units, with activations one to eight. They add up to thirty-six. Now flip a coin for each unit. Heads, keep it. Tails, silence it. This mask keeps units one, five, six and seven. Their sum is nineteen.

### B03 · scale up (0:38–0:49)
> Silencing half the units cuts the sum in half. So scale the survivors up by two. Nineteen becomes thirty-eight. One mask, one answer, near the thirty-six we would get with every unit.

### B04 · many masks (0:49–1:01)
> Draw five more masks. The outputs jump around: eighteen, forty, forty-four, twenty-two, twenty-eight. Any single mask is noisy. Now draw ten thousand. The average is thirty-five point nine eight. The noise averages away.

### B05 · why scale (1:01–1:12)
> Why scale? Without it, the average output is eighteen, half the truth. With the factor of two, it's thirty-six, the same as with no dropout. Scaling is what keeps the expected output unchanged.

### B06 · 256 networks (1:12–1:28)
> Count the masks. Eight units, two choices each: two to the eighth, two hundred fifty-six thinned networks, all sharing one set of weights. For a plain sum like this one, averaging all two hundred fifty-six gives exactly thirty-six. At test time, you skip the masks and use the full network. That is the average.

### B07 · where it bites (1:28–1:43)
> Where it bites. Dropout adds noise. At drop probability point one, the output wobbles by about five. At point five, fourteen. At point nine, forty-three, more than the answer itself. And forget to switch it off at test time, and the same input gives a different answer every run.

### BVDT · verdict (1:43–2:05)
> Let's recap with Claude. Dropout silences each unit with probability p during training. Survivors are scaled by one over one minus p, so the average output stays at thirty-six. One mask gives thirty-eight, and ten thousand average thirty-five point nine eight. Eight units give two hundred fifty-six thinned networks that share one set of weights. Noise grows with p. And at test time, dropout is switched off.

### BHTF · your turn (2:05–2:41)
> Your turn. Paste this into Claude: Write a short Python script, numpy only, that applies dropout to the activations 1 through 8: keep each unit with probability 1 minus p, scale the survivors by 1 over 1 minus p, then sum. Run it on 10,000 random masks and print the mean and the standard deviation of the sum, for p = 0.1, 0.5 and 0.9. Predict the means before you run it. Here's what to check. The mean should be about thirty-six for every p. The standard deviation should be about four point eight, fourteen point three, and forty-three. And see whether Claude explains why the mean does not move while the noise grows.

### BOUT · outro (2:41–2:46)
> Dropout, One Silenced Unit at a Time. At Nik Bear Brown.
