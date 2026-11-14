/**
 * WhatWeAskFor.tsx — reel-local scenes for `yatra-what-we-ask-for`
 * ("What We Ask For." — redefining human creativity and labor when a machine can draft a
 * novel or paint an image in seconds).
 *
 * ── WHY THESE ARE NEW COMPONENTS ─────────────────────────────────────────────
 * The human asked for a new video, not a variation. No earlier family (Seo*, Geo*, Ctr*,
 * …) is reused. Shapes come from this reel's argument: a struck fear line, a schematic
 * of expected-vs-found earnings, two isotype rows (1 in 4 vs 1 in 5), a three-stage
 * creative process where judgment stays with the artist, a pay-premium range band, a
 * 100-square disclosure grid beside the Article 50 rule, two workflow lanes, five human
 * layers above the draft, a definition fork, and a limits page.
 *
 * ── ONE COMPONENT, BOTH ASPECTS ──────────────────────────────────────────────
 * Each scene reads the composition size and lays out for 16:9 or 9:16 (stacked, re-banded
 * — never scaled). Portrait keeps content above y≈1440 and left of x≈960 (platform UI
 * keep-out) and moves the @Yatra bug lower-left. Root.tsx registers each scene twice:
 * `WwaX` at 1920×1080 and `WwaX916` at 1080×1920. Length is a prop (`data.durationS`,
 * the MEASURED Kokoro length) read by calculateMetadata — no hand-tuned frame counts.
 *
 * ── THE SOURCING CONSTRAINT, ENFORCED BY THE TYPES ───────────────────────────
 * Seven supplied findings, no others. So:
 *   · Every figure-bearing scene REQUIRES a `source` string (muted ink, never accent).
 *   · Displayed values are verbatim STRINGS; numeric props (`lit`, `bar`) only draw.
 *   · WwaEarnings plots NO data: it is captioned as a schematic (direction only).
 *   · WwaPremium's baseline carries a label, never a number.
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

const ease = (t: number) => 1 - Math.pow(1 - Math.min(1, Math.max(0, t)), 3);
const win = (p: number, a: number, b: number) => ease((p - a) / (b - a));
const typed = (text: string, g: number) => text.slice(0, Math.round(text.length * g));

const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

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
    <Eyebrow B={B} text={meta} opacity={win(p, 0.0, 0.06)} />
    <div style={{position: 'absolute', left: B.x, top: B.y + (B.pt ? 60 : 56), width: B.w, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 66 : 76, color: INK, lineHeight: 1.06, opacity: win(p, 0.02, 0.08)}}>
      {title}
    </div>
  </>
);

/** Provenance: always muted ink, never the accent. */
const Source: React.FC<{B: Box; source: string; opacity: number; top?: number}> = ({B, source, opacity, top}) => (
  <div style={{position: 'absolute', left: B.x, top: top ?? (B.pt ? 1300 : SAFE.b - 120), width: B.pt ? B.w : B.w - 220, fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 26 : 25, lineHeight: 1.3, color: MUTE, opacity}}>
    Source: {source}
  </div>
);

const Note: React.FC<{B: Box; text: string; opacity: number; top?: number; italic?: boolean}> = ({B, text, opacity, top, italic}) => (
  <div style={{position: 'absolute', left: B.x, top: top ?? (B.pt ? 1180 : SAFE.b - 196), width: B.pt ? B.w : B.w - 220, fontFamily: CLAUDE_FONT.serif, fontStyle: italic ? 'italic' : 'normal', fontSize: B.pt ? 42 : 44, color: INK, opacity, lineHeight: 1.2}}>
    {text}
  </div>
);

const Chip: React.FC<{text: string; hot?: boolean; size?: number}> = ({text, hot, size = 22}) => (
  <span style={{fontFamily: CLAUDE_FONT.ui, fontSize: size, fontWeight: 600, letterSpacing: '.14em', textTransform: 'uppercase', color: hot ? ACC : INK, border: `${hot ? 2 : 1}px solid ${hot ? ACC : RULE}`, padding: '10px 18px', display: 'inline-block', whiteSpace: 'nowrap', backgroundColor: CARD}}>
    {text}
  </span>
);

const Arrow: React.FC<{x1: number; y1: number; x2: number; y2: number; g: number; id: string; color?: string; dashed?: boolean}> = ({x1, y1, x2, y2, g, id, color = INK, dashed}) => (
  <svg width={1920} height={1920} style={{position: 'absolute', left: 0, top: 0, opacity: g}}>
    <defs>
      <marker id={id} markerWidth="12" markerHeight="12" refX="9" refY="6" orient="auto">
        <path d="M0,0 L12,6 L0,12 z" fill={color} />
      </marker>
    </defs>
    <line x1={x1} y1={y1} x2={x1 + (x2 - x1) * g} y2={y1 + (y2 - y1) * g} stroke={color} strokeWidth={4} strokeDasharray={dashed ? '12 9' : undefined} markerEnd={`url(#${id})`} opacity={0.75} />
  </svg>
);

/* ═══════════════════════════════════════════════════════════════════════════
   WwaBluf — the fear line is struck through on the spoken contrast; the replacement
   types in beneath it; three chips land in narration order.
   ═══════════════════════════════════════════════════════════════════════════ */
export type WwaBlufData = {slideMeta: string; old: string; replacement: string; chips: string[]; closer: string; durationS?: number};

export const WwaBluf: React.FC<{data: WwaBlufData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const strike = win(p, 0.22, 0.32);
  const rep = win(p, 0.3, 0.46);
  const big = B.pt ? 92 : 112;
  const oldTop = B.pt ? B.y + 150 : B.y + 140;
  const repTop = B.pt ? B.y + 420 : B.y + 330;
  const chipsTop = B.pt ? B.y + 700 : B.y + 590;
  return (
    <Stage B={B}>
      <Eyebrow B={B} text={data.slideMeta} opacity={win(p, 0, 0.06)} />
      <div style={{position: 'absolute', left: B.x, top: oldTop, width: B.w, opacity: win(p, 0.02, 0.1) * (1 - 0.5 * strike)}}>
        <span style={{position: 'relative', display: 'inline-block', fontFamily: CLAUDE_FONT.serif, fontSize: big, lineHeight: 1.08, color: INK}}>
          {data.old}
          <span style={{position: 'absolute', left: 0, top: '54%', height: B.pt ? 7 : 8, width: `${strike * 100}%`, backgroundColor: INK}} />
        </span>
      </div>
      <div style={{position: 'absolute', left: B.x, top: repTop, width: B.w, fontFamily: CLAUDE_FONT.serif, fontSize: big, lineHeight: 1.08, color: INK, opacity: rep > 0 ? 1 : 0}}>
        {typed(data.replacement, rep)}
        <div style={{height: B.pt ? 7 : 8, width: `${win(p, 0.44, 0.52) * (B.pt ? 100 : 62)}%`, backgroundColor: ACC, marginTop: 14}} />
      </div>
      <div style={{position: 'absolute', left: B.x, top: chipsTop, width: B.w, display: 'flex', flexDirection: B.pt ? 'column' : 'row', gap: B.pt ? 26 : 28, flexWrap: 'wrap'}}>
        {data.chips.map((c, i) => {
          const g = win(p, 0.52 + i * 0.1, 0.6 + i * 0.1);
          return (
            <div key={i} style={{opacity: g, transform: `translateY(${(1 - g) * 18}px)`}}>
              <Chip text={c} size={B.pt ? 32 : 30} />
            </div>
          );
        })}
      </div>
      <Note B={B} text={data.closer} italic opacity={win(p, 0.86, 0.94)} top={B.pt ? 1100 : SAFE.b - 150} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   WwaAct — part card: eyebrow + serif title + terracotta period + hairline.
   ═══════════════════════════════════════════════════════════════════════════ */
export type WwaActData = {index: string; title: string; durationS?: number};

export const WwaAct: React.FC<{data: WwaActData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const a = win(p, 0, 0.25);
  const t = win(p, 0.08, 0.35);
  const top = B.pt ? B.y + 480 : B.y + 330;
  return (
    <Stage B={B}>
      <div style={{position: 'absolute', left: B.x, top, width: B.w, opacity: a, transform: `translateY(${(1 - a) * 24}px)`}}>
        <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 30 : 28, letterSpacing: '.2em', fontWeight: 600, color: MUTE}}>{data.index.toUpperCase()}</div>
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 110 : 140, lineHeight: 1.04, color: INK, marginTop: 26, opacity: t}}>
          {data.title}<span style={{color: ACC}}>.</span>
        </div>
        <div style={{height: 2, width: `${t * (B.pt ? 90 : 46)}%`, backgroundColor: INK, opacity: 0.35, marginTop: 34}} />
      </div>
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   WwaEarnings — SCHEMATIC, NO DATA. From one starting point, a dashed "expected" path
   falls steeply; the solid "found" path (the accent) holds. Captioned as direction-only.
   ═══════════════════════════════════════════════════════════════════════════ */
export type WwaEarningsData = {slideMeta: string; title: string; expected: string; found: string; finding: string; schematic: string; source: string; durationS?: number};

export const WwaEarnings: React.FC<{data: WwaEarningsData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const C = B.pt
    ? {x0: B.x + 20, y0: B.y + 300, w: 620, h: 430}
    : {x0: B.x + 20, y0: B.y + 250, w: 900, h: 470};
  const startY = C.y0 + C.h * 0.28;
  const exp = win(p, 0.14, 0.36);
  const fnd = win(p, 0.4, 0.62);
  const expEnd = {x: C.x0 + C.w, y: C.y0 + C.h * 0.94};
  const fndEnd = {x: C.x0 + C.w, y: startY + C.h * 0.04};
  const expPath = `M ${C.x0} ${startY} C ${C.x0 + C.w * 0.35} ${startY}, ${C.x0 + C.w * 0.55} ${expEnd.y}, ${expEnd.x} ${expEnd.y}`;
  const fndPath = `M ${C.x0} ${startY} C ${C.x0 + C.w * 0.3} ${startY - 14}, ${C.x0 + C.w * 0.6} ${startY + 22}, ${fndEnd.x} ${fndEnd.y}`;
  const L = 1400;
  const textX = B.pt ? B.x : B.x + 1010;
  const textW = B.pt ? B.w : B.w - 1010;
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      <svg width={1920} height={1920} style={{position: 'absolute', left: 0, top: 0}}>
        <line x1={C.x0} y1={C.y0 + C.h} x2={C.x0 + C.w} y2={C.y0 + C.h} stroke={INK} strokeWidth={3} opacity={0.5 * win(p, 0.04, 0.1)} />
        <line x1={C.x0} y1={C.y0} x2={C.x0} y2={C.y0 + C.h} stroke={INK} strokeWidth={3} opacity={0.5 * win(p, 0.04, 0.1)} />
        <defs>
          <clipPath id="wwaExpClip">
            <rect x={C.x0 - 10} y={C.y0 - 40} width={(C.w + 20) * exp} height={C.h + 80} />
          </clipPath>
        </defs>
        <path d={expPath} fill="none" stroke={INK} strokeWidth={6} strokeDasharray="18 14" opacity={0.7} clipPath="url(#wwaExpClip)" />
        <path d={fndPath} fill="none" stroke={ACC} strokeWidth={9} strokeLinecap="round" pathLength={L} strokeDasharray={`${L * fnd} ${L}`} />
        <circle cx={C.x0} cy={startY} r={12} fill={INK} opacity={win(p, 0.08, 0.14)} />
      </svg>
      {/* legend under the axis — keeps labels off the paths */}
      <div style={{position: 'absolute', left: C.x0, top: C.y0 + C.h + 20, width: B.pt ? B.w : C.w + 60, display: 'flex', flexDirection: B.pt ? 'column' : 'row', gap: B.pt ? 10 : 40}}>
        <div style={{display: 'flex', alignItems: 'center', gap: 14, opacity: win(p, 0.3, 0.38)}}>
          <svg width={60} height={10}><line x1={0} y1={5} x2={60} y2={5} stroke={INK} strokeWidth={5} strokeDasharray="12 8" opacity={0.7} /></svg>
          <span style={{fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: B.pt ? 34 : 34, color: INK}}>{data.expected}</span>
        </div>
        <div style={{display: 'flex', alignItems: 'center', gap: 14, opacity: win(p, 0.56, 0.64)}}>
          <svg width={60} height={10}><line x1={0} y1={5} x2={60} y2={5} stroke={ACC} strokeWidth={8} /></svg>
          <span style={{fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: B.pt ? 34 : 34, color: ACC}}>{data.found}</span>
        </div>
      </div>
      <div style={{position: 'absolute', left: C.x0, top: C.y0 + C.h + (B.pt ? 118 : 74), width: B.pt ? B.w : C.w, fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 24 : 24, color: MUTE, opacity: win(p, 0.1, 0.18)}}>{data.schematic}</div>
      <div style={{position: 'absolute', left: textX, top: B.pt ? B.y + 900 : B.y + 290, width: textW, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 54 : 58, lineHeight: 1.14, color: INK, opacity: win(p, 0.62, 0.72)}}>
        {data.finding}
      </div>
      <Source B={B} source={data.source} opacity={win(p, 0.7, 0.8)} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   WwaAdoption — two isotype rows of 20. `lit` people light in sequence on the spoken
   figure; the artists' row is the accent. Values print verbatim.
   ═══════════════════════════════════════════════════════════════════════════ */
export type WwaPeopleRow = {label: string; value: string; lit: number; of: number; hot: boolean};
export type WwaAdoptionData = {slideMeta: string; title: string; rows: WwaPeopleRow[]; note: string; source: string; durationS?: number};

const Person: React.FC<{w: number; on: number; hot: boolean}> = ({w, on, hot}) => {
  const color = hot ? ACC : INK;
  const h = w * 2.1;
  return (
    <svg width={w} height={h} viewBox="0 0 50 105" style={{display: 'block'}}>
      <circle cx={25} cy={14} r={12} fill={on > 0.5 ? color : 'none'} stroke={on > 0.5 ? color : INK} strokeWidth={3} opacity={on > 0.5 ? 1 : 0.45} />
      <path d="M6 100 L6 46 Q6 32 25 32 Q44 32 44 46 L44 100 Z" fill={on > 0.5 ? color : 'none'} stroke={on > 0.5 ? color : INK} strokeWidth={3} opacity={on > 0.5 ? 1 : 0.45} />
    </svg>
  );
};

export const WwaAdoption: React.FC<{data: WwaAdoptionData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const ats = [0.14, 0.42];
  const perLine = B.pt ? 10 : 20;
  const pw = B.pt ? 60 : 52;
  const gap = B.pt ? 12 : 8;
  const labelW = B.pt ? B.w : 470;
  const rowTop = (i: number) => (B.pt ? B.y + 230 + i * 450 : B.y + 250 + i * 290);
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      {data.rows.map((r, i) => {
        const at = ats[i] ?? 0.2 + i * 0.25;
        const top = rowTop(i);
        const peopleX = B.pt ? B.x : B.x + labelW + 20;
        const peopleY = B.pt ? top + 140 : top;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: B.x, top: B.pt ? top : top + 4, width: labelW, opacity: win(p, at - 0.04, at + 0.04)}}>
              <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 76 : 76, lineHeight: 1, color: r.hot ? ACC : INK}}>{r.value}</div>
              <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 30 : 30, fontWeight: 600, lineHeight: 1.25, color: INK, marginTop: 12}}>{r.label}</div>
            </div>
            <div style={{position: 'absolute', left: peopleX, top: peopleY, width: perLine * pw + (perLine - 1) * gap, display: 'flex', flexWrap: 'wrap', columnGap: gap, rowGap: 18, opacity: win(p, at - 0.06, at)}}>
              {Array.from({length: r.of}).map((_, k) => {
                const on = k < r.lit ? win(p, at + 0.04 + k * 0.025, at + 0.06 + k * 0.025) : 0;
                return <Person key={k} w={pw} on={on} hot={r.hot} />;
              })}
            </div>
          </React.Fragment>
        );
      })}
      <Note B={B} text={data.note} italic opacity={win(p, 0.72, 0.82)} top={B.pt ? 1222 : SAFE.b - 200} />
      <Source B={B} source={data.source} opacity={win(p, 0.66, 0.76)} top={B.pt ? 1330 : SAFE.b - 110} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   WwaUses — three stages of the creative process in narration order. The first two take
   an "AI helps" chip; the last — judgment — is the artist's (the accent).
   ═══════════════════════════════════════════════════════════════════════════ */
export type WwaStage = {label: string; tag: string; mine: boolean};
export type WwaUsesData = {slideMeta: string; title: string; stages: WwaStage[]; note: string; source: string; durationS?: number};

export const WwaUses: React.FC<{data: WwaUsesData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const n = data.stages.length;
  const gapX = 80;
  const cw = B.pt ? B.w : (B.w - gapX * (n - 1)) / n;
  const ch = B.pt ? 210 : 330;
  const top0 = B.pt ? B.y + 250 : B.y + 270;
  const stepY = B.pt ? 270 : 0;
  const ats = [0.14, 0.26, 0.44];
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      {data.stages.map((s, i) => {
        const at = ats[i] ?? 0.2 + i * 0.12;
        const g = win(p, at, at + 0.08);
        const x = B.pt ? B.x : B.x + i * (cw + gapX);
        const y = top0 + i * stepY;
        const ring = s.mine ? win(p, at + 0.08, at + 0.16) : 0;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: x, top: y, width: cw, height: ch, boxSizing: 'border-box', backgroundColor: CARD, border: `${s.mine ? 3 : 1}px solid ${s.mine ? (ring > 0.5 ? ACC : RULE) : RULE}`, borderRadius: 20, padding: B.pt ? '30px 36px' : '40px 40px', opacity: g, transform: `translateY(${(1 - g) * 20}px)`, display: 'flex', flexDirection: 'column', justifyContent: 'space-between'}}>
              <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 24 : 24, letterSpacing: '.16em', fontWeight: 600, color: MUTE}}>STEP {i + 1}</div>
              <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 58 : 60, lineHeight: 1.05, color: INK}}>{s.label}</div>
              <div>
                <span style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 26 : 26, fontWeight: 600, letterSpacing: '.12em', textTransform: 'uppercase', color: s.mine ? ACC : INK, border: `${s.mine ? 2 : 1}px solid ${s.mine ? ACC : INK}`, padding: '8px 16px', opacity: s.mine ? ring : win(p, at + 0.05, at + 0.11)}}>{s.tag}</span>
              </div>
            </div>
            {i < n - 1 && (B.pt
              ? <Arrow id={`wwaU${i}`} x1={B.x + 60} y1={y + ch + 8} x2={B.x + 60} y2={y + stepY - 10} g={win(p, at + 0.06, at + 0.12)} />
              : <Arrow id={`wwaU${i}`} x1={x + cw + 10} y1={y + ch / 2} x2={x + cw + gapX - 12} y2={y + ch / 2} g={win(p, at + 0.06, at + 0.12)} />)}
          </React.Fragment>
        );
      })}
      <Note B={B} text={data.note} italic opacity={win(p, 0.68, 0.78)} top={B.pt ? 1080 : B.y + 680} />
      <Source B={B} source={data.source} opacity={win(p, 0.6, 0.7)} top={B.pt ? 1300 : SAFE.b - 110} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   WwaPremium — baseline bar (labelled, NO number) vs an AI-proficient bar whose end is a
   RANGE band from lo to hi (the accent). The value prints verbatim.
   ═══════════════════════════════════════════════════════════════════════════ */
export type WwaPremiumData = {
  slideMeta: string; title: string;
  baseLabel: string; proLabel: string;
  value: string; lo: number; hi: number; loTag: string; hiTag: string;
  note: string; source: string; durationS?: number;
};

export const WwaPremium: React.FC<{data: WwaPremiumData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const labelW = B.pt ? 0 : 470;
  const TX = B.x + labelW;
  const unit = B.pt ? 600 : 720;                 // baseline length in px
  const barH = B.pt ? 96 : 100;
  const y0 = B.pt ? B.y + 330 : B.y + 290;
  const y1 = B.pt ? B.y + 640 : B.y + 500;
  const fb = win(p, 0.1, 0.24);
  const fp = win(p, 0.26, 0.4);
  const band = win(p, 0.4, 0.54);
  const loX = TX + unit * (1 + data.lo / 100);
  const hiX = TX + unit * (1 + data.hi / 100);
  const label = (text: string, y: number, g: number) => (
    <div style={{position: 'absolute', left: B.x, top: B.pt ? y - 70 : y + barH / 2 - 34, width: B.pt ? B.w : labelW - 30, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 42 : 42, lineHeight: 1.1, color: INK, opacity: g}}>{text}</div>
  );
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      {label(data.baseLabel, y0, win(p, 0.06, 0.14))}
      <div style={{position: 'absolute', left: TX, top: y0, width: unit * fb, height: barH, backgroundColor: INK, opacity: 0.55}} />
      {label(data.proLabel, y1, win(p, 0.22, 0.3))}
      <div style={{position: 'absolute', left: TX, top: y1, width: (loX - TX) * fp, height: barH, backgroundColor: INK, opacity: 0.85}} />
      <div style={{position: 'absolute', left: loX, top: y1, width: (hiX - loX) * band, height: barH, backgroundColor: ACC, opacity: 0.9}} />
      {/* baseline reference line */}
      <div style={{position: 'absolute', left: TX + unit, top: y0 - 20, width: 2, height: y1 + barH + 20 - (y0 - 20), backgroundColor: INK, opacity: 0.35 * win(p, 0.2, 0.28)}} />
      {[{x: loX, t: data.loTag}, {x: hiX, t: data.hiTag}].map((m, i) => (
        <div key={i} style={{position: 'absolute', left: m.x - 80, top: y1 + barH + 14, width: 160, textAlign: 'center', fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 30 : 30, fontWeight: 600, color: INK, opacity: win(p, 0.46 + i * 0.04, 0.54 + i * 0.04)}}>{m.t}</div>
      ))}
      <div style={{position: 'absolute', left: B.pt ? B.x : TX + unit + 50, top: B.pt ? y1 + barH + 80 : y0 + barH / 2 - 44, width: B.pt ? B.w : B.r - (TX + unit + 50), whiteSpace: 'nowrap', fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 104 : 88, lineHeight: 1, color: ACC, opacity: win(p, 0.5, 0.6)}}>{data.value}</div>
      <Note B={B} text={data.note} italic opacity={win(p, 0.76, 0.86)} top={B.pt ? 1130 : SAFE.b - 200} />
      <Source B={B} source={data.source} opacity={win(p, 0.6, 0.7)} top={B.pt ? 1300 : SAFE.b - 110} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   WwaDisclose — a 10×10 grid: `bar` squares fill (the accent) as the figure is spoken;
   then the rule card (ink) sets beside it: the law that asks for disclosure.
   ═══════════════════════════════════════════════════════════════════════════ */
export type WwaDiscloseData = {
  slideMeta: string; value: string; bar: number; label: string;
  ruleEyebrow: string; ruleTitle: string; ruleLine: string; ruleWhen: string;
  note: string; source: string; durationS?: number;
};

export const WwaDisclose: React.FC<{data: WwaDiscloseData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const cell = B.pt ? 38 : 44;
  const gap = B.pt ? 7 : 8;
  const gridW = 10 * cell + 9 * gap;
  const gx = B.x;
  const gy = B.pt ? B.y + 330 : B.y + 110;
  const fill = win(p, 0.08, 0.3);
  const card = win(p, 0.4, 0.5);
  const valX = B.pt ? B.x + gridW + 40 : B.x + gridW + 50;
  const valW = B.pt ? B.w - gridW - 40 : 520;
  const cardX = B.pt ? B.x : B.x + gridW + 50 + 560;
  const cardW = B.pt ? B.w : B.r - cardX;
  const cardY = B.pt ? B.y + 830 : B.y + 110;
  return (
    <Stage B={B}>
      <Eyebrow B={B} text={data.slideMeta} opacity={win(p, 0, 0.06)} />
      <div style={{position: 'absolute', left: gx, top: gy, width: gridW, display: 'flex', flexWrap: 'wrap', gap}}>
        {Array.from({length: 100}).map((_, k) => {
          const on = k < data.bar && fill * 100 > k;
          return <div key={k} style={{width: cell, height: cell, borderRadius: 4, boxSizing: 'border-box', border: `1px solid ${on ? ACC : RULE}`, backgroundColor: on ? ACC : 'transparent', opacity: on ? 1 : 0.9 * win(p, 0.02, 0.08)}} />;
        })}
      </div>
      <div style={{position: 'absolute', left: valX, top: B.pt ? gy : gy + 10, width: valW, opacity: win(p, 0.22, 0.32)}}>
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 110 : 150, lineHeight: 1, color: ACC}}>{data.value}</div>
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 36 : 46, lineHeight: 1.15, color: INK, marginTop: 18}}>{data.label}</div>
      </div>
      <div style={{position: 'absolute', left: cardX, top: cardY, width: cardW, boxSizing: 'border-box', backgroundColor: CARD, border: `1px solid ${CLAUDE.BORDER}`, borderRadius: 22, padding: B.pt ? '34px 40px' : '40px 44px', opacity: card, transform: `translateY(${(1 - card) * 20}px)`, boxShadow: '0 10px 30px rgba(61,57,41,0.06)'}}>
        <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 24, letterSpacing: '.16em', fontWeight: 600, color: MUTE}}>{data.ruleEyebrow.toUpperCase()}</div>
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 58 : 60, lineHeight: 1.05, color: INK, marginTop: 16}}>{data.ruleTitle}</div>
        <div style={{height: 1, backgroundColor: RULE, margin: '22px 0'}} />
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 40 : 40, lineHeight: 1.18, color: INK, opacity: win(p, 0.48, 0.56)}}>{data.ruleLine}</div>
        <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 28 : 28, fontWeight: 600, color: INK, marginTop: 22, opacity: win(p, 0.54, 0.62)}}>{data.ruleWhen}</div>
      </div>
      <Note B={B} text={data.note} italic opacity={win(p, 0.82, 0.9)} top={B.pt ? 1290 : SAFE.b - 196} />
      <Source B={B} source={data.source} opacity={win(p, 0.6, 0.7)} top={B.pt ? 1380 : SAFE.b - 110} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   WwaLoop — two workflow lanes. Lane A ("some workflows"): Brief → (human, minimal) →
   Output, the human node dims to ≥45% and is bypassed by the accent arrow. Lane B keeps
   the human in the loop.
   ═══════════════════════════════════════════════════════════════════════════ */
export type WwaLane = {label: string; nodes: string[]; bypass: boolean; tag: string};
export type WwaLoopData = {slideMeta: string; title: string; lanes: WwaLane[]; note: string; source: string; durationS?: number};

export const WwaLoop: React.FC<{data: WwaLoopData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const labelW = B.pt ? 0 : 380;
  const nw = B.pt ? 250 : 330;
  const nh = B.pt ? 120 : 130;
  const gapN = B.pt ? (B.w - 3 * nw) / 2 : (B.w - labelW - 3 * nw) / 2;
  const laneTop = (i: number) => (B.pt ? B.y + 300 + i * 420 : B.y + 270 + i * 300);
  const ats = [0.12, 0.5];
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      {data.lanes.map((ln, li) => {
        const at = ats[li] ?? 0.2 + li * 0.3;
        const ly = laneTop(li);
        const ny = B.pt ? ly + 100 : ly;
        const xs = [0, 1, 2].map((k) => B.x + labelW + k * (nw + gapN));
        const by = win(p, at + 0.12, at + 0.22);
        return (
          <React.Fragment key={li}>
            <div style={{position: 'absolute', left: B.x, top: B.pt ? ly - 10 : ly + nh / 2 - 30, width: B.pt ? B.w : labelW - 30, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 44 : 44, lineHeight: 1.1, color: INK, opacity: win(p, at, at + 0.06)}}>{ln.label}</div>
            {ln.nodes.map((nd, k) => {
              const human = k === 1;
              const dim = ln.bypass && human ? 1 - 0.55 * by : 1;
              const g = win(p, at + 0.02 + k * 0.03, at + 0.08 + k * 0.03);
              return (
                <div key={k} style={{position: 'absolute', left: xs[k], top: ny, width: nw, height: nh, boxSizing: 'border-box', backgroundColor: CARD, border: `${human && !ln.bypass ? 3 : 1}px ${ln.bypass && human ? 'dashed' : 'solid'} ${human && !ln.bypass ? INK : RULE}`, borderRadius: 18, display: 'flex', alignItems: 'center', justifyContent: 'center', textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 38 : 44, color: INK, opacity: g * dim}}>{nd}</div>
              );
            })}
            {!ln.bypass && [0, 1].map((k) => (
              <Arrow key={k} id={`wwaL${li}${k}`} x1={xs[k] + nw + 6} y1={ny + nh / 2} x2={xs[k + 1] - 10} y2={ny + nh / 2} g={win(p, at + 0.08 + k * 0.04, at + 0.14 + k * 0.04)} />
            ))}
            {ln.bypass && (
              <svg width={1920} height={1920} style={{position: 'absolute', left: 0, top: 0}}>
                <path d={`M ${xs[0] + nw / 2} ${ny} C ${xs[0] + nw / 2} ${ny - (B.pt ? 60 : 80)}, ${xs[2] + nw / 2} ${ny - (B.pt ? 60 : 80)}, ${xs[2] + nw / 2} ${ny - 8}`}
                  fill="none" stroke={ACC} strokeWidth={6} pathLength={1000} strokeDasharray={`${1000 * by} 1000`} />
              </svg>
            )}
            <div style={{position: 'absolute', left: B.pt ? B.x : xs[0], top: ny + nh + 20, width: B.pt ? B.w : B.r - xs[0], fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 28 : 28, fontWeight: 600, letterSpacing: '.06em', color: ln.bypass ? ACC : MUTE, opacity: win(p, at + 0.2, at + 0.28)}}>{ln.tag}</div>
          </React.Fragment>
        );
      })}
      <Note B={B} text={data.note} italic opacity={win(p, 0.84, 0.92)} top={B.pt ? 1180 : SAFE.b - 190} />
      <Source B={B} source={data.source} opacity={win(p, 0.6, 0.7)} top={B.pt ? 1300 : SAFE.b - 110} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   WwaOwn — the draft (machine-fast) sits on the left / bottom; five human layers stack
   on the spoken words; a terracotta bracket gathers them: what the artifact is for.
   ═══════════════════════════════════════════════════════════════════════════ */
export type WwaOwnData = {slideMeta: string; title: string; draft: string; draftTag: string; layers: string[]; bracket: string; source: string; durationS?: number};

export const WwaOwn: React.FC<{data: WwaOwnData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const n = data.layers.length;
  const lx = B.pt ? B.x + 70 : B.x + 620;
  const lw = B.pt ? B.w - 70 : 860;
  const lh = B.pt ? 88 : 96;
  const lg = B.pt ? 16 : 18;
  const ly0 = B.pt ? B.y + 250 : B.y + 220;
  const stackH = n * lh + (n - 1) * lg;
  const ats = [0.18, 0.26, 0.34, 0.42, 0.5];
  const br = win(p, 0.62, 0.72);
  const dx = B.x;
  const dy = B.pt ? ly0 + stackH + 60 : B.y + 220;
  const dw = B.pt ? B.w : 520;
  const dh = B.pt ? 200 : stackH;
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      {/* the draft */}
      <div style={{position: 'absolute', left: dx, top: dy, width: dw, height: dh, boxSizing: 'border-box', backgroundColor: CARD, border: `1px solid ${CLAUDE.BORDER}`, borderRadius: 20, padding: B.pt ? '26px 34px' : '36px 40px', opacity: win(p, 0.06, 0.14), display: 'flex', flexDirection: 'column', gap: B.pt ? 14 : 22}}>
        <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 24, letterSpacing: '.16em', fontWeight: 600, color: MUTE}}>{data.draftTag.toUpperCase()}</div>
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 46 : 52, lineHeight: 1.08, color: INK}}>{data.draft}</div>
        {!B.pt && Array.from({length: 5}).map((_, i) => (
          <div key={i} style={{height: 14, width: `${i === 4 ? 55 : 92}%`, borderRadius: 7, backgroundColor: INK, opacity: 0.2}} />
        ))}
      </div>
      {/* the five human layers */}
      {data.layers.map((t, i) => {
        const at = ats[i] ?? 0.2 + i * 0.08;
        const g = win(p, at, at + 0.06);
        return (
          <div key={i} style={{position: 'absolute', left: lx, top: ly0 + i * (lh + lg), width: lw, height: lh, boxSizing: 'border-box', border: `2px solid ${INK}`, borderRadius: 14, backgroundColor: CARD, display: 'flex', alignItems: 'center', padding: '0 32px', gap: 24, opacity: g, transform: `translateX(${(1 - g) * 30}px)`}}>
            <div style={{fontFamily: CLAUDE_FONT.mono, fontSize: B.pt ? 28 : 28, color: MUTE, width: 30}}>{i + 1}</div>
            <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 46 : 50, color: INK}}>{t}</div>
          </div>
        );
      })}
      {/* the bracket */}
      <svg width={1920} height={1920} style={{position: 'absolute', left: 0, top: 0, opacity: br}}>
        {B.pt ? (
          <path d={`M ${lx - 24} ${ly0} L ${lx - 44} ${ly0} L ${lx - 44} ${ly0 + stackH} L ${lx - 24} ${ly0 + stackH}`} fill="none" stroke={ACC} strokeWidth={6} />
        ) : (
          <path d={`M ${lx + lw + 20} ${ly0} L ${lx + lw + 44} ${ly0} L ${lx + lw + 44} ${ly0 + stackH} L ${lx + lw + 20} ${ly0 + stackH}`} fill="none" stroke={ACC} strokeWidth={6} />
        )}
      </svg>
      <div style={{position: 'absolute', left: B.pt ? B.x : lx, top: B.pt ? dy + dh + 36 : ly0 + stackH + 30, width: B.pt ? B.w : lw + 44, fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: B.pt ? 46 : 50, color: ACC, opacity: win(p, 0.68, 0.78)}}>{data.bracket}</div>
      <Source B={B} source={data.source} opacity={win(p, 0.56, 0.66)} top={B.pt ? 1320 : SAFE.b - 70} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   WwaFork — "Is AI creative?" splits at the definition (the accent junction) into two
   cards: IF [definition] → THEN [verdict], each landing on its spoken clause.
   ═══════════════════════════════════════════════════════════════════════════ */
export type WwaBranch = {ifText: string; thenText: string};
export type WwaForkData = {slideMeta: string; question: string; junction: string; branches: WwaBranch[]; closer: string; source: string; durationS?: number};

export const WwaFork: React.FC<{data: WwaForkData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const qTop = B.pt ? B.y + 60 : B.y + 56;
  const jx = B.pt ? B.x + 40 : B.x + B.w / 2;
  const jy = B.pt ? B.y + 250 : B.y + 230;
  const cw = B.pt ? B.w - 80 : (B.w - 80) / 2;
  const ch = B.pt ? 340 : 420;
  const cards = data.branches.map((_, i) => (B.pt
    ? {x: B.x + 80, y: B.y + 330 + i * (ch + 40)}
    : {x: B.x + i * (cw + 80), y: B.y + 330}));
  const ats = [0.3, 0.56];
  return (
    <Stage B={B}>
      <Eyebrow B={B} text={data.slideMeta} opacity={win(p, 0, 0.06)} />
      <div style={{position: 'absolute', left: B.x, top: qTop, width: B.w, textAlign: B.pt ? 'left' : 'center', fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 72 : 80, lineHeight: 1.05, color: INK, opacity: win(p, 0.02, 0.1)}}>{data.question}</div>
      <svg width={1920} height={1920} style={{position: 'absolute', left: 0, top: 0}}>
        {cards.map((c, i) => {
          const g = win(p, (ats[i] ?? 0.4) - 0.06, ats[i] ?? 0.4);
          const tx = B.pt ? c.x - 8 : c.x + cw / 2;
          const ty = B.pt ? c.y + 60 : c.y - 6;
          const d = B.pt ? `M ${jx} ${jy} L ${jx} ${ty} L ${tx} ${ty}` : `M ${jx} ${jy} C ${jx} ${jy + 60}, ${tx} ${jy + 30}, ${tx} ${ty}`;
          return <path key={i} d={d} fill="none" stroke={INK} strokeWidth={4} opacity={0.6} pathLength={1000} strokeDasharray={`${1000 * g} 1000`} />;
        })}
        <circle cx={jx} cy={jy} r={16} fill={ACC} opacity={win(p, 0.12, 0.2)} />
      </svg>
      <div style={{position: 'absolute', left: B.pt ? jx + 34 : jx + 30, top: jy - 24, fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 28 : 28, fontWeight: 600, letterSpacing: '.12em', textTransform: 'uppercase', color: ACC, opacity: win(p, 0.14, 0.22)}}>{data.junction}</div>
      {data.branches.map((b, i) => {
        const at = ats[i] ?? 0.4;
        const g = win(p, at, at + 0.06);
        const v = win(p, at + 0.1, at + 0.16);
        return (
          <div key={i} style={{position: 'absolute', left: cards[i].x, top: cards[i].y, width: cw, height: ch, boxSizing: 'border-box', backgroundColor: CARD, border: `1px solid ${CLAUDE.BORDER}`, borderRadius: 22, padding: B.pt ? '30px 36px' : '38px 44px', opacity: g, transform: `translateY(${(1 - g) * 20}px)`, display: 'flex', flexDirection: 'column', justifyContent: 'space-between'}}>
            <div>
              <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 24, letterSpacing: '.16em', fontWeight: 600, color: MUTE}}>IF CREATIVITY MEANS</div>
              <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 44 : 46, lineHeight: 1.12, color: INK, marginTop: 14}}>{b.ifText}</div>
            </div>
            <div style={{opacity: v}}>
              <div style={{height: 1, backgroundColor: RULE, marginBottom: 18}} />
              <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 50 : 54, lineHeight: 1.05, color: INK}}>{b.thenText}</div>
            </div>
          </div>
        );
      })}
      <Note B={B} text={data.closer} italic opacity={win(p, 0.86, 0.94)} top={B.pt ? 1190 : SAFE.b - 150} />
      <Source B={B} source={data.source} opacity={win(p, 0.7, 0.8)} top={B.pt ? 1320 : SAFE.b - 70} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   WwaLimits — what the findings show vs what they don't; REQUIRES provenance and a
   falsifier string, so the falsifiability beat cannot be authored without them.
   ═══════════════════════════════════════════════════════════════════════════ */
export type WwaList = {heading: string; items: string[]};
export type WwaLimitsData = {slideMeta: string; title: string; found: WwaList; notFound: WwaList; provenance: string; falsifier: string; durationS?: number};

export const WwaLimits: React.FC<{data: WwaLimitsData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const colW = B.pt ? B.w : 820;
  const itemStep = B.pt ? 58 : 92;
  const cols = [
    {list: data.found, x: B.x, y: B.y + 220, at: 0.1, mark: 'yes' as const},
    {list: data.notFound, x: B.pt ? B.x : B.x + 900, y: B.pt ? B.y + 220 + 76 + data.found.items.length * itemStep + 30 : B.y + 220, at: 0.36, mark: 'no' as const},
  ];
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      {cols.map((c, ci) => (
        <React.Fragment key={ci}>
          <div style={{position: 'absolute', left: c.x, top: c.y, width: colW, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 42 : 46, color: INK, opacity: win(p, c.at - 0.04, c.at + 0.02), borderBottom: `1px solid ${RULE}`, paddingBottom: 10}}>{c.list.heading}</div>
          {c.list.items.map((it, i) => {
            const at = c.at + i * 0.05;
            return (
              <div key={i} style={{position: 'absolute', left: c.x, top: c.y + (B.pt ? 76 : 100) + i * itemStep, width: colW, display: 'flex', alignItems: 'center', gap: 20, opacity: win(p, at, at + 0.05)}}>
                {c.mark === 'yes'
                  ? <div style={{width: 20, height: 20, borderRadius: 10, backgroundColor: INK, flexShrink: 0}} />
                  : <div style={{width: 20, height: 20, borderRadius: 10, border: `2px solid ${INK}`, boxSizing: 'border-box', flexShrink: 0}} />}
                <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 30 : 38, lineHeight: 1.2, color: INK}}>{it}</div>
              </div>
            );
          })}
        </React.Fragment>
      ))}
      <div style={{position: 'absolute', left: B.x, top: B.pt ? 1150 : SAFE.b - 250, width: B.pt ? B.w : B.w - 220, fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: B.pt ? 40 : 44, lineHeight: 1.2, color: ACC, opacity: win(p, 0.76, 0.84)}}>{data.falsifier}</div>
      <div style={{position: 'absolute', left: B.x, top: B.pt ? 1300 : SAFE.b - 110, width: B.w - (B.pt ? 0 : 220), fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 24 : 24, lineHeight: 1.35, color: MUTE, opacity: win(p, 0.82, 0.9)}}>Sources: {data.provenance}</div>
    </Stage>
  );
};
