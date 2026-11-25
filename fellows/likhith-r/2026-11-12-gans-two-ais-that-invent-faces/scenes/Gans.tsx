/**
 * Gans.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-gans ("GANs: Two AIs That Invent Faces", @HumanitariansAI).
 *
 * Same contract as Grokking.tsx (stage helpers from JevExplainer.tsx): each component lays out natively
 * for 16:9 (<Name>) and 9:16 (<Name>916) — never a crop — and every motion is a pure function of
 * progress, conformed via `durationSeconds`. Every number from our run comes from ./gansData.ts, which is
 * GENERATED from the reel's evidence/gan_toy.json (seeded numpy 1-D GAN). The faces are seeded ink
 * DRAWINGS (labelled as stand-ins), not GAN output.
 *
 *   GnFace     — a face assembles out of noise; no camera, two competing networks made it
 *   GnIdea     — Goodfellow et al. 2014: generator = forger, discriminator = detective
 *   GnGame     — noise → forger → fake; detective calls real/fake; our run's fakes move onto the bell curve
 *   GnFinish   — our run's detective accuracy: 99.9 % early, settles on the 50 % coin-flip line
 *   GnProgress — blurry 2014 → NVIDIA StyleGAN 2019 → a new face every refresh
 *   GnDanger   — harms, the 2024 Hong Kong video call (≈ US$25 M), diffusion footnote
 *   GnCautions — four cautions
 *   GnClose    — the detective can't tell; the job falls to us
 */
import React from 'react';
import { AbsoluteFill, Img, staticFile } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ACC_TEXT, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';
import { GN } from './gansData';

const W = (P: boolean) => (P ? 1080 : 1920);
const H = (P: boolean) => (P ? 1920 : 1080);
const lerp = (a: number, b: number, p: number) => a + (b - a) * p;
const fmtInt = (n: number) => Math.round(n).toLocaleString('en-US');
const pct = (v: number, dp = 0) => `${(v * 100).toFixed(dp)}%`;

type Curve = ReadonlyArray<ReadonlyArray<number>>; // [step, detective accuracy, forger mean, forger sd]
const CURVE = GN.curve as unknown as Curve;
const HISTS = GN.hists as unknown as Record<string, number[]>;
const SNAPS = GN.snapSteps as unknown as number[];
const REAL = GN.realHist as unknown as number[];

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

const Arrow: React.FC<{ size?: number; color?: string }> = ({ size = 1, color }) => (
  <svg viewBox="0 0 20 16" style={{ width: `${size}em`, height: `${size * 0.8}em`, verticalAlign: '-0.05em', overflow: 'visible', color: color ?? CLAUDE.INK }}>
    <path d="M1 8H18M11 1.5L18 8L11 14.5" fill="none" stroke="currentColor" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

// ---------------------------------------------------------------------------
// seeded hash → [0,1)
// ---------------------------------------------------------------------------
const hash = (s: number) => {
  const x = Math.sin(s * 127.1 + 311.7) * 43758.5453;
  return x - Math.floor(x);
};

// ---------------------------------------------------------------------------
// DrawnFace — a seeded ink portrait (a stand-in for a GAN sample, never a real person)
// ---------------------------------------------------------------------------
// Features in a warm brown > 48 RGB from both INK and MUTE: GATE T's text mask reads small INK strokes as sub-floor text.
const FEAT = '#8A4A2E';
const DrawnFace: React.FC<{ seed: number; size: number; blur?: number; a?: number; bg?: string }> = ({ seed, size, blur = 0, a = 1, bg }) => {
  const r = (k: number) => hash(seed * 13 + k);
  const fw = 64 + r(1) * 16;          // half face width
  const fh = 88 + r(2) * 12;          // half face height
  const ey = 120 + r(3) * 10, ex = 30 + r(4) * 8;
  const brow = (r(5) - 0.5) * 10;
  const nose = 26 + r(6) * 14;
  const mouthW = 22 + r(7) * 12, smile = 4 + r(8) * 12;
  const hair = Math.floor(r(9) * 3);
  const hairPath = [
    `M${100 - fw - 6} ${150} Q${100 - fw - 14} ${40} 100 ${34} Q${100 + fw + 14} ${40} ${100 + fw + 6} ${150} Q${100 + fw - 4} ${80} 100 ${76} Q${100 - fw + 4} ${80} ${100 - fw - 6} 150Z`,
    `M${100 - fw - 4} ${130} Q${100 - fw} ${36} 100 ${40} Q${100 + fw} ${36} ${100 + fw + 4} ${130} L${100 + fw - 6} ${96} Q100 ${70} ${100 - fw + 6} ${96}Z`,
    `M${100 - fw - 10} ${230} Q${100 - fw - 24} ${30} 100 ${32} Q${100 + fw + 24} ${30} ${100 + fw + 10} ${230} L${100 + fw - 2} ${150} Q${100 + fw - 6} ${84} 100 ${80} Q${100 - fw + 6} ${84} ${100 - fw + 2} 150Z`,
  ][hair];
  const id = `fb${seed}`;
  return (
    <svg viewBox="0 0 200 260" width={size} height={size * 1.3} style={{ opacity: a, display: 'block' }}>
      {blur > 0 && <defs><filter id={id}><feGaussianBlur stdDeviation={blur} /></filter></defs>}
      {bg && <rect x={0} y={0} width={200} height={260} rx={10} fill={bg} />}
      <g filter={blur > 0 ? `url(#${id})` : undefined}>
        {/* shoulders */}
        <path d={`M20 260 Q30 ${205} 100 ${200} Q170 ${205} 180 260Z`} fill={CLAUDE.INK} />
        {/* neck */}
        <path d={`M86 ${150 + fh * 0.45} L86 205 L114 205 L114 ${150 + fh * 0.45}`} fill={CLAUDE.CARD} stroke={CLAUDE.INK} strokeWidth={5} />
        <ellipse cx={100} cy={140} rx={fw} ry={fh * 0.75} fill={CLAUDE.CARD} stroke={CLAUDE.INK} strokeWidth={6} />
        <path d={hairPath} fill={CLAUDE.INK} />
        {/* brows */}
        <path d={`M${100 - ex - 14} ${ey - 16 + brow} L${100 - ex + 12} ${ey - 18 - brow}`} stroke={FEAT} strokeWidth={6} strokeLinecap="round" />
        <path d={`M${100 + ex - 12} ${ey - 18 - brow} L${100 + ex + 14} ${ey - 16 + brow}`} stroke={FEAT} strokeWidth={6} strokeLinecap="round" />
        {/* eyes */}
        <ellipse cx={100 - ex} cy={ey} rx={9} ry={6} fill={FEAT} />
        <ellipse cx={100 + ex} cy={ey} rx={9} ry={6} fill={FEAT} />
        {/* nose */}
        <path d={`M100 ${ey + 4} L${96} ${ey + nose} L${106} ${ey + nose + 2}`} fill="none" stroke={FEAT} strokeWidth={5} strokeLinecap="round" strokeLinejoin="round" />
        {/* mouth */}
        <path d={`M${100 - mouthW} ${ey + nose + 22} Q100 ${ey + nose + 22 + smile} ${100 + mouthW} ${ey + nose + 22}`} fill="none" stroke={FEAT} strokeWidth={6} strokeLinecap="round" />
      </g>
    </svg>
  );
};

// noise dots that fade as the face resolves (B02)
const NoiseField: React.FC<{ x: number; y: number; w: number; h: number; a: number; n?: number; seed?: number }> = ({ x, y, w, h, a, n = 160, seed = 7 }) => (
  <svg width={w} height={h} style={{ position: 'absolute', left: x, top: y, opacity: a }}>
    {Array.from({ length: n }, (_, i) => (
      <rect key={i} x={hash(seed + i) * (w - 16)} y={hash(seed + i + 999) * (h - 16)} width={16} height={16} rx={3}
        fill={hash(seed + i + 555) > 0.8 ? ACC_TEXT : CLAUDE.INK} />
    ))}
  </svg>
);

// ===========================================================================
// GnFace — B02 hook
// ===========================================================================
export const gnFaceSchema = z.object({
  title: z.string().default('This person never existed'),
  caption: z.string().default('no camera took this'),
  meta: z.array(z.tuple([z.string(), z.string()])).default([['camera', 'none'], ['lens', 'none'], ['made by', 'two competing AIs']]),
  forger: z.string().default('forger'),
  detective: z.string().default('detective'),
  note: z.string().default('drawn stand-in for a GAN face'),
  sparkLine: z.string().default('Made, not photographed.'),
  durationSeconds: z.number().optional(),
});
export const gnFaceMeta = durMeta(4);
export const GnFace: React.FC<z.infer<typeof gnFaceSchema>> = ({ title, caption, meta, forger, detective, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const noise = 1 - ease(ramp(t, 0.08, 0.34));
  const face = ease(ramp(t, 0.12, 0.34));
  const cap = ease(ramp(t, 0.36, 0.44));
  const mIn = (i: number) => ease(ramp(t, 0.44 + i * 0.06, 0.5 + i * 0.06));
  const vs = ease(ramp(t, 0.66, 0.74));
  const fs = P ? 420 : 370;                       // face svg width
  const fx = P ? S.x + (S.w - fs) / 2 : S.x + 40, fy = P ? 270 : 230;
  const fhh = fs * 1.3;
  const rx = P ? S.x : S.x + fs + 160, rw = P ? S.w : S.r - rx;
  const ry = P ? fy + fhh + 110 : 230;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      {!P && <Title st={st} text={title} />}
      <Card style={{ left: fx - 20, top: fy - 20, width: fs + 40, height: fhh + 40, opacity: ease(ramp(t, 0.02, 0.08)) }} />
      <NoiseField x={fx} y={fy} w={fs} h={fhh} a={noise * ease(ramp(t, 0.02, 0.08))} />
      <div style={{ position: 'absolute', left: fx, top: fy }}><DrawnFace seed={3} size={fs} a={face} /></div>
      <div style={{ position: 'absolute', left: fx, width: fs, top: fy + fhh + 34, textAlign: 'center', opacity: cap }}>
        <Pill text={caption} size={P ? 42 : 40} accent />
      </div>
      {P && <Label text={title} size={76} serif style={{ left: S.x, top: S.y + 40, width: S.w, textAlign: 'center', opacity: ease(ramp(t, 0, 0.1)) }} />}
      <div style={{ position: 'absolute', left: rx, top: ry, width: rw, display: 'flex', flexDirection: 'column', gap: P ? 14 : 26 }}>
        {meta.map(([k, v], i) => (
          <div key={k} style={{ display: 'flex', gap: 24, alignItems: 'baseline', opacity: mIn(i), justifyContent: P ? 'center' : 'flex-start' }}>
            <span style={{ fontFamily: MONO, fontSize: P ? 44 : 50, color: CLAUDE.INK_SOFT, width: P ? 240 : 270, textAlign: P ? 'right' : 'left' }}>{k}</span>
            <span style={{ fontFamily: SERIF, fontSize: P ? 54 : 66, color: i === 2 ? ACC_TEXT : CLAUDE.INK }}>{v}</span>
          </div>
        ))}
      </div>
      <div style={{ position: 'absolute', left: rx, top: P ? ry + 260 : ry + 380, width: rw, display: 'flex', alignItems: 'center', gap: 24, opacity: vs, justifyContent: P ? 'center' : 'flex-start' }}>
        <Pill text={forger} size={P ? 50 : 54} />
        <span style={{ fontFamily: SERIF, fontSize: P ? 56 : 60, color: CLAUDE.INK, fontStyle: 'italic' }}>vs.</span>
        <Pill text={detective} size={P ? 50 : 54} accent />
      </div>
      <Label text={note} size={P ? 34 : 32} color={CLAUDE.INK_SOFT} style={{ left: P ? S.x : fx - 20, width: P ? S.w : fs + 40, textAlign: 'center', top: P ? ry + 360 : fy + fhh + 110, opacity: cap }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GnIdea — B03: the paper and the two roles
// ===========================================================================
export const gnIdeaSchema = z.object({
  title: z.string().default('Generative Adversarial Networks'),
  paper: z.string().default('Generative Adversarial Nets'),
  authors: z.string().default('Goodfellow et al.'),
  year: z.string().default('2014'),
  roles: z.array(z.object({ net: z.string(), role: z.string(), does: z.string() })).default([
    { net: 'generator', role: 'the forger', does: 'makes fakes' },
    { net: 'discriminator', role: 'the detective', does: 'calls real or fake' },
  ]),
  sparkLine: z.string().default('A forger and a detective.'),
  durationSeconds: z.number().optional(),
});
export const gnIdeaMeta = durMeta(6);
export const GnIdea: React.FC<z.infer<typeof gnIdeaSchema>> = ({ title, paper, authors, year, roles, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const pIn = ease(ramp(t, 0.03, 0.12));
  const rIn = (i: number) => ease(ramp(t, 0.34 + i * 0.24, 0.42 + i * 0.24));
  const px = S.x, py = P ? 410 : 220, pw = P ? S.w : 600, ph = P ? 250 : 640;
  const cx = P ? S.x : S.x + pw + 70, cw = P ? S.w : S.r - cx;
  const ch = P ? 270 : 300;
  const cy = (i: number) => (P ? py + ph + 60 + i * (ch + 40) : py + i * (ch + 40));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: px, top: py, width: pw, height: ph, borderRadius: 14, background: CLAUDE.INK, opacity: pIn,
        transform: `translateY(${(1 - pIn) * 20}px)`, boxSizing: 'border-box', padding: P ? '34px 44px' : '70px 50px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
        <div style={{ fontFamily: SERIF, fontSize: P ? 66 : 74, lineHeight: 1.1, color: CLAUDE.CARD }}>{paper}</div>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', flexDirection: P ? 'row' : 'column' }}>
          <div style={{ fontFamily: SANS, fontSize: P ? 44 : 46, color: CLAUDE.CARD }}>{authors}</div>
          <div style={{ fontFamily: SERIF, fontSize: P ? 76 : 96, color: CLAUDE.CARD, marginTop: 8 }}>{year}</div>
        </div>
      </div>
      {roles.map((r, i) => (
        <React.Fragment key={r.net}>
          <Card accent={i === 1} style={{ left: cx, top: cy(i), width: cw, height: ch, opacity: rIn(i), padding: P ? '50px 44px 0' : '70px 50px 0',
            display: 'flex', flexDirection: 'column', gap: 6 }}>
            <span style={{ fontFamily: SERIF, fontSize: P ? 110 : 118, lineHeight: 1.05, color: i ? ACC_TEXT : CLAUDE.INK }}>{r.role}</span>
            <span style={{ fontFamily: SANS, fontSize: P ? 46 : 48, color: CLAUDE.INK }}>{r.does}</span>
          </Card>
          <div style={{ position: 'absolute', left: cx + 34, top: cy(i) - 32, opacity: rIn(i) }}><Pill text={r.net} size={P ? 46 : 48} accent={i === 1} /></div>
        </React.Fragment>
      ))}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// Histogram — the forger's fakes vs the real bell curve (our run)
// ===========================================================================
const histAt = (u: number) => {
  // u in [0,1] across the snapshot list, interpolated bar by bar
  const f = u * (SNAPS.length - 1), i = Math.min(SNAPS.length - 2, Math.floor(f)), k = f - i;
  const a = HISTS[String(SNAPS[i])], b = HISTS[String(SNAPS[i + 1])];
  return { bars: a.map((v, j) => lerp(v, b[j], k)), step: Math.round(lerp(SNAPS[i], SNAPS[i + 1], k)) };
};
const Histogram: React.FC<{ x: number; y: number; w: number; h: number; u: number; a: number; P: boolean; realLabel: string; fakeLabel: string }> = ({ x, y, w, h, u, a, P, realLabel, fakeLabel }) => {
  const { bars, step } = histAt(u);
  const yMax = Math.max(...REAL) * 1.25;
  const n = REAL.length, bw = w / n;
  const Y = (v: number) => y + h - Math.min(1, v / yMax) * h;
  let real = `M${x} ${y + h}`;
  REAL.forEach((v, j) => { real += `L${x + j * bw} ${Y(v)}L${x + (j + 1) * bw} ${Y(v)}`; });
  real += `L${x + w} ${y + h}`;
  const fs = P ? 38 : 38;
  return (
    <>
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0, opacity: a }}>
        {bars.map((v, j) => {
          const top = Y(v);
          return <rect key={j} x={x + j * bw + bw * 0.12} y={top} width={bw * 0.76} height={y + h - top} fill={ACC_TEXT} />;
        })}
        <path d={real} fill="none" stroke={CLAUDE.INK} strokeWidth={6} strokeLinejoin="round" />
        <line x1={x} y1={y + h + 6} x2={x + w} y2={y + h + 6} stroke={CLAUDE.INK} strokeWidth={4} />
      </svg>
      <div style={{ position: 'absolute', left: x, top: y + h + 22, width: w, display: 'flex', gap: 30, alignItems: 'center', opacity: a, flexWrap: 'wrap' }}>
        <span style={{ fontFamily: SANS, fontSize: fs, color: CLAUDE.INK }}>━ {realLabel}</span>
        <span style={{ fontFamily: SANS, fontSize: fs, color: ACC_TEXT }}>■ {fakeLabel}</span>
        <span style={{ fontFamily: MONO, fontSize: fs, color: CLAUDE.INK, marginLeft: 'auto' }}>step {fmtInt(step)}</span>
      </div>
    </>
  );
};

// ===========================================================================
// GnGame — B04: the loop, then our run's fakes landing on the real curve
// ===========================================================================
export const gnGameSchema = z.object({
  title: z.string().default('The game'),
  noise: z.string().default('random noise'),
  forger: z.string().default('forger'),
  fake: z.string().default('fake'),
  real: z.string().default('real'),
  detective: z.string().default('detective'),
  verdict: z.string().default('real or fake?'),
  feedback: z.string().default('both learn from the mistakes'),
  realLabel: z.string().default('real data'),
  fakeLabel: z.string().default("forger's fakes"),
  note: z.string().default('our numpy run: a 1-D bell curve'),
  sparkLine: z.string().default('Each learns from the other.'),
  durationSeconds: z.number().optional(),
});
export const gnGameMeta = durMeta(5.7);
export const GnGame: React.FC<z.infer<typeof gnGameSchema>> = ({ title, noise, forger, fake, real, detective, verdict, feedback, realLabel, fakeLabel, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const r1 = ease(ramp(t, 0.03, 0.14));
  const r2 = ease(ramp(t, 0.22, 0.34));
  const fb = ease(ramp(t, 0.5, 0.58));
  const hIn = ease(ramp(t, 0.5, 0.58));
  const u = ramp(t, 0.56, 0.86);
  const fs = P ? 46 : 50;
  const row = (items: React.ReactNode[], top: number, a: number) => (
    <div style={{ position: 'absolute', left: S.x, top, width: S.w, display: 'flex', alignItems: 'center', gap: P ? 18 : 28, opacity: a, justifyContent: P ? 'center' : 'flex-start', fontSize: fs }}>
      {items.map((it, i) => <React.Fragment key={i}>{i > 0 && <Arrow />}{it}</React.Fragment>)}
    </div>
  );
  const word = (s: string, c?: string) => <span style={{ fontFamily: SANS, fontSize: fs, color: c ?? CLAUDE.INK }}>{s}</span>;
  const y1 = P ? 300 : 210, y2 = P ? 420 : 320;
  const hx = P ? S.x + 20 : S.x + 120, hw = P ? S.w - 40 : 1100;
  const hy = P ? 640 : 520, hh = P ? 440 : 330;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {row([word(noise, CLAUDE.INK_SOFT), <Pill text={forger} size={fs} />, word(fake, ACC_TEXT)], y1 + (P ? 0 : 0), r1)}
      {row([word(`${real} + ${fake}`), <Pill text={detective} size={fs} accent />, word(verdict)], y2, r2)}
      <div style={{ position: 'absolute', left: S.x, width: S.w, top: P ? 530 : 420, textAlign: P ? 'center' : 'left', opacity: fb }}>
        <span style={{ fontFamily: SERIF, fontStyle: 'italic', fontSize: P ? 52 : 52, color: CLAUDE.INK }}>↺ {feedback}</span>
      </div>
      <Histogram x={hx} y={hy} w={hw} h={hh} u={u} a={hIn} P={P} realLabel={realLabel} fakeLabel={fakeLabel} />
      <Label text={note} size={P ? 34 : 34} color={CLAUDE.INK_SOFT} style={P ? { left: S.x, top: hy + hh + 90, width: S.w, textAlign: 'center', opacity: hIn } : { left: hx + hw + 50, top: hy + 40, width: S.r - (hx + hw + 50), opacity: hIn }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GnFinish — B05: detective accuracy falls to the coin-flip line (our run)
// ===========================================================================
export const gnFinishSchema = z.object({
  title: z.string().default("The detective's accuracy"),
  coin: z.string().default('coin flip · 50%'),
  xTitle: z.string().default('training step'),
  sparkLine: z.string().default('A coin flip.'),
  durationSeconds: z.number().optional(),
});
export const gnFinishMeta = durMeta(2.9);
export const GnFinish: React.FC<z.infer<typeof gnFinishSchema>> = ({ title, coin, xTitle, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const xMax = GN.steps as number;
  const b = P ? { x: S.x + 150, y: 330, w: S.w - 230, h: 640 } : { x: S.x + 170, y: 210, w: 1080, h: 600 };
  const X = (s: number) => b.x + (s / xMax) * b.w;
  const Y = (v: number) => b.y + b.h - v * b.h;
  const ax = ease(ramp(t, 0.0, 0.06));
  const lim = ramp(t, 0.04, 0.5) * xMax;
  const pts = CURVE.filter((c) => c[0] >= 1 && c[0] <= Math.max(1, lim)).map((c) => `${X(c[0])},${Y(c[1])}`).join(' ');
  const pk = ease(ramp(t, 0.08, 0.16)), fin = ease(ramp(t, 0.5, 0.6)), cIn = ease(ramp(t, 0.3, 0.4));
  const fs = P ? 38 : 36;
  const ticks = [0, 2000, 4000, 6000].filter((s) => s <= xMax);
  const rx = P ? S.x : b.x + b.w + 60, rw = P ? S.w : S.r - rx;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0 }}>
        <g opacity={ax}>
          <line x1={b.x} y1={b.y + b.h} x2={b.x + b.w} y2={b.y + b.h} stroke={CLAUDE.INK} strokeWidth={4} />
          <line x1={b.x} y1={b.y} x2={b.x} y2={b.y + b.h} stroke={CLAUDE.INK} strokeWidth={4} />
          {ticks.map((s) => <line key={s} x1={X(s)} y1={b.y + b.h + 8} x2={X(s)} y2={b.y + b.h + 22} stroke={CLAUDE.INK} strokeWidth={4} />)}
          {[0, 0.5, 1].map((v) => <line key={v} x1={b.x - 22} y1={Y(v)} x2={b.x - 8} y2={Y(v)} stroke={CLAUDE.INK} strokeWidth={4} />)}
        </g>
        <line x1={b.x + 6} y1={Y(0.5)} x2={b.x + b.w} y2={Y(0.5)} stroke={ACC_TEXT} strokeWidth={4} strokeDasharray="14 12" opacity={cIn} />
        <polyline points={pts} fill="none" stroke={CLAUDE.INK} strokeWidth={6} strokeLinejoin="round" />
      </svg>
      {ticks.map((s) => <Label key={s} text={fmtInt(s)} size={fs} style={{ left: X(s) - 100, width: 200, textAlign: 'center', top: b.y + b.h + 30, opacity: ax }} />)}
      {[{ v: 0, l: '0%' }, { v: 0.5, l: '50%' }, { v: 1, l: '100%' }].map((k) => (
        <Label key={k.l} text={k.l} size={fs} style={{ left: b.x - 188, width: 156, textAlign: 'right', top: Y(k.v) - fs * 0.6, opacity: ax }} />
      ))}
      <Label text={xTitle} size={fs} color={CLAUDE.INK_SOFT} style={{ left: b.x, width: b.w, textAlign: 'center', top: b.y + b.h + 30 + fs * 1.3, opacity: ax }} />
      <Label text={coin} size={P ? 40 : 40} color={ACC_TEXT} style={{ left: b.x + b.w - 420, width: 410, textAlign: 'right', top: Y(0.5) + 18, opacity: cIn }} />
      <div style={{ position: 'absolute', left: rx, top: P ? b.y + b.h + 150 : b.y + 10, width: rw, display: 'flex', flexDirection: P ? 'row' : 'column', gap: P ? 30 : 40, justifyContent: P ? 'space-between' : 'flex-start' }}>
        <div style={{ opacity: pk }}>
          <div style={{ fontFamily: SANS, fontSize: P ? 38 : 38, color: CLAUDE.INK }}>early · step {fmtInt(GN.accPeakStep as number)}</div>
          <div style={{ fontFamily: SERIF, fontSize: P ? 110 : 120, lineHeight: 1.05, color: CLAUDE.INK }}>{pct(GN.accPeak as number, 1)}</div>
        </div>
        <div style={{ opacity: fin }}>
          <div style={{ fontFamily: SANS, fontSize: P ? 38 : 38, color: ACC_TEXT }}>last 500 steps</div>
          <div style={{ fontFamily: SERIF, fontSize: P ? 110 : 120, lineHeight: 1.05, color: ACC_TEXT }}>{pct(GN.accLast500 as number, 1)}</div>
        </div>
      </div>
      <Spark st={st} text={sparkLine} at={0.72} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GnProgress — B06: blurry 2014 → StyleGAN 2019 → a new face every refresh
// ===========================================================================
export const gnProgressSchema = z.object({
  title: z.string().default('How good it got'),
  early: z.string().default('2014 · first GAN faces'),
  earlyNote: z.string().default('small and blurry'),
  style: z.string().default('2019 · StyleGAN'),
  styleNote: z.string().default('sharp, high-resolution'),
  site: z.string().default('thispersondoesnotexist.com'),
  siteNote: z.string().default('a new fake face every refresh'),
  note: z.string().default('faces: drawn stand-ins'),
  sparkLine: z.string().default('A new face every refresh.'),
  durationSeconds: z.number().optional(),
});
export const gnProgressMeta = durMeta(6);
export const GnProgress: React.FC<z.infer<typeof gnProgressSchema>> = ({ title, early, earlyNote, style, styleNote, site, siteNote, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const a = [ease(ramp(t, 0.03, 0.12)), ease(ramp(t, 0.28, 0.37)), ease(ramp(t, 0.55, 0.64))];
  const refreshes = Math.max(0, Math.floor((t - 0.6) / 0.07));
  const siteSeed = 40 + refreshes;
  const n = 3;
  const colW = P ? S.w : (S.w - 2 * 50) / 3;
  const cardH = P ? 300 : 680;
  const pos = (i: number) => (P ? { x: S.x, y: 270 + i * (cardH + 34) } : { x: S.x + i * (colW + 50), y: 200 });
  const faceS = P ? 200 : 260;
  const panels = [
    { head: early, sub: earlyNote, face: <DrawnFace seed={11} size={faceS} blur={9} a={0.6} />, logo: null as string | null, mono: false },
    { head: style, sub: styleNote, face: <DrawnFace seed={23} size={faceS} />, logo: 'logos/nvidia/nvidia-01.svg', mono: false },
    { head: site, sub: siteNote, face: <DrawnFace seed={siteSeed} size={faceS} />, logo: null, mono: true },
  ];
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {panels.slice(0, n).map((p, i) => {
        const { x, y } = pos(i);
        return (
          <Card key={i} accent={i === 2} style={{ left: x, top: y, width: colW, height: cardH, opacity: a[i], padding: P ? '20px 34px' : '40px 36px',
            display: 'flex', flexDirection: P ? 'row' : 'column', alignItems: P ? 'center' : 'flex-start', gap: P ? 34 : 24 }}>
            <div style={{ flex: 'none', alignSelf: P ? 'center' : 'center' }}>{p.face}</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 12, minWidth: 0 }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
                {p.logo && <Img src={staticFile(p.logo)} style={{ height: P ? 46 : 52 }} />}
                  {p.mono
                  ? <Pill text={p.head} size={P ? 30 : 27} accent style={{ fontFamily: MONO }} />
                  : <span style={{ fontFamily: SANS, fontSize: 44, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>{p.head}</span>}
              </div>
              {/* filled pills: an all-x-height serif word ("small") is a sub-floor run to GATE T */}
              <Pill text={p.sub} size={P ? 36 : 36} style={{ alignSelf: 'flex-start' }} />
              {i === 2 && <Pill text={`↻ refresh × ${refreshes + 1}`} size={P ? 32 : 32} accent style={{ alignSelf: 'flex-start', fontFamily: MONO }} />}
            </div>
          </Card>
        );
      })}
      <Label text={note} size={P ? 34 : 32} color={CLAUDE.INK_SOFT} style={P ? { left: S.x, top: 270 + 3 * (cardH + 34) - 10, width: S.w, textAlign: 'right', opacity: a[0] } : { left: S.x, top: 200 + cardH + 14, width: S.w, textAlign: 'right', opacity: a[0] }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GnDanger — B07: harms + the 2024 Hong Kong video call
// ===========================================================================
export const gnDangerSchema = z.object({
  title: z.string().default('The deepfake era'),
  harms: z.array(z.string()).default(['fake faces for bot and scam accounts', 'faked videos of real people', 'non-consensual imagery']),
  tiles: z.array(z.tuple([z.string(), z.boolean()])).default([['"CFO"', true], ['"colleague"', true], ['"colleague"', true], ['employee', false]]),
  fakeTag: z.string().default('deepfake'),
  realTag: z.string().default('real'),
  amount: z.string().default('≈ US$25 million'),
  where: z.string().default('Hong Kong · early 2024 · HK$200 million'),
  footnote: z.string().default('Newer deepfakes often use diffusion models. GANs opened the door.'),
  sparkLine: z.string().default('Seeing is not believing.'),
  durationSeconds: z.number().optional(),
});
export const gnDangerMeta = durMeta(10.4);
export const GnDanger: React.FC<z.infer<typeof gnDangerSchema>> = ({ title, harms, tiles, fakeTag, realTag, amount, where, footnote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const hIn = (i: number) => ease(ramp(t, 0.04 + i * 0.09, 0.1 + i * 0.09));
  const gIn = ease(ramp(t, 0.4, 0.48));
  const tagIn = (i: number) => ease(ramp(t, 0.5 + i * 0.04, 0.54 + i * 0.04));
  const aIn = ease(ramp(t, 0.6, 0.68));
  const fIn = ease(ramp(t, 0.74, 0.8));
  // layout
  const lx = S.x, lw = P ? S.w : 900;
  const hy = P ? 280 : 210;
  const gx = P ? S.x : S.x + lw + 60, gw = P ? S.w : S.r - gx;
  const gy = P ? 520 : 210;
  const tw = (gw - 24) / 2, th = P ? 210 : 300;
  const ay = P ? gy + 2 * th + 24 + 30 : 560;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: lx, top: hy, width: lw, display: 'flex', flexDirection: 'column', gap: P ? 14 : 20, alignItems: 'flex-start' }}>
        {harms.map((h, i) => <Pill key={h} text={h} size={P ? 40 : 42} a={hIn(i)} />)}
      </div>
      {tiles.map(([who, fake], i) => {
        const x = gx + (i % 2) * (tw + 24), y = gy + Math.floor(i / 2) * (th + 24);
        return (
          <div key={i} style={{ position: 'absolute', left: x, top: y, width: tw, height: th, borderRadius: 14, background: CLAUDE.INK, opacity: gIn, overflow: 'hidden' }}>
            <div style={{ position: 'absolute', left: (tw - th * 0.62) / 2, top: 18 }}>
              <DrawnFace seed={60 + i} size={th * 0.62} bg={CLAUDE.CARD} />
            </div>
            <div style={{ position: 'absolute', left: 14, bottom: 12, fontFamily: SANS, fontSize: P ? 32 : 32, color: CLAUDE.CARD }}>{who}</div>
            <div style={{ position: 'absolute', right: 12, top: 12 }}>
              <Pill text={fake ? fakeTag : realTag} size={P ? 30 : 32} accent={fake} fill={fake ? undefined : CLAUDE.INK_SOFT} a={tagIn(i)} />
            </div>
          </div>
        );
      })}
      <div style={{ position: 'absolute', left: lx, top: ay, width: lw, opacity: aIn }}>
        <div style={{ fontFamily: SERIF, fontSize: P ? 110 : 120, lineHeight: 1.05, color: ACC_TEXT, whiteSpace: 'nowrap' }}>{amount}</div>
        <div style={{ fontFamily: SANS, fontSize: P ? 40 : 40, color: CLAUDE.INK, marginTop: 8 }}>{where}</div>
      </div>
      <Label text={footnote} size={P ? 36 : 34} color={CLAUDE.INK_SOFT} style={{ left: lx, top: P ? ay + 190 : 830, width: P ? S.w : lw + 100, opacity: fIn }} />
      <Spark st={st} text={sparkLine} at={0.86} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GnCautions — B08: four cautions, revealed in step with the narration
// ===========================================================================
export const gnCautionsSchema = z.object({
  title: z.string().default('What you can do'),
  items: z.array(z.object({ head: z.string(), body: z.string(), at: z.number() })).default([
    { head: 'Verify', body: 'Confirm a surprising request through a second channel you already trust', at: 0.02 },
    { head: 'Check', body: 'Look for content credentials (the C2PA standard)', at: 0.37 },
    { head: 'Doubt', body: 'Detectors miss fakes: a "real" verdict is not proof', at: 0.53 },
    { head: 'Consent', body: "Never create or share someone's likeness without their consent", at: 0.68 },
  ]),
  sparkLine: z.string().default('Verify, then trust.'),
  durationSeconds: z.number().optional(),
});
export const gnCautionsMeta = durMeta(7.2);
export const GnCautions: React.FC<z.infer<typeof gnCautionsSchema>> = ({ title, items, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const colW = P ? S.w : (S.w - 50) / 2;
  const ch = P ? 230 : 330;
  const pos = (i: number) => (P ? { x: S.x, y: 270 + i * (ch + 26) } : { x: S.x + (i % 2) * (colW + 50), y: 200 + Math.floor(i / 2) * (ch + 34) });
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {items.map((it, i) => {
        const a = ease(ramp(t, it.at, it.at + 0.07));
        const { x, y } = pos(i);
        return (
          <Card key={it.head} accent={i === 3} style={{ left: x, top: y, width: colW, height: ch, opacity: a, transform: `translateY(${(1 - a) * 16}px)`,
            padding: P ? '26px 36px' : '40px 44px', display: 'flex', gap: P ? 28 : 34, alignItems: 'flex-start' }}>
            <span style={{ fontFamily: SERIF, fontSize: P ? 120 : 140, lineHeight: 0.9, color: ACC_TEXT, flex: 'none' }}>{i + 1}</span>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
              <span style={{ fontFamily: SERIF, fontSize: P ? 62 : 66, lineHeight: 1.05, color: CLAUDE.INK }}>{it.head}</span>
              <span style={{ fontFamily: SANS, fontSize: P ? 38 : 42, lineHeight: 1.2, color: CLAUDE.INK }}>{it.body}</span>
            </div>
          </Card>
        );
      })}
      <Spark st={st} text={sparkLine} at={0.88} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GnClose — B09: the detective can't tell; the job falls to us
// ===========================================================================
export const gnCloseSchema = z.object({
  title: z.string().default('When the detective can’t tell'),
  detective: z.string().default('detective'),
  verdict: z.string().default('real? fake?'),
  us: z.string().default('us'),
  usNote: z.string().default('ask, verify, consent'),
  sparkLine: z.string().default('The job falls to us.'),
  durationSeconds: z.number().optional(),
});
export const gnCloseMeta = durMeta(2.95);
export const GnClose: React.FC<z.infer<typeof gnCloseSchema>> = ({ title, detective, verdict, us, usNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const dIn = ease(ramp(t, 0.02, 0.12));
  const arr = ease(ramp(t, 0.3, 0.42));
  const uIn = ease(ramp(t, 0.4, 0.52));
  const lx = S.x, top = P ? 320 : 240;
  const leftW = P ? S.w : 760;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: lx, top, width: leftW, height: P ? 440 : 560, opacity: dIn, padding: P ? '60px 44px' : '70px 50px', display: 'flex', flexDirection: 'column', gap: 14 }}>
        <Pill text={detective} size={P ? 50 : 54} accent style={{ alignSelf: 'flex-start' }} />
        <span style={{ fontFamily: SERIF, fontSize: P ? 96 : 104, lineHeight: 1.05, color: CLAUDE.INK }}>{verdict}</span>
        <span style={{ fontFamily: SANS, fontSize: P ? 42 : 44, color: CLAUDE.INK }}>right {pct(GN.accLast500 as number, 1)} of the time</span>
      </Card>
      <div style={{ position: 'absolute', left: P ? S.x + S.w / 2 - 60 : lx + leftW + 50, top: P ? top + 470 : top + 220, fontSize: 120, opacity: arr, transform: P ? 'rotate(90deg)' : undefined }}>
        <Arrow size={1} color={ACC_TEXT} />
      </div>
      <div style={{ position: 'absolute', left: P ? S.x : lx + leftW + 250, top: P ? top + 620 : top + 70, width: P ? S.w : S.r - (lx + leftW + 250), textAlign: P ? 'center' : 'left', opacity: uIn }}>
        <div style={{ fontFamily: SERIF, fontSize: P ? 280 : 320, lineHeight: 1, color: ACC_TEXT }}>{us}</div>
        <div style={{ fontFamily: SANS, fontSize: P ? 46 : 48, color: CLAUDE.INK, marginTop: 10 }}>{usNote}</div>
      </div>
      <Spark st={st} text={sparkLine} at={0.6} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
