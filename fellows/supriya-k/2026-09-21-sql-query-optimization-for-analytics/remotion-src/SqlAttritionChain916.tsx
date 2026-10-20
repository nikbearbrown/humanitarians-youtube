/**
 * SqlAttritionChain916 — portrait (9:16) variant of B01's isotype funnel.
 *
 * RE-BAND: the landscape version lays the three stages SIDE BY SIDE; portrait
 * STACKS them top to bottom, each panel full width. Rows of dots get wider and
 * shallower, which suits a portrait frame. Dots that fail a stage drift to the
 * RIGHT and fade (landscape dropped them downward — in a stacked layout that
 * would collide with the next panel).
 *
 * Carries both landscape fixes forward (_qc/REPORT.md #3, #4): the isotype scale
 * declaration lives in its own `scaleNote` at the bottom, and `slideMeta` is
 * width-capped so the counter card can never paint over it.
 *
 * No library `AttritionChain916` (checked Root.tsx: absent).
 * Registered 1080x1920; --scale=2 renders 2160x3840 native.
 *
 * REEL-LOCAL. Register per remotion-src/REGISTER.md.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import { HandleChip } from './ClaudeCodeBeat';
import {clamp, lerp, remap, easeOutCubic, seeded, BG, INK, ACCENT, MUTE, FONT, scW} from './sqlDeckKit';

export const sqlAttritionChain916Schema = z.object({
  /** Lower-right author handle chip (e.g. "Supriya"). Omitted → no chip. */
  handle: z.string().optional(),
  /** Put the handle chip top-right instead of bottom-right. Omitted → bottom. */
  handleTop: z.boolean().optional(),
  data: z.object({
    title: z.string().default(''),
    slideMeta: z.string().default(''),
    scaleNote: z.string().default(''),
    total: z.number().default(400),
    startLabel: z.string().default('start'),
    stages: z.array(z.object({label: z.string(), survival: z.number()})).default([]),
    /** Optional exact figure per panel (start + each stage), right-aligned on the
     *  panel's label row; each fades in once its stage settles. */
    panelCounts: z.array(z.string()).optional(),
    script: z.string().optional(),
  }),
});
export type SqlAttritionChain916Props = z.infer<typeof sqlAttritionChain916Schema>;

export const SqlAttritionChain916: React.FC<SqlAttritionChain916Props> = ({handle, handleTop, data}) => {
  const frame = useCurrentFrame();
  const {width: W, height: H, durationInFrames} = useVideoConfig();
  const p = clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);
  const S = scW(W);

  const total = data.total;
  const stages = data.stages;
  const rows = stages.length + 1;

  const padX = 56 * S;
  const panelW = W - padX * 2;
  const headTop = 244 * S;                    // below slideMeta + counter
  const scaleBand = data.scaleNote ? 96 * S : 40 * S;
  const labelH = 44 * S;
  const gapY = 30 * S;
  const panelH = (H - headTop - scaleBand - rows * labelH - (rows - 1) * gapY) / rows;

  const rowTop = (r: number) => headTop + r * (labelH + panelH + gapY) + labelH;

  const counts = [total];
  for (const s of stages) counts.push(Math.round(counts[counts.length - 1] * s.survival));

  const gridPos = (i: number, count: number, r: number) => {
    const n = Math.max(1, count);
    const cc = Math.max(4, Math.ceil(Math.sqrt(n * (panelW / panelH))));
    const rr = Math.max(1, Math.ceil(n / cc));
    const ipx = 18 * S, ipy = 18 * S;
    const uw = panelW - ipx * 2, uh = panelH - ipy * 2;
    const gc = i % cc, gr = Math.floor(i / cc);
    const x = padX + ipx + (cc === 1 ? uw / 2 : (gc / (cc - 1)) * uw);
    const y = rowTop(r) + ipy + (rr === 1 ? uh / 2 : (gr / Math.max(1, rr - 1)) * uh);
    return {x, y};
  };
  // Stacked layout: a failing dot drifts a SHORT distance right of where it
  // already sits and fades out fast. QC pass 1 on the portrait cut sent losers
  // all the way to the frame edge, which turned 97% of the field into long
  // crossing trajectories — it read as noise, not as a grid dissolving, and
  // dots spilled outside the panel border. Landscape drops them a short way
  // down; stacked panels cannot use "down" (it collides with the next panel),
  // so this drifts a short way right instead. `from` is passed in so the drift
  // is relative to the dot's own position, not to the frame.
  const lossPos = (i: number, from: {x: number; y: number}) => ({
    // clamped to the panel's own right edge: QC pass 2 showed rightmost-column
    // dots drifting past the border before they finished fading.
    x: Math.min(from.x + (40 + seeded(i) * 56) * S, padX + panelW - 6 * S),
    y: from.y + (seeded(i * 3) - 0.5) * 30 * S,
  });

  const dotR = (() => {
    const n = Math.max(1, counts[0]);
    const cc = Math.max(4, Math.ceil(Math.sqrt(n * (panelW / panelH))));
    const rr = Math.max(1, Math.ceil(n / cc));
    const uw = panelW - 36 * S, uh = panelH - 36 * S;
    const pitch = Math.min(cc > 1 ? uw / (cc - 1) : uw, rr > 1 ? uh / (rr - 1) : uh);
    return clamp(pitch * 0.34, 1.6 * S, 8 * S);
  })();

  const intro = 0.10, outro = 0.14;
  const span = 1 - intro - outro;
  const each = span / Math.max(1, stages.length);
  const ranges = stages.map((_, k) => ({a: intro + k * each, b: intro + (k + 1) * each}));

  let curCount = counts[0], stageIdx = 0;
  for (let k = 0; k < stages.length; k++) {
    const r = ranges[k];
    if (p >= r.b) {curCount = counts[k + 1]; stageIdx = k + 1;}
    else if (p >= r.a) {
      curCount = Math.round(lerp(counts[k], counts[k + 1], easeOutCubic((p - r.a) / (r.b - r.a))));
      stageIdx = k; break;
    } else break;
  }
  const pct = (curCount / total) * 100;

  const dots: React.ReactNode[] = [];
  for (let i = 0; i < total; i++) {
    let x = 0, y = 0, op = i < counts[0] ? 1 : 0, placed = false;
    for (let k = 0; k < stages.length; k++) {
      const fromCount = counts[k], toCount = counts[k + 1];
      const r = ranges[k];
      const survives = i < toCount;
      const from = gridPos(i, fromCount, k);
      if (p < r.a) {x = from.x; y = from.y; op = i < fromCount ? 1 : 0; placed = true; break;}
      const t = easeOutCubic((p - r.a) / (r.b - r.a));
      if (p < r.b) {
        if (survives) {
          const to = gridPos(i, toCount, k + 1);
          x = lerp(from.x, to.x, t); y = lerp(from.y, to.y, t); op = 1;
        } else {
          const lp = lossPos(i, from);
          x = lerp(from.x, lp.x, t); y = lerp(from.y, lp.y, t);
          op = remap(t, 0, 0.45, 1, 0);   // gone well before it can reach the border
        }
        placed = true; break;
      }
      if (survives) {const set = gridPos(i, toCount, k + 1); x = set.x; y = set.y; op = 1; continue;}
      op = 0; placed = true; break;
    }
    if (!placed && op > 0) {const q = gridPos(i, counts[counts.length - 1], rows - 1); x = q.x; y = q.y;}
    if (op <= 0.01) continue;
    const isFinal = stageIdx >= stages.length && i < counts[counts.length - 1];
    dots.push(<circle key={i} cx={x} cy={y} r={dotR} fill={isFinal ? ACCENT : INK} opacity={op} />);
  }

  const counterW = 420 * S, counterH = 92 * S;
  const counterLeft = (W - counterW) / 2;

  return (
    <AbsoluteFill style={{backgroundColor: BG, fontFamily: FONT}}>
      <div style={{
        position: 'absolute', left: padX, top: 100 * S, maxWidth: W - padX * 2,
        fontSize: 21 * S, letterSpacing: '.16em', color: MUTE, fontWeight: 600,
        whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis',
      }}>{data.slideMeta}</div>

      <svg width={W} height={H} style={{position: 'absolute', inset: 0}}>
        {Array.from({length: rows}).map((_, r) => (
          <g key={r}>
            <rect x={padX} y={rowTop(r)} width={panelW} height={panelH} rx={8 * S}
              fill="none" stroke={INK} strokeWidth={(r === 0 ? 2.5 : 1.5) * S} strokeOpacity={0.28} />
            <text x={padX} y={rowTop(r) - 14 * S} fontFamily={FONT} fontSize={25 * S} fontWeight={700}
              fill={r <= stageIdx ? INK : MUTE} fillOpacity={r <= stageIdx + 1 ? 1 : 0.35}>
              {(r === 0 ? data.startLabel : stages[r - 1].label).toUpperCase()}
            </text>
            {data.panelCounts && data.panelCounts[r] ? (
              <text x={padX + panelW} y={rowTop(r) - 14 * S} textAnchor="end" fontFamily={FONT}
                fontSize={30 * S} fontWeight={800} fill={r === rows - 1 ? ACCENT : INK}
                opacity={clamp(remap(p, r === 0 ? 0.02 : ranges[r - 1].b - 0.02, (r === 0 ? 0.02 : ranges[r - 1].b - 0.02) + 0.05, 0, 1), 0, 1)}>
                {data.panelCounts[r]}
              </text>
            ) : null}
          </g>
        ))}
        {dots}
      </svg>

      <div style={{
        position: 'absolute', left: counterLeft, top: 136 * S, width: counterW, height: counterH,
        borderRadius: 8 * S, background: '#fff', border: `${3 * S}px solid ${ACCENT}`,
        display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
      }}>
        <div style={{fontSize: 46 * S, fontWeight: 800, color: INK, lineHeight: 1}}>
          {curCount} / {total}
        </div>
        <div style={{fontSize: 20 * S, fontWeight: 700, color: ACCENT, marginTop: 5 * S}}>
          {pct >= 1 ? `${pct.toFixed(0)}% remain` : `${pct.toFixed(1)}% remain`}
        </div>
      </div>

      {data.scaleNote ? (
        <div style={{
          position: 'absolute', left: padX, bottom: 44 * S, maxWidth: W - padX * 2,
          fontSize: 24 * S, letterSpacing: '.08em', color: INK, fontWeight: 700,
          opacity: clamp(remap(p, 0.02, 0.10, 0, 1), 0, 1),
        }}>{data.scaleNote}</div>
      ) : null}
      {/* handleTop: chip top-right, inside the 5% title-safe inset, where this layout's
          bottom-right corner is occupied by content. */}
      <HandleChip handle={handle} fontSize={H * (H > W ? 0.016 : 0.024)} right={W * 0.07}
        bottom={handleTop ? H - H * 0.05 - 10 * S - H * (H > W ? 0.016 : 0.024) * 1.9 : H * (H > W ? 0.06 : 0.055)} opacity={0.9} />
    </AbsoluteFill>
  );
};
