import React from 'react';
import { AbsoluteFill, Img, staticFile } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { CAP, Caps, Stat, WhisperTag, PhoneBaseline, LandBaseline } from './captions/capKit';

/**
 * CapSpectro — B01 of "How Auto-Captions Find Each Word."
 *
 * Test sentence 1 as Whisper's front end sees it: an 80-band log-Mel spectrogram (export_cap_data.py, from the
 * run's own WAV), then the words faster-whisper wrote for it appearing one by one below (the run's own output).
 * Stats: 80 bands, 30-second chunks, 680,000 hours of training audio (the original Whisper models; facts-asr §1).
 *
 *   picture / eighty / chunks / whisper / hours / predicts / piece
 */

export const capSpectroSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Sound Becomes a Picture'),
  sparkLine: z.string().default('A picture of sound, read like a page.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type CapSpectroProps = z.infer<typeof capSpectroSchema>;

export const CapSpectro: React.FC<CapSpectroProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tPic = at('picture', 0.02), tEighty = at('eighty', 0.15), tChunks = at('chunks', 0.28), tWh = at('whisper', 0.38);
  const tHours = at('hours', 0.5), tPred = at('predicts', 0.72), tPiece = at('piece', 0.85);
  const headIn = sp(0);
  const sPic = sp(tPic), sE = sp(tEighty), sC = sp(tChunks), sW = sp(tWh), sH = sp(tHours), words = ramp(tPred, Math.min(tPiece + 0.08, 0.95));
  const sparkIn = sp(clamp(Math.min(tPiece + 0.04, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const ex = CAP.example as any;
  const ws = ex.whisper as { w: string; start: number }[];

  const MW = portrait ? CW : CW * 0.62, MH = portrait ? height * 0.13 : height * 0.36;
  const MX = PAD_X, MY = portrait ? height * 0.215 : height * 0.27;
  const mel = (
    <div style={{ position: 'absolute', left: MX, top: MY, width: MW, height: MH, opacity: op(sPic), background: CLAUDE.CARD, border: `1.5px solid ${CLAUDE.BORDER}` }}>
      <Img src={staticFile(CAP.mel.src)} style={{ width: MW, height: MH, display: 'block' }} />
    </div>
  );
  const tokens = (
    <div style={{ position: 'absolute', left: MX, top: MY + MH + (portrait ? 24 : 26 * U), width: MW, display: 'flex', flexWrap: 'wrap', gap: portrait ? 10 : 10 * U }}>
      {ws.map((w, i) => {
        const o = clamp(words * ws.length - i, 0, 1);
        return <span key={i} style={{ opacity: 0.35 + 0.65 * o, fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.body * 1.02 : 44 * U, color: CLAUDE.INK, background: CLAUDE.CARD,
          border: `1.5px solid ${CLAUDE.BORDER}`, borderRadius: 8, padding: portrait ? '4px 12px' : `${3 * U}px ${10 * U}px` }}>{w.w.replace(/[.,]$/, '')}</span>;
      })}
    </div>
  );
  const big = portrait ? T.title * 0.95 : 62 * U;
  const side = (dir: 'row' | 'column') => (
    <div style={{ display: 'flex', flexDirection: dir, gap: dir === 'row' ? 0 : 26 * U, justifyContent: 'space-between', width: dir === 'row' ? CW : undefined, flexWrap: 'wrap' }}>
      <Stat value="80" label="FREQUENCY BANDS" size={big} opacity={0.3 + 0.7 * op(sE)} />
      <Stat value="30 s" label="CHUNKS AT A TIME" size={big} opacity={0.3 + 0.7 * op(sC)} />
      {dir === 'column' ? <div style={{ opacity: 0.3 + 0.7 * op(sW) }}><WhisperTag size={lbl} /></div> : null}
      <Stat value="680,000" label={dir === 'row' ? 'HOURS OF AUDIO' : 'HOURS OF TRAINING AUDIO'} size={big} opacity={0.3 + 0.7 * op(sH)} accent />
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        {mel}
        {tokens}
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.556, opacity: 0.3 + 0.7 * op(sW) }}><WhisperTag size={lbl} /></div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.593 }}>{side('row')}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: MX, top: MY - lbl * 1.9, opacity: op(sPic) }}>ONE TEST SENTENCE AS THE MODEL SEES IT: 80 BANDS, LOW AT THE BOTTOM</Caps>
      {mel}
      {tokens}
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.68, top: MY }}>{side('column')}</div>
      <LandBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
