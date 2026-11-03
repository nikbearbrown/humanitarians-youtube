import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { ANC, WaveStrip, PhoneBaseline, Caps } from './anc/ancKit';

/**
 * AncWaves — B01 of "How Noise-Cancelling Headphones Work."
 *
 * Destructive interference on the run's own 40 ms of engine hum at the ear (anc.py, after the filter has
 * adapted): the hum, its upside-down copy, and what is left with the anti-noise on. All three are drawn on
 * the same scale, so the residual's near-flat line is the measured result, not a drawing.
 *
 *   wave / flip / cancel / anti / hum / made / left
 */

export const ancWavesSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Add the Wave, Upside Down'),
  sparkLine: z.string().default('Noise plus anti-noise: almost nothing.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type AncWavesProps = z.infer<typeof ancWavesSchema>;

export const AncWaves: React.FC<AncWavesProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tWave = at('wave', 0.0), tFlip = at('flip', 0.15), tCancel = at('cancel', 0.3), tAnti = at('anti', 0.45);
  const tHum = at('hum', 0.58), tMade = at('made', 0.7), tLeft = at('left', 0.88);
  const headIn = sp(0);
  const s1 = sp(tWave), d1 = ramp(tWave, tWave + 0.1), s2 = sp(tFlip), d2 = ramp(tFlip, tFlip + 0.1), s3 = sp(tCancel), d3 = ramp(tMade, tMade + 0.08);
  const sAnti = sp(tAnti), sHum = sp(tHum), sMade = sp(tMade), sLeft = sp(Math.min(tLeft, 0.88));
  const sparkIn = sp(clamp(Math.min(tLeft + 0.02, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const W = ANC.waves as { hum_off: number[]; hum_on: number[]; hum_anti: number[] };
  const pk = Math.max(...W.hum_off.map(Math.abs));
  const g = 1 / pk;

  const SW = portrait ? CW : CW * 0.72, SH = portrait ? height * 0.1 : height * 0.15;
  const gap = portrait ? height * 0.025 : 20 * U;
  const row = (label: string, ys: number[], color: string, reveal: number, o: number, lo: number, tag?: string) => (
    <div style={{ opacity: o }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', width: SW, marginBottom: 8 }}>
        <Caps size={lbl} color={color === SPARK_TEXT ? SPARK_TEXT : CLAUDE.INK}>{label}</Caps>
        {tag ? <Caps size={lbl} color={SPARK_TEXT} style={{ opacity: lo }}>{tag}</Caps> : null}
      </div>
      <WaveStrip ys={ys} w={SW} h={SH} color={color} reveal={reveal} gain={g} stroke={portrait ? 5 : 4 * U} />
    </div>
  );
  const offRms = Math.sqrt(W.hum_off.reduce((a, v) => a + v * v, 0) / W.hum_off.length);
  const onRms = Math.sqrt(W.hum_on.reduce((a, v) => a + v * v, 0) / W.hum_on.length);
  const dbLeft = 20 * Math.log10(onRms / offRms);
  const rows = (
    <div style={{ display: 'flex', flexDirection: 'column', gap }}>
      {row(op(sHum) > 0.5 ? 'ENGINE HUM AT THE EAR' : 'A SOUND WAVE', W.hum_off, CLAUDE.INK, d1, op(s1), 0)}
      {row(op(sAnti) > 0.5 ? 'ANTI-NOISE' : 'THE SAME WAVE, UPSIDE DOWN', W.hum_anti, SPARK_TEXT, d2, op(s2), op(sMade), portrait ? 'MY SIMULATION' : "MY SIMULATED HEADPHONE'S")}
      {row(portrait ? 'WHAT IS LEFT' : 'ADDED TOGETHER: WHAT IS LEFT', W.hum_on, CLAUDE.INK, d3, op(s3), op(sLeft), `${dbLeft.toFixed(0)} DB`)}
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.215 }}>{rows}</div>
        <Caps size={lbl} style={{ position: 'absolute', left: PAD_X, top: height * 0.7, opacity: op(s1) }}>40 MILLISECONDS, SAME SCALE</Caps>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.25 }}>{rows}</div>
      <Caps size={lbl} style={{ position: 'absolute', left: PAD_X + SW + 30 * U, top: height * 0.27, opacity: op(s1) }}>40 MS · ONE SCALE</Caps>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
