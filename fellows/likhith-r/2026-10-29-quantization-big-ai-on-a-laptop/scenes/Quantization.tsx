/**
 * Quantization.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-quantization ("Quantization: Big AI on a Laptop", @HumanitariansAI).
 *
 * Same contract as RagOkf.tsx / ApiGateway.tsx (stage helpers from JevExplainer.tsx):
 * each component lays out natively for 16:9 (<Name>) and 9:16 (<Name>916) — never a
 * crop — and every motion is a pure function of progress, conformed via
 * `durationSeconds`. Every number on screen is a default copied from the reel's
 * evidence/quant_toy.out.txt (seeded numpy run); nothing is hand-made.
 *
 *   QzHook    — 70B weights × 2 bytes = 140 GB vs. a 16 GB laptop (8.75×)
 *   QzWeights — a patch of real toy weights; one zooms into its 16 bits; 7B × 2 B = 14 GB
 *   QzGrid    — eight weights on a number line snap onto the 4-bit grid (q = −8…7)
 *   QzLevels  — 256 vs. 16 levels; ŵ = s·q; one scale per row vs. a scale per 32 weights
 *   QzPayoff  — 14 → 7 → 3.5 GB; tokens/s bound at an illustrative 100 GB/s
 *   QzCancel  — errors centred on zero; 49× cancellation; one outlier crushes its group
 *   QzLimit   — weight error vs. bits (8 → 2): the curve breaks below 4
 *   QzLocal   — llama.cpp + Ollama: 4-bit by default; the verdict lines
 */
import React from 'react';
import { AbsoluteFill, Img, staticFile } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ACC_TEXT, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';

const W = (P: boolean) => (P ? 1080 : 1920);
const H = (P: boolean) => (P ? 1920 : 1080);
const lerp = (a: number, b: number, p: number) => a + (b - a) * p;

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

// a horizontal bar that grows to `f` of its track
const Bar: React.FC<{ x: number; y: number; w: number; h: number; f: number; accent?: boolean }> = ({ x, y, w, h, f, accent }) => (
  <>
    <div style={{ position: 'absolute', left: x, top: y, width: w, height: h, borderRadius: 12, background: CLAUDE.PILL, border: `3px solid ${CLAUDE.BORDER}`, boxSizing: 'border-box' }} />
    <div style={{ position: 'absolute', left: x, top: y, width: Math.max(f > 0 ? 12 : 0, w * f), height: h, borderRadius: 12, background: accent ? ACC_TEXT : CLAUDE.INK }} />
  </>
);

const fmtInt = (n: number) => Math.round(n).toLocaleString('en-US');

// ===========================================================================
// QzHook — 70B weights × 2 bytes = 140 GB, against a 16 GB laptop
// ===========================================================================
export const qzHookSchema = z.object({
  title: z.string().default('Weights alone: 140 GB'),
  params: z.number().default(70e9),
  bytes: z.number().default(2),
  modelGB: z.number().default(140),
  laptopGB: z.number().default(16),
  ratio: z.string().default('8.75×'),
  modelLabel: z.string().default('70B model at 16 bits'),
  laptopLabel: z.string().default('a 16 GB laptop: all of its memory'),
  sparkLine: z.string().default('So how?'),
  durationSeconds: z.number().optional(),
});
export const qzHookMeta = durMeta(6);
export const QzHook: React.FC<z.infer<typeof qzHookSchema>> = ({ title, params, bytes, modelGB, laptopGB, ratio, modelLabel, laptopLabel, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const count = ease(ramp(t, 0.04, 0.24));
  const b1 = ease(ramp(t, 0.2, 0.42));
  const b2 = ease(ramp(t, 0.44, 0.56));
  const r = ease(ramp(t, 0.58, 0.66));
  const top = P ? 330 : 210;
  const barH = P ? 130 : 120;
  const y1 = P ? 760 : 480, y2 = P ? 1060 : 740;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, width: S.w, display: 'flex', flexDirection: P ? 'column' : 'row', alignItems: P ? 'flex-start' : 'baseline', gap: P ? 6 : 28, opacity: ease(ramp(t, 0.02, 0.08)) }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 112 : 112, lineHeight: 1, color: CLAUDE.INK }}>{fmtInt(params * count)}</span>
        <span style={{ fontFamily: SANS, fontSize: P ? 56 : 52, color: CLAUDE.INK }}>weights × {bytes} bytes</span>
      </div>
      <Label text={modelLabel} size={P ? 56 : 48} style={{ left: S.x, top: y1 - (P ? 78 : 66), opacity: b1 > 0 ? 1 : 0 }} />
      <Bar x={S.x} y={y1} w={S.w} h={barH} f={b1} accent />
      <div style={{ position: 'absolute', right: W(P) - S.r + 28, top: y1 + barH * 0.14, opacity: ease(ramp(t, 0.38, 0.44)) }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 80 : 70, color: CLAUDE.CARD, lineHeight: 1 }}>{Math.round(modelGB * b1)} GB</span>
      </div>
      <Label text={laptopLabel} size={P ? 56 : 48} style={{ left: S.x, top: y2 - (P ? 78 : 66), opacity: b2 > 0 ? 1 : 0, width: S.w }} />
      <Bar x={S.x} y={y2} w={S.w} h={barH} f={(laptopGB / modelGB) * b2} />
      <div style={{ position: 'absolute', left: S.x + S.w * (laptopGB / modelGB) + 30, top: y2 + barH * 0.16, opacity: b2 }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 76 : 66, color: CLAUDE.INK, lineHeight: 1 }}>{laptopGB} GB</span>
      </div>
      <div style={{ position: 'absolute', opacity: r, transform: `scale(${lerp(0.9, 1, r)})`, transformOrigin: 'left center',
        ...(P ? { left: S.x, top: y2 + barH + 60 } : { right: W(P) - S.r + 24, top: y2 + (barH - 72) / 2 }) }}>
        <Pill text={`${ratio} too big`} size={P ? 64 : 56} accent />
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// QzWeights — a patch of real weights; one weight's 16 bits; 7B × 2 B = 14 GB
// ===========================================================================
export const qzWeightsSchema = z.object({
  title: z.string().default('A weight is a number'),
  weights: z.array(z.number()).default([-0.0112, 0.0172, -0.0043, -0.0027, -0.001, -0.0112, -0.0039, 0.0112, 0.0056, 0.0371, -0.0116, 0.026,
    -0.0097, 0.0126, -0.008, 0.0057, 0.0162, 0.017, -0.0069, 0.0029, 0.0288, -0.0239, -0.0092, 0.007]),
  k: z.number().default(1),
  bits: z.string().default('0010010001100111'),
  patchNote: z.string().default('toy layer, row 0'),
  params: z.number().default(7e9),
  gb: z.number().default(14),
  sparkLine: z.string().default('Two bytes each.'),
  durationSeconds: z.number().optional(),
});
export const qzWeightsMeta = durMeta(5);
export const QzWeights: React.FC<z.infer<typeof qzWeightsSchema>> = ({ title, weights, k, bits, patchNote, params, gb, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const cols = P ? 4 : 6;
  const n = P ? 16 : 24;
  const cw = P ? 232 : 186, ch = P ? 84 : 76, g = P ? 14 : 14;
  const gx = S.x, gy = P ? 330 : 220;
  const zoom = ease(ramp(t, 0.22, 0.34));
  const bitsIn = (i: number) => ease(ramp(t, 0.3 + i * 0.012, 0.36 + i * 0.012));
  const total = ease(ramp(t, 0.58, 0.74));
  const hx = gx + (k % cols) * (cw + g), hy = gy + Math.floor(k / cols) * (ch + g);
  // bits row: landscape right of the patch, portrait below it
  const bw = P ? 56 : 80, bg = P ? 4 : 10;
  const bx = P ? S.x + (S.w - (16 * bw + 15 * bg)) / 2 : S.x;
  const by = P ? gy + 4 * (ch + g) + 170 : gy + 4 * (ch + g) + 150;
  const groups = [{ a: 0, b: 1, name: 'sign' }, { a: 1, b: 6, name: 'exponent' }, { a: 6, b: 16, name: 'mantissa' }];
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {weights.slice(0, n).map((v, i) => {
        const a = ease(ramp(t, 0.02 + i * 0.006, 0.08 + i * 0.006));
        const hit = i === k;
        return (
          <Card key={i} style={{ ...(hit && zoom > 0.5 ? { border: `4px solid ${ACC_TEXT}` } : {}), left: gx + (i % cols) * (cw + g), top: gy + Math.floor(i / cols) * (ch + g), width: cw, height: ch,
            opacity: a * (hit ? 1 : lerp(1, 0.55, zoom)), display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontFamily: MONO, fontSize: P ? 44 : 38, color: CLAUDE.INK }}>{(v >= 0 ? '+' : '') + v.toFixed(4)}</Card>
        );
      })}
      <Label text={patchNote} size={P ? 44 : 36} color={CLAUDE.INK_SOFT}
        style={{ left: gx, top: gy + (n / cols) * (ch + g) + 6, opacity: ease(ramp(t, 0.1, 0.16)) }} />
      {bits.split('').map((c, i) => {
        const grp = i === 0 ? 0 : i < 6 ? 1 : 2;
        return (
          <div key={i} style={{ position: 'absolute', left: bx + i * (bw + bg), top: by, width: bw, height: bw * 1.25, borderRadius: 8,
            background: grp === 0 ? ACC_TEXT : grp === 1 ? CLAUDE.INK : CLAUDE.INK_SOFT, opacity: bitsIn(i),
            display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: MONO, fontSize: P ? 44 : 40, color: CLAUDE.CARD }}>{c}</div>
        );
      })}
      {groups.map((gr, j) => (
        <div key={gr.name} style={{ position: 'absolute', left: bx + gr.a * (bw + bg), top: by + bw * 1.25 + 16, width: (gr.b - gr.a) * (bw + bg) - bg,
          display: 'flex', justifyContent: 'center', opacity: ease(ramp(t, 0.42 + j * 0.03, 0.48 + j * 0.03)) }}>
          {gr.name === 'sign'
            ? <span style={{ fontFamily: SANS, fontSize: P ? 40 : 34, color: CLAUDE.INK }}>±</span>
            : <span style={{ fontFamily: SANS, fontSize: P ? 40 : 34, color: CLAUDE.INK }}>{gr.name}</span>}
        </div>
      ))}
      <div style={{ position: 'absolute', left: bx, top: by - (P ? 78 : 84), opacity: zoom }}>
        <Pill text={`${weights[k] >= 0 ? '+' : ''}${weights[k].toFixed(4)} in 16 bits = 2 bytes`} size={P ? 46 : 44} accent />
      </div>
      <div style={{ position: 'absolute', opacity: total, display: 'flex', flexDirection: 'column', gap: 10,
        ...(P ? { left: S.x, top: by + bw * 1.25 + 110, width: S.w } : { left: gx + cols * (cw + g) + 50, top: gy + 10, width: S.r - (gx + cols * (cw + g) + 50) }) }}>
        <span style={{ fontFamily: SANS, fontSize: P ? 50 : 46, color: CLAUDE.INK }}>{fmtInt(params)}</span>
        <span style={{ fontFamily: SANS, fontSize: P ? 50 : 46, color: CLAUDE.INK }}>weights × 2 bytes</span>
        <span style={{ fontFamily: SERIF, fontSize: P ? 128 : 120, lineHeight: 1, color: ACC_TEXT }}>= {Math.round(gb * total)} GB</span>
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// QzGrid — eight real weights snap onto the 4-bit grid of allowed values
// ===========================================================================
export const qzGridSchema = z.object({
  title: z.string().default('Round onto a grid'),
  w: z.array(z.number()).default([-0.0068, 0.0177, 0.0091, -0.0001, -0.0133, -0.0121, -0.0471, -0.0138]),
  s: z.number().default(0.00673),
  q: z.array(z.number()).default([-1, 3, 1, 0, -2, -2, -7, -2]),
  from: z.string().default('16 bits: any value'),
  to: z.string().default('4 bits: 16 allowed values'),
  sparkLine: z.string().default('Round to the grid.'),
  durationSeconds: z.number().optional(),
});
export const qzGridMeta = durMeta(5);
export const QzGrid: React.FC<z.infer<typeof qzGridSchema>> = ({ title, w, s, q, from, to, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const lo = -8 * s - s * 0.6, hi = 7 * s + s * 0.6;
  const lx = S.x + 20, lw = S.w - 40;
  const X = (v: number) => lx + ((v - lo) / (hi - lo)) * lw;
  const lineY = P ? 960 : 720;
  const grid = ease(ramp(t, 0.3, 0.42));
  const snap = (i: number) => ease(ramp(t, 0.46 + i * 0.025, 0.56 + i * 0.025));
  const lab = ease(ramp(t, 0.68, 0.76));
  // stagger dots vertically above the line so near-equal values stay readable
  const rowY = (i: number) => lineY - (P ? 150 : 120) - (i % 4) * (P ? 80 : 70);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top: P ? 300 : 190, display: 'flex', flexDirection: P ? 'column' : 'row', gap: P ? 18 : 24, alignItems: 'flex-start' }}>
        <Pill text={from} size={P ? 50 : 44} fill={CLAUDE.INK_SOFT} a={ease(ramp(t, 0.03, 0.1))} />
        <Pill text={to} size={P ? 50 : 44} accent a={grid} />
      </div>
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0 }}>
        <line x1={lx} y1={lineY} x2={lx + lw} y2={lineY} stroke={CLAUDE.INK} strokeWidth={5} />
        {/* the 4-bit grid: s × q for q = −8 … 7 */}
        {Array.from({ length: 16 }, (_, j) => {
          const v = (j - 8) * s;
          return <line key={j} x1={X(v)} y1={lineY - 30} x2={X(v)} y2={lineY + 30} stroke={j === 8 ? CLAUDE.INK : CLAUDE.INK_SOFT}
            strokeWidth={j === 8 ? 6 : 4} opacity={grid} />;
        })}
        {w.map((v, i) => {
          const p = snap(i);
          const x = lerp(X(v), X(q[i] * s), p), y = lerp(rowY(i), lineY, p);
          const a = ease(ramp(t, 0.04 + i * 0.02, 0.1 + i * 0.02));
          return (
            <g key={i} opacity={a}>
              <line x1={X(v)} y1={rowY(i)} x2={x} y2={y} stroke={CLAUDE.SPARK} strokeWidth={4} opacity={p > 0 && p < 1 ? 0.8 : 0} />
              <circle cx={x} cy={y} r={P ? 18 : 16} fill={p >= 1 ? CLAUDE.SPARK : CLAUDE.INK} />
            </g>
          );
        })}
      </svg>
      {/* integer level labels under the ticks that received a weight */}
      {Array.from(new Set(q)).map((qq) => (
        <div key={qq} style={{ position: 'absolute', left: X(qq * s) - 50, width: 100, top: lineY + 46, textAlign: 'center',
          fontFamily: MONO, fontSize: P ? 38 : 40, color: CLAUDE.INK, opacity: lab }}>{qq > 0 ? `+${qq}` : qq}</div>
      ))}
      <div style={{ position: 'absolute', left: S.x, top: P ? 1170 : 300, display: 'flex', flexWrap: 'wrap', gap: P ? 12 : 16, alignItems: 'center', width: S.w, opacity: ease(ramp(t, 0.74, 0.82)) }}>
        <span style={{ fontFamily: SANS, fontSize: P ? 46 : 42, color: CLAUDE.INK, marginRight: 8 }}>stored:</span>
        {q.map((qq, i) => <Pill key={i} text={qq > 0 ? `+${qq}` : `${qq}`} size={P ? 46 : 44} style={{ fontFamily: MONO }} />)}
        <span style={{ fontFamily: SANS, fontSize: P ? 46 : 42, color: CLAUDE.INK, marginLeft: 8 }}>+ one scale <i style={{ fontFamily: SERIF }}>s</i> = {s}</span>
      </div>
      <Label text="level q (a whole number from −8 to 7)" size={P ? 44 : 38} color={CLAUDE.INK_SOFT}
        style={{ left: S.x, top: lineY + (P ? 130 : 110), width: S.w, opacity: lab }} />
      <Label text={`each dot: a real weight from the toy layer (${w[6].toFixed(4)} … ${w[1] > 0 ? '+' : ''}${w[1].toFixed(4)})`} size={P ? 40 : 34} color={CLAUDE.INK_SOFT}
        style={{ left: S.x, top: lineY + (P ? 130 : 110), width: S.w, opacity: ease(ramp(t, 0.1, 0.18)) * (lab > 0 ? 0 : 1) }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// QzLevels — 256 vs 16 levels; ŵ = s·q; one scale per row vs a scale per group
// ===========================================================================
export const qzLevelsSchema = z.object({
  title: z.string().default('Levels, and a scale'),
  errRow: z.number().default(43.3),
  errGroup: z.number().default(13.1),
  rowLabel: z.string().default('one scale per row'),
  groupLabel: z.string().default('a scale per 32 weights'),
  errNote: z.string().default('4-bit weight error, toy layer'),
  sparkLine: z.string().default('A scale per group.'),
  durationSeconds: z.number().optional(),
});
export const qzLevelsMeta = durMeta(5.5);
export const QzLevels: React.FC<z.infer<typeof qzLevelsSchema>> = ({ title, errRow, errGroup, rowLabel, groupLabel, errNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const r8 = ease(ramp(t, 0.03, 0.16));
  const r4 = ease(ramp(t, 0.16, 0.28));
  const eq = ease(ramp(t, 0.36, 0.46));
  const e1 = ease(ramp(t, 0.56, 0.66)), e2 = ease(ramp(t, 0.66, 0.76));
  const rx = S.x, rw = S.w;
  const ruler = (y: number, n: number, p: number, label: string, accent: boolean) => (
    <React.Fragment key={label}>
      <div style={{ position: 'absolute', left: rx, top: y - (P ? 74 : 62), opacity: p > 0 ? 1 : 0 }}>
        <Pill text={label} size={P ? 48 : 42} accent={accent} />
      </div>
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0 }}>
        <line x1={rx} y1={y + 30} x2={rx + rw * p} y2={y + 30} stroke={CLAUDE.INK} strokeWidth={4} />
        {Array.from({ length: n }, (_, j) => {
          const x = rx + (j / (n - 1)) * rw;
          return x <= rx + rw * p + 0.5 ? <line key={j} x1={x} y1={y + (n > 20 ? 6 : 0)} x2={x} y2={y + 54} stroke={accent ? CLAUDE.SPARK : CLAUDE.INK} strokeWidth={n > 20 ? 2 : 6} /> : null;
        })}
      </svg>
    </React.Fragment>
  );
  const y8 = P ? 400 : 290, y4 = P ? 590 : 440;
  const eqY = P ? 760 : 560;
  const barY = P ? 1040 : 760;
  const barW = P ? S.w : S.w / 2 - 40;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {ruler(y8, 256, r8, '8 bits · 256 levels', false)}
      {ruler(y4, 16, r4, '4 bits · 16 levels', true)}
      {/* structured math: hat, italic variables, upright operators */}
      <div style={{ position: 'absolute', left: S.x, top: eqY, width: S.w, display: 'flex', flexDirection: P ? 'column' : 'row', alignItems: P ? 'flex-start' : 'baseline', gap: P ? 8 : 56, opacity: eq }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 110 : 100, color: CLAUDE.INK, lineHeight: 1.1 }}>
          <i>ŵ</i> = <i>s</i> · <i>q</i>
        </span>
        <span style={{ fontFamily: SANS, fontSize: P ? 46 : 42, color: CLAUDE.INK }}><i style={{ fontFamily: SERIF }}>q</i>: the level &nbsp;·&nbsp; <i style={{ fontFamily: SERIF }}>s</i>: the scale back to real values</span>
      </div>
      {[{ l: rowLabel, v: errRow, p: e1, acc: false }, { l: groupLabel, v: errGroup, p: e2, acc: true }].map((b, i) => {
        const x = P ? S.x : S.x + i * (barW + 80);
        const y = P ? barY + i * 140 : barY;
        return (
          <React.Fragment key={b.l}>
            <Label text={b.l} size={P ? 46 : 42} style={{ left: x, top: y - (P ? 64 : 58), opacity: b.p > 0 ? 1 : 0 }} />
            <Bar x={x} y={y} w={P ? barW - 200 : barW - 190} h={P ? 70 : 66} f={(b.v / 50) * b.p} accent={b.acc} />
            <span style={{ position: 'absolute', left: x + (P ? barW - 180 : barW - 170), top: y + 2, fontFamily: SERIF, fontSize: P ? 62 : 58, lineHeight: 1, color: b.acc ? ACC_TEXT : CLAUDE.INK, opacity: b.p }}>{(b.v * b.p).toFixed(1)} %</span>
          </React.Fragment>
        );
      })}
      <Label text={errNote} size={P ? 40 : 34} color={CLAUDE.INK_SOFT}
        style={{ left: S.x, top: P ? barY + 222 : barY + 84, opacity: e1 }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// QzPayoff — 14 → 7 → 3.5 GB, and the tokens/s bound at a fixed bandwidth
// ===========================================================================
export const qzPayoffSchema = z.object({
  title: z.string().default('A 7B model, weights only'),
  rows: z.array(z.object({ bits: z.string(), gb: z.number(), tps: z.number() })).default([
    { bits: '16-bit', gb: 14, tps: 7.1 },
    { bits: '8-bit', gb: 7, tps: 14.3 },
    { bits: '4-bit', gb: 3.5, tps: 28.6 },
  ]),
  memHead: z.string().default('memory'),
  speedHead: z.string().default('tokens/s, at most'),
  speedNote: z.string().default('each token reads every weight once; illustrative 100 GB/s memory'),
  sparkLine: z.string().default('Smaller is faster.'),
  durationSeconds: z.number().optional(),
});
export const qzPayoffMeta = durMeta(5.5);
export const QzPayoff: React.FC<z.infer<typeof qzPayoffSchema>> = ({ title, rows, memHead, speedHead, speedNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const maxGB = rows[0].gb, maxT = rows[rows.length - 1].tps;
  const colW = P ? S.w : S.w / 2 - 50;
  const memX = S.x, spX = P ? S.x : S.x + colW + 100;
  const memY = P ? 330 : 240, spY = P ? 780 : 240;
  const rh = P ? 66 : 96, rg = P ? 50 : 90;
  const lw = P ? 170 : 150; // bits label column
  const memIn = (i: number) => ease(ramp(t, 0.04 + i * 0.12, 0.14 + i * 0.12));
  const spIn = (i: number) => ease(ramp(t, 0.48 + i * 0.07, 0.56 + i * 0.07));
  const col = (x: number, y: number, head: string, val: (r: typeof rows[0]) => number, max: number, fmt: (v: number) => string, inF: (i: number) => number, headA: number) => (
    <>
      <div style={{ position: 'absolute', left: x, top: y, opacity: headA }}><Pill text={head} size={P ? 46 : 42} fill={CLAUDE.INK_SOFT} /></div>
      {rows.map((r, i) => {
        const y0 = y + (P ? 90 : 100) + i * (rh + rg);
        const p = inF(i);
        const bw = colW - lw - (P ? 220 : 200);
        return (
          <React.Fragment key={r.bits}>
            <div style={{ position: 'absolute', left: x, top: y0 + rh * 0.12, opacity: p > 0 ? 1 : 0 }}>
              <Pill text={r.bits} size={P ? 42 : 40} accent={i === rows.length - 1} />
            </div>
            <Bar x={x + lw} y={y0} w={bw} h={rh} f={(val(r) / max) * p} accent={i === rows.length - 1} />
            <span style={{ position: 'absolute', left: x + lw + bw + 24, top: y0 + 4, fontFamily: SERIF, fontSize: P ? 60 : 58, lineHeight: 1, color: CLAUDE.INK, opacity: p }}>{fmt(val(r) * p)}</span>
          </React.Fragment>
        );
      })}
    </>
  );
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {col(memX, memY, memHead, (r) => r.gb, maxGB, (v) => `${v.toFixed(v < 10 ? 1 : 0)} GB`, memIn, ease(ramp(t, 0.02, 0.08)))}
      {col(spX, spY, speedHead, (r) => r.tps, maxT, (v) => v.toFixed(1), spIn, ease(ramp(t, 0.44, 0.5)))}
      <Label text={speedNote} size={P ? 42 : 40} color={CLAUDE.INK_SOFT}
        style={{ left: spX, top: spY + (P ? 90 : 100) + 3 * (rh + rg) - (P ? 20 : 30), width: colW, opacity: ease(ramp(t, 0.6, 0.68)) }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// QzCancel — rounding errors centre on zero and cancel; one outlier crushes its group
// ===========================================================================
export const qzCancelSchema = z.object({
  title: z.string().default('Why it still works'),
  hist: z.array(z.number()).default([197, 413, 376, 409, 403, 520, 398, 404, 386, 397, 193]),
  histLabel: z.string().default('4,096 rounding errors: half up, half down'),
  worst: z.number().default(6.6247),
  net: z.number().default(0.134),
  ratio: z.string().default('49×'),
  worstLabel: z.string().default('if every error pushed one way'),
  netLabel: z.string().default('actual error of the output'),
  nzPlain: z.number().default(4),
  nzProt: z.number().default(21),
  maskPlain: z.string().default('00000100001000010100100000000000'),
  maskProt: z.string().default('10111111001010011101111101001111'),
  outlierIdx: z.number().default(5),
  methods: z.array(z.object({ name: z.string(), does: z.string() })).default([
    { name: 'GPTQ', does: 'fixes error as it goes' },
    { name: 'AWQ', does: 'guards the key weights' },
  ]),
  sparkLine: z.string().default('Errors cancel.'),
  durationSeconds: z.number().optional(),
});
export const qzCancelMeta = durMeta(5.5);
export const QzCancel: React.FC<z.infer<typeof qzCancelSchema>> = ({ title, hist, histLabel, worst, net, ratio, worstLabel, netLabel, nzPlain, nzProt, maskPlain, maskProt, outlierIdx, methods, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const hIn = ease(ramp(t, 0.03, 0.2));
  const nIn = ease(ramp(t, 0.24, 0.4));
  const oIn = ease(ramp(t, 0.46, 0.56));
  const prot = ease(ramp(t, 0.6, 0.68));
  const mIn = ease(ramp(t, 0.7, 0.78));
  // histogram block
  const hx = S.x, hy = P ? 300 : 220, hw = P ? S.w : 620, hh = P ? 260 : 440;
  const max = Math.max(...hist);
  const bwid = hw / hist.length;
  // cancellation bars
  const cx = P ? S.x : S.x + 700, cy = P ? 720 : 250, cw = P ? S.w : S.w - 700;
  // outlier row
  const ox = P ? S.x : S.x + 700, oy = P ? 1040 : 660, ow = P ? S.w : S.w - 700;
  const cell = ow / 32 - 4;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0 }}>
        {hist.map((v, i) => {
          const h = (v / max) * hh * hIn;
          return <rect key={i} x={hx + i * bwid + 4} y={hy + hh - h} width={bwid - 8} height={h} rx={6} fill={i === 5 ? CLAUDE.SPARK : CLAUDE.INK_SOFT} />;
        })}
        <line x1={hx + hw / 2} y1={hy - 10} x2={hx + hw / 2} y2={hy + hh + 10} stroke={CLAUDE.INK} strokeWidth={4} opacity={hIn} />
      </svg>
      <Label text="−½ step" size={P ? 40 : 34} style={{ left: hx, top: hy + hh + 14, opacity: hIn }} />
      <Label text="0" size={P ? 40 : 34} style={{ left: hx + hw / 2 - 10, top: hy + hh + 14, opacity: hIn }} />
      <Label text="+½ step" size={P ? 40 : 34} style={{ right: W(P) - (hx + hw), top: hy + hh + 14, opacity: hIn, textAlign: 'right' }} />
      {!P && <Label text={histLabel} size={36} color={CLAUDE.INK_SOFT} style={{ left: hx, top: hy + hh + 70, width: hw, opacity: hIn }} />}
      {/* the same sum, two ways */}
      {[{ l: worstLabel, v: worst, acc: false }, { l: netLabel, v: net, acc: true }].map((b, i) => {
        const y = cy + i * (P ? 130 : 130);
        return (
          <React.Fragment key={b.l}>
            <Label text={b.l} size={P ? 44 : 38} style={{ left: cx, top: y - (P ? 58 : 52), opacity: nIn }} />
            <Bar x={cx} y={y} w={cw - 200} h={P ? 54 : 52} f={(b.v / worst) * nIn} accent={b.acc} />
            <span style={{ position: 'absolute', left: cx + cw - 180, top: y, fontFamily: MONO, fontSize: P ? 46 : 42, color: CLAUDE.INK, opacity: nIn }}>{b.v.toFixed(i ? 3 : 2)}</span>
          </React.Fragment>
        );
      })}
      <div style={{ position: 'absolute', opacity: ease(ramp(t, 0.36, 0.42)), ...(P ? { left: cx, top: cy + 190 } : { left: cx, top: cy + 210 }) }}>
        <Pill text={`${ratio} smaller: they cancel`} size={P ? 48 : 42} accent />
      </div>
      {/* one outlier in a group of 32 */}
      <Label text={prot < 0.5 ? `one outlier in 32: ${nzPlain} of 31 others survive` : `outlier set aside: ${nzProt} of 31 survive`} size={P ? 44 : 38}
        style={{ left: ox, top: oy - (P ? 64 : 56), opacity: oIn, width: ow }} />
      {Array.from({ length: 32 }, (_, i) => {
        const isO = i === outlierIdx;
        // dark = keeps a non-zero level (evidence masks); the outlier itself is terracotta
        const alive2 = (prot < 0.5 ? maskPlain : maskProt)[i] === '1';
        return (
          <div key={i} style={{ position: 'absolute', left: ox + i * (cell + 4), top: oy + (isO ? -18 : 0), width: cell, height: isO ? (P ? 86 : 100) : (P ? 50 : 64), borderRadius: 5,
            background: isO ? CLAUDE.SPARK : alive2 ? CLAUDE.INK : CLAUDE.PILL, border: `2px solid ${CLAUDE.BORDER}`, boxSizing: 'border-box',
            opacity: oIn * (isO && prot > 0.5 ? 0.5 : 1) }} />
        );
      })}
      <div style={{ position: 'absolute', left: ox, top: oy + (P ? 110 : 120), display: 'flex', flexDirection: 'column', gap: 16, opacity: mIn }}>
        {methods.map((m) => (
          <div key={m.name} style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
            <Pill text={m.name} size={P ? 48 : 42} />
            <span style={{ fontFamily: SANS, fontSize: P ? 46 : 38, color: CLAUDE.INK }}>{m.does}</span>
          </div>
        ))}
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// QzLimit — weight error vs bits: the curve breaks below 4
// ===========================================================================
export const qzLimitSchema = z.object({
  title: z.string().default('Below 4 bits, it breaks'),
  pts: z.array(z.object({ bits: z.number(), err: z.number() })).default([
    { bits: 8, err: 0.7 }, { bits: 6, err: 3.0 }, { bits: 5, err: 6.2 }, { bits: 4, err: 13.1 }, { bits: 3, err: 29.4 }, { bits: 2, err: 65.7 },
  ]),
  yLabel: z.string().default('weight error, %'),
  note: z.string().default('toy layer; a proxy for quality, not a benchmark'),
  first: z.array(z.string()).default(['small models', 'maths', 'code']),
  firstHead: z.string().default('feel it first:'),
  sparkLine: z.string().default('Four bits is the floor.'),
  durationSeconds: z.number().optional(),
});
export const qzLimitMeta = durMeta(5);
export const QzLimit: React.FC<z.infer<typeof qzLimitSchema>> = ({ title, pts, yLabel, note, first, firstHead, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const ch = P ? { x: S.x + 30, y: 330, w: S.w - 60, h: 620 } : { x: S.x + 30, y: 210, w: 1060, h: 640 };
  const yMax = 70;
  const X = (b: number) => ch.x + ((8 - b) / 6) * ch.w;
  const Y = (e: number) => ch.y + ch.h - (e / yMax) * ch.h;
  const draw = ease(ramp(t, 0.05, 0.5));
  const zone = ease(ramp(t, 0.42, 0.52));
  const chips = (i: number) => ease(ramp(t, 0.6 + i * 0.05, 0.66 + i * 0.05));
  // the polyline revealed left → right
  const segs = pts.length - 1;
  const shown = draw * segs;
  const path: string[] = [];
  pts.forEach((p, i) => {
    if (i <= shown) path.push(`${i ? 'L' : 'M'}${X(p.bits)},${Y(p.err)}`);
    else if (i - 1 < shown) {
      const f = shown - (i - 1), a = pts[i - 1];
      path.push(`L${lerp(X(a.bits), X(p.bits), f)},${lerp(Y(a.err), Y(p.err), f)}`);
    }
  });
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: X(4) - 3, top: ch.y, width: 6, height: ch.h, background: ACC_TEXT, opacity: zone, borderRadius: 3 }} />
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0 }}>
        <line x1={ch.x} y1={ch.y + ch.h} x2={ch.x + ch.w} y2={ch.y + ch.h} stroke={CLAUDE.INK} strokeWidth={4} />
        <line x1={ch.x} y1={ch.y} x2={ch.x} y2={ch.y + ch.h} stroke={CLAUDE.INK} strokeWidth={4} />
        <path d={path.join(' ')} fill="none" stroke={CLAUDE.INK} strokeWidth={7} strokeLinejoin="round" />
        {pts.map((p, i) => i <= shown + 0.001
          ? <circle key={p.bits} cx={X(p.bits)} cy={Y(p.err)} r={p.bits < 4 ? 17 : 14} fill={p.bits < 4 ? CLAUDE.SPARK : CLAUDE.INK} /> : null)}
      </svg>
      {pts.map((p, i) => (
        <React.Fragment key={p.bits}>
          <div style={{ position: 'absolute', left: X(p.bits) - 40, width: 80, top: ch.y + ch.h + 14, textAlign: 'center', fontFamily: SANS, fontSize: P ? 44 : 38, color: CLAUDE.INK,
            opacity: ease(ramp(t, 0.03, 0.09)) }}>{p.bits}</div>
          <div style={{ position: 'absolute', top: Y(p.err) - (P ? 66 : 58), fontFamily: SERIF, fontSize: P ? 46 : 42, color: p.bits < 4 ? ACC_TEXT : CLAUDE.INK,
            opacity: i <= shown + 0.001 ? 1 : 0, ...(p.bits === 8 ? { left: X(p.bits) + 30 } : { left: X(p.bits) - (p.bits === 2 ? 150 : 110) }) }}>{p.err.toFixed(1)}</div>
        </React.Fragment>
      ))}
      <Label text="bits per weight" size={P ? 42 : 36} color={CLAUDE.INK_SOFT} style={{ left: ch.x, top: ch.y + ch.h + (P ? 70 : 62), opacity: ease(ramp(t, 0.03, 0.09)) }} />
      <Label text={yLabel} size={P ? 42 : 36} color={CLAUDE.INK_SOFT} style={{ left: ch.x + 24, top: ch.y, opacity: ease(ramp(t, 0.03, 0.09)) }} />
      <div style={{ position: 'absolute', left: X(4) + 16, top: ch.y + (P ? 230 : 250), opacity: zone }}>
        <Pill text="below 4 bits" size={P ? 44 : 40} accent />
      </div>
      <div style={{ position: 'absolute', display: 'flex', flexDirection: P ? 'row' : 'column', flexWrap: 'wrap', gap: P ? 16 : 22, alignItems: P ? 'center' : 'flex-start',
        ...(P ? { left: S.x, top: ch.y + ch.h + 150, width: S.w } : { left: ch.x + ch.w + 80, top: ch.y + 40, width: S.r - (ch.x + ch.w + 80) }) }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 54 : 50, color: CLAUDE.INK, opacity: chips(0) }}>{firstHead}</span>
        {first.map((f, i) => <Pill key={f} text={f} size={P ? 48 : 46} a={chips(i)} />)}
      </div>
      <Label text={note} size={P ? 38 : 32} color={CLAUDE.INK_SOFT}
        style={{ ...(P ? { left: S.x, top: ch.y + ch.h + 260, width: S.w } : { left: ch.x + ch.w + 80, top: ch.y + 430, width: S.r - (ch.x + ch.w + 80) }), opacity: ease(ramp(t, 0.5, 0.58)) }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// QzLocal — llama.cpp + Ollama: 4-bit by default; the verdict
// ===========================================================================
export const qzLocalSchema = z.object({
  title: z.string().default('Running it locally'),
  tools: z.array(z.object({ name: z.string(), logo: z.string(), dark: z.boolean() })).default([
    { name: 'llama.cpp', logo: 'logos/llama-cpp/llama1-logo.png', dark: true },
    { name: 'Ollama', logo: 'logos/ollama/ollama-01.svg', dark: false },
  ]),
  badge: z.string().default('4-bit by default'),
  format: z.string().default('GGUF · Q4_K_M'),
  lines: z.array(z.string()).default([
    'A model is billions of numbers; fewer bits per number, a smaller model.',
    '4 bits: about a quarter of the memory, and often faster.',
    'Below 4 bits, test the tasks you care about first.',
  ]),
  sparkLine: z.string().default('Same model, fewer bits.'),
  durationSeconds: z.number().optional(),
});
export const qzLocalMeta = durMeta(5);
export const QzLocal: React.FC<z.infer<typeof qzLocalSchema>> = ({ title, tools, badge, format, lines, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const lw = P ? S.w : 760;
  const lh = P ? 230 : 230;
  const bIn = ease(ramp(t, 0.26, 0.34));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {tools.map((tl, i) => {
        const a = ease(ramp(t, 0.03 + i * 0.07, 0.1 + i * 0.07));
        const x = S.x, y = (P ? 300 : 210) + i * (lh + 30);
        return (
          <Card key={tl.name} style={{ left: x, top: y, width: P ? (S.w - 30) / 2 + (i ? 0 : 0) : lw, height: lh, opacity: a, overflow: 'hidden',
            background: tl.dark ? '#1E2021' : CLAUDE.CARD, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 30,
            ...(P ? { left: x + i * ((S.w + 30) / 2), top: 300 } : {}) }}>
            <Img src={staticFile(tl.logo)} style={tl.dark ? { width: '100%', height: '100%', objectFit: 'cover' } : { height: lh * 0.7 }} />
            {!tl.dark && <span style={{ fontFamily: SANS, fontWeight: 600, fontSize: P ? 54 : 64, color: CLAUDE.INK }}>{tl.name}</span>}
          </Card>
        );
      })}
      <div style={{ position: 'absolute', display: 'flex', alignItems: 'center', gap: 22, opacity: bIn, flexWrap: 'wrap',
        ...(P ? { left: S.x, top: 300 + lh + 50, width: S.w } : { left: S.x, top: 210 + 2 * (lh + 30) + 10, width: lw }) }}>
        <Pill text={badge} size={P ? 56 : 50} accent />
        <span style={{ fontFamily: MONO, fontSize: P ? 46 : 42, color: CLAUDE.INK }}>{format}</span>
      </div>
      <div style={{ position: 'absolute', display: 'flex', flexDirection: 'column', gap: P ? 30 : 34, background: CLAUDE.INK, borderRadius: 16,
        boxSizing: 'border-box', padding: P ? '34px 34px' : '40px 44px', opacity: ease(ramp(t, 0.38, 0.44)),
        ...(P ? { left: S.x, top: 740, width: S.w } : { left: S.x + lw + 70, top: 210, width: S.w - lw - 70 }) }}>
        {lines.map((l, i) => {
          const a = ease(ramp(t, 0.42 + i * 0.1, 0.5 + i * 0.1));
          return (
            <div key={l} style={{ display: 'flex', gap: 22, opacity: a, transform: `translateY(${(1 - a) * 16}px)` }}>
              <span style={{ fontFamily: SERIF, fontSize: P ? 58 : 56, color: CLAUDE.SPARK, lineHeight: 1.15 }}>{i + 1}</span>
              <span style={{ fontFamily: SERIF, fontSize: P ? 54 : 52, color: CLAUDE.PAGE, lineHeight: 1.2 }}>{l}</span>
            </div>
          );
        })}
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
