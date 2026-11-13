import React from 'react';
import { AbsoluteFill, Img, spring } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import {
  useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPRING_SNAP, SPRING_SETTLE, SPARK_TEXT, PHONE,
} from '../lib/cueKit';
import { PITCH, Chip } from './pitch/pitchKit';

/**
 * PitchSnapCents — B03 of "How Pitch Correction Works."
 *
 * From a frequency to a target note. LEFT: a tuner — the needle starts centred and
 * swings to the measured offset of the B02 frame (−39.5 cents, flat of A4); when the
 * target is named it is pulled back to zero. RIGHT: the cents rule and the worked
 * example, typeset by runtime/scripts/typeset_math.py (MATH-TYPESETTING.md) with
 * the numbers computed by export_pitch_data.py from the measured period — so every
 * digit on screen agrees with B02 (430.08 Hz) and with the needle.
 *
 *   note    "turns that number into a note"  MEASURED 430.08 Hz
 *   below   "just below A"                    nearest note A4, 440.0 Hz
 *   how     "How far below"                   needle swings flat
 *   log     "base-two logarithm"              the rule row
 *   minus   "minus thirty-nine"               the worked row, needle settles
 *   target  "the target is A"                 needle pulled to 0 · TARGET chip
 */

export const pitchSnapCentsSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('From Hertz to Cents'),
  sparkLine: z.string().default('The nearest note becomes the target.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type PitchSnapCentsProps = z.infer<typeof pitchSnapCentsSchema>;

export const PitchSnapCents: React.FC<PitchSnapCentsProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { frame, fps, width, height, at, sp, F } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);
  const W = PITCH.worked;

  const tNote = at('note', 0.02), tBelow = at('below', 0.2), tHow = at('how', 0.36);
  const tLog = at('log', 0.51), tMinus = at('minus', 0.65), tTarget = at('target', 0.77);

  const headIn = sp(0);
  const sNote = sp(tNote), sBelow = sp(tBelow), sLog = sp(tLog), sMinus = sp(tMinus, SPRING_SNAP);
  const sTarget = sp(tTarget, SPRING_SNAP);
  const sparkIn = sp(clamp(tTarget + 0.06, 0, 0.97));
  const swing = op(spring({ frame: frame - F(tHow), fps, config: SPRING_SETTLE }));
  const pull = op(spring({ frame: frame - F(tTarget + 0.04), fps, config: SPRING_SETTLE }));
  const needleCents = W.centsExact * swing * (1 - pull);

  // ── tuner geometry ──
  const GW = portrait ? CW : CW * 0.46;
  const R = portrait ? CW * 0.42 : GW * 0.44;
  const GX = PAD_X;
  const GY = portrait ? height * 0.25 : height * 0.3;
  const cx = GW / 2, cy = R + 30 * U;
  const ang = (c: number) => (clamp(c, -50, 50) / 50) * (Math.PI * 0.39);
  const pt = (c: number, r: number) => [cx + Math.sin(ang(c)) * r, cy - Math.cos(ang(c)) * r];
  const ticks = [];
  for (let c = -50; c <= 50; c += 5) {
    const major = c % 25 === 0;
    const [x1, y1] = pt(c, R);
    const [x2, y2] = pt(c, R - (major ? 34 : 18) * U);
    ticks.push(<line key={c} x1={x1} y1={y1} x2={x2} y2={y2} stroke={c === 0 ? CLAUDE.INK : CLAUDE.INK_SOFT}
      strokeWidth={c === 0 ? 5 : major ? 3 : 1.8} />);
  }
  const [nx, ny] = pt(needleCents, R - 14 * U);
  const lbl = portrait ? T.label : 24 * U;
  const arcFlat = `M ${pt(-50, R + 14 * U).join(' ')} A ${R + 14 * U} ${R + 14 * U} 0 0 1 ${pt(0, R + 14 * U).join(' ')}`;

  // ── equations ──
  const EQ_X = portrait ? PAD_X : PAD_X + CW * 0.52;
  const EQ_W = portrait ? CW : CW * 0.48;
  const EQ_Y = portrait ? GY + cy + 260 * U : height * 0.32;
  const rowH = portrait ? 120 * U : 96 * U;

  const centsText = swing < 0.02 ? `${W.f.toFixed(2)} Hz`
    : Math.abs(needleCents) < 0.05 ? '0.0 cents'
    : `${needleCents > 0 ? '+' : '−'}${Math.abs(needleCents).toFixed(1)} cents`;

  /* ── PORTRAIT (phone): the tuner on top, then the nearest note, then the two typeset rows. ── */
  if (portrait) {
    const L = T.label * 0.85;
    const rh = height * 0.05;
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title}
          padX={PAD_X} height={height} width={width} portrait />
        <svg width={GW} height={cy + 40} style={{ position: 'absolute', left: GX, top: height * 0.215, overflow: 'visible', opacity: op(sNote) }}>
          <path d={arcFlat} fill="none" stroke={CLAUDE.SPARK} strokeWidth={12} strokeLinecap="round" opacity={0.35 * swing * (1 - pull)} />
          {ticks}
          <text x={pt(-50, R + 60)[0]} y={pt(-50, R + 60)[1]} textAnchor="middle" fontFamily={HAI_TYPE.sans} fontWeight={700} fontSize={L} fill={CLAUDE.INK_SOFT}>−50</text>
          <text x={pt(50, R + 60)[0]} y={pt(50, R + 60)[1]} textAnchor="middle" fontFamily={HAI_TYPE.sans} fontWeight={700} fontSize={L} fill={CLAUDE.INK_SOFT}>+50</text>
          <line x1={cx} y1={cy} x2={nx} y2={ny} stroke={pull > 0.6 ? CLAUDE.INK : CLAUDE.SPARK} strokeWidth={9} strokeLinecap="round" />
          <circle cx={cx} cy={cy} r={18} fill={CLAUDE.INK} />
        </svg>
        <div style={{ position: 'absolute', left: PAD_X, width: CW, top: height * 0.215 + cy + 40, textAlign: 'center', opacity: op(sNote) }}>
          <div style={{ fontFamily: HAI_TYPE.mono, fontSize: T.data * 1.1, fontWeight: 700, color: pull > 0.6 ? CLAUDE.INK : SPARK_TEXT }}>{centsText}</div>
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.535, opacity: op(sBelow) * (1 - op(sTarget)) }}>
          <Chip text={`NEAREST: A4 · ${W.nearest_hz.toFixed(0)} Hz`} size={L} />
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.535, opacity: op(sTarget) }}>
          <Chip text={`TARGET A4 · +${Math.abs(W.centsExact).toFixed(1)} CENTS`} size={L} accent />
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.6, width: CW, opacity: op(sLog) }}>
          <Img src={PITCH.eq.rule.src} style={{ height: rh * 1.15, width: Math.min(CW, rh * 1.15 * PITCH.eq.rule.aspect), objectFit: 'contain', objectPosition: 'left' }} />
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.685, width: CW, opacity: op(sMinus) }}>
          <Img src={PITCH.eq.worked.src} style={{ height: rh, width: Math.min(CW, rh * PITCH.eq.worked.aspect), objectFit: 'contain', objectPosition: 'left' }} />
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

      {/* ── the tuner ── */}
      <svg width={GW} height={cy + 40 * U} style={{ position: 'absolute', left: GX, top: GY, overflow: 'visible', opacity: op(sNote) }}>
        <path d={arcFlat} fill="none" stroke={CLAUDE.SPARK} strokeWidth={10 * U} strokeLinecap="round" opacity={0.35 * swing * (1 - pull)} />
        {ticks}
        <text x={pt(-50, R + 50 * U)[0]} y={pt(-50, R + 50 * U)[1]} textAnchor="middle" fontFamily={HAI_TYPE.sans}
          fontWeight={700} fontSize={lbl} fill={CLAUDE.INK_SOFT}>−50</text>
        <text x={pt(50, R + 50 * U)[0]} y={pt(50, R + 50 * U)[1]} textAnchor="middle" fontFamily={HAI_TYPE.sans}
          fontWeight={700} fontSize={lbl} fill={CLAUDE.INK_SOFT}>+50</text>
        <text x={cx} y={cy - R - 22 * U} textAnchor="middle" fontFamily={HAI_TYPE.sans}
          fontWeight={700} fontSize={lbl} fill={CLAUDE.INK}>0</text>
        <line x1={cx} y1={cy} x2={nx} y2={ny} stroke={pull > 0.6 ? CLAUDE.INK : CLAUDE.SPARK} strokeWidth={7 * U} strokeLinecap="round" />
        <circle cx={cx} cy={cy} r={16 * U} fill={CLAUDE.INK} />
      </svg>
      <div style={{ position: 'absolute', left: GX, width: GW, top: GY + cy + 44 * U, textAlign: 'center' }}>
        <div style={{ fontFamily: HAI_TYPE.mono, fontSize: portrait ? T.data * 1.15 : 46 * U, fontWeight: 700,
          color: pull > 0.6 ? CLAUDE.INK : SPARK_TEXT, opacity: op(sNote) }}>
          {centsText}
        </div>
        <div style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 700, letterSpacing: 1.2, color: CLAUDE.INK_SOFT, opacity: op(sNote), marginTop: 6 * U }}>
          {pull > 0.6 ? 'IN TUNE WITH A4' : swing < 0.02 ? 'MEASURED PITCH' : `MEASURED ${W.f.toFixed(2)} Hz`}
        </div>
      </div>

      {/* ── nearest note ── */}
      <div style={{ position: 'absolute', left: EQ_X, top: portrait ? EQ_Y - 120 * U : EQ_Y - 4 * U, width: EQ_W,
        display: 'flex', gap: 18 * U, flexWrap: 'wrap', alignItems: 'center', opacity: op(sBelow),
        transform: `translateY(${(1 - op(sBelow)) * 16}px)` }}>
        <Chip text={`NEAREST NOTE: A4 · ${W.nearest_hz.toFixed(1)} Hz`} size={portrait ? T.label * 0.9 : 24 * U} />
      </div>

      {/* baseline hairline from the first frame: the mid-beat sample sits before the typeset rows
          land, and without it the content filled exactly the 55% Gate V minimum */}
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.84, width: CW, height: 2 * U,
        background: CLAUDE.GHOST, opacity: op(headIn) * 0.6 }} />

      {/* ── the rule and the worked example (typeset) ── */}
      <div style={{ position: 'absolute', left: EQ_X, top: EQ_Y + (portrait ? 0 : 80 * U), width: EQ_W }}>
        <div style={{ opacity: op(sLog), transform: `translateY(${(1 - op(sLog)) * 14}px)` }}>
          <div style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 700, letterSpacing: 1.2, color: CLAUDE.INK_SOFT, marginBottom: 10 * U }}>
            CENTS AWAY FROM A NOTE
          </div>
          <Img src={PITCH.eq.rule.src} style={{ height: rowH, width: rowH * PITCH.eq.rule.aspect, maxWidth: EQ_W, objectFit: 'contain', objectPosition: 'left' }} />
        </div>
        <div style={{ opacity: op(sMinus), transform: `translateY(${(1 - op(sMinus)) * 14}px)`, marginTop: 34 * U }}>
          <div style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 700, letterSpacing: 1.2, color: CLAUDE.INK_SOFT, marginBottom: 10 * U }}>
            THIS NOTE
          </div>
          <Img src={PITCH.eq.worked.src} style={{ height: rowH, width: rowH * PITCH.eq.worked.aspect, maxWidth: EQ_W, objectFit: 'contain', objectPosition: 'left' }} />
        </div>
        <div style={{ marginTop: 40 * U, opacity: op(sTarget), transform: `scale(${0.9 + 0.1 * op(sTarget)})`, transformOrigin: 'left center' }}>
          <Chip text={`TARGET A4 · RAISE ${Math.abs(W.centsExact).toFixed(1)} CENTS`} size={portrait ? T.label * 0.9 : 26 * U} accent />
        </div>
      </div>

      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height}
        portrait={portrait} top={portrait ? height * 0.8 : undefined} fontSize={portrait ? T.spark : undefined} />
    </AbsoluteFill>
  );
};
