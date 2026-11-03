import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { NOTES, BLACK, PhoneBaseline, Caps } from './keys/keyKit';

/**
 * KeyNotes — B01 of "How Apps Find a Song's Key."
 *
 * What a key is, on one octave of a piano: C major's seven notes are the white keys, with C as home (a ring);
 * then A minor lights the very same seven keys with the home moved to A. Two cards spell both scales so the
 * viewer can see the notes are identical and only the home differs.
 *
 *   seven / white / chome / aminor / ahome / wrong
 */

export const keyNotesSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Seven Notes and a Home'),
  sparkLine: z.string().default('Same notes, different home.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type KeyNotesProps = z.infer<typeof keyNotesSchema>;

const WHITE = [0, 2, 4, 5, 7, 9, 11];

export const KeyNotes: React.FC<KeyNotesProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tSeven = at('seven', 0.03), tWhite = at('white', 0.16), tCh = at('chome', 0.3), tAm = at('aminor', 0.42);
  const tAh = at('ahome', 0.6), tWrong = at('wrong', 0.8);
  const headIn = sp(0);
  const sKeys = sp(tSeven), sWhite = sp(tWhite), sC = sp(tCh), sAm = sp(tAm), sAh = sp(tAh), sWrong = sp(tWrong);
  const sparkIn = sp(clamp(tWrong + 0.04, 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const home = op(sAh) > 0.5 ? 9 : 0;           // the ring moves from C to A
  const homeOn = Math.max(op(sC) * (1 - op(sAm)), op(sAh));

  const KW = portrait ? CW : CW * 0.62, KH = portrait ? height * 0.17 : height * 0.46;
  const KX = PAD_X, KY = portrait ? height * 0.215 : height * 0.27;
  const ww = KW / 7;
  const whiteIdx = (pc: number) => WHITE.indexOf(pc);
  const keyboard = (
    <svg width={KW} height={KH + lbl * 2.2} style={{ position: 'absolute', left: KX, top: KY, overflow: 'visible', opacity: op(sKeys) }}>
      {WHITE.map((pc, i) => {
        const lit = op(sWhite);
        return (
          <g key={pc}>
            <rect x={i * ww} y={0} width={ww - 4} height={KH} rx={8} fill={lit > 0.5 ? CLAUDE.CARD : CLAUDE.PAGE}
              stroke={lit > 0.5 ? CLAUDE.INK : CLAUDE.BORDER} strokeWidth={lit > 0.5 ? 4 : 2} />
            <text x={i * ww + ww / 2 - 2} y={KH + lbl * 1.5} textAnchor="middle" fontFamily={HAI_TYPE.sans} fontWeight={800}
              fontSize={lbl * 1.2} fill={pc === home && homeOn > 0.5 ? SPARK_TEXT : CLAUDE.INK}>{NOTES[pc]}</text>
          </g>
        );
      })}
      {BLACK.map((pc) => {
        const left = whiteIdx(pc - 1);
        return <rect key={pc} x={(left + 1) * ww - ww * 0.3 - 2} y={0} width={ww * 0.6} height={KH * 0.6} rx={6} fill={CLAUDE.INK} opacity={0.85} />;
      })}
      <circle cx={whiteIdx(home) * ww + ww / 2 - 2} cy={KH * 0.8} r={ww * 0.26} fill="none" stroke={SPARK_TEXT} strokeWidth={portrait ? 8 : 7 * U} opacity={homeOn} />
      {portrait ? null : <text x={whiteIdx(home) * ww + ww / 2 - 2} y={KH * 0.8 + lbl * 0.36} textAnchor="middle" fontFamily={HAI_TYPE.sans} fontWeight={800}
        fontSize={lbl * 0.8} fill={SPARK_TEXT} opacity={homeOn}>HOME</text>}
    </svg>
  );
  const scaleCard = (name: string, notes: string[], homeNote: string, o: number, lit: boolean) => (
    <div style={{ opacity: o, background: CLAUDE.CARD, border: `2px solid ${lit ? SPARK_TEXT : CLAUDE.BORDER}`, borderRadius: 14 * U,
      padding: portrait ? '22px 28px' : `${20 * U}px ${26 * U}px`, width: portrait ? CW : CW * 0.33, boxSizing: 'border-box' }}>
      <Caps size={lbl} color={CLAUDE.INK}>{name}</Caps>
      <div style={{ fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.body : 40 * U, color: CLAUDE.INK, marginTop: portrait ? 10 : 10 * U, whiteSpace: 'nowrap' }}>
        {notes.map((n, i) => <span key={i} style={{ color: n === homeNote ? SPARK_TEXT : CLAUDE.INK, fontWeight: n === homeNote ? 700 : 400, marginRight: portrait ? 22 : 18 * U }}>{n}</span>)}
      </div>
    </div>
  );
  const cards = (
    <>
      {scaleCard('C MAJOR · HOME C', ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'C', op(sC), op(sAh) < 0.5)}
      {scaleCard('A MINOR · HOME A', ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'A', op(sAm), op(sAh) > 0.5)}
    </>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        {keyboard}
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.46, display: 'flex', flexDirection: 'column', gap: height * 0.018 }}>{cards}</div>
        <Caps size={lbl} color={SPARK_TEXT} style={{ position: 'absolute', left: PAD_X, top: height * 0.72, opacity: op(sWrong) }}>SAME 7 NOTES · APPS MIX THEM UP</Caps>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      {keyboard}
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.67, top: KY, display: 'flex', flexDirection: 'column', gap: 26 * U }}>
        {cards}
        <Caps size={lbl} color={SPARK_TEXT} style={{ opacity: op(sWrong) }}>SAME SEVEN NOTES · APPS MIX THEM UP</Caps>
      </div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
