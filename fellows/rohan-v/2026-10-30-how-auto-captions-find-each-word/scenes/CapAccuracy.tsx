import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { CAP, Caps, Stat, WhisperTag, PhoneBaseline, LandBaseline } from './captions/capKit';

/**
 * CapAccuracy — B03 of "How Auto-Captions Find Each Word."
 *
 * The clean-speech result of captions.py: one dot per test word (238), ink where faster-whisper base wrote the
 * word right and terracotta where it did not (the count, not the positions), then the run's three numbers: words
 * right, the median start error (early), and the 90th-percentile start error.
 *
 *   built / know / base / words / early / nine
 */

export const capAccuracySchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Words Right, Slightly Early'),
  sparkLine: z.string().default('Almost every word, a quarter second early.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type CapAccuracyProps = z.infer<typeof capAccuracySchema>;

export const CapAccuracy: React.FC<CapAccuracyProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tBuilt = at('built', 0.02), tBase = at('base', 0.25), tWords = at('words', 0.38), tEarly = at('early', 0.6), tNine = at('nine', 0.78);
  const headIn = sp(0);
  const fill = ramp(tBuilt, tBase), sBase = sp(tBase), sWords = sp(tWords), sEarly = sp(tEarly), sNine = sp(tNine);
  const sparkIn = sp(clamp(Math.min(tNine + 0.06, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const C = CAP.clean;
  const wrong = C.words - C.matched;

  const cols = portrait ? 22 : 24, rows = Math.ceil(C.words / cols);
  const GW = portrait ? CW : CW * 0.55;
  const cell = GW / cols, r = cell * 0.36;
  const grid = (
    <svg width={GW} height={rows * cell} style={{ display: 'block' }}>
      {Array.from({ length: C.words }, (_, i) => {
        const bad = i >= C.matched;
        const shown = clamp(fill * C.words - i, 0, 1);
        const lit = bad ? op(sWords) : 1;
        return <circle key={i} cx={(i % cols) * cell + cell / 2} cy={Math.floor(i / cols) * cell + cell / 2} r={r}
          fill={bad && lit > 0.5 ? SPARK_TEXT : CLAUDE.INK} opacity={0.18 + 0.82 * shown} />;
      })}
    </svg>
  );
  const big = portrait ? T.title * 0.78 : 84 * U;
  const stats = (dir: 'row' | 'column') => (
    <div style={{ display: 'flex', flexDirection: dir, gap: dir === 'row' ? 0 : 48 * U, justifyContent: 'space-between', width: dir === 'row' ? CW : undefined }}>
      <Stat value={`${C.matched}/${C.words}`} label="WORDS RIGHT" size={big} opacity={0.3 + 0.7 * op(sWords)} />
      <Stat value={`${(Math.abs(C.signed_med_ms) / 1000).toFixed(2)} s`} label="EARLY, TYPICALLY" size={big} opacity={0.3 + 0.7 * op(sEarly)} accent />
      <Stat value={`${(C.p90_ms / 1000).toFixed(1)} s`} label={dir === 'row' ? 'NINE IN TEN WITHIN' : 'NINE IN TEN WORDS WITHIN'} size={big} opacity={0.3 + 0.7 * op(sNine)} />
    </div>
  );
  const key = (
    <div style={{ display: 'flex', flexWrap: 'wrap', gap: portrait ? 28 : 30 * U, alignItems: 'center' }}>
      <Caps size={lbl} color={CLAUDE.INK} style={{ opacity: 0.3 + 0.7 * fill }}>{`EACH DOT: ONE WORD (${C.words})`}</Caps>
      <Caps size={lbl} color={SPARK_TEXT} style={{ opacity: 0.3 + 0.7 * op(sWords) }}>{`WRITTEN WRONG: ${wrong}`}</Caps>
    </div>
  );
  const tag = <div style={{ opacity: 0.3 + 0.7 * op(sBase) }}><WhisperTag size={lbl} label="WHISPER BASE" /></div>;

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.2 }}>{tag}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.25 }}>{grid}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.25 + rows * cell + 20 }}>{key}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.6 }}>{stats('row')}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.25 }}>{tag}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.32 }}>{grid}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.32 + rows * cell + 22 * U }}>{key}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.62, top: height * 0.27 }}>{stats('column')}</div>
      <LandBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
