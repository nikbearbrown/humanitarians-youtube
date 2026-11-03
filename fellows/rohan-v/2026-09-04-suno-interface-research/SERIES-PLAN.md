# Lyrical Literacy — Suno Tutorial Series
## Series Planning Document

**Host:** Rohan V. (Humanitarians AI) — voice via Kokoro `af_bella`  
**Palette:** Claude (cream `#FAF9F5`, warm ink `#3D3929`, terracotta `#D97757`)  
**Audience:** HAI Lyrical Literacy volunteers with no music or video background  
**Format:** Remotion + Kokoro TTS — no screen recordings, all UI recreated in code  

---

## Spine Question

Every HAI educational video answers: **when should you use this tool, and when shouldn't you?**

For Suno:
- Use it when you need original music that fits a specific educational moment
- Use it when you want to experiment quickly and cheaply
- Do NOT use it as a final product without listening critically
- Do NOT rely on its lyrics alone when specific vocabulary is required — write your own

---

## Series Structure

| Video | Title | Duration | Core skill | Status |
|-------|-------|----------|-----------|--------|
| Part 1 | Your First Song with Suno | ~3:30 | Get access, navigate, generate first song | Scenes built |
| Part 2 | Crafting Your Prompt | ~3–4 min | Write descriptions that produce the exact sound you need | Plan only |
| Part 3 | Refining and Downloading | ~3–4 min | Extend, edit lyrics, Song Editor, export | Plan only |

---

## Format Standards (apply to all three parts)

**Narration style:**
- Warm and direct — not corporate, not academic
- Every jargon term is explained the first time it appears
- Use "you" throughout, never "one" or passive voice
- Use analogies that work for someone with no music background
- Each beat ends on a clear teachable point

**Visual standards:**
- Suno UI recreated as dark-theme mockups on the Claude cream stage
- Every UI element annotated with callout cards when first introduced
- No screenshots — all UI is programmatic Remotion
- Spark line on every body beat (≤4 words, SERIF, terracotta)
- Eyebrow label on every beat: "LYRICAL LITERACY · SUNO TUTORIAL PART N"

**Beat lengths:**
- Cold open: 18–22s
- BLUF: 15–22s
- Body beats: 22–38s
- Verdict: 28–32s
- Handoff: 26–30s
- Outro: 4–5s

---

---

# PART 1: Your First Song with Suno

**Goal:** A complete beginner can sign in, navigate the interface, write their first prompt, and generate a song.  
**Scenes:** All 8 body scenes already built (`SunoL1Bluf` through `SunoL1SongCards`).  
**Beat count:** 12

---

## Part 1 — Beat Table

| Beat | Act | Scene | Duration |
|------|-----|-------|----------|
| B00 | Cold open | ClaudeComposerAsk | 16s |
| B01 | What Suno does (BLUF) | SunoL1Bluf | 16s |
| B02 | How it works | SunoL1HowItWorks | 18s |
| B03 | Getting Pro access | SunoL1DiscordLogin | 20s |
| B04 | The Suno interface | SunoL1Interface | 16s |
| B05 | Simple mode | SunoL1SimpleMode | 14s |
| B06 | The prompt formula | SunoL1PromptFormula | 24s |
| B07 | Generating + credits | SunoL1Generate | 16s |
| B08 | Song cards | SunoL1SongCards | 18s |
| BVDT | Verdict | ClaudeVerdictArtifact | 22s |
| BHTF | Recap + Part 2 tease | ClaudeComposerAsk | 24s |
| BOUT | Outro | ClaudeTitleOutro | 4s |

**Total estimated runtime:** ~3 min 28s

---

## Part 1 — Full Script

### B00 — Cold Open

**Narration (speak word for word):**

> Hi — I'm Rohan from Humanitarians AI. This video covers exactly one thing: making your first song with Suno. No music background required. No AI experience needed. Follow along and by the end you will have made a complete original song.

**On screen:**  
`ClaudeComposerAsk` — HAI channel skin (cream composer on cream page)  
- Greeting: **"Ciao, HAI"** appears above the composer card  
- The command types itself: *"Walk me through making my first song with Suno — I've never done this before."*  
- Running text: *"setting up your Lyrical Literacy session…"*  
- Three output lines appear one by one:  
  1. *"Step 1: Sign in via HAI Discord — Pro access activates instantly."*  
  2. *"Step 2: Type a description. Style + mood + topic. That's the whole formula."*  
  3. *"Step 3: Click Create. Two original songs appear in about 30 seconds."*  
- Footer chip: `@HumanitariansAI`

**Teaching point:** By the end of this video, the viewer will have generated a song.

---

### B01 — What Suno Does (BLUF)

**Narration:**

> Here's the whole picture before we dive in. Suno is a tool where you type a description — the style, mood, and topic of the song you want — and it creates a complete, original song. Not remixed from something that already exists. Not a loop or a sample. Brand new audio, made from scratch, every single time. HAI has set up free Pro access for you through Discord. By the end of this video, you will be logged in and generating your first song.

**On screen:**  
`SunoL1Bluf` — SourceFlow pipeline illustration on cream stage  
- Three nodes appear left to right:  
  1. **"Your description"** (cream card, serif text showing the example prompt)  
  2. **"suno"** (dark node, terracotta border, terracotta connecting arrows)  
  3. **"Original song"** (cream card with waveform bars + "Vocals · Melody · Instruments")  
- Caption below: *"Not remixed from existing music — generated fresh, every time."*  
- Spark line: **✦ Text in. Original song out.**

**Teaching point:** Suno creates, it does not search. The output is genuinely new.

---

### B02 — How It Works

**Narration:**

> You might be wondering: how does a computer actually make music? Here's a simple way to think about it. Suno was trained on millions of songs across every genre — folk, hip-hop, pop, jazz, classical, reggae, everything. Over that training, it learned what makes music feel hopeful or tense, fast or slow, acoustic or electronic. Think of it the way autocomplete works on your phone. You type the beginning of a sentence, and your phone guesses what comes next based on patterns it's learned from thousands of messages. Suno does the same thing with music. You give it a starting point — your description — and it fills in the rest. You don't need to understand how this works to use it well. What matters is your description.

**On screen:**  
`SunoL1HowItWorks` — genre convergence concept illustration  
- Left: eight genre chips animate in (Folk · Hip-Hop · Pop · Jazz · Classical · Electronic · R&B · Country)  
- Each chip has a small colored border matching its mood (green=folk, purple=pop, etc.)  
- Lines converge from each chip toward a central dark circle labeled "suno / trained"  
- Right of the central node: a waveform output card labeled "Your song"  
- Caption: *"Like autocomplete — but for music."*  
- Spark line: **✦ Describe the feeling. Suno fills it in.**

**Teaching point:** No music knowledge needed. The model has already learned everything — you just describe what you want.

---

### B03 — Getting Pro Access

**Narration:**

> Before you can create anything, you need to sign in. HAI gives every Lyrical Literacy volunteer free Pro access — here's how to activate it in five steps. One: join the HAI Discord server. Your team lead will send you the invite link — if you haven't joined yet, do that first. Two: go to suno.com. Three: click Sign In in the top right corner. Four: choose the Discord option from the sign-in menu. Five: sign in with your HAI Discord account. The moment you log in, Pro access activates automatically. No credit card. Nothing to install. Nothing to pay.

**On screen:**  
`SunoL1DiscordLogin` — five-step numbered list  
- Five cards stack in from top to bottom, one by one, timed to the narration  
- Each card: circle number badge + headline + one-line detail  
- As each card appears, it is highlighted (terracotta border, number badge in terracotta)  
- Previous cards show a green check mark as the narration moves on  
- Final card stays highlighted longest  
- Below all cards: *"No credit card. Nothing to install. Pro activates automatically."*  
- Spark line: **✦ Five steps. Free forever.**

**Teaching point:** The sign-in process is simple and costs nothing. HAI has already done the setup work.

---

### B04 — The Suno Interface

**Narration:**

> You're in. The first thing you'll see is the Suno interface. On the left side is a sidebar with three main items. Explore — this is where you can browse songs that other people have made on Suno. Spend a few minutes here when you start — it's the best way to hear what's possible before you make something yourself. Library — this is where every song you generate gets saved automatically. You don't have to do anything to save your work; it just appears here. Create — this is where you work. That's where we're going next. And in the top right corner you'll see a credit balance. We'll come back to what credits are in a moment.

**On screen:**  
`SunoL1Interface` — faithful Suno sidebar reconstruction  
- Dark Suno window (sidebar + dimmed main area) on cream stage  
- Sidebar shows: "suno" logo, then three nav items  
- Each nav item highlights in sequence as narration mentions it:  
  - Explore → callout card: *"Browse what others are making. Good for inspiration."*  
  - Library → callout card: *"Every song you generate is saved here automatically."*  
  - Create → callout card: *"Where you work. This is where you make songs."*  
- Credit counter at bottom of sidebar then highlights:  
  - Callout: *"2,500 credits/month with HAI Pro. That's 500 songs. More on credits shortly."*  
- Spark line: **✦ Three items. Start with Create.**

**Teaching point:** The interface has three sections. Only one matters right now: Create.

---

### B05 — Simple Mode

**Narration:**

> Click Create. Inside, you'll see two tabs at the top — Simple and Custom. Start with Simple. Custom mode gives you more control over lyrics and song structure, and we cover that in Part 3. In Simple mode, you have three things. A description field — this is where you type what you want the song to be. An Instrumental checkbox — tick this if you want music without vocals, just the melody and instruments. And a Create button. That's everything. Three elements. You are ready to make a song.

**On screen:**  
`SunoL1SimpleMode` — Suno Create page reconstruction  
- Suno window with sidebar (Create highlighted) + main content panel  
- Simple/Custom tab row at top — Simple tab is active (terracotta underline)  
  → Callout: *"Simple / Custom tabs — start with Simple. Custom is for Part 3."*  
- Description textarea below, placeholder text fades in  
  → Typing animation: the example prompt types itself character by character  
  → Callout: *"Description field — type style, mood, and topic here."*  
- Instrumental checkbox below  
  → Callout: *"Tick this for music without vocals — melody and instruments only."*  
- Create button at bottom  
  → Callout: *"Create button — click when your description is ready. Suno makes two versions."*  
- Spark line: **✦ Simple mode. One field. One button.**

**Teaching point:** Simple mode is three things: description, checkbox, button. That's all you need.

---

### B06 — The Prompt Formula

**Narration:**

> Before you hit Create, you need to write your description. Good news: there's a simple formula with three ingredients. First, musical style — what genre or sound are you going for? Folk, pop, hip-hop, jazz, reggae, something electronic? Second, mood or feeling — what emotion should this music carry? Hopeful, melancholy, playful, driving, calm, dreamy? Third, topic — what is the song actually about? You don't need to use technical music language. Just describe the feeling. Here's an example that puts all three together: "A gentle acoustic folk song, warm and hopeful, about children discovering the joy of reading." Style: acoustic folk. Mood: warm and hopeful. Topic: children discovering reading. That is a complete, usable Suno prompt.

**On screen:**  
`SunoL1PromptFormula` — three-ingredient formula  
- Three ingredient cards appear one by one, each with its label, example, and a color-coded border:  
  1. **Musical Style** (green border) — *"acoustic folk"* — detail: *"Genre, instruments, or sonic reference"*  
  2. **Mood or Feeling** (terracotta border) — *"warm and hopeful"* — detail: *"The emotion the music should carry"*  
  3. **Topic** (blue border) — *"children discovering the joy of reading"* — detail: *"What the song is actually about"*  
- Plus signs appear between cards  
- Equals sign appears below  
- Assembled example prompt appears in a bordered card:  
  *"A gentle **acoustic folk song**, **warm and hopeful**, about **children discovering the joy of reading**."*  
  Each section colored to match its ingredient card  
- Spark line: **✦ Style. Mood. Topic.**

**Teaching point:** Three ingredients. Remember them: style, mood, topic. That's the whole formula.

---

### B07 — Generating and Credits

**Narration:**

> Now click Create. Suno makes two versions of your song at the same time — two different takes on the same description. This means you almost always have something to choose from. It takes about 30 to 60 seconds. Each time you click Create, it costs 5 credits. Your HAI Pro account gives you 2,500 credits every month. That's 500 songs. You have plenty of room to experiment, try different descriptions, and not worry about running out.

**On screen:**  
`SunoL1Generate` — three-phase animation  

*Phase 1 (frames 0–59):* The Create page with the filled description field visible. The Create button is present and clearly labeled.  

*Phase 2 (frames 60–159):* Button click animation (brief scale pulse). Then loading state: three bouncing dots, text *"Generating two versions…"*, sub-text *"30–60 seconds · 5 credits"*.  

*Phase 3 (frames 160–end):* Credits info panel slides in from right:  
- Large **"5"** in terracotta — *"per generation (2 songs)"*  
- Divider  
- **"2,500"** — *"= 500 songs / month"*  
- Spark line: **✦ 500 songs a month. Experiment freely.**

**Teaching point:** Two versions per generation, 5 credits each, 2,500 credits per month. This is abundant — experiment freely.

---

### B08 — Song Cards

**Narration:**

> When Suno is done, two song cards appear. Hit play on the first one and just listen. You don't need to judge it technically. Ask yourself: does this feel like what I described? Is the mood right? Are the vocals working? If you like it, you have your first song. If it's not quite right — that's fine too. That's information. You can download either one, regenerate using the same description to get two fresh versions, or use one as a starting point to build something longer. Part 2 covers how to write better descriptions. Part 3 covers how to extend and download.

**On screen:**  
`SunoL1SongCards` — two result cards side by side  
- Both cards are dark Suno-style cards on cream stage  
- Left card: auto-generated artwork (teal gradient), title "Morning Pages", tags (acoustic folk · hopeful · children), waveform in green (active), Duration "2:47", Version 1 badge  
  → Play button pulses gently (active card)  
- Right card: blue gradient artwork, title "Open the Book", same tags, waveform in gray (inactive), Duration "2:53", Version 2 badge  
- Action row on each card: ▶ Play · ⬇ Download · ↺ Regenerate  
- Caption: *"Play both. If neither is right, regenerate — or take the better one into Part 2 to refine it."*  
- Spark line: **✦ Two versions. Pick one. Build from there.**

**Teaching point:** You always get two versions. Pick the better one. Regenerating is free in spirit — just 5 more credits.

---

### BVDT — Verdict

**Narration:**

> Let's put it all together. Suno generates complete, original songs from text descriptions. Sign in at suno.com using your HAI Discord account — Pro access activates the moment you log in. Inside Create, select Simple mode. Write a description using three ingredients: style, mood, and topic. Click Create. Two versions appear in about 30 seconds for 5 credits. Your HAI Pro account includes 2,500 credits a month — 500 songs. Listen to both versions, pick the one that fits better, and decide where to take it next. In Part 2, we go deeper on how to write descriptions that get you exactly the sound you need for your project.

**On screen:**  
`ClaudeVerdictArtifact` — cream artifact card  
- Title: *"Suno, Part One."*  
- Heading: *"What you can do right now"*  
- Four lines:  
  1. *"Sign in at suno.com via HAI Discord — Pro activates instantly, no credit card."*  
  2. *"In Create → Simple mode, write a description: musical style + mood + topic."*  
  3. *"Click Create. Two original songs generate in ~30 seconds at 5 credits."*  
  4. *"Your HAI Pro account includes 2,500 credits/month — 500 songs to experiment with."*

---

### BHTF — Recap and Part 2 Tease

**Narration:**

> In this video we covered what Suno is and how it works, getting Pro access through HAI Discord, navigating the interface, writing a three-ingredient prompt, and generating your first song. In Part 2, we go deeper on the prompt — how to write descriptions that get you the exact sound and feeling your project needs. I'm Rohan V. from Humanitarians AI. See you in Part 2.

**On screen:**  
`ClaudeComposerAsk` — Part 2 preview  
- Greeting: *"See you in Part 2."*  
- Command: *"What do we cover in Suno Part 2?"*  
- Running text: *"previewing Part 2…"*  
- Output lines:  
  1. *"How to write descriptions that get you the exact sound you need."*  
  2. *"Style vocabulary, mood vocabulary, and topic specificity."*  
  3. *"Iteration — how to improve a prompt in three passes."*  
- Footer: `@HumanitariansAI`

---

### BOUT — Outro

**Narration:** *"Rohan V. Humanitarians AI."*

**On screen:**  
`ClaudeTitleOutro`  
- Title: *"Rohan V."*  
- Handle: *"@HumanitariansAI"*  
- Subline: *"Lyrical Literacy · Suno Tutorial Series"*

---
---

# PART 2: Crafting Your Prompt

**Goal:** Volunteers can write descriptions that produce exactly the sound and mood their educational project needs, using style vocabulary, mood vocabulary, topic specificity, and iteration.  
**Scenes to build:** 8 new scenes (`SunoL2Bluf` through `SunoL2LLPrompt`)  
**Beat count:** 13

---

## Part 2 — Beat Table

| Beat | Act | Scene | Duration |
|------|-----|-------|----------|
| B00 | Cold open | ClaudeComposerAsk | 22s |
| B01 | The core idea (BLUF) | SunoL2Bluf | 22s |
| B02 | Two prompts, two songs | SunoL2PromptComparison | 28s |
| B03 | Style vocabulary | SunoL2StyleGuide | 34s |
| B04 | Mood and energy vocabulary | SunoL2MoodGuide | 30s |
| B05 | Topic specificity — the zoom lens | SunoL2TopicZoom | 26s |
| B06 | Iteration: improving a prompt three times | SunoL2Iteration | 32s |
| B07 | Custom mode introduction | SunoL2CustomMode | 24s |
| B08 | Style tags in Custom mode | SunoL2TagSystem | 24s |
| B09 | Building a Lyrical Literacy prompt | SunoL2LLPrompt | 38s |
| BVDT | Verdict | ClaudeVerdictArtifact | 30s |
| BHTF | Your turn | ClaudeComposerAsk | 28s |
| BOUT | Outro | ClaudeTitleOutro | 5s |

**Total estimated runtime:** ~8 min 23s

---

## Part 2 — Full Script

---

### B00 — Cold Open

**Narration:**

> Ciao — Bella here, Lyrical Literacy. In Part 1, you made your first song with Suno. Now let's talk about the part that actually determines the quality of what you get: the description you write. Because two different descriptions of the exact same idea can produce two completely different songs. One might feel like what you needed. The other might feel completely off. In this video, you'll learn how to write descriptions that get you the exact sound and feeling your project needs.

**On screen:**  
`ClaudeComposerAsk`  
- Greeting: *"Ciao, HAI"*  
- Command: *"How do I write better Suno descriptions to get the exact song I need for a Lyrical Literacy project?"*  
- Running text: *"building your prompting vocabulary…"*  
- Output lines:  
  1. *"Key 1: Specificity drives quality. Vague descriptions produce vague songs."*  
  2. *"Key 2: Style + mood + topic is the formula. Each one can be made more precise."*  
  3. *"Key 3: Iteration is the method. Every attempt asks: what am I still not saying?"*

---

### B01 — The Core Idea (BLUF)

**Narration:**

> Here's the key idea for this whole video. Suno is not a search engine. You are not looking up a song that already exists somewhere. You are giving instructions to something that will create whatever you describe. That means the quality of your output is entirely controlled by the quality of your input. A vague description produces a vague song. A specific, feeling-rich description produces a song that lands exactly where you need it. This video gives you the vocabulary and the method to write descriptions that work.

**On screen:**  
`SunoL2Bluf` — split-screen contrast illustration  
- Two columns side by side, each with a prompt card and a "result" description below  

LEFT column (weak):  
- Prompt card (gray border): *"A children's song about reading."*  
- Result description below: *"Generic melody, unclear emotional tone, could be about anything."*  
- Label: **Weak prompt**  

RIGHT column (strong):  
- Prompt card (terracotta border): *"A playful acoustic ukulele song with hand claps and a bouncing melody, joyful and encouraging, about a child sounding out their very first word."*  
- Result description below: *"Bright, specific energy — instruments named, moment named, emotion named."*  
- Label: **Strong prompt**  

- Central dividing line with label: *"Same idea. Very different songs."*  
- Spark line: **✦ Better description. Better song.**

**Teaching point:** Output quality = input quality. There's no other way to improve results.

---

### B02 — Two Prompts, Two Songs

**Narration:**

> Let me show you the difference concretely. Two descriptions of the same basic idea — a song for kids learning to read. The first: "A children's song about reading." The second: "A playful acoustic ukulele song with hand claps and a bouncing melody, joyful and encouraging, about a child sounding out their very first word." I want you to notice what the second description does differently. It names the instruments. It names the energy — bouncing melody. It names the emotion — joyful and encouraging. And it names the specific moment — their very first word. Everything that makes a song feel intentional comes from that specificity.

**On screen:**  
`SunoL2PromptComparison` — annotated comparison  
- Two prompt cards appear side by side  
- On the STRONG prompt, four terracotta annotation arrows point to specific phrases:  
  - Arrow 1 → *"acoustic ukulele"* — label: **"Instruments named"**  
  - Arrow 2 → *"bouncing melody"* — label: **"Energy named"**  
  - Arrow 3 → *"joyful and encouraging"* — label: **"Emotion named"**  
  - Arrow 4 → *"very first word"* — label: **"Specific moment named"**  
- The weak prompt has no annotations — it sits with a single label: *"What does Suno do with this?"*  
- Spark line: **✦ Name the instruments. Name the moment.**

**Teaching point:** Four things to name: instruments, energy, emotion, specific moment. That's the difference between weak and strong.

---

### B03 — Style Vocabulary

**Narration:**

> Let's build your vocabulary, starting with style. Style is about genre and sonic texture — what kind of music world this song lives in. You have a huge range. Folk: acoustic guitars, natural feeling, often storytelling. Hip-hop: beat-driven, rhythm comes first, vocal flow. Pop: clean production, a strong chorus, accessible. Reggae: relaxed off-beat rhythm, warm bass, unhurried. Blues: soulful, emotionally weighted, bends in the melody. Gospel: uplifting, choir energy, call-and-response. Lullaby: gentle, slow, minimal. You can combine styles — "folk-pop" or "acoustic hip-hop" both work. And you don't need the exact term. If you write "like a song from a children's TV show from the nineties," Suno understands that. Use whatever language best describes the sound you hear in your head.

**On screen:**  
`SunoL2StyleGuide` — animated genre vocabulary grid  
- Grid of genre cards animate in group by group  
- Each card: genre name (SERIF, large) + 3-word descriptor (SANS, muted) + color-coded border  
  - Folk (green) — *"acoustic · natural · storytelling"*  
  - Hip-Hop (purple) — *"beat-driven · rhythmic · flow"*  
  - Pop (terracotta) — *"produced · hooky · accessible"*  
  - Reggae (teal) — *"off-beat · warm · unhurried"*  
  - Blues (dark blue) — *"soulful · emotional · bending"*  
  - Gospel (amber) — *"uplifting · choir · call-response"*  
  - Lullaby (soft gray) — *"gentle · slow · minimal"*  
  - Classical (dark gray) — *"orchestral · structured · expressive"*  
- Below grid: two combination examples appear  
  - *"folk-pop"* — and what that means  
  - *"acoustic hip-hop"* — and what that means  
- Spark line: **✦ Name the sound world.**

**Teaching point:** Genre vocabulary is a starting point, not a requirement. Any descriptive language that conveys the sound works.

---

### B04 — Mood and Energy Vocabulary

**Narration:**

> The second ingredient is mood — the emotional temperature of the music. This is where you tell Suno how the music should make someone feel. Useful mood words: warm, hopeful, gentle, dreamy, calm, melancholic, wistful, tender, joyful, playful, bouncy, energetic, driving, urgent, triumphant, solemn. Energy level matters separately from emotion. "Slow and meditative" is very different from "upbeat and driving," even if both songs could be described as hopeful. For Lyrical Literacy projects with younger listeners, words like warm, encouraging, playful, and joyful tend to work well. But for a song about the struggle to learn something hard, "quietly determined" might capture exactly the right feeling — the kind of music that says "you can do this."

**On screen:**  
`SunoL2MoodGuide` — mood spectrum grid  
- A two-axis grid appears:  
  - Horizontal axis: **"Gentle / Calm" ←→ "Energetic / Driving"**  
  - Vertical axis: **"Melancholic / Heavy" ↕ "Joyful / Light"**  
- Mood words appear at their positions on the grid, color-coded by quadrant:  
  - Top-right (joyful + energetic): bouncy · playful · triumphant · upbeat  
  - Top-left (joyful + gentle): warm · tender · dreamy · hopeful  
  - Bottom-left (melancholic + gentle): wistful · calm · reflective · solemn  
  - Bottom-right (melancholic + energetic): urgent · driving · determined · intense  
- Lyrical Literacy examples highlighted with a terracotta dot: warm, hopeful, playful, encouraging, gently determined  
- Spark line: **✦ Emotion. Then energy level.**

**Teaching point:** Mood has two dimensions — the emotion AND the energy level. Name both.

---

### B05 — Topic Specificity — The Zoom Lens

**Narration:**

> The third ingredient is topic — and this is where most people leave the most quality on the table. A vague topic gives Suno too much room to go anywhere. A specific topic locks it into exactly what you need. Think of it like a zoom lens on a camera. "Children learning" is the wide shot — you could be anywhere, any subject. "A seven-year-old at a library table, taking a deep breath before she reads the first paragraph of her first chapter book" is a close-up. That level of specificity produces music with genuine feeling. For educational songs, you don't need to be this poetic. But do try to name: who is in the song, what moment are we in, what emotion lives in that moment.

**On screen:**  
`SunoL2TopicZoom` — zoom lens illustration  
- A camera lens graphic at left, with a zoom slider below it  
- As the slider moves from "wide" to "close-up," the right panel changes:  

  *Wide (vague):*  
  - Topic text: *"Children learning"*  
  - Description: *"Suno could go anywhere — classroom, reading, maths, science, sports…"*  
  - Result preview: blurry, undefined waveform  

  *Mid (better):*  
  - Topic text: *"A child learning to read"*  
  - Description: *"Narrower — but still no moment, no emotion"*  
  - Result preview: slightly clearer waveform  

  *Close-up (specific):*  
  - Topic text: *"A child at a library table, taking a breath before reading her first chapter book"*  
  - Description: *"A moment. A person. An emotion. Suno has everything it needs."*  
  - Result preview: clear, focused waveform  

- Below: *"Name the who. Name the moment. Name the emotion in that moment."*  
- Spark line: **✦ Zoom in. Get specific.**

**Teaching point:** Three things to name in any topic: the person, the moment, the emotion in that moment.

---

### B06 — Iteration: Improving a Prompt Three Times

**Narration:**

> Prompting is not a one-shot activity. It's a conversation you have with the tool over several tries. Here is the same starting idea, improved three times. Attempt one: "A song about reading for kids." This is a starting point, nothing more — there's no style, no mood, no moment. Attempt two: "An upbeat pop song, cheerful and encouraging, about kids who love reading." Better — we have style and mood now. Attempt three: "A bright, bouncy pop song with xylophone and hand claps, warmly encouraging, for a child who just finished their first book on their own." Now we have instruments, a specific energy, and a specific emotional moment. Each pass asks the same question: what am I still not saying? What can I name that I haven't named yet?

**On screen:**  
`SunoL2Iteration` — three-step prompt evolution  
- Three prompt cards appear vertically, each replacing or building on the previous  
- Each card is labeled Attempt 1 / 2 / 3 with a version number  

  *Card 1 (attempt 1):*  
  - Prompt: *"A song about reading for kids."*  
  - Annotation in terracotta: *"Missing: style, mood, specific moment"*  

  *Card 2 (attempt 2):*  
  - Prompt: *"An upbeat pop song, cheerful and encouraging, about kids who love reading."*  
  - Terracotta check marks on: style (pop) · mood (cheerful, encouraging)  
  - Annotation: *"Still missing: instruments, specific moment"*  

  *Card 3 (attempt 3):*  
  - Prompt: *"A bright, bouncy pop song with xylophone and hand claps, warmly encouraging, for a child who just finished their first book on their own."*  
  - Terracotta check marks on: style · instruments · mood · specific moment  
  - Annotation: *"Complete"* ✓  

- Below: *"Each pass asks: what am I still not saying?"*  
- Spark line: **✦ Each attempt, add one thing.**

**Teaching point:** Iteration method: write one pass, identify what's missing, add it, repeat. Three passes usually produces something strong.

---

### B07 — Custom Mode Introduction

**Narration:**

> So far we've been working in Simple mode. Custom mode gives you two things Simple mode doesn't: the ability to write or paste your own lyrics, and a Style field where you can enter specific production tags for even more precision. You don't have to use Custom mode. For many Lyrical Literacy projects, a well-written Simple mode prompt is completely sufficient. But if you need a song to use specific words — vocabulary a curriculum requires, or a repeated phrase for a phonics lesson — Custom mode is how you put exactly those words into the song. To switch: click the Custom tab inside Create.

**On screen:**  
`SunoL2CustomMode` — Suno Create page, Custom tab  
- The Suno Create page mock with the Simple/Custom tab row at top  
- Animation: Simple tab is active → Custom tab activates (tab switch animation)  
- Custom mode shows additional fields compared to Simple:  
  - **Lyrics** (large textarea, labeled) → Callout: *"Write or paste your own lyrics here. Suno will use your exact words."*  
  - **Style** (single-line field with tags) → Callout: *"Production tags — genre terms, instrument names, mood words."*  
  - **Title** (single-line field) → Callout: *"Optional — Suno will generate a title if you leave this blank."*  
  - Create button  
- Spark line: **✦ Your lyrics. Your words. Exactly.**

**Teaching point:** Custom mode = your lyrics + style tags. Use it when the specific words matter for educational reasons.

---

### B08 — Style Tags in Custom Mode

**Narration:**

> In the Custom mode Style field, you enter specific production tags. Tags are short phrases that tell Suno's system exactly how to render the song. Examples: "acoustic guitar," "male vocals," "slow tempo," "children's choir," "ukulele," "hand claps," "no electric instruments." You separate tags with commas. The more specific your tags, the more control you have. For Lyrical Literacy projects, some particularly useful tags: "children's music," "educational," "call and response," "simple melody," "gentle percussion." You can combine these with a broader genre description in the same field — for example: "upbeat children's folk-pop, ukulele, hand claps, simple repeating melody, call and response."

**On screen:**  
`SunoL2TagSystem` — Style field tag demonstration  
- Close-up view of the Custom mode Style field  
- Tags appear one by one as chips being typed into the field:  
  - *"children's music"* → tooltip: *"signals the overall register"*  
  - *"ukulele"* → tooltip: *"specific instrument"*  
  - *"hand claps"* → tooltip: *"rhythmic texture"*  
  - *"simple repeating melody"* → tooltip: *"instructs melodic complexity"*  
  - *"call and response"* → tooltip: *"song structure element"*  
  - *"gentle percussion"* → tooltip: *"instructs energy of the rhythm"*  
- Below the field: the assembled tag string shown as a single line  
- Callout: *"Separate tags with commas. More specific = more control."*  
- A "Lyrical Literacy recommended tags" panel on the right showing the most useful 6 tags  
- Spark line: **✦ More specific tags. More precise sound.**

**Teaching point:** Tags give granular control. Instrument names, structure terms, and energy words are the most useful categories.

---

### B09 — Building a Lyrical Literacy Prompt

**Narration:**

> Let's put everything together and build a real Lyrical Literacy prompt from scratch. The project: a phonics song for 6-year-olds, focusing on the short "A" sound — words like at, cat, bat, hat. Step one: style. We want this to feel familiar and safe for young children — upbeat children's folk-pop with acoustic guitar and ukulele. Step two: mood. Encouraging and playful. Learning should feel fun, never stressful. Step three: topic. The short A sound — name the actual words in the song. "At, cat, bat, hat — each one sung clearly in the lyric." Step four: add a production note. Simple repeating melody, easy to sing along to. Assemble: "Upbeat children's folk-pop with acoustic guitar and ukulele, playful and encouraging, about the short A sound — at, cat, bat, hat — with a simple repeating melody that kids can sing along to." That is a complete, production-ready Suno prompt.

**On screen:**  
`SunoL2LLPrompt` — four-layer prompt assembly  
- Four labeled layers build up vertically, each adding to the assembled prompt below  

  *Layer 1 — Style:*  
  - Green card: *"upbeat children's folk-pop, acoustic guitar and ukulele"*  
  - Label: **Musical Style**  

  *Layer 2 — Mood:*  
  - Terracotta card: *"playful and encouraging"*  
  - Label: **Mood**  

  *Layer 3 — Topic:*  
  - Blue card: *"the short A sound — at, cat, bat, hat — each one named in the song"*  
  - Label: **Topic (specific vocabulary)**  

  *Layer 4 — Production note:*  
  - Gray card: *"simple repeating melody, easy to sing along to"*  
  - Label: **Production note**  

- All four layers merge into a final assembled prompt card at the bottom:  
  *"Upbeat children's folk-pop with acoustic guitar and ukulele, playful and encouraging, about the short A sound — at, cat, bat, hat — with a simple repeating melody that kids can sing along to."*  
  Each phrase color-highlighted in its layer's color  

- Label: **Production-ready prompt** ✓  
- Spark line: **✦ Four layers. One prompt. Ready to generate.**

**Teaching point:** A production-ready Lyrical Literacy prompt has four layers: style + mood + specific topic vocabulary + production note.

---

### BVDT — Verdict

**Narration:**

> Here's what we covered. Suno is not a search engine — you're giving instructions for something that will be created. Specificity drives quality. Use the three-ingredient formula: style, mood, topic. Build your style vocabulary — genre names, instrument names. Use mood words that name both the emotion and the energy level. Make your topic specific — name the person, the moment, the emotion in that moment. Iterate: each attempt asks "what am I still not saying?" Custom mode lets you write exact lyrics and use production tags for granular control. For Lyrical Literacy, always name the educational content — the specific words, sounds, or concepts — directly in the topic. Part 3 covers what to do once you have a song you like.

**On screen:**  
`ClaudeVerdictArtifact`  
- Title: *"Suno, Part Two."*  
- Heading: *"What makes a prompt work"*  
- Four lines:  
  1. *"Specificity drives quality — name instruments, energy, emotion, and the specific moment."*  
  2. *"Use the three-ingredient formula: style (genre/instruments) + mood (emotion + energy) + topic (person, moment, feeling)."*  
  3. *"Iterate with one question each pass: what am I still not saying?"*  
  4. *"Custom mode for specific lyrics or production tags — use when exact vocabulary matters for the curriculum."*

---

### BHTF — Your Turn

**Narration:**

> Your turn. Here's the prompt — read it with me. "I'm making a song for 7 and 8-year-olds about the difference between silent-E words and short vowel words — like cap versus cape. I need a Suno description that makes the distinction feel fun rather than confusing. Use the style-mood-topic formula and suggest two or three production tags for the Style field in Custom mode." The reason this is worth asking Claude first: the linguistic concept needs to land emotionally for the kids. Getting that framing right before you go into Suno will save you several iteration cycles. Try this now, and compare what Claude gives you against the four-layer formula from this video.

**On screen:**  
`ClaudeComposerAsk`  
- Greeting: *"Your turn."*  
- Command: *"I'm making a song for 7 and 8-year-olds about the difference between silent-E words and short vowel words — like cap versus cape. I need a Suno description that makes the distinction feel fun rather than confusing. Use the style-mood-topic formula and suggest two or three production tags for the Style field in Custom mode."*  
- Running text: *"paste this into Claude…"*

---

### BOUT — Outro

**Narration:** *"Suno, Part Two."*

**On screen:**  
`ClaudeTitleOutro`  
- Title: *"Suno, Part Two."*  
- Handle: *"@HumanitariansAI"*  
- Subline: *"Lyrical Literacy Tutorial Series"*

---
---

# PART 3: Refining and Downloading

**Goal:** Volunteers can take a generated clip, extend it to a full song, edit the lyrics when needed, use the Song Editor to build a complete track, and download a finished file.  
**Scenes to build:** 8 new scenes (`SunoL3Bluf` through `SunoL3FileWorkflow`)  
**Beat count:** 12

---

## Part 3 — Beat Table

| Beat | Act | Scene | Duration |
|------|-----|-------|----------|
| B00 | Cold open | ClaudeComposerAsk | 20s |
| B01 | The starting point (BLUF) | SunoL3Bluf | 18s |
| B02 | Listening critically | SunoL3ListenGuide | 28s |
| B03 | The Extend feature | SunoL3ExtendFlow | 26s |
| B04 | The Lyrics Editor | SunoL3LyricsEditor | 28s |
| B05 | Writing your own lyrics | SunoL3CustomLyrics | 24s |
| B06 | The Song Editor | SunoL3SongEditor | 30s |
| B07 | Downloading | SunoL3Download | 22s |
| B08 | File workflow for the team | SunoL3FileWorkflow | 24s |
| BVDT | Verdict | ClaudeVerdictArtifact | 28s |
| BHTF | Your turn | ClaudeComposerAsk | 26s |
| BOUT | Outro | ClaudeTitleOutro | 5s |

**Total estimated runtime:** ~7 min 39s

---

## Part 3 — Full Script

---

### B00 — Cold Open

**Narration:**

> Ciao — Bella, Lyrical Literacy. You've made a song. You have a prompt that works and a clip you like. Now what? In this video we cover everything that happens after that first generation: how to extend a clip to a full-length song, how to edit the lyrics when they're not quite right, how to use the Song Editor to build a complete track with a proper structure, and how to download a finished file that's ready for your project.

**On screen:**  
`ClaudeComposerAsk`  
- Greeting: *"Ciao, HAI"*  
- Command: *"I've generated a 90-second Suno clip I like. How do I turn it into a complete song and download it for my Lyrical Literacy project?"*  
- Running text: *"mapping the refinement workflow…"*  
- Output lines:  
  1. *"Step 1: Listen critically before you touch anything — mood, vocals, melody structure."*  
  2. *"Step 2: Extend to full length (2–4 minutes) using Suno's Extend feature."*  
  3. *"Step 3: Edit lyrics if needed → Song Editor → Download as MP3."*

---

### B01 — The Starting Point (BLUF)

**Narration:**

> Here's the frame for this whole video. What Suno generates in 30 seconds is a starting point — a short clip, usually 30 seconds to 2 minutes, sometimes with a rough structure. To make it a usable track for a Lyrical Literacy program — a real song with a verse, a chorus, and a clear ending — you will usually need to extend it, shape it, and then export it. Those three steps — extend, shape, export — are what this video teaches.

**On screen:**  
`SunoL3Bluf` — three-stage pipeline illustration  
- Three nodes, left to right, on cream stage:  
  1. **"Generated clip"** — dark card, shows a short waveform (30s–2min labeled)  
     Terracotta arrow →  
  2. **"Extended + shaped track"** — dark card, longer waveform, sections labeled (Verse · Chorus · Verse · Chorus)  
     Terracotta arrow →  
  3. **"Downloaded file"** — cream card, file icon, "MP3 · Ready to use"  
- Caption: *"A generated clip is raw material. A finished track takes three more steps."*  
- Spark line: **✦ Extend. Shape. Export.**

---

### B02 — Listening Critically

**Narration:**

> Before you extend or edit anything, spend two minutes listening carefully. Here's what to pay attention to. First: does the mood match your description? If you asked for warm and hopeful and got something that sounds anxious or tense, that's a signal to regenerate rather than invest time in extending the wrong song. Second: are the vocals sitting clearly over the instruments? You should be able to make out the words without straining. Third: is the melody simple enough for your audience? For 6 to 8-year-olds, simple, stepwise melodies — ones that move by small steps rather than big jumps — work much better than complex or unpredictable ones. Fourth: can you hear the structure? Most Suno songs start with an intro, then move into verse-chorus patterns. Listen for where those sections fall before you extend.

**On screen:**  
`SunoL3ListenGuide` — annotated waveform  
- A waveform of a song stretched across the full width of the frame  
- Vertical markers divide it into labeled sections: **Intro · Verse 1 · Chorus · Verse 2 · Chorus · Outro**  
- Four callout bubbles appear one by one above the waveform:  
  1. Over the intro: *"Does the mood feel right? Warm? Playful? Urgent?"*  
  2. Over the first verse: *"Are vocals clear above the instruments?"*  
  3. Over the chorus: *"Is the melody simple enough for your audience to follow?"*  
  4. Over the structure divisions: *"Can you hear where sections change?"*  
- Green checkmarks appear on each as the narration passes  
- Bottom: *"Two minutes of careful listening saves thirty minutes of editing the wrong song."*  
- Spark line: **✦ Listen before you touch anything.**

---

### B03 — The Extend Feature

**Narration:**

> Suno's generated clips are usually 30 seconds to 2 minutes. For a usable educational song, you'll typically want 2 to 4 minutes. The Extend feature continues the song from wherever it left off. Suno picks up the musical idea and keeps building. To extend: open the song in your Library, click the three-dot menu on the song card, and choose Extend. Suno generates a continuation and adds it to your library linked to the original. You can extend multiple times to build longer songs. You can also extend from the middle of a song — useful when the music is building somewhere interesting and you want to branch before it ends rather than after.

**On screen:**  
`SunoL3ExtendFlow` — extend workflow illustration  
- Suno Library mockup showing a song card  
- The three-dot menu opens → "Extend" option highlighted in terracotta  
- Animation: the waveform grows to the right as the extension generates  
- Duration counter updates: *"1:24 → 2:48"*  
- Below: two separate diagrams:  
  *Option A:* Extend from end — arrow at the end of clip  
  *Option B:* Extend from middle — arrow in the middle of clip with a branch  
- Callout: *"Extending from the middle creates a branch — useful for exploring different directions."*  
- Spark line: **✦ Extend. Grow the song.**

---

### B04 — The Lyrics Editor

**Narration:**

> Every song Suno generates comes with lyrics — the words it created to match the music. You can view and edit these. Open any song, find the three-dot menu, and choose Edit in Song Editor. Then click the Lyrics tab. You'll see the full text of what was generated, broken into sections — verse, chorus, and so on. If there are words that don't fit your educational goal — or phrases that are simply off — you can edit them here and regenerate the vocals. One important thing to understand: editing lyrics does not change the instrumental track. The melody and instruments stay exactly as they are. You are only changing the words. This makes it perfect for small fixes, but if you need a complete lyrical overhaul, Custom mode with your own lyrics is the better route.

**On screen:**  
`SunoL3LyricsEditor` — Song Editor Lyrics tab  
- Suno Song Editor interface (dark, full-width)  
- Tabs visible at top: **Lyrics · Arrangement · Mix** (Lyrics tab active, terracotta underline)  
- Lyrics panel shows structured text:  
  ```
  [Verse 1]
  The cat sat on the mat
  The bat flew with a pat
  
  [Chorus]
  A, A, the short A sound
  A, A, it's all around
  ```
- A cursor edits one word in the verse  
- A **"Regenerate Vocals"** button appears, highlighted  
- Callout arrows:  
  - On the lyrics: *"Edit any word or line here"*  
  - On Regenerate Vocals: *"Regenerates only the singing — instruments stay unchanged"*  
- Bottom annotation: *"Melody stays. Only the words change."*  
- Spark line: **✦ Fix the words. Keep the melody.**

---

### B05 — Writing Your Own Lyrics

**Narration:**

> If you need a song to use specific words — vocabulary terms a phonics lesson requires, a repeated phrase that reinforces a concept, a specific sentence structure — Custom mode is how you put those exact words into the song. Before you go into Suno, write your lyrics in any text editor. Structure them as simple verse-chorus patterns. Keep each line short — eight words or fewer is a good target for children. Avoid words with three or more syllables if your audience is 5 to 7 years old. A simple chorus that repeats the key learning point is almost always more effective than complex or varied lyrics. Once you have your text, paste it into the Lyrics field in Custom mode and generate.

**On screen:**  
`SunoL3CustomLyrics` — lyrics writing guide  
- Two-panel illustration, cream stage:  

  LEFT panel — "Write first":  
  - A simple text document showing a lyric structure:  
    ```
    [Verse]
    The cat sat on the mat
    Pat had a bat and a hat
    
    [Chorus]
    Short A, short A, it's the sound of the day
    Short A, short A, let's learn it and play
    ```  
  - Annotation checks: ✓ *"Short lines (≤8 words)"*, ✓ *"Simple words"*, ✓ *"Repeating chorus"*, ✓ *"Key concept in chorus"*  

  RIGHT panel — "Then paste":  
  - The Suno Custom mode Lyrics field with the text pasted in  
  - The Style field showing: *"upbeat children's folk-pop, ukulele, hand claps"*  
  - Create button visible  

- Spark line: **✦ Write it first. Then paste.**

---

### B06 — The Song Editor

**Narration:**

> The Song Editor is where you assemble multiple clips into a complete track. Here's a typical workflow. You generate a clip — the opening verse and intro. You extend it once to get a chorus. You extend again to get a second verse and a closing chorus. Then you open the Song Editor to see all your clips arranged on a timeline. You can trim clips at the end, reorder sections, and add a brief silence between sections. For most Lyrical Literacy projects, you won't need complicated editing. A simple linear arrangement — intro, verse, chorus, verse, chorus, outro — is usually enough. The Song Editor gives you the space to confirm that structure and make small adjustments before you export.

**On screen:**  
`SunoL3SongEditor` — Song Editor timeline  
- Suno Song Editor interface showing a horizontal timeline  
- Multiple clip blocks arranged left to right, each a different shade of the same dark:  
  - Block 1: **Intro** (8s)  
  - Block 2: **Verse 1** (24s)  
  - Block 3: **Chorus** (16s)  
  - Block 4: **Verse 2** (24s)  
  - Block 5: **Chorus** (16s)  
  - Block 6: **Outro** (10s)  
- A cursor trims the end of Block 5 (the chorus is slightly too long)  
- Callout annotations:  
  - On the timeline ruler: *"Total length: 1 min 38s"*  
  - On the trim cursor: *"Trim to tighten a section"*  
  - Above the arrangement: *"Simple linear structure works for most educational songs"*  
- Below: *"Assemble in order. Trim for length. Export when it sounds right."*  
- Spark line: **✦ Arrange. Trim. Export.**

---

### B07 — Downloading

**Narration:**

> When your song is ready, download it. From the Library or from inside the Song Editor, find the download icon — it looks like a downward arrow. Click it and choose your format. For audio-only projects, choose MP3. For anything where you want Suno's auto-generated artwork combined with the audio in a video file — for a presentation or a social post — choose video. The MP3 quality Suno exports is clean and more than sufficient for educational contexts. Save the file right away to a folder you can find again. Your Downloads folder fills up fast on this workflow.

**On screen:**  
`SunoL3Download` — download flow  
- Suno Library view showing a song card  
- Download icon (downward arrow) highlighted in terracotta  
- A small dropdown appears with two options:  
  - **MP3** (highlighted) — label: *"Audio only. Best for most projects."*  
  - **Video** — label: *"Audio + generated artwork. Good for presentations."*  
- An arrow from the dropdown points to a file system view showing the saved file:  
  - File named: `lyrical-literacy-short-a-folk-v1.mp3`  
- Callout: *"Save to a clearly named folder right away."*  
- Bottom annotation: *"MP3 for educational use. Video only if you need the artwork."*  
- Spark line: **✦ Download MP3. Save immediately.**

---

### B08 — File Workflow for the Team

**Narration:**

> A few habits that will save you and your teammates significant time. When you save a file, name it descriptively. "lyrical-literacy-short-a-folk-v2.mp3" tells you everything. "suno-export-3.mp3" tells you nothing in three months. Keep a prompt log — a shared document or a note in your project folder — recording the Suno prompt you used for each song. If a song gets removed from your Suno library, having the prompt means you can regenerate it. Suno's free and Pro tiers have storage limits — things do get removed. Share files with your team through Google Drive or the shared channel your team uses, not by email attachments, which creates version confusion. One final habit: name your versions clearly — v1, v2, final — so you and your teammates never work on the wrong file.

**On screen:**  
`SunoL3FileWorkflow` — file workflow illustration  
- Two columns side by side, cream stage:  

  LEFT — **Messy workflow** (red border on column):  
  - Filenames: `suno-export-3.mp3`, `untitled.mp3`, `song(2).mp3`  
  - No prompt log visible  
  - Multiple email attachments shown  
  - Label: *"Which file is the final version?"*  

  RIGHT — **Clean workflow** (green border on column):  
  - Filenames: `lyrical-literacy-short-a-folk-v1.mp3`, `lyrical-literacy-short-a-folk-v2-final.mp3`  
  - Prompt log document visible with entries  
  - Google Drive folder icon  
  - Check marks on: descriptive names · prompt log · shared folder · version numbering  
  - Label: *"Three months later, you still know what everything is."*  

- Spark line: **✦ Prompt log. Descriptive names. Shared folder.**

---

### BVDT — Verdict

**Narration:**

> Here's the complete Part 3 picture. After you generate your first clip, spend two minutes listening before you extend or edit anything — check mood, vocals, melody simplicity, and structure. Use the Extend feature to grow the clip to 2 to 4 minutes. Edit lyrics in the Lyrics tab if small word-level fixes are needed — this only changes the words, not the melody. Use Custom mode if you need your exact vocabulary in the song. Use the Song Editor to arrange clips into a complete track and trim for length. Download as MP3 for audio-only projects. Name files descriptively, keep a prompt log, and share through a shared folder. That is the complete Suno workflow from first generation to finished, team-ready file.

**On screen:**  
`ClaudeVerdictArtifact`  
- Title: *"Suno, Part Three."*  
- Heading: *"The complete workflow"*  
- Four lines:  
  1. *"Listen critically first — mood, vocal clarity, melody simplicity, and structure."*  
  2. *"Extend to 2–4 minutes. Edit lyrics in the Lyrics tab (words only, melody unchanged)."*  
  3. *"Use the Song Editor to arrange sections and trim. Download as MP3."*  
  4. *"Prompt log + descriptive file names + shared folder = no lost work, no confusion."*

---

### BHTF — Your Turn

**Narration:**

> Your turn. Here's the prompt — read it with me. "I have a Suno clip that is 1 minute and 20 seconds long — a phonics song for 6 to 7-year-olds about the letter B. I need it to be about 3 minutes, with a clear verse-chorus structure. Write me a step-by-step plan for extending it in Suno and then assembling it in the Song Editor." This is worth planning before you start clicking — because extending in the wrong order produces an incoherent structure. Let Claude sketch the plan first. Then execute in Suno.

**On screen:**  
`ClaudeComposerAsk`  
- Greeting: *"Your turn."*  
- Command: *"I have a Suno clip that is 1 minute and 20 seconds long — a phonics song for 6 to 7-year-olds about the letter B. I need it to be about 3 minutes with a clear verse-chorus structure. Write me a step-by-step plan for extending it in Suno and assembling it in the Song Editor."*  
- Running text: *"paste this into Claude…"*

---

### BOUT — Outro

**Narration:** *"Suno, Part Three."*

**On screen:**  
`ClaudeTitleOutro`  
- Title: *"Suno, Part Three."*  
- Handle: *"@HumanitariansAI"*  
- Subline: *"Lyrical Literacy Tutorial Series"*

---
---

# Scenes Required — Build List

## Part 2 — New Scenes (8)

| Scene ID | Beat | What it shows | Key animation |
|----------|------|---------------|---------------|
| `SunoL2Bluf` | B01 | Split-screen: weak vs strong prompt comparison | Left/right panels slide in |
| `SunoL2PromptComparison` | B02 | Two prompts side by side, strong prompt annotated with 4 arrows | Annotation arrows draw on |
| `SunoL2StyleGuide` | B03 | Animated genre vocabulary grid (8 cards) + combination examples | Cards enter by group |
| `SunoL2MoodGuide` | B04 | Two-axis mood spectrum with words plotted by position | Words appear at grid positions |
| `SunoL2TopicZoom` | B05 | Zoom lens metaphor: 3 zoom levels, prompt text sharpens | Slider moves, text sharpens |
| `SunoL2Iteration` | B06 | 3 prompt cards building vertically with annotations between | Card 1 → annotate → card 2 → annotate → card 3 |
| `SunoL2CustomMode` | B07 | Suno Create page: Simple → Custom tab switch, new fields revealed | Tab switch animation, callouts |
| `SunoL2TagSystem` | B08 | Custom mode Style field, tags appear as chips with tooltips | Tags type in one by one |
| `SunoL2LLPrompt` | B09 | 4-layer prompt assembly (style/mood/topic/production note) | Layers stack, merge into final prompt |

## Part 3 — New Scenes (8)

| Scene ID | Beat | What it shows | Key animation |
|----------|------|---------------|---------------|
| `SunoL3Bluf` | B01 | Pipeline: generated clip → extended track → downloaded file | Three nodes, left to right |
| `SunoL3ListenGuide` | B02 | Annotated waveform with section markers + 4 listening questions | Markers appear, questions appear, checkmarks |
| `SunoL3ExtendFlow` | B03 | Suno Library card + 3-dot menu + extend animation, waveform grows | Waveform extends right, duration updates |
| `SunoL3LyricsEditor` | B04 | Suno Song Editor Lyrics tab with editable lyrics + Regenerate Vocals button | Cursor edits text, button highlights |
| `SunoL3CustomLyrics` | B05 | Two-panel: write lyrics in text editor LEFT, paste into Custom mode RIGHT | Left panel builds, arrow, right panel fills |
| `SunoL3SongEditor` | B06 | Song Editor timeline with 6 labeled clip blocks + trim cursor | Blocks appear, cursor trims |
| `SunoL3Download` | B07 | Library card → download icon → format dropdown → saved file | Click animation, dropdown, file appears |
| `SunoL3FileWorkflow` | B08 | Two-column comparison: messy vs clean file workflow | Red vs green borders, check marks on right |

---

# What to Do Next

1. **Review this document** — confirm narration tone, visual descriptions, and beat structure match what you want before any scenes are built
2. **Generate audio first** — run `generate_audio_kokoro.py` on the Part 2 and Part 3 beat sheets; real durations become the master clock
3. **Build Part 2 scenes** — 9 new Remotion components
4. **Build Part 3 scenes** — 8 new Remotion components
5. **Compile previz** — Part 2 and Part 3 slate cuts for review
6. **Visual QC** — frame-level review per `CLAUDE-CODE-VISUAL-QC-CHECK.md`
