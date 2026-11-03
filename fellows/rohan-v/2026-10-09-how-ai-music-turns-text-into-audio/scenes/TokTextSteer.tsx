import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { TOK, PhoneBaseline, Label, TokenBox, Chip, listening } from './tokens/tokKit';

/**
 * TokTextSteer — B06 of "How AI Music Generators Turn Text Into Audio."
 *
 * Left: how published systems use the prompt (prompt → text encoder → numbers that tilt every
 * next-token prediction), with MusicGen's verified settings (Meta, 2023: 4 codebooks, 50 frames per
 * second, a T5 text encoder; week-07/_research/facts.md). Right: my toy, where the prompt only picks
 * which music the model learned from: the first tokens it generated for each prompt (codec.py) and
 * the longest stretch it copied from its training music. The beat's audio then plays both
 * generations, and the prompt being heard is lit.
 *
 *   text / encoder   "And the text" / "a text encoder turns your prompt"   left diagram
 *   musicgen / t5    "Meta's MusicGen" / "called T5"                       fact card
 *   toy / calm       "In my toy" / "Calm piano"                            prompt rows
 *   copied           "Neither is copied"                                   copied-stretch stat
 *   listen           (props.listen)                                        now playing
 */

export const tokTextSteerSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('The Words Tilt the Odds'),
  sparkLine: z.string().default("The prompt steers. It doesn't write the notes."),
  listen: z.array(z.object({ label: z.string(), from: z.number(), to: z.number() })).optional(),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type TokTextSteerProps = z.infer<typeof tokTextSteerSchema>;

export const TokTextSteer: React.FC<TokTextSteerProps> = ({ eyebrow, title, sparkLine, listen, cues }) => {
  const { frame, D, width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tText = at('text', 0.02), tEnc = at('encoder', 0.08), tMg = at('musicgen', 0.22), tT5 = at('t5', 0.32);
  const tToy = at('toy', 0.42), tCalm = at('calm', 0.52), tCopied = at('copied', 0.6), tListen = at('listen', 0.72);
  const headIn = sp(0);
  const sText = sp(tText), sEnc = sp(tEnc), sMg = sp(tMg), sT5 = sp(tT5), sToy = sp(tToy), sCalm = sp(tCalm), sCop = sp(tCopied);
  const flow = ramp(tEnc, tEnc + 0.08);
  const sparkIn = sp(clamp(tListen, 0, 0.97));
  const now = listening(listen, frame / D);
  const lbl = portrait ? T.label * 0.7 : 22 * U;

  const G = TOK.gen as Record<string, { prompt: string; first_tokens: number[][]; longest_copied_s: number; seams: number }>;
  const box = portrait ? T.label * 0.6 : 22 * U;
  const pill = (text: string, lit: boolean, size: number) => (
    <span style={{ fontFamily: HAI_TYPE.serif, fontStyle: 'italic', fontSize: size, color: lit ? CLAUDE.CARD : CLAUDE.INK,
      background: lit ? SPARK_TEXT : CLAUDE.CARD, border: `2px solid ${lit ? SPARK_TEXT : CLAUDE.INK}`, borderRadius: size, padding: `${size * 0.15}px ${size * 0.6}px`, whiteSpace: 'nowrap' }}>“{text}”</span>
  );

  const published = (w: number, size: number) => (
    <div style={{ width: w, opacity: op(sText) }}>
      <Label text="PUBLISHED SYSTEMS" size={lbl} color={CLAUDE.INK} style={{ marginBottom: size * 0.7 }} />
      <div style={{ display: 'flex', alignItems: 'center', gap: size * 0.5, flexWrap: 'wrap', rowGap: size * 0.6 }}>
        {pill('the prompt', false, portrait ? T.body : size)}
        <svg width={size * 1.2} height={size} style={{ opacity: flow, flexShrink: 0 }}><path d={`M 0 ${size / 2} L ${size * 0.85} ${size / 2} M ${size * 0.55} ${size * 0.18} L ${size * 1.05} ${size / 2} L ${size * 0.55} ${size * 0.82}`} fill="none" stroke={CLAUDE.INK_SOFT} strokeWidth={4} strokeLinecap="round" strokeLinejoin="round" /></svg>
        <span style={{ opacity: flow, fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.CARD, background: CLAUDE.INK, borderRadius: 8, padding: '8px 14px' }}>TEXT ENCODER</span>
        <svg width={size * 1.2} height={size} style={{ opacity: flow, flexShrink: 0 }}><path d={`M 0 ${size / 2} L ${size * 0.85} ${size / 2} M ${size * 0.55} ${size * 0.18} L ${size * 1.05} ${size / 2} L ${size * 0.55} ${size * 0.82}`} fill="none" stroke={CLAUDE.INK_SOFT} strokeWidth={4} strokeLinecap="round" strokeLinejoin="round" /></svg>
        <span style={{ opacity: flow, fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1.2, color: SPARK_TEXT }}>TILTS EVERY GUESS</span>
      </div>
      <div style={{ marginTop: size * 1.0, background: CLAUDE.CARD, border: `1.5px solid ${CLAUDE.BORDER}`, borderTop: `6px solid ${CLAUDE.INK}`, borderRadius: 14,
        padding: `${size * 0.5}px ${size * 0.7}px`, opacity: op(sMg) }}>
        <Label text="META'S MUSICGEN, 2023" size={lbl} color={CLAUDE.INK} />
        {[['4', 'CODEBOOKS'], ['50', 'FRAMES PER SECOND'], ['T5', 'TEXT ENCODER']].map(([v, k], i) => (
          <div key={k} style={{ display: 'flex', alignItems: 'baseline', gap: 16, marginTop: 8, opacity: i === 2 ? op(sT5) : 1 }}>
            <span style={{ fontFamily: HAI_TYPE.serif, fontSize: size * 1.3, fontWeight: 700, color: i === 2 ? SPARK_TEXT : CLAUDE.INK, minWidth: size * 2 }}>{v}</span>
            <Label text={k} size={lbl} />
          </div>
        ))}
      </div>
    </div>
  );

  const toyRow = (key: 'piano' | 'drums', label: string, o: number, size: number, n: number) => {
    const g = G[key];
    const lit = now?.label === label;
    return (
      <div style={{ opacity: 0.65 + 0.35 * o, marginBottom: size * (portrait ? 0.5 : 0.9) }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 14, marginBottom: portrait ? 0 : 10, float: portrait ? 'left' : undefined, marginRight: portrait ? 18 : 0 }}>
          {pill(g.prompt, !!lit, portrait ? T.body : size * 0.95)}
          {lit ? <Label text="▶ PLAYING" size={lbl} color={SPARK_TEXT} /> : null}
        </div>
        <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap', paddingTop: portrait ? T.body * 0.3 : 0 }}>
          {g.first_tokens.slice(0, n).map((r, i) => <TokenBox key={i} n={r[0]} size={box} />)}
          <span style={{ fontFamily: HAI_TYPE.mono, fontSize: box, color: CLAUDE.INK_SOFT }}>…</span>
        </div>
      </div>
    );
  };
  const toy = (w: number, size: number, n: number) => (
    <div style={{ width: w, opacity: 0.65 + 0.35 * op(sToy) }}>
      <Label text={portrait ? 'MY TOY: WORDS PICK THE MUSIC' : 'MY TOY: THE WORDS PICK THE MUSIC IT LEARNED'} size={lbl} color={CLAUDE.INK} style={{ marginBottom: size * 0.7 }} />
      {toyRow('piano', 'CALM PIANO', op(sCalm), size, n)}
      {toyRow('drums', 'BUSY DRUMS', op(sCalm), size, n)}
      <div style={{ opacity: 0.65 + 0.35 * op(sCop), display: portrait ? 'flex' : 'block', alignItems: 'baseline', gap: 16 }}>
        <div style={{ fontFamily: HAI_TYPE.serif, fontSize: size * 1.5, fontWeight: 700, color: SPARK_TEXT }}>{G.piano.longest_copied_s.toFixed(2)} s</div>
        <Label text={portrait ? 'LONGEST STRETCH COPIED' : 'LONGEST STRETCH COPIED FROM ITS TRAINING MUSIC'} size={lbl} />
      </div>
    </div>
  );

  if (portrait) {
    /* Phone: every block at a fixed height share, nothing left to flow (the first phone final was
       blocked by GATE T §8.6b: the toy label landed on the MusicGen card, and the PLAYING label
       pushed a token row into a column). Rows: pill + tokens on one line, no PLAYING label (the
       lit pill says it). */
    const arrow = (s: number) => (
      <svg width={s * 1.2} height={s} style={{ opacity: flow, flexShrink: 0 }}><path d={`M 0 ${s / 2} L ${s * 0.85} ${s / 2} M ${s * 0.55} ${s * 0.18} L ${s * 1.05} ${s / 2} L ${s * 0.55} ${s * 0.82}`} fill="none" stroke={CLAUDE.INK_SOFT} strokeWidth={4} strokeLinecap="round" strokeLinejoin="round" /></svg>
    );
    const at_ = (y: number, child: React.ReactNode, o = 1) => <div style={{ position: 'absolute', left: PAD_X, top: height * y, width: CW, opacity: o }}>{child}</div>;
    const row = (key: 'piano' | 'drums', label: string) => {
      const g = G[key];
      return (
        <div style={{ display: 'flex', alignItems: 'center', gap: 16, flexWrap: 'nowrap', opacity: 0.65 + 0.35 * op(sCalm) }}>
          {pill(g.prompt, now?.label === label, T.body)}
          {g.first_tokens.slice(0, 3).map((r, i) => <TokenBox key={i} n={r[0]} size={box} />)}
        </div>
      );
    };
    const enc = <span style={{ opacity: flow, fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.CARD, background: CLAUDE.INK, borderRadius: 8, padding: '8px 14px', whiteSpace: 'nowrap' }}>TEXT ENCODER</span>;
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        {at_(0.19, <Label text="PUBLISHED SYSTEMS" size={lbl} color={CLAUDE.INK} />, op(sText))}
        {at_(0.222, <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>{pill('the prompt', false, T.body)}{arrow(lbl)}</div>, op(sText))}
        {at_(0.305, <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>{enc}{arrow(lbl)}<Label text="TILTS EVERY GUESS" size={lbl} color={SPARK_TEXT} opacity={flow} /></div>, op(sText))}
        {at_(0.35, (
          <div style={{ background: CLAUDE.CARD, border: `1.5px solid ${CLAUDE.BORDER}`, borderTop: `6px solid ${CLAUDE.INK}`, borderRadius: 14, padding: '14px 22px' }}>
            <Label text="META'S MUSICGEN, 2023" size={lbl} color={CLAUDE.INK} />
            {[['4', 'CODEBOOKS'], ['50', 'FRAMES PER SECOND'], ['T5', 'TEXT ENCODER']].map(([v, k], i) => (
              <div key={k} style={{ display: 'flex', alignItems: 'baseline', gap: 18, marginTop: 6, opacity: i === 2 ? op(sT5) : 1 }}>
                <span style={{ fontFamily: HAI_TYPE.serif, fontSize: T.body * 0.9, fontWeight: 700, color: i === 2 ? SPARK_TEXT : CLAUDE.INK, minWidth: T.body * 1.3 }}>{v}</span>
                <Label text={k} size={lbl} />
              </div>
            ))}
          </div>
        ), op(sMg))}
        {at_(0.56, <Label text="MY TOY: WORDS PICK THE MUSIC" size={lbl} color={CLAUDE.INK} />, 0.65 + 0.35 * op(sToy))}
        {at_(0.594, row('piano', 'CALM PIANO'))}
        {at_(0.666, row('drums', 'BUSY DRUMS'))}
        {at_(0.737, (
          <div style={{ display: 'flex', alignItems: 'baseline', gap: 16 }}>
            <span style={{ fontFamily: HAI_TYPE.serif, fontSize: T.body, fontWeight: 700, color: SPARK_TEXT }}>{G.piano.longest_copied_s.toFixed(2)} s</span>
            <Label text="LONGEST STRETCH COPIED" size={lbl} />
          </div>
        ), 0.65 + 0.35 * op(sCop))}
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn * (now ? 0 : 1)} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.27 }}>{published(CW * 0.46, 30 * U)}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.54, top: height * 0.27 }}>{toy(CW * 0.46, 30 * U, 6)}</div>
      {now ? <div style={{ position: 'absolute', right: PAD_X, top: height * 0.82 }}><Chip text={`▶ NOW PLAYING: ${now.label}`} size={24 * U} accent /></div> : null}
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
