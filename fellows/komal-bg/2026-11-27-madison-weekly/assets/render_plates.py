#!/usr/bin/env python3
"""Claude-palette teaching plates for Madison Weekly — Nov 27. 16:9 and 9:16."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

PAGE, INK, SOFT, SPARK, BORDER = "#FAF9F5", "#3D3929", "#73705F", "#D97757", "#E5E2D9"
ART = Path("/Users/komalganapathy/Desktop/brutalist.art/runtime/fonts/EB_Garamond/static")
SERIF = str(ART / "EBGaramond-Medium.ttf")
SERIF_I = str(ART / "EBGaramond-Italic.ttf")
SANS = "/System/Library/Fonts/Avenir Next.ttc"
OUT = Path(__file__).resolve().parents[1]


def font(path, size, index=0):
    try:
        return ImageFont.truetype(path, size, index=index)
    except OSError:
        return ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", size)


def text(draw, xy, s, f, fill=INK, anchor="lt"):
    draw.text(xy, s, font=f, fill=fill, anchor=anchor)


def plate(w, h):
    im = Image.new("RGB", (w, h), PAGE)
    d = ImageDraw.Draw(im)
    return im, d


def header(d, w, y, kicker, title, sub, sizes):
    fk, ft, fs = (font(SANS, sizes[0], 1), font(SERIF, sizes[1]), font(SERIF, sizes[2]))
    text(d, (w * 0.08, y), kicker.upper(), fk, SOFT)
    text(d, (w * 0.08, y + sizes[0] * 1.8), title, ft, INK)
    text(d, (w * 0.08, y + sizes[0] * 1.8 + sizes[1] * 1.15), sub, fs, SOFT)
    return y + sizes[0] * 1.8 + sizes[1] * 1.15 + sizes[2] * 1.6


def footer(d, w, h, source, falsifier, sizes):
    ff, fi = font(SANS, sizes[0], 1), font(SERIF_I, sizes[1])
    d.line((w * 0.08, h * 0.90, w * 0.92, h * 0.90), fill=BORDER, width=3)
    text(d, (w * 0.08, h * 0.925), source, ff, SOFT)
    text(d, (w * 0.08, h * 0.96), falsifier, fi, SPARK)


def wrap(d, xy, s, f, fill, max_w, line_h, anchor="lt"):
    words = s.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    x, y = xy
    for i, line in enumerate(lines):
        text(d, (x, y + i * line_h), line, f, fill, anchor)
    return len(lines)


def two_cards(path, w, h, kicker, title, sub, left, right, source, falsifier, accent="right"):
    """left/right: (kicker, heading, body). Drawn cards, not photographs."""
    im, d = plate(w, h)
    portrait = h > w
    unit = w if portrait else h
    s = (int(unit * (0.032 if portrait else 0.018)),
         int(unit * (0.070 if portrait else 0.055)),
         int(unit * (0.034 if portrait else 0.028)))
    top = header(d, w, h * (0.055 if portrait else 0.07), kicker, title, sub, s)
    fl = font(SANS, int(unit * (0.028 if portrait else 0.018)), 1)
    fh = font(SERIF, int(unit * (0.048 if portrait else 0.042)))
    fb = font(SERIF, int(unit * (0.032 if portrait else 0.026)))
    pad = w * 0.08
    gap = w * 0.03
    if portrait:
        card_w = w - 2 * pad
        avail = h * 0.88 - top
        card_h = (avail - gap) / 2
        boxes = [(pad, top + h * 0.01, pad + card_w, top + h * 0.01 + card_h),
                 (pad, top + h * 0.01 + card_h + gap, pad + card_w, top + h * 0.01 + 2 * card_h + gap)]
    else:
        card_w = (w - 2 * pad - gap) / 2
        card_h = h * 0.82 - top
        y0 = top + h * 0.02
        boxes = [(pad, y0, pad + card_w, y0 + card_h),
                 (pad + card_w + gap, y0, pad + 2 * card_w + gap, y0 + card_h)]
    cards = (left, right)
    for i, ((x0, y0, x1, y1), card) in enumerate(zip(boxes, cards)):
        ink = SPARK if (accent == "right" and i == 1) or (accent == "left" and i == 0) else INK
        d.rounded_rectangle([x0, y0, x1, y1], radius=int(unit * 0.012), outline=BORDER, width=4)
        d.rectangle([x0, y0, x0 + 10, y1], fill=ink)
        text(d, (x0 + w * 0.03, y0 + h * 0.03), card[0].upper(), fl, ink)
        text(d, (x0 + w * 0.03, y0 + h * 0.08), card[1], fh, INK)
        wrap(d, (x0 + w * 0.03, y0 + h * 0.18), card[2], fb, SOFT,
             max_w=(x1 - x0) - w * 0.06, line_h=int(unit * (0.040 if portrait else 0.032)))
    footer(d, w, h, source, falsifier, (int(unit * (0.022 if portrait else 0.016)),
                                        int(unit * (0.032 if portrait else 0.024))))
    im.save(path)
    print("wrote", path, im.size)


def main():
    src = "Madison project brief · Intelligence Agents layer · Nov 2026"
    two_cards(
        OUT / "media/B02.png", 3840, 2160,
        "plate 1 · who can check",
        "The desk is not equally open.",
        "Who can verify an influencer audience today.",
        ("Enterprise", "Can buy a desk.", "Large companies can afford proprietary vetting tools."),
        ("Madison's people", "Cannot buy that desk.", "Smaller brands, independent creators, and nonprofits — the groups Humanitarians AI exists to support."),
        src, "Access is not a product that shipped.", accent="right")
    two_cards(
        OUT / "pantry/B02-916.png", 2160, 3840,
        "plate 1 · who can check",
        "The desk is not equally open.",
        "Who can verify an influencer audience today.",
        ("Enterprise", "Can buy a desk.", "Large companies can afford proprietary vetting tools."),
        ("Madison's people", "Cannot.", "Smaller brands, independent creators, and nonprofits."),
        src, "Access is not a product that shipped.", accent="right")
    two_cards(
        OUT / "media/B03.png", 3840, 2160,
        "plate 2 · two questions",
        "A score on the account is not a score on the comments.",
        "Explainable risk. Two answers, not one.",
        ("Account", "Is the account fake?", "How likely the profile itself is inauthentic — bots, fake followers."),
        ("The post", "Are the comments fake?", "How likely the likes and comments on a given post are fake — separate from the account."),
        src, "Two questions are not two shipped scores.", accent="right")
    two_cards(
        OUT / "pantry/B03-916.png", 2160, 3840,
        "plate 2 · two questions",
        "Two questions. Not one.",
        "Explainable risk. Separate answers.",
        ("Account", "Is the account fake?", "How likely the profile itself is inauthentic."),
        ("The post", "Are the comments fake?", "How likely the likes and comments on that post are fake."),
        src, "Two questions are not two shipped scores.", accent="right")
    two_cards(
        OUT / "media/B04.png", 3840, 2160,
        "plate 3 · how it differs",
        "Rules on the account. A model with a second layer.",
        "What Madison's competitive reading actually compared.",
        ("Reviewed desks", "Account-level rules.", "HypeAuditor, Modash, CreatorIQ: one score from account-wide stats. Thresholds, not a trained, validated model."),
        ("Madison's build", "Train, then look at the post.", "Classifier on TwiBot-20, a labeled real-versus-bot set, plus a separate engagement layer."),
        src, "A Twitter benchmark is not Instagram ground truth.", accent="right")
    two_cards(
        OUT / "pantry/B04-916.png", 2160, 3840,
        "plate 3 · how it differs",
        "Rules versus a second layer.",
        "What the competitive reading compared.",
        ("Reviewed desks", "Account-level rules.", "One score from account-wide stats. Thresholds, not a trained model."),
        ("Madison's build", "Train, then the post.", "TwiBot-20 labeled real versus bot, plus a separate engagement layer."),
        src, "A Twitter benchmark is not Instagram ground truth.", accent="right")
    for name in ("B02", "B03", "B04"):
        (OUT / "pantry" / f"{name}.png").write_bytes((OUT / "media" / f"{name}.png").read_bytes())


if __name__ == "__main__":
    main()
