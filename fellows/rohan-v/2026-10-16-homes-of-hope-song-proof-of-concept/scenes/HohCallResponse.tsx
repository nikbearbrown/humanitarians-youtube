import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { PhoneBaseline } from './shazam/shzKit';

/**
 * HohCallResponse — a call-and-response lyric card for a bilingual song (week-08, Lyrical
 * Literacy x Homes of Hope progress, B01). Each card holds one real line pair from the songs:
 * the lead's line in the home language (Roman script) and the group's answer in English, with
 * an arrow between them; a footnote carries the review status. No person is drawn (the method
 * is the subject), so the PROFESSOR BEAR LAW is not triggered.
 *
 *   method "call and response"   cards in
 *   lead   "The lead sings"      lead lines light
 *   group  "the group answers"   group lines light
 *   meaning "arrives with its meaning"  footnote
 */

export const hohCallResponseSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · WEEKLY PROGRESS'),
  title: z.string().default('Call and Response'),
  pairs: z.array(z.object({ lead: z.string(), group: z.string(), song: z.string() })).default([]),
  leadLabel: z.string().default('LEAD · HINDI'),
  groupLabel: z.string().default('GROUP · ENGLISH'),
  note: z.string().default(''),
  sparkLine: z.string().default(''),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type HohCallResponseProps = z.infer<typeof hohCallResponseSchema>;

export const HohCallResponse: React.FC<HohCallResponseProps> = ({ eyebrow, title, pairs, leadLabel, groupLabel, note, sparkLine, cues }) => {
  const { width, height, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tMethod = at('method', 0.05), tLead = at('lead', 0.22), tGroup = at('group', 0.45), tMeaning = at('meaning', 0.85);
  const headIn = sp(0);
  const sCards = sp(tMethod), sLead = sp(tLead), sGroup = sp(tGroup), sNote = sp(tMeaning);
  const sparkIn = sp(clamp(tMeaning + 0.03, 0, 0.97));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const lineSize = portrait ? T.body * 1.06 : 62 * U;

  const card = (p: { lead: string; group: string; song: string }, i: number, w: number) => {
    const lag = i * 0.08;
    const lead = op(sp(tLead + lag)), group = op(sp(tGroup + lag));
    return (
      <div key={i} style={{ width: w, boxSizing: 'border-box', background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 18 * U,
        padding: portrait ? '28px 36px' : `${52 * U}px ${48 * U}px`, opacity: op(sCards), transform: `translateY(${(1 - op(sCards)) * 20}px)` }}>
        <div style={{ fontFamily: HAI_TYPE.sans, fontSize: portrait ? lbl : lbl * 0.9, fontWeight: 800, letterSpacing: 1.4, color: CLAUDE.INK_SOFT, marginBottom: portrait ? 16 : 34 * U }}>{p.song}</div>
        <div style={{ opacity: 0.25 + 0.75 * lead }}>
          <div style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1.2, color: SPARK_TEXT }}>{leadLabel}</div>
          <div style={{ fontFamily: HAI_TYPE.serif, fontStyle: 'italic', fontSize: lineSize, color: CLAUDE.INK, lineHeight: 1.2, marginTop: 8 }}>{p.lead}</div>
        </div>
        <div style={{ opacity: 0.25 + 0.75 * group, marginTop: portrait ? 18 : 40 * U }}>
          <div style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK }}>
            {portrait ? null : <span style={{ color: SPARK_TEXT, opacity: group }}>→ </span>}{groupLabel}</div>
          <div style={{ fontFamily: HAI_TYPE.serif, fontSize: lineSize, fontWeight: 600, color: CLAUDE.INK, lineHeight: 1.2, marginTop: 8 }}>{p.group}</div>
        </div>
      </div>
    );
  };
  const footnote = note ? (
    <div style={{ fontFamily: HAI_TYPE.sans, fontSize: portrait ? lbl : lbl * 0.9, fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK_SOFT, opacity: op(sNote), whiteSpace: 'nowrap' }}>{note.toUpperCase()}</div>
  ) : null;

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        {/* phone: one card slot; the second pair replaces the first after the group's answer */}
        {pairs.map((p, i) => {
          const swap = clamp(tGroup + 0.17, 0, 0.9);
          const o = pairs.length < 2 ? 1 : i === 0 ? 1 - op(sp(swap)) : op(sp(swap));
          return <div key={i} style={{ position: 'absolute', left: PAD_X, top: height * 0.215, opacity: o }}>{card(p, 0, CW)}</div>;
        })}
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.73 }}>{footnote}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  const gap = 48 * U;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.28, display: 'flex', gap }}>
        {pairs.map((p, i) => card(p, i, (CW - gap * (pairs.length - 1)) / Math.max(1, pairs.length)))}
      </div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.775 }}>{footnote}</div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
