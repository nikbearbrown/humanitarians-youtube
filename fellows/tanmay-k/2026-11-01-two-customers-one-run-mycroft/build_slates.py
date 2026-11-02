#!/usr/bin/env python3
"""Week 29 work-video review stills. Long film: one 3840x2160 slate per beat (_stills/Bxx-16x9.png).
Short: one 2160x3840 frame per beat (_stills/Sxx-9x16.png). House look as Week 27/29 topic video (cream page, EB Garamond + Inter + PT Mono).
Every figure on screen is read from _source/ (copies of committed files on nikbearbrown/mycroft main) and asserted against the signed narration.
Run: /opt/homebrew/bin/python3.12 build_slates.py [B00 S3 ...]"""
import json, re, sys, math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent; OUT = HERE / "_stills"; OUT.mkdir(exist_ok=True)
SRC = HERE / "_source"; SLUG = "scenariostresstestingagent"
FONTS = Path("/Users/tanny/Humanitarians_AI/brutalist.art/runtime/fonts")
S = 2
PAD = 34  # breathing room between a desk header and its contents (the box grows by the same amount)
PAGE, CARD, BORDER = "#FAF9F5", "#FFFFFF", "#E5E2D9"
INK, INK_SOFT, GHOST, SPARK, SEND, SAGE = "#3D3929", "#73705F", "#A9A491", "#D97757", "#C6613F", "#5B7B6A"
SPARK_TEXT = "#B5532F"; WASH = "#FBE9E1"; WASH2 = "#E8F0EB"

LOG = json.load(open(SRC / f"{SLUG}-2026-11-01.json")); DLOG = json.load(open(SRC / f"{SLUG}-2026-11-01-defective.json"))
REP = (SRC / f"{SLUG}-2026-11-01.md").read_text(); DREP = (SRC / f"{SLUG}-2026-11-01-defective.md").read_text()
HEADS = re.findall(r"^## (.+)$", REP, flags=re.M)
assert len(LOG) == 16 and len(HEADS) == 15 and LOG["records_seen"] == 12 and "12 request(s) read" in REP
assert "Stop conditions: 0 of 4 triggered" in REP

_fc = {}
def F(kind, size):
    k = (kind, size)
    if k not in _fc:
        p = {"serif": "EB_Garamond/static/EBGaramond-Regular.ttf", "serifi": "EB_Garamond/static/EBGaramond-Italic.ttf",
             "serifm": "EB_Garamond/static/EBGaramond-Medium.ttf", "sans": "Inter/static/Inter_28pt-Regular.ttf",
             "sansm": "Inter/static/Inter_28pt-Medium.ttf", "mono": "PT_Mono/PTMono-Regular.ttf"}[kind]
        _fc[k] = ImageFont.truetype(str(FONTS / p), round(size * S))
    return _fc[k]

class Canvas:
    def __init__(self, W, H, cap=99):
        self.cap, self.cur = cap, 0  # motion: elements drawn after step(k) with k > cap are skipped
        self.W, self.H = W, H; self.bodies = []; self._noshift = False; self.im = Image.new("RGB", (W * S, H * S), PAGE); self.d = ImageDraw.Draw(self.im); self.log = []
    def step(self, k): self.cur = k
    def tw(self, s, kind, size): return F(kind, size).getlength(s) / S
    def _dy(self, x, y):
        if self._noshift: return 0
        for (bx0, by0, bx1, by1) in self.bodies:
            if bx0 <= x <= bx1 and by0 + 112 <= y < by1: return PAD
        return 0
    def _sf(self, y): return 0  # Short: centre content so the lower third is not empty
    def text(self, x, y, s, kind="sans", size=24, fill=INK, anchor="la", maxw=None):
        if self.cur > self.cap: return
        y += self._dy(x, y); y += self._sf(y)
        mn = 32 if self.W == 1080 else 24  # phone-width Short: nothing under 32
        if kind in ("sans", "sansm", "mono") and size < mn: size = mn
        if fill == SPARK: fill = SPARK_TEXT if size < 48 else SEND
        if maxw is not None: assert self.tw(s, kind, size) <= maxw + 0.5, f"overflow {self.tw(s,kind,size):.0f}>{maxw}: {s}"
        self.log.append((s, kind, size, x, y, self.tw(s, kind, size), anchor)); self.d.text((x * S, y * S), s, font=F(kind, size), fill=fill, anchor=anchor)
    def rect(self, x0, y0, x1, y1, fill=None, outline=None, width=2, r=0):
        if self.cur > self.cap: return
        dy = self._dy(x0, y0); y0 += dy; y1 += dy; sf = self._sf(y0); y0 += sf; y1 += sf
        b = (x0 * S, y0 * S, x1 * S, y1 * S)
        self.d.rounded_rectangle(b, radius=r * S, fill=fill, outline=outline, width=round(width * S)) if r else self.d.rectangle(b, fill=fill, outline=outline, width=round(width * S))
    def line(self, pts, fill=INK, width=3):
        if self.cur > self.cap: return
        pts = [(x, y + self._sf(pts[0][1])) for x, y in pts]; self.d.line([(x * S, y * S) for x, y in pts], fill=fill, width=round(width * S), joint="curve")
    def arrow(self, p0, p1, fill=SPARK, width=4):
        if self.cur > self.cap: return
        sf = self._sf(p0[1]); p0 = (p0[0], p0[1] + sf); p1 = (p1[0], p1[1] + sf); self.line([(p0[0], p0[1] - sf), (p1[0], p1[1] - sf)], fill, width); (x0, y0), (x1, y1) = p0, p1; a = math.atan2(y1 - y0, x1 - x0); L = 20
        self.d.polygon([(x1 * S, y1 * S), ((x1 - L * math.cos(a - .45)) * S, (y1 - L * math.sin(a - .45)) * S), ((x1 - L * math.cos(a + .45)) * S, (y1 - L * math.sin(a + .45)) * S)], fill=fill)
    def wrap(self, x, y, s, kind, size, fill, maxw, lh=1.32):
        lines, cur = [], ""
        for w in s.split():
            t = (cur + " " + w).strip()
            if self.tw(t, kind, size) <= maxw: cur = t
            else: lines.append(cur); cur = w
        lines.append(cur)
        for i, l in enumerate(lines): self.text(x, y + i * size * lh, l, kind, size, fill)
        return y + len(lines) * size * lh
    def shift_value(self):
        """Short: how far to move everything under the headline so it is centred in the space left (computed on the full frame)."""
        return 0  # Short is laid out inside the safe area directly; no re-centring
        top = 300 * S; body = self.im.crop((0, top, self.im.width, self.im.height)); bb = Image.eval(body.convert("L"), lambda v: 255 if v < 240 else 0).getbbox()
        if not bb: return 0
        free_top, free_bot = top, self.im.height - 90 * S; h = bb[3] - bb[1]; new_y = free_top + max(0, (free_bot - free_top - h) // 2)
        return max(0, new_y - (top + bb[1]))
    def final(self, shift=None):
        im = self.im; shift = self.shift_value() if shift is None else shift
        if self.W == 1080 and shift > 0:
            top = 300 * S; body = im.crop((0, top, im.width, im.height)); im = im.copy(); im.paste(PAGE, (0, top, im.width, im.height)); im.paste(body, (0, top + shift))
        return im
    def save(self, name): self.final().save(OUT / name, optimize=True)

def desk(cv, x0, y0, x1, y1, who, what, on=False, tint=None):
    cv._noshift = True; y1 += PAD
    cv.rect(x0, y0, x1, y1, fill=CARD, outline=SPARK if on else BORDER, width=4 if on else 2, r=14)
    cv.rect(x0 + 2, y0 + 2, x1 - 2, y0 + 112, fill=tint or "#F4F1E8", r=12)
    cv.text(x0 + 32, y0 + 14, who, "sansm", 24, INK_SOFT); cv.text(x0 + 32, y0 + 52, what, "serif", 34, INK)
    cv._noshift = False; cv.bodies.append((x0, y0, x1, y1))
def mono_rows(cv, x, y, rows, size=26, lh=1.55, maxw=None, hi=(), only=None):
    for i, r in enumerate(rows):
        if only is not None and i not in only: continue
        yy = y + i * size * lh
        if i in hi: cv.rect(x - 14, yy - 6, x + (maxw or 700), yy + size * 1.25, fill=WASH, r=6)
        cv.text(x, yy, r, "mono", size, SEND if i in hi else INK, maxw=maxw)
def header(cv, s, sub=None, y=64):
    cv.text(115, y, s, "serif", 62, INK)
    if sub: cv.text(115, y + 82, sub, "sans", 28, INK_SOFT)
def chip(cv, x, y, s, fill=WASH, ink=SEND, size=26):
    w = cv.tw(s, "sansm", size) + 44; cv.rect(x, y, x + w, y + 54, fill=fill, r=27); cv.text(x + 22, y + 11, s, "sansm", size, ink); return x + w + 16
def foot(cv, s): cv.text(115, 1010, s, "sans", 24, INK_SOFT)

# ---------- long film (1920x1080 logical) ----------
LP = "MACHINE'S DESK · the agent log"; PP = "PERSON'S DESK · the report"
def long_frames(cap=99, only=None):
    out = {}
    def mk(n, fn):
        if only is None or n == only: c = Canvas(1920, 1080, cap); fn(c); out[n] = c
    def B00(c):
        c.text(115, 250, "Two Customers, One Run", "serif", 128, INK)
        c.text(115, 420, "Writing a pipeline's results for a program and a person", "serifi", 48, INK_SOFT)
        c.rect(115, 540, 1805, 544, fill=SPARK)
        c.text(115, 590, "Tanmay Kulkarni", "serifm", 56, INK); c.text(115, 666, "for Humanitarians AI", "sans", 32, INK_SOFT)
        c.step(1); c.text(115, 820, "This week: a contribution to Mycroft", "serif", 44, INK); c.step(2); c.text(115, 886, "github.com/nikbearbrown/mycroft", "mono", 30, SEND)
    def B00b(c):
        header(c, "One fact, written down twice")
        desk(c, 115, 250, 920, 880, LP, "a field", on=True); desk(c, 1000, 250, 1805, 880, PP, "a sentence", on=True, tint=WASH2)
        c.step(1); c.text(517, 370, "12", "serifm", 250, SEND, anchor="ma")
        c.text(160, 730, '"records_seen": 12', "mono", 44, INK, maxw=720); c.text(160, 800, "a field, for the next script", "sans", 28, INK_SOFT)
        c.step(2); c.text(1402, 370, "12", "serifm", 250, SEND, anchor="ma"); c.wrap(1040, 715, "12 request(s) read from the `clean` sample folder", "mono", 32, INK, 720, 1.3); c.text(1040, 820, "a sentence, for the person deciding", "sans", 28, INK_SOFT)
        c.step(3); c.text(960, 560, "=", "serifm", 90, SPARK, anchor="ma"); c.text(960, 940, "Same run, same fact. Two pages for two readers.", "serifi", 50, SEND, anchor="ma")
    def B01(c):
        header(c, "The recipe: a scenario stress testing agent", "It takes a portfolio and a market shock and works out what the shock does.")
        xs = [115 + i * 285 for i in range(6)]
        names = ["Verify provenance", "Ingest declared inputs", "Validate data shape", "Transform and quality check", "Run approved tools", "Produce human report"]
        for i, x in enumerate(xs):
            c.step(0)
            c.rect(x, 300, x + 255, 680, fill=CARD, outline=BORDER, width=2, r=14)
            c.text(x + 128, 330, str(i + 1), "serifm", 90, INK, anchor="ma"); c.wrap(x + 20, 450, names[i], "serif", 30, INK, 215, 1.2)
        for i, x in enumerate(xs):
            on = i + 1 in (4, 6); built = i + 1 in (1, 3, 5)
            c.step(1 if built or i == 1 else 2)
            if on: c.rect(x, 300, x + 255, 680, fill=WASH, outline=SPARK, width=4, r=14); c.text(x + 128, 330, str(i + 1), "serifm", 90, SEND, anchor="ma"); c.wrap(x + 20, 450, names[i], "serif", 30, INK, 215, 1.2)
            c.text(x + 20, 620, "this time" if on else ("built earlier" if built else "next piece"), "sansm", 24, SEND if on else INK_SOFT)
        c.step(1); chip(c, 115, 760, "steps 1, 3, 5: pull request 74", CARD, INK_SOFT); c.step(2); chip(c, 560, 760, "steps 4, 6: pull request 81", WASH, SEND)
        c.step(3); c.text(115, 890, "This film is about step six.", "serif", 54, INK)
    def B02(c):
        header(c, "Every run ends in front of two readers")
        desk(c, 115, 230, 905, 740, "READER ONE", "A program", tint="#F4F1E8"); desk(c, 1015, 230, 1805, 740, "READER TWO", "A person", tint=WASH2)
        c.step(1); c.wrap(150, 350, "The next script in the line.", "serif", 44, INK, 700)
        for i, t in enumerate(["a field it can count on", "one name, one meaning", "the same shape every run"]): c.text(150, 470 + i * 70, "· " + t, "sans", 32, SEND if i == 0 else INK, maxw=700)
        c.step(2); c.wrap(1050, 350, "Someone who decides whether to go on.", "serif", 44, INK, 700)
        for i, t in enumerate(["a page they can act on", "its reader and decision named", "sentences, not fields"]): c.text(1050, 470 + i * 70, "· " + t, "sans", 32, SEND if i == 0 else INK, maxw=700)
        c.step(3); c.text(960, 840, "two customers, twice", "serifi", 76, SEND, anchor="ma"); c.text(960, 940, "SNICKERDOODLE.md, principle five: a log for the agent, a report for the human", "sans", 28, INK_SOFT, anchor="ma")
    def B03(c):
        header(c, "The machine's desk", "The agent log: a plain file with sixteen fields")
        names = list(LOG); desk(c, 115, 240, 1805, 900, LP, "logs/scenariostresstestingagent-2026-11-01.json", on=True)
        hi = {"records_seen", "rejects", "flags", "stop_conditions", "gate_decisions"}
        for i, k in enumerate(names):
            col, row = divmod(i, 8); x = 160 + col * 830; y = 360 + row * 62
            c.step(1); c.text(x, y, f"{i+1:>2}  {k}", "mono", 32, INK)
        for i, k in enumerate(names):
            col, row = divmod(i, 8); x = 160 + col * 830; y = 360 + row * 62
            if k in hi:
                c.step(2 if k in ("records_seen", "rejects", "flags") else 3)
                c.rect(x - 14, y - 6, x + 760, y + 46, fill=WASH, r=6); c.text(x, y, f"{i+1:>2}  {k}", "mono", 32, SEND)
        c.step(4); foot(c, "One name and one meaning for each field, so the next script can read it without guessing.")
    def B04(c):
        header(c, "The person's desk", "The report: its reader, its decision, fifteen sections")
        desk(c, 115, 240, 1805, 935, PP, "reports/generated/scenariostresstestingagent-2026-11-01.md", on=True, tint=WASH2)
        c.step(1); c.text(160, 368, "Reader:", "sansm", 26, SEND); c.text(290, 368, "the domain lead or human boss responsible for accepting the `ScenarioStressTestingAgent` run.", "sans", 26, INK, maxw=1480)
        c.text(160, 418, "Decision enabled:", "sansm", 26, SEND); c.text(420, 418, "approve the run for the next phase, request source or schema fixes, or block live execution.", "sans", 26, INK, maxw=1370)
        for i, h in enumerate(HEADS):
            col, row = divmod(i, 8); x = 160 + col * 830; y = 505 + row * 50
            c.step(2); c.text(x, y, f"{i+1:>2}  {h}", "sans", 28, INK, maxw=760)
        for i, h in enumerate(HEADS):
            col, row = divmod(i, 8); x = 160 + col * 830; y = 505 + row * 50
            if i in (0, 14): c.step(3 if i == 14 else 2); c.rect(x - 14, y - 6, x + 760, y + 42, fill=WASH, r=6); c.text(x, y, f"{i+1:>2}  {h}", "sans", 28, SEND, maxw=760)
    def B05(c):
        header(c, "A count, followed across both desks")
        desk(c, 115, 230, 790, 880, LP, "records_seen", on=True); desk(c, 1010, 230, 1805, 880, PP, "Run summary", on=True, tint=WASH2)
        c.step(1); c.text(450, 380, "12", "serifm", 300, SEND, anchor="ma"); c.text(160, 760, '"records_seen": 12', "mono", 36, INK, maxw=600)
        c.step(2); c.arrow((810, 540), (990, 540)); c.text(900, 480, "same files", "sansm", 24, INK_SOFT, anchor="ma")
        L = ["12 request(s) read from the", "`clean` sample folder;", "12 accepted at step 3,", "0 rejected there.", "11 stress-tested at step 5,", "1 stopped at the Groq handoff;"]
        mono_rows(c, 1050, 350, L, 34, 1.65, 730)
        c.step(3); mono_rows(c, 1050, 350, L, 34, 1.65, 730, hi=(0, 1, 2), only=(0, 2))
        c.step(4); mono_rows(c, 1050, 350, L, 34, 1.65, 730, hi=(4, 5), only=(4, 5))
        c.step(5); foot(c, "Neither count is typed: both are computed from the same files.")
    def B06(c):
        header(c, "A reason, followed across both desks", "A second set of requests, built with ten deliberate faults")
        e = [r for r in DLOG["rejects"] if r["id"] == "d06-all-weights-zero"][0]; reason = e["reasons"][0]
        desk(c, 115, 270, 905, 840, LP, "rejects, one entry each", on=True); desk(c, 1015, 270, 1805, 840, PP, "Rejects", on=True, tint=WASH2)
        rows = ['{', f'  "id": "{e["id"]}",', f'  "stage": "{e["stage"]}",', '  "reasons": [']
        c.step(1); mono_rows(c, 150, 390, rows, 32, 1.55, 740)
        c.step(2); y = c.wrap(190, 390 + 4 * 32 * 1.55, f'"{reason}"', "mono", 26, SEND, 680, 1.4); c.text(150, y + 4, "  ]", "mono", 32, INK); c.text(150, y + 54, "}", "mono", 32, INK)
        c.step(3)
        for i, t in enumerate(["- `d03-holding-without-ticker` ...", "- `d04-holdings-is-an-object` ...", "- `d05-weight-is-a-string` ..."]): c.text(1050, 400 + i * 44, t, "mono", 24, GHOST, maxw=730)
        c.step(4); c.rect(1036, 550, 1790, 770, fill=WASH, r=8); c.text(1050, 566, "- `d06-all-weights-zero` at step 3:", "mono", 26, INK, maxw=730); c.wrap(1050, 616, reason, "mono", 26, SEND, 730, 1.4)
        c.text(960, 905, "the same line, word for word", "serifi", 44, SEND, anchor="ma")
    def B07(c):
        header(c, "A call, followed across both desks")
        desk(c, 115, 230, 905, 880, LP, "gate_decisions: seven", on=True); desk(c, 1015, 230, 1805, 880, PP, "Decision recommendation", on=True, tint=WASH2)
        rows = [f'{g["gate"][:20]:<20} {g["result"][:12]}' for g in LOG["gate_decisions"]]
        rows = [f'{g["gate"].split(" ",1)[1] if g["gate"][0].isdigit() else g["gate"]}'[:16].ljust(17) + g["result"].split(" (")[0] for g in LOG["gate_decisions"]]
        c.step(1); mono_rows(c, 150, 360, rows, 27, 1.7, 740)
        asks = [("Approve for the next phase", "YES"), ("Request source or schema fixes", "NO"), ("Block live execution", "YES")]
        for i, (a, v) in enumerate(asks):
            y = 360 + i * 110; c.step(2); c.text(1050, y, a, "serif", 36, INK, maxw=560); c.step(3); chip(c, 1650, y - 4, v, WASH if v == "YES" else CARD, SEND if v == "YES" else INK_SOFT, 30)
        c.step(2); c.text(1050, 408, "(sample mode only)", "sans", 24, INK_SOFT); c.step(4); c.text(1050, 700, "The faulty run flips them:", "sans", 28, INK_SOFT); chip(c, 1050, 750, "approve NO", CARD, INK_SOFT, 28); chip(c, 1295, 750, "fixes YES", WASH, SEND, 28); chip(c, 1520, 750, "block YES", WASH, SEND, 28)
        c.step(5); foot(c, "Computed from the run's files, never typed.")
    def B08(c):
        header(c, "Then I read the machine's page as a person would", "The committed log and report at pull request 81")
        desk(c, 115, 270, 905, 860, LP, "stop_conditions, first entry", on=True); desk(c, 1015, 270, 1805, 860, PP, "Run summary", on=True, tint=WASH2)
        LL = ['"condition": "Stop if credentials,', '  API keys ... are hardcoded', '  instead of read from', '  environment variables.",', '"triggered": true']
        c.step(1); mono_rows(c, 150, 390, LL, 27, 1.6, 740, only=(0, 1, 2, 3))
        c.step(2); mono_rows(c, 150, 390, LL, 27, 1.6, 740, hi=(4,), only=(4,))
        c.step(3); mono_rows(c, 1050, 390, ["12 request(s) read ...", "11 stress-tested ...", "Mode sample: every request", "is invented; ... no credential", "was used."], 27, 1.6, 730)
        c.step(4); c.text(1050, 740, "(no line about stop conditions)", "sansm", 26, INK_SOFT)
        c.text(960, 930, "Two pages, two different answers.", "serifi", 50, SEND, anchor="ma")
    def B09(c):
        header(c, "Reading both pages is what showed it", "The correction: pull request 82")
        desk(c, 115, 270, 905, 700, LP, "stop_conditions, first entry", on=True); desk(c, 1015, 270, 1805, 700, PP, "Run summary", on=True, tint=WASH2)
        c.step(1); mono_rows(c, 150, 390, ['"triggered": false,', '"evidence": "scanned 41 file(s)', '  ... none found"'], 27, 1.6, 740, hi=(0,))
        c.step(2); mono_rows(c, 1050, 390, ["Stop conditions: 0 of 4 triggered;", "each is judged from evidence", "in the agent log."], 27, 1.6, 730, hi=(0,))
        c.step(1); x = chip(c, 115, 780, "each of four judged from evidence", CARD, INK_SOFT); c.step(3); x = chip(c, x, 780, "planted fake key: caught", WASH, SEND); c.step(4); chip(c, x, 780, "30 of 30 checks pass", CARD, INK_SOFT)
        c.step(5); c.text(960, 910, "merged as pull request 82", "serifi", 48, SEND, anchor="ma")
    def B10(c):
        header(c, "What keeps the two pages in agreement", "One source of facts")
        c.step(1); c.rect(115, 250, 640, 560, fill=CARD, outline=SPARK, width=4, r=14); c.text(378, 300, "the same files", "serifm", 52, INK, anchor="ma"); c.wrap(150, 390, "the recipe, the sample requests, the step-four check", "sans", 28, INK_SOFT, 450)
        c.step(2); c.arrow((660, 360), (1000, 300)); c.arrow((660, 450), (1000, 520))
        c.rect(1010, 230, 1805, 380, fill=CARD, outline=BORDER, width=2, r=14); c.text(1050, 270, "agent log", "serifm", 46, INK); c.text(1050, 330, "16 fields", "sans", 28, INK_SOFT)
        c.rect(1010, 430, 1805, 580, fill=CARD, outline=BORDER, width=2, r=14); c.text(1050, 470, "human report", "serifm", 46, INK); c.text(1050, 530, "15 sections", "sans", 28, INK_SOFT)
        c.step(4); c.text(115, 650, "Two commands, run from a clone:", "serif", 44, INK)
        c.text(115, 730, "python3 scripts/gigo/scenariostresstestingagent-transform-quality-check.py", "mono", 28, INK, maxw=1690)
        c.text(115, 790, "python3 scripts/tools/scenariostresstestingagent-produce-human-report.py --now 2026-11-01T09:00:00Z", "mono", 28, INK, maxw=1690)
        c.step(3); foot(c, "With the clock pinned, two runs give identical bytes.")
    def B11(c):
        header(c, "Your turn", "Think of the last thing your own pipeline produced")
        q = [("Who reads it next?", "a script, or a person"), ("What do they do with it?", "carry on, or decide"), ("What must be on their page?", "so they can do it")]
        for i, (a, b) in enumerate(q):
            y = 270 + i * 210; c.step(i + 1); c.rect(115, y, 1805, y + 170, fill=CARD, outline=SPARK if i == 2 else BORDER, width=4 if i == 2 else 2, r=14)
            c.text(160, y + 28, f"{i+1}", "serifm", 80, SEND); c.text(260, y + 24, a, "serif", 56, INK); c.text(260, y + 104, b, "sans", 30, INK_SOFT)
        c.step(4); c.text(115, 930, "Then build both pages from one set of facts.", "serifi", 50, SEND)
    def B12(c):
        header(c, "Where the recipe stands")
        c.step(1); c.rect(115, 230, 1805, 520, fill=CARD, outline=BORDER, width=2, r=14); c.text(160, 260, "recipes/scenariostresstestingagent.md", "sansm", 26, INK_SOFT)
        mono_rows(c, 160, 330, ["status: DRAFT", "todos_open: 3", "recipe_version: 0.3.1"], 40, 1.4, 900)
        c.text(960, 330, "three pieces left to build,", "serif", 44, INK); c.text(960, 396, "named in the report's source list", "serif", 44, INK)
        c.step(2); c.rect(115, 590, 880, 860, fill=CARD, outline=SPARK, width=4, r=14); c.text(160, 630, "pull request 81", "serifm", 56, INK); c.wrap(160, 720, "builds steps four and six: the quality check and the two pages", "sans", 28, INK_SOFT, 680)
        c.step(3); c.rect(1040, 590, 1805, 860, fill=CARD, outline=SPARK, width=4, r=14); c.text(1085, 630, "pull request 82", "serifm", 56, INK); c.wrap(1085, 720, "the correction that came from reading both pages", "sans", 28, INK_SOFT, 680)
    def B13(c):
        c.text(960, 340, "Tanmay Kulkarni", "serifm", 120, INK, anchor="ma"); c.text(960, 520, "for Humanitarians AI", "serif", 64, INK_SOFT, anchor="ma")
        c.step(1); c.rect(760, 640, 1160, 644, fill=SPARK); c.text(960, 700, "signing off", "serifi", 64, SEND, anchor="ma")
    for n, f in [("B00", B00), ("B00b", B00b), ("B01", B01), ("B02", B02), ("B03", B03), ("B04", B04), ("B05", B05), ("B06", B06), ("B07", B07), ("B08", B08), ("B09", B09), ("B10", B10), ("B11", B11), ("B12", B12), ("B13", B13)]: mk(n, f)
    return out

# ---------- Short (1080x1920 logical). Safe area: ink only between 12% and 75% of the height (y 230 to 1440), nothing right of x 910;
# body kept to y 1370 so the progress rail (added at motion time) sits at y 1410. ----------
def short_frames(cap=99, only=None):
    out = {}
    def mk(n, fn):
        if only is None or n == only: c = Canvas(1080, 1920, cap); fn(c); out[n] = c
    M, R = 70, 905
    def hd(c, s, y=240): c.wrap(M, y, s, "serif", 58, INK, R - M, 1.12)
    def card(c, y0, y1, label, big, on=True, tint=None): desk(c, M, y0, R, y1, label, big, on=on, tint=tint)
    def Sm1(c):
        c.wrap(M, 250, "Every run of a pipeline needs two different pages", "serif", 62, INK, R - M, 1.12)
        c.step(1); c.rect(M, 400, 560, 404, fill=SPARK)
        c.step(2); c.text(M, 500, "Hi, I'm", "serif", 46, INK_SOFT); c.text(M, 565, "Tanmay Kulkarni", "serifm", 88, INK, maxw=R - M)
        c.step(3); c.text(M, 700, "for Humanitarians AI", "serif", 48, INK_SOFT); c.rect(M, 780, R, 784, fill=SPARK)
        c.step(4); c.text(M, 830, "This week:", "serif", 46, INK); c.step(5); c.wrap(M, 900, "a contribution to Mycroft, a public repository of recipes an agent can run and a person can read", "serif", 46, INK, R - M, 1.25)
        c.step(6); c.text(M, 1260, "github.com/nikbearbrown/mycroft", "mono", 34, SEND, maxw=R - M)
    def S0(c):
        hd(c, "An AI pipeline has just finished a run"); c.step(1); c.wrap(M, 470, "Somebody needs to know what happened.", "serifi", 50, INK_SOFT, R - M, 1.2)
        c.step(2); c.rect(M, 640, R, 930, fill=CARD, outline=BORDER, width=2, r=16)
        for i, t in enumerate(["read", "check", "stress test", "report"]):
            x = M + 20 + i * 201; c.rect(x, 700, x + 190, 870, fill=WASH if i == 3 else "#F4F1E8", r=14); c.text(x + 95, 765, t, "sansm", 32, SEND if i == 3 else INK, anchor="ma")
        c.step(3); c.text(M, 1060, "But who, exactly?", "serif", 84, SEND)
    def S1(c):
        hd(c, "Two readers, two pages")
        c.step(1); card(c, 410, 790, "READER ONE", "A program"); c.step(2); c.wrap(M + 32, 590, "the next script in the line", "serif", 46, INK, 740)
        c.step(3); card(c, 840, 1220, "READER TWO", "A person", tint=WASH2); c.step(4); c.wrap(M + 32, 1020, "decides whether to carry on", "serif", 46, INK, 740)
        c.step(5); c.text(M, 1290, "different needs, different pages", "serifi", 46, SEND)
    def S2(c):
        hd(c, "The machine's page"); card(c, 410, 1350, "THE AGENT LOG", "sixteen fields, built for a script")
        for i, k in enumerate(list(LOG)[:9]):
            y = 580 + i * 60
            c.step(1); c.text(M + 40, y, k, "mono", 38, INK)
            if k == "records_seen": c.step(2); c.rect(M + 20, y - 8, R - 20, y + 52, fill=WASH, r=8); c.text(M + 40, y, k, "mono", 38, SEND)
        c.step(2); c.text(M + 40, 1220, '"records_seen": 12', "mono", 40, SEND)
    def S3(c):
        hd(c, "The person's page"); card(c, 410, 1180, "THE REPORT", "names its reader and the decision", tint=WASH2)
        c.step(1); c.text(M + 40, 570, "Reader: the domain lead or human boss", "sans", 32, INK, maxw=R - M - 60); c.text(M + 40, 630, "Decision enabled: approve, request", "sans", 32, INK); c.text(M + 40, 680, "fixes, or block live execution", "sans", 32, INK)
        c.step(2); c.text(M + 40, 770, "Run summary", "sansm", 32, INK_SOFT); c.rect(M + 20, 830, R - 20, 1060, fill=WASH, r=10); c.wrap(M + 40, 850, "12 request(s) read from the `clean` sample folder", "mono", 34, SEND, R - M - 80, 1.35)
        c.step(3); c.text(M, 1250, "Same fact. Same run.", "serif", 76, SEND)
    def S4(c):
        hd(c, "They agree because they share one source")
        c.step(1); c.rect(M, 470, R, 760, fill=CARD, outline=SPARK, width=4, r=16); c.text((M + R) // 2, 530, "the same files", "serifm", 70, INK, anchor="ma"); c.text((M + R) // 2, 640, "counts compared before writing", "sans", 32, INK_SOFT, anchor="ma")
        c.step(2); c.arrow((260, 790), (260, 930)); c.arrow((720, 790), (720, 930))
        c.rect(M, 950, 450, 1250, fill=CARD, outline=BORDER, r=16); c.text(260, 1070, "agent log", "serifm", 50, INK, anchor="ma"); c.rect(500, 950, R, 1250, fill=CARD, outline=BORDER, r=16); c.text(702, 1070, "report", "serifm", 50, INK, anchor="ma")
    def S5(c):
        hd(c, "Then the report adds the call"); card(c, 410, 1100, "DECISION RECOMMENDATION", "computed, not typed", tint=WASH2)
        for i, (a, v) in enumerate([("Approve the next phase", "YES"), ("(sample mode only)", ""), ("Block live execution", "YES")]):
            y = 580 + i * 125
            c.step(1 if i < 2 else 2); c.text(M + 40, y, a, "serif" if v else "sans", 44 if v else 32, INK if v else INK_SOFT)
            if v: chip(c, 700, y - 4, v, WASH, SEND, 34)
        c.step(3); c.text(M, 1190, "from the run's files, never typed", "serifi", 48, SEND)
    def S6(c):
        hd(c, "Reading it as a person found a mistake")
        c.step(1); card(c, 400, 700, "THE LOG SAID", 'stop condition: triggered'); c.text(M + 40, 600, '"triggered": true', "mono", 38, SEND)
        c.step(2); card(c, 760, 1050, "THE REPORT SAID", "nothing", tint=WASH2); c.text(M + 40, 930, "(no line about it)", "sans", 34, INK_SOFT)
        c.step(3); c.rect(M, 1120, R, 1330, fill=WASH, r=16); c.text(M + 40, 1150, "Now:", "sansm", 34, SEND); c.wrap(M + 40, 1210, "Stop conditions: 0 of 4 triggered", "mono", 36, SEND, R - M - 80, 1.3)
    def S7(c):
        hd(c, "For your pipeline")
        for i, t in enumerate(["Who reads its last output?", "What do they do next?", "What must be on their page?"]):
            y = 410 + i * 310; c.step(i + 1); c.rect(M, y, R, y + 270, fill=CARD, outline=SPARK if i == 2 else BORDER, width=4 if i == 2 else 2, r=16); c.text(M + 36, y + 50, str(i + 1), "serifm", 110, SEND); c.wrap(M + 180, y + 70, t, "serif", 48, INK, 640, 1.2)
    def S8(c):
        c.text(M, 300, "The long film", "serifi", 48, INK_SOFT); c.step(1); c.wrap(M, 400, "Two Customers, One Run:", "serifm", 70, INK, R - M, 1.2)
        c.step(2); c.wrap(M, 490, "Writing a Pipeline's Results for a Program and a Person", "serifm", 70, INK, R - M, 1.2)
        c.step(3); c.rect(M, 1000, R, 1004, fill=SPARK)
    def S9(c):
        c.text(M, 560, "Tanmay Kulkarni", "serifm", 90, INK, maxw=R - M); c.text(M, 690, "for Humanitarians AI", "serif", 50, INK_SOFT)
        c.step(1); c.rect(M, 790, 470, 794, fill=SPARK); c.text(M, 840, "signing off", "serifi", 58, SEND)
    for n, f in [("S-1", Sm1), ("S0", S0), ("S1", S1), ("S2", S2), ("S3", S3), ("S4", S4), ("S5", S5), ("S6", S6), ("S7", S7), ("S8", S8), ("S9", S9)]: mk(n, f)
    return out

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for n, c in long_frames().items():
        if not want or n in want: c.save(f"{n}-16x9.png")
    for n, c in short_frames().items():
        if not want or n in want: c.save(f"{n.replace('-','m')}-9x16.png")
    print("rendered", len(list(OUT.glob("*.png"))))
