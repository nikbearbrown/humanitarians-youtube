/**
 * SqlScaleComparison916 — portrait (9:16) variant of B04's log-scale comparison.
 *
 * RE-BAND: the landscape version is a wide horizontal log axis with three
 * lollipop rows crammed into 740px of height. Portrait keeps the axis horizontal
 * (a magnitude axis must stay one continuous line to read as a scale) but gives
 * each item its OWN generous vertical band — label, then the lollipop, then the
 * value — stacked top to bottom with room to breathe. This is a re-band, not a
 * scale-down: each row gains ~2.5x the vertical space it had.
 *
 * Carries the landscape fixes forward: labels sit ABOVE their row with a width
 * budget (_qc/REPORT.md #2) and integers are thousands-separated (#9).
 *
 * No library `ScaleComparison916` (checked Root.tsx: absent).
 * Registered 1080x1920; --scale=2 renders 2160x3840 native.
 *
 * REEL-LOCAL. Register per remotion-src/REGISTER.md.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import { HandleChip } from './ClaudeCodeBeat';
import {clamp, lerp, remap, easeOutCubic, BG, INK, ACCENT, MUTE, FONT, scW, wrapText} from './sqlDeckKit';

export const sqlScaleComparison916Schema = z.object({
  /** Lower-right author handle chip (e.g. "Supriya"). Omitted → no chip. */
  handle: z.string().optional(),
  /** Put the handle chip top-right instead of bottom-right. Omitted → bottom. */
  handleTop: z.boolean().optional(),
  data: z.object({
    slideMeta: z.string().default(''),
    axis: z.object({min: z.number(), max: z.number(), unit: z.string()}),
    band: z.object({from: z.number(), to: z.number(), label: z.string()}),
    axisLabel: z.string().optional(),
    items: z.array(z.object({
      label: z.string(), value: z.number(), hot: z.boolean().optional(),
    })).default([]),
    script: z.string().optional(),
  }),
});
export type SqlScaleComparison916Props = z.infer<typeof sqlScaleComparison916Schema>;

const fmtInt = (v: number) =>
  Number.isInteger(v) ? v.toLocaleString('en-US') : String(Math.round(v * 100) / 100);

export const SqlScaleComparison916: React.FC<SqlScaleComparison916Props> = ({handle, handleTop, data}) => {
  const frame = useCurrentFrame();
  const {width: W, height: H, durationInFrames} = useVideoConfig();
  const p = clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);
  const S = scW(W);

  const ax = data.axis, items = data.items;
  const x0 = 100 * S, x1 = W - 110 * S;   // v2: end tick labels stay inside the 5% side inset
  const yAxis = H - 250 * S;
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
  const rowTop = 344 * S;
  const bandH = (yAxis - rowTop - 60 * S) / rows;
  const yOf = (i: number) => rowTop + i * bandH + bandH * 0.62;

  const labelChars = 30;

  return (
    <AbsoluteFill style={{backgroundColor: BG, fontFamily: FONT}}>
      <div style={{
        position: 'absolute', left: 56 * S, top: 100 * S, maxWidth: W - 112 * S,
        fontSize: 21 * S, letterSpacing: '.14em', color: MUTE, fontWeight: 600,
      }}>
        {wrapText(data.slideMeta, 40).map((ln, i) => <div key={i}>{ln}</div>)}
      </div>

      <svg width={W} height={H} style={{position: 'absolute', inset: 0}}>
        {/* the band, drawn behind everything */}
        <g opacity={bandP}>
          <rect x={bx0} y={rowTop - 66 * S} width={(bx1 - bx0) * easeOutCubic(bandP)}
            height={yAxis - (rowTop - 66 * S)} fill={ACCENT} opacity={0.1} />
          <text x={(bx0 + bx1) / 2} y={rowTop - 80 * S} textAnchor="middle" fontFamily={FONT}
            fontSize={20 * S} fontWeight={700} fill={ACCENT}>
            {data.band.label.toUpperCase()}
          </text>
        </g>

        {/* axis */}
        <g>
          <line x1={x0} x2={x1} y1={yAxis} y2={yAxis} stroke={INK} strokeWidth={3 * S}
            strokeDasharray={axLen} strokeDashoffset={axLen * (1 - axP)} />
          {ticks.map((d, k) => (
            <g key={k}>
              <line x1={xOf(d)} x2={xOf(d)} y1={yAxis} y2={yAxis + 12 * S} stroke={MUTE} strokeWidth={1.5 * S} />
              <text x={xOf(d)} y={yAxis + 40 * S} textAnchor="middle" fontFamily={FONT}
                fontSize={19 * S} fill={MUTE}>{fmtInt(d)}</text>
            </g>
          ))}
          <text x={x1} y={yAxis + 78 * S} textAnchor="end" fontFamily={FONT} fontSize={19 * S}
            fill={MUTE} letterSpacing=".08em">
            {`${(data.axisLabel || 'value').toUpperCase()} — LOG SCALE, ${unit.toUpperCase()}`}
          </text>
        </g>

        {/* items — each in its own vertical band */}
        {items.map((d, i) => {
          const st = 0.30 + (i / rows) * 0.5;
          const en = st + 0.28;
          const t = easeOutCubic(remap(p, st, en, 0, 1));
          const y = yOf(i);
          const curX = lerp(x0, xOf(d.value), t);
          const col = d.hot ? ACCENT : INK;
          const lines = wrapText(d.label, labelChars);
          return (
            <g key={i}>
              {lines.map((ln, k) => (
                <text key={k} x={x0} y={y - (58 - k * 34) * S} textAnchor="start" fontFamily={FONT}
                  fontWeight={700} fontSize={(d.hot ? 31 : 28) * S} fill={col} opacity={t}>
                  {ln}
                </text>
              ))}
              <line x1={x0} x2={curX} y1={y} y2={y} stroke={col} strokeWidth={(d.hot ? 3 : 2) * S}
                strokeOpacity={0.32 * t} />
              <line x1={curX} x2={curX} y1={y} y2={yAxis} stroke={col} strokeWidth={(d.hot ? 3 : 2) * S}
                strokeOpacity={0.30 * t} />
              <circle cx={curX} cy={y} r={(d.hot ? 13 : 10) * S} fill={col} opacity={t} />
              <text x={x0} y={y + 44 * S} textAnchor="start" fontFamily={FONT}
                fontSize={26 * S} fontWeight={d.hot ? 700 : 400}
                fill={d.hot ? ACCENT : MUTE} opacity={t}>
                {`${fmtInt(d.value)} ${unit}`}
              </text>
            </g>
          );
        })}
      </svg>
      {/* handleTop: chip top-right, inside the 5% title-safe inset, where this layout's
          bottom-right corner is occupied by content. */}
      <HandleChip handle={handle} fontSize={H * (H > W ? 0.016 : 0.024)} right={W * 0.07}
        bottom={handleTop ? H - H * 0.05 - 10 * S - H * (H > W ? 0.016 : 0.024) * 1.9 : H * (H > W ? 0.06 : 0.055)} opacity={0.9} />
    </AbsoluteFill>
  );
};
