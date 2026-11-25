import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { RECS, Caps, Stat, BigStat, PhoneBaseline, LandBaseline, SpotifyTag, Tiles } from './recs/recsKit';

/**
 * RecsExplore — B06 of "How Spotify Picks Songs."
 *
 * Exploration in recs.py: two of every ten slots go to songs few people have heard. Measured at round 0 of the
 * feedback-loop run, with and without those slots: the share of the catalogue that gets recommended at all, and
 * the share of all slots taken by the top 10% of songs.
 *
 *   two / whole / share / fell / spotify
 */

export const recsExploreSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · TECH CONCEPTS'),
  title: z.string().default('Leave Room to Explore'),
  sparkLine: z.string().default('Two slots in ten for the unknown.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type RecsExploreProps = z.infer<typeof recsExploreSchema>;

export const RecsExplore: React.FC<RecsExploreProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tTwo = at('two', 0.02), tWhole = at('whole', 0.25), tShare = at('share', 0.45), tFell = at('fell', 0.6), tSp = at('spotify', 0.82);
  const headIn = sp(0);
  const sTwo = sp(tTwo), sWhole = sp(tWhole), sShare = sp(tShare), sFell = sp(tFell), sSp = sp(tSp);
  const sparkIn = sp(clamp(Math.min(tSp + 0.05, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.86 : 22 * U;
  const a = RECS.loopPlain[0], b = RECS.loopExplore[0];

  const tile = portrait ? 74 : 74 * U, gap = portrait ? 10 : 12 * U;
  const slots = (
    <div style={{ opacity: 0.3 + 0.7 * op(sTwo) }}>
      <Caps size={lbl} color={CLAUDE.INK}>TEN PICKS</Caps>
      <div style={{ marginTop: portrait ? 12 : 10 * U }}><Tiles n={10} size={tile} gap={gap} accent={op(sTwo) > 0.5 ? [8, 9] : []} /></div>
      <div style={{ marginTop: portrait ? 10 : 8 * U, display: 'flex', flexDirection: portrait ? 'column' : 'row', gap: portrait ? 8 : 30 * U }}>
        <Caps size={lbl}>8 BEST MATCHES</Caps><Caps size={lbl} color={SPARK_TEXT}>2 FEW HAVE HEARD</Caps>
      </div>
    </div>
  );
  const pct = (v: number) => (v >= 0.99 && v < 1 ? (v * 100).toFixed(1) : String(Math.round(v * 100)));
  const pair = (lab: string, before: number, after: number, o: number, unit = '%') => (
    <div style={{ opacity: 0.3 + 0.7 * o }}>
      <Caps size={lbl} color={CLAUDE.INK}>{lab}</Caps>
      <div style={{ display: 'flex', alignItems: 'baseline', gap: portrait ? 30 : 28 * U, marginTop: portrait ? 10 : 8 * U }}>
        <BigStat value={`${pct(before)}${unit}`} label="WITHOUT" size={portrait ? T.title * 0.85 : 76 * U} lbl={lbl} />
        <svg width={portrait ? 90 : 70 * U} height={portrait ? 40 : 32 * U} style={{ alignSelf: 'center' }}>
          <path d={`M 4 ${portrait ? 20 : 16 * U} L ${portrait ? 80 : 62 * U} ${portrait ? 20 : 16 * U} M ${portrait ? 62 : 48 * U} 4 L ${portrait ? 82 : 64 * U} ${portrait ? 20 : 16 * U} L ${portrait ? 62 : 48 * U} ${portrait ? 36 : 28 * U}`}
            fill="none" stroke={CLAUDE.INK_SOFT} strokeWidth={5} strokeLinecap="round" strokeLinejoin="round" />
        </svg>
        <BigStat value={`${pct(after)}${unit}`} label={portrait ? 'EXPLORING' : 'WITH EXPLORING'} size={portrait ? T.title * 0.85 : 76 * U} lbl={lbl} accent />
      </div>
    </div>
  );
  const stats = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 40 : 40 * U }}>
      {pair(portrait ? 'CATALOGUE IN PLAY' : 'SHARE OF THE CATALOGUE RECOMMENDED', a.coverage, b.coverage, op(sWhole))}
      {pair(portrait ? 'SLOTS FOR THE TOP 10%' : 'SLOTS TAKEN BY THE TOP 10% OF SONGS', a.top10_share, b.top10_share, op(sShare) * (0.5 + 0.5 * op(sFell)))}
    </div>
  );
  const tag = <div style={{ opacity: 0.3 + 0.7 * op(sSp) }}><SpotifyTag size={lbl} label={portrait ? 'SPOTIFY TESTS THIS TOO' : 'SPOTIFY EXPERIMENTS WITH EXPLORATION'} /></div>;

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.178, width: CW, height: height * 0.667, display: 'flex', flexDirection: 'column', justifyContent: 'space-evenly' }}>
          <div>{slots}</div>
          <div>{stats}</div>
          <div>{tag}</div>
        </div>
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.27 }}>{slots}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.55 }}>{tag}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.52, top: height * 0.25 }}>{stats}</div>
      <LandBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
