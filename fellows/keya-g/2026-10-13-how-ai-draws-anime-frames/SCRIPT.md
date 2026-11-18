# How AI Draws Anime Frames — Script

**Fellow:** Keya G. · **Week 1** · **Voice:** Kokoro `af_bella` · **Pronounce:** Keya = kˈeɪjɛə ("Kay-Yeah")

Story plan, topic research and decisions: Keya. Example script drafted with Claude from Keya's story plan; Keya approved it and chose the Naruto examples.
Visuals use simple illustrative shapes only — no frames or characters from Naruto or any real anime. The named fights are examples of a kind of movement, not claims about how those scenes were animated.

## 1. Intro
Hi, I am Keya and this video is about how AI draws the frames between an animator's drawings, and why it should be a helping hand, not a replacement. The voice you're hearing is an AI voice reading my script.

## 2. Hook
Fans often say AI-smoothed anime looks unnatural. Yet in 2025, Toei, the studio behind One Piece, said it expects to use AI to draw in-between frames. So if AI drew your favourite anime on its own, would you still love it the same way?
`[Anime Corner]`

## 3. Overview
On screen, typed then corrected: "AI will replace animators." → "AI can be the animator's helping hand: it draws the in-betweens, but only the animator decides the timing."

AI can be the animator's helping hand. It can draw the in-betweens, but only the animator decides the timing. Let's see why.

## 4. Anime and key frames
Anime is hand-drawn animation, and every scene starts with key frames. A key animator draws the most important poses, like Rock Lee launching his kick at Gaara, and the moment it lands. Then in-between artists draw the frames that connect them. Those in-betweens are exactly the drawings AI is being asked to make.
`[Wikipedia: Inbetweening]`

## 5. Ones, twos, threes
Video plays at twenty-four frames a second, but anime rarely draws all twenty-four. Most of it is drawn on twos or threes: each drawing is held for two or three frames, so just twelve or eight drawings a second. Fast action, like a punch, can be drawn on ones. These holds are a choice, about budget and about feel.
`[Wikipedia: Inbetweening; AnimeInterp]`

## 6. How AI fills the gap
So how does AI make a new frame? First it calculates optical flow: a map of arrows showing where each pixel moved from one frame to the next. Then it follows those arrows halfway and draws the frame in the middle. On live-action video, full of texture and small movements, this works surprisingly well.
`[RIFE; AnimeInterp]`

## 7. Why anime breaks it
Anime breaks it in three ways. Flat colors: a sleeve painted one solid color has no texture, so the AI can't tell which pixel went where. Big movement: think of Naruto and Sasuke's final fight. Between two drawings, a fist can fly halfway across the screen along a curve. And hidden parts: a hand that slips behind the body has nothing to match. The result is ghosting, blur, even extra limbs.
`[AnimeInterp; Kreinin 2024]`

## 8. Fans vs. 60 fps
That's why many fans and animators dislike 60 fps AI edits. Smoothing every frame wipes out the timing the animator chose. One critic called the result lifeless. As a fan, I agree. A little AI here and there is fine, but a whole anime smoothed this way looks unnatural to me.
`[A.V. Club; uhighmidway]`

## 9. AI built for anime
Researchers are now building AI for anime itself. One 2021 project, AnimeInterp, built a dataset of twelve thousand sets of anime frames, and its model matches the flat color shapes between two drawings before it guesses the motion. Tools like this could take repetitive in-betweens off an animator's desk, with the animator still checking every frame.
`[AnimeInterp; Kreinin 2024]`

## 10. Verdict
So, can AI draw anime frames? It can draw the in-betweens. But it struggles with flat colors, big movement and hidden parts, and it can't choose the timing. That choice is where the feeling lives. AI should be the animator's helping hand, not their replacement.

## 11. Your turn
Your turn. Paste this into Claude: I'm an anime fan, not an animator. Using a scene from my favourite anime, explain like I'm twelve how an animator decides which drawings to make and how long to hold each one. Then tell me which parts AI could safely help with, and which should stay hand-drawn. And next time an animation amazes you, look up how it was made, frame by frame. You'll never watch it the same way.

Prompt shown on screen: "I'm an anime fan, not an animator. Using a scene from [my favourite anime], explain like I'm 12 how an animator decides which drawings to make and how long to hold each one. Then tell me which parts AI could safely help with, and which should stay hand-drawn."

## 12. Outro
How AI Draws Anime Frames. Built with Claude, for Humanitarians AI.

## Sources
- Li Siyao et al., "Deep Animation Video Interpolation in the Wild" (AnimeInterp), CVPR 2021 — https://arxiv.org/abs/2104.02495
- Yossi Kreinin, "The state of AI for hand-drawn animation inbetweening", 2024 — https://yosefk.com/blog/the-state-of-ai-for-hand-drawn-animation-inbetweening.html
- Wikipedia, "Inbetweening" — https://en.wikipedia.org/wiki/Inbetweening
- Huang et al., "RIFE: Real-Time Intermediate Flow Estimation for Video Frame Interpolation" — https://arxiv.org/abs/2011.06294
- Anime Corner, "Toei Animation Responds After Backlash to AI Plans", May 19 2025 — https://animecorner.me/toei-animation-ai-backlash-denies/
- Elijah Gonzalez, The A.V. Club, Nov 5 2025 — https://www.avclub.com/ai-brained-sickos-who-upscale-anime-to-60-fps-need-to-be-stopped
- "Stop AI interpolation", uhighmidway (student opinion) — https://uhighmidway.com/19415/opinion/stop-ai-interpolation-people-should-listen-to-animators-and-authentic-animation/
