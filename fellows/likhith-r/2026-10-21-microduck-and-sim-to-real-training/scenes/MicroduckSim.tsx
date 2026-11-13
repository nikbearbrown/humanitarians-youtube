/**
 * MicroduckSim.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-microduck-sim-to-real ("Microduck and Sim-to-Real Training", @HumanitariansAI).
 *
 * Same contract as RagOkf.tsx (stage helpers from JevExplainer.tsx): each component lays
 * out natively for 16:9 (<Name>) and 9:16 (<Name>916) — never a crop — and every motion
 * is a pure function of progress, conformed via `durationSeconds`. One drawn duck (<Duck>)
 * carries every beat; it walks, sits and falls by pose props, never by a lifted image.
 * Specs and numbers come from SOURCES.md; the B07 fall counts are copied from
 * evidence/sim_to_real_toy.out.txt, not hand-made.
 *
 *   MdHook      — GTC Berlin: four ducks told sit / stand / take a nap; how is that taught?
 *   MdSpec      — 25 cm, 15 motors lit joint by joint, $399, open RL stack (Pollen + HF)
 *   MdSimFirst  — training on fragile hardware (struck) vs. a physics simulation first
 *   MdParallel  — Isaac Lab: a grid of copies walking, falling, resetting across terrains
 *   MdHandoff   — the policy file leaves the sim and lands on the real duck's motors
 *   MdWhySim    — the toy run's 12,649 falls, all reset at zero hardware cost
 *   MdStageFall — "take a nap": three of four topple; the sim-to-real gap
 */
import React from 'react';
import { AbsoluteFill, Img, staticFile } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ACC_TEXT, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';

const Pill: React.FC<{ text: string; size: number; a?: number; accent?: boolean; fill?: string; style?: React.CSSProperties }> = ({ text, size, a = 1, accent, fill, style }) => (
  <span style={{
    display: 'inline-block', padding: `${size * 0.16}px ${size * 0.42}px`, borderRadius: size, boxSizing: 'border-box',
    background: fill ?? (accent ? ACC_TEXT : CLAUDE.INK),
    fontFamily: SANS, fontSize: size, lineHeight: 1.1, color: CLAUDE.CARD, opacity: a, whiteSpace: 'nowrap', ...style,
  }}>{text}</span>
);

const lerp = (a: number, b: number, p: number) => a + (b - a) * p;
const W = (P: boolean) => (P ? 1080 : 1920);
const H = (P: boolean) => (P ? 1920 : 1080);
// deterministic per-index noise in [0, 1)
const hash = (i: number) => { const x = Math.sin(i * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); };

// ===========================================================================
// Duck — the Microduck, drawn. (x, y) is the point between its feet; h its height.
// tilt rotates about the outer foot on the falling side (±90 = lying on the floor, never
// through it; + falls right, − falls left; lying length = h); sit folds the legs;
// walk is a gait phase (radians) that swings the legs and bobs the body.
// joints > 0 lights that many of the 15 motor dots (MdSpec).
// ===========================================================================
// Dots sit BESIDE strokes (legs) or wholly INSIDE outlines (neck, head, beak), never on a
// line: a dot drawn across an outline splits it into fragments GATE T reads as tiny text.
const JOINTS: Array<[number, number, number]> = [
  // per leg: hip yaw, hip roll, hip pitch, knee, ankle (5 × 2) · neck pitch, head pitch, head yaw, head roll · beak (5)
  [32.5, 96, 4.2], [32.5, 102, 4.2], [32.5, 108, 4.2], [31, 114, 4.2], [31, 120, 4.2],
  [67.5, 96, 4.2], [67.5, 102, 4.2], [67.5, 108, 4.2], [69, 114, 4.2], [69, 120, 4.2],
  [56.5, 51, 4.2], [52, 33, 4.2], [52, 24, 4.2], [60, 37, 4.2], [80, 31, 2.4],
];
export const Duck: React.FC<{
  x: number; y: number; h: number; tilt?: number; sit?: number; walk?: number; a?: number;
  joints?: number; outline?: string; ghost?: boolean;
}> = ({ x, y, h, tilt = 0, sit = 0, walk, a = 1, joints = 0, outline = CLAUDE.INK, ghost }) => {
  const w = h * 0.8;
  const sw = walk === undefined ? 0 : Math.sin(walk);
  const bob = walk === undefined ? 0 : Math.abs(Math.cos(walk)) * 2;
  const drop = sit * 18 - bob;
  const hipY = 86 + drop;
  const knee = (side: number, ph: number) => ({ x: 50 + side * (12 + sit * 10) + ph * 6, y: lerp(106, 112, sit) + drop * 0.3 });
  const foot = (side: number, ph: number) => ({ x: 50 + side * 12 + ph * 9, y: 124 - Math.max(0, -ph) * 4 });
  const leg = (side: number, ph: number) => {
    const k = knee(side, ph), f = foot(side, ph);
    return <polyline points={`${50 + side * 10},${hipY} ${k.x},${k.y} ${f.x},${f.y} ${f.x + 8},${f.y}`}
      fill="none" stroke={ghost ? CLAUDE.GHOST : outline} strokeWidth={4} strokeLinecap="round" strokeLinejoin="round" />;
  };
  const ink = ghost ? CLAUDE.GHOST : outline;
  const dash = ghost ? { strokeDasharray: '6 5' } : {};
  const dots = joints > 0 && JOINTS.slice(0, joints).map(([jx, jy, r], i) => (
    <circle key={i} cx={jx} cy={jy + (i >= 10 ? drop : 0)} r={r} fill={CLAUDE.SPARK} stroke={i === 14 ? 'none' : CLAUDE.CARD} strokeWidth={1.5} />
  ));
  return (
    <svg width={w} height={h} viewBox="0 0 100 125" style={{
      position: 'absolute', left: x - w / 2, top: y - h, opacity: a, overflow: 'visible',
      transform: `translateY(${Math.abs(Math.sin((tilt * Math.PI) / 180)) * w * (tilt < 0 ? 0.18 : 0.09)}px) rotate(${tilt}deg)`, transformOrigin: tilt > 0 ? '100% 100%' : tilt < 0 ? '0% 100%' : '50% 100%',
    }}>
      {!ghost && (
        <g transform={`translate(0 ${drop})`}>
          <ellipse cx={50} cy={70} rx={31} ry={22} fill={CLAUDE.CARD} />
          <rect x={50} y={38} width={13} height={20} rx={6} fill={CLAUDE.CARD} />
          <circle cx={58} cy={30} r={16} fill={CLAUDE.CARD} />
        </g>
      )}
      {leg(-1, sw)}
      {leg(1, -sw)}
      <g transform={`translate(0 ${drop})`} fill="none" stroke={ink} strokeWidth={4} {...dash}>
        <ellipse cx={50} cy={70} rx={31} ry={22} />
        {/* neck: two side lines from the head outline to the body outline (no box inside the head) */}
        <path d="M50.5 43 L50.5 50 M62.5 43 L62.5 50" strokeLinecap="round" />
        <circle cx={58} cy={30} r={16} />
      </g>
      <g transform={`translate(0 ${drop})`}>
        <path d="M72 26 L90 31 L72 37 Z" fill={ghost ? 'none' : CLAUDE.INK_SOFT} stroke={ink} strokeWidth={3} strokeLinejoin="round" />
        <circle cx={62} cy={26} r={3} fill={ink} />
      </g>
      {dots}
    </svg>
  );
};

const Logo: React.FC<{ src: string; h: number; style?: React.CSSProperties }> = ({ src, h, style }) => (
  <Img src={staticFile(src)} style={{ height: h, width: 'auto', ...style }} />
);

// ===========================================================================
// MdHook — GTC Berlin: four ducks, three commands, one question
// ===========================================================================
export const mdHookSchema = z.object({
  title: z.string().default('GTC Berlin · October 21, 2026'),
  logo: z.string().default('logos/nvidia/nvidia-01.svg'),
  commands: z.array(z.string()).default(['“Sit.”', '“Stand.”', '“Take a nap.”']),
  speaker: z.string().default('Jensen Huang, on stage'),
  question: z.string().default('How do you teach a robot that?'),
  sparkLine: z.string().default('How is that taught?'),
  durationSeconds: z.number().optional(),
});
export const mdHookMeta = durMeta(6);
export const MdHook: React.FC<z.infer<typeof mdHookSchema>> = ({ title, logo, commands, speaker, question, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const cmdAt = [0.14, 0.32, 0.5];
  const cmdIn = cmdAt.map((c) => ease(ramp(t, c, c + 0.06)));
  const sit = ease(ramp(t, 0.2, 0.28)) * (1 - ease(ramp(t, 0.38, 0.46)));
  const qIn = ease(ramp(t, 0.64, 0.72));
  const floorY = P ? 1010 : 880;
  const dh = P ? 250 : 380;
  const span = P ? S.w - 60 : 1080;
  const x0 = P ? S.x + 30 : S.x + 40;
  const active = cmdIn[2] > 0.5 ? 2 : cmdIn[1] > 0.5 ? 1 : cmdIn[0] > 0.5 ? 0 : -1;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', opacity: ease(ramp(t, 0.02, 0.1)), ...(P ? { left: S.r - 150, top: 330 } : { left: S.r - 150, top: S.y + 4 }) }}>
        <Logo src={logo} h={P ? 150 : 150} />
      </div>
      {/* the stage */}
      <div style={{ position: 'absolute', left: x0 - 20, top: floorY, width: span + 40, height: 8, borderRadius: 4, background: CLAUDE.INK_SOFT, opacity: ease(ramp(t, 0.02, 0.08)) }} />
      {[0, 1, 2, 3].map((i) => {
        const cx = x0 + span * (i + 0.5) / 4;
        const a = ease(ramp(t, 0.03 + i * 0.025, 0.09 + i * 0.025));
        return <Duck key={i} x={cx} y={floorY} h={dh} a={a} sit={sit} walk={t < 0.14 ? t * 60 + i : undefined} />;
      })}
      {/* question marks above the ducks once "take a nap" lands */}
      {[0, 1, 2, 3].map((i) => (
        <div key={i} style={{ position: 'absolute', left: x0 + span * (i + 0.5) / 4 - 20, top: floorY - dh - (P ? 90 : 100),
          fontFamily: SERIF, fontSize: P ? 80 : 84, color: CLAUDE.INK, opacity: ease(ramp(t, 0.56 + i * 0.02, 0.6 + i * 0.02)) }}>?</div>
      ))}
      {/* command column */}
      <div style={{ position: 'absolute', display: 'flex', gap: P ? 18 : 22, flexDirection: P ? 'row' : 'column', flexWrap: 'wrap',
        ...(P ? { left: S.x, top: 520, width: S.w } : { left: S.x + 1200, top: 240, width: S.w - 1200 }) }}>
        {P
          ? <div style={{ width: '100%', opacity: cmdIn[0] }}><Pill text={speaker} size={46} fill={CLAUDE.INK_SOFT} /></div>
          : <span style={{ fontFamily: SANS, fontSize: 42, color: CLAUDE.INK_SOFT, width: '100%', opacity: cmdIn[0] }}>{speaker}</span>}
        {commands.map((c, i) => (
          <Pill key={c} text={c} size={P ? 60 : 64} accent={i === active} a={0.25 + 0.75 * cmdIn[i]} />
        ))}
      </div>
      <Card accent style={{ opacity: qIn, transform: `translateY(${(1 - qIn) * 24}px)`, padding: P ? '26px 32px' : '24px 40px',
        ...(P ? { left: S.x, top: 1100, width: S.w } : { left: S.x + 1200, top: 690, width: S.w - 1200 }) }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 70 : 60, lineHeight: 1.1, color: CLAUDE.INK }}>{question}</span>
      </Card>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MdSpec — what Microduck is: 25 cm, 15 motors, $399, an RL stack you can rerun
// ===========================================================================
export const mdSpecSchema = z.object({
  title: z.string().default('Meet Microduck'),
  height: z.string().default('25 cm'),
  motors: z.number().default(15),
  motorsLabel: z.string().default('motors'),
  price: z.string().default('$399'),
  priceNote: z.string().default('preorder, before tax + shipping'),
  makers: z.string().default('Pollen Robotics · Hugging Face'),
  logos: z.array(z.string()).default(['logos/pollen-robotics/pollen-robotics-01.svg', 'logos/huggingface/huggingface-01.svg']),
  open: z.array(z.string()).default(['SDK', 'simulation', 'RL training stack']),
  openLabel: z.string().default('open source, Apache-2.0'),
  sparkLine: z.string().default('Retrain it yourself.'),
  durationSeconds: z.number().optional(),
});
export const mdSpecMeta = durMeta(6);
export const MdSpec: React.FC<z.infer<typeof mdSpecSchema>> = ({ title, height, motors, motorsLabel, price, priceNote, makers, logos, open, openLabel, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const dh = P ? 500 : 640;
  const barX = S.x + (P ? 150 : 240);
  const duck = P ? { x: barX + 60 + dh * 0.4, y: 400 + dh } : { x: barX + 80 + dh * 0.4, y: 230 + dh + 30 };
  const lit = Math.floor(ease(ramp(t, 0.34, 0.6)) * motors);
  const dimIn = ease(ramp(t, 0.16, 0.26));
  const col = P ? { x: S.x + 600, y: 340, w: S.w - 600 } : { x: S.x + 860, y: 230, w: S.w - 860 };
  const row = (at: number) => ease(ramp(t, at, at + 0.07));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Duck x={duck.x} y={duck.y} h={dh} joints={lit} a={ease(ramp(t, 0.02, 0.1))} />
      {/* height dimension line */}
      <div style={{ position: 'absolute', left: barX, top: duck.y - dh * dimIn, width: 5, height: dh * dimIn, background: CLAUDE.INK }} />
      {[0, 1].map((k) => <div key={k} style={{ position: 'absolute', left: barX - 16, top: k ? duck.y - 3 : duck.y - dh - 3, width: 37, height: 5, background: CLAUDE.INK, opacity: dimIn }} />)}
      {/* portrait: the label sits above the bar (no room to its left inside SAFE) */}
      <div style={{ position: 'absolute', opacity: dimIn, ...(P
        ? { left: barX, top: duck.y - dh - 84, transform: 'translateX(-50%)' }
        : { left: barX - 30, top: duck.y - dh / 2 - 40, transform: 'translateX(-100%)' }) }}>
        <Pill text={height} size={P ? 48 : 48} />
      </div>
      {/* spec column */}
      <div style={{ position: 'absolute', left: col.x, top: col.y, width: col.w, display: 'flex', flexDirection: 'column', gap: P ? 34 : 30 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 24, opacity: row(0.04) }}>
          {logos.map((l) => <Logo key={l} src={l} h={P ? 110 : 140} />)}
        </div>
        <span style={{ fontFamily: SANS, fontSize: P ? 46 : 44, color: CLAUDE.INK, opacity: row(0.06), lineHeight: 1.15 }}>{makers}</span>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 20, opacity: row(0.34) }}>
          <span style={{ fontFamily: SERIF, fontSize: P ? 120 : 120, lineHeight: 1, color: ACC_TEXT }}>{lit || motors}</span>
          <span style={{ fontFamily: SANS, fontSize: P ? 50 : 50, color: CLAUDE.INK }}>{motorsLabel}</span>
        </div>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 20, flexWrap: 'wrap', opacity: row(0.62) }}>
          <span style={{ fontFamily: SERIF, fontSize: P ? 120 : 120, lineHeight: 1, color: CLAUDE.INK }}>{price}</span>
          <span style={{ fontFamily: SANS, fontSize: P ? 40 : 38, color: CLAUDE.INK_SOFT }}>{priceNote}</span>
        </div>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 14, alignItems: 'center', opacity: row(0.74) }}>
          {open.map((o, i) => <Pill key={o} text={o} size={P ? 38 : 44} accent={i === open.length - 1} />)}
        </div>
        <span style={{ fontFamily: SANS, fontSize: P ? 42 : 40, color: CLAUDE.INK_SOFT, opacity: row(0.78) }}>{openLabel}</span>
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MdSimFirst — not on fragile hardware: inside a physics simulation first
// ===========================================================================
export const mdSimFirstSchema = z.object({
  title: z.string().default('Sim-to-real transfer'),
  realHead: z.string().default('Train on the real robot'),
  realNote: z.string().default('fragile servos, one body, real time'),
  simHead: z.string().default('Train in a physics simulation'),
  simNote: z.string().default('virtual body, virtual floor'),
  transfer: z.string().default('then transfer to hardware'),
  sparkLine: z.string().default('Sim first, then real.'),
  durationSeconds: z.number().optional(),
});
export const mdSimFirstMeta = durMeta(5);
export const MdSimFirst: React.FC<z.infer<typeof mdSimFirstSchema>> = ({ title, realHead, realNote, simHead, simNote, transfer, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const colW = P ? S.w : (S.w - 80) / 2;
  const boxH = P ? 430 : 600;
  const L = P ? { x: S.x, y: 300 } : { x: S.x, y: 230 };
  const R = P ? { x: S.x, y: 300 + boxH + 120 } : { x: S.x + colW + 80, y: 230 };
  const fall = ease(ramp(t, 0.1, 0.22));
  const strike = ease(ramp(t, 0.3, 0.38));
  const rIn = ease(ramp(t, 0.4, 0.5));
  const xfer = ease(ramp(t, 0.68, 0.8));
  const dh = P ? 250 : 290;
  const grid = (bx: number, by: number) => {
    const lines = [];
    // inset 12px so no grid line touches (and splits) the accent card border
    const gx0 = bx + 12, gx1 = bx + colW - 12, gy0 = by + 90, gy1 = by + boxH - 12;
    for (let i = 1; i < 8; i++) lines.push(<line key={`v${i}`} x1={bx + (colW * i) / 8} y1={gy0} x2={bx + (colW * i) / 8} y2={gy1} stroke={CLAUDE.BORDER} strokeWidth={2} />);
    for (let j = 0; j < 5; j++) lines.push(<line key={`h${j}`} x1={gx0} y1={gy0 + ((gy1 - gy0) * j) / 5} x2={gx1} y2={gy0 + ((gy1 - gy0) * j) / 5} stroke={CLAUDE.BORDER} strokeWidth={2} />);
    return lines;
  };
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {/* real hardware lane */}
      <Card style={{ left: L.x, top: L.y, width: colW, height: boxH, opacity: 1 - 0.45 * strike }} />
      {/* the strike sits BEHIND the glyphs so it never splits a letter (GATE T reads split glyphs as tiny runs) */}
      <div style={{ position: 'absolute', left: L.x + (P ? 24 : 30), top: L.y + (P ? 20 : 22), opacity: ease(ramp(t, 0.02, 0.08)) }}>
        <span style={{ position: 'relative', display: 'inline-block' }}>
          <span style={{ position: 'absolute', left: 0, top: '52%', height: P ? 9 : 7, width: `${strike * 100}%`, background: CLAUDE.SPARK, zIndex: 0 }} />
          {P
            ? <span style={{ position: 'relative', zIndex: 1 }}><Pill text={realHead} size={48} fill={CLAUDE.INK_SOFT} /></span>
            : <span style={{ position: 'relative', zIndex: 1, fontFamily: SERIF, fontSize: 54, color: CLAUDE.INK }}>{realHead}</span>}
        </span>
      </div>
      <div style={{ position: 'absolute', left: L.x + 40, top: L.y + boxH - 40, width: colW - 80, height: 5, background: CLAUDE.INK_SOFT }} />
      <Duck x={L.x + colW * 0.36} y={L.y + boxH - 40} h={dh} tilt={fall * 82} a={0.4 + 0.6 * (1 - strike * 0.5)} />
      {/* crack marks where it hits */}
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0, opacity: ease(ramp(t, 0.2, 0.24)) }}>
        {[[-1, -1], [0, -1.4], [1, -1]].map(([dx, dy], k) => {
          const cx = L.x + colW * 0.36 + dh * 0.9, cy = L.y + boxH - 60;
          return <line key={k} x1={cx + dx * 20} y1={cy + dy * 20} x2={cx + dx * 50} y2={cy + dy * 50} stroke={CLAUDE.SPARK} strokeWidth={6} strokeLinecap="round" />;
        })}
      </svg>
      <div style={{ position: 'absolute', left: L.x + colW - 30, top: L.y + 120, transform: 'translateX(-100%)', opacity: ease(ramp(t, 0.18, 0.24)) }}>
        <Pill text={realNote} size={P ? 40 : 38} fill={CLAUDE.INK_SOFT} style={{ whiteSpace: P ? 'nowrap' : 'normal', maxWidth: P ? undefined : colW * 0.5 }} />
      </div>
      {/* simulation lane */}
      <Card accent style={{ left: R.x, top: R.y, width: colW, height: boxH, opacity: rIn }} />
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0, opacity: rIn }}>{grid(R.x, R.y)}</svg>
      <div style={{ position: 'absolute', left: R.x + (P ? 24 : 30), top: R.y + (P ? 20 : 22), fontFamily: SERIF, fontSize: 54, color: CLAUDE.INK, opacity: rIn }}>
        {P ? <Pill text={simHead} size={48} /> : simHead}
      </div>
      <Duck x={R.x + colW * 0.36} y={R.y + boxH - 40} h={dh} ghost outline={CLAUDE.INK} a={rIn} walk={t * 40} />
      <div style={{ position: 'absolute', left: R.x + colW - 30, top: R.y + 120, transform: 'translateX(-100%)', opacity: ease(ramp(t, 0.5, 0.56)) }}>
        <Pill text={simNote} size={P ? 40 : 38} />
      </div>
      {/* the transfer arrow: sim → real */}
      <div style={{ position: 'absolute', opacity: xfer, display: 'flex', alignItems: 'center', gap: 18,
        ...(P ? { left: S.x, top: 300 + boxH + 26 } : { left: S.x + colW / 2 + 40, top: 230 + boxH + 40 }) }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 64 : 60, color: CLAUDE.SPARK }}>{P ? '↑' : '←'}</span>
        <Pill text={transfer} size={P ? 46 : 44} accent />
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MdParallel — Isaac Lab: many copies practicing at once; fall, reset, retry
// ===========================================================================
export const mdParallelSchema = z.object({
  title: z.string().default('Isaac Lab: copies in parallel'),
  logo: z.string().default('logos/nvidia/nvidia-01.svg'),
  envs: z.string().default('4,096 environments · one GPU'),
  rate: z.string().default('up to 1.25 M sim steps / second'),
  terrains: z.array(z.string()).default(['flat', 'slopes', 'stairs', 'rough', 'shoves']),
  shown: z.string().default('showing 40 of 4,096'),
  sparkLine: z.string().default('Fail, reset, retry.'),
  durationSeconds: z.number().optional(),
});
export const mdParallelMeta = durMeta(6);
export const MdParallel: React.FC<z.infer<typeof mdParallelSchema>> = ({ title, logo, envs, rate, terrains, shown, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const cols = P ? 5 : 10, rows = P ? 8 : 4;
  const gx = S.x, gy = P ? 360 : 230;
  const gw = S.w, gh = P ? 740 : 560;
  const cw = gw / cols, ch = gh / rows;
  const fill = ease(ramp(t, 0.04, 0.24));
  const nLive = Math.ceil(fill * cols * rows);
  const tIn = ease(ramp(t, 0.3, 0.38));
  const infoY = gy + gh + (P ? 24 : 22);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', right: W(P) - S.r, top: S.y + (P ? 168 : 34), opacity: ease(ramp(t, 0.02, 0.1)) }}>
        <Logo src={logo} h={P ? 90 : 76} />
      </div>
      {Array.from({ length: cols * rows }, (_, i) => {
        const c = i % cols, r = Math.floor(i / cols);
        const x = gx + c * cw, y = gy + r * ch;
        const terrain = (c + r * 3) % terrains.length;
        // each copy: a fall at its own time, then a reset (fade back upright), then walking again
        const tf = 0.3 + hash(i) * 0.4;
        const falls = hash(i + 99) < 0.55;
        const down = falls ? ease(ramp(t, tf, tf + 0.05)) * (1 - ramp(t, tf + 0.12, tf + 0.13)) : 0;
        const reset = falls ? ramp(t, tf + 0.13, tf + 0.18) : 1;
        const a = i < nLive ? (down > 0 || reset >= 1 || t < tf ? 1 : 0.25 + 0.75 * reset) : 0;
        const sign = hash(i + 7) < 0.5 ? -1 : 1;
        const isSlope = terrains[terrain] === 'slopes', isStairs = terrains[terrain] === 'stairs', isRough = terrains[terrain] === 'rough';
        const floorY = y + ch - 16;
        return (
          <React.Fragment key={i}>
            <div style={{ position: 'absolute', left: x + 4, top: y + 4, width: cw - 8, height: ch - 8, borderRadius: 10,
              background: CLAUDE.CARD, border: `2px solid ${down > 0.5 ? ACC_TEXT : CLAUDE.BORDER}`, boxSizing: 'border-box', opacity: i < nLive ? 1 : 0 }} />
            <svg width={cw} height={ch} style={{ position: 'absolute', left: x, top: y, opacity: i < nLive ? tIn * 0.9 + 0.1 : 0 }}>
              {isSlope && <polygon points={`8,${ch - 10} ${cw - 8},${ch - 10} ${cw - 8},${ch - 36}`} fill={CLAUDE.PILL} />}
              {isStairs && [0, 1, 2].map((k) => <rect key={k} x={cw * 0.55 + k * 16} y={ch - 18 - k * 9} width={cw * 0.45 - 8 - k * 16} height={8 + k * 9} fill={CLAUDE.PILL} />)}
              {isRough && [0, 1, 2, 3, 4].map((k) => <circle key={k} cx={14 + k * (cw - 28) / 4} cy={ch - 12} r={5} fill={CLAUDE.PILL} />)}
              <line x1={8} y1={ch - 10} x2={cw - 8} y2={ch - 10} stroke={CLAUDE.GHOST} strokeWidth={2} />
            </svg>
            {(() => {
              const dh = Math.min(ch * 0.7, (cw - 24) / 1.8);
              const dx = sign > 0 ? x + 12 + dh * 0.4 : x + cw - 12 - dh * 0.4;
              return <Duck x={dx} y={floorY} h={dh} tilt={sign * down * 88} walk={t * 50 + hash(i) * 6} a={a} />;
            })()}
          </React.Fragment>
        );
      })}
      <div style={{ position: 'absolute', left: S.x, top: infoY, width: S.w, display: 'flex', flexWrap: 'wrap', gap: P ? 14 : 18, alignItems: 'center' }}>
        <Pill text={envs} size={P ? 44 : 40} accent a={ease(ramp(t, 0.2, 0.28))} />
        <Pill text={rate} size={P ? 44 : 40} a={ease(ramp(t, 0.5, 0.58))} />
        {!P && <span style={{ fontFamily: SANS, fontSize: 32, color: CLAUDE.INK_SOFT, marginLeft: 'auto', opacity: ease(ramp(t, 0.5, 0.58)) }}>{shown}</span>}
      </div>
      <div style={{ position: 'absolute', left: S.x, top: infoY + (P ? 150 : 76), display: 'flex', gap: 12, flexWrap: 'wrap', opacity: tIn }}>
        {terrains.map((g) => <Pill key={g} text={g} size={P ? 40 : 34} fill={CLAUDE.INK_SOFT} />)}
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MdHandoff — export the walking policy; deploy it on the real duck's motors
// ===========================================================================
export const mdHandoffSchema = z.object({
  title: z.string().default('The handoff'),
  simLabel: z.string().default('simulation'),
  file: z.string().default('policy.onnx'),
  io: z.array(z.string()).default(['61 observations in', '14 joint targets out']),
  realLabel: z.string().default('the real Microduck'),
  board: z.string().default('runs onboard · 50 Hz'),
  sparkLine: z.string().default('Export, then deploy.'),
  durationSeconds: z.number().optional(),
});
export const mdHandoffMeta = durMeta(5);
export const MdHandoff: React.FC<z.infer<typeof mdHandoffSchema>> = ({ title, simLabel, file, io, realLabel, board, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  // landscape: sim box left, real box right, the file crosses the middle lane;
  // portrait: sim box on top, real box below, the file drops down the middle.
  const boxW = P ? S.w : 560, boxH = P ? 360 : 680;
  const A = P ? { x: S.x, y: 290 } : { x: S.x, y: 220 };
  const B = P ? { x: S.x, y: 290 + boxH + 270 } : { x: S.r - boxW, y: 220 };
  const fw = P ? 440 : 440, fh = P ? 220 : 230;
  const dh = P ? 230 : 440;
  const duckA = { x: A.x + (P ? 200 : boxW / 2), y: A.y + boxH - 34 };
  const duckB = { x: B.x + (P ? 200 : boxW / 2), y: B.y + boxH - 34 };
  const f0 = P ? { x: A.x + boxW - fw - 30, y: A.y + 110 } : { x: A.x + boxW / 2 - fw / 2, y: A.y + 110 };
  const f1 = P ? { x: S.x + S.w / 2 - fw / 2, y: A.y + boxH + (270 - fh) / 2 } : { x: S.x + S.w / 2 - fw / 2, y: A.y + boxH / 2 - fh / 2 };
  const f2 = { x: duckB.x - fw / 2, y: duckB.y - dh * 0.55 - fh / 2 };
  const go = ease(ramp(t, 0.3, 0.46));
  const sink = ease(ramp(t, 0.5, 0.6));
  const fx = sink > 0 ? lerp(f1.x, f2.x, sink) : lerp(f0.x, f1.x, go);
  const fy = sink > 0 ? lerp(f1.y, f2.y, sink) : lerp(f0.y, f1.y, go);
  const land = ramp(t, 0.58, 0.62);
  const walking = t > 0.64;
  const stride = walking ? (t - 0.64) * (P ? 520 : 300) : 0;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {/* simulation box with the ghost duck still walking */}
      <Card style={{ left: A.x, top: A.y, width: boxW, height: boxH, opacity: ease(ramp(t, 0.02, 0.08)) }} />
      <div style={{ position: 'absolute', left: A.x + 26, top: A.y + 22 }}><Pill text={simLabel} size={P ? 42 : 40} fill={CLAUDE.INK_SOFT} /></div>
      <Duck x={duckA.x} y={duckA.y} h={P ? 250 : 360} ghost walk={t * 40} />
      {/* the real robot */}
      <Card accent style={{ left: B.x, top: B.y, width: boxW, height: boxH, opacity: ease(ramp(t, 0.06, 0.12)) }} />
      <div style={{ position: 'absolute', left: B.x + 26, top: B.y + 22 }}><Pill text={realLabel} size={P ? 42 : 40} /></div>
      <div style={{ position: 'absolute', left: B.x + 30, top: duckB.y, width: boxW - 60, height: 5, background: CLAUDE.INK_SOFT }} />
      <Duck x={duckB.x + stride} y={duckB.y} h={dh} walk={walking ? (t - 0.64) * 80 : undefined} joints={land >= 1 ? 15 : 0} />
      <div style={{ position: 'absolute', opacity: ease(ramp(t, 0.64, 0.7)), ...(P
        ? { left: B.x + boxW - 26, top: B.y + 22, transform: 'translateX(-100%)' }
        : { left: B.x + 26, top: B.y + 96 }) }}>
        <Pill text={board} size={P ? 42 : 40} accent />
      </div>
      {/* the lane the file travels */}
      {!P && <div style={{ position: 'absolute', left: A.x + boxW + 20, top: A.y + boxH / 2 - 3, width: B.x - A.x - boxW - 40, height: 6, background: CLAUDE.GHOST, opacity: ease(ramp(t, 0.2, 0.26)) }} />}
      {P && <div style={{ position: 'absolute', left: S.x + S.w / 2 - 3, top: A.y + boxH + 14, width: 6, height: 242, background: CLAUDE.GHOST, opacity: ease(ramp(t, 0.2, 0.26)) }} />}
      {/* the exported policy file: leaves the sim, crosses, sinks into the robot */}
      <div style={{ position: 'absolute', left: fx, top: fy, width: fw, height: fh, borderRadius: 16, background: CLAUDE.INK, boxSizing: 'border-box',
        padding: '22px 28px', opacity: ease(ramp(t, 0.1, 0.18)) * (1 - land), transform: `scale(${1 - 0.7 * sink})`, transformOrigin: '50% 50%' }}>
        <div style={{ fontFamily: MONO, fontSize: P ? 46 : 46, color: CLAUDE.PAGE, marginBottom: 14 }}>{file}</div>
        {io.map((l) => <div key={l} style={{ fontFamily: SANS, fontSize: P ? 38 : 38, color: '#CFCBBE', lineHeight: 1.3 }}>{l}</div>)}
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MdWhySim — the toy run: thousands of falls, every one reset at zero hardware cost
// ===========================================================================
// evidence/sim_to_real_toy.out.txt — "falls by generation"
const TOY_FALLS = [2925, 2265, 1606, 1177, 846, 605, 454, 336, 262, 212, 150, 151, 116, 113, 114, 112, 101, 95, 81, 91, 94, 85, 83, 78, 96, 85, 83, 88, 65, 80];
export const mdWhySimSchema = z.object({
  title: z.string().default('Why simulation first'),
  falls: z.array(z.number()).default(TOY_FALLS),
  fallsLabel: z.string().default('falls while learning'),
  axis: z.string().default('falls per round, 30 rounds'),
  realHead: z.string().default('on a real robot'),
  realNote: z.string().default('each fall risks a servo'),
  simHead: z.string().default('in simulation'),
  simCost: z.string().default('$0'),
  simNote: z.string().default('hardware cost: every fall is a reset'),
  toyNote: z.string().default('toy run: 4,096 simulated balancers (evidence/sim_to_real_toy.py)'),
  sparkLine: z.string().default('A fall costs nothing.'),
  durationSeconds: z.number().optional(),
});
export const mdWhySimMeta = durMeta(5);
export const MdWhySim: React.FC<z.infer<typeof mdWhySimSchema>> = ({ title, falls, fallsLabel, axis, realHead, realNote, simHead, simCost, simNote, toyNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const grow = ease(ramp(t, 0.06, 0.5));
  const shownBars = grow * falls.length;
  const total = falls.reduce((a, f, i) => a + f * Math.max(0, Math.min(1, shownBars - i)), 0);
  const max = Math.max(...falls);
  const chart = P ? { x: S.x, y: 470, w: S.w, h: 360 } : { x: S.x, y: 340, w: 1000, h: 420 };
  const bw = chart.w / falls.length;
  const side = P ? { x: S.x, y: 900, w: S.w } : { x: S.x + 1080, y: 230, w: S.w - 1080 };
  const sideIn = (k: number) => ease(ramp(t, 0.5 + k * 0.12, 0.58 + k * 0.12));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: chart.x, top: P ? 290 : 210, display: 'flex', alignItems: 'baseline', gap: 20, flexWrap: 'wrap', width: chart.w }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 120 : 110, lineHeight: 1, color: ACC_TEXT }}>{Math.round(total).toLocaleString('en-US')}</span>
        <span style={{ fontFamily: SANS, fontSize: P ? 48 : 44, color: CLAUDE.INK }}>{fallsLabel}</span>
      </div>
      {falls.map((f, i) => {
        const p = Math.max(0, Math.min(1, shownBars - i));
        const h = (f / max) * chart.h * p;
        return <div key={i} style={{ position: 'absolute', left: chart.x + i * bw + 3, top: chart.y + chart.h - h, width: bw - 6, height: h, borderRadius: 4, background: i === 0 ? CLAUDE.SPARK : CLAUDE.INK_SOFT }} />;
      })}
      <div style={{ position: 'absolute', left: chart.x, top: chart.y + chart.h, width: chart.w, height: 4, background: CLAUDE.INK }} />
      <div style={{ position: 'absolute', left: chart.x, top: chart.y + chart.h + 14, fontFamily: SANS, fontSize: P ? 40 : 36, color: CLAUDE.INK_SOFT, opacity: ease(ramp(t, 0.1, 0.16)) }}>{axis}</div>
      {/* the two costs */}
      <div style={{ position: 'absolute', left: side.x, top: side.y, width: side.w, display: 'flex', flexDirection: P ? 'row' : 'column', gap: P ? 24 : 30 }}>
        <Card style={{ position: 'relative', flex: 1, padding: P ? '24px 26px' : '28px 34px', opacity: sideIn(0) }}>
          <div style={{ fontFamily: SERIF, fontSize: P ? 52 : 54, color: CLAUDE.INK }}>{realHead}</div>
          <div style={{ marginTop: 14 }}><Pill text={realNote} size={P ? 36 : 38} fill={CLAUDE.INK_SOFT} style={{ whiteSpace: 'normal' }} /></div>
        </Card>
        <Card accent style={{ position: 'relative', flex: 1, padding: P ? '24px 26px' : '28px 34px', opacity: sideIn(1) }}>
          <div style={{ fontFamily: SERIF, fontSize: P ? 52 : 54, color: CLAUDE.INK }}>{simHead}</div>
          <div style={{ fontFamily: SERIF, fontSize: P ? 100 : 100, lineHeight: 1.05, color: ACC_TEXT }}>{simCost}</div>
          <div style={{ fontFamily: SANS, fontSize: P ? 36 : 36, lineHeight: 1.2, color: CLAUDE.INK }}>{simNote}</div>
        </Card>
      </div>
      <div style={{ position: 'absolute', left: S.x, top: P ? 1250 : 850, width: P ? S.w : 1000, fontFamily: SANS, fontSize: P ? 34 : 32, lineHeight: 1.2, color: CLAUDE.INK_SOFT, opacity: ease(ramp(t, 0.2, 0.26)) }}>{toyNote}</div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MdStageFall — "take a nap": three of four topple; simulation ≠ the real world
// ===========================================================================
export const mdStageFallSchema = z.object({
  title: z.string().default('The honest part'),
  command: z.string().default('“Take a nap.”'),
  fell: z.number().default(3),
  count: z.string().default('3 of 4 fell over'),
  gapHead: z.string().default('typical gap sources'),
  gaps: z.array(z.string()).default(['floor friction', 'motor slack', 'timing']),
  sparkLine: z.string().default('Sim isn’t real.'),
  durationSeconds: z.number().optional(),
});
export const mdStageFallMeta = durMeta(5);
export const MdStageFall: React.FC<z.infer<typeof mdStageFallSchema>> = ({ title, command, fell, count, gapHead, gaps, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  // every faller tips LEFT about its left foot, so a lying duck spans [x − w/2 − h, x − w/2]:
  // spacing ≥ h keeps them apart, and the first sits ≥ h + w/2 from the safe edge.
  const dh = P ? 170 : 300;
  const w = dh * 0.8;
  const x0 = S.x + dh + w / 2 + 20;
  const gapX = P ? (S.r - w / 2 - 20 - x0) / 3 : 380;
  const floorY = P ? 700 : 600;
  const cIn = ease(ramp(t, 0.04, 0.1));
  const nIn = ease(ramp(t, 0.42, 0.5));
  const gIn = ease(ramp(t, 0.54, 0.62));
  const card = P ? { x: S.x, y: 900, w: S.w } : { x: S.x, y: 760, w: S.w };
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', opacity: cIn, ...(P ? { left: S.x, top: 290 } : { left: S.r - 420, top: S.y + 26 }) }}>
        <Pill text={command} size={P ? 60 : 60} />
      </div>
      <div style={{ position: 'absolute', left: S.x, top: floorY, width: S.w, height: 8, borderRadius: 4, background: CLAUDE.INK_SOFT }} />
      {[0, 1, 2, 3].map((i) => {
        const cx = x0 + i * gapX;
        const falls = i < fell;
        const at = 0.12 + i * 0.06;
        const p = falls ? ramp(t, at, at + 0.07) : 0;
        // topple with a small bounce at the end
        const tilt = falls ? -(ease(p) * 90 - Math.sin(ramp(t, at + 0.07, at + 0.11) * Math.PI) * 6) : 0;
        return <Duck key={i} x={cx} y={floorY} h={dh} tilt={tilt} walk={falls ? undefined : t * 30} />;
      })}
      <div style={{ position: 'absolute', left: S.x, top: floorY + (P ? 30 : 30), opacity: nIn }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 80 : 76, color: ACC_TEXT }}>{count}</span>
      </div>
      {/* the gap: the simulator is a model, the stage is not */}
      <Card style={{ left: card.x, top: card.y, width: card.w, opacity: gIn, padding: P ? '26px 30px' : '24px 36px',
        display: 'flex', flexDirection: P ? 'column' : 'row', alignItems: P ? 'flex-start' : 'center', gap: P ? 20 : 40 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 18 }}>
          <Pill text="sim" size={P ? 48 : 44} fill={CLAUDE.INK_SOFT} />
          <span style={{ fontFamily: SERIF, fontSize: P ? 64 : 60, color: CLAUDE.SPARK }}>≠</span>
          <Pill text="real" size={P ? 48 : 44} />
        </div>
        <span style={{ fontFamily: SERIF, fontSize: P ? 58 : 54, color: CLAUDE.INK }}>{gapHead}</span>
        <div style={{ display: 'flex', flexDirection: P ? 'column' : 'row', gap: P ? 10 : 30 }}>
          {gaps.map((g, k) => (
            <span key={g} style={{ fontFamily: SANS, fontSize: P ? 46 : 42, color: CLAUDE.INK, opacity: ease(ramp(t, 0.62 + k * 0.05, 0.68 + k * 0.05)) }}>· {g}</span>
          ))}
        </div>
      </Card>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
