import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { VOICE, Caps, Chip, Mark, PhoneBaseline, LandBaseline, listening } from './voice/voiceKit';

/**
 * VoiceNumbers — B04 of "How AI Voices Read a Script."
 *
 * The clean-up step on seven cases (voice.py): what was typed, and what the narrator's G2P turned it into, read
 * back as words from its IPA (export_voice_data.py). Six read the way a person would; the price comes out
 * "dollar three. fifty". Ends with the run's own clip of that price (props.listen).
 *
 *   better / list / price / dollar / listen
 */

export const voiceNumbersSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Numbers and Short Forms'),
  sparkLine: z.string().default("Six of seven right. Prices aren't."),
  listen: z.array(z.object({ label: z.string(), from: z.number(), to: z.number() })).optional(),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type VoiceNumbersProps = z.infer<typeof voiceNumbersSchema>;

export const VoiceNumbers: React.FC<VoiceNumbersProps> = ({ eyebrow, title, sparkLine, listen, cues }) => {
  const { width, height, frame, D, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tBetter = at('better', 0.02), tList = at('list', 0.1), tPrice = at('price', 0.45), tDollar = at('dollar', 0.6);
  const headIn = sp(0);
  const sRows = sp(tBetter), fill = ramp(tList, tPrice), sPrice = sp(tPrice), sDollar = sp(tDollar);
  const now = listening(listen, frame / D);
  const sparkIn = sp(clamp(Math.min(tDollar + 0.1, 0.86), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const N = VOICE.normalise as any[];
  const ok = N.filter((n) => n.ok).length;

  const typedW = portrait ? 380 : 380 * U, fs = portrait ? T.body * 1.02 : 44 * U, mark = portrait ? 52 : 42 * U;
  // the phone stacks each row (typed, then what was read) and keeps the five the narration names
  const SAID = ['Dr. Smith', 'Main St.', '1,024 bytes', 'the 5th of May'];
  const shown = portrait ? N.filter((n) => !n.ok || SAID.includes(n.text)) : N;
  const rows = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 10 : 14 * U, opacity: op(sRows) }}>
      <div style={{ display: 'flex', gap: 24 }}>
        <Caps size={lbl} color={CLAUDE.INK} style={{ width: portrait ? undefined : typedW }}>{portrait ? 'TYPED,' : 'TYPED'}</Caps>
        <Caps size={lbl} color={SPARK_TEXT}>{portrait ? 'READ AS' : 'READ AS (FROM ITS PHONEMES)'}</Caps>
      </div>
      {shown.map((n, i) => {
        const isPrice = !n.ok;
        const o = isPrice ? op(sPrice) : clamp(fill * (shown.length - 1) - i, 0, 1);
        if (portrait) return (
          <div key={n.text} style={{ display: 'flex', flexDirection: 'column', gap: 2, opacity: 0.25 + 0.75 * o }}>
            <div style={{ fontFamily: HAI_TYPE.serif, fontSize: fs, color: CLAUDE.INK, whiteSpace: 'nowrap', lineHeight: 1.1 }}>{n.text}</div>
            <div style={{ display: 'flex', alignItems: 'center', gap: 18 }}>
              <Mark ok={n.ok} size={mark} opacity={o} />
              <div style={{ fontFamily: HAI_TYPE.serif, fontStyle: 'italic', fontSize: fs, lineHeight: 1.05, color: isPrice && op(sDollar) > 0.5 ? SPARK_TEXT : CLAUDE.INK, maxWidth: CW - mark - 18 }}>{n.reads}</div>
            </div>
          </div>
        );
        return (
          <div key={n.text} style={{ display: 'flex', alignItems: 'center', gap: 24, opacity: 0.25 + 0.75 * o }}>
            <div style={{ width: typedW, fontFamily: HAI_TYPE.serif, fontSize: fs, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>{n.text}</div>
            <Mark ok={n.ok} size={mark} opacity={o} />
            <div style={{ fontFamily: HAI_TYPE.serif, fontStyle: 'italic', fontSize: fs, color: isPrice && op(sDollar) > 0.5 ? SPARK_TEXT : CLAUDE.INK, whiteSpace: 'nowrap' }}>{n.reads}</div>
          </div>
        );
      })}
    </div>
  );
  const chips = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 16 : 16 * U, alignItems: 'flex-start' }}>
      <div style={{ opacity: op(sDollar) }}><Chip text={`${ok} OF ${N.length} READ RIGHT`} size={portrait ? T.label * 0.8 : 24 * U} /></div>
      <div style={{ opacity: now ? 1 : 0.3 }}><Chip text="▶ NOW PLAYING: THE PRICE" size={portrait ? T.label * 0.8 : 24 * U} accent /></div>
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.19 }}>{rows}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.25 }}>{rows}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.7, top: height * 0.3 }}>{chips}</div>
      <LandBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
