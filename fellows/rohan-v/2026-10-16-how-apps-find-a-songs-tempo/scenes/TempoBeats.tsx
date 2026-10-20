import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { EX, SHOW_S, Waveform, TimeAxis, Stat, Chip, listening, PhoneBaseline, Caps } from './tempo/tmpKit';

/**
 * TempoBeats — B01 of "How Apps Find a Song's Tempo."
 *
 * What tempo is, on the reel's own worked example: four seconds of the test set's rock groove at
 * 120 BPM (tempo.py / grooves.py), drawn as its waveform, with the true beats marked every half
 * second. Then the marks fade to ghosts: the app gets only the sound. The beat ends with the same
 * four seconds played (props.listen, mix_listen.py) and a playhead crossing the waveform.
 *
 *   counted  "counted in beats per minute"   120 BPM stat
 *   half     "every half second"             2 per second / 0.5 s apart
 *   tap      "tap your foot"                 (stats settle)
 *   groove   "four seconds of a rock groove" waveform draws
 *   marked   "with its beats marked"         beat ticks drop in
 *   only     "gets only the sound"           ticks fade to ghosts + chip
 *   listen   (props.listen)                  playhead + now-playing chip
 */

export const tempoBeatsSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('A Beat Every Half Second'),
  sparkLine: z.string().default('The app hears the sound, not the marks.'),
  listen: z.array(z.object({ label: z.string(), from: z.number(), to: z.number() })).optional(),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type TempoBeatsProps = z.infer<typeof tempoBeatsSchema>;

export const TempoBeats: React.FC<TempoBeatsProps> = ({ eyebrow, title, sparkLine, listen, cues }) => {
  const { width, height, frame, D, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tCount = at('counted', 0.03), tHalf = at('half', 0.23), tGroove = at('groove', 0.4), tMark = at('marked', 0.5);
  const tOnly = at('only', 0.6), tListen = at('listen', 0.71);
  const headIn = sp(0);
  const sCount = sp(tCount), sHalf = sp(tHalf), sWave = sp(tGroove), draw = ramp(tGroove, tGroove + 0.06);
  const ticks = ramp(tMark, tMark + 0.07), sOnly = sp(tOnly);
  const now = listening(listen, frame / D);
  const sparkIn = sp(clamp(tListen - 0.04, 0, 0.97));
  const lbl = portrait ? T.label * 0.74 : 22 * U;

  const PW = CW, PH = portrait ? height * 0.15 : height * 0.26;
  const PX = PAD_X, PY = portrait ? height * 0.255 : height * 0.29;
  const beats = EX.beats as number[];
  const env = (EX.env as number[]).slice(0, Math.max(2, Math.round((EX.env as number[]).length * draw)));
  const ghost = op(sOnly);
  const head = now ? now.progress : null;

  const panel = (
    <svg width={PW} height={PH + lbl * 2} style={{ position: 'absolute', left: PX, top: PY, overflow: 'visible', opacity: op(sWave) }}>
      <rect x={0} y={0} width={PW} height={PH} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
      <Waveform w={PW * (env.length / (EX.env as number[]).length)} h={PH} env={env} color={CLAUDE.INK_SOFT} />
      {beats.map((b, i) => {
        const k = clamp(ticks * beats.length - i, 0, 1);
        const x = (b / SHOW_S) * PW;
        return (
          <g key={i} opacity={k}>
            <line x1={x} x2={x} y1={-14} y2={PH + 4} stroke={ghost > 0.5 ? CLAUDE.GHOST : SPARK_TEXT} strokeWidth={portrait ? 5 : 4 * U}
              strokeDasharray={ghost > 0.5 ? '10 9' : undefined} opacity={1 - 0.45 * ghost} />
            <circle cx={x} cy={-14} r={portrait ? 10 : 8 * U} fill={ghost > 0.5 ? CLAUDE.GHOST : SPARK_TEXT} opacity={1 - 0.45 * ghost} />
          </g>
        );
      })}
      {head !== null ? <line x1={head * PW} x2={head * PW} y1={0} y2={PH} stroke={CLAUDE.INK} strokeWidth={portrait ? 5 : 4 * U} /> : null}
      <TimeAxis w={PW} y={PH} size={lbl} secs={[0, 1, 2, 3, 4]} span={SHOW_S} opacity={1} />
    </svg>
  );
  const stats = (dir: 'row' | 'column') => (
    <div style={{ display: 'flex', flexDirection: dir, gap: dir === 'row' ? 90 * U : height * 0.022 }}>
      <Stat value={`${EX.bpm}`} label="BEATS PER MINUTE" size={portrait ? T.title * 1.5 : 92 * U} opacity={op(sCount)} accent />
      <Stat value="2" label="BEATS EVERY SECOND" size={portrait ? T.title * 1.5 : 92 * U} opacity={op(sHalf)} />
      <Stat value="0.5 s" label="FROM ONE BEAT TO THE NEXT" size={portrait ? T.title * 1.5 : 92 * U} opacity={op(sp(tHalf + 0.03))} />
    </div>
  );
  // one slot: "only the sound" until the clip plays, then the now-playing chip replaces it
  const chips = (
    <div style={{ position: 'relative' }}>
      <div style={{ opacity: now ? 0 : op(sOnly) }}><Chip text="THE APP GETS ONLY THE SOUND" size={portrait ? T.label * 0.8 : 24 * U} /></div>
      <div style={{ position: 'absolute', left: portrait ? 0 : undefined, right: portrait ? undefined : 0, top: 0, opacity: now ? 1 : 0 }}>
        <Chip text={portrait ? '▶ NOW PLAYING' : `▶ NOW PLAYING: ${listen && listen[0] ? listen[0].label : ''}`} size={portrait ? T.label * 0.8 : 24 * U} accent /></div>
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: PAD_X, top: height * 0.205, opacity: op(sWave) }}>ROCK GROOVE · 4 SECONDS</Caps>
        {panel}
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.47, width: CW, display: 'flex', justifyContent: 'space-between' }}>
          <Stat value={`${EX.bpm}`} label="BEATS PER MINUTE" size={T.title * 1.15} opacity={op(sCount)} accent />
          <Stat value="2" label="BEATS EVERY SECOND" size={T.title * 1.15} opacity={op(sHalf)} />
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.585 }}>
          <Stat value="0.5 s" label="FROM ONE BEAT TO THE NEXT" size={T.title * 1.15} opacity={op(sp(tHalf + 0.03))} />
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.705 }}>{chips}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: PAD_X, top: PY - lbl * 3.3, opacity: op(sWave) }}>A ROCK GROOVE I GENERATED · FOUR SECONDS · BEATS MARKED</Caps>
      {panel}
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.665 }}>{stats('row')}</div>
      <div style={{ position: 'absolute', right: PAD_X, top: PY - 24 * U * 3.5 }}>{chips}</div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
