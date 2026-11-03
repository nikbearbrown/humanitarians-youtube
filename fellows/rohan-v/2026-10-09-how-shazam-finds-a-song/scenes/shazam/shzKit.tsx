import React from 'react';
import { Img, staticFile } from 'remotion';
import { CLAUDE } from '../../tokens/claude';
import { HAI_TYPE, SPARK_TEXT, clamp, op } from '../../lib/cueKit';
import { SHZ } from './shazamData';

export { Chip, listening } from '../pitch/pitchKit';
export { SHZ };

/**
 * shzKit — shared drawing for "How Shazam Finds a Song."
 *
 * Everything drawn here is a column of `shazamData.ts`, GENERATED from a real run of
 * fingerprint.py (spectrogram peaks, anchor/target-zone hashes, offset voting) on synthetic
 * songs. The spectrogram is a pre-rendered image of the run's own STFT (louder = darker ink);
 * peaks, hashes and votes are drawn over it as vectors at their measured positions.
 *
 * Colour: anything small or line-like that carries meaning (peaks, hash lines, the winning
 * votes) is SPARK_TEXT, never SPARK: GATE T §8.3 reads small #D97757 marks as accent text.
 */

export const COL_S: number = SHZ.params.col_s;
export const HZ_PER_BIN: number = SHZ.params.sr / SHZ.params.nfft;
export const fmt = (n: number) => n.toLocaleString('en-US');

/** A spectrogram panel: the image plus a coordinate map for overlays (t in columns, f in bins). */
export const useSpec = (w: number, h: number) => {
  const { cols, bins } = SHZ.spec;
  return {
    x: (t: number) => (t / cols) * w,
    y: (f: number) => h - (f / bins) * h,
  };
};

export const SpecImage: React.FC<{ w: number; h: number; clean: number; noisy?: number }> = ({ w, h, clean, noisy = 0 }) => (
  <>
    <Img src={staticFile(SHZ.spec.clean)} style={{ position: 'absolute', left: 0, top: 0, width: w, height: h, opacity: clean * (1 - noisy) }} />
    {noisy > 0 ? <Img src={staticFile(SHZ.spec.noisy)} style={{ position: 'absolute', left: 0, top: 0, width: w, height: h, opacity: clean * noisy }} /> : null}
  </>
);

/** Frequency ticks (Hz) on the left of a spectrogram panel and seconds below it. */
export const SpecAxes: React.FC<{ w: number; h: number; size: number; opacity: number; seconds?: number[] }> = ({ w, h, size, opacity, seconds = [0, 1, 2, 3] }) => {
  const fmax: number = SHZ.spec.fmaxHz;
  return (
    <g opacity={opacity} fontFamily={HAI_TYPE.sans} fontWeight={700} fontSize={size} fill={CLAUDE.INK_SOFT}>
      {[0, 1000, 2000].map((hz) => (
        <g key={hz}>
          <line x1={-10} x2={0} y1={h - (hz / fmax) * h} y2={h - (hz / fmax) * h} stroke={CLAUDE.INK_SOFT} strokeWidth={2} />
          <text x={-16} y={h - (hz / fmax) * h + size * 0.35} textAnchor="end">{hz === 0 ? '0' : `${fmt(hz)}`}</text>
        </g>
      ))}
      {seconds.map((s) => (
        <text key={s} x={(s / 3) * w} y={h + size * 1.4} textAnchor={s === 0 ? 'start' : s === 3 ? 'end' : 'middle'}>{s} S</text>
      ))}
    </g>
  );
};

/** A stat block: big serif number over a caps label. */
export const Stat: React.FC<{ value: string; label: string; size: number; opacity: number; accent?: boolean; style?: React.CSSProperties }> = ({ value, label, size, opacity, accent, style }) => (
  <div style={{ opacity, transform: `translateY(${(1 - opacity) * 14}px)`, ...style }}>
    <div style={{ fontFamily: HAI_TYPE.serif, fontSize: size, fontWeight: 700, lineHeight: 1.0, color: accent ? SPARK_TEXT : CLAUDE.INK }}>{value}</div>
    <div style={{ fontFamily: HAI_TYPE.sans, fontSize: Math.max(22, size * 0.34), fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK_SOFT, marginTop: size * 0.12 }}>{label}</div>
  </div>
);

/** Phone baseline: a ghost hairline above the spark line from the first frame (Gate V canvas-fill). */
export const PhoneBaseline: React.FC<{ padX: number; width: number; height: number; inOp: number }> = ({ padX, width, height, inOp }) => (
  <div style={{ position: 'absolute', left: padX, top: height * 0.782, width: width - padX * 2, height: 3, background: CLAUDE.GHOST, opacity: op(inOp) * 0.7 }} />
);

/** A vote histogram as an SVG path of bars (bins over -2..40 s), scaled to `max`. */
export const histBars = (hist: number[], w: number, h: number, max: number, grow = 1) => {
  const bw = w / hist.length;
  return hist.map((v, i) => ({ x: i * bw, w: Math.max(1, bw * 0.8), h: (clamp(v, 0, max) / max) * h * grow, v }));
};
