import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import {
  useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPRING_SNAP, SPARK_TEXT, PHONE,
} from '../lib/cueKit';
import { PITCH, Lanes, curvePath, Chip } from './pitch/pitchKit';

/**
 * PitchWrongNote — B06 of "How Pitch Correction Works."
 *
 * The catch: a corrector picks the NEAREST allowed note, not the intended one. The
 * melody's last note was written as G4 but sung 75 cents flat, which is nearer to
 * F♯4 (25 cents). Corrected with every semitone allowed (chromatic) it is re-measured
 * on F♯4 — in tune, wrong; with the key set to C major (no F♯) it is re-measured on
 * G4. Both results are the run's own (pitch_demo.py: runs.chromatic, runs.instant).
 *
 *   cant      "what it can't do"        the sung note on F4 / F♯4 / G4 lanes
 *   seventyfive "seventy-five cents below G" the distance to G
 *   closer    "closer to F sharp"       the distance to F♯ (25)
 *   every     "pick from every note"    chromatic result draws, lands on F♯4
 *   wrong     "The wrong note"          ✗ WRONG NOTE
 *   major     "in C major"              F♯4 lane struck: not in the key
 *   g         "it goes to G"            C-major result draws on G4 · ✓
 */

export const pitchWrongNoteSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default("In Tune Isn't the Same as Right"),
  sparkLine: z.string().default('It picks the nearest note, not the one you meant.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type PitchWrongNoteProps = z.infer<typeof pitchWrongNoteSchema>;

const M0 = 64.5, M1 = 68.5;

export const PitchWrongNote: React.FC<PitchWrongNoteProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);
  const last = PITCH.melody[PITCH.melody.length - 1];
  const t0 = last.start - 0.05, t1 = last.end + 0.02;
  const chrom = PITCH.runs.chromatic, major = PITCH.runs.instant;

  const tCant = at('cant', 0.015), t62 = at('seventyfive', 0.217), tClo = at('closer', 0.328);
  const tEvery = at('every', 0.45), tWrong = at('wrong', 0.68), tMaj = at('major', 0.8), tG = at('g', 0.946);

  const headIn = sp(0);
  const sCant = sp(tCant);
  const s62 = sp(t62), sClo = sp(tClo);
  const chromD = ramp(tEvery, tEvery + 0.12);
  const sWrong = sp(tWrong, SPRING_SNAP);
  const struck = ramp(tMaj, tMaj + 0.06);
  const majD = ramp(Math.min(tG, 0.93) - 0.04, Math.min(0.99, tG + 0.03));
  const sG = sp(Math.min(tG, 0.95), SPRING_SNAP);
  const sparkIn = sp(clamp(tWrong + 0.04, 0, 0.97));

  const LABEL_W = portrait ? 120 * U : 90 * U;
  const PX = PAD_X + LABEL_W;
  const PW = portrait ? CW - LABEL_W : CW * 0.6 - LABEL_W;
  const PY = portrait ? height * 0.25 : height * 0.29;
  const PH = portrait ? height * 0.27 : height * 0.5;
  const lbl = portrait ? T.label * 0.85 : 24 * U;
  const unit = PH / (M1 - M0);
  const yOf = (m: number) => PH - (m - M0) * unit;
  const det = Math.abs(last.detune_cents);
  const sungM = 67 - det / 100;

  const row = (text: string, sub: string, ok: boolean | null, o: number) => (
    <div style={{ opacity: o, transform: `translateY(${(1 - o) * 14}px)`, marginBottom: portrait ? 18 * U : 30 * U }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 14 * U }}>
        {ok !== null ? (
          <span style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl * 1.4, fontWeight: 900, color: ok ? CLAUDE.INK : SPARK_TEXT }}>
            {ok ? '✓' : '✗'}
          </span>
        ) : null}
        <span style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl * 1.05, fontWeight: 800, letterSpacing: 1, color: CLAUDE.INK }}>{text}</span>
      </div>
      <div style={{ fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.label * 0.95 : 28 * U, color: ok === false ? SPARK_TEXT : CLAUDE.INK_SOFT, marginTop: 4 * U }}>{sub}</div>
    </div>
  );

  /* ── PORTRAIT (phone): the three lanes on top, the three outcomes beneath, short strings. ── */
  if (portrait) {
    const L = T.label * 0.85;
    const lw = 120, px0 = PAD_X + lw, pw = CW - lw, py = height * 0.255, ph = height * 0.23;
    const pu = ph / (M1 - M0);
    const pyOf = (m: number) => ph - (m - M0) * pu;
    const prow = (text: string, sub: string, ok: boolean | null, o: number, top: number) => (
      <div style={{ position: 'absolute', left: PAD_X, top, width: CW, opacity: o, transform: `translateY(${(1 - o) * 14}px)` }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
          {ok !== null ? <span style={{ fontFamily: HAI_TYPE.sans, fontSize: L * 1.2, fontWeight: 900, color: ok ? CLAUDE.INK : SPARK_TEXT }}>{ok ? '✓' : '✗'}</span> : null}
          <span style={{ fontFamily: HAI_TYPE.sans, fontSize: L, fontWeight: 800, color: CLAUDE.INK }}>{text}</span>
        </div>
        <div style={{ fontFamily: HAI_TYPE.serif, fontSize: L, color: ok === false ? SPARK_TEXT : CLAUDE.INK_SOFT, marginTop: 2 }}>{sub}</div>
      </div>
    );
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title}
          padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: px0, top: height * 0.215, opacity: op(sCant),
          fontFamily: HAI_TYPE.sans, fontSize: L * 0.85, fontWeight: 700, color: CLAUDE.INK_SOFT }}>WRITTEN AS G4</div>
        <svg width={pw} height={ph} style={{ position: 'absolute', left: px0, top: py, overflow: 'visible', opacity: op(sCant) }}>
          <rect x={0} y={0} width={pw} height={ph} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} />
          <Lanes w={pw} h={ph} m0={M0} m1={M1} labelSize={L * 0.8} labelW={lw} onlyLabels={[65, 66, 67]}
            highlight={{ 66: { color: CLAUDE.SPARK, strength: op(sClo) * (1 - struck) }, 67: { color: CLAUDE.INK, strength: op(sG) * 0.12 } }}
            struck={{ 66: struck }} />
          <path d={curvePath(PITCH.sung, t0, t1, M0, M1, pw, ph, 1)} fill="none" stroke={CLAUDE.INK} strokeWidth={4} opacity={1 - 0.5 * op(sWrong)} />
          <path d={curvePath(chrom.after, t0, t1, M0, M1, pw, ph, chromD)} fill="none" stroke={SPARK_TEXT} strokeWidth={6}
            strokeDasharray={op(sG) > 0.3 ? '12 12' : undefined} opacity={1 - 0.6 * op(sG)} />
          <path d={curvePath(major.after, t0, t1, M0, M1, pw, ph, majD)} fill="none" stroke={CLAUDE.INK} strokeWidth={7} />
          <g opacity={op(s62) * (1 - op(sWrong) * 0.7)}>
            <line x1={pw * 0.88} x2={pw * 0.88} y1={pyOf(sungM)} y2={pyOf(67)} stroke={CLAUDE.INK} strokeWidth={4} />
          </g>
        </svg>
        {prow(`SUNG ${det}¢ BELOW G4`, `only ${100 - det}¢ above F♯4`, null, op(s62), height * 0.515)}
        {prow('ANY NOTE', `lands on ${chrom.lastNote.replace('#', '♯')}: wrong`, false, op(sWrong), height * 0.595)}
        {prow('KEY: C MAJOR', `no F♯ · lands on ${major.lastNote}`, true, op(sG), height * 0.675)}
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

      <div style={{ position: 'absolute', left: PX, top: PY - lbl * 2, opacity: op(sCant),
        fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 700, letterSpacing: 1.2, color: CLAUDE.INK_SOFT }}>
        THE LAST NOTE · WRITTEN AS G4
      </div>
      <svg width={PW} height={PH} style={{ position: 'absolute', left: PX, top: PY, overflow: 'visible', opacity: op(sCant) }}>
        <rect x={0} y={0} width={PW} height={PH} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} />
        <Lanes w={PW} h={PH} m0={M0} m1={M1} labelSize={lbl} labelW={LABEL_W} onlyLabels={[65, 66, 67]}
          highlight={{
            66: { color: CLAUDE.SPARK, strength: op(sClo) * (1 - struck) },
            67: { color: CLAUDE.INK, strength: op(sG) * 0.12 },
          }}
          struck={{ 66: struck }} />
        <path d={curvePath(PITCH.sung, t0, t1, M0, M1, PW, PH, 1)} fill="none" stroke={CLAUDE.INK} strokeWidth={4 * U}
          opacity={1 - 0.5 * op(sWrong)} />
        <path d={curvePath(chrom.after, t0, t1, M0, M1, PW, PH, chromD)} fill="none" stroke={SPARK_TEXT}
          strokeWidth={6 * U} strokeDasharray={op(sG) > 0.3 ? '10 10' : undefined} opacity={1 - 0.6 * op(sG)} />
        <path d={curvePath(major.after, t0, t1, M0, M1, PW, PH, majD)} fill="none" stroke={CLAUDE.INK} strokeWidth={7 * U} />
        {/* distance markers at the held part of the note */}
        <g opacity={op(s62) * (1 - op(sWrong) * 0.7)}>
          <line x1={PW * 0.86} x2={PW * 0.86} y1={yOf(sungM)} y2={yOf(67)} stroke={CLAUDE.INK} strokeWidth={3} />
          <text x={PW * 0.86 + 12 * U} y={(yOf(sungM) + yOf(67)) / 2 + lbl * 0.35} fontFamily={HAI_TYPE.sans}
            fontWeight={800} fontSize={lbl} fill={CLAUDE.INK}>{det}¢</text>
        </g>
        <g opacity={op(sClo) * (1 - op(sWrong) * 0.7)}>
          <line x1={PW * 0.74} x2={PW * 0.74} y1={yOf(sungM)} y2={yOf(66)} stroke={SPARK_TEXT} strokeWidth={3} />
          <text x={PW * 0.74 - 12 * U} y={(yOf(sungM) + yOf(66)) / 2 + lbl * 0.35} textAnchor="end" fontFamily={HAI_TYPE.sans}
            fontWeight={800} fontSize={lbl} fill={SPARK_TEXT}>{100 - det}¢</text>
        </g>
      </svg>

      <div style={{
        position: 'absolute', left: portrait ? PAD_X : PAD_X + CW * 0.64,
        top: portrait ? PY + PH + 50 * U : PY, width: portrait ? CW : CW * 0.36,
      }}>
        {row(`SUNG ${det} CENTS BELOW G4`, `only ${100 - det} cents above F♯4`, null, op(s62))}
        {row('ANY NOTE ALLOWED', `re-measured on ${chrom.lastNote.replace('#', '♯')}: in tune, wrong note`, false, op(sWrong))}
        {row('KEY SET TO C MAJOR', `F♯ not allowed · re-measured on ${major.lastNote}`, true, op(sG))}
      </div>

      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height}
        portrait={portrait} top={portrait ? height * 0.8 : undefined} fontSize={portrait ? T.spark : undefined} />
    </AbsoluteFill>
  );
};
