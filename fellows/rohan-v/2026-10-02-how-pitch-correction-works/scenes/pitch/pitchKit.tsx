import React from 'react';
import { CLAUDE } from '../../tokens/claude';
import { HAI_TYPE, SPARK_TEXT, clamp } from '../../lib/cueKit';
import { PITCH } from './pitchData';

/**
 * pitchKit — shared drawing for "How Pitch Correction Works".
 *
 * Every curve these helpers draw is a column of `pitchData.ts`, GENERATED from a
 * real run of pitch_demo.py (YIN detection, snap, glide, TD-PSOLA, then the same
 * detector run again on the corrected audio). Nothing here invents a pitch: the
 * helpers map measured Hz to note lanes and paint. The one synthetic element is
 * `ToneWave`, a clean periodic wave used to explain what "a vibration that
 * repeats" means — it is never presented as a measurement.
 *
 * Colour: corrected (re-measured) curves are drawn in SPARK_TEXT, not SPARK. GATE T §8.3
 * reads thick or dashed #D97757 strokes as accent text (2.74:1 on cream) — the first
 * final was blocked on exactly that in B04 and B06.
 */

export const NOTE = ['C', 'C♯', 'D', 'D♯', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'A♯', 'B'];
export const toMidi = (hz: number) => 69 + 12 * Math.log2(hz / 440);
export const noteName = (m: number) => {
  const r = Math.round(m);
  return `${NOTE[((r % 12) + 12) % 12]}${Math.floor(r / 12) - 1}`;
};
export const isNatural = (m: number) => [0, 2, 4, 5, 7, 9, 11].includes(((Math.round(m) % 12) + 12) % 12);

/** Index range of PITCH.times inside [t0, t1] seconds. */
export const frameRange = (t0: number, t1: number) => {
  const ts = PITCH.times;
  let a = 0;
  while (a < ts.length && ts[a] < t0) a++;
  let b = a;
  while (b < ts.length && ts[b] <= t1) b++;
  return [a, b] as const;
};

/**
 * A pitch curve as an SVG path on a piano roll. Unvoiced frames (0 Hz) break the
 * line, so breaths between notes read as gaps rather than as dives to the floor.
 * `reveal` (0..1) draws the curve left to right in time.
 */
export const curvePath = (
  f0: number[], t0: number, t1: number, m0: number, m1: number,
  w: number, h: number, reveal = 1,
) => {
  const ts = PITCH.times;
  const tEnd = t0 + (t1 - t0) * clamp(reveal, 0, 1);
  let d = '';
  let pen = false;
  for (let i = 0; i < ts.length; i++) {
    const t = ts[i];
    if (t < t0) continue;
    if (t > tEnd) break;
    const f = f0[i];
    if (!f || f <= 0) { pen = false; continue; }
    const m = toMidi(f);
    const x = ((t - t0) / (t1 - t0)) * w;
    const y = h - ((m - m0) / (m1 - m0)) * h;
    d += `${pen ? 'L' : 'M'} ${x.toFixed(1)} ${y.toFixed(1)} `;
    pen = true;
  }
  return d;
};

/** Note lanes: one horizontal band per semitone, naturals labelled. */
export const Lanes: React.FC<{
  w: number; h: number; m0: number; m1: number; labelSize: number; labelW: number;
  highlight?: Record<number, { color: string; strength: number }>;
  struck?: Record<number, number>; opacity?: number; onlyLabels?: number[];
}> = ({ w, h, m0, m1, labelSize, labelW, highlight = {}, struck = {}, opacity = 1, onlyLabels }) => {
  const rows: React.ReactNode[] = [];
  const unit = h / (m1 - m0);
  for (let m = Math.ceil(m0 + 0.5); m <= Math.floor(m1 - 0.5); m++) {
    const yc = h - (m - m0) * unit;
    const hi = highlight[m];
    const showLabel = onlyLabels ? onlyLabels.includes(m) : isNatural(m);
    rows.push(
      <g key={m} opacity={opacity}>
        <rect x={0} y={yc - unit / 2} width={w} height={unit}
          fill={hi ? hi.color : (isNatural(m) ? CLAUDE.CARD : CLAUDE.FOOTER)}
          fillOpacity={hi ? 0.06 + 0.09 * hi.strength : 1} />
        {/* A highlighted lane is marked by a solid line along its centre plus a faint tint.
            A strong tint over a whole lane is read by Gate V as mid-tone "ink" and pulls the
            frame's ink/background separation under 0.30 (week-06 B05/B06). */}
        {hi ? <line x1={0} x2={w} y1={yc} y2={yc} stroke={hi.color === CLAUDE.SPARK ? SPARK_TEXT : hi.color}
          strokeWidth={Math.max(3, unit * 0.06)} opacity={clamp(0.35 + hi.strength, 0, 1)} /> : null}
        <line x1={0} x2={w} y1={yc + unit / 2} y2={yc + unit / 2} stroke={CLAUDE.BORDER} strokeWidth={1} />
        {showLabel ? (
          <text x={-labelW * 0.12} y={yc + labelSize * 0.36} textAnchor="end"
            fontFamily={HAI_TYPE.sans} fontWeight={700} fontSize={labelSize}
            fill={hi && hi.strength > 0.5 ? SPARK_TEXT : CLAUDE.INK_SOFT}>
            {noteName(m)}
          </text>
        ) : null}
        {struck[m] ? (
          <line x1={0} x2={w * clamp(struck[m], 0, 1)} y1={yc} y2={yc}
            stroke={SPARK_TEXT} strokeWidth={Math.max(3, unit * 0.12)} strokeLinecap="round" />
        ) : null}
      </g>,
    );
  }
  return <g>{rows}</g>;
};

/** Target note blocks (where each sung note SHOULD be), from the melody record. */
export const TargetBlocks: React.FC<{
  t0: number; t1: number; m0: number; m1: number; w: number; h: number; opacity: number;
}> = ({ t0, t1, m0, m1, w, h, opacity }) => {
  const unit = h / (m1 - m0);
  return (
    <g opacity={opacity}>
      {PITCH.melody.map((n, i) => {
        const x0 = ((n.start - t0) / (t1 - t0)) * w;
        const x1 = ((n.end - t0) / (t1 - t0)) * w;
        const yc = h - (n.midi - m0) * unit;
        return <rect key={i} x={x0} y={yc - unit * 0.32} width={Math.max(0, x1 - x0)} height={unit * 0.64}
          rx={unit * 0.2} fill="none" stroke={CLAUDE.INK_SOFT} strokeWidth={2} strokeDasharray="7 6" />;
      })}
    </g>
  );
};

/** A clean periodic tone (explanatory, not measured): a few harmonics, `cycles` across `w`. */
export const ToneWave = (w: number, h: number, amp: number, cycles: number, n = 900) => {
  let d = '';
  for (let i = 0; i <= n; i++) {
    const t = i / n;
    const p = t * cycles * Math.PI * 2;
    const v = (Math.sin(p) * 0.72 + Math.sin(2 * p + 0.6) * 0.2 + Math.sin(3 * p + 1.1) * 0.08) * amp;
    d += `${i === 0 ? 'M' : 'L'} ${(t * w).toFixed(1)} ${(h / 2 - v).toFixed(1)} `;
  }
  return d;
};

/** A labelled chip — ink fill, or an outline in SPARK_TEXT for the accent. */
export const Chip: React.FC<{
  text: string; size: number; accent?: boolean; style?: React.CSSProperties;
}> = ({ text, size, accent = false, style }) => (
  <span style={{
    fontFamily: HAI_TYPE.sans, fontSize: size, fontWeight: 800, letterSpacing: 1.2,
    color: accent ? SPARK_TEXT : CLAUDE.CARD,
    background: accent ? 'transparent' : CLAUDE.INK,
    border: accent ? `2px solid ${SPARK_TEXT}` : 'none',
    borderRadius: size * 0.35, padding: `${size * 0.22}px ${size * 0.5}px`,
    whiteSpace: 'nowrap', display: 'inline-block', ...style,
  }}>{text}</span>
);

/** Which listening clip (if any) is playing at this beat fraction. */
export const listening = (listen: { label: string; from: number; to: number }[] | undefined, frac: number) => {
  if (!listen) return null;
  for (const c of listen) if (frac >= c.from && frac <= c.to) {
    return { ...c, progress: (frac - c.from) / Math.max(1e-6, c.to - c.from) };
  }
  return null;
};

export { PITCH };
