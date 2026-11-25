import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { VOICE, Caps, Mark, Ipa, Stat, PhoneBaseline, LandBaseline } from './voice/voiceKit';

/**
 * VoiceHeteronyms — B03 of "How AI Voices Read a Script."
 *
 * The heteronym test (voice.py): 8 words, each in two sentences that fix its meaning; right / wrong per
 * sentence from the narrator's own phonemes. Then the totals (10 of 16; both right for 2 of 8) and the worked
 * case: "Last night I read a book" gets /ɹˈiːd/ (reed), not /ɹˈɛd/ (red).
 *
 *   eight / sixteen / ten / two / last / reed / clues
 */

export const voiceHeteronymsSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Same Spelling, Two Words'),
  sparkLine: z.string().default('Sixteen sentences, ten right.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type VoiceHeteronymsProps = z.infer<typeof voiceHeteronymsSchema>;

export const VoiceHeteronyms: React.FC<VoiceHeteronymsProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tEight = at('eight', 0.02), tSixteen = at('sixteen', 0.3), tTen = at('ten', 0.36), tTwo = at('two', 0.45);
  const tLast = at('last', 0.58), tReed = at('reed', 0.68), tClues = at('clues', 0.85);
  const headIn = sp(0);
  const sGrid = sp(tEight), fill = ramp(tEight + 0.05, tSixteen), sTen = sp(tTen), sTwo = sp(tTwo), sLast = sp(tLast), sReed = sp(tReed);
  const sparkIn = sp(clamp(Math.min(tClues, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const H = VOICE.heteronyms as any[];
  const read = H[0].forms[1];

  const rowH = portrait ? 64 : 58 * U, mark = portrait ? 46 : 40 * U;
  const grid = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 6 : 8 * U, opacity: op(sGrid) }}>
      {H.map((h, i) => {
        const on = clamp(fill * H.length - i, 0, 1);
        return (
          <div key={h.word} style={{ display: 'flex', alignItems: 'center', height: rowH, gap: portrait ? 20 : 20 * U }}>
            <div style={{ width: portrait ? 250 : 220 * U, fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.body * 1.05 : 46 * U, color: h.both_right && op(sTwo) > 0.5 ? CLAUDE.INK : CLAUDE.INK }}>{h.word}</div>
            {h.forms.map((f: any, j: number) => (
              <div key={j} style={{ display: 'flex', alignItems: 'center', gap: 12, width: portrait ? 320 : 260 * U, opacity: on }}>
                <Mark ok={f.right} size={mark} />
                <Caps size={lbl * 0.9} color={f.right ? CLAUDE.INK_SOFT : SPARK_TEXT}>{f.meaning.toUpperCase()}</Caps>
              </div>
            ))}
          </div>
        );
      })}
    </div>
  );
  const big = portrait ? T.title * 1.0 : 70 * U;
  const stats = (dir: 'row' | 'column') => (
    <div style={{ display: 'flex', flexDirection: dir, gap: dir === 'row' ? 0 : 28 * U, justifyContent: 'space-between', width: dir === 'row' ? CW : undefined }}>
      <Stat value={`${VOICE.heteronym_right} / 16`} label="SENTENCES RIGHT" size={big} opacity={0.3 + 0.7 * op(sTen)} accent />
      <Stat value={`${VOICE.heteronym_both} / 8`} label="WORDS RIGHT BOTH WAYS" size={big} opacity={0.3 + 0.7 * op(sTwo)} />
    </div>
  );
  const example = (
    <div style={{ opacity: op(sLast) }}>
      <div style={{ fontFamily: HAI_TYPE.serif, fontStyle: 'italic', fontSize: portrait ? T.body : 40 * U, color: CLAUDE.INK }}>“{read.sentence}”</div>
      <div style={{ display: 'flex', alignItems: 'center', gap: portrait ? 18 : 18 * U, marginTop: portrait ? 12 : 12 * U, flexWrap: 'wrap' }}>
        <Caps size={lbl} color={SPARK_TEXT}>SAID</Caps><Ipa ipa={read.ipa.split(' ')[3]} size={portrait ? T.body : 40 * U} color={SPARK_TEXT} />
        <Caps size={lbl} style={{ opacity: op(sReed) }}>NOT</Caps><span style={{ opacity: op(sReed) }}><Ipa ipa={read.expected} size={portrait ? T.body : 40 * U} /></span>
      </div>
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.2 }}>{grid}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.505 }}>{stats('row')}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.6 }}>{example}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.25 }}>{grid}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.6, top: height * 0.26 }}>{stats('column')}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.6, top: height * 0.58, width: CW * 0.4 }}>{example}</div>
      <LandBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
