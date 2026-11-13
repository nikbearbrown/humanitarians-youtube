/**
 * SqlDivergentFates — fork of the library `DivergentFates` (deckPatterns.tsx).
 *
 * FIX (vs the library component), from _qc/REPORT.md #1 (BLOCKER):
 *
 *   The library gates the endpoint badges — which carry each track's `label`
 *   and `outcome` — on:
 *       const badgeOp = remap(p, 0.82, 0.94, 0, 1);
 *   The composition is registered at 900 frames (30s) but this beat's audio is
 *   21.33s, and remotion_scenes.py renders the full composition then truncates
 *   with `-t`, so the clip only ever contains p <= 0.711. The badges were
 *   mathematically unreachable: the track labels and the SCAN/SEARCH outcomes
 *   NEVER appeared, on the beat that carries the episode's one insight.
 *
 *   FIX, three parts:
 *     1. badgeOp moves to remap(p, 0.55, 0.68) — comfortably inside the
 *        truncation window even if the audio shortens, and the badges then HOLD
 *        for the last third of the beat instead of flashing at the very end.
 *     2. This fork registers at 640 frames (21.33s), matching the measured
 *        audio, so nothing is truncated at all. Belt and braces: either fix
 *        alone would work; together the badges cannot be lost again.
 *     3. Curves end earlier (x1 = W*0.62 rather than W-300) so the badge boxes
 *        sit fully inside the frame with room for real SQL strings. The library
 *        box was 268px wide at fontSize 14 — about 32 characters. This reel's
 *        labels are up to 44, so the box widens and the label auto-shrinks and
 *        wraps rather than overflowing. Legibility beats designer intent.
 *
 * ALSO — #10 MINOR: registered at 1920x1080 with hardcoded pixels scaled by
 *   sc(H), so it renders at a true 3840x2160 under the existing --scale=2.
 *
 * Bezier geometry, arc-length travel and easing are VERBATIM from the library.
 *
 * REEL-LOCAL. Register per remotion-src/REGISTER.md.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import { HandleChip } from './ClaudeCodeBeat';
import {clamp, lerp, remap, easeOutCubic, cubicPoint, BG, INK, ACCENT, MUTE, WARN, GOOD, FONT, sc, Pt} from './sqlDeckKit';

const trackSchema = z.object({
  label: z.string(),
  outcome: z.string(),
  tone: z.enum(['good', 'warn']).default('good'),
  path: z.enum(['up', 'down']),
  notes: z.array(z.string()).default([]),
});

export const sqlDivergentFatesSchema = z.object({
  /** Lower-right author handle chip (e.g. "Supriya"). Omitted → no chip. */
  handle: z.string().optional(),
  data: z.object({
    slideMeta: z.string().default(''),
    startLabel: z.string().default('start'),
    splitLabel: z.string().default('split'),
    tracks: z.array(trackSchema).default([]),
    script: z.string().optional(),
  }),
});
export type SqlDivergentFatesProps = z.infer<typeof sqlDivergentFatesSchema>;

/** Greedy wrap by character budget — Remotion cannot measure the DOM. */
const wrap = (text: string, maxChars: number): string[] => {
  if (text.length <= maxChars) return [text];
  const words = text.split(' ');
  const lines: string[] = [];
  let cur = '';
  for (const w of words) {
    if (cur && (cur + ' ' + w).length > maxChars) {lines.push(cur); cur = w;}
    else cur = cur ? cur + ' ' + w : w;
  }
  if (cur) lines.push(cur);
  return lines;
};

export const SqlDivergentFates: React.FC<SqlDivergentFatesProps> = ({handle, data}) => {
  const frame = useCurrentFrame();
  const {width: W, height: H, durationInFrames} = useVideoConfig();
  const p = clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);
  const S = sc(H);

  const x0 = 150 * S;
  const xSplit = W * 0.30;
  // FIX 3: curves stop earlier so badges fit inside the frame.
  const x1 = W * 0.62;
  const yMid = H * 0.46, yUp = H * 0.20, yDn = H * 0.72;
  const tracks = data.tracks;
  const toneCol = (t: string) => (t === 'warn' ? WARN : t === 'good' ? GOOD : INK);
  const yEnd = (t: z.infer<typeof trackSchema>) => (t.path === 'up' ? yUp : yDn);
  const trackPath = (t: z.infer<typeof trackSchema>) => {
    const ye = yEnd(t);
    return `M ${x0} ${yMid} L ${xSplit} ${yMid} C ${(xSplit + x1) / 2} ${yMid}, ${(xSplit + x1) / 2} ${ye}, ${x1} ${ye}`;
  };

  const travelT = easeOutCubic(remap(p, 0.15, 0.55, 0, 1));
  const trackGeom = (t: z.infer<typeof trackSchema>) => {
    const ye = yEnd(t);
    const P0: Pt = {x: xSplit, y: yMid}, P1: Pt = {x: (xSplit + x1) / 2, y: yMid};
    const P2: Pt = {x: (xSplit + x1) / 2, y: ye}, P3: Pt = {x: x1, y: ye};
    const straightLen = xSplit - x0;
    const N = 60;
    const samples: {x: number; y: number; c: number}[] = [{x: xSplit, y: yMid, c: straightLen}];
    let acc = straightLen;
    let prev: Pt = {x: xSplit, y: yMid};
    for (let i = 1; i <= N; i++) {
      const pt = cubicPoint(P0, P1, P2, P3, i / N);
      acc += Math.hypot(pt.x - prev.x, pt.y - prev.y);
      samples.push({x: pt.x, y: pt.y, c: acc});
      prev = pt;
    }
    const total = acc;
    const pointAt = (f: number): Pt => {
      const target = total * f;
      if (target <= straightLen) return {x: x0 + target, y: yMid};
      for (let i = 1; i < samples.length; i++) {
        if (samples[i].c >= target) {
          const denom = samples[i].c - samples[i - 1].c;
          const seg = denom === 0 ? 0 : (target - samples[i - 1].c) / denom;
          return {
            x: lerp(samples[i - 1].x, samples[i].x, seg),
            y: lerp(samples[i - 1].y, samples[i].y, seg),
          };
        }
      }
      return {x: x1, y: ye};
    };
    return {total, pointAt};
  };

  // FIX 1: badges reveal at p=0.55 and are fully opaque by p=0.68 — well inside
  // the visible window, and they HOLD for the rest of the beat.
  const badgeOp = clamp(remap(p, 0.55, 0.68, 0, 1), 0, 1);

  // FIX 3: generous badge box, sized to what is actually left of the frame.
  const badgeX = x1 + 22 * S;
  // v2: right edge held inside the 5% title-safe inset (Gate V edge-bleed).
  const badgeW = W - badgeX - Math.max(50 * S, W * 0.05 + 8 * S);
  const labelChars = Math.floor(badgeW / (16 * S * 0.62));
  const outcomeChars = Math.floor(badgeW / (14 * S * 0.62));

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
        <line x1={xSplit} x2={xSplit} y1={110 * S} y2={H - 120 * S} stroke={MUTE}
          strokeWidth={1 * S} strokeDasharray={`${4 * S} ${5 * S}`} opacity={0.5} />
        <text x={x0} y={96 * S} fontFamily={FONT} fontSize={14 * S} fontWeight={700}
          fill={MUTE} letterSpacing=".08em">
          {data.startLabel.toUpperCase()}
        </text>
        <text x={xSplit + 12 * S} y={96 * S} fontFamily={FONT} fontSize={14 * S} fontWeight={700}
          fill={ACCENT} letterSpacing=".08em">
          {`→ ${data.splitLabel.toUpperCase()}`}
        </text>

        {tracks.map((d, i) => {
          const l = trackGeom(d).total;
          return (
            <path key={i} d={trackPath(d)} fill="none" stroke={toneCol(d.tone)} strokeWidth={3 * S}
              strokeDasharray={l} strokeDashoffset={l * (1 - travelT)} />
          );
        })}

        {/* notes */}
        {tracks.map((d, i) => (
          <g key={i}>
            {d.notes.map((nn, k) => (
              <text key={k} x={xSplit + 30 * S}
                y={(d.path === 'up' ? yUp - 12 * S : yDn + 30 * S) + k * 20 * S}
                fontFamily={FONT} fontSize={13 * S} fill={MUTE}
                opacity={clamp(remap(p, 0.30 + k * 0.06, 0.40 + k * 0.06, 0, 1), 0, 1)}>
                {`· ${nn}`}
              </text>
            ))}
          </g>
        ))}

        {/* travelling markers */}
        {tracks.map((d, i) => {
          const pt = trackGeom(d).pointAt(travelT);
          return <circle key={i} cx={pt.x} cy={pt.y} r={9 * S} fill={toneCol(d.tone)}
            stroke="#fff" strokeWidth={2 * S} />;
        })}

        {/* endpoint badges — label + outcome. THE FIX. */}
        {tracks.map((d, i) => {
          const ye = yEnd(d);
          const labelLines = wrap(d.label, labelChars);
          const outcomeLines = wrap(`→ ${d.outcome}`, outcomeChars);
          // Box geometry — top pad, label lines, gap, outcome lines, bottom pad.
          // QC pass 2 caught the first version double-counting the label line
          // height, which pushed the outcome baseline BELOW the box border.
          const PT = 8, LLH = 22, GAP = 6, OLH = 19, PB = 10;
          const boxH = (PT + labelLines.length * LLH + GAP + outcomeLines.length * OLH + PB) * S;
          const top = ye - boxH / 2;
          return (
            <g key={i} opacity={badgeOp}>
              <rect x={badgeX} y={ye - boxH / 2} width={badgeW} height={boxH} rx={6 * S}
                fill="#fff" stroke={toneCol(d.tone)} strokeWidth={2 * S} />
              {labelLines.map((ln, k) => (
                <text key={`l${k}`} x={badgeX + 16 * S}
                  y={top + (PT + 16 + k * LLH) * S}
                  fontFamily={FONT} fontSize={16 * S} fontWeight={800} fill={toneCol(d.tone)}>
                  {ln}
                </text>
              ))}
              {outcomeLines.map((ln, k) => (
                <text key={`o${k}`} x={badgeX + 16 * S}
                  y={top + (PT + labelLines.length * LLH + GAP + 14 + k * OLH) * S}
                  fontFamily={FONT} fontSize={14 * S} fontWeight={700} fill={toneCol(d.tone)}>
                  {ln}
                </text>
              ))}
            </g>
          );
        })}
      </svg>
      <HandleChip handle={handle} fontSize={H * (H > W ? 0.016 : 0.024)} right={W * 0.07}
        bottom={H * (H > W ? 0.06 : 0.055)} opacity={0.9} />
    </AbsoluteFill>
  );
};
