import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { SHZ, SpecImage, SpecAxes, Stat, PhoneBaseline, Chip, useSpec, fmt } from './shazam/shzKit';

/**
 * ShazamPeaks — B01 of "How Shazam Finds a Song."
 *
 * Three seconds of Song C as fingerprint.py's own spectrogram (time across, pitch up, louder =
 * darker). The image then fades back and only the constellation remains: the run's local maxima,
 * popping in left to right. Last, the same seconds as the phone heard them (0 dB cafe noise,
 * 150-4,000 Hz): the clean peaks that are still there stay solid, the lost ones go hollow. The
 * counts (values in the picture, peaks kept, peaks per second, peaks surviving) are the run's.
 *
 *   spec          "becomes a spectrogram"     image + axes
 *   time / pitch  "Time runs" / "pitch runs"  axis captions light
 *   darker        "darker means louder"       legend
 *   thrown        "thrown away"               image fades back
 *   kept          "are kept"                  peaks pop in
 *   twelve        "about twelve"              per-second stat
 *   constellation "constellation map"         2003 chip
 *   noise         "with noise as loud"        noisy image crossfades in
 *   survive       "twenty-four of these forty" survived vs lost
 */

export const shazamPeaksSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Keep Only the Loudest Points'),
  sparkLine: z.string().default('Thousands of numbers become a few stars.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type ShazamPeaksProps = z.infer<typeof shazamPeaksSchema>;

export const ShazamPeaks: React.FC<ShazamPeaksProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tSpec = at('spec', 0.02), tTime = at('time', 0.08), tPitch = at('pitch', 0.13), tDark = at('darker', 0.19);
  const tThrown = at('thrown', 0.27), tKept = at('kept', 0.36), tTwelve = at('twelve', 0.42);
  const tConst = at('constellation', 0.55), tNoise = at('noise', 0.72), tSurv = at('survive', 0.8);

  const headIn = sp(0);
  const sSpec = sp(tSpec);
  const fadeBack = ramp(tThrown, tThrown + 0.06);
  const reveal = ramp(tKept, tKept + 0.1);
  const noisy = ramp(tNoise, tNoise + 0.05);
  const sSurv = sp(tSurv);
  const sparkIn = sp(clamp(tSurv + 0.06, 0, 0.97));

  const LAB = portrait ? 175 : 92 * U;
  const SW = portrait ? CW - LAB : CW * 0.6 - LAB;
  const SH = portrait ? height * 0.25 : height * 0.5;
  const SX = PAD_X + LAB;
  const SY = portrait ? height * 0.255 : height * 0.27;
  const lbl = portrait ? T.label * 0.68 : 22 * U;
  const { x, y } = useSpec(SW, SH);

  const peaks: number[][] = SHZ.spec.peaks;
  const survived = new Set((SHZ.spec.survived as number[][]).map((p) => `${p[0]}:${p[1]}`));
  const n = peaks.length;
  const imgOp = op(sSpec) * (1 - 0.8 * fadeBack);
  const R = portrait ? 11 : 8 * U;

  const panel = (
    <>
      <div style={{ position: 'absolute', left: SX, top: SY, width: SW, height: SH, background: CLAUDE.CARD,
        border: `1.5px solid ${CLAUDE.BORDER}`, opacity: op(sSpec) }}>
        <SpecImage w={SW} h={SH} clean={imgOp} noisy={noisy} />
      </div>
      <svg width={SW} height={SH} style={{ position: 'absolute', left: SX, top: SY, overflow: 'visible' }}>
        <SpecAxes w={SW} h={SH} size={lbl} opacity={op(sSpec)} />
        {peaks.map((p, i) => {
          const k = clamp(reveal * n - i, 0, 1);
          if (k <= 0) return null;
          const lost = !survived.has(`${p[0]}:${p[1]}`);
          const hollow = lost ? noisy : 0;
          return (
            <circle key={i} cx={x(p[0])} cy={y(p[1])} r={R * (0.6 + 0.4 * k) * (1 + 0.25 * op(sSurv) * (lost ? 0 : 1))}
              fill={hollow > 0.5 ? CLAUDE.CARD : SPARK_TEXT} stroke={hollow > 0.5 ? CLAUDE.GHOST : SPARK_TEXT}
              strokeWidth={3} opacity={k * (lost ? 1 - 0.35 * hollow : 1)} />
          );
        })}
      </svg>
      {/* axis captions */}
      <div style={{ position: 'absolute', left: SX, top: SY - lbl * 1.6, opacity: op(sp(tPitch)),
        fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK }}>↑ PITCH (HZ)</div>
      <div style={{ position: 'absolute', left: SX + SW - 300, top: SY + SH + lbl * 2.2, width: 300, textAlign: 'right', whiteSpace: 'nowrap', opacity: op(sp(tTime)),
        fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK }}>TIME →</div>
      <div style={{ position: 'absolute', left: SX + SW, top: SY - lbl * 1.6, transform: 'translateX(-100%)', opacity: op(sp(tDark)) * (1 - fadeBack),
        fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK_SOFT, whiteSpace: 'nowrap' }}>DARKER = LOUDER</div>
      {noisy > 0.05 ? (
        <div style={{ position: 'absolute', left: SX + SW, top: SY - lbl * 1.6, transform: 'translateX(-100%)', opacity: noisy,
          fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1.2, color: SPARK_TEXT, whiteSpace: 'nowrap' }}>
          {portrait ? 'NOISY PHONE CLIP' : 'THE SAME 3 S, NOISY PHONE CLIP'}</div>
      ) : null}
    </>
  );

  const stats = [
    { v: fmt(SHZ.spec.values), l: portrait ? 'NUMBERS IN 3 S' : 'NUMBERS IN THESE 3 SECONDS', o: op(sSpec) },
    { v: `${n}`, l: 'LOUDEST POINTS KEPT', o: op(sp(tKept)), a: true },
    { v: `${SHZ.library.peaks_per_s}`, l: 'PEAKS PER SECOND', o: op(sp(tTwelve)) },
    { v: `${(SHZ.spec.survived as number[][]).length} of ${n}`, l: portrait ? 'SURVIVE THE NOISE' : 'SURVIVE NOISE AS LOUD AS THE MUSIC', o: op(sSurv), a: true },
  ];

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        {panel}
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.58, width: CW, display: 'grid',
          gridTemplateColumns: '1fr 1fr', rowGap: 26, columnGap: 30 }}>
          {stats.map((s, i) => <Stat key={i} value={s.v} label={s.l} size={T.title * 0.95} opacity={s.o} accent={s.a} />)}
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.535, opacity: op(sp(tConst)) * (1 - noisy) }}>
          <Chip text="“CONSTELLATION MAP”" size={T.label * 0.8} accent />
        </div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      {panel}
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.66, top: SY - 6 * U, width: CW * 0.34, display: 'flex', flexDirection: 'column', gap: 30 * U }}>
        {stats.map((s, i) => <Stat key={i} value={s.v} label={s.l} size={58 * U} opacity={s.o} accent={s.a} />)}
      </div>
      <div style={{ position: 'absolute', left: SX, top: SY + SH + 84 * U, opacity: op(sp(tConst)) }}>
        <Chip text="THE 2003 SHAZAM PAPER: A “CONSTELLATION MAP”" size={22 * U} accent />
      </div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
