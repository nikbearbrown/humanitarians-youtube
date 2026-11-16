/**
 * Grokking.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-grokking ("Grokking: When AI Suddenly Understands", @HumanitariansAI).
 *
 * Same contract as RLHF.tsx (stage helpers from JevExplainer.tsx): each component lays out natively
 * for 16:9 (<Name>) and 9:16 (<Name>916) — never a crop — and every motion is a pure function of
 * progress, conformed via `durationSeconds`. Every number on screen comes from ./grokkingData.ts,
 * which is GENERATED from the reel's evidence/grok_toy.json (seeded numpy run).
 *
 *   GkHook     — practice vs. new problems scoreboards, driven by the real run's step counter
 *   GkTable    — Power et al. 2022 setup: (a + b) mod 97, the 97×97 table, the shown 40 %
 *   GkMemorize — train 100 % by step N, held-out ~0 %: a lookup table
 *   GkJump     — both curves on a log-scale step axis; the long gap, then the jump
 *   GkDecay    — weight size with vs. without weight decay; memorizing costs more than the rule
 *   GkClock    — Nanda et al. 2023: adding as turning; our embeddings' energy sits in a few waves
 *   GkAlike    — same run, two snapshots: identical practice scores, opposite new-problem scores
 *   GkWord     — Heinlein, Stranger in a Strange Land (1961): grok
 */
import React from 'react';
import { AbsoluteFill, Img, staticFile } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ACC_TEXT, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';
import type { Stage } from './JevExplainer';
import { GK } from './grokkingData';

const W = (P: boolean) => (P ? 1080 : 1920);
const H = (P: boolean) => (P ? 1920 : 1080);
const lerp = (a: number, b: number, p: number) => a + (b - a) * p;
const fmtInt = (n: number) => Math.round(n).toLocaleString('en-US');
const pct = (v: number, dp = 0) => `${(v * 100).toFixed(dp)}%`;

type Curve = ReadonlyArray<ReadonlyArray<number>>; // [step, train, test, norm]
const CW = GK.curveWd as unknown as Curve;
const CN = GK.curveNoWd as unknown as Curve;

// value of column `col` at `step`, linear in log(step) between logged samples
const at = (c: Curve, step: number, col: number) => {
  if (step <= c[0][0]) return c[0][col];
  for (let i = 1; i < c.length; i++) {
    if (c[i][0] >= step) {
      const a = Math.log(c[i - 1][0]), b = Math.log(c[i][0]);
      const f = b === a ? 1 : (Math.log(step) - a) / (b - a);
      return lerp(c[i - 1][col], c[i][col], f);
    }
  }
  return c[c.length - 1][col];
};

// filled pill (GATE T reads outlined pills as overlapping text — always filled)
const Pill: React.FC<{ text: string; size: number; a?: number; accent?: boolean; fill?: string; style?: React.CSSProperties }> = ({ text, size, a = 1, accent, fill, style }) => (
  <span style={{
    display: 'inline-block', padding: `${size * 0.16}px ${size * 0.42}px`, borderRadius: size, boxSizing: 'border-box',
    background: fill ?? (accent ? ACC_TEXT : CLAUDE.INK),
    fontFamily: SANS, fontSize: size, lineHeight: 1.1, color: CLAUDE.CARD, opacity: a, whiteSpace: 'nowrap', ...style,
  }}>{text}</span>
);

const Label: React.FC<{ text: string; size: number; style?: React.CSSProperties; color?: string; serif?: boolean }> = ({ text, size, style, color, serif }) => (
  <div style={{ position: 'absolute', fontFamily: serif ? SERIF : SANS, fontSize: size, lineHeight: 1.15, color: color ?? CLAUDE.INK, ...style }}>{text}</div>
);

// ---------------------------------------------------------------------------
// log-x chart frame shared by GkJump and GkDecay
// ---------------------------------------------------------------------------
type Box = { x: number; y: number; w: number; h: number };
const logX = (b: Box, step: number, xMax: number) => b.x + (Math.log10(Math.max(1, step)) / Math.log10(xMax)) * b.w;
const polyline = (c: Curve, col: number, b: Box, xMax: number, Y: (v: number) => number, limStep: number) => {
  const pts: string[] = [];
  for (let i = 0; i < c.length; i++) {
    if (c[i][0] <= limStep) pts.push(`${logX(b, c[i][0], xMax)},${Y(c[i][col])}`);
    else {
      if (i > 0 && c[i - 1][0] < limStep) pts.push(`${logX(b, limStep, xMax)},${Y(at(c, limStep, col))}`);
      break;
    }
  }
  return pts.join(' ');
};
// Drawn arrow, sized in em: the mono "→" glyph is a short, wide ink blob that GATE T reads as sub-floor text.
const Arrow: React.FC = () => (
  <svg viewBox="0 0 20 16" style={{ width: '1em', height: '0.8em', verticalAlign: '-0.05em', margin: '0 0.3em', overflow: 'visible' }}>
    <path d="M1 8H18M11 1.5L18 8L11 14.5" fill="none" stroke="currentColor" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

const LogAxes: React.FC<{ b: Box; xMax: number; a: number; P: boolean; xTitle: string; yTicks: { v: number; label: string }[]; Y: (v: number) => number }> = ({ b, xMax, a, P, xTitle, yTicks, Y }) => {
  const ticks = [1, 10, 100, 1000, 10000].filter((s) => s <= xMax);
  const fs = P ? 36 : 34;
  return (
    <>
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0, opacity: a }}>
        <line x1={b.x} y1={b.y + b.h} x2={b.x + b.w} y2={b.y + b.h} stroke={CLAUDE.INK} strokeWidth={4} />
        <line x1={b.x} y1={b.y} x2={b.x} y2={b.y + b.h} stroke={CLAUDE.INK} strokeWidth={4} />
        {ticks.map((s) => <line key={s} x1={logX(b, s, xMax)} y1={b.y + b.h + 8} x2={logX(b, s, xMax)} y2={b.y + b.h + 22} stroke={CLAUDE.INK} strokeWidth={4} />)}
        {yTicks.map((tk) => <line key={tk.label} x1={b.x - 22} y1={Y(tk.v)} x2={b.x - 8} y2={Y(tk.v)} stroke={CLAUDE.INK} strokeWidth={4} />)}
      </svg>
      {ticks.map((s) => (
        <Label key={s} text={fmtInt(s)} size={fs} style={{ left: logX(b, s, xMax) - 100, width: 200, textAlign: 'center', top: b.y + b.h + 30, opacity: a }} />
      ))}
      {yTicks.map((tk) => (
        <Label key={tk.label} text={tk.label} size={fs} style={{ left: b.x - 188, width: 156, textAlign: 'right', top: Y(tk.v) - fs * 0.6, opacity: a }} />
      ))}
      <Label text={xTitle} size={fs} color={CLAUDE.INK_SOFT} style={{ left: b.x, width: b.w, textAlign: 'center', top: b.y + b.h + 22 + fs * 1.4, opacity: a }} />
    </>
  );
};

// ===========================================================================
// GkHook — practice vs. new problems, driven by the run's own step counter
// ===========================================================================
export const gkHookSchema = z.object({
  title: z.string().default('Practice vs. new problems'),
  practiceLabel: z.string().default('practice problems'),
  newLabel: z.string().default('new problems'),
  stepLabel: z.string().default('training step'),
  note: z.string().default('a real run: small numpy network, (a + b) mod 97'),
  sparkLine: z.string().default('Stuck, then sudden.'),
  durationSeconds: z.number().optional(),
});
export const gkHookMeta = durMeta(5.5);
export const GkHook: React.FC<z.infer<typeof gkHookSchema>> = ({ title, practiceLabel, newLabel, stepLabel, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const maxStep = Math.ceil((GK.test99 as number) * 1.6 / 500) * 500;
  const u = ramp(t, 0.08, 0.8);
  const step = Math.max(1, Math.round(maxStep * u * u)); // eased clock: the first hundreds fly by, then the long wait
  const tr = at(CW, step, 1), te = at(CW, step, 2);
  const cIn = ease(ramp(t, 0.02, 0.08));
  const colW = P ? S.w : (S.w - 60) / 2;
  const cardH = P ? 330 : 430;
  const top = P ? 320 : 240;
  const pos = [{ x: S.x, y: top }, { x: P ? S.x : S.x + colW + 60, y: P ? top + cardH + 40 : top }];
  const big = P ? 200 : 220;
  const cards = [
    { label: practiceLabel, v: tr, accent: false },
    { label: newLabel, v: te, accent: te > 0.5 },
  ];
  const sy = P ? top + 2 * cardH + 80 : top + cardH + 40;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {cards.map((c, i) => (
        <Card key={c.label} style={{ left: pos[i].x, top: pos[i].y, width: colW, height: cardH, opacity: cIn, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: P ? 6 : 10 }}>
          <Pill text={c.label} size={P ? 46 : 46} accent={i === 1} />
          <span style={{ fontFamily: SERIF, fontSize: big, lineHeight: 1, color: c.accent ? ACC_TEXT : CLAUDE.INK }}>{pct(c.v)}</span>
        </Card>
      ))}
      <div style={{ position: 'absolute', left: S.x, top: sy, width: S.w, display: 'flex', alignItems: 'baseline', gap: 24, opacity: cIn }}>
        <span style={{ fontFamily: SANS, fontSize: P ? 46 : 44, color: CLAUDE.INK }}>{stepLabel}</span>
        <span style={{ fontFamily: SERIF, fontSize: P ? 96 : 88, lineHeight: 1, color: CLAUDE.INK }}>{fmtInt(step)}</span>
      </div>
      <div style={{ position: 'absolute', left: S.x, top: sy + (P ? 120 : 110), width: S.w, height: 14, borderRadius: 7, background: CLAUDE.BORDER, opacity: cIn }} />
      <div style={{ position: 'absolute', left: S.x, top: sy + (P ? 120 : 110), width: S.w * (step / maxStep), height: 14, borderRadius: 7, background: CLAUDE.INK, opacity: cIn }} />
      {P && <Label text={note} size={36} color={CLAUDE.INK_SOFT} style={{ left: S.x, top: sy + 160, width: S.w, opacity: cIn }} />}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GkTable — (a + b) mod 97; the 97×97 answer table, 40 % shown
// ===========================================================================
export const gkTableSchema = z.object({
  title: z.string().default('Clock arithmetic'),
  source: z.string().default('Power et al., OpenAI, 2022 · a tiny transformer'),
  equation: z.string().default('(a + b) mod 97'),
  shownLabel: z.string().default('shown in training'),
  heldLabel: z.string().default('held out'),
  note: z.string().default('our numpy re-run of the setup'),
  sparkLine: z.string().default('Part of the table.'),
  durationSeconds: z.number().optional(),
});
export const gkTableMeta = durMeta(8);
export const GkTable: React.FC<z.infer<typeof gkTableSchema>> = ({ title, source, equation, shownLabel, heldLabel, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const Pn = GK.P as number;
  const hIn = ease(ramp(t, 0.02, 0.1));
  const eIn = ease(ramp(t, 0.1, 0.2));
  const xIn = ease(ramp(t, 0.22, 0.32));
  const gIn = ease(ramp(t, 0.36, 0.42));
  const rows = Math.floor(ramp(t, 0.42, 0.72) * Pn);
  const lIn = ease(ramp(t, 0.6, 0.7));
  const [ea, eb, ey] = GK.shownExamples[0] as unknown as number[];
  // grid geometry
  const G = P ? 580 : 690;
  const gx = P ? S.x + (S.w - G) / 2 : S.r - G, gy = P ? 700 : 250;
  const c = G / Pn;
  let path = '';
  const gap = c * 0.25, sq = (c - gap).toFixed(2);
  for (let a = 0; a < rows; a++) {
    for (let b = 0; b < Pn; b++) {
      if (GK.mask[a * Pn + b] === '1') path += `M${(gx + b * c + gap / 2).toFixed(2)} ${(gy + a * c + gap / 2).toFixed(2)}h${sq}v${sq}h-${sq}z`;
    }
  }
  const lx = S.x, logo = P ? 84 : 92;
  const pctShown = Math.round((GK.trainFrac as number) * 100);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: lx, top: P ? 290 : 200, display: 'flex', alignItems: 'center', gap: 22, opacity: hIn, width: P ? S.w : 1010 }}>
        <Img src={staticFile('logos/openai/openai-01.svg')} style={{ width: logo, height: logo }} />
        <span style={{ fontFamily: SANS, fontSize: P ? 40 : 42, color: CLAUDE.INK, lineHeight: 1.2 }}>{source}</span>
      </div>
      <Label text={equation} size={P ? 100 : 112} serif style={{ left: lx, top: P ? 410 : 330, opacity: eIn, whiteSpace: 'nowrap' }} />
      <div style={{ position: 'absolute', left: lx, top: P ? 540 : 490, display: 'flex', alignItems: 'baseline', gap: 22, opacity: xIn }}>
        <span style={{ fontFamily: MONO, fontSize: P ? 54 : 62, color: CLAUDE.INK }}>{ea} + {eb} = {ea + eb}<Arrow /></span>
        <span style={{ fontFamily: SERIF, fontSize: P ? 80 : 92, lineHeight: 1, color: ACC_TEXT }}>{ey}</span>
      </div>
      {/* legend */}
      <div style={{ position: 'absolute', left: lx, top: P ? 620 : 620, display: 'flex', flexDirection: P ? 'row' : 'column', gap: P ? 16 : 22, opacity: lIn }}>
        <Pill text={`${shownLabel}: ${pctShown}%`} size={P ? 34 : 44} />
        <Pill text={`${heldLabel}: ${100 - pctShown}%`} size={P ? 34 : 44} fill={CLAUDE.INK_SOFT} />
      </div>
      {!P && (
        <>
          <Label text={`${fmtInt(GK.train as number)} of ${fmtInt(GK.cells as number)} answers shown`} size={40} style={{ left: lx, top: 790, width: 900, opacity: lIn }} />
          <Label text={note} size={34} color={CLAUDE.INK_SOFT} style={{ left: lx, top: 850, width: 900, opacity: lIn }} />
        </>
      )}
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0 }}>
        <rect x={gx - 3} y={gy - 3} width={G + 6} height={G + 6} fill="none" stroke={CLAUDE.INK} strokeWidth={4} opacity={gIn} />
        <path d={path} fill={CLAUDE.INK} />
        <rect x={gx + eb * c - c * 2} y={gy + ea * c - c * 2} width={c * 5} height={c * 5} fill={ACC_TEXT} opacity={rows > ea ? xIn : 0} />
      </svg>
      {!P && <Label text="a ↓   b →" size={36} color={CLAUDE.INK_SOFT} style={{ left: gx, top: gy - 52, opacity: gIn }} />}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GkMemorize — train 100 % by step N, held-out ~0 %: a lookup table
// ===========================================================================
export const gkMemorizeSchema = z.object({
  title: z.string().default('First, it memorizes'),
  trainLabel: z.string().default('training accuracy'),
  testLabel: z.string().default('test accuracy'),
  shownLabel: z.string().default('shown in training'),
  heldLabel: z.string().default('held out'),
  sparkLine: z.string().default('A lookup table.'),
  durationSeconds: z.number().optional(),
});
export const gkMemorizeMeta = durMeta(4.6);
export const GkMemorize: React.FC<z.infer<typeof gkMemorizeSchema>> = ({ title, trainLabel, testLabel, shownLabel, heldLabel, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const N = GK.train100 as number;
  const run = ease(ramp(t, 0.08, 0.42));
  const step = Math.max(1, Math.round(N * run));
  const tr = at(CW, step, 1), te = at(CW, step, 2);
  const sIn = ease(ramp(t, 0.03, 0.09));
  const tick = (i: number) => ease(ramp(t, 0.16 + i * 0.07, 0.22 + i * 0.07));
  const cross = (i: number) => ease(ramp(t, 0.48 + i * 0.06, 0.54 + i * 0.06));
  const statW = P ? (S.w - 40) / 2 : 700;
  const big = P ? 150 : 190;
  const stat = (label: string, v: number, sub: string, i: number) => (
    <div key={label} style={{ position: 'absolute', left: P ? S.x + i * (statW + 40) : S.x, top: P ? 300 : 230 + i * 360, width: statW, opacity: sIn }}>
      <div style={{ fontFamily: SANS, fontSize: P ? 42 : 46, color: CLAUDE.INK }}>{label}</div>
      <div style={{ fontFamily: SERIF, fontSize: big, lineHeight: 1.05, color: i ? ACC_TEXT : CLAUDE.INK }}>{pct(v, i ? 1 : 0)}</div>
      <div style={{ fontFamily: SANS, fontSize: P ? 38 : 40, color: CLAUDE.INK_SOFT }}>{sub}</div>
    </div>
  );
  const cx = P ? S.x : S.x + 820, cw = P ? S.w : S.r - (S.x + 820);
  const ch = P ? 300 : 360;
  const cy = [P ? 650 : 240, P ? 1000 : 640];
  const fs = P ? 50 : 54;
  const rowsOf = (ex: ReadonlyArray<ReadonlyArray<number>>, held: boolean) => ex.map(([a, b, y], i) => (
    <div key={`${a}-${b}`} style={{ display: 'flex', alignItems: 'center', gap: 22, fontFamily: MONO, fontSize: fs, color: CLAUDE.INK, lineHeight: 1.2 }}>
      <span>{a} + {b}<Arrow />{held ? '?' : y}</span>
      <span style={{ fontFamily: SANS, color: held ? ACC_TEXT : CLAUDE.INK, opacity: held ? cross(i) : tick(i) }}>{held ? '✗' : '✓'}</span>
    </div>
  ));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {stat(trainLabel, tr, `step ${fmtInt(step)}`, 0)}
      {stat(testLabel, te, `${fmtInt(GK.test as number)} held-out answers`, 1)}
      {[0, 1].map((k) => (
        <Card key={k} style={{ left: cx, top: cy[k], width: cw, height: ch, opacity: k ? ease(ramp(t, 0.42, 0.48)) : sIn, padding: P ? '70px 40px 0' : '80px 44px 0',
          display: 'flex', flexDirection: 'column', gap: P ? 14 : 20 }}>
          {rowsOf((k ? GK.heldExamples : GK.shownExamples) as unknown as number[][], k === 1)}
        </Card>
      ))}
      <div style={{ position: 'absolute', left: cx + 30, top: cy[0] - 30, opacity: sIn }}><Pill text={shownLabel} size={P ? 40 : 42} /></div>
      <div style={{ position: 'absolute', left: cx + 30, top: cy[1] - 30, opacity: ease(ramp(t, 0.42, 0.48)) }}><Pill text={heldLabel} size={P ? 40 : 42} accent /></div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GkJump — both curves on a log-scale step axis
// ===========================================================================
export const gkJumpSchema = z.object({
  title: z.string().default('Then, the jump'),
  trainLabel: z.string().default('train'),
  testLabel: z.string().default('test'),
  xTitle: z.string().default('training steps (log scale)'),
  sparkLine: z.string().default('Understood, suddenly.'),
  durationSeconds: z.number().optional(),
});
export const gkJumpMeta = durMeta(4);
export const GkJump: React.FC<z.infer<typeof gkJumpSchema>> = ({ title, trainLabel, testLabel, xTitle, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const xMax = GK.steps as number;
  const b: Box = P ? { x: S.x + 150, y: 360, w: S.w - 170, h: 680 } : { x: S.x + 170, y: 220, w: S.w - 200, h: 560 };
  const Y = (v: number) => b.y + b.h - v * b.h;
  const ax = ease(ramp(t, 0.02, 0.08));
  const draw = ramp(t, 0.06, 0.62);
  const lim = Math.pow(10, draw * Math.log10(xMax));
  const s1 = GK.train100 as number, s2 = GK.test99 as number;
  const a1 = ease(ramp(t, 0.24, 0.3)), a2 = ease(ramp(t, 0.6, 0.66)), br = ease(ramp(t, 0.66, 0.74));
  const x1 = logX(b, s1, xMax), x2 = logX(b, s2, xMax);
  const by = Y(0.5);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <LogAxes b={b} xMax={xMax} a={ax} P={P} xTitle={xTitle} Y={Y} yTicks={[{ v: 0, label: '0%' }, { v: 0.5, label: '50%' }, { v: 1, label: '100%' }]} />
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0 }}>
        <line x1={x1} y1={b.y} x2={x1} y2={b.y + b.h - 10} stroke={CLAUDE.INK} strokeWidth={3} strokeDasharray="10 10" opacity={a1} />
        <line x1={x2} y1={b.y} x2={x2} y2={b.y + b.h - 10} stroke={ACC_TEXT} strokeWidth={3} strokeDasharray="10 10" opacity={a2} />
        <polyline points={polyline(CW, 1, b, xMax, Y, lim)} fill="none" stroke={CLAUDE.INK} strokeWidth={8} strokeLinejoin="round" />
        <polyline points={polyline(CW, 2, b, xMax, Y, lim)} fill="none" stroke={ACC_TEXT} strokeWidth={8} strokeLinejoin="round" />
        {/* the gap bracket */}
        <g opacity={br}>
          <line x1={x1 + 8} y1={by} x2={x2 - 8} y2={by} stroke={CLAUDE.INK} strokeWidth={5} />
          <line x1={x1 + 8} y1={by - 18} x2={x1 + 8} y2={by + 18} stroke={CLAUDE.INK} strokeWidth={5} />
          <line x1={x2 - 8} y1={by - 18} x2={x2 - 8} y2={by + 18} stroke={CLAUDE.INK} strokeWidth={5} />
        </g>
      </svg>
      <div style={{ position: 'absolute', left: (x1 + x2) / 2 - 260, width: 520, top: by - (P ? 86 : 84), textAlign: 'center', opacity: br }}>
        <Pill text={`≈ ${Math.round(GK.gapRatio as number)}× more steps`} size={P ? 40 : 44} />
      </div>
      {P ? (
        <div style={{ position: 'absolute', left: S.x, top: b.y + b.h + 150, width: S.w, display: 'flex', flexDirection: 'column', gap: 12 }}>
          <span style={{ fontFamily: SANS, fontSize: 40, color: CLAUDE.INK, opacity: a1 }}>{trainLabel} 100% · step {fmtInt(s1)}</span>
          <span style={{ fontFamily: SANS, fontSize: 40, color: ACC_TEXT, opacity: a2 }}>{testLabel} 99% · step {fmtInt(s2)}</span>
        </div>
      ) : (
        <>
          <Label text={`${trainLabel} 100% · step ${fmtInt(s1)}`} size={38} style={{ left: x1 + 16, top: Y(1) + 14, opacity: a1, whiteSpace: 'nowrap' }} />
          {/* right of its marker: left of it the test curve is still climbing through the label */}
          <Label text={`${testLabel} 99%`} size={38} color={ACC_TEXT} style={{ left: x2 + 16, top: by + 30, opacity: a2, whiteSpace: 'nowrap' }} />
          <Label text={`step ${fmtInt(s2)}`} size={38} color={ACC_TEXT} style={{ left: x2 + 16, top: by + 76, opacity: a2, whiteSpace: 'nowrap' }} />
        </>
      )}
      <Label text={testLabel} size={P ? 40 : 42} color={ACC_TEXT} style={{ left: b.x + 20, top: Y(0) - (P ? 60 : 62), opacity: ease(ramp(t, 0.12, 0.18)) }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GkDecay — weight size with vs. without weight decay; the table costs more than the rule
// ===========================================================================
export const gkDecaySchema = z.object({
  title: z.string().default('Why it switches'),
  yTitle: z.string().default('size of the weights'),
  wdLabel: z.string().default('with weight decay'),
  noLabel: z.string().default('without'),
  tableLabel: z.string().default('lookup table'),
  ruleLabel: z.string().default('the rule'),
  xTitle: z.string().default('training steps (log scale)'),
  sparkLine: z.string().default('Cheaper to understand.'),
  durationSeconds: z.number().optional(),
});
export const gkDecayMeta = durMeta(6.2);
export const GkDecay: React.FC<z.infer<typeof gkDecaySchema>> = ({ title, yTitle, wdLabel, noLabel, tableLabel, ruleLabel, xTitle, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const xMax = GK.steps as number;
  const yMax = Math.ceil(Math.max(...CW.map((c) => c[3]), ...CN.map((c) => c[3])) / 20) * 20;
  const b: Box = P ? { x: S.x + 150, y: 380, w: S.w - 170, h: 340 } : { x: S.x + 170, y: 260, w: 860, h: 520 };
  const Y = (v: number) => b.y + b.h - (v / yMax) * b.h;
  const ax = ease(ramp(t, 0.02, 0.08));
  const lim = Math.pow(10, ramp(t, 0.06, 0.5) * Math.log10(xMax));
  const barIn = ease(ramp(t, 0.5, 0.62));
  const outIn = ease(ramp(t, 0.66, 0.74));
  const rx = P ? S.x : S.x + 1160, rw = P ? S.w : S.r - (S.x + 1160);
  const ry = P ? 880 : 250;
  const barMax = rw - 20;
  const peak = GK.normPeakWd as number, end = GK.normEndWd as number;
  const bars = [
    { label: `${tableLabel} · step ${fmtInt(GK.normPeakStep as number)}`, v: peak, accent: false },
    { label: `${ruleLabel} · step ${fmtInt(xMax)}`, v: end, accent: true },
  ];
  const bh = P ? 50 : 64, rowH = P ? 112 : 150;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Label text={yTitle} size={P ? 38 : 38} color={CLAUDE.INK_SOFT} style={{ left: b.x, top: b.y - (P ? 70 : 62), opacity: ax }} />
      <LogAxes b={b} xMax={xMax} a={ax} P={P} xTitle={xTitle} Y={Y} yTicks={[{ v: 0, label: '0' }, { v: yMax / 2, label: fmtInt(yMax / 2) }, { v: yMax, label: fmtInt(yMax) }]} />
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0 }}>
        <polyline points={polyline(CN, 3, b, xMax, Y, lim)} fill="none" stroke={CLAUDE.INK} strokeWidth={7} strokeLinejoin="round" />
        <polyline points={polyline(CW, 3, b, xMax, Y, lim)} fill="none" stroke={ACC_TEXT} strokeWidth={8} strokeLinejoin="round" />
      </svg>
      <Label text={noLabel} size={P ? 38 : 38} style={{ left: b.x + b.w - (P ? 240 : 260), width: P ? 240 : 260, textAlign: 'right', top: Y(at(CN, xMax, 3)) - (P ? 56 : 58), opacity: ramp(t, 0.45, 0.5) }} />
      <Label text={wdLabel} size={P ? 38 : 38} color={ACC_TEXT} style={{ left: b.x + b.w - (P ? 420 : 420), width: P ? 420 : 420, textAlign: 'right', top: Y(at(CW, xMax, 3)) + 16, opacity: ramp(t, 0.45, 0.5) }} />
      {/* the cost comparison: the same run, memorized vs. with the rule */}
      <div style={{ position: 'absolute', left: rx, top: ry, width: rw, opacity: barIn }}>
        {bars.map((br, i) => (
          <div key={br.label} style={{ position: 'absolute', top: i * rowH, left: 0, width: rw }}>
            <div style={{ fontFamily: SANS, fontSize: P ? 38 : 40, color: br.accent ? ACC_TEXT : CLAUDE.INK, whiteSpace: 'nowrap' }}>{br.label}</div>
            <div style={{ marginTop: 8, display: 'flex', alignItems: 'center', gap: 18 }}>
              <div style={{ width: (barMax - 140) * (br.v / peak) * barIn, height: bh, borderRadius: 10, background: br.accent ? ACC_TEXT : CLAUDE.INK }} />
              <span style={{ fontFamily: SERIF, fontSize: P ? 54 : 58, lineHeight: 1, color: br.accent ? ACC_TEXT : CLAUDE.INK }}>{Math.round(br.v)}</span>
            </div>
          </div>
        ))}
      </div>
      <div style={{ position: 'absolute', left: rx, top: ry + 2 * rowH + (P ? 10 : 30), width: rw, display: 'flex', flexDirection: 'column', gap: P ? 14 : 20, opacity: outIn }}>
        <Pill text={`${wdLabel}: test ${pct(GK.finalTestWd as number)}`} size={P ? 38 : 40} accent />
        <Pill text={`${noLabel}: test ${pct(GK.finalTestNoWd as number)}`} size={P ? 38 : 40} />
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GkClock — adding as turning; the learned embeddings sit in a few waves
// ===========================================================================
export const gkClockSchema = z.object({
  title: z.string().default('Arithmetic with waves'),
  source: z.string().default('Nanda et al., 2023: inside a trained transformer'),
  specLabel: z.string().default('our run: number embeddings, energy by wave frequency'),
  sparkLine: z.string().default('Arithmetic with waves.'),
  durationSeconds: z.number().optional(),
});
export const gkClockMeta = durMeta(6.3);
export const GkClock: React.FC<z.infer<typeof gkClockSchema>> = ({ title, source, specLabel, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const Pn = GK.P as number;
  const [ea, eb, ey] = GK.shownExamples[0] as unknown as number[];
  const sIn = ease(ramp(t, 0.02, 0.08));
  const hA = ease(ramp(t, 0.08, 0.2));
  const hB = ease(ramp(t, 0.24, 0.44));
  const res = ease(ramp(t, 0.44, 0.5));
  const spec = ease(ramp(t, 0.52, 0.7));
  const capIn = ease(ramp(t, 0.66, 0.74));
  const R = P ? 220 : 250;
  const cx = P ? S.x + S.w / 2 : S.x + 40 + R, cy = P ? 400 + R : 290 + R;
  const ang = (k: number) => (k / Pn) * 2 * Math.PI - Math.PI / 2; // 0 at the top, clockwise
  const pt = (k: number, r: number) => [cx + r * Math.cos(ang(k)), cy + r * Math.sin(ang(k))];
  const aNow = ea * hA, bNow = ea + eb * hB;
  const [axp, ayp] = pt(aNow, R * 0.78);
  const [bxp, byp] = pt(bNow, R * 0.9);
  // arc for "+ b"
  const arc = () => {
    if (hB <= 0) return '';
    const r = R * 0.62; const [x0, y0] = pt(ea, r); const [x1, y1] = pt(bNow, r);
    const large = eb * hB / Pn > 0.5 ? 1 : 0;
    return `M ${x0} ${y0} A ${r} ${r} 0 ${large} 1 ${x1} ${y1}`;
  };
  let ticks = '';
  for (let k = 0; k < Pn; k++) {
    const [x0, y0] = pt(k, R - (k % 10 === 0 ? 30 : 16)); const [x1, y1] = pt(k, R);
    ticks += `M${x0.toFixed(1)} ${y0.toFixed(1)}L${x1.toFixed(1)} ${y1.toFixed(1)}`;
  }
  // spectrum
  const E = GK.fourierWd as unknown as number[];
  const top5 = new Set((GK.topKWd as unknown as number[]));
  const eMax = Math.max(...E);
  const sx = P ? S.x : S.x + 2 * R + 130, sw = P ? S.w : S.r - sx;
  const sy = P ? 1010 : 330, sh = P ? 230 : 420;
  const bw = sw / E.length;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Label text={source} size={P ? 38 : 40} style={{ left: S.x, top: P ? 290 : 200, width: S.w, opacity: sIn }} />
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0 }}>
        <g opacity={sIn}>
          <circle cx={cx} cy={cy} r={R} fill={CLAUDE.CARD} stroke={CLAUDE.INK} strokeWidth={5} />
          <path d={ticks} stroke={CLAUDE.INK} strokeWidth={3} />
        </g>
        <path d={arc()} fill="none" stroke={ACC_TEXT} strokeWidth={7} />
        <line x1={cx} y1={cy} x2={axp} y2={ayp} stroke={CLAUDE.INK} strokeWidth={10} strokeLinecap="round" opacity={hA > 0 ? 1 : 0} />
        <line x1={cx} y1={cy} x2={bxp} y2={byp} stroke={ACC_TEXT} strokeWidth={8} strokeLinecap="round" opacity={hB > 0 ? 1 : 0} />
        <circle cx={cx} cy={cy} r={14} fill={CLAUDE.INK} opacity={sIn} />
        {/* spectrum bars */}
        {E.map((e, i) => {
          const h = (e / eMax) * (sh - 10) * spec;
          return <rect key={i} x={sx + i * bw + bw * 0.18} y={sy + sh - h} width={bw * 0.64} height={h} fill={top5.has(i + 1) ? ACC_TEXT : CLAUDE.INK} />;
        })}
        <line x1={sx} y1={sy + sh} x2={sx + sw} y2={sy + sh} stroke={CLAUDE.INK} strokeWidth={4} opacity={spec > 0 ? 1 : 0} />
      </svg>
      {/* clock labels */}
      <Label text="0" size={P ? 40 : 44} style={{ left: cx - 40, width: 80, textAlign: 'center', top: cy - R + 34, opacity: sIn }} />
      <div style={{ position: 'absolute', left: P ? S.x : cx - R, width: P ? S.w : 2 * R, top: cy + R + (P ? 18 : 22), textAlign: 'center', opacity: res }}>
        <span style={{ fontFamily: MONO, fontSize: P ? 50 : 52, color: CLAUDE.INK }}>{ea} + {eb}<Arrow /></span>
        <span style={{ fontFamily: SERIF, fontSize: P ? 70 : 72, color: ACC_TEXT }}>{ey}</span>
      </div>
      <Label text={specLabel} size={P ? 34 : 38} style={{ left: sx, top: sy - (P ? 54 : 60), width: sw, opacity: spec > 0 ? 1 : 0 }} />
      <Label text={`top 5 of ${E.length} frequencies: ${pct(GK.top5Wd as number)} of the energy`} size={P ? 38 : 42} color={ACC_TEXT}
        style={{ left: sx, top: sy + sh + (P ? 16 : 20), width: sw, opacity: capIn }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GkAlike — same run, two snapshots: identical practice score, opposite new-problem score
// ===========================================================================
export const gkAlikeSchema = z.object({
  title: z.string().default('Same practice score'),
  leftLabel: z.string().default('memorized'),
  rightLabel: z.string().default('understood'),
  practiceLabel: z.string().default('practice'),
  newLabel: z.string().default('new problems'),
  sparkLine: z.string().default("Alike, until they aren't."),
  durationSeconds: z.number().optional(),
});
export const gkAlikeMeta = durMeta(4.2);
export const GkAlike: React.FC<z.infer<typeof gkAlikeSchema>> = ({ title, leftLabel, rightLabel, practiceLabel, newLabel, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const s0 = GK.train100 as number, s1 = GK.steps as number;
  const snaps = [
    { label: `${leftLabel} · step ${fmtInt(s0)}`, tr: at(CW, s0, 1), te: GK.testAtTrain100 as number, accent: false },
    { label: `${rightLabel} · step ${fmtInt(s1)}`, tr: at(CW, s1, 1), te: GK.finalTestWd as number, accent: true },
  ];
  const cIn = (i: number) => ease(ramp(t, 0.03 + i * 0.06, 0.09 + i * 0.06));
  const pIn = ease(ramp(t, 0.16, 0.24));
  const nIn = ease(ramp(t, 0.42, 0.52));
  const colW = P ? S.w : (S.w - 60) / 2;
  const ch = P ? 470 : 660;
  const top = P ? 310 : 240;
  const big = P ? 130 : 160;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {snaps.map((s, i) => {
        const x = P ? S.x : S.x + i * (colW + 60), y = P ? top + i * (ch + 40) : top;
        return (
          <React.Fragment key={s.label}>
            <Card style={{ left: x, top: y, width: colW, height: ch, opacity: cIn(i), padding: P ? '64px 40px 0' : '90px 50px 0', boxSizing: 'border-box',
              display: 'flex', flexDirection: P ? 'row' : 'column', gap: P ? 40 : 30 }}>
              {[{ l: practiceLabel, v: s.tr, a: pIn, acc: false }, { l: newLabel, v: s.te, a: nIn, acc: s.accent }].map((r) => (
                <div key={r.l} style={{ opacity: r.a, flex: P ? 1 : undefined }}>
                  <div style={{ fontFamily: SANS, fontSize: P ? 40 : 44, color: CLAUDE.INK }}>{r.l}</div>
                  <div style={{ fontFamily: SERIF, fontSize: big, lineHeight: 1.05, color: r.acc ? ACC_TEXT : CLAUDE.INK }}>{pct(r.v, r.v < 0.995 && r.v > 0.005 ? 1 : 0)}</div>
                </div>
              ))}
            </Card>
            <div style={{ position: 'absolute', left: x + 30, top: y - 30, opacity: cIn(i) }}><Pill text={s.label} size={P ? 42 : 44} accent={s.accent} /></div>
          </React.Fragment>
        );
      })}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GkWord — Heinlein's word
// ===========================================================================
export const gkWordSchema = z.object({
  title: z.string().default('The word grok'),
  book: z.string().default('Stranger in a Strange Land'),
  author: z.string().default('Robert A. Heinlein'),
  year: z.string().default('1961'),
  word: z.string().default('grok'),
  pos: z.string().default('verb, coined in the novel'),
  meaning: z.string().default('to understand something so fully that it becomes part of you'),
  note: z.string().default('meaning paraphrased'),
  sparkLine: z.string().default('Part of you.'),
  durationSeconds: z.number().optional(),
});
export const gkWordMeta = durMeta(6.8);
export const GkWord: React.FC<z.infer<typeof gkWordSchema>> = ({ title, book, author, year, word, pos, meaning, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const bIn = ease(ramp(t, 0.03, 0.12));
  const wIn = ease(ramp(t, 0.24, 0.32));
  const words = meaning.split(' ');
  const typed = ramp(t, 0.38, 0.7) * words.length;
  const nIn = ease(ramp(t, 0.7, 0.78));
  const bx = P ? S.x + (S.w - 560) / 2 : S.x, by = P ? 280 : 220, bw = P ? 560 : 520, bh = P ? 400 : 720;
  const rx = P ? S.x : S.x + bw + 100, rw = P ? S.w : S.r - rx;
  const ry = P ? by + bh + 40 : 200;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: bx, top: by, width: bw, height: bh, borderRadius: 14, background: CLAUDE.INK, opacity: bIn,
        transform: `translateY(${(1 - bIn) * 20}px)`, boxSizing: 'border-box', padding: P ? '50px 44px' : '80px 50px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
        <div style={{ fontFamily: SERIF, fontSize: P ? 70 : 80, lineHeight: 1.1, color: CLAUDE.CARD }}>{book}</div>
        <div>
          <div style={{ fontFamily: SANS, fontSize: P ? 40 : 44, color: CLAUDE.CARD }}>{author}</div>
          <div style={{ fontFamily: SERIF, fontSize: P ? 64 : 76, color: CLAUDE.CARD, marginTop: 8 }}>{year}</div>
        </div>
      </div>
      <div style={{ position: 'absolute', left: rx, top: ry, width: rw, opacity: wIn }}>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 30, flexWrap: 'wrap' }}>
          <span style={{ fontFamily: SERIF, fontSize: P ? 170 : 290, lineHeight: 1, color: ACC_TEXT }}>{word}</span>
          <span style={{ fontFamily: SANS, fontSize: P ? 40 : 46, color: CLAUDE.INK }}>{pos}</span>
        </div>
        <div style={{ fontFamily: SERIF, fontSize: P ? 92 : 72, lineHeight: 1.15, color: CLAUDE.INK, marginTop: P ? 24 : 50 }}>
          {words.map((w, i) => <span key={i} style={{ opacity: i < Math.floor(typed) ? 1 : i < typed ? typed - i : 0 }}>{w} </span>)}
        </div>
        <div style={{ fontFamily: SANS, fontSize: P ? 34 : 36, color: CLAUDE.INK_SOFT, marginTop: P ? 14 : 30, opacity: nIn }}>{note}</div>
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
