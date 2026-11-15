# How a QR Code Works (script draft for approval, v2: fact-checked)

**Fellow:** Tanishaa · **Channel:** @HumanitariansAI · **Narrator:** Bella (Kokoro `af_bella`, an AI voice; disclosed on screen and aloud)
**Target length:** ~2½ minutes (about 430 spoken words), inside the 2–3 minute range · **Exports:** 16:9 at 3840×2160, plus a native 9:16 at 2160×3840
**Audience:** students who are new to the topic.
**Hook:** you can tear a chunk out of a QR code and it still works. The missing part is rebuilt from the rest.
**Sync rule:** on-screen text never runs on its own clock. Short lines can be shown word for word; when Bella says a lot, the screen shows only the key points, each appearing exactly as she says it.

Each beat lists what's **on screen** first, then what Bella **says**.

---

### B00 · Cold open: the ask (~13 s)
**On screen:** The Claude app opens with the greeting "Hi, Tanishaa". The composer types: *"How does my phone read a QR code?"* The first lines of the answer appear. A small label reads "AI narration: Bella".
**Says:** "Hi, I am Tanishaa, and this video is about how a QR code works. The voice you're hearing is Bella, an AI narrator reading a script Claude drafted and I approved."

### B01 · The hook (~12 s)
**On screen:** A real QR code (our channel link). A sticker covers its middle, and a phone still reads it. Key points on their words: **cover part of it** · **still reads** (accent) · **rebuilt from the rest**.
**Says:** "You can cover part of a QR code, and your phone still reads it. The missing piece isn't guessed. It's rebuilt from the rest of the code."

### B02 · It's just a grid of bits (~16 s)
**On screen:** The code zooms in until the squares separate into a grid: **29 × 29 squares**. One square flips to show **dark = 1 · light = 0**. Label: **Quick Response · 1994 · built to track car parts**.
**Says:** "A QR code is a grid of tiny squares. Each one is a single bit: dark means one, light means zero. It was invented in Japan in 1994, to track car parts on a factory line, which is why it's called Quick Response."

### B03 · How the camera finds it (~18 s)
**On screen:** The three big corner squares light up: **finder patterns**. A camera frame tilts and the code straightens itself. Then the dotted lines between the finders glow: **timing patterns → the grid size**.
**Says:** "First your camera has to find it. Those three big squares in the corners are finder patterns. They tell the phone where the code is, and which way up it's turned, even at an angle. The dotted lines between them count out the grid, so the phone knows where every square sits."

### B04 · Reading the data (~18 s)
**On screen:** A path snakes up and down from the bottom-right corner, two columns at a time, collecting bits into bytes. The bytes turn into letters: **h t t p s : / / …**. A small tag: **mask: a pattern flipped on top so no big blank patches form**.
**Says:** "Then it reads the data, starting at the bottom-right corner and snaking up and down, two columns at a time. Every eight bits make a byte, and the bytes spell out the link. A mask pattern is flipped over the top, so there are no big blank patches to confuse the camera."

### B05 · The trick: spare data (~20 s)
**On screen:** The squares split into two colors: **message** and **extra recovery data**. Four labels appear on their words: **L 7%** · **M 15%** · **Q 25%** · **H 30%**. Label: **Reed–Solomon codes (also used on CDs)**.
**Says:** "Here's the trick. A QR code carries more than your message. It also carries extra recovery data, worked out with a bit of math called Reed–Solomon, the same idea that lets a scratched CD keep playing. There are four levels. The lowest can recover about seven percent of the code. The highest, about thirty."

### B06 · Worked example, run for real (~20 s)
**On screen:** Real output from `demo/qr_demo.py`: the same link encoded at level L and at level H, side by side. A white sticker grows over the middle of each. **Level L: fails once 7 × 7 squares are covered.** **Level H: still reads with 17 × 17 covered, about a fifth of the code.**
**Says:** "Here it is for real. I made the same link at the lowest level and the highest, and covered the middle of each with a growing sticker. The low one broke once a seven by seven patch was gone. The high one still read with about a fifth of the whole code covered."

### B07 · Why logos fit (~12 s)
**On screen:** The level-H code with a small round logo in the middle. Label: **the logo is "damage" the code repairs**. Then: **bigger code, more squares**.
**Says:** "That's why some QR codes have a logo in the middle. The logo is just damage, and the recovery data fills it in. The cost is a bigger code with more squares."

### B08 · When to trust it (~22 s)
**On screen:** Two columns sort themselves as each item is spoken.
**It's good at:** smudges, scratches, a logo · reading at an angle.
**It can't tell you:** whether the link is safe · a sticker swapped over the real code.
At the end, a third card drops in: **"Check the link before you open it."**
**Says:** "So when can you trust it? A QR code is great at surviving smudges, scratches, and logos, and reading at an angle. But it has no idea whether the link inside is safe, and a scammer can just stick a new code over the real one. So always check the link your phone shows you before you open it."

### B09 · Verdict (~10 s)
**On screen:** A Claude-style card titled "How a QR Code Works" with three key findings, each on its words:
1. A QR code is a grid of bits.
2. Corner squares find it; spare data repairs it.
3. It checks the code, not the link.
**Says:** "Three things to keep. A QR code is a grid of bits. The corner squares find it, and spare data repairs it. And it checks the code, not the link."

### B10 · Your turn (~18 s)
**On screen:** The Claude composer, greeting "Your turn.", with this prompt typed in:
> *"Act as my tutor. Give me a short message as bits, add one extra parity bit, then flip a bit and let me find the error. Then show me how QR codes go further and fix errors, not just find them."*

**Says:** "Your turn. Ask Claude to be your tutor: send a message with one spare bit, flip a bit, and catch the error yourself. That's the first step toward how a QR code repairs itself."

### B11 · Outro (~4 s)
**On screen:** The title "How QR Codes Work." in serif with a terracotta period, and @HumanitariansAI below it.
**Says:** "How a QR code works. At Humanitarians AI."

---

## Fact-check notes (to verify before recording)
- **Real (from `demo/qr_demo.py` → `demo/qr_output.json`, segno 1.6.6 + OpenCV 5.0.0 reader):** the channel link (40 bytes) is version 3 = 29 × 29 at levels L and M, 33 × 33 at Q, 37 × 37 at H. Covering a centred square in white: L reads up to 6 × 6 and fails at 7 × 7 (4.3% of the area); H reads up to 17 × 17 (21.1% of the area) and fails at 18 × 18. The area share is below 30% because the percentage refers to codewords, and a covered block cuts across many of them, so the screen says "about a fifth of the code", not 30%.
- **To confirm from sources (Denso Wave, ISO/IEC 18004):** invented 1994 at Denso Wave (Masahiro Hara's team) for tracking auto parts; "QR" = Quick Response; recovery levels about 7 / 15 / 25 / 30%; Reed–Solomon error correction; three finder patterns; timing patterns; eight mask patterns; data placed in two-module columns starting bottom-right; Reed–Solomon used on CDs; QR phishing via stickers over real codes (FTC consumer alert).
- **B04** simplifies the format/version info and the interleaving of blocks; it says "starting at the bottom-right corner", which is how placement begins.
