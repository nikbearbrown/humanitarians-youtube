import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import {
  useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPRING_SNAP, SPARK_TEXT, PHONE,
} from '../lib/cueKit';
import { PITCH, Lanes, curvePath, Chip, listening } from './pitch/pitchKit';

/**
 * PitchRetuneSpeed — B05 of "How Pitch Correction Works."
 *
 * The same held note (the melody's last, sung flat with vibrato) corrected twice:
 * INSTANT (glide time constant 0 ms) and SLOW (250 ms). Faint ink is the sung
 * pitch; spark is the pitch RE-MEASURED on each corrected file. Instant flattens
 * the scoop and the vibrato into a step; slow keeps the wobble and lands later.
 * The error figures are each run's mean distance from target over the whole
 * melody, re-measured (pitch_demo.py). The beat's audio then plays both files,
 * and the panel being heard is lit.
 *
 *   speed     "matters most is speed"     both panels, sung curve only
 *   instantly "Pull it instantly"         instant result draws
 *   vanish    "vibrato vanish"            flat-step callout
 *   robotic   "robotic sound"             the 1998 chip
 *   slowly    "Pull it slowly"            slow result draws
 *   survives  "the vibrato survives"      vibrato bracket
 *   nineteen  "nineteen cents"            the two error figures
 *   listen    (props.listen)              now-playing panel
 */

export const pitchRetuneSpeedSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Speed Decides How Human It Sounds'),
  robotLabel: z.string().default('THE ROBOTIC “CHER EFFECT” · 1998'),
  sparkLine: z.string().default('Instant is robotic. Slow keeps the voice.'),
  listen: z.array(z.object({ label: z.string(), from: z.number(), to: z.number() })).optional(),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type PitchRetuneSpeedProps = z.infer<typeof pitchRetuneSpeedSchema>;

const M0 = 64.5, M1 = 68.5;

export const PitchRetuneSpeed: React.FC<PitchRetuneSpeedProps> = ({ eyebrow, title, robotLabel, sparkLine, listen, cues }) => {
  const { frame, D, width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);
  const last = PITCH.melody[PITCH.melody.length - 1];
  const t0 = last.start - 0.05, t1 = last.end + 0.02;

  const tSpeed = at('speed', 0.015), tInst = at('instantly', 0.135), tVan = at('vanish', 0.19);
  const tRob = at('robotic', 0.28), tSlow = at('slowly', 0.41), tSurv = at('survives', 0.475);
  const tEig = at('nineteen', 0.53), tListen = at('listen', 0.628);

  const headIn = sp(0);
  const sPanels = sp(tSpeed);
  const instD = ramp(tInst, tVan + 0.02);
  const sVan = sp(tVan);
  const sRob = sp(tRob, SPRING_SNAP);
  const slowD = ramp(tSlow, tSurv + 0.02);
  const sSurv = sp(tSurv);
  const sEig = sp(tEig, SPRING_SNAP);
  const sparkIn = sp(clamp(tListen, 0, 0.97));
  const now = listening(listen, frame / D);

  const LABEL_W = portrait ? 110 * U : 74 * U;
  const PW = portrait ? CW - LABEL_W : (CW - LABEL_W * 2 - CW * 0.05) / 2;
  const PH = portrait ? height * 0.17 : height * 0.4;
  const PY = portrait ? height * 0.27 : height * 0.33;
  const lbl = portrait ? T.label * 0.85 : 22 * U;

  const panel = (key: 'instant' | 'natural', i: number, draw: number, name: string, sub: string) => {
    const run = PITCH.runs[key];
    const x = portrait ? PAD_X + LABEL_W : PAD_X + LABEL_W + i * (PW + LABEL_W + CW * 0.05);
    const y = portrait ? PY + i * (PH + height * 0.12) : PY;
    const playing = now && ((i === 0 && now.label === 'INSTANT') || (i === 1 && now.label === 'SLOW'));
    return (
      <React.Fragment key={key}>
        <div style={{ position: 'absolute', left: x, top: y - lbl * 1.9, display: 'flex', gap: 14 * U, alignItems: 'baseline', opacity: op(sPanels) }}>
          <span style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl * 1.15, fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK }}>{name}</span>
          <span style={{ fontFamily: HAI_TYPE.mono, fontSize: lbl, fontWeight: 700, color: CLAUDE.INK_SOFT }}>{sub}</span>
        </div>
        <svg width={PW} height={PH} style={{ position: 'absolute', left: x, top: y, overflow: 'visible', opacity: op(sPanels) }}>
          <rect x={0} y={0} width={PW} height={PH} fill={CLAUDE.CARD} stroke={playing ? CLAUDE.SPARK : CLAUDE.BORDER} strokeWidth={playing ? 6 : 1.5} />
          <Lanes w={PW} h={PH} m0={M0} m1={M1} labelSize={lbl} labelW={LABEL_W} onlyLabels={[65, 66, 67]}
            highlight={{ 67: { color: CLAUDE.SPARK, strength: 0.25 } }} />
          <path d={curvePath(PITCH.sung, t0, t1, M0, M1, PW, PH, 1)} fill="none" stroke={CLAUDE.INK_SOFT} strokeWidth={3 * U} opacity={0.55} />
          <path d={curvePath(run.after, t0, t1, M0, M1, PW, PH, draw)} fill="none" stroke={SPARK_TEXT} strokeWidth={5.5 * U} strokeLinejoin="round" />
          {playing && now ? <rect x={0} y={PH + 10 * U} width={PW * now.progress} height={8 * U} rx={4 * U} fill={CLAUDE.SPARK} /> : null}
        </svg>
        <div style={{ position: 'absolute', left: x, top: y + PH + (portrait ? 26 : 30) * U, opacity: op(sEig),
          fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, color: i === 1 ? SPARK_TEXT : CLAUDE.INK }}>
          {run.meanErr.toFixed(1)} CENTS FROM TARGET{portrait ? '' : ', RE-MEASURED'}
        </div>
      </React.Fragment>
    );
  };

  // callouts
  const instX = portrait ? PAD_X + LABEL_W : PAD_X + LABEL_W;
  const slowX = portrait ? PAD_X + LABEL_W : PAD_X + LABEL_W + PW + LABEL_W + CW * 0.05;
  const slowY = portrait ? PY + PH + height * 0.12 : PY;

  /* ── PORTRAIT (phone): the two panels stacked; the callout chip sits inside each panel. ── */
  if (portrait) {
    const L = T.label * 0.85;
    const lw = 110, pw = CW - lw, ph = height * 0.145;
    const pp = (key: 'instant' | 'natural', i: number, draw: number, name: string, sub: string, chip: string, chipOn: number, accent: boolean) => {
      const run = PITCH.runs[key];
      const y = height * (i === 0 ? 0.255 : 0.5);
      const playing = now && ((i === 0 && now.label === 'INSTANT') || (i === 1 && now.label === 'SLOW'));
      return (
        <React.Fragment key={key}>
          <div style={{ position: 'absolute', left: PAD_X + lw, top: y - L * 1.55, opacity: op(sPanels), display: 'flex', gap: 16, alignItems: 'baseline' }}>
            <span style={{ fontFamily: HAI_TYPE.sans, fontSize: L, fontWeight: 800, color: CLAUDE.INK }}>{name}</span>
            <span style={{ fontFamily: HAI_TYPE.mono, fontSize: L * 0.8, fontWeight: 700, color: CLAUDE.INK_SOFT }}>{sub}</span>
          </div>
          <svg width={pw} height={ph} style={{ position: 'absolute', left: PAD_X + lw, top: y, overflow: 'visible', opacity: op(sPanels) }}>
            <rect x={0} y={0} width={pw} height={ph} fill={CLAUDE.CARD} stroke={playing ? CLAUDE.SPARK : CLAUDE.BORDER} strokeWidth={playing ? 7 : 2} />
            <Lanes w={pw} h={ph} m0={M0} m1={M1} labelSize={L * 0.8} labelW={lw} onlyLabels={[66, 67]}
              highlight={{ 67: { color: CLAUDE.SPARK, strength: 0.25 } }} />
            <path d={curvePath(PITCH.sung, t0, t1, M0, M1, pw, ph, 1)} fill="none" stroke={CLAUDE.INK_SOFT} strokeWidth={3} opacity={0.55} />
            <path d={curvePath(run.after, t0, t1, M0, M1, pw, ph, draw)} fill="none" stroke={SPARK_TEXT} strokeWidth={6} />
            {playing && now ? <rect x={0} y={ph + 10} width={pw * now.progress} height={9} rx={4} fill={CLAUDE.SPARK} /> : null}
          </svg>
          <div style={{ position: 'absolute', right: PAD_X + 14, top: y + 12, opacity: chipOn }}>
            <Chip text={chip} size={L * 0.8} accent={accent} />
          </div>
          <div style={{ position: 'absolute', left: PAD_X + lw, top: y + ph + 30, opacity: op(sEig),
            fontFamily: HAI_TYPE.sans, fontSize: L * 0.85, fontWeight: 800, color: i === 1 ? SPARK_TEXT : CLAUDE.INK }}>
            {run.meanErr.toFixed(1)} CENTS OFF
          </div>
        </React.Fragment>
      );
    };
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title}
          padX={PAD_X} height={height} width={width} portrait />
        {pp('instant', 0, instD, 'INSTANT', '0 ms', op(sRob) > 0.5 ? '“CHER EFFECT”' : 'FLAT STEP', op(sVan), op(sRob) > 0.5)}
        {pp('natural', 1, slowD, 'SLOW', '250 ms', 'VIBRATO KEPT', op(sSurv), true)}
        {now ? (
          <div style={{ position: 'absolute', left: PAD_X, top: height * 0.725 }}>
            <Chip text={`▶ ${now.label}`} size={L} accent={now.label === 'SLOW'} />
          </div>
        ) : null}
        {/* phone baseline: a hairline above the spark line from the first frame, so the content
            spans the 9:16 safe area at every Gate V sample (fill >= 55%) without adding text */}
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.782, width: CW, height: 3,
          background: CLAUDE.GHOST, opacity: op(headIn) * 0.7 }} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height}
          portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={portrait ? '' : eyebrow} title={title} inOp={headIn}
        padX={PAD_X} height={height} width={width} portrait={portrait}
        titleSize={portrait ? T.title : undefined} />

      {panel('instant', 0, instD, 'INSTANT', '0 ms')}
      {panel('natural', 1, slowD, 'SLOW', '250 ms')}

      <div style={{ position: 'absolute', left: instX + PW * 0.32, top: PY + PH * 0.12, opacity: op(sVan) * (1 - op(sSurv) * 0.5) }}>
        <Chip text="FLAT STEP" size={lbl} />
      </div>
      <div style={{ position: 'absolute', left: instX, top: (portrait ? PY + PH + 80 * U : PY + PH + 76 * U),
        opacity: op(sRob), transform: `scale(${0.9 + 0.1 * op(sRob)})`, transformOrigin: 'left center' }}>
        <Chip text={portrait ? 'THE “CHER EFFECT”' : robotLabel} size={lbl} accent />
      </div>
      <div style={{ position: 'absolute', left: slowX + PW * 0.55, top: slowY + PH * 0.12, opacity: op(sSurv) }}>
        <Chip text="VIBRATO KEPT" size={lbl} accent />
      </div>
      <div style={{ position: 'absolute', right: PAD_X, top: portrait ? height * 0.215 : height * 0.215, opacity: op(sPanels),
        display: 'flex', gap: 22 * U, fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 700, color: CLAUDE.INK_SOFT }}>
        <span>GREY: AS SUNG</span><span style={{ color: SPARK_TEXT }}>RED: CORRECTED</span>
      </div>
      {now ? (
        <div style={{ position: 'absolute', left: PAD_X, top: portrait ? height * 0.735 : height * 0.205 }}>
          <Chip text={`▶ NOW PLAYING: ${now.label}`} size={portrait ? T.label * 0.85 : 24 * U} accent={now.label === 'SLOW'} />
        </div>
      ) : null}

      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height}
        portrait={portrait} top={portrait ? height * 0.8 : undefined} fontSize={portrait ? T.spark : undefined} />
    </AbsoluteFill>
  );
};
