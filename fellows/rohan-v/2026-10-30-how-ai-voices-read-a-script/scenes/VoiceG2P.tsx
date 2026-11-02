import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { VOICE, Caps, Chip, Ipa, PhoneBaseline, LandBaseline } from './voice/voiceKit';

/**
 * VoiceG2P — B02 of "How AI Voices Read a Script."
 *
 * G2P (graphemes to phonemes) on four everyday words, each with the narrator's own phonemes from voice.py; then
 * the two ways the step works (a dictionary for words it knows, letter rules for the rest; espeak-ng's
 * docs, facts-tts) as two plain cards; then where it goes wrong: one spelling, two words.
 *
 *   g2p / letters / espeak / dict / rules / works / wrong
 */

export const voiceG2PSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Letters to Sounds'),
  sparkLine: z.string().default('A dictionary first, then rules.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type VoiceG2PProps = z.infer<typeof voiceG2PSchema>;

export const VoiceG2P: React.FC<VoiceG2PProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tG = at('g2p', 0.02), tL = at('letters', 0.12), tE = at('espeak', 0.32), tD = at('dict', 0.42);
  const tR = at('rules', 0.55), tW = at('works', 0.75), tWrong = at('wrong', 0.86);
  const headIn = sp(0);
  const sG = sp(tG), sL = sp(tL), sD = sp(tD), sR = sp(tR), sWrong = sp(Math.min(tWrong, 0.88));
  const sparkIn = sp(clamp(Math.min(tWrong + 0.03, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const ex = VOICE.examples as { word: string; ipa: string }[];
  const big = portrait ? T.body * 1.05 : 50 * U;

  const rows = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 18 : 20 * U, opacity: 0.35 + 0.65 * op(sL) }}>
      <div style={{ display: 'flex', gap: portrait ? 30 : 40 * U }}>
        <Caps size={lbl} color={CLAUDE.INK} style={{ width: portrait ? 330 : 260 * U }}>LETTERS</Caps>
        <Caps size={lbl} color={SPARK_TEXT}>SOUNDS</Caps>
      </div>
      {ex.map((e, i) => (
        <div key={e.word} style={{ display: 'flex', alignItems: 'center', gap: portrait ? 30 : 40 * U, opacity: op(sp(tL + 0.03 * i)) }}>
          <div style={{ width: portrait ? 330 : 260 * U, fontFamily: HAI_TYPE.serif, fontSize: big, color: CLAUDE.INK }}>{e.word}</div>
          <Ipa ipa={e.ipa} size={big} />
        </div>
      ))}
    </div>
  );
  const box = (head: string, body: string, o: number) => (
    <div style={{ opacity: 0.3 + 0.7 * o, background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 14 * U,
      padding: portrait ? '20px 26px' : `${22 * U}px ${26 * U}px`, width: portrait ? CW : CW * 0.36, boxSizing: 'border-box' }}>
      <Caps size={lbl} color={CLAUDE.INK}>{head}</Caps>
      <div style={{ fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.body * 1.05 : 44 * U, color: CLAUDE.INK, marginTop: 8 }}>{body}</div>
    </div>
  );
  const boxes = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 18 : 22 * U, opacity: op(sG) }}>
      {box('1 · A DICTIONARY', portrait ? 'Words it knows' : 'For the words it knows', op(sD))}
      {box('2 · LETTER RULES', portrait ? 'A guess for the rest' : 'A guess for the rest', op(sR))}
    </div>
  );
  const wrong = <div style={{ opacity: op(sWrong) }}><Chip text={portrait ? 'SAME LETTERS, TWO WORDS' : 'IT GOES WRONG WHEN THE SAME LETTERS MAKE TWO WORDS'} size={portrait ? T.label * 0.8 : 22 * U} accent /></div>;

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.205 }}>{rows}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.48 }}>{boxes}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.715 }}>{wrong}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.27 }}>{rows}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.62, top: height * 0.27 }}>{boxes}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.76 }}>{wrong}</div>
      <LandBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
