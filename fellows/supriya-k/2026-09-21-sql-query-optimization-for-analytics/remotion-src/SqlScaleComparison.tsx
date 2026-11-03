/**
 * SqlScaleComparison — fork of the library `ScaleComparison` (deckPatterns.tsx).
 *
 * FIX (vs the library component), from _qc/REPORT.md #2 (BLOCKER):
 *
 *   The library right-aligns each item label to the LEFT of the axis origin:
 *       <text x={x0 - 14} textAnchor="end" fontSize={14}>{label}</text>
 *   with x0 = 150 and no width budget, no wrap, no shrink. Its own design copy
 *   is ~10 characters ("Baseline"). This reel's labels are 27-42 characters
 *   ("Plan B — SEARCH via idx_postings_posted_at"), so they overflowed past
 *   x=0 and off the frame: the render showed "· SCAN POSTINGS" and
 *   "OSTINGS_POSTED_AT", and the third label vanished entirely.
 *
 *   FIX: labels move ABOVE their own lollipop row, LEFT-aligned at the axis
 *   origin, where the full frame width is available. Each gets an explicit
 *   character budget and auto-shrinks if it exceeds it, so a longer label can
 *   never leave the frame. The value chip stays to the right of the marker.
 *   Legibility beats designer intent, per the build instruction.
 *
 * ALSO FIXED — #9 MINOR: values rendered as "400000 rows" while every other
 *   surface in the reel uses "400,000". The fork thousands-separates integers.
 *
 * ALSO — #10 MINOR: registered at 1920x1080 with hardcoded pixels scaled by
 *   sc(H), so it renders at a true 3840x2160 under the existing --scale=2.
 *
 * Log axis math, band, draw-on timing and easing are VERBATIM from the library.
 *
 * REEL-LOCAL. Register per remotion-src/REGISTER.md.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import { HandleChip } from './ClaudeCodeBeat';
import {clamp, lerp, remap, easeOutCubic, BG, INK, ACCENT, MUTE, FONT, sc} from './sqlDeckKit';

export const sqlScaleComparisonSchema = z.object({
  /** Lower-right author handle chip (e.g. "Supriya"). Omitted → no chip. */
  handle: z.string().optional(),
  data: z.object({
    slideMeta: z.string().default(''),
    axis: z.object({min: z.number(), max: z.number(), unit: z.string()}),
    band: z.object({from: z.number(), to: z.number(), label: z.string()}),
    axisLabel: z.string().optional(),
    items: z.array(z.object({
      label: z.string(),
      value: z.number(),
      hot: z.boolean().optional(),
    })).default([]),
    script: z.string().optional(),
  }),
});
export type SqlScaleComparisonProps = z.infer<typeof sqlScaleComparisonSchema>;

/** Thousands separators for integers (fix #9). */
const fmtInt = (v: number) =>
  Number.isInteger(v) ? v.toLocaleString('en-US') : String(Math.round(v * 100) / 100);

export const SqlScaleComparison: React.FC<SqlScaleComparisonProps> = ({handle, data}) => {
  const frame = useCurrentFrame();
  const {width: W, height: H, durationInFrames} = useVideoConfig();
  const p = clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);
  const S = sc(H);

  const ax = data.axis, items = data.items;
  const x0 = 150 * S, x1 = W - 110 * S, yAxis = H - 150 * S;
  const lg = (v: number) => Math.log10(v);
  const xOf = (v: number) => remap(lg(v), lg(ax.min), lg(ax.max), x0, x1);
  const unit = ax.unit;

  const axP = remap(p, 0, 0.18, 0, 1);
  const axLen = x1 - x0;

  const ticks: number[] = [];
  for (let e = Math.ceil(lg(ax.min)); e <= Math.floor(lg(ax.max)); e++) ticks.push(Math.pow(10, e));

  const bandP = remap(p, 0.18, 0.34, 0, 1);
  const bx0 = xOf(data.band.from), bx1 = xOf(data.band.to);

  const rows = items.length;
  // Rows sit lower than the library's to leave headroom for the label above each.
  const rowTop = 190 * S;
  const yOf = (i: number) => rowTop + (i + 0.5) * ((yAxis - rowTop - 40 * S) / rows);

  // FIX: explicit width budget. Label is left-aligned at x0 and must fit the
  // span to the frame's right safe edge; shrink the font if it would not.
  const labelBudgetPx = x1 - x0;
  const fitFontSize = (text: string, base: number) => {
    const charW = 0.62;                       // JetBrains Mono advance ratio
    const needed = text.length * base * charW;
    return needed <= labelBudgetPx ? base : Math.max(11 * S, base * (labelBudgetPx / needed));
  };

  return (
    <AbsoluteFill style={{backgroundColor: BG, fontFamily: FONT}}>
      <div style={{
        position: 'absolute', left: 60 * S, top: 34 * S, maxWidth: W - 120 * S,
        fontSize: 13 * S, letterSpacing: '.18em', color: MUTE, fontWeight: 600,
        whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis',
      }}>
        {data.slideMeta}
      </div>

      <svg width={W} height={H} style={{position: 'absolute', inset: 0}}>
        {/* axis — draws first, constant velocity (MOTION.md §4) */}
        <g>
          <line x1={x0} x2={x1} y1={yAxis} y2={yAxis} stroke={INK} strokeWidth={2 * S}
            strokeDasharray={axLen} strokeDashoffset={axLen * (1 - axP)} />
          {ticks.map((d, k) => (
            <g key={k}>
              <line x1={xOf(d)} x2={xOf(d)} y1={yAxis} y2={yAxis + 8 * S} stroke={MUTE} strokeWidth={1 * S} />
              <text x={xOf(d)} y={yAxis + 26 * S} textAnchor="middle" fontFamily={FONT}
                fontSize={12 * S} fill={MUTE}>
                {`${fmtInt(d)} ${unit}`}
              </text>
            </g>
          ))}
          <text x={x1} y={yAxis + 48 * S} textAnchor="end" fontFamily={FONT} fontSize={12 * S}
            fill={MUTE} letterSpacing=".1em">
            {`${(data.axisLabel || 'value').toUpperCase()} (LOG SCALE, ${unit.toUpperCase()})`}
          </text>
        </g>

        {/* band */}
        <g opacity={bandP}>
          <rect x={bx0} y={rowTop - 54 * S} width={(bx1 - bx0) * easeOutCubic(bandP)}
            height={yAxis - (rowTop - 54 * S)} fill={ACCENT} opacity={0.1} />
          <text x={(bx0 + bx1) / 2} y={rowTop - 66 * S} textAnchor="middle" fontFamily={FONT}
            fontSize={13 * S} fontWeight={700} fill={ACCENT}>
            {data.band.label.toUpperCase()}
          </text>
        </g>

        {/* items — label ABOVE the row, left-aligned, width-budgeted */}
        {items.map((d, i) => {
          const st = 0.30 + (i / rows) * 0.5;
          const en = st + 0.28;
          const t = easeOutCubic(remap(p, st, en, 0, 1));
          const y = yOf(i);
          const tx = xOf(d.value);
          const curX = lerp(x0, tx, t);
          const col = d.hot ? ACCENT : INK;
          const base = (d.hot ? 20 : 18) * S;
          const fs = fitFontSize(d.label, base);
          return (
            <g key={i}>
              <text x={x0} y={y - 26 * S} textAnchor="start" fontFamily={FONT} fontWeight={700}
                fontSize={fs} fill={col} opacity={t}>
                {d.label}
              </text>
              <line x1={x0} x2={curX} y1={y} y2={y} stroke={col} strokeWidth={(d.hot ? 2 : 1) * S}
                strokeOpacity={0.30 * t} />
              <line x1={curX} x2={curX} y1={y} y2={yAxis} stroke={col} strokeWidth={(d.hot ? 2 : 1) * S}
                strokeOpacity={0.30 * t} />
              <circle cx={curX} cy={y} r={(d.hot ? 9 : 7) * S} fill={col} opacity={t} />
              <text x={curX + 18 * S} y={y} dy="0.35em" fontFamily={FONT}
                fontSize={15 * S} fontWeight={d.hot ? 700 : 400} fill={d.hot ? ACCENT : MUTE} opacity={t}>
                {`${fmtInt(d.value)} ${unit}`}
              </text>
            </g>
          );
        })}
      </svg>
      <HandleChip handle={handle} fontSize={H * (H > W ? 0.016 : 0.024)} right={W * 0.07}
        bottom={H * (H > W ? 0.06 : 0.055)} opacity={0.9} />
    </AbsoluteFill>
  );
};
