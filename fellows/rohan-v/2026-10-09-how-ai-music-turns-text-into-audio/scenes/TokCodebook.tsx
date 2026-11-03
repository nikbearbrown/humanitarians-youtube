import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { TOK, PhoneBaseline, Label, TokenBox, shapePath, SHAPE_LO, SHAPE_HI, fmt } from './tokens/tokKit';

/**
 * TokCodebook — B02 of "How AI Music Generators Turn Text Into Audio."
 *
 * One frame of the test piece (its 256 MDCT coefficients, shown as a 64-band log-magnitude shape)
 * next to the codebook: 1,024 learned entries (a 32 x 32 grid; six of the most-used entries drawn as
 * their own shapes). The entry the codec chose for this frame is that frame's token: its shape (the
 * one-codebook reconstruction) overlays the frame, and its number is the run's token. The row below
 * is the next eight frames' first tokens, from the same run.
 *
 *   codec / frames  "the job of a codec" / "short frames"   frame strip
 *   codebook        "compares each frame with a codebook"    grid + example entries
 *   learned         "learned from music"                     caption
 *   closest         "number of the closest one"              chosen entry lit, overlay
 *   token           "That number is a token"                 token box
 *   range           "between zero and one thousand"          token row + range note
 */

export const tokCodebookSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('A Frame Becomes a Token'),
  sparkLine: z.string().default('Find the closest shape. Keep its number.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type TokCodebookProps = z.infer<typeof tokCodebookSchema>;

export const TokCodebook: React.FC<TokCodebookProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tCodec = at('codec', 0.02), tFrames = at('frames', 0.1), tBook = at('codebook', 0.25), tLearn = at('learned', 0.38);
  const tClose = at('closest', 0.5), tTok = at('token', 0.62), tRange = at('range', 0.75);
  const headIn = sp(0);
  const sCodec = sp(tCodec), sFrames = sp(tFrames), sBook = sp(tBook), sLearn = sp(tLearn), sClose = sp(tClose), sTok = sp(tTok), sRange = sp(tRange);
  const overlay = ramp(tClose, tClose + 0.06);
  const sparkIn = sp(clamp(tRange + 0.07, 0, 0.97));
  const lbl = portrait ? T.label * 0.72 : 22 * U;

  const tok0: number = TOK.tokens.first[0][0];
  const row: number[] = TOK.tokens.first.map((r: number[]) => r[0]);
  const frameShape: number[] = TOK.frame.orig;
  const entryShape: number[] = TOK.frame.stages['1'];

  // frame panel
  const FW = portrait ? CW : CW * 0.36, FH = portrait ? height * 0.13 : height * 0.3;
  const FX = PAD_X, FY = portrait ? height * 0.255 : height * 0.33;
  const framePanel = (
    <div style={{ position: 'absolute', left: FX, top: FY, opacity: op(sFrames) }}>
      <Label text={op(sClose) > 0.5 ? 'THIS FRAME + ITS CLOSEST ENTRY' : 'ONE FRAME: 10.7 MS OF SOUND'} size={lbl} color={CLAUDE.INK} style={{ marginBottom: lbl * 0.6 }} />
      <svg width={FW} height={FH} style={{ display: 'block', overflow: 'visible' }}>
        <rect x={0} y={0} width={FW} height={FH} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
        <path d={shapePath(frameShape, FW, FH, SHAPE_LO, SHAPE_HI, true)} fill={CLAUDE.INK} opacity={0.42} />
        <path d={shapePath(frameShape, FW, FH, SHAPE_LO, SHAPE_HI)} fill="none" stroke={CLAUDE.INK} strokeWidth={3} />
        <path d={shapePath(entryShape, FW, FH, SHAPE_LO, SHAPE_HI, false, overlay)} fill="none" stroke={SPARK_TEXT} strokeWidth={5} strokeDasharray="12 8" />
      </svg>
      <div style={{ display: 'flex', justifyContent: 'space-between', width: FW, marginTop: 8 }}>
        <Label text="LOW" size={lbl * 0.95} /><Label text="PITCH →" size={lbl * 0.95} /><Label text="12 KHZ" size={lbl * 0.95} />
      </div>
    </div>
  );

  // codebook grid
  const GW = portrait ? CW * 0.36 : CW * 0.24;
  const cell = GW / 32;
  const GX = portrait ? PAD_X : PAD_X + CW * 0.43, GY = portrait ? height * 0.475 : height * 0.33;
  const chosen = tok0;
  const grid = (
    <div style={{ position: 'absolute', left: GX, top: GY, opacity: op(sBook) }}>
      <Label text="CODEBOOK: 1,024 ENTRIES" size={lbl} color={CLAUDE.INK} style={{ marginBottom: lbl * 0.6 }} />
      <svg width={GW} height={GW} style={{ display: 'block', overflow: 'visible' }}>
        <rect x={0} y={0} width={GW} height={GW} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
        {Array.from({ length: 1024 }, (_, k) => {
          const x = (k % 32) * cell, y = Math.floor(k / 32) * cell;
          const hit = k === chosen && op(sClose) > 0.4;
          const k2 = clamp(op(sBook) * 1024 / 300 - k / 300, 0, 1);
          return <rect key={k} x={x + cell * 0.22} y={y + cell * 0.22} width={cell * 0.56} height={cell * 0.56}
            fill={hit ? SPARK_TEXT : CLAUDE.INK} opacity={hit ? 1 : 0.6 * k2} />;
        })}
        {op(sClose) > 0.4 ? <rect x={(chosen % 32) * cell - cell * 1.2} y={Math.floor(chosen / 32) * cell - cell * 1.2} width={cell * 3.4} height={cell * 3.4}
          fill="none" stroke={SPARK_TEXT} strokeWidth={4} rx={6} /> : null}
      </svg>
      {portrait ? null : <Label text="EACH ONE A TYPICAL SOUND SHAPE, LEARNED FROM MUSIC" size={lbl * 0.95} opacity={op(sLearn)} style={{ marginTop: 10 }} />}
    </div>
  );

  // example entries
  const ex: number[][] = TOK.codebook_examples;
  const EW = portrait ? (CW * 0.55 - 20) / 2 : CW * 0.11, EH = EW * 0.55;
  const EX = portrait ? PAD_X + CW * 0.45 : PAD_X + CW * 0.77, EY = GY + lbl * 1.6;
  const examples = (
    <div style={{ position: 'absolute', left: EX, top: EY, display: 'grid', gridTemplateColumns: `repeat(2, ${EW}px)`, gap: portrait ? 20 : 16 * U, opacity: 0.5 * op(sBook) + 0.5 * op(sLearn) }}>
      {ex.map((v, i) => (
        <svg key={i} width={EW} height={EH} style={{ overflow: 'visible' }}>
          <rect x={0} y={0} width={EW} height={EH} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
          <path d={shapePath(v, EW, EH, SHAPE_LO, SHAPE_HI)} fill="none" stroke={CLAUDE.INK_SOFT} strokeWidth={2.5} />
        </svg>
      ))}
    </div>
  );

  const tokenRow = (size: number) => (
    <div style={{ display: 'flex', alignItems: 'center', gap: size * 0.5, flexWrap: 'wrap', opacity: portrait ? op(sTok) : 0.5 + 0.5 * op(sTok) }}>
      <Label text={portrait ? 'TOKEN' : 'TOKEN (0 TO 1,023)'} size={lbl} color={SPARK_TEXT} />
      {row.slice(0, portrait ? 4 : 8).map((t, i) => <TokenBox key={i} n={t} size={size} accent={i === 0} opacity={i === 0 ? 1 : clamp(op(sRange) * 8 - i, 0, 1)} />)}
      <span style={{ opacity: op(sRange), fontFamily: HAI_TYPE.mono, fontSize: size, color: CLAUDE.INK_SOFT }}>…</span>
    </div>
  );
  const rangeNote = <Label text={`EVERY FRAME → ONE NUMBER, 0 TO ${fmt(1023)}`} size={lbl} opacity={op(sRange)} />;

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        {framePanel}{grid}{examples}
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.745 }}>{tokenRow(T.label * 0.7)}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.755 - 6, opacity: 0 }}>{rangeNote}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn * op(sCodec)} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      {framePanel}{grid}{examples}
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.79 }}>{tokenRow(28 * U)}</div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
