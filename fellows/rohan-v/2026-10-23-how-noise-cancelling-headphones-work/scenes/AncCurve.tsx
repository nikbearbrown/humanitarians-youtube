import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { ANC, PhoneBaseline, Caps, Chip } from './anc/ancKit';

/**
 * AncCurve — B05 of "How Noise-Cancelling Headphones Work."
 *
 * Broadband pink noise through the simulated headphone (anc.py): ANC on vs off at the ear in every
 * one-third-octave band from 50 Hz to 8 kHz, as bars from a zero line. The marked points are the run's:
 * at least 10 dB quieter up to 315 Hz, some reduction up to 3,150 Hz, slightly louder above. The high
 * region is labelled as the ear cups' job (passive isolation, per the fact sheet), not drawn as data.
 *
 *   every / ten / little / louder / cups
 */

export const ancCurveSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Quiet Lows, Untouched Highs'),
  sparkLine: z.string().default('The cups block the highs; the chip cancels the lows.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type AncCurveProps = z.infer<typeof ancCurveSchema>;

const LO = -18, HI = 4;

export const AncCurve: React.FC<AncCurveProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tEvery = at('every', 0.0), tTen = at('ten', 0.18), tLittle = at('little', 0.38), tLouder = at('louder', 0.55), tCups = at('cups', 0.75);
  const headIn = sp(0);
  const sChart = sp(tEvery), grow = ramp(tEvery, tEvery + 0.15), sTen = sp(tTen), sLittle = sp(tLittle), sLouder = sp(tLouder), sCups = sp(Math.min(tCups, 0.88));
  const sparkIn = sp(clamp(Math.min(tCups + 0.05, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const bands = ANC.bands as { hz: number; db: number }[];

  const AW = portrait ? CW - 110 : CW * 0.68 - 90 * U, AH = portrait ? height * 0.26 : height * 0.46;
  const AX = PAD_X + (portrait ? 110 : 90 * U), AY = portrait ? height * 0.22 : height * 0.26;
  const bw = AW / bands.length;
  const y = (db: number) => ((HI - db) / (HI - LO)) * AH;
  const i10 = bands.reduce((b, x, i) => (x.db <= -10 ? i : b), -1);
  const i0 = bands.reduce((b, x, i) => (x.db < 0 ? i : b), -1);
  const fmt = (hz: number) => (hz >= 1000 ? `${(hz / 1000).toLocaleString('en-US')}K` : `${hz}`);
  const chart = (
    <svg width={AW} height={AH + lbl * 2.4} style={{ position: 'absolute', left: AX, top: AY, overflow: 'visible', opacity: op(sChart) }}>
      <rect x={0} y={0} width={AW} height={AH} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
      {/* the cups' region: where ANC no longer helps */}
      <rect x={(i0 + 1) * bw} y={0} width={AW - (i0 + 1) * bw} height={AH} fill={CLAUDE.BORDER} opacity={0.6 * op(sCups)} />
      {[0, -10].map((d) => (
        <g key={d}>
          <line x1={0} x2={AW} y1={y(d)} y2={y(d)} stroke={d === 0 ? CLAUDE.INK : CLAUDE.GHOST} strokeWidth={d === 0 ? 3 : 2} strokeDasharray={d === 0 ? undefined : '8 8'} />
          <text x={-12} y={y(d) + lbl * 0.36} textAnchor="end" fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl} fill={CLAUDE.INK_SOFT}>{d === 0 ? '0 DB' : '-10'}</text>
        </g>
      ))}
      {bands.map((b, i) => {
        const v = b.db * clamp(grow * bands.length - i, 0, 1);
        const y0 = y(0), y1 = y(v);
        const hot = (op(sTen) > 0.5 && i <= i10) ;
        return <rect key={b.hz} x={i * bw + bw * 0.14} y={Math.min(y0, y1)} width={bw * 0.72} height={Math.abs(y1 - y0)}
          fill={v > 0 ? SPARK_TEXT : hot ? CLAUDE.INK : CLAUDE.INK_SOFT} opacity={v > 0 && op(sLouder) < 0.5 ? 0.6 : 1} />;
      })}
      {bands.map((b, i) => ([50, 100, 250, 500, 1000, 2500, 8000].includes(b.hz) && (!portrait || [50, 250, 1000, 8000].includes(b.hz)) ? (
        <text key={b.hz} x={i * bw + bw / 2} y={AH + lbl * 1.35} textAnchor="middle" fontFamily={HAI_TYPE.sans} fontWeight={700} fontSize={lbl} fill={CLAUDE.INK_SOFT}>{fmt(b.hz)}</text>) : null))}
      <text x={AW} y={AH + lbl * 2.5} textAnchor="end" fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl} fill={CLAUDE.INK_SOFT}>HZ</text>
      <text x={(i0 + 1) * bw + (AW - (i0 + 1) * bw) / 2} y={y(-8)} textAnchor="middle" fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl} fill={CLAUDE.INK} opacity={op(sCups)}>CUPS</text>
    </svg>
  );
  const big = portrait ? T.title * 0.95 : 62 * U;
  const statBlock = (v: string, label: string, o: number, accent = false) => (
    <div style={{ opacity: o }}>
      <div style={{ fontFamily: HAI_TYPE.serif, fontSize: big, fontWeight: 700, color: accent ? SPARK_TEXT : CLAUDE.INK, lineHeight: 1 }}>{v}</div>
      <Caps size={Math.max(22, big * 0.34)} style={{ marginTop: big * 0.12 }}>{label}</Caps>
    </div>
  );
  const side = (dir: 'row' | 'column') => (
    <div style={{ display: 'flex', flexDirection: dir, gap: dir === 'row' ? 0 : 28 * U, justifyContent: 'space-between', width: dir === 'row' ? CW : undefined }}>
      {statBlock(`${bands[i10].hz} Hz`, portrait ? '10 DB QUIETER, UP TO' : 'AT LEAST 10 DB QUIETER, UP TO', op(sTen))}
      {statBlock(`${bands[i0].hz.toLocaleString('en-US')} Hz`, portrait ? 'SOME HELP, UP TO' : 'SOME REDUCTION, UP TO', op(sLittle))}
    </div>
  );
  const louder = <div style={{ opacity: op(sLouder) }}><Chip text={portrait ? 'ABOVE: SLIGHTLY LOUDER' : `ABOVE ${(bands[i0 + 1].hz / 1000).toFixed(0)} KHZ: SLIGHTLY LOUDER`} size={portrait ? T.label * 0.74 : 22 * U} accent /></div>;

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        {chart}
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.56 }}>{side('row')}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.7 }}>{louder}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: PAD_X, top: AY - lbl * 1.9, opacity: op(sChart) }}>PINK NOISE, ANC ON VS OFF, BY BAND</Caps>
      <Caps size={lbl} style={{ position: 'absolute', left: AX, top: AY + AH + lbl * 3.4, opacity: op(sCups) }}>SHADED: WHAT THE EAR CUPS BLOCK INSTEAD</Caps>
      {chart}
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.73, top: AY }}>{side('column')}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.73, top: AY + AH - 40 * U }}>{louder}</div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
