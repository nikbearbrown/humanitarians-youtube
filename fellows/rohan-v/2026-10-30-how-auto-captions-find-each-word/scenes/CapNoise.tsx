import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { CAP, Caps, Chip, PhoneBaseline, LandBaseline, listening } from './captions/capKit';

/**
 * CapNoise — B04 of "How Auto-Captions Find Each Word."
 *
 * captions.py's noise curve: word error rate for the same 238 words, clean and with pink noise at +20, +10, +5
 * and 0 dB SNR (how much louder the speech is than the noise). Each bar is the run's value. Ends with the run's
 * own 0 dB sentence (props.listen) and the words Whisper wrote for it under the words actually said.
 *
 *   noise / ten / five / equal / rate / listen
 */

export const capNoiseSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('How Much Noise It Takes'),
  sparkLine: z.string().default('Five decibels of headroom matters.'),
  listen: z.array(z.object({ label: z.string(), from: z.number(), to: z.number() })).optional(),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type CapNoiseProps = z.infer<typeof capNoiseSchema>;

export const CapNoise: React.FC<CapNoiseProps> = ({ eyebrow, title, sparkLine, listen, cues }) => {
  const { width, height, frame, D, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tNoise = at('noise', 0.02), tTen = at('ten', 0.12), tFive = at('five', 0.3), tEqual = at('equal', 0.42), tListen = at('listen', 0.6);
  const headIn = sp(0);
  const grow = [sp(tNoise), sp(tNoise + 0.03), sp(tTen), sp(tFive), sp(tEqual)];
  const sListen = sp(tListen);
  const now = listening(listen, frame / D);
  const heard = now ? 1 : op(sp(Math.min(tListen + 0.12, 0.9)));
  const sparkIn = sp(clamp(Math.min(tListen + 0.04, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const curve = (CAP.curve as { snr: number | null; wer: number }[]).filter((c) => c.snr === null || c.snr >= 0);
  const name = (snr: number | null) => (snr === null ? 'CLEAN' : `${snr} dB`);

  const BW = portrait ? CW : CW * 0.55, BH = portrait ? height * 0.1 : height * 0.36;
  const MAX = 100, slot = BW / curve.length, bw = slot * 0.62;
  const valS = portrait ? T.label * 0.9 : 30 * U;
  const chart = (
    <svg width={BW} height={BH + lbl * 2.4} style={{ display: 'block', overflow: 'visible' }}>
      <line x1={0} x2={BW} y1={BH} y2={BH} stroke={CLAUDE.INK} strokeWidth={3} />
      <line x1={0} x2={BW} y1={0} y2={0} stroke={CLAUDE.GHOST} strokeWidth={2} strokeDasharray="10 8" />
      {curve.map((c, i) => {
        const g = op(grow[i]);
        const h = Math.max(4, (c.wer / MAX) * BH) * (0.15 + 0.85 * g);
        const bad = c.wer > 20;
        const x = i * slot + (slot - bw) / 2;
        return (
          <g key={i}>
            <rect x={x} y={BH - h} width={bw} height={h} fill={bad ? SPARK_TEXT : CLAUDE.INK} opacity={0.3 + 0.7 * g} />
            <text x={x + bw / 2} y={BH - h - valS * 0.4} textAnchor="middle" fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={valS}
              fill={bad ? SPARK_TEXT : CLAUDE.INK} opacity={g}>{`${Math.round(c.wer)}%`}</text>
            <text x={x + bw / 2} y={BH + lbl * 1.5} textAnchor="middle" fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl} fill={CLAUDE.INK}>{name(c.snr)}</text>
          </g>
        );
      })}
    </svg>
  );
  const axis = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 8 : 8 * U }}>
      <Caps size={lbl} color={CLAUDE.INK}>{portrait ? 'ERROR RATE, dB OVER NOISE' : 'WORD ERROR RATE, SAME 238 WORDS'}</Caps>
      {portrait ? null : <Caps size={lbl}>dB: HOW MUCH LOUDER THE SPEECH IS THAN THE NOISE</Caps>}
    </div>
  );
  const S = CAP.sent1_0db;
  const lineS = portrait ? T.body * 1.0 : 44 * U;
  const playChip = <div style={{ opacity: now ? 1 : 0.3 }}><Chip text={now && !portrait ? `▶ ${now.label}` : now ? '▶ NOW PLAYING' : '▶ LISTEN'} size={portrait ? T.label * 0.8 : 24 * U} accent /></div>;
  const said = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 10 : 10 * U, opacity: 0.3 + 0.7 * op(sListen), maxWidth: portrait ? CW : CW * 0.38 }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: portrait ? 24 : 24 * U }}><Caps size={lbl} color={CLAUDE.INK}>SAID</Caps>{playChip}</div>
      <div style={{ fontFamily: HAI_TYPE.serif, fontSize: lineS, color: CLAUDE.INK, lineHeight: portrait ? 1.12 : 1.25 }}>{S.ref}</div>
      <Caps size={lbl} color={SPARK_TEXT} style={{ marginTop: portrait ? 10 : 12 * U }}>WHISPER WROTE</Caps>
      <div style={{ fontFamily: HAI_TYPE.serif, fontSize: lineS, color: SPARK_TEXT, lineHeight: portrait ? 1.12 : 1.25, opacity: 0.3 + 0.7 * heard }}>{S.hyp}</div>
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.195 }}>{axis}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.25 }}>{chart}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.402 }}>{said}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.25 }}>{axis}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.36 }}>{chart}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.62, top: height * 0.3 }}>{said}</div>
      <LandBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
