import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { KEY, NOTES, ProfileBars, PhoneBaseline, Caps, Chip, listening } from './keys/keyKit';

/**
 * KeyChroma — B02 of "How Apps Find a Song's Key."
 *
 * Step one, on the worked example (key.py): the C major pop song's chroma, 12 rows (C at the bottom) by the
 * run's first 40 frames, darker = more of that note; then the whole song's note profile as 12 bars, the three
 * tallest (C, G, E: the run's own ranking) in terracotta. Ends with the song itself (props.listen).
 *
 *   one / fold / octave / chroma / added / bars / tallest / listen
 */

export const keyChromaSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Step One: Count the Notes'),
  sparkLine: z.string().default("Twelve bars: the song's note profile."),
  listen: z.array(z.object({ label: z.string(), from: z.number(), to: z.number() })).optional(),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type KeyChromaProps = z.infer<typeof keyChromaSchema>;

export const KeyChroma: React.FC<KeyChromaProps> = ({ eyebrow, title, sparkLine, listen, cues }) => {
  const { width, height, frame, D, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tOne = at('one', 0.0), tFold = at('fold', 0.08), tChroma = at('chroma', 0.25), tAdded = at('added', 0.32);
  const tBars = at('bars', 0.4), tTall = at('tallest', 0.58), tListen = at('listen', 0.68);
  const headIn = sp(0);
  const sGrid = sp(tFold), reveal = ramp(tFold, tFold + 0.12), sChroma = sp(tChroma), grow = ramp(tAdded, tAdded + 0.1);
  const sBars = sp(tAdded), sTall = sp(tTall);
  const now = listening(listen, frame / D);
  const sparkIn = sp(clamp(Math.min(tListen, 0.88), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;

  const chroma = KEY.pop.chroma as number[][];      // frames x 12
  const profile = KEY.pop.profile as number[];
  const top3 = profile.map((v, i) => [v, i]).sort((a, b) => b[0] - a[0]).slice(0, 3).map((x) => x[1]);

  const GW = portrait ? CW - 90 : CW * 0.5 - 70 * U, GH = portrait ? height * 0.18 : height * 0.46;
  const GX = PAD_X + (portrait ? 90 : 70 * U), GY = portrait ? height * 0.25 : height * 0.27;
  const cw = GW / chroma.length, ch = GH / 12;
  const grid = (
    <svg width={GW} height={GH} style={{ position: 'absolute', left: GX, top: GY, overflow: 'visible', opacity: op(sGrid) }}>
      <rect x={0} y={0} width={GW} height={GH} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
      {chroma.map((fr, i) => clamp(reveal * chroma.length - i, 0, 1) > 0 ? fr.map((v, k) => (
        <rect key={`${i}-${k}`} x={i * cw} y={GH - (k + 1) * ch} width={cw + 0.5} height={ch + 0.5} fill={CLAUDE.INK} opacity={Math.pow(v, 0.8) * 0.9} />
      )) : null)}
      {NOTES.map((n, k) => (k % (portrait ? 2 : 1) === 0 ? (
        <text key={n} x={-12} y={GH - (k + 0.5) * ch + lbl * 0.34} textAnchor="end" fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl * (portrait ? 1 : 0.85)}
          fill={CLAUDE.INK_SOFT}>{n}</text>) : null))}
    </svg>
  );
  const BW = portrait ? CW : CW * 0.42, BH = portrait ? height * 0.13 : height * 0.3;
  const bars = <ProfileBars values={profile} w={BW} h={BH} size={portrait ? lbl * 0.9 : lbl} grow={grow} hot={op(sTall) > 0.5 ? top3 : []} opacity={op(sBars)} />;
  const playChip = <div style={{ opacity: now ? 1 : 0 }}><Chip text={portrait ? '▶ NOW PLAYING' : `▶ NOW PLAYING: ${listen && listen[0] ? listen[0].label : ''}`} size={portrait ? T.label * 0.8 : 24 * U} accent /></div>;

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: PAD_X, top: GY - lbl * 1.7, opacity: op(sChroma) }}>CHROMA · 12 NOTE NAMES</Caps>
        {grid}
        <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: PAD_X, top: height * 0.5 - lbl * 1.7, opacity: op(sBars) }}>THE WHOLE SONG</Caps>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.5 }}>{bars}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.715 }}>{playChip}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: PAD_X, top: GY - lbl * 1.9, opacity: op(sChroma) }}>CHROMA: EVERY OCTAVE FOLDED INTO 12 NOTE NAMES</Caps>
      {grid}
      <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: PAD_X + CW * 0.58, top: GY - lbl * 1.9, opacity: op(sBars) }}>THE WHOLE SONG, ADDED UP</Caps>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.58, top: GY + GH - BH }}>{bars}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: GY + GH + 40 * U }}>{playChip}</div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
