import React from 'react';
import { AbsoluteFill, Easing, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import {
  useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPRING_SNAP, SPARK_TEXT, PHONE,
} from '../lib/cueKit';
import { PITCH, Chip } from './pitch/pitchKit';

/**
 * PitchFindPeriod — B02 of "How Pitch Correction Works."
 *
 * How the detector finds the pitch, on the REAL frame it measured (pitch_demo.py,
 * the A4 note sung 40 cents flat, t = 2.56 s). Top: the recorded wave in ink and a
 * copy of it in spark, sliding right one sample at a time. Bottom: the YIN
 * difference between the two at every shift, drawn as the copy moves — it falls
 * almost to zero when the copy has moved exactly one cycle (51.27 samples), and
 * again at every whole number of cycles after that. The shift at the first dip is
 * the period; 1 / period is the pitch. Every value is the run's own.
 *
 *   slides  "slides a copy of the sound"   copy starts moving, curve draws
 *   lineup  "the two line up"              copy lands at one period
 *   zero    "drops almost to zero"         the dip is circled · more dips appear
 *   period  "That shift is one period"     bracket: 51.3 samples = 2.33 ms
 *   hz      "…four hundred and thirty hertz" 1 / 2.33 ms = 430 Hz
 *   first   "The first Auto-Tune"          the method chip
 *
 * Portrait: the two plots stacked full width, the readout beneath.
 */

export const pitchFindPeriodSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Slide the Sound Along Itself'),
  methodLabel: z.string().default('AUTOCORRELATION · the idea behind the first Auto-Tune (1997)'),
  sparkLine: z.string().default('Where the copy lines up, you have one period.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type PitchFindPeriodProps = z.infer<typeof pitchFindPeriodSchema>;

const SHOW = 300;      // samples of the frame shown (≈ 13.6 ms, almost six cycles)
const TAU_MAX = 200;   // shifts plotted on the difference curve

export const PitchFindPeriod: React.FC<PitchFindPeriodProps> = ({ eyebrow, title, methodLabel, sparkLine, cues }) => {
  const { frame, width, height, at, sp, F } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);
  const W = PITCH.worked;
  const P = W.period_samples;

  const tSl = at('slides', 0.07), tLu = at('lineup', 0.32), tZe = at('zero', 0.42);
  const tPe = at('period', 0.51), tHz = at('hz', 0.72), tFi = at('first', 0.77);

  const headIn = sp(0);
  const sPlots = sp(Math.max(0, tSl - 0.04));
  const tau = interpolate(frame, [F(tSl), F(tLu)], [0, P], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.inOut(Easing.cubic),
  });
  const extend = interpolate(frame, [F(tZe), F(tPe)], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const drawnTau = Math.max(tau, P + (TAU_MAX - P) * extend);
  const sDip = sp(tZe, SPRING_SNAP);
  const sPer = sp(tPe);
  const sHz = sp(tHz, SPRING_SNAP);
  const sFirst = sp(tFi);
  const sparkIn = sp(clamp(tFi + 0.05, 0, 0.97));

  // ── geometry ──
  const PLOT_W = portrait ? CW : CW * 0.66;
  const WAVE_Y = portrait ? height * 0.235 : height * 0.27;
  const WAVE_H = portrait ? height * 0.14 : height * 0.22;
  const DIFF_Y = portrait ? WAVE_Y + WAVE_H + height * 0.085 : WAVE_Y + WAVE_H + height * 0.115;
  const DIFF_H = portrait ? height * 0.12 : height * 0.17;
  const label = portrait ? T.label : 22 * U;

  const xs = PLOT_W / SHOW;
  const wavePath = (offset: number) => {
    let d = '';
    for (let i = 0; i < SHOW; i++) {
      const x = (i + offset) * xs;
      if (x > PLOT_W) break;
      const y = WAVE_H / 2 - W.wave[i] * WAVE_H * 0.4;
      d += `${i === 0 ? 'M' : 'L'} ${x.toFixed(1)} ${y.toFixed(1)} `;
    }
    return d;
  };
  const dx = PLOT_W / TAU_MAX;
  const yMax = 1.4;
  const diffY = (v: number) => DIFF_H - clamp(v / yMax, 0, 1) * DIFF_H;
  let diffD = '';
  for (let k = 0; k <= Math.min(TAU_MAX, Math.floor(drawnTau)); k++) {
    diffD += `${k === 0 ? 'M' : 'L'} ${(k * dx).toFixed(1)} ${diffY(W.cmnd[k]).toFixed(1)} `;
  }
  const tauI = Math.floor(tau), tauF = tau - tauI;
  const curVal = W.cmnd[tauI] * (1 - tauF) + (W.cmnd[Math.min(tauI + 1, W.cmnd.length - 1)] ?? 0) * tauF;
  const dipVal = W.cmnd[Math.round(P)];

  const readout = (k: string, v: string, accent = false, o = 1) => (
    <div style={{ opacity: o, marginBottom: portrait ? T.label * 0.5 : 26 * U }}>
      <div style={{ fontFamily: HAI_TYPE.sans, fontSize: label, fontWeight: 700, letterSpacing: 1.2, color: CLAUDE.INK_SOFT }}>{k}</div>
      <div style={{ fontFamily: HAI_TYPE.mono, fontSize: portrait ? T.data * 1.05 : 40 * U, fontWeight: 700,
        color: accent ? SPARK_TEXT : CLAUDE.INK, lineHeight: 1.15 }}>{v}</div>
    </div>
  );

  /* ── PORTRAIT (phone): wave, difference curve and readout stacked down y 21–78%. ── */
  if (portrait) {
    const L = T.label * 0.85;
    const wY = height * 0.255, wH = height * 0.105;
    const dY = height * 0.465, dH = height * 0.09;
    const pxs = CW / SHOW, pdx = CW / TAU_MAX;
    const pWave = (offset: number) => {
      let d = '';
      for (let i = 0; i < SHOW; i++) {
        const x = (i + offset) * pxs;
        if (x > CW) break;
        d += `${i === 0 ? 'M' : 'L'} ${x.toFixed(1)} ${(wH / 2 - W.wave[i] * wH * 0.4).toFixed(1)} `;
      }
      return d;
    };
    const pY = (v: number) => dH - clamp(v / yMax, 0, 1) * dH;
    let pd = '';
    for (let k = 0; k <= Math.min(TAU_MAX, Math.floor(drawnTau)); k++) pd += `${k === 0 ? 'M' : 'L'} ${(k * pdx).toFixed(1)} ${pY(W.cmnd[k]).toFixed(1)} `;
    const lab = (text: string, top: number, o = op(sPlots), color: string = CLAUDE.INK_SOFT) => (
      <div style={{ position: 'absolute', left: PAD_X, top, opacity: o, fontFamily: HAI_TYPE.sans, fontSize: L,
        fontWeight: 700, letterSpacing: 1, color }}>{text}</div>
    );
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title}
          padX={PAD_X} height={height} width={width} portrait />
        {lab('SOUND + SLIDING COPY', height * 0.215)}
        <svg width={CW} height={wH} style={{ position: 'absolute', left: PAD_X, top: wY, overflow: 'visible', opacity: op(sPlots) }}>
          <rect x={0} y={0} width={CW} height={wH} rx={14} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} />
          <path d={pWave(0)} fill="none" stroke={CLAUDE.INK} strokeWidth={4} />
          <path d={pWave(tau)} fill="none" stroke={SPARK_TEXT} strokeWidth={4} opacity={0.85} />
          <path d={`M 2 ${wH + 12} v 12 H ${P * pxs} v -12`} fill="none" stroke={SPARK_TEXT} strokeWidth={4} opacity={op(sPer)} />
        </svg>
        {lab(`1 PERIOD = ${W.periodMs.toFixed(2)} ms`, wY + wH + 34, op(sPer), SPARK_TEXT)}
        {lab('DIFFERENCE', height * 0.428)}
        <svg width={CW} height={dH} style={{ position: 'absolute', left: PAD_X, top: dY, overflow: 'visible', opacity: op(sPlots) }}>
          <rect x={0} y={0} width={CW} height={dH} rx={14} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} />
          <path d={pd} fill="none" stroke={CLAUDE.INK} strokeWidth={4} />
          <circle cx={tau * pdx} cy={pY(curVal)} r={11} fill={SPARK_TEXT} />
          <circle cx={P * pdx} cy={pY(dipVal)} r={26 + 8 * (1 - op(sDip))} fill="none" stroke={SPARK_TEXT} strokeWidth={5} opacity={op(sDip)} />
        </svg>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.57, width: CW, display: 'flex', gap: 60, opacity: op(sPlots) }}>
          {readout('SHIFT', `${tau.toFixed(1)}`)}
          {readout('DIFFERENCE', curVal.toFixed(2), op(sDip) > 0.5)}
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.665, width: CW, display: 'flex', alignItems: 'center',
          justifyContent: 'space-between', opacity: op(sHz) }}>
          <div>
            <div style={{ fontFamily: HAI_TYPE.serif, fontSize: T.title * 1.15, fontWeight: 700, color: CLAUDE.INK, lineHeight: 1 }}>{W.hz.toFixed(0)} Hz</div>
            <div style={{ fontFamily: HAI_TYPE.mono, fontSize: L, color: CLAUDE.INK_SOFT, marginTop: 8 }}>1 ÷ {W.periodMs.toFixed(2)} ms</div>
          </div>
          <div style={{ opacity: op(sFirst) }}><Chip text="AUTOCORRELATION" size={L * 0.9} accent /></div>
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

      {/* ── the wave and its sliding copy ── */}
      <div style={{ position: 'absolute', left: PAD_X, top: WAVE_Y - label * 1.6, opacity: op(sPlots),
        fontFamily: HAI_TYPE.sans, fontSize: label, fontWeight: 700, letterSpacing: 1.2, color: CLAUDE.INK_SOFT }}>
        {portrait ? 'THE SOUND + A SLIDING COPY' : 'THE MEASURED SOUND (ink) AND A SLIDING COPY (spark)'}
      </div>
      <svg width={PLOT_W} height={WAVE_H} style={{ position: 'absolute', left: PAD_X, top: WAVE_Y, overflow: 'visible', opacity: op(sPlots) }}>
        <rect x={0} y={0} width={PLOT_W} height={WAVE_H} rx={12 * U} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} />
        <path d={wavePath(0)} fill="none" stroke={CLAUDE.INK} strokeWidth={3.5 * U} />
        <path d={wavePath(tau)} fill="none" stroke={CLAUDE.SPARK} strokeWidth={3.5 * U} opacity={0.85} />
        {/* one-period bracket */}
        <g opacity={op(sPer)}>
          <path d={`M 2 ${WAVE_H + 12 * U} v ${12 * U} H ${P * xs} v ${-12 * U}`} fill="none" stroke={SPARK_TEXT} strokeWidth={3} />
        </g>
      </svg>
      <div style={{ position: 'absolute', left: PAD_X, top: WAVE_Y + WAVE_H + 30 * U, opacity: op(sPer),
        fontFamily: HAI_TYPE.sans, fontSize: label, fontWeight: 800, color: SPARK_TEXT }}>
        ONE PERIOD = {P.toFixed(1)} SAMPLES = {W.periodMs.toFixed(2)} ms
      </div>

      {/* ── the difference at every shift ── */}
      <div style={{ position: 'absolute', left: PAD_X, top: DIFF_Y - label * 0.4 - (portrait ? 0 : 6 * U), opacity: op(sPlots),
        transform: `translateY(${-label * 1.2}px)`,
        fontFamily: HAI_TYPE.sans, fontSize: label, fontWeight: 700, letterSpacing: 1.2, color: CLAUDE.INK_SOFT }}>
        {portrait ? 'DIFFERENCE AT EACH SHIFT' : 'DIFFERENCE BETWEEN THEM, AT EACH SHIFT'}
      </div>
      <svg width={PLOT_W} height={DIFF_H} style={{ position: 'absolute', left: PAD_X, top: DIFF_Y + label * 0.6, overflow: 'visible', opacity: op(sPlots) }}>
        <rect x={0} y={0} width={PLOT_W} height={DIFF_H} rx={12 * U} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} />
        <line x1={0} x2={PLOT_W} y1={diffY(0)} y2={diffY(0)} stroke={CLAUDE.BORDER} strokeWidth={2} />
        <path d={diffD} fill="none" stroke={CLAUDE.INK} strokeWidth={3.5 * U} />
        <circle cx={tau * dx} cy={diffY(curVal)} r={9 * U} fill={CLAUDE.SPARK} />
        <circle cx={P * dx} cy={diffY(dipVal)} r={(22 + 8 * (1 - op(sDip))) * U} fill="none"
          stroke={SPARK_TEXT} strokeWidth={4} opacity={op(sDip)} />
      </svg>

      {/* ── readout ── */}
      <div style={{
        position: 'absolute',
        left: portrait ? PAD_X : PAD_X + PLOT_W + CW * 0.045,
        top: portrait ? DIFF_Y + DIFF_H + label * 2.2 : WAVE_Y,
        width: portrait ? CW : CW * 0.29, opacity: op(sPlots),
        display: portrait ? 'flex' : 'block', gap: portrait ? 40 * U : 0, flexWrap: 'wrap',
      }}>
        {readout('SHIFT', `${tau.toFixed(1)} samples`)}
        {readout('DIFFERENCE', curVal.toFixed(2), op(sDip) > 0.5)}
        <div style={{ opacity: op(sHz), transform: `scale(${0.9 + 0.1 * op(sHz)})`, transformOrigin: 'left top', flexBasis: '100%' }}>
          <div style={{ fontFamily: HAI_TYPE.sans, fontSize: label, fontWeight: 700, letterSpacing: 1.2, color: CLAUDE.INK_SOFT }}>PITCH</div>
          <div style={{ fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.title * 1.1 : 68 * U, fontWeight: 700, color: CLAUDE.INK, lineHeight: 1.05 }}>
            {W.hz.toFixed(0)} Hz
          </div>
          <div style={{ fontFamily: HAI_TYPE.mono, fontSize: portrait ? T.label : 24 * U, color: CLAUDE.INK_SOFT, marginTop: 6 * U }}>
            1 ÷ {W.periodMs.toFixed(2)} ms
          </div>
        </div>
      </div>
      {!portrait ? (
        <div style={{ position: 'absolute', left: PAD_X + PLOT_W + CW * 0.045, top: DIFF_Y + DIFF_H - 20 * U,
          width: CW * 0.29, opacity: op(sFirst) }}>
          <Chip text="MEASURED" size={20 * U} accent />
          <div style={{ fontFamily: HAI_TYPE.serif, fontSize: 24 * U, color: CLAUDE.INK, marginTop: 10 * U, lineHeight: 1.35 }}>
            {methodLabel}
          </div>
        </div>
      ) : (
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.73, opacity: op(sFirst) }}>
          <Chip text="AUTOCORRELATION" size={T.label} accent />
        </div>
      )}

      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height}
        portrait={portrait} top={portrait ? height * 0.8 : undefined} fontSize={portrait ? T.spark : undefined} />
    </AbsoluteFill>
  );
};
