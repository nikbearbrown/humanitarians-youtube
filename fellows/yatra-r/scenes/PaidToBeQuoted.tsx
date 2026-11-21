/**
 * PaidToBeQuoted.tsx — reel-local scenes for `yatra-paid-to-be-quoted`
 * ("Paid to Be Quoted." — publishers selling brands a new service: not ad space, but
 * getting cited by ChatGPT and Gemini; plus the Internet Licensing Collective and the
 * AI Overviews backdrop).
 *
 * ── WHY THESE ARE NEW COMPONENTS ─────────────────────────────────────────────
 * The human asked for a new video, not a variation. No earlier family (Geo*, Seo*, Wk*,
 * Wwa*, …) is reused. Shapes come from this reel's argument: a struck "ad space" sale
 * replaced by three kinetic lines, an article-with-ad-slot beside an AI chat with one
 * cited line, a publisher selling an in-answer mention with paid-brand tokens, a field of
 * sites whose one-at-a-time deal lines collapse into a single licensing hub, two 10×10
 * waffles (24 → 85 of every 100 searches), a three-layer market stack, and a
 * know / don't-know ledger.
 *
 * ── ONE COMPONENT, BOTH ASPECTS ──────────────────────────────────────────────
 * Each scene reads the composition size and lays out for 16:9 (side by side) or 9:16
 * (stacked, re-banded — never scaled). Portrait keeps content above y≈1440 and left of
 * x≈960 (platform UI keep-out) and moves the bug lower-left. Root.tsx registers each
 * scene twice: `PqX` at 1920×1080 and `PqX916` at 1080×1920.
 *
 * ── THE SOURCING CONSTRAINT, ENFORCED BY THE TYPES ───────────────────────────
 * Three supplied points, no others. So:
 *   · Every figure-bearing scene REQUIRES a `source` string (muted ink, never accent).
 *   · `value` strings print verbatim ("24%", "at least 3"); `cells` / `paidCount` are
 *     separate numbers that only drive drawing. Nothing parses a displayed string.
 *   · PqService draws exactly `paidCount` filled tokens plus ONE dashed open token whose
 *     label says the rest is not reported — "at least" stays "at least".
 *   · PqLicense's site field is decorative and carries a REQUIRED `marksNote` — the dot
 *     count is never a figure. There is no count prop for the field.
 *   · No brand names, prices, or outcomes exist as props anywhere: none were supplied.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE, SAFE916} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';

const STAGE = '#F2F0E9';
const RULE = '#D8D4C8';
const MUTE = '#7A7265';
const INK = CLAUDE.INK;
const ACC = CLAUDE.SPARK;
const CARD = CLAUDE.CARD;
const BORDER = CLAUDE.BORDER;

const ease = (t: number) => 1 - Math.pow(1 - Math.min(1, Math.max(0, t)), 3);
const win = (p: number, a: number, b: number) => ease((p - a) / (b - a));
const typed = (text: string, g: number) => text.slice(0, Math.round(text.length * g));

const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

/** Layout box: landscape = SAFE; portrait = column left of the keep-out, above y 1440. */
type Box = {pt: boolean; x: number; y: number; w: number; r: number; b: number};
const useBox = (): Box => {
  const {width, height} = useVideoConfig();
  if (height > width) {
    return {pt: true, x: SAFE916.x, y: SAFE916.y, w: 906, r: SAFE916.x + 906, b: 1440};
  }
  return {pt: false, x: SAFE.x, y: SAFE.y, w: SAFE.w, r: SAFE.r, b: SAFE.b};
};

const Stage: React.FC<{B: Box; children: React.ReactNode}> = ({B, children}) => (
  <AbsoluteFill style={{backgroundColor: STAGE}}>
    {children}
    {B.pt ? (
      <div style={{position: 'absolute', left: B.x, top: B.b + 40, fontFamily: CLAUDE_FONT.serif, fontSize: 30, color: INK, opacity: 0.3, letterSpacing: '.04em'}}>@Yatra</div>
    ) : (
      <div style={{position: 'absolute', right: 1920 - SAFE.r, bottom: 1080 - SAFE.b, fontFamily: CLAUDE_FONT.serif, fontSize: 26, color: INK, opacity: 0.3, letterSpacing: '.04em'}}>@Yatra</div>
    )}
  </AbsoluteFill>
);

const Eyebrow: React.FC<{B: Box; text: string; opacity?: number}> = ({B, text, opacity = 1}) => (
  <div style={{position: 'absolute', left: B.x, top: B.y + 6, width: B.w, fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 26 : 22, letterSpacing: '.18em', color: MUTE, fontWeight: 600, opacity}}>
    {text.toUpperCase()}
  </div>
);

const Head: React.FC<{B: Box; meta: string; title: string; p: number}> = ({B, meta, title, p}) => (
  <>
    <Eyebrow B={B} text={meta} opacity={win(p, 0.0, 0.08)} />
    <div style={{position: 'absolute', left: B.x, top: B.y + (B.pt ? 64 : 62), width: B.w, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 74 : 80, color: INK, lineHeight: 1.06, opacity: win(p, 0.02, 0.1)}}>
      {title}
    </div>
  </>
);

/** Provenance: always muted ink, never the accent. */
const Source: React.FC<{B: Box; source: string; opacity: number; top?: number}> = ({B, source, opacity, top}) => (
  <div style={{position: 'absolute', left: B.x, top: top ?? (B.pt ? 1270 : SAFE.b - 128), width: B.w - (B.pt ? 0 : 220), fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 27 : 25, lineHeight: 1.3, color: MUTE, opacity}}>
    Source: {source}
  </div>
);

const Note: React.FC<{B: Box; text: string; opacity: number; top?: number}> = ({B, text, opacity, top}) => (
  <div style={{position: 'absolute', left: B.x, top: top ?? (B.pt ? 1352 : SAFE.b - 62), width: B.w - (B.pt ? 0 : 220), fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: 42, color: INK, opacity, lineHeight: 1.2}}>
    {text}
  </div>
);

const Chip: React.FC<{text: string; hot?: boolean; size?: number}> = ({text, hot, size = 22}) => (
  <span style={{fontFamily: CLAUDE_FONT.ui, fontSize: size, fontWeight: 600, letterSpacing: '.16em', textTransform: 'uppercase', color: hot ? ACC : MUTE, border: `${hot ? 2 : 1}px solid ${hot ? ACC : RULE}`, padding: '8px 16px', display: 'inline-block', whiteSpace: 'nowrap', backgroundColor: hot ? '#FFFFFF' : 'transparent'}}>
    {text}
  </span>
);

const Line: React.FC<{w: number; h?: number; o?: number; color?: string}> = ({w, h = 14, o = 0.2, color = INK}) => (
  <div style={{width: Math.max(0, w), height: h, borderRadius: h / 2, backgroundColor: color, opacity: o}} />
);

/** A word with a strike line drawn across it as `g` goes 0→1. */
const Struck: React.FC<{text: string; g: number; size: number; color?: string}> = ({text, g, size, color = INK}) => (
  <span style={{position: 'relative', display: 'inline-block', fontFamily: CLAUDE_FONT.serif, fontSize: size, lineHeight: 1.05, color, opacity: 1 - 0.45 * g}}>
    {text}
    <span style={{position: 'absolute', left: 0, top: '54%', height: Math.max(3, size / 16), width: `${g * 100}%`, backgroundColor: INK}} />
  </span>
);

/* ═══════════════════════════════════════════════════════════════════════════
   B01 — PqBluf: "Ad space" (the old sale) is struck; "The citation" sets beside it; then
   three numbered lines land in narration order — line `hot` in the accent.
   ═══════════════════════════════════════════════════════════════════════════ */
export type PqBlufData = {slideMeta: string; oldSale: string; newSale: string; lines: string[]; hot: number; closer: string};

export const PqBluf: React.FC<{data: PqBlufData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const strike = win(p, 0.08, 0.15);
  const neu = win(p, 0.12, 0.2);
  const ats = [0.16, 0.42, 0.68];
  const saleSize = B.pt ? 84 : 92;
  const linesTop = B.pt ? B.y + 470 : B.y + 330;
  const step = B.pt ? 250 : 165;
  return (
    <Stage B={B}>
      <Eyebrow B={B} text={data.slideMeta} opacity={win(p, 0, 0.06)} />
      <div style={{position: 'absolute', left: B.x, top: B.y + (B.pt ? 80 : 74), width: B.w, display: 'flex', flexDirection: B.pt ? 'column' : 'row', alignItems: B.pt ? 'flex-start' : 'center', gap: B.pt ? 24 : 40}}>
        <div style={{display: 'flex', alignItems: 'center', gap: 24, opacity: win(p, 0.02, 0.08)}}>
          <Chip text="Old sale" size={B.pt ? 24 : 22} />
          <Struck text={data.oldSale} g={strike} size={saleSize} />
        </div>
        {!B.pt && <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: 72, color: MUTE, opacity: neu}}>→</div>}
        <div style={{display: 'flex', alignItems: 'center', gap: 24, opacity: neu}}>
          <Chip text="New sale" size={B.pt ? 24 : 22} />
          <span style={{fontFamily: CLAUDE_FONT.serif, fontSize: saleSize, lineHeight: 1.05, color: INK}}>{data.newSale}</span>
        </div>
      </div>
      <div style={{position: 'absolute', left: B.x, top: linesTop - 50, width: B.w, height: 2, backgroundColor: RULE, opacity: win(p, 0.12, 0.18)}} />
      {data.lines.map((ln, i) => {
        const at = ats[i] ?? 0.2 + i * 0.2;
        const g = win(p, at, at + 0.08);
        const hot = i === data.hot;
        return (
          <div key={i} style={{position: 'absolute', left: B.x, top: linesTop + i * step + 20 * (1 - g), width: B.w, display: 'flex', gap: B.pt ? 26 : 40, alignItems: 'baseline', opacity: g}}>
            <div style={{width: B.pt ? 44 : 56, flexShrink: 0, fontFamily: CLAUDE_FONT.mono, fontSize: B.pt ? 40 : 44, color: hot ? ACC : MUTE}}>{i + 1}</div>
            <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 64 : 74, lineHeight: 1.1, color: hot ? ACC : INK}}>{ln}</div>
          </div>
        );
      })}
      <Note B={B} text={data.closer} opacity={win(p, 0.86, 0.94)} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B02 — PqShift: THEN an article page with an AD slot beside the text; NOW a chat card —
   shopper bubble, answer lines, ONE line cited (the accent). Placeholder lines only.
   ═══════════════════════════════════════════════════════════════════════════ */
export type PqShiftData = {
  slideMeta: string; thenLabel: string; thenLine: string; adLabel: string;
  nowLabel: string; nowLine: string; question: string; citedLabel: string; closer: string;
};

export const PqShift: React.FC<{data: PqShiftData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const ad = win(p, 0.12, 0.26);
  const now = win(p, 0.4, 0.48);
  const q = win(p, 0.46, 0.54);
  const cite = win(p, 0.62, 0.72);
  const L = B.pt
    ? {tx: B.x, ty: B.y + 60, tw: B.w, tCard: B.y + 200, tH: 300, nx: B.x, ny: B.y + 540, nw: B.w, nCard: B.y + 680, nH: 460, line: 50}
    : {tx: B.x, ty: B.y + 60, tw: 780, tCard: B.y + 250, tH: 540, nx: B.x + 900, ny: B.y + 60, nw: B.w - 900, nCard: B.y + 250, nH: 540, line: 58};
  const pad = B.pt ? 32 : 44;
  const textW = (L.tw - 2 * pad) * 0.58;
  const adW = (L.tw - 2 * pad) * 0.34;
  const answerW = L.nw - 2 * pad;
  return (
    <Stage B={B}>
      <Eyebrow B={B} text={data.slideMeta} opacity={win(p, 0, 0.06)} />
      {/* THEN */}
      <div style={{position: 'absolute', left: L.tx, top: L.ty, width: L.tw, opacity: win(p, 0.02, 0.1) * (1 - 0.4 * now)}}>
        <Chip text={data.thenLabel} size={B.pt ? 24 : 22} />
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: L.line, color: INK, lineHeight: 1.08, marginTop: 16}}>{data.thenLine}</div>
      </div>
      <div style={{position: 'absolute', left: L.tx, top: L.tCard, width: L.tw, height: L.tH, backgroundColor: CARD, border: `1px solid ${BORDER}`, borderRadius: 18, boxSizing: 'border-box', padding: pad, opacity: win(p, 0.04, 0.12) * (1 - 0.4 * now)}}>
        <Line w={textW * 0.9} h={B.pt ? 18 : 24} o={0.55} />
        <div style={{display: 'flex', gap: (L.tw - 2 * pad) * 0.08, marginTop: B.pt ? 24 : 36}}>
          <div style={{display: 'flex', flexDirection: 'column', gap: B.pt ? 16 : 24}}>
            {Array.from({length: B.pt ? 6 : 10}).map((_, i) => <Line key={i} w={textW * (i % 4 === 3 ? 0.7 : 1)} h={B.pt ? 10 : 12} o={0.18} />)}
          </div>
          <div style={{position: 'relative', width: adW, height: B.pt ? 170 : 330, border: `2px solid ${INK}`, boxSizing: 'border-box', overflow: 'hidden'}}>
            <div style={{position: 'absolute', left: 0, bottom: 0, width: '100%', height: `${ad * 100}%`, backgroundColor: INK, opacity: 0.14}} />
            <div style={{position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: CLAUDE_FONT.ui, fontWeight: 700, letterSpacing: '.2em', fontSize: B.pt ? 34 : 40, color: INK, opacity: ad}}>{data.adLabel}</div>
          </div>
        </div>
      </div>

      {/* NOW */}
      <div style={{position: 'absolute', left: L.nx, top: L.ny, width: L.nw, opacity: now}}>
        <Chip text={data.nowLabel} size={B.pt ? 24 : 22} />
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: L.line, color: INK, lineHeight: 1.08, marginTop: 16}}>{data.nowLine}</div>
      </div>
      <div style={{position: 'absolute', left: L.nx, top: L.nCard, width: L.nw, height: L.nH, backgroundColor: CARD, border: `1px solid ${BORDER}`, borderRadius: 18, boxSizing: 'border-box', padding: pad, opacity: now, boxShadow: '0 10px 30px rgba(61,57,41,0.06)'}}>
        <div style={{display: 'flex', justifyContent: 'flex-end', opacity: q, transform: `translateY(${14 * (1 - q)}px)`}}>
          <div style={{backgroundColor: STAGE, borderRadius: 20, padding: B.pt ? '16px 26px' : '20px 32px', fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 40 : 46, color: INK}}>{data.question}</div>
        </div>
        <div style={{display: 'flex', flexDirection: 'column', gap: B.pt ? 26 : 34, marginTop: B.pt ? 36 : 54}}>
          {Array.from({length: 4}).map((_, i) => {
            const g = win(p, 0.52 + i * 0.025, 0.58 + i * 0.025);
            const w = answerW * (i === 3 ? 0.5 : 0.92);
            if (i === 1) {
              return (
                <div key={i} style={{display: 'flex', alignItems: 'center', gap: 18, opacity: g}}>
                  <div style={{position: 'relative', width: w - 170, height: B.pt ? 16 : 20}}>
                    <div style={{position: 'absolute', inset: 0, borderRadius: 10, backgroundColor: INK, opacity: 0.2}} />
                    <div style={{position: 'absolute', left: 0, top: 0, bottom: 0, width: `${cite * 100}%`, borderRadius: 10, backgroundColor: ACC}} />
                  </div>
                  <div style={{opacity: win(p, 0.68, 0.74)}}><Chip text={data.citedLabel} hot size={B.pt ? 22 : 22} /></div>
                </div>
              );
            }
            return <div key={i} style={{opacity: g}}><Line w={w} h={B.pt ? 13 : 16} o={0.2} /></div>;
          })}
        </div>
      </div>
      <Note B={B} text={data.closer} opacity={win(p, 0.84, 0.93)} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B04 — PqService: the publisher card sells brands one outcome — a cited line inside an
   AI answer (ChatGPT · Gemini). A struck AD box: not a banner. Then exactly `paidCount`
   filled tokens + ONE dashed open token ("at least" — the rest is not reported).
   ═══════════════════════════════════════════════════════════════════════════ */
export type PqServiceData = {
  slideMeta: string; publisher: string; titles: string[]; question: string; engines: string[];
  outcome: string; notLabel: string; paidValue: string; paidCount: number; paidLabel: string;
  unknownLabel: string; source: string;
};

export const PqService: React.FC<{data: PqServiceData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const pub = win(p, 0.03, 0.1);
  const card = win(p, 0.24, 0.32);
  const q = win(p, 0.3, 0.38);
  const cite = win(p, 0.44, 0.54);
  const notG = win(p, 0.58, 0.62);
  const notStrike = win(p, 0.6, 0.66);
  const paidHead = win(p, 0.74, 0.8);

  const L = B.pt
    ? {pubX: B.x, pubY: B.y + 70, pubW: 600, pubH: 270, adX: B.x + 640, adY: B.y + 110, adW: 266, adH: 190,
       cardX: B.x, cardY: B.y + 420, cardW: B.w, cardH: 450, rowY: B.y + 920, tokX: B.x + 470, tok: 84}
    : {pubX: B.x, pubY: B.y + 70, pubW: 560, pubH: 330, adX: B.x, adY: B.y + 470, adW: 560, adH: 150,
       cardX: B.x + 700, cardY: B.y + 70, cardW: B.w - 700, cardH: 550, rowY: B.y + 680, tokX: B.x + 1150, tok: 96};
  const pad = B.pt ? 30 : 40;
  const lineW = L.cardW - 2 * pad;
  // connector: publisher → the cited line
  const ax1 = B.pt ? L.pubX + 120 : L.pubX + L.pubW + 14;
  const ay1 = B.pt ? L.pubY + L.pubH + 10 : L.pubY + 170;
  const ax2 = B.pt ? L.pubX + 120 : L.cardX - 14;
  const ay2 = B.pt ? L.cardY - 12 : L.pubY + 170;
  const arrowG = win(p, 0.4, 0.5);
  return (
    <Stage B={B}>
      <Eyebrow B={B} text={data.slideMeta} opacity={win(p, 0, 0.06)} />

      {/* publisher */}
      <div style={{position: 'absolute', left: L.pubX, top: L.pubY, width: L.pubW, height: L.pubH, backgroundColor: CARD, border: `1px solid ${BORDER}`, borderRadius: 18, boxSizing: 'border-box', padding: pad, opacity: pub, transform: `translateY(${16 * (1 - pub)}px)`}}>
        <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 22 : 22, letterSpacing: '.16em', fontWeight: 600, color: MUTE}}>PUBLISHER</div>
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 54 : 62, lineHeight: 1.05, color: INK, marginTop: 14}}>{data.publisher}</div>
        <div style={{display: 'flex', gap: 12, flexWrap: 'wrap', marginTop: B.pt ? 18 : 26}}>
          {data.titles.map((t, i) => (
            <div key={i} style={{opacity: win(p, 0.1 + i * 0.04, 0.16 + i * 0.04)}}><Chip text={t} size={B.pt ? 22 : 22} /></div>
          ))}
        </div>
      </div>

      {/* not a banner */}
      <div style={{position: 'absolute', left: L.adX, top: L.adY, width: L.adW, height: L.adH, opacity: notG, display: 'flex', alignItems: 'center', gap: 24}}>
        <div style={{position: 'relative', width: B.pt ? 120 : 150, height: B.pt ? 90 : 110, flexShrink: 0, border: `2px solid ${INK}`, boxSizing: 'border-box', display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: CLAUDE_FONT.ui, fontWeight: 700, letterSpacing: '.2em', fontSize: B.pt ? 26 : 30, color: INK, opacity: 1 - 0.45 * notStrike}}>
          AD
          <svg width="100%" height="100%" style={{position: 'absolute', inset: 0}} viewBox="0 0 100 100" preserveAspectRatio="none">
            <line x1={0} y1={100} x2={100 * notStrike} y2={100 - 100 * notStrike} stroke={INK} strokeWidth={3} vectorEffect="non-scaling-stroke" />
          </svg>
        </div>
        <div style={{fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: B.pt ? 40 : 46, lineHeight: 1.1, color: INK}}>{data.notLabel}</div>
      </div>

      {/* connector */}
      <svg width={1920} height={1920} style={{position: 'absolute', left: 0, top: 0, opacity: arrowG}}>
        <defs>
          <marker id="pqSvcArr" markerWidth="12" markerHeight="12" refX="9" refY="6" orient="auto">
            <path d="M0,0 L12,6 L0,12 z" fill={INK} />
          </marker>
        </defs>
        <line x1={ax1} y1={ay1} x2={ax1 + (ax2 - ax1) * arrowG} y2={ay1 + (ay2 - ay1) * arrowG} stroke={INK} strokeWidth={4} strokeDasharray="14 10" markerEnd="url(#pqSvcArr)" opacity={0.7} />
      </svg>

      {/* AI answer */}
      <div style={{position: 'absolute', left: L.cardX, top: L.cardY, width: L.cardW, height: L.cardH, backgroundColor: CARD, border: `1px solid ${BORDER}`, borderRadius: 18, boxSizing: 'border-box', padding: pad, opacity: card, boxShadow: '0 10px 30px rgba(61,57,41,0.06)'}}>
        <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: 16}}>
          <div style={{display: 'flex', gap: 12}}>
            {data.engines.map((e, i) => <div key={i} style={{opacity: win(p, 0.34 + i * 0.03, 0.4 + i * 0.03)}}><Chip text={e} size={B.pt ? 22 : 22} /></div>)}
          </div>
          <div style={{backgroundColor: STAGE, borderRadius: 20, padding: B.pt ? '14px 22px' : '18px 28px', fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 36 : 42, color: INK, opacity: q, whiteSpace: 'nowrap'}}>{data.question}</div>
        </div>
        <div style={{display: 'flex', flexDirection: 'column', gap: B.pt ? 30 : 38, marginTop: B.pt ? 40 : 56}}>
          {Array.from({length: 4}).map((_, i) => {
            const g = win(p, 0.36 + i * 0.02, 0.42 + i * 0.02);
            const w = lineW * (i === 3 ? 0.5 : 0.94);
            if (i === 1) {
              return (
                <div key={i} style={{opacity: g}}>
                  <div style={{position: 'relative', width: w, height: B.pt ? 18 : 22}}>
                    <div style={{position: 'absolute', inset: 0, borderRadius: 11, backgroundColor: INK, opacity: 0.2}} />
                    <div style={{position: 'absolute', left: 0, top: 0, bottom: 0, width: `${cite * 100}%`, borderRadius: 11, backgroundColor: ACC}} />
                  </div>
                  <div style={{fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: B.pt ? 40 : 46, color: ACC, marginTop: 14, opacity: win(p, 0.5, 0.56)}}>{data.outcome}</div>
                </div>
              );
            }
            return <div key={i} style={{opacity: g}}><Line w={w} h={B.pt ? 14 : 16} o={0.2} /></div>;
          })}
        </div>
      </div>

      {/* paid row */}
      <div style={{position: 'absolute', left: B.pt ? B.x : B.x + 700, top: L.rowY, width: B.pt ? 440 : 440, opacity: paidHead}}>
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 84 : 92, lineHeight: 1, color: INK}}>{data.paidValue}</div>
        <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 30 : 32, fontWeight: 600, lineHeight: 1.2, color: INK, marginTop: 12}}>{data.paidLabel}</div>
      </div>
      <div style={{position: 'absolute', left: L.tokX, top: L.rowY + 4, display: 'flex', gap: B.pt ? 16 : 22, alignItems: 'flex-start'}}>
        {Array.from({length: data.paidCount}).map((_, i) => {
          const g = win(p, 0.76 + i * 0.035, 0.8 + i * 0.035);
          return <div key={i} style={{width: L.tok, height: L.tok, borderRadius: 14, backgroundColor: INK, opacity: 0.85 * g, transform: `scale(${0.7 + 0.3 * g})`}} />;
        })}
        <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 10, opacity: win(p, 0.88, 0.94)}}>
          <div style={{width: L.tok, height: L.tok, borderRadius: 14, border: `3px dashed ${MUTE}`, boxSizing: 'border-box', display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 44 : 50, color: MUTE}}>?</div>
        </div>
      </div>
      <div style={{position: 'absolute', left: L.tokX, top: L.rowY + L.tok + 22, width: B.pt ? 436 : 600, fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 26 : 27, color: MUTE, opacity: win(p, 0.88, 0.94)}}>{data.unknownLabel}</div>
      <Source B={B} source={data.source} opacity={win(p, 0.9, 0.96)} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B05 — PqLicense: a decorative field of site marks (REQUIRED marksNote — never a count),
   each wiring its own deal line to "AI companies"; the lines collapse into ONE hub
   (the collective) and ONE accent line carries the blanket license.
   ═══════════════════════════════════════════════════════════════════════════ */
export type PqLicenseData = {
  slideMeta: string; countLabel: string; membersLabel: string; marksNote: string; beforeLabel: string;
  hub: string; hubKind: string; buyer: string; licenseLabel: string; source: string;
};

export const PqLicense: React.FC<{data: PqLicenseData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const field = win(p, 0.03, 0.12);
  const many = win(p, 0.18, 0.32) * (1 - win(p, 0.54, 0.62));
  const hubG = win(p, 0.56, 0.64);
  const conv = win(p, 0.58, 0.68);
  const lic = win(p, 0.7, 0.8);

  const F = B.pt
    ? {x: B.x + 10, y: B.y + 290, cols: 20, rows: 6, sp: 44, r: 9}
    : {x: B.x + 10, y: B.y + 90, cols: 13, rows: 11, sp: 40, r: 8};
  const dots: {x: number; y: number; i: number}[] = [];
  for (let r = 0; r < F.rows; r++) for (let c = 0; c < F.cols; c++) dots.push({x: F.x + c * F.sp, y: F.y + r * F.sp, i: r * F.cols + c});
  const fieldR = F.x + (F.cols - 1) * F.sp;
  const fieldB = F.y + (F.rows - 1) * F.sp;

  const hub = B.pt ? {x: 400, y: 850, r: 115} : {x: 1110, y: 340, r: 130};
  const box = B.pt ? {x: 180, y: 1120, w: 440, h: 110} : {x: 1520, y: 270, w: 304, h: 140};
  const boxIn = B.pt ? {x: box.x + box.w / 2, y: box.y} : {x: box.x, y: box.y + box.h / 2};
  // sampled one-to-one deal lines (deterministic)
  const sample = dots.filter((d) => (d.i * 7) % 5 === 0);
  const edge = B.pt ? dots.filter((d) => d.y === fieldB) : dots.filter((d) => d.x === fieldR);
  return (
    <Stage B={B}>
      <Eyebrow B={B} text={data.slideMeta} opacity={win(p, 0, 0.06)} />
      <svg width={1920} height={1920} style={{position: 'absolute', left: 0, top: 0}}>
        {/* one-at-a-time deals */}
        {sample.map((d, k) => {
          const ex = boxIn.x + (B.pt ? ((k % 9) - 4) * 40 : 0);
          const ey = boxIn.y + (B.pt ? 0 : ((k % 9) - 4) * 13);
          return <line key={`m${k}`} x1={d.x} y1={d.y} x2={d.x + (ex - d.x) * many} y2={d.y + (ey - d.y) * many} stroke={INK} strokeWidth={1.6} opacity={0.32 * Math.min(1, many * 3)} />;
        })}
        {/* converge into the hub */}
        {edge.map((d, k) => {
          const hx = B.pt ? hub.x : hub.x - hub.r;
          const hy = B.pt ? hub.y - hub.r : hub.y;
          return <line key={`c${k}`} x1={d.x} y1={d.y} x2={d.x + (hx - d.x) * conv} y2={d.y + (hy - d.y) * conv} stroke={INK} strokeWidth={2.4} opacity={0.5 * Math.min(1, conv * 2)} />;
        })}
        {/* the blanket license */}
        {B.pt ? (
          <line x1={hub.x} y1={hub.y + hub.r} x2={hub.x} y2={hub.y + hub.r + (box.y - hub.y - hub.r) * lic} stroke={ACC} strokeWidth={16} />
        ) : (
          <line x1={hub.x + hub.r} y1={hub.y} x2={hub.x + hub.r + (box.x - hub.x - hub.r) * lic} y2={hub.y} stroke={ACC} strokeWidth={16} />
        )}
        {dots.map((d) => (
          <circle key={d.i} cx={d.x} cy={d.y} r={F.r} fill={INK} opacity={0.55 * win(p, 0.03 + (d.i % 17) * 0.004, 0.09 + (d.i % 17) * 0.004) * field} />
        ))}
        <circle cx={hub.x} cy={hub.y} r={hub.r * (0.8 + 0.2 * hubG)} fill={CARD} stroke={INK} strokeWidth={3} opacity={hubG} />
      </svg>
      <div style={{position: 'absolute', left: hub.x - hub.r + 14, top: hub.y - (B.pt ? 56 : 62), width: 2 * hub.r - 28, textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 32 : 34, lineHeight: 1.1, color: INK, opacity: hubG}}>{data.hub}</div>
      <div style={{position: 'absolute', left: B.pt ? B.x : hub.x - 150, top: B.pt ? hub.y - 22 : hub.y + hub.r + 18, width: B.pt ? 220 : 300, textAlign: B.pt ? 'left' : 'center', opacity: hubG}}><Chip text={data.hubKind} size={22} /></div>
      {/* buyer */}
      <div style={{position: 'absolute', left: box.x, top: box.y, width: box.w, height: box.h, border: `2px solid ${INK}`, backgroundColor: CARD, boxSizing: 'border-box', display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 44 : 46, color: INK, opacity: win(p, 0.14, 0.2)}}>{data.buyer}</div>
      {/* labels */}
      <div style={{position: 'absolute', left: B.pt ? 640 : 1230, top: B.pt ? 1030 : 160, width: B.pt ? 340 : 360, fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: B.pt ? 36 : 40, color: MUTE, opacity: Math.min(1, many * 2)}}>{data.beforeLabel}</div>
      <div style={{position: 'absolute', left: B.pt ? 440 : 1256, top: B.pt ? 1010 : 364, width: B.pt ? 400 : 256, fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: B.pt ? 42 : 46, lineHeight: 1.1, color: ACC, opacity: win(p, 0.76, 0.84)}}>{data.licenseLabel}</div>
      <div style={{position: 'absolute', left: B.x, top: B.pt ? B.y + 56 : fieldB + 44, width: B.pt ? B.w : 700, opacity: win(p, 0.4, 0.5)}}>
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 76 : 84, lineHeight: 1, color: INK}}>{data.countLabel}</div>
        <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 30 : 32, fontWeight: 600, color: INK, marginTop: 10}}>{data.membersLabel}</div>
        <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 25, color: MUTE, marginTop: 8}}>{data.marksNote}</div>
      </div>
      <Source B={B} source={data.source} opacity={win(p, 0.88, 0.95)} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B06 — PqOverviews: two 10×10 waffles ("out of every 100 searches"); cells fill to each
   `cells` count; values print verbatim beneath. The later share is the accent.
   ═══════════════════════════════════════════════════════════════════════════ */
export type PqWafflePoint = {when: string; value: string; cells: number; hot: boolean};
export type PqOverviewsData = {slideMeta: string; title: string; points: PqWafflePoint[]; label: string; note: string; source: string};

export const PqOverviews: React.FC<{data: PqOverviewsData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const cell = B.pt ? 36 : 38;
  const gap = B.pt ? 6 : 8;
  const side = 10 * cell + 9 * gap;
  const top = B.pt ? B.y + 290 : B.y + 260;
  const xs = B.pt ? [B.x, B.x + side + 72] : [B.x, B.x + side + 110];
  const ats = [0.22, 0.48];
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      {data.points.map((pt, k) => {
        const at = ats[k] ?? 0.2 + k * 0.25;
        const fillTo = pt.cells * win(p, at, at + 0.14);
        const color = pt.hot ? ACC : INK;
        return (
          <React.Fragment key={k}>
            <div style={{position: 'absolute', left: xs[k], top, width: side, height: side, display: 'grid', gridTemplateColumns: `repeat(10, ${cell}px)`, gap, opacity: win(p, 0.04, 0.12)}}>
              {Array.from({length: 100}).map((_, i) => {
                const on = Math.min(1, Math.max(0, fillTo - i));
                return (
                  <div key={i} style={{width: cell, height: cell, borderRadius: 6, boxSizing: 'border-box', border: `1px solid ${RULE}`, position: 'relative'}}>
                    <div style={{position: 'absolute', inset: -1, borderRadius: 6, backgroundColor: color, opacity: 0.88 * on}} />
                  </div>
                );
              })}
            </div>
            <div style={{position: 'absolute', left: xs[k], top: top + side + 24, width: side, display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', gap: 16}}>
              <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 30 : 32, fontWeight: 600, color: INK, opacity: win(p, at - 0.04, at + 0.02)}}>{pt.when}</div>
              <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 92 : 100, lineHeight: 1, color, opacity: win(p, at + 0.08, at + 0.16)}}>{pt.value}</div>
            </div>
          </React.Fragment>
        );
      })}
      <div style={{position: 'absolute', left: B.pt ? B.x : B.x + 2 * side + 200, top: B.pt ? top + side + 150 : top + 20, width: B.pt ? B.w : B.w - 2 * side - 200, opacity: win(p, 0.72, 0.8)}}>
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 54 : 60, lineHeight: 1.12, color: INK}}>{data.label}</div>
        <div style={{fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: B.pt ? 42 : 44, lineHeight: 1.2, color: INK, marginTop: B.pt ? 30 : 48, opacity: win(p, 0.82, 0.9)}}>{data.note}</div>
      </div>
      <Source B={B} source={data.source} opacity={win(p, 0.84, 0.92)} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B07 — PqStack: three layers built bottom-up in narration order (search → service →
   supply), each with its own source line; an accent bracket spans them; the closer
   strikes the old word and sets the new one.
   ═══════════════════════════════════════════════════════════════════════════ */
export type PqLayer = {tag: string; line: string; src: string};
export type PqStackData = {slideMeta: string; title: string; layers: PqLayer[]; bracket: string; oldWord: string; newWord: string};

export const PqStack: React.FC<{data: PqStackData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const n = data.layers.length;
  const h = B.pt ? 236 : 150;
  const g = B.pt ? 22 : 22;
  const top = B.pt ? B.y + 230 : B.y + 250;
  const w = B.pt ? B.w : 1340;
  const ats = [0.06, 0.26, 0.46];
  const br = win(p, 0.66, 0.76);
  const stackB = top + n * h + (n - 1) * g;
  const strike = win(p, 0.84, 0.9);
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      {data.layers.map((L, i) => {
        // i = 0 is the BASE (bottom) layer
        const y = top + (n - 1 - i) * (h + g);
        const at = ats[i] ?? 0.1 + i * 0.2;
        const k = win(p, at, at + 0.1);
        return (
          <div key={i} style={{position: 'absolute', left: B.x, top: y + 24 * (1 - k), width: w, height: h, backgroundColor: CARD, border: `1px solid ${BORDER}`, borderRadius: 16, boxSizing: 'border-box', padding: B.pt ? '22px 30px' : '0 36px', display: 'flex', flexDirection: B.pt ? 'column' : 'row', alignItems: B.pt ? 'flex-start' : 'center', gap: B.pt ? 12 : 36, opacity: k}}>
            <div style={{width: B.pt ? 'auto' : 190, flexShrink: 0}}><Chip text={L.tag} size={B.pt ? 24 : 24} /></div>
            <div>
              <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 42 : 46, lineHeight: 1.12, color: INK}}>{L.line}</div>
              <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 24 : 24, color: MUTE, marginTop: 8}}>{L.src}</div>
            </div>
          </div>
        );
      })}
      {B.pt ? (
        <>
          <div style={{position: 'absolute', left: B.x, top: stackB + 26, width: B.w * br, height: 6, backgroundColor: ACC}} />
          <div style={{position: 'absolute', left: B.x, top: stackB + 46, width: B.w, fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: 46, color: ACC, opacity: win(p, 0.7, 0.78)}}>{data.bracket}</div>
        </>
      ) : (
        <>
          <svg width={1920} height={1080} style={{position: 'absolute', left: 0, top: 0, opacity: br}}>
            <path d={`M ${B.x + w + 30} ${top} h 24 V ${top + (stackB - top) * br} h -24`} fill="none" stroke={ACC} strokeWidth={6} />
          </svg>
          <div style={{position: 'absolute', left: B.x + w + 80, top: top + (stackB - top) / 2 - 90, width: B.r - (B.x + w + 80), fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: 44, lineHeight: 1.12, color: ACC, opacity: win(p, 0.7, 0.78)}}>{data.bracket}</div>
        </>
      )}
      <div style={{position: 'absolute', left: B.x, top: B.pt ? 1300 : stackB + 46, width: B.w, display: 'flex', flexWrap: 'wrap', alignItems: 'baseline', gap: 24, opacity: win(p, 0.8, 0.86)}}>
        <span style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 30 : 32, fontWeight: 600, color: MUTE}}>Getting cited:</span>
        <Struck text={data.oldWord} g={strike} size={B.pt ? 50 : 54} />
        <span style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 50 : 54, color: INK, opacity: win(p, 0.88, 0.94)}}>→ {typed(data.newWord, win(p, 0.88, 0.96))}</span>
      </div>
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B08 — PqLimits: what we know vs what we don't know yet; REQUIRES provenance and a
   falsifier string, so the falsifiability beat cannot be authored without them.
   ═══════════════════════════════════════════════════════════════════════════ */
export type PqList = {heading: string; items: string[]};
export type PqLimitsData = {slideMeta: string; title: string; found: PqList; notFound: PqList; provenance: string; falsifier: string};

export const PqLimits: React.FC<{data: PqLimitsData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const colW = B.pt ? B.w : 820;
  const itemStep = B.pt ? 64 : 78;
  const cols = [
    {list: data.found, x: B.x, y: B.y + 260, at: 0.12, mark: 'yes' as const},
    {list: data.notFound, x: B.pt ? B.x : B.x + 900, y: B.pt ? B.y + 260 + 80 + data.found.items.length * itemStep + 50 : B.y + 260, at: 0.46, mark: 'no' as const},
  ];
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      {cols.map((c, ci) => (
        <React.Fragment key={ci}>
          <div style={{position: 'absolute', left: c.x, top: c.y, width: colW, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 44 : 48, color: INK, opacity: win(p, 0.06, 0.12), borderBottom: `1px solid ${RULE}`, paddingBottom: 10}}>{c.list.heading}</div>
          {c.list.items.map((it, i) => {
            const at = c.at + i * 0.06;
            return (
              <div key={i} style={{position: 'absolute', left: c.x, top: c.y + (B.pt ? 84 : 100) + i * itemStep, width: colW, display: 'flex', alignItems: 'center', gap: 20, opacity: win(p, at, at + 0.06)}}>
                {c.mark === 'yes'
                  ? <div style={{width: 18, height: 18, borderRadius: 9, backgroundColor: INK, flexShrink: 0}} />
                  : <div style={{width: 18, height: 18, borderRadius: 9, border: `2px solid ${INK}`, boxSizing: 'border-box', flexShrink: 0}} />}
                <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 32 : 35, lineHeight: 1.2, color: INK}}>{it}</div>
              </div>
            );
          })}
        </React.Fragment>
      ))}
      <div style={{position: 'absolute', left: B.x, top: B.pt ? 1150 : SAFE.b - 250, width: B.w, fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: B.pt ? 42 : 48, lineHeight: 1.2, color: ACC, opacity: win(p, 0.8, 0.88)}}>{data.falsifier}</div>
      <div style={{position: 'absolute', left: B.x, top: B.pt ? 1290 : SAFE.b - 128, width: B.w - (B.pt ? 0 : 220), fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 26 : 25, lineHeight: 1.35, color: MUTE, opacity: win(p, 0.84, 0.92)}}>Sources: {data.provenance}</div>
    </Stage>
  );
};
