# How GPS Knows Where You Are (script draft for approval, v1)

**Fellow:** Tanishaa · **Channel:** @HumanitariansAI · **Narrator:** Bella (Kokoro `af_bella`, an AI voice; disclosed on screen and aloud)
**Target length:** ~2½ minutes (about 440 spoken words), inside the 2–3 minute range · **Exports:** 16:9 at 3840×2160, plus a native 9:16 at 2160×3840
**Audience:** students who are new to the topic.
**Hook:** your phone never talks to the satellites. It only listens, and it finds you with a stopwatch.
**Sync rule (Tanishaa's feedback):** on-screen text never runs on its own clock. Short lines can be shown word for word; when Bella says a lot, the screen shows only the key points, each appearing exactly as she says it, so nothing lags or distracts.

Each beat lists what's **on screen** first, then what Bella **says**.

---

### B00 · Cold open: the ask (~13 s)
**On screen:** The Claude app opens with the greeting "Hi, Tanishaa". The composer types: *"How does GPS know where I am?"* The first lines of the answer appear. A small label reads "AI narration: Bella".
**Says:** "Hi, I am Tanishaa, and this video is about how GPS knows where you are. The voice you're hearing is Bella, an AI narrator reading a script Claude drafted and I approved."

### B01 · The one-line summary (~12 s)
**On screen:** Three key points, each appearing as Bella says it: **never sends** · **only listens** (accent) · **times the signals → finds you**.
**Says:** "Your phone never sends anything to a GPS satellite. It only listens. It times how long each signal takes to arrive, and works out the one place you could be."

### B02 · The problem (~15 s)
**On screen:** A small phone on a dark Earth. Far above it, about thirty satellite dots trace their orbits, with a label: **~20,000 km up**. Faint signal rings pulse down from them.
**Says:** "Start with the problem. Your phone has no idea where it is, and no way to ask. All it can do is listen to radio signals from about thirty satellites, twenty thousand kilometers up."

### B03 · Time becomes distance (~20 s)
**On screen:** One satellite with a broadcast card: **"I'm here: (x, y, z)" · "It's exactly 12:00:00.000000"**, with an atomic-clock icon. A pulse travels down to the phone while a stopwatch runs: **0.0706 s**. Then: **0.0706 s × speed of light = 21,162 km**.
**Says:** "Each satellite broadcasts two things, over and over: where it is, and exactly what time it is, from an atomic clock on board. Your phone notes when each signal arrives. Multiply that delay by the speed of light, and you get the distance. Seven hundredths of a second means about twenty-one thousand kilometers."

### B04 · Where the circles meet (~22 s)
**On screen:** A flat map. One satellite's distance draws a circle; you could be anywhere on it. A second circle crosses it at two points. A third circle picks one point, which pulses. A caption reads: **Flattened to circles. In 3D they're spheres.**
**Says:** "One distance tells you you're somewhere on a giant sphere around that satellite. A second sphere narrows it to a circle. A third narrows it to just two points, and one of them is out in space. Here it's flattened into circles, but the idea is the same: you're where they all meet."

### B05 · The catch: a cheap clock (~16 s)
**On screen:** A phone's clock reads **off by 0.000001 s**. A ruler grows to **300 m**. The three circles all swell by the same amount, and the meeting point blurs into a smudge. A fourth circle arrives, and the smudge snaps back to a point. Two labels: **3 satellites → where · 1 more → when**.
**Says:** "But there's a catch. Your phone's clock is cheap. If it's off by just one millionth of a second, every distance is off by three hundred meters. So your phone uses a fourth satellite to work out its own clock error. Three for where, one for when."

### B06 · Worked example, run for real (~19 s)
**On screen:** Real output from `demo/gps_demo.py`: four satellites above Boston Common, their distances and travel times, and a phone clock off by one microsecond. Two results side by side: **Ignore the clock → 390 m off** (a pin across the park) · **Solve for the clock → right on the spot, clock error found: 1.000000 µs**.
**Says:** "Here it is on real numbers. I gave a solver four satellites above Boston Common and a phone clock that's off by one millionth of a second. Ignore the clock, and the answer lands three hundred ninety meters away. Solve for it, and it lands right on the spot, and finds the clock error too."

### B07 · Einstein is in your pocket (~17 s)
**On screen:** A satellite clock gains time beside a ground clock: **+38 µs a day**. Two arrows: **weaker gravity → faster (+45)** · **orbital speed → slower (−7)**. A map pin drifts away: **~11 km a day if uncorrected**. Then a "set slow before launch" tag.
**Says:** "One more surprise. Because of Einstein's relativity, the satellite clocks run fast by about thirty-eight millionths of a second a day. Left alone, your position would drift about eleven kilometers every day. So the clocks are set to tick slightly slow before launch."

### B08 · When to trust it (~24 s)
**On screen:** Two columns sort themselves as each item is spoken.
**Trust it:** outdoors, open sky · within about 5 m.
**Expect it to slip:** between tall buildings (signals bounce) · indoors and underground (it falls back on Wi-Fi and cell towers).
At the end, a third card drops in: **"GPS only listens. Your apps might share."**
**Says:** "So when can you trust it? Outdoors under open sky, a phone is usually accurate to within about five meters. Between tall buildings, signals bounce, and your dot can jump across the street. Indoors and underground, the signal barely gets through, so your phone guesses from Wi-Fi and cell towers. And remember, GPS only listens. The satellites never know where you are, but your apps might."

### B09 · Verdict (~10 s)
**On screen:** A Claude artifact page titled "How GPS Knows Where You Are" with three key findings, each on its words:
1. GPS turns time into distance.
2. Three satellites for where, one for when.
3. GPS only listens; your apps are what share.
**Says:** "Three things to keep. GPS turns time into distance. Three satellites for where, one for when. And GPS only listens; your apps are what share your location."

### B10 · Your turn (~20 s)
**On screen:** The Claude composer, greeting "Your turn.", with this prompt typed in:
> *"Act as my tutor. Draw three circles on a simple map, give me each center and radius, and let me find where they meet. Then check my answer, and show me what happens if every radius is off by the same amount."*

**Says:** "Your turn. Ask Claude to be your tutor: have it give you three circles, find where they meet yourself, then see what happens when every distance is off by the same amount. That's the clock problem, by hand."

### B11 · Outro (~4 s)
**On screen:** The title "How GPS Works." in serif with a terracotta period, and @HumanitariansAI below it.
**Says:** "How GPS knows where you are. At Humanitarians AI."

---

## Fact-check notes (to verify before recording)
- **Real (from `demo/gps_demo.py` → `demo/gps_output.json`):** satellites about 20,200 km up. Ranges from Boston Common are 21,162–21,854 km, with travel times of 70.6–72.9 ms. A 1 µs clock error = 299.8 m per range. Ignoring the clock puts the answer 390 m off; solving with the fourth unknown recovers the position (to under a micrometre, since there's no other noise in the demo) and the 1.000000 µs clock error. The satellite positions are chosen for illustration (all 42–54° above the horizon), not taken from a live almanac. The screen will say so.
- **To confirm from sources (gps.gov and standard references):** about 31 operational GPS satellites ("about thirty"). Relativity: net about +38 µs/day (about +45 from gravity, about −7 from speed), corrected by a factory frequency offset. Uncorrected drift: 38 µs × c ≈ 11.4 km/day. Typical smartphone accuracy under open sky: within about 4.9 m (gps.gov). Receivers only listen; GPS is one-way.
- **B04** simplifies: the "two points, one in space" is the 3-sphere case. The flat circles are labeled as a 2D picture.
