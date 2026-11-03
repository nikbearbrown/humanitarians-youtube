import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import {
  useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPRING_SNAP, CountTo, SPARK_TEXT, PHONE,
} from '../lib/cueKit';
import { ToneWave, Chip } from './pitch/pitchKit';

/**
 * PitchCycles — B01 of "How Pitch Correction Works."
 *
 * What pitch IS, before any software touches it. A periodic wave is drawn and its
 * cycles are bracketed one by one as they are counted, so "repeats 440 times a
 * second" is something the viewer watches happen; a second wave at twice the rate
 * shows the octave; then a ruler between two neighbouring keys is cut into the
 * hundred steps called cents — the unit the rest of the film works in.
 * The waves are explanatory drawings, not measurements (the measured data starts in B02).
 *
 *   air     "air vibrating"                 the wave draws on
 *   faster  "faster the vibration repeats"  cycles bracketed one by one
 *   a440    "four hundred and forty times"  counter to 440 · "= 440 Hz"
 *   double  "Double that"                   the 880 Hz wave · octave label
 *   cents   "called cents"                  the A → A♯ ruler, 100 ticks
 *   works   "Pitch correction works…"       the 1 semitone = 100 cents chip
 *
 * Portrait: the same three rows stacked, larger and with less text.
 */

export const pitchCyclesSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('A Note Is a Vibration That Repeats'),
  sparkLine: z.string().default('Faster repeats, higher note. Correction works in cents.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type PitchCyclesProps = z.infer<typeof pitchCyclesSchema>;

export const PitchCycles: React.FC<PitchCyclesProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp, F } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tAir = at('air', 0.02), tFaster = at('faster', 0.15), tA = at('a440', 0.3);
  const tDouble = at('double', 0.55), tCents = at('cents', 0.75), tWorks = at('works', 0.88);

  const headIn = sp(0);
  const sWave = sp(tAir);
  const counted = ramp(tFaster, tA + 0.04);           // cycles bracketed one by one
  const sHz = sp(tA, SPRING_SNAP);
  const sOct = sp(tDouble);
  const sRuler = sp(tCents);
  const ticks = ramp(tCents, tCents + 0.08);
  const sWorks = sp(tWorks, SPRING_SNAP);
  const sparkIn = sp(clamp(tWorks + 0.03, 0, 0.97));

  const CYC = portrait ? 5 : 8;
  // geometry
  const WAVE_Y = portrait ? height * 0.24 : height * 0.29;
  const WAVE_H = portrait ? height * 0.11 : height * 0.15;
  const WAVE_W = portrait ? CW : CW * 0.66;
  const OCT_Y = portrait ? height * 0.47 : height * 0.515;
  const OCT_H = portrait ? height * 0.075 : height * 0.1;
  const RUL_Y = portrait ? height * 0.62 : height * 0.70;
  const RUL_H = portrait ? height * 0.1 : height * 0.12;

  const label = portrait ? T.label : 24 * U;
  const data = portrait ? T.data : 26 * U;
  const big = portrait ? T.title * 1.25 : 92 * U;
  const nCounted = Math.floor(counted * CYC + 0.0001);

  const cycW = WAVE_W / CYC;
  const brackets = Array.from({ length: CYC }, (_, i) => {
    const k = clamp(counted * CYC - i, 0, 1);
    return (
      <g key={i} opacity={k}>
        <path d={`M ${i * cycW + 4} ${WAVE_H + 10 * U} v ${10 * U} H ${(i + 1) * cycW - 4} v ${-10 * U}`}
          fill="none" stroke={i === nCounted - 1 ? CLAUDE.SPARK : CLAUDE.INK_SOFT} strokeWidth={3} />
      </g>
    );
  });

  const rulerTicks = Array.from({ length: 101 }, (_, i) => {
    const k = clamp(ticks * 101 - i, 0, 1);
    const major = i % 10 === 0;
    const x = (i / 100) * CW;
    return <line key={i} x1={x} x2={x} y1={RUL_H * 0.5} y2={RUL_H * 0.5 + (major ? 30 : 14) * U}
      stroke={major ? CLAUDE.INK : CLAUDE.INK_SOFT} strokeWidth={major ? 3 : 1.6} opacity={k} />;
  });

  /* ── PORTRAIT (phone): PHONE type scale, five cycles, one row per idea, filling y 21–78%. ── */
  if (portrait) {
    const L = T.label * 0.85;
    const wY = height * 0.215, wH = height * 0.11;
    const oY = height * 0.47, oH = height * 0.07;
    const rY = height * 0.665;
    const pcw = CW / 5;
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title}
          padX={PAD_X} height={height} width={width} portrait />
        <svg width={CW} height={wH + 40} style={{ position: 'absolute', left: PAD_X, top: wY, overflow: 'visible', opacity: op(sWave) }}>
          <rect x={0} y={0} width={CW} height={wH} rx={14} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} />
          {/* counted cycles as shaded bands behind the wave (light fills: thin bracket strokes
              under the wave read as sub-floor text to GATE T §8.1 on the phone frame) */}
          {Array.from({ length: 5 }, (_, i) => (
            <rect key={i} x={i * pcw + 3} y={3} width={pcw - 6} height={wH - 6} rx={10}
              fill={i === Math.min(4, Math.floor(counted * 5 + 1e-4) - 1) ? '#F6DED3' : CLAUDE.PILL}
              opacity={clamp(counted * 5 - i, 0, 1)} />
          ))}
          <path d={ToneWave(CW, wH, wH * 0.36, 5)} fill="none" stroke={CLAUDE.INK} strokeWidth={5} />
        </svg>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.345, opacity: op(sWave),
          fontFamily: HAI_TYPE.sans, fontSize: L, fontWeight: 700, letterSpacing: 1, color: CLAUDE.INK_SOFT }}>CYCLES EACH SECOND</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.38, display: 'flex', alignItems: 'center', gap: 28, opacity: op(sWave) }}>
          <div style={{ fontFamily: HAI_TYPE.serif, fontSize: T.title * 1.3, fontWeight: 700, color: CLAUDE.INK, lineHeight: 1 }}>
            {op(sHz) > 0.02 ? <CountTo to={440} fromFrame={Math.round(F(tA))} frames={24} /> : Math.min(5, Math.floor(counted * 5 + 1e-4))}
          </div>
          <div style={{ opacity: op(sHz) }}><Chip text="= 440 Hz" size={T.data} /></div>
        </div>
        <svg width={CW} height={oH} style={{ position: 'absolute', left: PAD_X, top: oY, overflow: 'visible',
          opacity: 0.3 * op(sWave) + 0.7 * op(sOct) }}>
          <rect x={0} y={0} width={CW} height={oH} rx={14} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} />
          <path d={ToneWave(CW, oH, oH * 0.34, 10)} fill="none" stroke={CLAUDE.SPARK} strokeWidth={5} opacity={op(sOct)} />
        </svg>
        <div style={{ position: 'absolute', left: PAD_X, top: oY + oH + 26, display: 'flex', alignItems: 'center', gap: 22, opacity: op(sOct) }}>
          <Chip text="880 Hz" size={L} accent />
          <span style={{ fontFamily: HAI_TYPE.serif, fontSize: T.body, color: CLAUDE.INK }}>an octave up</span>
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: rY - T.body * 1.35, width: CW, display: 'flex', justifyContent: 'space-between',
          opacity: 0.3 * op(sWave) + 0.7 * op(sRuler), fontFamily: HAI_TYPE.serif, fontSize: T.body, fontWeight: 700, color: CLAUDE.INK }}>
          <span>A</span><span>A♯</span>
        </div>
        <svg width={CW} height={60} style={{ position: 'absolute', left: PAD_X, top: rY, overflow: 'visible', opacity: 0.3 * op(sWave) + 0.7 * op(sRuler) }}>
          <line x1={0} x2={CW} y1={0} y2={0} stroke={CLAUDE.INK} strokeWidth={4} />
          {Array.from({ length: 21 }, (_, i) => (
            <line key={i} x1={(i / 20) * CW} x2={(i / 20) * CW} y1={0} y2={i % 10 === 0 ? 40 : 22}
              stroke={CLAUDE.INK} strokeWidth={i % 10 === 0 ? 4 : 2} opacity={clamp(ticks * 21 - i, 0, 1)} />
          ))}
        </svg>
        <div style={{ position: 'absolute', left: PAD_X, top: rY + 56, width: CW, textAlign: 'center', opacity: op(ticks),
          fontFamily: HAI_TYPE.sans, fontSize: L, fontWeight: 800, color: CLAUDE.INK }}>100 CENTS</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.735, opacity: op(sWorks) }}>
          <Chip text="1 OCTAVE = 1200 CENTS" size={L} accent />
        </div>
        {/* phone baseline: a hairline above the spark line from the first frame, so the content
            spans the 9:16 safe area at every Gate V sample (fill >= 55%) without adding text */}
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.782, width: CW, height: 3,
          background: CLAUDE.GHOST, opacity: op(headIn) * 0.7 }} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height}
          portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={portrait ? '' : eyebrow} title={title} inOp={headIn}
        padX={PAD_X} height={height} width={width} portrait={portrait}
        titleSize={portrait ? T.title : undefined} />

      {/* ── one tone: count its cycles ───────────────────────────── */}
      <svg width={WAVE_W} height={WAVE_H + 40 * U}
        style={{ position: 'absolute', left: PAD_X, top: WAVE_Y, overflow: 'visible', opacity: op(sWave) }}>
        <rect x={0} y={0} width={WAVE_W} height={WAVE_H} rx={12 * U} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} />
        <path d={ToneWave(WAVE_W, WAVE_H, WAVE_H * 0.36, CYC)} fill="none" stroke={CLAUDE.INK}
          strokeWidth={4 * U} strokeDasharray={WAVE_W * 3} strokeDashoffset={WAVE_W * 3 * (1 - op(sWave))} />
        {brackets}
      </svg>
      <div style={{
        position: 'absolute', left: portrait ? PAD_X : PAD_X + WAVE_W + CW * 0.04,
        top: portrait ? WAVE_Y + WAVE_H + 60 * U : WAVE_Y - 6 * U,
        width: portrait ? CW : CW * 0.3, opacity: op(sWave),
      }}>
        <div style={{ fontFamily: HAI_TYPE.sans, fontSize: label, fontWeight: 700, letterSpacing: 1.2, color: CLAUDE.INK_SOFT }}>
          CYCLES EACH SECOND
        </div>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 18 * U }}>
          <div style={{ fontFamily: HAI_TYPE.serif, fontSize: big, fontWeight: 700, color: CLAUDE.INK, lineHeight: 1.05 }}>
            {op(sHz) > 0.02 ? <CountTo to={440} fromFrame={Math.round(F(tA))} frames={24} /> : nCounted}
          </div>
          <div style={{ opacity: op(sHz), transform: `scale(${0.85 + 0.15 * op(sHz)})`, transformOrigin: 'left center' }}>
            <Chip text="= 440 Hz" size={data} />
          </div>
        </div>
        {!portrait ? (
          <div style={{ fontFamily: HAI_TYPE.serif, fontSize: 26 * U, color: CLAUDE.INK_SOFT, marginTop: 8 * U, opacity: op(sHz) }}>
            the A above middle C
          </div>
        ) : null}
      </div>

      {/* ── twice as fast: one octave up (its frame is a faint shell until spoken) ── */}
      <svg width={WAVE_W} height={OCT_H}
        style={{ position: 'absolute', left: PAD_X, top: OCT_Y, overflow: 'visible', opacity: 0.3 * op(sWave) + 0.7 * op(sOct) }}>
        <rect x={0} y={0} width={WAVE_W} height={OCT_H} rx={12 * U} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} />
        <path d={ToneWave(WAVE_W, OCT_H, OCT_H * 0.34, CYC * 2)} fill="none" stroke={CLAUDE.SPARK} strokeWidth={4 * U} opacity={op(sOct)} />
      </svg>
      <div style={{
        position: 'absolute', left: portrait ? PAD_X : PAD_X + WAVE_W + CW * 0.04,
        top: portrait ? OCT_Y + OCT_H + 24 * U : OCT_Y + OCT_H * 0.18, opacity: op(sOct),
        transform: `translateX(${(1 - op(sOct)) * 20}px)`,
      }}>
        <Chip text="880 Hz" size={data} accent />
        <span style={{ fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.body : 30 * U, color: CLAUDE.INK, marginLeft: 16 * U }}>
          one octave up
        </span>
      </div>

      {/* ── between two keys: a hundred cents ────────────────────── */}
      <div style={{ position: 'absolute', left: PAD_X, top: RUL_Y, width: CW, height: RUL_H + 60 * U, opacity: 0.3 * op(sWave) + 0.7 * op(sRuler) }}>
        <svg width={CW} height={RUL_H + 40 * U} style={{ overflow: 'visible' }}>
          <line x1={0} x2={CW} y1={RUL_H * 0.5} y2={RUL_H * 0.5} stroke={CLAUDE.INK} strokeWidth={3} />
          {rulerTicks}
        </svg>
        {[['A', 0], ['A♯', 1]].map(([n, p]) => (
          <div key={String(n)} style={{
            position: 'absolute', top: RUL_H * 0.5 - (portrait ? T.label * 2.1 : 62 * U),
            left: (p as number) === 0 ? 0 : undefined, right: (p as number) === 1 ? 0 : undefined,
            fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.body : 40 * U, fontWeight: 700, color: CLAUDE.INK,
          }}>{n}</div>
        ))}
        <div style={{
          position: 'absolute', left: 0, right: 0, top: RUL_H * 0.5 + 44 * U, textAlign: 'center',
          fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.body : 34 * U, color: CLAUDE.INK, opacity: op(ticks),
        }}>
          100 cents between neighbouring keys
        </div>
      </div>
      <div style={{
        position: 'absolute', left: PAD_X, top: portrait ? RUL_Y - T.label * 2.6 : RUL_Y - 70 * U,
        width: CW, textAlign: portrait ? 'left' : 'center', opacity: op(sWorks),
        transform: `scale(${0.9 + 0.1 * op(sWorks)})`,
      }}>
        <Chip text={portrait ? '1 OCTAVE = 1200 CENTS' : '1 SEMITONE = 100 CENTS  ·  1 OCTAVE = 1200 CENTS'} size={portrait ? T.label : 24 * U} accent />
      </div>

      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height}
        portrait={portrait} top={portrait ? height * 0.8 : undefined} fontSize={portrait ? T.spark : undefined} />
    </AbsoluteFill>
  );
};
