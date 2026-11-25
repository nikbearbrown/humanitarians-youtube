import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { VOICE, Caps, Chip, Ipa, PhoneBaseline, LandBaseline, listening } from './voice/voiceKit';

/**
 * VoiceRespell — B05 of "How AI Voices Read a Script."
 *
 * The fix, on our narrator's own past mistakes (voice.py): each word, its phonemes as read, the respelling our
 * scripts use, and the new phonemes. Ends with the run's own two clips of the presenter's name, as read and
 * respelled (props.listen); the matching row lights while each plays.
 *
 *   fix / name / dhol / sitar / here
 */

export const voiceRespellSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Spell It the Way It Sounds'),
  sparkLine: z.string().default('Respell it, then listen again.'),
  listen: z.array(z.object({ label: z.string(), from: z.number(), to: z.number() })).optional(),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type VoiceRespellProps = z.infer<typeof voiceRespellSchema>;

export const VoiceRespell: React.FC<VoiceRespellProps> = ({ eyebrow, title, sparkLine, listen, cues }) => {
  const { width, height, frame, D, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tFix = at('fix', 0.02), tName = at('name', 0.15), tDhol = at('dhol', 0.4), tSitar = at('sitar', 0.55), tHere = at('here', 0.68);
  const headIn = sp(0);
  const s0 = sp(tFix);
  const rowIn = [sp(tName), sp(tDhol), sp(tSitar), sp(tSitar + 0.04)];
  const now = listening(listen, frame / D);
  const sparkIn = sp(clamp(Math.min(tHere, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const R = VOICE.respell as any[];
  const fs = portrait ? T.body * 1.02 : 50 * U, ipaS = portrait ? T.body * 0.8 : 44 * U;

  const row = (r: any, i: number) => {
    const o = op(rowIn[i]);
    const playing = i === 0 && now;
    return (
      <div key={r.word} style={{ display: 'flex', flexDirection: portrait ? 'column' : 'row', alignItems: portrait ? 'flex-start' : 'center',
        gap: portrait ? 6 : 26 * U, opacity: 0.25 + 0.75 * o, background: playing ? CLAUDE.CARD : 'transparent', borderRadius: 12,
        padding: portrait ? '4px 0' : `${8 * U}px 0` }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: portrait ? 16 : 26 * U }}>
          <div style={{ width: portrait ? 410 : 210 * U, fontFamily: HAI_TYPE.serif, fontSize: fs, lineHeight: 1.1, whiteSpace: 'nowrap', color: CLAUDE.INK }}>{r.word}</div>
          <Ipa ipa={r.ipa} size={ipaS} color={SPARK_TEXT} style={{ outline: playing && now && now.label === 'AS READ' ? `3px solid ${SPARK_TEXT}` : 'none' }} />
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: portrait ? 16 : 26 * U, marginLeft: portrait ? 0 : 0 }}>
          {portrait ? null : <Caps size={lbl} style={{ width: 170 * U }}>RESPELLED</Caps>}
          <div style={{ fontFamily: HAI_TYPE.serif, fontSize: fs, fontWeight: portrait ? 700 : 400, lineHeight: 1.1, whiteSpace: 'nowrap', color: CLAUDE.INK, width: portrait ? 410 : 250 * U }}>{r.fix}</div>
          <Ipa ipa={r.ipa_fix} size={ipaS} style={{ outline: playing && now && now.label === 'RESPELLED' ? `3px solid ${CLAUDE.INK}` : 'none' }} />
        </div>
      </div>
    );
  };
  const rows = <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 10 : 26 * U, opacity: op(s0) }}>
    {portrait ? <Caps size={lbl} color={CLAUDE.INK}>WRITTEN, THEN RESPELLED</Caps> : null}{R.map(row)}</div>;
  const playChip = <div style={{ opacity: now ? 1 : 0.3 }}><Chip text={now ? `▶ MY NAME: ${now.label}` : '▶ LISTEN: MY NAME'} size={portrait ? T.label * 0.8 : 24 * U} accent /></div>;

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.2 }}>{rows}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.715 }}>{playChip}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.27 }}>{rows}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.74 }}>{playChip}</div>
      <LandBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
