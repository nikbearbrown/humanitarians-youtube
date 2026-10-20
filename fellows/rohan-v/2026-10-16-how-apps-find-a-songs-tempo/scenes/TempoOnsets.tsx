import React from 'react';
import { AbsoluteFill, Img, staticFile } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { TMP, EX, SHOW_S, TimeAxis, Chip, PhoneBaseline, Caps, seriesPath } from './tempo/tmpKit';

/**
 * TempoOnsets — B02 of "How Apps Find a Song's Tempo."
 *
 * Step one, on the worked example's own analysis (tempo.py): the 40 mel bands of the four-second
 * rock groove (a pre-rendered image, louder = darker, low bands at the bottom), and under it the
 * onset curve the detector computed from them: at each frame, how much louder every band just got,
 * added up (spectral flux). Drum hits are spikes; the held chord between them adds almost nothing.
 * The tallest spikes are marked; they sit on the beats.
 *
 *   one    "Step one"               panels in
 *   bands  "forty frequency bands"  bands image + axis
 *   louder "how much louder"        (bands brighten)
 *   add    "Add those jumps up"     onset curve draws
 *   curve  "the onset curve"        curve label
 *   spike  "makes a spike"          tallest spikes marked
 *   chord  "A held chord"           held-sound chip
 *   flux   "spectral flux"          name chip
 */

export const tempoOnsetsSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Step One: Where New Sounds Start'),
  sparkLine: z.string().default('Every hit becomes a spike.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type TempoOnsetsProps = z.infer<typeof tempoOnsetsSchema>;

export const TempoOnsets: React.FC<TempoOnsetsProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const T = PHONE(height);

  const tOne = at('one', 0.0), tBands = at('bands', 0.1), tLouder = at('louder', 0.25), tAdd = at('add', 0.4);
  const tCurve = at('curve', 0.5), tSpike = at('spike', 0.62), tChord = at('chord', 0.72), tFlux = at('flux', 0.88);
  const headIn = sp(0);
  const sBands = sp(tBands), bright = 0.8 + 0.2 * ramp(tLouder, tLouder + 0.08);
  const draw = ramp(tAdd, tAdd + 0.1), sCurve = sp(tCurve), sSpike = sp(tSpike), sChord = sp(tChord), sFlux = sp(tFlux);
  const sparkIn = sp(clamp(tFlux + 0.04, 0, 0.97));
  const lbl = portrait ? T.label * 0.74 : 22 * U;

  const LAB = portrait ? 0 : 130 * U;
  const PX = PAD_X + LAB, PW = width - PAD_X * 2 - LAB;
  const BH = portrait ? height * 0.15 : height * 0.25, BY = portrait ? height * 0.235 : height * 0.25;
  const OH = portrait ? height * 0.12 : height * 0.2, OY = portrait ? height * 0.475 : height * 0.585;
  const onset = EX.onset as number[];
  // the tallest spikes: local maxima above 0.45, at least 0.2 s apart (they land on the beats)
  const fps: number = EX.fps;
  const peaks: number[] = [];
  onset.forEach((v, i) => {
    if (v > 0.45 && v === Math.max(...onset.slice(Math.max(0, i - 4), i + 5)) && (!peaks.length || i - peaks[peaks.length - 1] > 0.2 * fps)) peaks.push(i);
  });

  const bandsPanel = (
    <div style={{ position: 'absolute', left: PX, top: BY, width: PW, height: BH, opacity: op(sBands) }}>
      <div style={{ position: 'absolute', inset: 0, background: CLAUDE.CARD, border: `1.5px solid ${CLAUDE.BORDER}` }} />
      <Img src={staticFile(TMP.bands.src)} style={{ position: 'absolute', left: 0, top: 0, width: PW, height: BH, opacity: bright }} />
    </div>
  );
  const onsetPanel = (
    <svg width={PW} height={OH + lbl * 2} style={{ position: 'absolute', left: PX, top: OY, overflow: 'visible', opacity: 0.45 * op(sBands) + 0.55 * op(sp(tAdd)) }}>
      <rect x={0} y={0} width={PW} height={OH} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
      <path d={seriesPath(onset, PW, OH * 0.92)} transform={`translate(0 ${OH * 0.08})`} fill="none" stroke={CLAUDE.GHOST} strokeWidth={portrait ? 3 : 2 * U} opacity={0.5 * (1 - draw)} />
      <path d={seriesPath(onset, PW, OH * 0.92, draw, true)} transform={`translate(0 ${OH * 0.08})`} fill={CLAUDE.INK} opacity={0.18} />
      <path d={seriesPath(onset, PW, OH * 0.92, draw)} transform={`translate(0 ${OH * 0.08})`} fill="none" stroke={CLAUDE.INK} strokeWidth={portrait ? 4 : 3 * U} />
      {peaks.map((i, k) => (
        <circle key={k} cx={(i / (onset.length - 1)) * PW} cy={OH * 0.08 + OH * 0.92 * (1 - onset[i])} r={portrait ? 11 : 8 * U}
          fill={SPARK_TEXT} opacity={op(sSpike) * clamp(draw * onset.length - i, 0, 1)} />
      ))}
      <TimeAxis w={PW} y={OH} size={lbl} secs={[0, 1, 2, 3, 4]} span={SHOW_S} opacity={1} />
    </svg>
  );
  const chips = (
    <div style={{ display: 'flex', flexDirection: portrait ? 'column' : 'row', gap: portrait ? 20 : 22 * U, alignItems: 'flex-start' }}>
      <div style={{ opacity: op(sChord) }}><Chip text={portrait ? "HELD CHORDS: NEARLY FLAT" : "A HELD CHORD ADDS ALMOST NOTHING"} size={portrait ? T.label * 0.72 : 22 * U} /></div>
      <div style={{ opacity: op(sFlux) }}><Chip text="THIS IS SPECTRAL FLUX" size={portrait ? T.label * 0.72 : 22 * U} accent /></div>
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: PAD_X, top: BY - lbl * 1.6, opacity: op(sBands) }}>40 BANDS · LOW AT THE BOTTOM</Caps>
        {bandsPanel}
        <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: PAD_X, top: OY - lbl * 1.6, opacity: op(sCurve) }}>ONSET CURVE · HOW MUCH LOUDER</Caps>
        {onsetPanel}
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.665 }}>{chips}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: BY, width: LAB - 20 * U, height: BH, display: 'flex', flexDirection: 'column', justifyContent: 'space-between', opacity: op(sBands) }}>
        <Caps size={lbl}>HIGH</Caps><Caps size={lbl} color={CLAUDE.INK}>40 BANDS</Caps><Caps size={lbl}>LOW</Caps>
      </div>
      {bandsPanel}
      <div style={{ position: 'absolute', left: PAD_X, top: OY, width: LAB - 20 * U, opacity: op(sCurve) }}>
        <Caps size={lbl} color={CLAUDE.INK}>ONSET</Caps><Caps size={lbl} color={CLAUDE.INK}>CURVE</Caps>
      </div>
      {onsetPanel}
      <div style={{ position: 'absolute', left: PX, top: height * 0.84 }}>{chips}</div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} top={height * 0.9} />
    </AbsoluteFill>
  );
};
