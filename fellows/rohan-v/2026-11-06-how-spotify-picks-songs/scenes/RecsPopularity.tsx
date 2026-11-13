import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { RECS, Caps, Stat, PhoneBaseline, LandBaseline } from './recs/recsKit';

/**
 * RecsPopularity — B05 of "How Spotify Picks Songs."
 *
 * Popularity bias in recs.py's run: the catalogue ranked from biggest hit to least played (the drawn curve is the
 * run's popularity law, 1/rank), split into its more and less popular halves; the share of all listening that
 * happens in the less popular half vs the share of the recommender's picks that come from it. Then cold start: a
 * brand-new song with no plays, in none of the 3,000 top-10 lists.
 *
 *   look / six / quarter / new / nobody / cold
 */

export const recsPopularitySchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · TECH CONCEPTS'),
  title: z.string().default('It Leans on the Hits'),
  sparkLine: z.string().default('No plays, no picks.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type RecsPopularityProps = z.infer<typeof recsPopularitySchema>;

export const RecsPopularity: React.FC<RecsPopularityProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tLook = at('look', 0.02), tSix = at('six', 0.12), tQ = at('quarter', 0.3), tNew = at('new', 0.5), tNob = at('nobody', 0.68), tCold = at('cold', 0.85);
  const headIn = sp(0);
  const sLook = sp(tLook), sSix = sp(tSix), sQ = sp(tQ), sNew = sp(tNew), sNob = sp(tNob), sCold = sp(tCold);
  const sparkIn = sp(clamp(Math.min(tCold + 0.05, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;

  const PW = portrait ? CW : CW * 0.5, PH = portrait ? height * 0.13 : height * 0.3;
  const n = 120;
  const pts = Array.from({ length: n }, (_, i) => { const r = 1 + (i / (n - 1)) * (RECS.nSongs - 1); return [i / (n - 1), 1 / r]; });
  const path = pts.map(([x, y], i) => `${i ? 'L' : 'M'} ${x * PW} ${PH - Math.pow(y, 0.35) * PH * 0.95}`).join(' ');
  const curve = (
    <svg width={PW} height={PH + lbl * 2.2} style={{ display: 'block', overflow: 'visible', opacity: op(sLook) }}>
      <rect x={PW / 2} y={0} width={PW / 2} height={PH} fill={SPARK_TEXT} opacity={0.04 + 0.04 * op(sQ)} />
      <path d={`${path} L ${PW} ${PH} L 0 ${PH} Z`} fill={CLAUDE.INK} opacity={0.3} />
      <path d={path} fill="none" stroke={CLAUDE.INK} strokeWidth={portrait ? 6 : 5 * U} />
      <line x1={0} x2={PW} y1={PH} y2={PH} stroke={CLAUDE.INK} strokeWidth={3} />
      <line x1={PW / 2} x2={PW / 2} y1={0} y2={PH} stroke={SPARK_TEXT} strokeWidth={3} strokeDasharray="10 8" />
      <text x={0} y={PH + lbl * 1.5} fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl} fill={CLAUDE.INK}>BIGGEST HITS</text>
      <text x={PW} y={PH + lbl * 1.5} textAnchor="end" fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl} fill={SPARK_TEXT}>LESS POPULAR HALF</text>
    </svg>
  );
  const BW = portrait ? CW * 0.55 : CW * 0.3, BH = portrait ? 66 : 54 * U;
  const share = (lab: string, v: number, col: string, o: number) => (
    <div style={{ opacity: 0.3 + 0.7 * o }}>
      <Caps size={lbl}>{lab}</Caps>
      <div style={{ display: 'flex', alignItems: 'center', gap: portrait ? 20 : 18 * U, marginTop: portrait ? 10 : 8 * U }}>
        <div style={{ width: BW * v * 2.5 * (0.1 + 0.9 * o), height: BH, background: col, borderRadius: BH * 0.2 }} />
        <span style={{ fontFamily: HAI_TYPE.serif, fontWeight: 700, fontSize: BH * 1.1, color: col }}>{`${Math.round(v * 100)}%`}</span>
      </div>
    </div>
  );
  const shares = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 26 : 24 * U }}>
      <Caps size={lbl} color={CLAUDE.INK}>{portrait ? 'FROM THE LESS POPULAR HALF' : 'SHARE FROM THE LESS POPULAR HALF'}</Caps>
      {share('OF ALL LISTENING', RECS.pop.tail_share_plays, CLAUDE.INK, op(sQ))}
      {share('OF ITS PICKS', RECS.pop.tail_share_recs, SPARK_TEXT, op(sSix))}
    </div>
  );
  const cold = (
    <div style={{ display: 'flex', alignItems: 'center', gap: portrait ? 26 : 26 * U, opacity: 0.3 + 0.7 * op(sNew), background: CLAUDE.CARD,
      border: `1.5px solid ${CLAUDE.BORDER}`, borderRadius: 18, padding: portrait ? '22px 28px' : `${18 * U}px ${24 * U}px` }}>
      <div style={{ width: portrait ? 90 : 70 * U, height: portrait ? 90 : 70 * U, borderRadius: 14, border: `4px dashed ${SPARK_TEXT}` }} />
      <div>
        <Caps size={lbl} color={CLAUDE.INK}>{portrait ? 'NEW SONG · 0 PLAYS' : 'A BRAND-NEW SONG · 0 PLAYS'}</Caps>
        <div style={{ opacity: 0.3 + 0.7 * op(sNob), fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.body * 1.02 : 44 * U, color: SPARK_TEXT, marginTop: portrait ? 8 : 6 * U }}>
          {`In 0 of ${RECS.nUsers.toLocaleString('en-US')} lists`}
        </div>
        <div style={{ opacity: op(sCold) }}><Caps size={lbl}>THE COLD-START PROBLEM</Caps></div>
      </div>
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.178, width: CW, height: height * 0.667, display: 'flex', flexDirection: 'column', justifyContent: 'space-evenly' }}>
          <div>{curve}</div>
          <div>{shares}</div>
          <div>{cold}</div>
        </div>
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.26 }}>{curve}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.58, top: height * 0.26 }}>{shares}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.65 }}>{cold}</div>
      <LandBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
