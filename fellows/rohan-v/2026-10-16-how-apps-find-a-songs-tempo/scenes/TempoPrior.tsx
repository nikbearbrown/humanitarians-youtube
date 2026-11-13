import React from 'react';
import { AbsoluteFill, Img, staticFile } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { TMP, EX, Chip, PhoneBaseline, Caps, Stat, prior } from './tempo/tmpKit';

/**
 * TempoPrior — B04 of "How Apps Find a Song's Tempo."
 *
 * Step three on the worked example: the example's match score at every shift, re-drawn against
 * tempo (BPM = 60 / shift, log scale, 40 to 300 BPM). Picking the highest point gives 60 BPM, the
 * two-beat repeat: half the true tempo. Then the preference (librosa's default prior: a bell on
 * log2 BPM, centred at 120, one octave wide) is drawn, and the curve multiplied by it: 120 wins.
 * The test-set counts beside it are tempo.py's: 13 of 40 right picking the strongest repeat, 20 of
 * the misses exactly half, and the five rock grooves right once the preference is on.
 *
 *   built     "I built a detector"         chart + tested-on stat
 *   forty     "forty grooves"              (stat)
 *   strongest "Picking the strongest repeat" raw pick marked at 60
 *   thirteen  "thirteen of forty"          13 / 40 stat
 *   halfmiss  "exactly half"               20 half stat
 *   pattern   "kick and snare pattern"     (raw pick label)
 *   pref      "adds a preference"          bell + weighted curve; 120 picked; librosa mark
 *   tap       "people tend to tap"         bell label
 *   rock      "five of five"               rock 5/5 chip
 */

export const tempoPriorSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Step Three: Choose the Beat'),
  sparkLine: z.string().default('A preference near 120 picks the beat.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type TempoPriorProps = z.infer<typeof tempoPriorSchema>;

const B0 = 40, B1 = 300;

export const TempoPrior: React.FC<TempoPriorProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tBuilt = at('built', 0.0), tForty = at('forty', 0.07), tStrong = at('strongest', 0.34), tThirteen = at('thirteen', 0.43);
  const tHalfMiss = at('halfmiss', 0.49), tPattern = at('pattern', 0.55), tPref = at('pref', 0.73), tTap = at('tap', 0.86), tRock = at('rock', 0.96);
  const headIn = sp(0);
  const sChart = sp(tBuilt), sForty = sp(tForty), sStrong = sp(tStrong), sThirteen = sp(tThirteen), sHalfMiss = sp(tHalfMiss);
  const sPattern = sp(tPattern), bell = ramp(tPref, tPref + 0.06), sPref = sp(tPref + 0.03), sTap = sp(tTap), sRock = sp(Math.min(tRock, 0.95));
  const sparkIn = sp(clamp(tRock + 0.01, 0, 0.98));
  const lbl = portrait ? T.label * 0.72 : 22 * U;

  // the example's match score against tempo
  const lags = EX.ac_lags_s as number[], ac = EX.ac as number[];
  const pts = lags.map((l, i) => ({ bpm: l > 0 ? 60 / l : Infinity, v: ac[i] })).filter((p) => p.bpm >= B0 && p.bpm <= B1);
  const S = TMP.summary as any;
  const rockRight = (TMP.rows as any[]).filter((r) => r.style === 'rock' && r.prior_class === 'right').length;
  const peakAt = (target: number) => pts.reduce((b, p) => (Math.abs(Math.log2(p.bpm / target)) < 0.08 && p.v > b.v ? p : b), { bpm: target, v: -1 });
  const pk60 = peakAt(60), pk120 = peakAt(120);

  const PW = portrait ? CW : CW * 0.58, PH = portrait ? height * 0.2 : height * 0.44;
  const PX = PAD_X, PY = portrait ? height * 0.235 : height * 0.27;
  const x = (b: number) => (Math.log(b / B0) / Math.log(B1 / B0)) * PW;
  const y = (v: number) => PH - clamp(v, 0, 1) * PH * 0.9;
  const path = (f: (p: { bpm: number; v: number }) => number) =>
    'M' + [...pts].sort((a, b) => a.bpm - b.bpm).map((p) => `${x(p.bpm).toFixed(1)},${y(f(p)).toFixed(1)}`).join(' L');
  const bellPath = 'M' + Array.from({ length: 80 }, (_, i) => B0 * Math.pow(B1 / B0, i / 79)).map((b) => `${x(b).toFixed(1)},${y(prior(b)).toFixed(1)}`).join(' L');
  const after = op(sPref);
  const pickMark = (p: { bpm: number; v: number }, v: number, o: number, label: string, accent: boolean) => (
    <g opacity={o}>
      <circle cx={x(p.bpm)} cy={y(v)} r={portrait ? 12 : 9 * U} fill={accent ? SPARK_TEXT : CLAUDE.INK} />
      <text x={x(p.bpm)} y={y(v) - lbl * 0.9} textAnchor="middle" fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl} fill={accent ? SPARK_TEXT : CLAUDE.INK}>{label}</text>
    </g>
  );

  const chart = (
    <svg width={PW} height={PH + lbl * 2.2} style={{ position: 'absolute', left: PX, top: PY, overflow: 'visible', opacity: op(sChart) }}>
      <rect x={0} y={0} width={PW} height={PH} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
      <path d={bellPath} fill="none" stroke={CLAUDE.GHOST} strokeWidth={portrait ? 4 : 3 * U} strokeDasharray="12 9" opacity={bell} />
      <path d={path((p) => p.v)} fill="none" stroke={CLAUDE.INK} strokeWidth={portrait ? 4 : 3 * U} opacity={1 - 0.6 * after} />
      <path d={path((p) => p.v * prior(p.bpm))} fill="none" stroke={SPARK_TEXT} strokeWidth={portrait ? 5 : 4 * U} opacity={after} />
      {pickMark(pk60, pk60.v, op(sStrong) * (1 - 0.65 * after), 'PICKED: 60', false)}
      {pickMark(pk120, pk120.v * prior(pk120.bpm), after, 'PICKED: 120', true)}
      {[60, 120, 240].map((b) => (
        <text key={b} x={x(b)} y={PH + lbl * 1.35} textAnchor="middle" fontFamily={HAI_TYPE.sans} fontWeight={700} fontSize={lbl} fill={CLAUDE.INK_SOFT}>{b}</text>
      ))}
      {portrait ? null : <text x={PW} y={PH + lbl * 1.35} textAnchor="end" fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl} fill={CLAUDE.INK_SOFT}>BPM</text>}
      <text x={x(150)} y={y(prior(150)) - lbl * 0.7} textAnchor="start" fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl} fill={CLAUDE.INK_SOFT} opacity={portrait ? 0 : op(sTap)}>NEAR WHERE PEOPLE TAP</text>
    </svg>
  );
  const big = portrait ? T.title * 1.25 : 76 * U;
  const statsCol = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? height * 0.02 : 30 * U }}>
      <Stat value="40" label="GROOVES · 8 STYLES" size={big} opacity={op(sForty)} />
      <Stat value={`${S.raw.acc1} / ${S.raw.n}`} label="RIGHT, STRONGEST REPEAT" size={big} opacity={op(sThirteen)} />
      <Stat value={`${S.raw.counts.half}`} label="MISSES THAT WERE EXACTLY HALF" size={big} opacity={op(sHalfMiss)} accent />
    </div>
  );
  const lib = (
    <div style={{ display: 'flex', alignItems: 'center', gap: portrait ? 18 : 16 * U, opacity: op(sPref) }}>
      <Img src={staticFile(TMP.logo.librosa)} style={{ height: portrait ? 260 : 230 * U, width: portrait ? 260 : 230 * U, margin: portrait ? '-80px -30px' : `${-70 * U}px ${-24 * U}px` }} />
      <Caps size={lbl} color={CLAUDE.INK}>{portrait ? 'CENTRED AT 120' : "LIBROSA'S DEFAULT: CENTRED AT 120"}</Caps>
    </div>
  );

  if (portrait) {
    const pb = T.title * 1.0;
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: PAD_X, top: PY - lbl * 1.7, opacity: op(sForty) }}>40 GROOVES · MATCH BY BPM</Caps>
        {chart}
        <Caps size={lbl} color={CLAUDE.INK_SOFT} style={{ position: 'absolute', left: PAD_X, top: PY + PH + lbl * 2.1, opacity: op(sTap) }}>BELL: NEAR WHERE PEOPLE TAP</Caps>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.51, width: CW, display: 'flex', justifyContent: 'space-between' }}>
          <Stat value={`${S.raw.acc1} / ${S.raw.n}`} label="RIGHT, STRONGEST" size={pb} opacity={op(sThirteen)} />
          <Stat value={`${S.raw.counts.half}`} label="MISSES: EXACTLY HALF" size={pb} opacity={op(sHalfMiss)} accent />
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.615 }}>{lib}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.722, opacity: op(sRock) }}><Chip text={`ROCK: ${rockRight} OF 5 RIGHT`} size={T.label * 0.78} accent /></div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: PX, top: PY - lbl * 1.8, opacity: op(sChart) }}>THE ROCK GROOVE'S MATCH, BY TEMPO</Caps>
      {chart}
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.65, top: PY }}>{statsCol}</div>
      <div style={{ position: 'absolute', left: PX, top: PY + PH + lbl * 3.2 }}>{lib}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.65, top: PY + PH + lbl * 3.2 + 30 * U, opacity: op(sRock) }}><Chip text={`ROCK GROOVES: ${rockRight} OF 5 RIGHT`} size={24 * U} accent /></div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
