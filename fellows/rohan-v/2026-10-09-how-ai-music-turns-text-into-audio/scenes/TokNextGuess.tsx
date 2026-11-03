import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { TOK, PhoneBaseline, Label, TokenBox } from './tokens/tokKit';

/**
 * TokNextGuess — B05 of "How AI Music Generators Turn Text Into Audio."
 *
 * The toy model at work on music it never heard: a real stretch of the test piece's coarse tokens,
 * and under each one (from the third on) what the trigram model guessed from the two before it;
 * hits are lit. Then the run's accuracy over the whole unseen test set against two baselines:
 * always guessing the most common token, and a blind guess (1 in 1,024).
 *
 *   model / reads   "Now the model" / "reads tokens"       token row
 *   tiny            "Mine is tiny"                          guesses fill in
 *   right           "guessed the next token right"          accuracy bar
 *   blind           "A blind guess"                         baselines
 *   trick           "That's the whole trick"                caption
 */

export const tokNextGuessSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Guess the Next Token'),
  sparkLine: z.string().default('Learning music is learning what comes next.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type TokNextGuessProps = z.infer<typeof tokNextGuessSchema>;

export const TokNextGuess: React.FC<TokNextGuessProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tModel = at('model', 0.02), tReads = at('reads', 0.1), tTiny = at('tiny', 0.2), tRight = at('right', 0.45);
  const tBlind = at('blind', 0.66), tTrick = at('trick', 0.8);
  const headIn = sp(0);
  const sModel = sp(tModel), rowIn = ramp(tReads, tReads + 0.08), guessIn = ramp(tTiny, tTiny + 0.16);
  const sRight = sp(tRight), barGrow = ramp(tRight, tRight + 0.06), sBlind = sp(tBlind), blindGrow = ramp(tBlind, tBlind + 0.06), sTrick = sp(tTrick);
  const sparkIn = sp(clamp(tTrick + 0.06, 0, 0.97));
  const lbl = portrait ? T.label * 0.72 : 22 * U;

  const ex = TOK.lm_example as { tokens: number[]; guesses: (number | null)[] };
  // the run picked this 12-token window as the one whose hit rate is closest to the overall accuracy;
  // the phone shows its last six (all of them guessed)
  const N = portrait ? 6 : 12;
  const off = portrait ? 6 : 0;
  const toks = ex.tokens.slice(off, off + N), gs = ex.guesses.slice(off, off + N);
  const box = portrait ? T.label * 0.62 : 24 * U;
  const hits = gs.filter((g, i) => g !== null && g === toks[i]).length;
  const tried = gs.filter((g) => g !== null).length;

  const stream = (
    <div style={{ opacity: op(sModel) }}>
      <div style={{ display: 'grid', gridTemplateColumns: `${portrait ? 170 : 230 * U}px repeat(${N}, auto)`, columnGap: portrait ? 10 : 12 * U, rowGap: portrait ? 18 : 16 * U, alignItems: 'center' }}>
        <Label text={portrait ? 'MUSIC' : 'THE MUSIC'} size={lbl} color={CLAUDE.INK} />
        {toks.map((t, i) => <TokenBox key={i} n={t} size={box} opacity={clamp(rowIn * N - i, 0, 1)} />)}
        <Label text={portrait ? 'GUESS' : 'MODEL GUESSED'} size={lbl} color={SPARK_TEXT} />
        {gs.map((g, i) => {
          const k = clamp(guessIn * N - i, 0, 1);
          if (g === null) return <span key={i} />;
          const hit = g === toks[i];
          return <TokenBox key={i} n={g} size={box} accent={hit} ghost={!hit} opacity={k} />;
        })}
      </div>
      <Label text={`HERE: ${hits} RIGHT OUT OF ${tried}, EACH FROM THE TWO TOKENS BEFORE IT`} size={lbl} opacity={guessIn} style={{ marginTop: portrait ? 18 : 18 * U, whiteSpace: portrait ? 'normal' : 'nowrap', width: portrait ? CW : undefined }} />
    </div>
  );

  const L = TOK.lm;
  const bars = [
    { name: portrait ? 'MY TINY MODEL' : 'MY TINY MODEL, ON MUSIC IT NEVER HEARD', v: L.accuracy, o: 0.7 + 0.3 * op(sRight), g: barGrow, accent: true },
    { name: portrait ? 'COMMONEST TOKEN' : 'ALWAYS GUESS THE COMMONEST', v: L.baseline_common, o: 0.7 + 0.3 * op(sBlind), g: blindGrow },
    { name: 'BLIND GUESS (1 IN 1,024)', v: L.blind, o: 0.7 + 0.3 * op(sBlind), g: blindGrow },
  ];
  const chart = (w: number, rowH: number, numSize: number) => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: rowH * 0.35 }}>
      {bars.map((b, i) => (
        <div key={i} style={{ opacity: b.o }}>
          <Label text={b.name} size={lbl} color={b.accent ? SPARK_TEXT : CLAUDE.INK_SOFT} />
          <div style={{ display: 'flex', alignItems: 'center', gap: 18, marginTop: 8 }}>
            <div style={{ width: w, height: rowH * 0.5, background: CLAUDE.FOOTER, border: `2px solid ${CLAUDE.GHOST}`, boxSizing: 'border-box', borderRadius: 8, position: 'relative' }}>
              <div style={{ position: 'absolute', left: 0, top: 0, height: '100%', borderRadius: 8, width: Math.max(4, (b.v / 0.2) * w * b.g),
                background: b.accent ? SPARK_TEXT : CLAUDE.INK_SOFT }} />
            </div>
            <div style={{ fontFamily: HAI_TYPE.serif, fontSize: numSize, fontWeight: 700, color: b.accent ? SPARK_TEXT : CLAUDE.INK }}>
              <span style={{ opacity: b.g }}>{(b.v * 100).toFixed(1)}%</span></div>
          </div>
        </div>
      ))}
    </div>
  );
  const trick = <Label text={portrait ? 'BIG MODELS: SAME IDEA' : 'BIG MODELS: SAME TASK, FAR MORE MUSIC'} size={lbl} color={CLAUDE.INK} opacity={op(sTrick)} />;

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.22 }}>{stream}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.44 }}>{chart(CW - 260, height * 0.07, T.title * 0.85)}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.39 }}>{trick}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.26 }}>{stream}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.5 }}>{chart(CW * 0.78, 90 * U, 52 * U)}</div>
      <div style={{ position: 'absolute', right: PAD_X, top: height * 0.445 }}>{trick}</div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
