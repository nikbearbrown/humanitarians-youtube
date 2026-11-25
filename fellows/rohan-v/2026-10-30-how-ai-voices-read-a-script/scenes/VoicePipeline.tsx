import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { VOICE, Caps, Chip, Ipa, PhoneBaseline, LandBaseline } from './voice/voiceKit';

/**
 * VoicePipeline — B01 of "How AI Voices Read a Script."
 *
 * The three steps of text-to-speech, carried through one real example from voice.py: "Dr. Smith" (the text),
 * "doctor smith" (cleaned up), the narrator's own phonemes for it, and then a voice. The last card says the voice
 * model only ever receives the phonemes. "About 44" phonemes in English (varies by accent; facts-tts §5).
 *
 *   three / clean / phonemes / fortyfour / model / never / only
 */

export const voicePipelineSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Text, Then Sounds, Then a Voice'),
  sparkLine: z.string().default('The voice only hears the sounds.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type VoicePipelineProps = z.infer<typeof voicePipelineSchema>;

export const VoicePipeline: React.FC<VoicePipelineProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tThree = at('three', 0.02), tClean = at('clean', 0.1), tPh = at('phonemes', 0.3), tFour = at('fortyfour', 0.45);
  const tModel = at('model', 0.6), tNever = at('never', 0.78), tOnly = at('only', 0.9);
  const headIn = sp(0);
  const s0 = sp(tThree), s1 = sp(tClean), s2 = sp(tPh), s4 = sp(tFour), s3 = sp(tModel), sNever = sp(tNever);
  const sparkIn = sp(clamp(Math.min(tOnly, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const ex = (VOICE.normalise as any[])[0];   // "Dr. Smith"

  const bars = Array.from({ length: 28 }, (_, i) => 0.25 + 0.75 * Math.abs(Math.sin(i * 1.7) * Math.cos(i * 0.6)));
  const card = (n: number, head: string, body: React.ReactNode, o: number, hot = false) => (
    <div style={{ opacity: 0.3 + 0.7 * o, background: CLAUDE.CARD, border: `2px solid ${hot && o > 0.5 ? SPARK_TEXT : CLAUDE.BORDER}`, borderRadius: 16 * U,
      padding: portrait ? '24px 28px' : `${28 * U}px ${30 * U}px`, width: portrait ? CW : (CW - 2 * 40 * U) / 3, boxSizing: 'border-box',
      minHeight: portrait ? undefined : height * 0.34 }}>
      <Caps size={lbl} color={hot ? SPARK_TEXT : CLAUDE.INK_SOFT}>{`${n} · ${head}`}</Caps>
      <div style={{ marginTop: portrait ? 14 : 22 * U }}>{body}</div>
    </div>
  );
  const big = portrait ? T.body * 1.05 : 46 * U;
  const cards = (
    <>
      {card(1, 'CLEAN UP THE TEXT', (
        <div style={{ fontFamily: HAI_TYPE.serif, fontSize: big, color: CLAUDE.INK, lineHeight: 1.3 }}>
          <span style={{ color: CLAUDE.INK_SOFT }}>{ex.text}</span><br />{ex.reads}
        </div>), op(s1))}
      {card(2, 'WORDS TO SOUNDS', (
        <div>
          <Ipa ipa={ex.ipa} size={big} />
          <Caps size={lbl} style={{ marginTop: portrait ? 12 : 16 * U, opacity: op(s4) }}>ABOUT 44 SOUNDS IN ENGLISH</Caps>
        </div>), op(s2))}
      {card(3, 'SOUNDS TO A VOICE', (
        <svg width={portrait ? CW - 60 : (CW - 80 * U) / 3 - 60 * U} height={portrait ? 90 : 110 * U} style={{ display: 'block', overflow: 'visible' }}>
          {bars.map((b, i) => {
            const w = (portrait ? CW - 60 : (CW - 80 * U) / 3 - 60 * U) / bars.length;
            const h = (portrait ? 90 : 110 * U) * b * op(s3);
            return <rect key={i} x={i * w + w * 0.2} y={((portrait ? 90 : 110 * U) - h) / 2} width={w * 0.6} height={h} rx={w * 0.3} fill={CLAUDE.INK} />;
          })}
        </svg>), op(s3), true)}
    </>
  );
  const never = <div style={{ opacity: op(sNever) }}><Chip text={portrait ? 'THE VOICE GETS ONLY SOUNDS' : 'THE VOICE MODEL NEVER SEES THE SPELLING'} size={portrait ? T.label * 0.8 : 24 * U} accent /></div>;

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.205, display: 'flex', flexDirection: 'column', gap: height * 0.018, opacity: op(s0) }}>{cards}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.715 }}>{never}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.27, display: 'flex', gap: 40 * U, opacity: op(s0) }}>{cards}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.7 }}>{never}</div>
      <LandBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
