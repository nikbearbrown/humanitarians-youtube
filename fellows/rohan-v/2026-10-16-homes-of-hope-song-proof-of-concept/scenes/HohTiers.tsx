import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE, sinePath } from '../lib/cueKit';
import { PhoneBaseline } from './shazam/shzKit';

/**
 * HohTiers — two proficiency tiers of one bilingual song (week-08, Lyrical Literacy x Homes of
 * Hope progress, B02). Each tier is a card with a language bar: home language (terracotta) and
 * English (ink). The bar shares are illustrative of the brief's wording ("about 50/50", "mostly
 * English with Hindi as a thread"), so no percentages are printed. One melody line runs through
 * both cards (the same melody and message), and an arrow shows a girl moving up a tier. No
 * person is drawn.
 *
 *   two / t1 / t2 / thread / melody / up
 */

export const hohTiersSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · WEEKLY PROGRESS'),
  title: z.string().default('Two Tiers, One Melody'),
  tiers: z.array(z.object({ name: z.string(), english: z.number(), line: z.string() })).default([]),
  home: z.string().default('HINDI'),
  melody: z.string().default('SAME MELODY, SAME MESSAGE'),
  upLabel: z.string().default('MOVE UP A TIER'),
  sparkLine: z.string().default(''),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type HohTiersProps = z.infer<typeof hohTiersSchema>;

export const HohTiers: React.FC<HohTiersProps> = ({ eyebrow, title, tiers, home, melody, upLabel, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tTwo = at('two', 0.07), tT1 = at('t1', 0.17), tT2 = at('t2', 0.38), tThread = at('thread', 0.57), tMel = at('melody', 0.66), tUp = at('up', 0.84);
  const headIn = sp(0);
  const sCards = sp(tTwo), s1 = sp(tT1), s2 = sp(tT2), sThread = sp(tThread), mel = ramp(tMel, tMel + 0.08), sUp = sp(tUp);
  const sparkIn = sp(clamp(tUp + 0.04, 0, 0.97));
  const lbl = portrait ? T.label * 0.72 : 22 * U;
  const cardIn = [s1, s2];

  const card = (t: { name: string; english: number; line: string }, i: number, w: number) => {
    const k = op(cardIn[i] ?? 1);
    const BW = w - (portrait ? 72 : 80 * U), BH = portrait ? 64 : 80 * U;
    const homeW = BW * (1 - t.english / 100);
    const thread = i === 1 ? op(sThread) : 1;
    return (
      <div key={i} style={{ width: w, boxSizing: 'border-box', background: CLAUDE.CARD, border: `2px solid ${k > 0.5 ? CLAUDE.INK_SOFT : CLAUDE.BORDER}`,
        borderRadius: 18 * U, padding: portrait ? '30px 36px' : `${44 * U}px ${44 * U}px`, opacity: 0.35 + 0.65 * op(sCards) * (0.4 + 0.6 * k) }}>
        <div style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1.4, color: CLAUDE.INK }}>{t.name}</div>
        <div style={{ display: 'flex', width: BW, height: BH, marginTop: portrait ? 22 : 24 * U, borderRadius: 10, overflow: 'hidden', opacity: k }}>
          <div style={{ width: homeW * (i === 1 ? 0.4 + 0.6 * thread : 1), background: SPARK_TEXT }} />
          <div style={{ flex: 1, background: CLAUDE.INK }} />
        </div>
        <div style={{ display: 'flex', justifyContent: 'space-between', width: BW, marginTop: 12, opacity: k }}>
          <span style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl * 0.9, fontWeight: 800, letterSpacing: 1.2, color: SPARK_TEXT }}>{home}</span>
          <span style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl * 0.9, fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK }}>ENGLISH</span>
        </div>
        <div style={{ fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.body * 0.78 : 46 * U, color: CLAUDE.INK, marginTop: portrait ? 18 : 30 * U, opacity: k }}>{t.line}</div>
      </div>
    );
  };
  const wave = (w: number, h: number) => (
    <svg width={w} height={h} style={{ overflow: 'visible', opacity: 0.3 + 0.7 * op(sp(tMel)) }}>
      <path d={sinePath(w, h, h * 0.38, 3.2, 0)} fill="none" stroke={CLAUDE.BORDER} strokeWidth={portrait ? 6 : 5 * U} strokeLinecap="round" />
      <path d={sinePath(w * mel, h, h * 0.38, 3.2 * mel, 0)} fill="none" stroke={SPARK_TEXT} strokeWidth={portrait ? 6 : 5 * U} strokeLinecap="round" />
    </svg>
  );
  const caps = (text: string, o: number, color: string = CLAUDE.INK) => (
    <div style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1.3, color, opacity: o, whiteSpace: 'nowrap' }}>{text}</div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.205, display: 'flex', flexDirection: 'column', gap: height * 0.02 }}>
          {tiers.map((t, i) => card(t, i, CW))}
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.625 }}>{wave(CW, 90)}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.69 }}>{caps(melody, op(sp(tMel)))}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.735 }}>{caps(`↑ ${upLabel}`, op(sUp), SPARK_TEXT)}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  const gap = 150 * U, w = (CW - gap) / 2;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.27, display: 'flex', gap }}>
        {tiers.map((t, i) => card(t, i, w))}
      </div>
      <div style={{ position: 'absolute', left: PAD_X + w + 30 * U, top: height * 0.38, width: gap - 60 * U, textAlign: 'center', opacity: op(sUp),
        fontFamily: HAI_TYPE.sans, fontSize: 64 * U, fontWeight: 800, color: SPARK_TEXT }}>→</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.64 }}>{wave(CW, 80 * U)}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.75, display: 'flex', gap: 60 * U }}>
        {caps(melody, op(sp(tMel)))}
        {caps(upLabel, op(sUp), SPARK_TEXT)}
      </div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
