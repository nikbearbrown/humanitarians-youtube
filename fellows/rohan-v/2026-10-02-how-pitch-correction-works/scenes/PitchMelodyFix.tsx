import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import {
  useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPRING_SNAP, SPARK_TEXT, PHONE,
} from '../lib/cueKit';
import { PITCH, Lanes, TargetBlocks, curvePath, Chip, listening } from './pitch/pitchKit';

/**
 * PitchMelodyFix — B04 of "How Pitch Correction Works."
 *
 * The measured beat. A piano roll of the whole test melody: dashed blocks are the
 * notes as written; the ink curve is the pitch my detector MEASURED in the sung
 * (synthesised) melody — scoops into every note, vibrato on the held ones; the
 * spark curve is the pitch measured AGAIN on the corrected audio (instant retune,
 * C major). The two numbers are the run's own: mean distance from the nearest
 * correct note before, and after re-measurement. Then the beat's audio plays the
 * two files themselves (mix_listen.py), and a playhead runs along whichever curve
 * is being heard.
 *
 *   wrote    "So I wrote one"          the roll + TEST SIGNAL label
 *   seven    "seven sung notes"        the written notes; the sung curve draws
 *   scoop    "scoop up into every note" the scoop is called out
 *   average  "On average"              BEFORE number
 *   measured "detector measured…"      the measurement rate
 *   pulled   "pulled each note"        the corrected curve draws
 *   again    "Measured again…"         AFTER number
 *   listen   (props.listen windows)    playhead + "now playing" badge
 */

export const pitchMelodyFixSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('I Built One and Measured It'),
  testLabel: z.string().default('TEST SIGNAL · a synthesised voice, not a recording'),
  sparkLine: z.string().default('Thirty-seven cents out, then under three.'),
  listen: z.array(z.object({ label: z.string(), from: z.number(), to: z.number() })).optional(),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type PitchMelodyFixProps = z.infer<typeof pitchMelodyFixSchema>;

const M0 = 57.5, M1 = 70.5;

export const PitchMelodyFix: React.FC<PitchMelodyFixProps> = ({ eyebrow, title, testLabel, sparkLine, listen, cues }) => {
  const { frame, D, width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);
  const run = PITCH.runs.instant;
  const t1 = PITCH.melody[PITCH.melody.length - 1].end + 0.04;

  const tWrote = at('wrote', 0.0), tSeven = at('seven', 0.064), tScoop = at('scoop', 0.135);
  const tAvg = at('average', 0.234), tMeas = at('measured', 0.318), tPull = at('pulled', 0.416);
  const tAgain = at('again', 0.478), tListen = at('listen', 0.576);

  const headIn = sp(0);
  const sShell = sp(tWrote);
  const sung = ramp(tSeven, tAvg);
  const sScoop = sp(tScoop);
  const sAvg = sp(tAvg, SPRING_SNAP);
  const sMeas = sp(tMeas);
  const fixed = ramp(tPull, tAgain + 0.02);
  const sAgain = sp(tAgain, SPRING_SNAP);
  const sparkIn = sp(clamp(tListen, 0, 0.97));
  const now = listening(listen, frame / D);
  const hearSung = now?.label === 'AS SUNG';
  const hearFix = now && !hearSung;

  // ── geometry ──
  const LABEL_W = portrait ? 120 * U : 80 * U;
  const RX = PAD_X + LABEL_W;
  const RW = portrait ? CW - LABEL_W : CW * 0.7 - LABEL_W;
  const RY = portrait ? height * 0.255 : height * 0.29;
  const RH = portrait ? height * 0.3 : height * 0.5;
  const lbl = portrait ? T.label * 0.85 : 22 * U;

  const sungD = curvePath(PITCH.sung, 0, t1, M0, M1, RW, RH, sung);
  const fixD = curvePath(run.after, 0, t1, M0, M1, RW, RH, fixed);
  const firstOnsetX = ((PITCH.melody[0].start + 0.02) / t1) * RW;

  const big = (label: string, value: string, accent: boolean, o: number) => (
    <div style={{ opacity: o, transform: `translateY(${(1 - o) * 14}px)`, marginBottom: portrait ? 0 : 34 * U, flex: 1 }}>
      <div style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 700, letterSpacing: 1.2, color: CLAUDE.INK_SOFT }}>{label}</div>
      <div style={{ fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.title * 1.05 : 72 * U, fontWeight: 700,
        color: accent ? SPARK_TEXT : CLAUDE.INK, lineHeight: 1.05 }}>{value}</div>
      <div style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 700, letterSpacing: 1, color: CLAUDE.INK_SOFT }}>
        CENTS OFF, ON AVERAGE
      </div>
    </div>
  );

  const playX = now ? now.progress * RW : 0;

  /* ── PORTRAIT (phone): the roll full width, the two numbers side by side, then what is playing. ── */
  if (portrait) {
    const L = T.label * 0.85;
    const lw = 120, rx = PAD_X + lw, rw = CW - lw, ry = height * 0.255, rh = height * 0.29;
    const m0 = 58.5, m1 = 70.5;
    const sD = curvePath(PITCH.sung, 0, t1, m0, m1, rw, rh, sung);
    const fD = curvePath(run.after, 0, t1, m0, m1, rw, rh, fixed);
    const num = (k: string, v: string, accent: boolean, o: number) => (
      <div style={{ flex: 1, opacity: o, transform: `translateY(${(1 - o) * 14}px)` }}>
        <div style={{ fontFamily: HAI_TYPE.sans, fontSize: L, fontWeight: 700, color: CLAUDE.INK_SOFT }}>{k}</div>
        <div style={{ fontFamily: HAI_TYPE.serif, fontSize: T.title * 1.2, fontWeight: 700, color: accent ? SPARK_TEXT : CLAUDE.INK, lineHeight: 1.05 }}>{v}</div>
        <div style={{ fontFamily: HAI_TYPE.sans, fontSize: L, fontWeight: 700, color: CLAUDE.INK_SOFT }}>CENTS OFF</div>
      </div>
    );
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title}
          padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.208, opacity: op(sShell) }}>
          <Chip text="TEST SIGNAL · SYNTHESISED" size={L * 0.85} />
        </div>
        <svg width={rw} height={rh} style={{ position: 'absolute', left: rx, top: ry, overflow: 'visible', opacity: op(sShell) }}>
          <rect x={0} y={0} width={rw} height={rh} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} />
          <Lanes w={rw} h={rh} m0={m0} m1={m1} labelSize={L * 0.8} labelW={lw} onlyLabels={[60, 62, 64, 65, 67, 69]} />
          <TargetBlocks t0={0} t1={t1} m0={m0} m1={m1} w={rw} h={rh} opacity={op(sp(tSeven))} />
          <path d={sD} fill="none" stroke={CLAUDE.INK} strokeWidth={hearSung ? 6 : 4} opacity={hearFix ? 0.3 : 1} />
          <path d={fD} fill="none" stroke={SPARK_TEXT} strokeWidth={hearFix ? 7 : 5} opacity={hearSung ? 0.3 : 1} />
          {now ? <line x1={now.progress * rw} x2={now.progress * rw} y1={0} y2={rh} stroke={hearSung ? CLAUDE.INK : SPARK_TEXT} strokeWidth={5} /> : null}
        </svg>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.575, width: CW, display: 'flex', gap: 40 }}>
          {num('BEFORE', PITCH.beforeMeanErr.toFixed(1), false, op(sAvg))}
          {num('AFTER', run.meanErr.toFixed(1), true, op(sAgain))}
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.725, opacity: now ? 1 : op(sMeas) }}>
          {now ? <Chip text={`▶ ${now.label}`} size={L} accent={!hearSung} />
            : <span style={{ fontFamily: HAI_TYPE.serif, fontSize: T.body * 0.9, color: CLAUDE.INK }}>measured every {(1000 * PITCH.hop / PITCH.sr).toFixed(1)} ms</span>}
        </div>
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

      <div style={{ position: 'absolute', left: RX, top: RY - lbl * 2, opacity: op(sShell) }}>
        <Chip text={portrait ? 'TEST SIGNAL · SYNTHESISED' : testLabel.toUpperCase()} size={lbl * 0.9} />
      </div>

      <svg width={RW} height={RH} style={{ position: 'absolute', left: RX, top: RY, overflow: 'visible', opacity: op(sShell) }}>
        <rect x={0} y={0} width={RW} height={RH} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} />
        <Lanes w={RW} h={RH} m0={M0} m1={M1} labelSize={lbl} labelW={LABEL_W} />
        <TargetBlocks t0={0} t1={t1} m0={M0} m1={M1} w={RW} h={RH} opacity={op(sp(tSeven))} />
        <path d={sungD} fill="none" stroke={CLAUDE.INK} strokeWidth={(hearSung ? 6 : 4) * U}
          opacity={hearFix ? 0.3 : 1} strokeLinejoin="round" />
        <path d={fixD} fill="none" stroke={SPARK_TEXT} strokeWidth={(hearFix ? 7 : 5) * U}
          opacity={hearSung ? 0.3 : 1} strokeLinejoin="round" />
        {/* the scoop, called out on the first note */}
        <g opacity={op(sScoop) * (1 - op(sAvg) * 0.6)}>
          <circle cx={firstOnsetX + 14 * U} cy={RH - ((59.4 - M0) / (M1 - M0)) * RH} r={30 * U}
            fill="none" stroke={SPARK_TEXT} strokeWidth={3} />
          <text x={firstOnsetX + 54 * U} y={RH - ((58.3 - M0) / (M1 - M0)) * RH} fontFamily={HAI_TYPE.sans}
            fontWeight={800} fontSize={lbl} fill={SPARK_TEXT}>SCOOP</text>
        </g>
        {now ? (
          <line x1={playX} x2={playX} y1={0} y2={RH} stroke={hearSung ? CLAUDE.INK : SPARK_TEXT} strokeWidth={4} />
        ) : null}
      </svg>

      {/* ── numbers ── */}
      <div style={{
        position: 'absolute', left: portrait ? PAD_X : PAD_X + CW * 0.74,
        top: portrait ? RY + RH + 70 * U : RY, width: portrait ? CW : CW * 0.26,
        display: portrait ? 'flex' : 'block', gap: 30 * U,
      }}>
        {big('BEFORE', PITCH.beforeMeanErr.toFixed(1), false, op(sAvg))}
        {big('AFTER, RE-MEASURED', run.meanErr.toFixed(1), true, op(sAgain))}
      </div>
      {!portrait ? (
        <div style={{ position: 'absolute', left: PAD_X + CW * 0.74, top: RY + RH - 60 * U, width: CW * 0.26,
          opacity: op(sMeas) * (now ? 0 : 1), fontFamily: HAI_TYPE.serif, fontSize: 24 * U, color: CLAUDE.INK, lineHeight: 1.35 }}>
          pitch measured every {(1000 * PITCH.hop / PITCH.sr).toFixed(1)} ms
        </div>
      ) : null}

      {/* ── now playing ── */}
      {now ? (
        <div style={{ position: 'absolute', left: portrait ? PAD_X : PAD_X + CW * 0.74,
          top: portrait ? height * 0.71 : RY + RH - 70 * U }}>
          <Chip text={`▶ NOW PLAYING: ${now.label}`} size={portrait ? T.label * 0.85 : 26 * U} accent={!hearSung} />
        </div>
      ) : null}

      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height}
        portrait={portrait} top={portrait ? height * 0.8 : undefined} fontSize={portrait ? T.spark : undefined} />
    </AbsoluteFill>
  );
};
