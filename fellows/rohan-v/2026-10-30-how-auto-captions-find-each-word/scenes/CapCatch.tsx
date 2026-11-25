import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { CAP, Caps, PhoneBaseline, LandBaseline } from './captions/capKit';

/**
 * CapCatch — B05 of "How Auto-Captions Find Each Word."
 *
 * Two ways the recogniser writes what wasn't said, all from runs. Loudest noise (captions.py, -5 dB SNR): words
 * said vs words written, with a stretch of the repeat loop it produced. Clean speech (the voice reel's audio
 * check, voice.py): the narrator's respelled name and a spoken price, and what Whisper wrote for each.
 *
 *   stop / never / count / repeat / expects / name / price
 */

export const capCatchSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('It Writes What It Expects'),
  sparkLine: z.string().default("Confident text isn't proof it was said."),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type CapCatchProps = z.infer<typeof capCatchSchema>;

export const CapCatch: React.FC<CapCatchProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tStop = at('stop', 0.02), tCount = at('count', 0.15), tRepeat = at('repeat', 0.3), tExp = at('expects', 0.45);
  const tName = at('name', 0.6), tPrice = at('price', 0.78);
  const headIn = sp(0);
  const sStop = sp(tStop), sCount = sp(tCount), sRep = sp(tRepeat), sExp = sp(tExp), sName = sp(tName), sPrice = sp(tPrice);
  const sparkIn = sp(clamp(Math.min(tPrice + 0.08, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const L = CAP.loudest, V = CAP.voiceCheck;

  const BW = portrait ? CW : CW * 0.5, barH = portrait ? 56 : 76 * U;
  const max = Math.max(L.hyp_words, L.ref_words);
  const bar = (n: number, label: string, accent: boolean, o: number) => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 6 : 6 * U, opacity: 0.3 + 0.7 * o }}>
      <Caps size={lbl} color={accent ? SPARK_TEXT : CLAUDE.INK}>{label}</Caps>
      <div style={{ display: 'flex', alignItems: 'center', gap: portrait ? 18 : 18 * U }}>
        <div style={{ width: (n / max) * BW * 0.78 * (0.2 + 0.8 * o), height: barH, background: accent ? SPARK_TEXT : CLAUDE.INK }} />
        <div style={{ fontFamily: HAI_TYPE.serif, fontWeight: 700, fontSize: barH * 1.05, color: accent ? SPARK_TEXT : CLAUDE.INK }}>{n}</div>
      </div>
    </div>
  );
  const repS = portrait ? T.body * 0.95 : 40 * U;
  const loud = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 16 : 26 * U, width: BW }}>
      <Caps size={lbl} color={CLAUDE.INK} style={{ opacity: 0.3 + 0.7 * op(sStop) }}>{`LOUDEST NOISE (${L.snr} dB)`}</Caps>
      {bar(L.ref_words, 'WORDS SAID', false, op(sStop))}
      {bar(L.hyp_words, 'WORDS WRITTEN', true, op(sCount))}
      <div style={{ fontFamily: HAI_TYPE.serif, fontStyle: 'italic', fontSize: repS, color: SPARK_TEXT, opacity: 0.3 + 0.7 * op(sRep),
        maxWidth: BW, lineHeight: 1.2 }}>{`“${portrait ? L.sample.split(' ').slice(0, 5).join(' ') : L.sample}…”`}</div>
    </div>
  );
  const pairS = portrait ? T.body * 1.02 : 50 * U;
  const pair = (saidText: string, wrote: string, o: number) => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 6 : 6 * U, opacity: 0.3 + 0.7 * o }}>
      <div style={{ display: 'flex', alignItems: 'baseline', gap: portrait ? 18 : 18 * U }}>
        <Caps size={lbl} color={CLAUDE.INK} style={{ width: portrait ? 210 : 230 * U }}>{portrait ? 'SAID' : 'VOICE SAID'}</Caps>
        <div style={{ fontFamily: HAI_TYPE.serif, fontSize: pairS, color: CLAUDE.INK }}>{saidText}</div>
      </div>
      <div style={{ display: 'flex', alignItems: 'baseline', gap: portrait ? 18 : 18 * U }}>
        <Caps size={lbl} color={SPARK_TEXT} style={{ width: portrait ? 210 : 230 * U }}>{portrait ? 'WROTE' : 'IT WROTE'}</Caps>
        <div style={{ fontFamily: HAI_TYPE.serif, fontSize: pairS, color: SPARK_TEXT }}>{wrote}</div>
      </div>
    </div>
  );
  const clean = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 12 : 44 * U }}>
      <Caps size={lbl} color={CLAUDE.INK} style={{ opacity: 0.3 + 0.7 * op(sExp) }}>CLEAN SPEECH</Caps>
      {pair('Row-Haan', V.name, op(sName))}
      {pair('dollar three fifty', V.price, op(sPrice))}
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.2 }}>{loud}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.512 }}>{clean}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.28 }}>{loud}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.56, top: height * 0.3 }}>{clean}</div>
      <LandBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
