/**
 * SqlDivergentFates916 — portrait (9:16) variant of B06's divergence beat.
 *
 * RE-BAND: the landscape version forks LEFT→RIGHT with badges stacked on the
 * right. Portrait forks TOP→DOWN: a shared trunk descends from the top, splits,
 * and the two tracks settle at different depths — the "good" track levels off
 * high, the "warn" track keeps falling. Each track's badge is a full-width block
 * directly beneath its own endpoint, so the vertical position and the tone
 * colour both identify it. This is the doctrine's "stacks TOP AND BOTTOM".
 *
 * Carries the landscape fix forward (_qc/REPORT.md #1): the badges reveal at
 * p=0.55 and the composition is registered at the measured audio length, so
 * they are reachable and then HELD. Badge box geometry uses the corrected
 * padding/line-height constants from QC pass 2.
 *
 * No library `DivergentFates916` (checked Root.tsx: absent).
 * Registered 1080x1920; --scale=2 renders 2160x3840 native.
 *
 * REEL-LOCAL. Register per remotion-src/REGISTER.md.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import { HandleChip } from './ClaudeCodeBeat';
import {clamp, lerp, remap, easeOutCubic, cubicPoint, BG, INK, ACCENT, MUTE, WARN, FONT, scW, wrapText, Pt} from './sqlDeckKit';

const trackSchema = z.object({
  label: z.string(),
  outcome: z.string(),
  tone: z.enum(['good', 'warn']).default('good'),
  path: z.enum(['up', 'down']),
  notes: z.array(z.string()).default([]),
});

export const sqlDivergentFates916Schema = z.object({
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
export type SqlDivergentFates916Props = z.infer<typeof sqlDivergentFates916Schema>;

export const SqlDivergentFates916: React.FC<SqlDivergentFates916Props> = ({handle, data}) => {
  const frame = useCurrentFrame();
  const {width: W, height: H, durationInFrames} = useVideoConfig();
  const p = clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);
  const S = scW(W);

  const tracks = data.tracks;
  const toneCol = (t: string) => (t === 'warn' ? WARN : INK);

  // Vertical trunk, then a downward fork.
  const cx = W * 0.5;
  const yStart = 294 * S;
  const ySplit = 474 * S;
  // 'up' = the good track levels off HIGH; 'down' = the bad track keeps falling.
  const xEnd = (t: z.infer<typeof trackSchema>) => (t.path === 'up' ? W * 0.72 : W * 0.28);
  const yEnd = (t: z.infer<typeof trackSchema>) => (t.path === 'up' ? 700 * S : 1180 * S);

  const trackPath = (t: z.infer<typeof trackSchema>) => {
    const xe = xEnd(t), ye = yEnd(t);
    return `M ${cx} ${yStart} L ${cx} ${ySplit} C ${cx} ${(ySplit + ye) / 2}, ${xe} ${(ySplit + ye) / 2}, ${xe} ${ye}`;
  };

  const travelT = easeOutCubic(remap(p, 0.15, 0.55, 0, 1));
  const geom = (t: z.infer<typeof trackSchema>) => {
    const xe = xEnd(t), ye = yEnd(t);
    const P0: Pt = {x: cx, y: ySplit}, P1: Pt = {x: cx, y: (ySplit + ye) / 2};
    const P2: Pt = {x: xe, y: (ySplit + ye) / 2}, P3: Pt = {x: xe, y: ye};
    const straight = ySplit - yStart;
    const N = 60;
    const samples: {x: number; y: number; c: number}[] = [{x: cx, y: ySplit, c: straight}];
    let acc = straight; let prev: Pt = {x: cx, y: ySplit};
    for (let i = 1; i <= N; i++) {
      const pt = cubicPoint(P0, P1, P2, P3, i / N);
      acc += Math.hypot(pt.x - prev.x, pt.y - prev.y);
      samples.push({x: pt.x, y: pt.y, c: acc}); prev = pt;
    }
    const total = acc;
    const pointAt = (f: number): Pt => {
      const target = total * f;
      if (target <= straight) return {x: cx, y: yStart + target};
      for (let i = 1; i < samples.length; i++) {
        if (samples[i].c >= target) {
          const den = samples[i].c - samples[i - 1].c;
          const seg = den === 0 ? 0 : (target - samples[i - 1].c) / den;
          return {x: lerp(samples[i - 1].x, samples[i].x, seg), y: lerp(samples[i - 1].y, samples[i].y, seg)};
        }
      }
      return {x: xe, y: ye};
    };
    return {total, pointAt};
  };

  const badgeOp = clamp(remap(p, 0.55, 0.68, 0, 1), 0, 1);

  // Badges sit BELOW every curve (both tracks have ended by y=1180) and are
  // half-width, offset toward their own track's side. QC pass 1 on the portrait
  // cut made them full-width, so the warn track's path ran straight through the
  // good track's badge (rubric #4 collision) — and a full-width badge leaves no
  // clear channel for the other track's leader line either.
  const badgeYUp = 1330 * S;      // the 'up' (good) track's badge
  const badgeYDown = 1560 * S;    // the 'down' (warn) track's badge
  const badgeOf = (t: z.infer<typeof trackSchema>) =>
    t.path === 'up'
      ? {x: 0.40 * W, w: W - 56 * S - 0.40 * W, y: badgeYUp}
      : {x: 56 * S, w: 0.60 * W - 56 * S, y: badgeYDown};
  const PT = 14, LLH = 36, GAP = 8, OLH = 32, PB = 16;

  return (
    <AbsoluteFill style={{backgroundColor: BG, fontFamily: FONT}}>
      <div style={{
        position: 'absolute', left: 56 * S, top: 100 * S, maxWidth: W - 112 * S,
        fontSize: 21 * S, letterSpacing: '.14em', color: MUTE, fontWeight: 600,
      }}>
        {wrapText(data.slideMeta, 40).map((ln, i) => <div key={i}>{ln}</div>)}
      </div>

      <svg width={W} height={H} style={{position: 'absolute', inset: 0}}>
        <text x={cx} y={yStart - 34 * S} textAnchor="middle" fontFamily={FONT} fontSize={24 * S}
          fontWeight={700} fill={MUTE} letterSpacing=".06em">
          {data.startLabel.toUpperCase()}
        </text>
        <line x1={56 * S} x2={W - 56 * S} y1={ySplit} y2={ySplit} stroke={MUTE}
          strokeWidth={1.5 * S} strokeDasharray={`${5 * S} ${6 * S}`} opacity={0.5} />
        <text x={56 * S} y={ySplit - 16 * S} fontFamily={FONT} fontSize={24 * S} fontWeight={700}
          fill={ACCENT} letterSpacing=".06em">
          {`→ ${data.splitLabel.toUpperCase()}`}
        </text>

        {tracks.map((d, i) => {
          const l = geom(d).total;
          return (
            <path key={i} d={trackPath(d)} fill="none" stroke={toneCol(d.tone)} strokeWidth={5 * S}
              strokeDasharray={l} strokeDashoffset={l * (1 - travelT)} />
          );
        })}

        {tracks.map((d, i) => (
          <g key={i}>
            {d.notes.map((nn, k) => (
              /* Beside the track's OWN endpoint, on the outward side. QC pass 1
                 put each track's notes on the opposite side from its endpoint,
                 so neither set could be attributed to a track. */
              <text key={k}
                x={d.path === 'up' ? W - 56 * S : 0.28 * W + 64 * S}
                textAnchor={d.path === 'up' ? 'end' : 'start'}
                /* ASYMMETRIC, because the two tracks have different clearances:
                     'up'   — BELOW its endpoint. Above it, the descending ink
                              curve clips the first line (QC pass 2).
                     'down' — ABOVE its endpoint. Below it, the third line runs
                              under the 'up' track's badge (QC pass 3).
                   Both placements were verified against the bezier's x at those
                   y values, not guessed. */
                y={(d.path === 'up' ? yEnd(d) + 104 * S : yEnd(d) - 130 * S) + k * 34 * S}
                fontFamily={FONT} fontSize={23 * S} fill={MUTE}
                opacity={clamp(remap(p, 0.30 + k * 0.06, 0.40 + k * 0.06, 0, 1), 0, 1)}>
                {`· ${nn}`}
              </text>
            ))}
          </g>
        ))}

        {tracks.map((d, i) => {
          const pt = geom(d).pointAt(travelT);
          return <circle key={i} cx={pt.x} cy={pt.y} r={14 * S} fill={toneCol(d.tone)}
            stroke="#fff" strokeWidth={3 * S} />;
        })}

        {/* badges — full-width blocks directly beneath their own endpoint */}
        {tracks.map((d, i) => {
          const bx = badgeOf(d);
          const labelChars = Math.floor(bx.w / (27 * S * 0.62));
          const outChars = Math.floor(bx.w / (24 * S * 0.62));
          const lines = wrapText(d.label, labelChars);
          const outs = wrapText(`→ ${d.outcome}`, outChars);
          const boxH = (PT + lines.length * LLH + GAP + outs.length * OLH + PB) * S;
          const col = toneCol(d.tone);
          return (
            <g key={i} opacity={badgeOp}>
              {/* leader: endpoint → its own badge, in the track's tone colour */}
              {/* a short stub, not a full line to the badge — a long leader
                  would run straight through the notes now sitting below. */}
              <line x1={xEnd(d)} x2={xEnd(d)} y1={yEnd(d) + 16 * S} y2={yEnd(d) + 74 * S}
                stroke={col} strokeWidth={3 * S} strokeOpacity={0.5} />
              <rect x={bx.x} y={bx.y} width={bx.w} height={boxH} rx={10 * S}
                fill="#fff" stroke={col} strokeWidth={3 * S} />
              {lines.map((ln, k) => (
                <text key={`l${k}`} x={bx.x + 24 * S} y={bx.y + (PT + 26 + k * LLH) * S}
                  fontFamily={FONT} fontSize={27 * S} fontWeight={800} fill={col}>
                  {ln}
                </text>
              ))}
              {outs.map((ln, k) => (
                <text key={`o${k}`} x={bx.x + 24 * S}
                  y={bx.y + (PT + lines.length * LLH + GAP + 24 + k * OLH) * S}
                  fontFamily={FONT} fontSize={24 * S} fontWeight={700} fill={col}>
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
