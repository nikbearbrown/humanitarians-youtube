import React from 'react';
import { AbsoluteFill, Img } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { TMP, EX, SHOW_S, Chip, PhoneBaseline, Caps, seriesPath } from './tempo/tmpKit';

/**
 * TempoAutocorr — B03 of "How Apps Find a Song's Tempo."
 *
 * Step two, autocorrelation, on the worked example's own onset curve: the curve and a copy of it,
 * the copy sliding right. Underneath, the match score for every shift (tempo.py's 8-second
 * windowed autocorrelation, normalised so no shift = 1) draws as the copy slides. Two real peaks
 * are marked: one beat (0.51 s, the frame nearest half a second) and two beats (1.00 s), the
 * two-beat repeat matching better. The rule and both divisions are typeset (typeset_math.py).
 *
 *   two   "Step two"                      curve + copy
 *   miss  "spikes miss spikes"            copy slides off the beat
 *   land  "land on top"                   copy slides onto one beat
 *   auto  "called autocorrelation"        the rule, typeset
 *   half  "matches at half a second"      one-beat peak marked
 *   one   "even better at one second"     copy slides to two beats; peak marked
 *   div   "Sixty divided by half"         BPM rule + 60/0.5 = 120
 *   sixty "divided by one second is sixty" 60/1.0 = 60
 *   which "which one is the beat"         chip
 */

export const tempoAutocorrSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Step Two: Find the Repeat'),
  sparkLine: z.string().default('Two real repeats. One beat.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type TempoAutocorrProps = z.infer<typeof tempoAutocorrSchema>;

const LAG_MAX = 1.6;  // seconds of shift shown

export const TempoAutocorr: React.FC<TempoAutocorrProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tTwo = at('two', 0.0), tMiss = at('miss', 0.17), tLand = at('land', 0.25), tAuto = at('auto', 0.38);
  const tHalf = at('half', 0.48), tOne = at('one', 0.53), tDiv = at('div', 0.6), tSixty = at('sixty', 0.78), tWhich = at('which', 0.93);
  const headIn = sp(0);
  const P1 = TMP.peaks.oneBeat, P2 = TMP.peaks.twoBeats;
  // the copy's shift (s): off-beat, then onto one beat, then onto two beats
  const shift = 0.27 * ramp(tMiss, tMiss + 0.05) + (P1.s - 0.27) * ramp(tLand, tLand + 0.06) + (P2.s - P1.s) * ramp(tOne, tOne + 0.07);
  const sCurves = sp(tTwo), sAuto = sp(tAuto), sHalf = sp(tHalf), sOneMark = sp(tOne + 0.06), sDiv = sp(tDiv), sSixty = sp(tSixty), sWhich = sp(Math.min(tWhich - 0.05, 0.9));
  const sparkIn = sp(clamp(Math.min(tWhich, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.72 : 22 * U;

  const onset = EX.onset as number[];
  const lags = EX.ac_lags_s as number[];
  const acAll = EX.ac as number[];
  const nShow = lags.findIndex((l) => l >= LAG_MAX);
  const ac = acAll.slice(0, nShow).map((v) => clamp(v, 0, 1));
  const fpsA: number = EX.fps;
  // reveal through the frame at the current shift (inclusive), then the whole curve once the divisions arrive
  const revealAc = Math.max(clamp((Math.round(shift * fpsA) + 1.5) / ac.length, 0.03, 1), ramp(tDiv, tDiv + 0.08));
  const atShift = Math.min(ac.length - 1, Math.round(shift * fpsA));

  const SW = portrait ? CW : CW * 0.56;          // strip width = 4 s of curve
  const SH = portrait ? height * 0.05 : height * 0.085;
  const SX = PAD_X, SY = portrait ? height * 0.235 : height * 0.28;
  const pxPerS = SW / SHOW_S;
  const AW = SW, AH = portrait ? height * 0.12 : height * 0.22, AY = portrait ? height * 0.41 : height * 0.55;
  const SPAN = lags[ac.length - 1];   // the curve's own last lag, so marks and curve share one x scale
  const ax = (s: number) => (s / SPAN) * AW, ay = (v: number) => AH - v * AH;

  const strip = (dx: number, color: string, label: string, y: number, o: number) => (
    <div style={{ position: 'absolute', left: SX, top: y, width: SW, height: SH, overflow: 'hidden', opacity: o, background: CLAUDE.CARD, border: `1.5px solid ${CLAUDE.BORDER}` }}>
      <svg width={SW} height={SH} style={{ position: 'absolute', left: dx, top: 0 }}>
        <path d={seriesPath(onset, SW, SH * 0.9)} transform={`translate(0 ${SH * 0.1})`} fill="none" stroke={color} strokeWidth={portrait ? 4 : 3 * U} />
      </svg>
      <div style={{ position: 'absolute', right: 0, top: 0, background: CLAUDE.CARD, padding: portrait ? '4px 10px' : `${3 * U}px ${8 * U}px`, borderLeft: `1.5px solid ${CLAUDE.BORDER}`, borderBottom: `1.5px solid ${CLAUDE.BORDER}` }}><Caps size={lbl * 0.8} color={color}>{label}</Caps></div>
    </div>
  );
  const strips = (
    <>
      {strip(0, CLAUDE.INK, 'THE CURVE', SY, op(sCurves))}
      {strip(shift * pxPerS, SPARK_TEXT, `COPY, SHIFTED ${shift.toFixed(2)} S`, SY + SH + (portrait ? 18 : 14 * U), op(sCurves))}
    </>
  );
  const mark = (p: { s: number; v: number }, o: number, text: string) => (
    <g opacity={o}>
      <line x1={ax(p.s)} x2={ax(p.s)} y1={ay(p.v)} y2={AH} stroke={SPARK_TEXT} strokeWidth={portrait ? 3 : 2.5 * U} strokeDasharray="8 7" />
      <circle cx={ax(p.s)} cy={ay(p.v)} r={portrait ? 11 : 8 * U} fill={SPARK_TEXT} />
      <text x={ax(p.s)} y={ay(p.v) - lbl * 0.9} textAnchor="middle" fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl} fill={SPARK_TEXT}>{text}</text>
    </g>
  );
  const acPanel = (
    <svg width={AW} height={AH + lbl * 2} style={{ position: 'absolute', left: SX, top: AY, overflow: 'visible', opacity: op(sCurves) }}>
      <rect x={0} y={0} width={AW} height={AH} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
      <path d={seriesPath(ac, AW, AH, revealAc)} fill="none" stroke={CLAUDE.INK} strokeWidth={portrait ? 4 : 3 * U} />
      <circle cx={ax(lags[atShift])} cy={ay(ac[atShift])} r={portrait ? 9 : 7 * U} fill={CLAUDE.INK} opacity={shift > 0.01 ? 1 : 0} />
      {mark(P1, op(sHalf), '0.5 S')}
      {mark(P2, op(sOneMark), '1.0 S')}
      {[0, 0.5, 1.0, 1.5].map((s) => (
        <text key={s} x={ax(s)} y={AH + lbl * 1.3} textAnchor={s === 0 ? 'start' : 'middle'} fontFamily={HAI_TYPE.sans} fontWeight={700} fontSize={lbl} fill={CLAUDE.INK_SOFT}>{s.toFixed(1)} S</text>
      ))}
    </svg>
  );
  const eqImg = (e: { src: string; aspect: number }, h: number, o: number, maxW: number) => (
    <div style={{ opacity: o }}><Img src={e.src} style={{ height: h, width: Math.min(maxW, h * e.aspect), objectFit: 'contain', objectPosition: 'left' }} /></div>
  );
  const EQ = TMP.eq as Record<string, { src: string; aspect: number }>;

  if (portrait) {
    const eqH = T.title * 0.95;
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        {strips}
        <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: PAD_X, top: AY - lbl * 1.7, opacity: op(sCurves) }}>MATCH AT EACH SHIFT</Caps>
        {acPanel}
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.6, display: 'flex', flexDirection: 'column', gap: 22 }}>
          {eqImg(EQ.half, eqH, op(sDiv), CW)}
          {eqImg(EQ.one, eqH, op(sSixty), CW)}
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.735, opacity: op(sWhich) }}><Chip text="BOTH ARE REAL REPEATS" size={T.label * 0.78} accent /></div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  const RX = PAD_X + CW * 0.63, RW = CW * 0.37, eqH = 54 * U;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      {strips}
      <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: PAD_X, top: AY - lbl * 1.8, opacity: op(sCurves) }}>HOW WELL THE COPY MATCHES, AT EACH SHIFT</Caps>
      {acPanel}
      <div style={{ position: 'absolute', left: RX, top: SY, display: 'flex', flexDirection: 'column', gap: 34 * U }}>
        <div style={{ opacity: op(sAuto) }}>
          <Caps size={lbl} style={{ marginBottom: 10 * U }}>AUTOCORRELATION</Caps>
          {eqImg(EQ.rule, eqH, 1, RW)}
        </div>
        {eqImg(EQ.bpm, eqH, op(sDiv), RW)}
        {eqImg(EQ.half, eqH, op(sDiv), RW)}
        {eqImg(EQ.one, eqH, op(sSixty), RW)}
        <div style={{ opacity: op(sWhich) }}><Chip text="BOTH ARE REAL REPEATS" size={24 * U} accent /></div>
      </div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
