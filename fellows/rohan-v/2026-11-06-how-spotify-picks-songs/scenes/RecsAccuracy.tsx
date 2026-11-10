import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { RECS, Caps, PhoneBaseline, LandBaseline, Tiles } from './recs/recsKit';

/**
 * RecsAccuracy — B04 of "How Spotify Picks Songs."
 *
 * The test (recs.py): a fifth of each listener's songs hidden, ten picks asked for, and the share of listeners
 * who got at least one hidden song back: taste vectors vs "just the hits" vs random. Bars are the run's values.
 *
 *   hid / ten / seventy / hits / random
 */

export const recsAccuracySchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · TECH CONCEPTS'),
  title: z.string().default('Better Than the Charts, Just'),
  sparkLine: z.string().default('Seventy-four against sixty-five.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type RecsAccuracyProps = z.infer<typeof recsAccuracySchema>;

export const RecsAccuracy: React.FC<RecsAccuracyProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tHid = at('hid', 0.02), tTen = at('ten', 0.18), tSev = at('seventy', 0.32), tHits = at('hits', 0.55), tRand = at('random', 0.82);
  const headIn = sp(0);
  const sHid = sp(tHid), sTen = sp(tTen), grow = [sp(tSev), sp(tHits), sp(tRand)];
  const sparkIn = sp(clamp(Math.min(tRand + 0.06, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;

  const tile = portrait ? 64 : 56 * U, gap = portrait ? 12 : 10 * U;
  const test = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 16 : 14 * U }}>
      <div style={{ opacity: 0.3 + 0.7 * op(sHid) }}>
        <Caps size={lbl} color={CLAUDE.INK}>{portrait ? 'A FIFTH HIDDEN' : "A FIFTH OF EACH LISTENER'S SONGS, HIDDEN"}</Caps>
        <div style={{ marginTop: portrait ? 12 : 10 * U }}><Tiles n={10} size={tile} gap={gap} hidden={[3, 7]} /></div>
      </div>
      <div style={{ opacity: 0.3 + 0.7 * op(sTen) }}>
        <Caps size={lbl} color={CLAUDE.INK}>TEN PICKS</Caps>
        <div style={{ marginTop: portrait ? 12 : 10 * U }}><Tiles n={10} size={tile} gap={gap} accent={[2]} /></div>
        <div style={{ marginTop: portrait ? 10 : 8 * U }}><Caps size={lbl} color={SPARK_TEXT}>A HIDDEN SONG CAME BACK</Caps></div>
      </div>
    </div>
  );
  const rows = [
    { lab: portrait ? 'TASTE NUMBERS' : 'TASTE NUMBERS (MY RECOMMENDER)', v: RECS.acc.als.hit, col: SPARK_TEXT },
    { lab: 'JUST THE HITS', v: RECS.acc.popular.hit, col: CLAUDE.INK },
    { lab: 'RANDOM', v: RECS.acc.random.hit, col: CLAUDE.GHOST },
  ];
  const BW = portrait ? CW * 0.7 : CW * 0.38, BH = portrait ? 70 : 56 * U;
  const bars = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 30 : 28 * U }}>
      <Caps size={lbl} color={CLAUDE.INK}>{portrait ? 'GOT ONE BACK' : 'LISTENERS WHO GOT A HIDDEN SONG BACK'}</Caps>
      {rows.map((r, i) => (
        <div key={r.lab} style={{ opacity: 0.3 + 0.7 * op(grow[i]) }}>
          <Caps size={lbl}>{r.lab}</Caps>
          <div style={{ display: 'flex', alignItems: 'center', gap: portrait ? 20 : 18 * U, marginTop: portrait ? 10 : 8 * U }}>
            <div style={{ width: BW * r.v * (0.1 + 0.9 * op(grow[i])), height: BH, background: r.col, borderRadius: BH * 0.2 }} />
            <span style={{ fontFamily: HAI_TYPE.serif, fontWeight: 700, fontSize: BH * 1.1, color: r.col === CLAUDE.GHOST ? CLAUDE.INK_SOFT : r.col }}>
              {`${Math.round(r.v * 100)}%`}
            </span>
          </div>
        </div>
      ))}
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.178, width: CW, height: height * 0.667, display: 'flex', flexDirection: 'column', justifyContent: 'space-evenly' }}>
          <div>{test}</div>
          <div>{bars}</div>
        </div>
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.27 }}>{test}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.5, top: height * 0.27 }}>{bars}</div>
      <LandBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
