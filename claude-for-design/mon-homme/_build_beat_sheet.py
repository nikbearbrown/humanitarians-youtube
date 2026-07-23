#!/usr/bin/env python3
"""Assemble mon-homme/beat_sheet.json from beat_data.json + forced-aligned
lyrics.json + authored scene prompts. Vocal beats = Tuzi (random plate),
instrumental beats = Paris b-roll (random plate). Lyric TEXT is verbatim
(drives the overlay); image prompts are softened/abstracted."""
import json, random, os
random.seed(42)

bd = json.load(open("beat_data.json"))
ly = {l["index"]: l for l in json.load(open("lyrics.json"))["lines"]}
sk = json.load(open("_beat_skeleton.json"))
fps = bd["fps"]

TUZI_N = len([f for f in os.listdir("references/characters/tuzi") if f.endswith(".png")])
PARIS_N = len([f for f in os.listdir("references/locations/paris") if f.endswith(".png")])
tuzi_pool = random.sample(range(1, TUZI_N + 1), TUZI_N)
paris_pool = random.sample(range(1, PARIS_N + 1), PARIS_N)
def tref(): return f"references/characters/tuzi/tuzi-{tuzi_pool.pop():03d}.png"
def pref(): return f"references/locations/paris/paris-{paris_pool.pop():03d}.png"

GLOSS = {
 0:"On this earth",1:"my only joy, my only happiness",2:"is my man",3:"I gave all that I have",
 4:"my love and all my heart",5:"to my man",6:"And even at night",7:"when I dream, it's of him",
 8:"of my man",9:"It's not that he's handsome",10:"nor rich nor strong",11:"but I love him, it's idiotic",
 12:"He knocks me about",13:"he takes my money",14:"I'm at the end of my rope",15:"but in spite of it all",
 16:"what do you expect",17:"I've got him so under my skin",18:"that I'm crazy for it",
 19:"the moment he comes near, it's over",20:"I'm his",21:"when his eyes settle on me",
 22:"it undoes me completely",23:"I've got him so under my skin",24:"that at the slightest word",
 25:"I'd do anything",26:"for him, for me",27:"for a smile, for a glance",28:"for a kiss sometimes",
 29:"I'd give all that I have",30:"all my joy, all my happiness",31:"to my man",
 32:"and if one day he leaves me",33:"I think I would die of it",34:"to my man"}

PROMPTS = {
"B01":("extreme wide, Paris rooftops and zinc chimneys under a pale overcast dawn, the Eiffel Tower distant in haze, cold charcoal monochrome, slow aerial drift",
       "wide, an empty cobbled Parisian street at first light, wet stone reflecting a single streetlamp, deep shadow, slow push-in down the street"),
"B02":("medium wide, a deserted boulevard with bare plane trees, one warm-lit cafe window far off, sepia and rust tones, slow push-in toward the light",
       "low-angle, an ornate wrought-iron lamppost against a bright blown-out sky, high-contrast black and white, slow tilt up"),
"B03":("medium close-up, the woman alone on a Paris street, eyes lowering then lifting to the horizon, soft overcast side-light, warm rust accent against grey stone, slow push-in",
       "wide, the woman small against a long empty boulevard, holding still, flat silver daylight, a single warm window glowing behind her, static"),
"B04":("close-up, the woman half-turned with a private inward look that softens, window light from camera-left, amber rim on her cheek, deep shadow on the far side, slow drift",
       "medium, the woman walking slowly toward camera through a misty street, the faint beginning of a smile, cool grey light, slow push-in"),
"B05":("extreme close-up, the woman's hand pressing flat to her chest, breath held, warm low light grazing her knuckles, rust and cream palette, micro push-in",
       "close-up, the woman's face lifted with eyes briefly closing as if offering herself up, a warm rim against deep shadow, very slow push-in"),
"B06":("close-up, the woman lying back with eyes half-closed as if dreaming, warm lamplight pooling on one side of her face, deep night-blue shadow, very slow push-in",
       "medium, the woman at a dark window, city lights in bokeh behind the glass, her faint reflection over them, warm interior glow, slow drift"),
"B07":("close-up, the woman with a wry resigned half-smile and a small shake of the head, soft side light, amber and charcoal, handheld micro-drift",
       "medium, the woman leaning against a stone wall, arms loosely crossed, a knowing look downward, flat daylight, rust against grey, static"),
"B08":("medium, the woman alone against a cold stone wall, arms wrapped around herself, face turned from a hard sliver of side-light, bruise-blue shadow, then a small helpless lift of the eyes, slow push-in",
       "close-up, the woman's downcast eyes with a single bright catchlight, exhaustion settling into a faint resigned shrug, low underexposed light, desaturated, static"),
"B09":("close-up, the woman's gaze sharpening as if drawn toward someone unseen, light shifting soft-to-hard, a warm rim, slow push-in",
       "medium close-up, the woman turning toward something off-frame, breath caught, hair just beginning to move, hard side light, a blur at the edge, whip-pan settling"),
"B10":("extreme close-up, the woman's eyes lifting to meet an unseen gaze, catchlight blooming, warm soft light, rust and cream, micro push-in",
       "close-up, the woman's composure dissolving into a soft, overwhelmed expression, warm diffuse light, shallow focus, slow drift"),
"B11":("medium, the woman stepping forward with quiet resolve, chin lifting, soft directional light, warm rust against grey, slow push-in",
       "close-up, the woman's determined eyes with a faint sheen of tears, hard key light, static"),
"B12":("close-up, the woman's faint yearning smile, eyes soft and far away, warm low light, amber palette, very slow push-in",
       "medium, the woman reaching a hand toward a blurred warm light off-frame, shallow focus, sepia, slow drift"),
"B13":("low-angle, an ornate black wrought-iron street lamp and balcony railings against a blown-out white sky, high-contrast monochrome, slow tilt",
       "detail, rain beading on an old Parisian window pane, blurred amber light beyond, abstract bokeh, static"),
"B14":("medium close-up, the woman opening her hands slightly as if giving herself over, warm light pooling in her palms, rust and cream, slow push-in",
       "close-up, the woman's face lifted, eyes closed in surrender, a warm rim against deep shadow, static"),
"B15":("extreme close-up, the woman's face crumpling as a single tear breaks free, dim warm light, deep shadow swallowing the edges, an almost imperceptible push-in",
       "close-up, the woman's brimming eyes holding the camera's gaze, one warm catchlight against black, static"),
"B16":("close-up, the woman stills after the last word, a fragile calm settling, warm light dimming, sepia, slow pull-back",
       "medium, the woman alone on the empty street as the light fades around her, small and resolute, static"),
"B17":("wide, a figure walking away into vanishing fog at the end of a long Parisian street, growing smaller, cold grey, slow pull-back",
       "medium, an empty park bench under bare trees with fallen leaves, flat winter light, desaturated, static hold"),
"B18":("wide, a rain-slick empty boulevard at dusk, blurred distant headlights, neon smearing on wet stone, cold blue with a single rust glow, slow handheld drift",
       "medium, an empty doorway and a worn stone stair in shadow, one shaft of pale light falling across it, charcoal monochrome, static hold"),
"B19":("extreme wide, the empty Parisian street at dusk, one streetlamp flickering on, the Eiffel Tower distant in mist, charcoal and amber, slow pull-back to black",
       "aerial, Paris dissolving into evening fog, lights coming on one by one, monochrome, slow drift fading out"),
}

# enforce contiguous tiling so the assembled video has no gaps:
# each beat ends where the next begins; first starts at 0, last ends at song end.
for i in range(len(sk) - 1):
    sk[i]["end"] = sk[i + 1]["start"]
sk[0]["start"] = 0
sk[-1]["end"] = bd["durationInFrames"]

beats = []
for i, b in enumerate(sk):
    bid = f"B{i+1:02d}"
    start, end = b["start"], b["end"]
    dur = round((end - start) / fps, 2)
    subject = "paris" if b["kind"] == "instrumental" else "tuzi"
    lyric = " / ".join(ly[x]["text"] for x in b["lines"]) if b["lines"] else ""
    gloss = " / ".join(GLOSS.get(x, "") for x in b["lines"]) if b["lines"] else ""
    pa, pb = PROMPTS[bid]
    ref = tref() if subject == "tuzi" else pref()
    cam = pa.split(",")[-1].strip()
    beats.append({
        "beat_id": bid,
        "start_s": round(start / fps, 2), "end_s": round(end / fps, 2),
        "start_frame": start, "end_frame": end, "duration_s": dur,
        "section": next((s["label"] for s in bd["sections"] if s["startFrame"] <= start < s["endFrame"]), bd["sections"][-1]["label"]),
        "kind": b["kind"],
        "subject": subject,
        "line_indices": b["lines"],
        "lyric_text": lyric,
        "lyric_gloss_en": gloss,
        "character_ref": ref if subject == "tuzi" else None,
        "location_ref": ref if subject == "paris" else None,
        "image_prompt": pa,
        "storyboard_prompts": [pa, pb],
        "camera": cam,
        "video_prompt": f"{pa}. Subtle natural motion only; hold so it cuts cleanly to the beat; duration {dur}s.",
        "clip_tier": 6 if dur <= 6 else 10,
        "images_per_beat": 2,
        "storyboard_candidates": [],
        "chosen_still": None,
        "raw_clip": None,
        "video_file": None,
    })

sheet = {
  "metadata": {
    "slug": "mon-homme", "title": "Mon Homme", "artist": "Tuzi Brown",
    "aspect_ratio": "16:9", "fps": fps,
    "duration_s": bd["durationInSeconds"], "duration_frames": bd["durationInFrames"],
    "bpm": bd["bpm"], "key": f'{bd["features"]["key"]} {bd["features"]["mode"]}',
    "audio_file": "MonHommeTuziGD-mastered.wav", "lyrics_file": "song-05.txt",
    "beat_data": "beat_data.json", "lyrics_timing": "lyrics.json",
    "timing_source": "librosa beat grid + faster-whisper forced alignment (word-level)",
    "language": "fr", "style_preset": "mon-homme-editorial",
    "style_bible": {
      "visual_style": "moody cinematic fashion-editorial photography, Parisian; warm sepia-and-rust tones with deep shadow, intercut with high-contrast charcoal monochrome; shallow depth of field, 35mm film grain, soft motivated available light, gentle vignette",
      "color_palette": "rust and amber, cream, charcoal black, desaturated stone-grey",
      "lighting_style": "soft directional low light and dramatic chiaroscuro; overcast Parisian daylight outdoors, warm interior lamp-glow at night"
    },
    "style_suffix": "moody cinematic editorial photography, Parisian, sepia-and-rust with charcoal monochrome accents, shallow depth of field, 35mm film grain, soft chiaroscuro, no text, no captions, no watermark",
    "characters": [
      {"name": "Tuzi", "ref_key": "tuzi", "driver": "reference",
       "reference_dir": "references/characters/tuzi", "reference_count": TUZI_N,
       "look": "a beautiful young woman; identity locked by the Tuzi reference plates (a randomly drawn plate per beat), two wardrobe modes — a warm rust top in the streets and a high-contrast braided/pearled editorial look"}
    ],
    "locations": [
      {"name": "Paris", "ref_key": "paris", "driver": "reference",
       "reference_dir": "references/locations/paris", "reference_count": PARIS_N,
       "look": "Parisian b-roll — rooftops, the Eiffel Tower, empty boulevards, ornate wrought-iron lampposts, wet stone, mist; high-contrast monochrome and sepia"}
    ],
    "generation": {
      "still_backend": "TBD (Higgsfield FLUX.2 multi-ref or Midjourney)",
      "images_per_beat": 2, "video_model": "minimax (image-to-video)",
      "rule": "image_prompt is a visual scene only — never the lyric text; identity/look comes from the assigned reference plate. Cut each generated clip to its beat duration."
    },
    "counts": {"beats": len(beats),
               "tuzi_beats": sum(1 for x in beats if x["subject"] == "tuzi"),
               "paris_beats": sum(1 for x in beats if x["subject"] == "paris")}
  },
  "beats": beats
}
json.dump(sheet, open("beat_sheet.json", "w"), ensure_ascii=False, indent=2)
print("wrote beat_sheet.json | beats:", len(beats),
      "| tuzi:", sheet["metadata"]["counts"]["tuzi_beats"],
      "| paris:", sheet["metadata"]["counts"]["paris_beats"])
print("max beat dur:", max(b["duration_s"] for b in beats), "s")
over = [(b["beat_id"], b["duration_s"]) for b in beats if b["duration_s"] > 8.05]
print("beats over 8s (within 10s clip tier):", over or "none")
assert all(b["duration_s"] <= 10.0 for b in beats)
# coverage check: beats must tile 0..duration with no gaps/overlaps
prev = 0
for b in beats:
    assert b["start_frame"] == prev, f"gap/overlap at {b['beat_id']}: {prev} vs {b['start_frame']}"
    prev = b["end_frame"]
print("coverage 0..%d frames contiguous: OK (ends at %d / %d)" % (bd["durationInFrames"], prev, bd["durationInFrames"]))
