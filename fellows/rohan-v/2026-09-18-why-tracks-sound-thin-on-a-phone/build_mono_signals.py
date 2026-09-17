import numpy as np, wave, struct
SR, DUR = 48000, 20.0
t = np.arange(int(SR*DUR)) / SR
bass = 0.30*np.sin(2*np.pi*110*t)     # centred
mid  = 0.22*np.sin(2*np.pi*440*t)     # centred
air  = 0.20*np.sin(2*np.pi*3000*t)    # "wide" layer, inverted on the right
L = bass + mid + air
R = bass + mid - air
def w16(path, chans):
    n = len(chans[0])
    data = np.empty(n*len(chans), dtype=np.int16)
    for i, c in enumerate(chans):
        data[i::len(chans)] = np.clip(c, -1, 1) * 32767
    with wave.open(path, "wb") as f:
        f.setnchannels(len(chans)); f.setsampwidth(2); f.setframerate(SR)
        f.writeframes(data.tobytes())
w16("stereo.wav", [L, R])
w16("mono.wav",   [(L+R)/2])
# what each side sounds like alone, for reference
w16("left.wav",   [L])
print("built stereo.wav mono.wav left.wav")

# Real-world case: a "stereo widener" that just delays one side (Haas).
# Summed to mono this comb-filters — some frequencies survive, some vanish.
d_ms = 0.6
d = int(SR * d_ms / 1000)
noise = np.random.default_rng(7).normal(0, 0.12, len(t))
wL = noise
wR = np.concatenate([np.zeros(d), noise[:-d]])
w16("wide_left.wav", [wL])
w16("wide_mono.wav", [(wL + wR) / 2])
print(f"built widener case, delay {d_ms} ms ({d} samples)")
