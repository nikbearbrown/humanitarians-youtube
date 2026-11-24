# Writes beat_sheet.json (9:16, 2160x3840) for the Short of "Why Did the AI Say No?" -- Boopesh M.
# A separate native-portrait reel, not a crop. Numbers from ../code/results.json (synthetic applicants).
import json
from pathlib import Path

VOICE = "am_onyx"
HAI = "@HumanitariansAI"
RES = json.loads((Path(__file__).resolve().parent.parent / "code" / "results.json").read_text())
A = RES["applicant_a"]
R = RES["reasons"]
CF = RES["counterfactual"]
assert round(A["risk_scorecard"] * 100) == 53 and round(A["risk_boosted"] * 100) == 34
assert R["scorecard"]["top3"] == ["dti", "util", "missed"] and R["agreement"]["n_shared"] == 2
assert R["boosted"]["model_runs"] == 16_000 and CF["both_approve_paydown"] == 3850


def manim(cls):
    return {"type": "GRAPHIC", "source": "manim", "motion": "fade",
            "manim": {"scene_class": cls, "file": "scenes.py"}}


def beat(bid, act, note, text, shot, **kw):
    b = {"beat_id": bid, "act": act, "role_note": note, "narration_text": text,
         "shot": shot, "voice": VOICE, "engine": "kokoro", "voice_kokoro": VOICE}
    b.update(kw)
    return b


beats = [
  beat("B00", "INTRO", "required fellow intro line + AI-voice disclosure (portrait composer)",
       "Hi, I am Boopesh M., and this video is about why an AI said no to a loan. Heads up: this is an AI voice "
       "reading my script, and the results come from my own small experiment, on synthetic applicants.",
       {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
        "remotion": {"pattern": "ClaudeComposerAsk916", "props": {
            "greeting": "Hi, Boopesh", "topic": "Irreducibly Human", "segment": "AI in Finance",
            "command": "When an AI credit model denies a loan, how do you find the specific reasons?",
            "runningText": "explaining the decision…", "folderLabel": HAI,
            "modelLabel": "Claude", "effortLabel": "High",
            "output": ["synthetic applicants, 5 plain features",
                       "two models deny Applicant A; they share 2 of 3 reasons"]},
            "rendered": {"out": "", "at": ""}}}),
  beat("B10", "THE RULE + APPLICANT A", "Reg B: specific reasons; A denied by both models (53 % / 34 % vs 30 %)",
       "US lending rules say a denial needs specific reasons. The model said no doesn't count. "
       "My made-up Applicant A is denied by two models: a simple scorecard, and a black box.",
       manim("B10_Denied")),
  beat("B20", "THE REASONS", "top 3 per model; 2 of 3 shared; 16,000 model runs",
       "The scorecard's reasons are exact: debt-to-income, card use, a missed payment. "
       "The black box needs sixteen thousand model runs to answer, and shares only two of three.",
       manim("B20_Reasons")),
  beat("B30", "WHAT WOULD CHANGE IT", "pay cards down $3,850 -> both approve; limits",
       "What would flip it? Pay card balances down by about three thousand eight hundred dollars, and both models "
       "say yes. That's a reason a person can act on.",
       manim("B30_Change")),
  beat("B90", "OUTRO", "HAI outro + fellow credit",
       "Why did the AI say no? With Boopesh M., for Humanitarians AI.",
       manim("B90_Outro"), lead_silence_s=0.3),
]

sheet = {
  "metadata": {
    "title": "Why Did the AI Say No? (Short)",
    "slug": "why-did-the-ai-say-no-short",
    "topic": "Irreducibly Human",
    "register": "Plain / Teardown-warm",
    "audience": "Humanitarians AI",
    "brand": "claude-hai",
    "channel_title": "",
    "creator": "Boopesh M.",
    "engine": "kokoro",
    "palette": "claude",
    "style_preset": "claude",
    "style": "claude-explainer",
    "voice_kokoro": VOICE,
    "voice_policy": "persistent-fellow-selected",
    "aspect_ratio": "9:16",
    "pronounce": {"Kokoro": "kˈoʊkəɹoʊ", "Boopesh": "bˈuːpɛʃ", "Shapley": "ʃˈæpli"},
    "brutalist_commit": "a99b5323",
    "parent": "../beat_sheet.json",
    "note": "Native 9:16 Short of 'Why Did the AI Say No?'. Same facts (../FACTCHECK.md), own layout. "
            "Not legal advice.",
    "tags": ["Humanitarians AI", "explainable AI", "AI in finance", "credit scoring", "Shorts"],
  },
  "beats": beats,
}
out = Path(__file__).with_name("beat_sheet.json")
if out.exists():
    old = json.loads(out.read_text())
    for k in ("approvals", "build"):
        if k in old.get("metadata", {}):
            sheet["metadata"][k] = old["metadata"][k]
    prev = {b["beat_id"]: b for b in old.get("beats", [])}
    for b in beats:
        o = prev.get(b["beat_id"])
        if o and o.get("narration_text") == b["narration_text"]:
            for k in ("actual_duration_s", "audio_file", "render_duration_s", "build"):
                if k in o:
                    b[k] = o[k]
            if (o.get("shot", {}).get("remotion") or {}).get("rendered") and \
                    o["shot"]["remotion"]["props"] == b["shot"]["remotion"]["props"]:
                b["shot"]["remotion"]["rendered"] = o["shot"]["remotion"]["rendered"]
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print("wrote", out, len(beats), "beats", sum(len(b["narration_text"].split()) for b in beats), "words")
