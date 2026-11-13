import React from 'react';
import { AbsoluteFill, random } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { RECS, Caps, Stat, BigStat, PhoneBaseline, LandBaseline } from './recs/recsKit';

/**
 * RecsGrid — B02 of "How Spotify Picks Songs."
 *
 * The listener x song grid. The drawn corner is an ILLUSTRATION (seeded, about as sparse as recs.py's grid);
 * the sizes are the run's: 3,000 listeners, 1,600 songs, 24 taste numbers each. Then matrix factorisation: one
 * listener's list and one song's list (illustrative values) multiply into a score.
 *
 *   grid / empty / made / fills / numbers / score
 */

export const recsGridSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · TECH CONCEPTS'),
  title: z.string().default("A Grid That's Mostly Empty"),
  sparkLine: z.string().default('Two short lists of numbers, one score.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type RecsGridProps = z.infer<typeof recsGridSchema>;

export const RecsGrid: React.FC<RecsGridProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tGrid = at('grid', 0.02), tEmpty = at('empty', 0.15), tMade = at('made', 0.3), tFills = at('fills', 0.5), tNum = at('numbers', 0.68), tScore = at('score', 0.82);
  const headIn = sp(0);
  const sGrid = sp(tGrid), fillIn = ramp(tEmpty, tEmpty + 0.08), sMade = sp(tMade), sFills = sp(tFills), sNum = sp(tNum), sScore = sp(tScore);
  const sparkIn = sp(clamp(Math.min(tScore + 0.06, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;

  const rows = portrait ? 8 : 18, cols = portrait ? 18 : 30;
  const GW = portrait ? CW : CW * 0.52;
  const cell = GW / cols;
  const grid = (
    <svg width={GW} height={rows * cell} style={{ display: 'block', opacity: op(sGrid) }}>
      {Array.from({ length: rows * cols }, (_, i) => {
        const r = Math.floor(i / cols), c = i % cols;
        const played = random(`g-${i}`) < 0.06;
        const lit = played ? clamp(fillIn * 3 - random(`d-${i}`) * 2, 0, 1) : 0;
        const fx = op(sFills) * (played ? 0 : random(`f-${i}`) * 0.5);
        return <rect key={i} x={c * cell + 1.5} y={r * cell + 1.5} width={cell - 3} height={cell - 3} rx={cell * 0.18}
          fill={played ? CLAUDE.INK : fx > 0.3 ? CLAUDE.INK_SOFT : CLAUDE.CARD} fillOpacity={played ? 0.2 + 0.8 * lit : fx > 0.3 ? 0.35 + fx : 1}
          stroke={CLAUDE.BORDER} strokeWidth={1.5} />;
      })}
    </svg>
  );
  const axes = (
    <div style={{ display: 'flex', flexWrap: 'wrap', maxWidth: GW, gap: portrait ? '8px 30px' : 30 * U, marginTop: portrait ? 14 : 12 * U }}>
      <Caps size={lbl} color={CLAUDE.INK}>{portrait ? 'ROWS: LISTENERS' : 'DOWN: LISTENERS'}</Caps>
      <Caps size={lbl} color={CLAUDE.INK}>{portrait ? 'COLUMNS: SONGS' : 'ACROSS: SONGS'}</Caps>
      <Caps size={lbl} style={{ opacity: op(sGrid) }}>ILLUSTRATION</Caps>
    </div>
  );
  const big = portrait ? T.title * 0.85 : 70 * U;
  const sizes = (
    <div style={{ display: 'flex', gap: portrait ? 60 : 50 * U, opacity: 0.3 + 0.7 * op(sMade) }}>
      <BigStat value={RECS.nUsers.toLocaleString('en-US')} label="LISTENERS" size={big} lbl={lbl} />
      <BigStat value={RECS.nSongs.toLocaleString('en-US')} label="SONGS" size={big} lbl={lbl} />
    </div>
  );
  const nums = (seed: string, n: number, h: number, w: number, col: string, o: number) => (
    <svg width={w} height={h}>
      {Array.from({ length: n }, (_, i) => {
        const v = random(`${seed}${i}`) * 2 - 1;
        const bh = Math.abs(v) * h * 0.45 * o;
        return <rect key={i} x={(i * w) / n + 1} y={v > 0 ? h / 2 - bh : h / 2} width={w / n - 2} height={Math.max(1, bh)} fill={col} />;
      })}
      <line x1={0} x2={w} y1={h / 2} y2={h / 2} stroke={CLAUDE.BORDER} strokeWidth={2} />
    </svg>
  );
  const VW = portrait ? CW * 0.56 : CW * 0.26, VH = portrait ? 120 : 90 * U;
  const vectors = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 16 : 14 * U, opacity: 0.3 + 0.7 * op(sNum) }}>
      <Caps size={lbl} color={CLAUDE.INK}>{`${RECS.k} HIDDEN TASTE NUMBERS EACH`}</Caps>
      <div style={{ display: 'flex', alignItems: 'center', gap: portrait ? 20 : 18 * U }}>
        <Caps size={lbl} style={{ width: portrait ? 320 : 190 * U }}>A LISTENER</Caps>{nums('u', RECS.k, VH, VW, CLAUDE.INK, op(sNum))}
      </div>
      <div style={{ display: 'flex', alignItems: 'center', gap: portrait ? 20 : 18 * U }}>
        <Caps size={lbl} style={{ width: portrait ? 320 : 190 * U }}>A SONG</Caps>{nums('s', RECS.k, VH, VW, SPARK_TEXT, op(sNum))}
      </div>
      <div style={{ opacity: op(sScore), fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.body * 1.02 : 44 * U, color: CLAUDE.INK }}>
        {portrait ? 'The score: their match' : 'Score: how well the two lists match'}
      </div>
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.178, width: CW, height: height * 0.667, display: 'flex', flexDirection: 'column', justifyContent: 'space-evenly' }}>
          <div>{grid}{axes}</div>
          <div>{sizes}</div>
          <div>{vectors}</div>
        </div>
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.25 }}>{grid}{axes}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.58, top: height * 0.25 }}>{sizes}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.58, top: height * 0.45 }}>{vectors}</div>
      <LandBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
