import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { CAP, Caps, Env, PhoneBaseline, LandBaseline } from './captions/capKit';

/**
 * CapTiming — B02 of "How Auto-Captions Find Each Word."
 *
 * Test sentence 1 (captions.py): its waveform, the true start of every word (known, because the sentence was
 * built word by word) as ink ticks above, and faster-whisper's word starts as terracotta ticks below, with each
 * word written at Whisper's start. The ticks are the run's values.
 *
 *   find / looking / order / dtw / one / really / says
 */

export const capTimingSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('When Was Each Word Said?'),
  sparkLine: z.string().default('Where it looked, lined up in order.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type CapTimingProps = z.infer<typeof capTimingSchema>;

export const CapTiming: React.FC<CapTimingProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tFind = at('find', 0.02), tLook = at('looking', 0.12), tOrder = at('order', 0.3), tDtw = at('dtw', 0.42);
  const tOne = at('one', 0.6), tReal = at('really', 0.72), tSays = at('says', 0.85);
  const headIn = sp(0);
  const sWave = sp(tFind), sDtw = sp(tDtw), trueD = ramp(tReal - 0.04, tReal + 0.06), whD = ramp(tSays - 0.03, Math.min(tSays + 0.08, 0.95));
  const sparkIn = sp(clamp(Math.min(tSays, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const ex = CAP.example as any;
  const dur: number = ex.seconds;
  const truth = ex.true as number[], ws = ex.whisper as { w: string; start: number }[];

  // the phone shows the first half of the sentence (five words) so labels fit
  const span = portrait ? truth[5] + 0.1 : dur;
  const nShow = portrait ? 5 : truth.length;
  const PW = CW, PH = portrait ? height * 0.12 : height * 0.2;
  const PY = portrait ? height * 0.3 : height * 0.36;
  const x = (s: number) => (s / span) * PW;
  const env = (ex.env as number[]).slice(0, Math.round((span / dur) * (ex.env as number[]).length));
  const tick = portrait ? 34 : 30 * U;
  const plot = (
    <svg width={PW} height={PH + 2 * tick + lbl * 4.5} style={{ position: 'absolute', left: PAD_X, top: PY - tick - lbl * 1.6, overflow: 'visible', opacity: op(sWave) }}>
      <g transform={`translate(0 ${tick + lbl * 1.6})`}>
        <rect x={0} y={0} width={PW} height={PH} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
        <Env env={env} w={PW} h={PH} />
        {truth.slice(0, nShow).map((t, i) => (
          <line key={`t${i}`} x1={x(t)} x2={x(t)} y1={-tick} y2={PH * 0.5} stroke={CLAUDE.INK} strokeWidth={portrait ? 5 : 4 * U} opacity={clamp(trueD * nShow - i, 0, 1)} />
        ))}
        {ws.slice(0, nShow).map((w, i) => {
          const o = clamp(whD * nShow - i, 0, 1);
          return (
            <g key={`w${i}`} opacity={o}>
              <line x1={x(w.start)} x2={x(w.start)} y1={PH * 0.5} y2={PH + tick} stroke={SPARK_TEXT} strokeWidth={portrait ? 5 : 4 * U} />
              <line x1={x(w.start)} x2={x(w.start)} y1={PH + tick} y2={PH + tick + (i % 2) * lbl * 1.3} stroke={SPARK_TEXT} strokeWidth={portrait ? 3 : 2 * U} />
              <text x={x(w.start) + (x(w.start) > PW * 0.8 ? -6 : 6)} y={PH + tick + lbl * 1.2 + (i % 2) * lbl * 1.3} textAnchor={x(w.start) > PW * 0.8 ? 'end' : 'start'}
                fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl} fill={SPARK_TEXT}>{w.w.replace(/[.,]$/, '').toUpperCase()}</text>
            </g>
          );
        })}
      </g>
    </svg>
  );
  const key = (
    <div style={{ display: 'flex', flexDirection: portrait ? 'column' : 'row', gap: portrait ? 12 : 40 * U }}>
      <Caps size={lbl} color={CLAUDE.INK} style={{ opacity: 0.3 + 0.7 * trueD }}>{portrait ? 'TOP: TRUE START' : 'TICKS ABOVE: WHEN EACH WORD REALLY STARTS'}</Caps>
      <Caps size={lbl} color={SPARK_TEXT} style={{ opacity: 0.3 + 0.7 * whD }}>{portrait ? 'BELOW: WHISPER' : "BELOW: WHISPER'S START"}</Caps>
    </div>
  );
  const dtw = (
    <div style={{ opacity: op(sDtw), fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.body * 1.02 : 44 * U, color: CLAUDE.INK, maxWidth: CW }}>
      {portrait ? 'Lined up by dynamic time warping' : 'Each word lined up with the sound by dynamic time warping'}
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: PAD_X, top: height * 0.2, opacity: op(sWave) }}>FIRST FIVE WORDS</Caps>
        {plot}
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.56 }}>{key}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.65 }}>{dtw}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.25 }}>{dtw}</div>
      {plot}
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.73 }}>{key}</div>
      <LandBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
