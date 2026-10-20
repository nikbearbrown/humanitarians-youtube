import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { TMP, Chip, PhoneBaseline, Caps, Stat } from './tempo/tmpKit';

/**
 * TempoDrift — B06 of "How Apps Find a Song's Tempo."
 *
 * A live drummer, from tempo.py: a rock groove that starts at 120 BPM and speeds up to 123.4 over
 * 30 s with a slow wobble and 8 ms of looseness. Plotted: for every true beat, how far off a beat
 * grid at the single detected tempo is (ink), and how far off the dynamic-programming beat
 * tracker's nearest beat is (terracotta), in milliseconds, with the +/-50 ms band shaded. The
 * marked points are the run's: the grid's first beat more than 50 ms off, and its largest miss.
 *
 *   drift / starts / grid / fifty / max / tracker / ellis / within
 */

export const tempoDriftSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Real Drummers Drift'),
  sparkLine: z.string().default('Follow the hits, not a fixed grid.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type TempoDriftProps = z.infer<typeof tempoDriftSchema>;

const YMAX = 160;

export const TempoDrift: React.FC<TempoDriftProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tDrift = at('drift', 0.04), tStarts = at('starts', 0.12), tGrid = at('grid', 0.3), tFifty = at('fifty', 0.4);
  const tMax = at('max', 0.47), tTracker = at('tracker', 0.55), tEllis = at('ellis', 0.75), tWithin = at('within', 0.9);
  const headIn = sp(0);
  const sPlot = sp(tDrift), sStarts = sp(tStarts), gDraw = ramp(tGrid, tGrid + 0.08), sFifty = sp(tFifty), sMax = sp(tMax);
  const kDraw = ramp(tTracker, tTracker + 0.08), sEllis = sp(tEllis), sWithin = sp(tWithin);
  const sparkIn = sp(clamp(tWithin + 0.04, 0, 0.97));
  const lbl = portrait ? T.label * 0.8 : 22 * U;

  const D = TMP.drift as any;
  const tb = D.true as number[], ge = D.grid_err_ms as number[], te = D.track_err_ms as number[];
  const span = 30;
  const PW = portrait ? CW - 120 : CW * 0.6 - 110 * U, PH = portrait ? height * 0.2 : height * 0.44;
  const PX = PAD_X + (portrait ? 120 : 110 * U), PY = portrait ? height * 0.245 : height * 0.27;
  const x = (s: number) => (s / span) * PW, y = (ms: number) => PH / 2 - (clamp(ms, -YMAX, YMAX) / YMAX) * (PH / 2);
  const line = (err: number[], reveal: number) => {
    const n = Math.max(2, Math.round(err.length * reveal));
    return 'M' + tb.slice(0, n).map((t, i) => `${x(t).toFixed(1)},${y(err[i]).toFixed(1)}`).join(' L');
  };
  const iFifty = ge.findIndex((e) => Math.abs(e) > 50);
  const iMax = ge.reduce((b, e, i) => (Math.abs(e) > Math.abs(ge[b]) ? i : b), 0);
  const dot = (i: number, o: number, label: string, row: number) => (
    <g opacity={o}>
      <line x1={x(tb[i])} x2={x(tb[i])} y1={lbl * (0.5 + 1.3 * row)} y2={y(ge[i])} stroke={CLAUDE.INK_SOFT} strokeWidth={2} strokeDasharray="6 6" />
      <circle cx={x(tb[i])} cy={y(ge[i])} r={portrait ? 12 : 9 * U} fill={CLAUDE.INK} />
      <text x={x(tb[i]) + (portrait ? 12 : 10 * U)} y={lbl * (1.2 + 1.3 * row)} fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl} fill={CLAUDE.INK}>{label}</text>
    </g>
  );
  const plot = (
    <svg width={PW} height={PH + lbl * 2.2} style={{ position: 'absolute', left: PX, top: PY, overflow: 'visible', opacity: op(sPlot) }}>
      <rect x={0} y={0} width={PW} height={PH} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
      <rect x={0} y={y(50)} width={PW} height={y(-50) - y(50)} fill={CLAUDE.BORDER} opacity={0.7} />
      <line x1={0} x2={PW} y1={y(0)} y2={y(0)} stroke={CLAUDE.GHOST} strokeWidth={2} />
      {[-150, -50, 0, 50, 150].map((ms) => (
        <text key={ms} x={-14} y={y(ms) + lbl * 0.35} textAnchor="end" fontFamily={HAI_TYPE.sans} fontWeight={700} fontSize={lbl} fill={CLAUDE.INK_SOFT}>{ms > 0 ? `+${ms}` : ms}</text>
      ))}
      {[0, 10, 20, 30].map((s) => (
        <text key={s} x={x(s)} y={PH + lbl * 1.35} textAnchor={s === 0 ? 'start' : s === 30 ? 'end' : 'middle'} fontFamily={HAI_TYPE.sans} fontWeight={700} fontSize={lbl} fill={CLAUDE.INK_SOFT}>{s} S</text>
      ))}
      <path d={line(ge, gDraw)} fill="none" stroke={CLAUDE.INK} strokeWidth={portrait ? 4 : 3 * U} opacity={gDraw > 0 ? 1 : 0} />
      <path d={line(te, kDraw)} fill="none" stroke={SPARK_TEXT} strokeWidth={portrait ? 5 : 4 * U} opacity={kDraw > 0 ? 1 : 0} />
      {dot(iFifty, op(sFifty), `${Math.round(Math.abs(ge[iFifty]))} MS OFF AT ${tb[iFifty].toFixed(1)} S`, 0)}
      {dot(iMax, op(sMax), `${Math.round(Math.abs(ge[iMax]))} MS`, 1)}
    </svg>
  );
  const yCap = <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: PAD_X, top: PY - lbl * 1.9, opacity: op(sPlot) }}>{portrait ? 'MS OFF EACH TRUE BEAT' : 'MILLISECONDS OFF EACH TRUE BEAT'}</Caps>;
  const bar = (c: string) => <span style={{ display: 'inline-block', width: portrait ? 56 : 44 * U, height: portrait ? 6 : 5 * U, background: c, marginRight: portrait ? 16 : 12 * U, verticalAlign: 'middle' }} />;
  const key = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 14 : 12 * U }}>
      <Caps size={lbl} color={CLAUDE.INK} style={{ opacity: gDraw > 0 ? 1 : 0.25 }}>{bar(CLAUDE.INK)}ONE FIXED TEMPO</Caps>
      <Caps size={lbl} color={SPARK_TEXT} style={{ opacity: kDraw > 0 ? 1 : 0.25 }}>{bar(SPARK_TEXT)}BEAT TRACKER</Caps>
    </div>
  );
  const big = portrait ? T.title * 1.0 : 70 * U;
  const stats = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? height * 0.018 : 28 * U }}>
      <Stat value={`${D.true_start} to ${D.true_end}`} label="BPM, START TO END" size={big} opacity={op(sStarts)} />
      <Stat value={`${Math.round(D.grid_max_ms)} ms`} label="FIXED GRID, WORST MISS" size={big} opacity={op(sMax)} />
      <Stat value={`${Math.round(D.track_median_ms)} ms`} label="TRACKER, HALF ITS BEATS WITHIN" size={big} opacity={op(sWithin)} accent />
    </div>
  );
  const ellis = <div style={{ opacity: op(sEllis) }}><Chip text={portrait ? 'DYNAMIC PROGRAMMING, 2007' : 'DYNAMIC PROGRAMMING · A 2007 PAPER'} size={portrait ? T.label * 0.66 : 22 * U} /></div>;

  if (portrait) {
    const pb = T.title * 0.95;
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        {yCap}
        {plot}
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.485, display: 'flex', gap: 50 }}>
          <Caps size={lbl} color={CLAUDE.INK} style={{ opacity: gDraw > 0 ? 1 : 0.25 }}>{bar(CLAUDE.INK)}FIXED</Caps>
          <Caps size={lbl} color={SPARK_TEXT} style={{ opacity: kDraw > 0 ? 1 : 0.25 }}>{bar(SPARK_TEXT)}TRACKER</Caps>
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.53 }}>
          <Stat value={`${D.true_start} to ${D.true_end}`} label="BPM, START TO END" size={pb} opacity={op(sStarts)} />
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.615, width: CW, display: 'flex', justifyContent: 'space-between' }}>
          <Stat value={`${Math.round(D.grid_max_ms)} ms`} label="FIXED, WORST" size={pb} opacity={op(sMax)} />
          <Stat value={`${Math.round(D.track_median_ms)} ms`} label="TRACKER, HALF WITHIN" size={pb} opacity={op(sWithin)} accent />
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.715 }}>{ellis}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      {yCap}
      {plot}
      <div style={{ position: 'absolute', left: PX, top: PY + PH + lbl * 3 }}>{key}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.66, top: PY }}>{stats}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.66, top: PY + PH + lbl * 3 }}>{ellis}</div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
