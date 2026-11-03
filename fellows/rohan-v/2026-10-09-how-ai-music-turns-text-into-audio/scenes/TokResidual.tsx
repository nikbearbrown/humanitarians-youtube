import React from 'react';
import { AbsoluteFill, Img } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { TOK, PhoneBaseline, Label, TokenBox, shapePath, SHAPE_LO, SHAPE_HI } from './tokens/tokKit';

/**
 * TokResidual — B03 of "How AI Music Generators Turn Text Into Audio."
 *
 * Residual vector quantization on the same frame as B02: the frame's shape (ink) and the codec's
 * reconstruction from 1, then 2, then 4 codebooks (each codebook coding what the previous ones
 * missed), with that frame's four tokens. The residual sum and the token-rate arithmetic are
 * typeset (typeset_math.py), computed from the run's parameters and the verified CD rate.
 *
 *   rough / second / third / add  "One guess is rough" ... "Add the pieces"  stages 1, 2, 4
 *   frames  "ninety-four frames"   rate equation
 *   four    "With four codebooks"  bits equation
 *   cd      "nearly four hundred times"  CD comparison
 */

export const tokResidualSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default("Each Codebook Fixes the Last One's Error"),
  sparkLine: z.string().default('Add the pieces. Get closer each time.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type TokResidualProps = z.infer<typeof tokResidualSchema>;

export const TokResidual: React.FC<TokResidualProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tRough = at('rough', 0.02), tSecond = at('second', 0.1), tThird = at('third', 0.2), tAdd = at('add', 0.3);
  const tFrames = at('frames', 0.48), tFour = at('four', 0.6), tCd = at('cd', 0.8);
  const headIn = sp(0);
  const s1 = sp(tRough), s2 = sp(tSecond), s3 = sp(tThird), sAdd = sp(tAdd), sFr = sp(tFrames), sFour = sp(tFour), sCd = sp(tCd);
  const sparkIn = sp(clamp(tCd + 0.07, 0, 0.97));
  const lbl = portrait ? T.label * 0.72 : 22 * U;

  const stage = op(s3) > 0.5 ? 4 : op(s2) > 0.5 ? 2 : 1;
  const shape: number[] = (TOK.frame.stages as Record<string, number[]>)[String(stage)];
  const toks: number[] = TOK.tokens.first[0];
  const FW = portrait ? CW : CW * 0.5, FH = portrait ? height * 0.14 : height * 0.36;
  const FX = PAD_X, FY = portrait ? height * 0.255 : height * 0.31;

  const chart = (
    <div style={{ position: 'absolute', left: FX, top: FY, opacity: op(s1) }}>
      <div style={{ display: 'flex', gap: 26, marginBottom: lbl * 0.6 }}>
        <Label text="THE FRAME" size={lbl} color={CLAUDE.INK} />
        <Label text={portrait ? `${stage} CODEBOOK${stage > 1 ? 'S' : ''}` : `DECODED FROM ${stage} CODEBOOK${stage > 1 ? 'S' : ''}`} size={lbl} color={SPARK_TEXT} />
      </div>
      <svg width={FW} height={FH} style={{ display: 'block', overflow: 'visible' }}>
        <rect x={0} y={0} width={FW} height={FH} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
        <path d={shapePath(TOK.frame.orig, FW, FH, SHAPE_LO, SHAPE_HI, true)} fill={CLAUDE.INK} opacity={0.42} />
        <path d={shapePath(TOK.frame.orig, FW, FH, SHAPE_LO, SHAPE_HI)} fill="none" stroke={CLAUDE.INK} strokeWidth={3} />
        <path d={shapePath(shape, FW, FH, SHAPE_LO, SHAPE_HI)} fill="none" stroke={SPARK_TEXT} strokeWidth={5} />
      </svg>
      <div style={{ display: 'flex', alignItems: 'center', gap: 14, marginTop: lbl * 0.8 }}>
        <Label text="TOKENS" size={lbl} />
        {toks.map((t, i) => <TokenBox key={i} n={t} size={portrait ? T.label * 0.72 : 26 * U} accent={i < stage} ghost={i >= stage} />)}
      </div>
    </div>
  );
  const eqH = portrait ? T.title * 0.95 : 52 * U;
  const eqRow = (e: { src: string; aspect: number }, o: number, cap: string, h = eqH) => (
    <div style={{ opacity: o }}>
      <Label text={cap} size={lbl} style={{ marginBottom: 6 }} />
      <Img src={e.src} style={{ height: h, width: h * e.aspect, maxWidth: portrait ? CW : CW * 0.44, objectFit: 'contain', objectPosition: 'left' }} />
    </div>
  );
  const eqs = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 14 : 24 * U }}>
      {eqRow(portrait ? TOK.eq.pResidual : TOK.eq.residual, op(sAdd), portrait ? 'ONE ENTRY PER CODEBOOK' : 'ADD THE PIECES', portrait ? T.title * 2.0 : eqH)}
      {portrait ? null : eqRow(TOK.eq.rate, op(sFr), 'TOKENS PER SECOND', eqH * 0.85)}
      {portrait ? null : eqRow(TOK.eq.bits, (portrait ? op(sFr) : op(sFour)), portrait ? `${TOK.derived.tok4} TOKENS/S × 10 BITS = BITS/S` : '10 BITS PER TOKEN (1,024 ENTRIES)', portrait ? eqH : eqH * 0.85)}
      {eqRow(portrait ? TOK.eq.pCd : TOK.eq.cd, op(sCd), portrait ? 'CD KBIT/S ÷ CODEC KBIT/S' : `A CD IS ${TOK.derived.ratio}× MORE DATA`, portrait ? eqH : eqH * 0.85)}
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        {chart}
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.5 }}>{eqs}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      {chart}
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.55, top: FY - 6 * U }}>{eqs}</div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
