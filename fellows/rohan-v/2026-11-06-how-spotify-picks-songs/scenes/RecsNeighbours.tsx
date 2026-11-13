import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { RECS, GENRE_COL, Caps, Stat, BigStat, PhoneBaseline, LandBaseline } from './recs/recsKit';

/**
 * RecsNeighbours — B03 of "How Spotify Picks Songs."
 *
 * The taste map: all 1,600 songs placed by their learned vectors (recs.py, first two principal components).
 * The dots start grey; at "eighty-four" they take their genre colours, which the model never saw, and the
 * clusters are already there. Then the run's example song and its five nearest songs (cosine similarity), and
 * the measured share of nearest songs in the same genre.
 *
 *   never / five / eighty / same / point / cosine
 */

export const recsNeighboursSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · TECH CONCEPTS'),
  title: z.string().default('It Found the Genres Itself'),
  sparkLine: z.string().default('Played by the same people, so close together.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type RecsNeighboursProps = z.infer<typeof recsNeighboursSchema>;

export const RecsNeighbours: React.FC<RecsNeighboursProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tNever = at('never', 0.02), tFive = at('five', 0.2), tEighty = at('eighty', 0.38), tPoint = at('point', 0.7), tCos = at('cosine', 0.85);
  const headIn = sp(0);
  const dotsIn = ramp(tNever, tNever + 0.1), colour = sp(tEighty), sFive = sp(tFive), sPoint = sp(tPoint), sCos = sp(tCos);
  const sparkIn = sp(clamp(Math.min(tCos + 0.05, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;

  const S = portrait ? CW * 0.7 : height * 0.6;
  const pts = RECS.pca as unknown as number[][];
  const ex = RECS.exampleSong as any;
  const px = (v: number) => S / 2 + v * S * 0.46, py = (v: number) => S / 2 - v * S * 0.46;
  const exP = pts[ex.id], nn = (ex.nearest as any[]).map((n) => pts[n[0]]);
  const map = (
    <svg width={S} height={S} style={{ display: 'block', overflow: 'visible' }}>
      <rect x={0} y={0} width={S} height={S} rx={20} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
      {pts.map((p, i) => {
        const g = RECS.genres[p[2]];
        const o = clamp(dotsIn * 1.6 - (i % 97) / 97 * 0.6, 0, 1);
        return <circle key={i} cx={px(p[0])} cy={py(p[1])} r={portrait ? 7 : 6 * U} fill={colour > 0.02 ? GENRE_COL[g] : CLAUDE.GHOST}
          fillOpacity={(0.35 + 0.5 * colour) * o} />;
      })}
      {nn.map((p, i) => (
        <line key={`l${i}`} x1={px(exP[0])} y1={py(exP[1])} x2={px(p[0])} y2={py(p[1])} stroke={CLAUDE.INK} strokeWidth={portrait ? 4 : 3 * U} opacity={op(sFive)} />
      ))}
      {nn.map((p, i) => <circle key={`n${i}`} cx={px(p[0])} cy={py(p[1])} r={portrait ? 14 : 11 * U} fill="none" stroke={CLAUDE.INK} strokeWidth={portrait ? 4 : 3 * U} opacity={op(sFive)} />)}
      <circle cx={px(exP[0])} cy={py(exP[1])} r={portrait ? 20 : 16 * U} fill={SPARK_TEXT} stroke={CLAUDE.CARD} strokeWidth={4} opacity={op(sFive)} />
    </svg>
  );
  const legend = (
    <div style={{ display: 'flex', flexWrap: 'wrap', gap: portrait ? '14px 30px' : `${10 * U}px ${24 * U}px`, maxWidth: portrait ? CW : CW * 0.4, opacity: op(colour) }}>
      {RECS.genres.map((g) => (
        <span key={g} style={{ display: 'flex', alignItems: 'center', gap: portrait ? 10 : 8 * U }}>
          <span style={{ width: portrait ? 26 : 20 * U, height: portrait ? 26 : 20 * U, borderRadius: '50%', background: GENRE_COL[g] }} />
          <Caps size={lbl} color={CLAUDE.INK}>{g.toUpperCase()}</Caps>
        </span>
      ))}
    </div>
  );
  const big = portrait ? T.title * 0.95 : 84 * U;
  const stat = (
    <div style={{ opacity: 0.3 + 0.7 * op(colour) }}>
      <BigStat value={`${Math.round(RECS.sameGenre * 100)}%`} label={portrait ? 'NEAREST 5: SAME GENRE' : "A SONG'S 5 NEAREST: SAME GENRE"} size={big} lbl={lbl} accent />
      <div style={{ marginTop: portrait ? 10 : 10 * U }}><Caps size={lbl}>{`CHANCE ALONE: ${Math.round(100 / RECS.genres.length)}%`}</Caps></div>
    </div>
  );
  const VA = portrait ? 260 : 210 * U;
  const cosine = (
    <div style={{ display: 'flex', alignItems: 'center', gap: portrait ? 24 : 24 * U, opacity: 0.3 + 0.7 * op(sPoint) }}>
      <svg width={VA} height={VA * 0.7}>
        <line x1={10} y1={VA * 0.65} x2={VA * 0.95} y2={VA * 0.2} stroke={CLAUDE.INK} strokeWidth={6} strokeLinecap="round" />
        <line x1={10} y1={VA * 0.65} x2={VA * 0.9} y2={VA * 0.06} stroke={SPARK_TEXT} strokeWidth={6} strokeLinecap="round" />
        <path d={`M ${VA * 0.42} ${VA * 0.44} A ${VA * 0.36} ${VA * 0.36} 0 0 0 ${VA * 0.4} ${VA * 0.36}`} fill="none" stroke={CLAUDE.INK_SOFT} strokeWidth={4} />
      </svg>
      <div>
        <div style={{ fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.body * 1.02 : 44 * U, color: CLAUDE.INK }}>Same direction</div>
        <div style={{ opacity: op(sCos) }}><Caps size={lbl} color={SPARK_TEXT}>COSINE SIMILARITY</Caps></div>
      </div>
    </div>
  );
  const top = (
    <Caps size={lbl} color={CLAUDE.INK} style={{ opacity: op(sp(tNever)) }}>{portrait ? '1,600 SONGS BY TASTE NUMBERS' : 'EVERY SONG, PLACED BY ITS TASTE NUMBERS (NO GENRE GIVEN)'}</Caps>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.178, width: CW, height: height * 0.667, display: 'flex', flexDirection: 'column', justifyContent: 'space-evenly' }}>
          <div>{top}<div style={{ marginTop: 14 }}>{map}</div><div style={{ marginTop: 24 }}>{legend}</div></div>
          <div>{stat}</div>
        </div>
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.215 }}>{top}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.245 }}>{map}</div>
      <div style={{ position: 'absolute', left: PAD_X + S + CW * 0.05, top: height * 0.25 }}>{stat}</div>
      <div style={{ position: 'absolute', left: PAD_X + S + CW * 0.05, top: height * 0.47 }}>{legend}</div>
      <div style={{ position: 'absolute', left: PAD_X + S + CW * 0.05, top: height * 0.62 }}>{cosine}</div>
      <LandBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
