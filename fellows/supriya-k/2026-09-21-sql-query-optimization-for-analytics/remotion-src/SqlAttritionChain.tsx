/**
 * SqlAttritionChain — fork of the library `AttritionChain` (deckPatterns.tsx).
 *
 * FIXES (vs the library component), both from _qc/REPORT.md:
 *
 *  #3 MAJOR — slideMeta was occluded by the counter card. The library draws
 *     slideMeta as a div at (60, 34) and the counter as a LATER div at
 *     (W/2-150, 20) with a white background, so the tail of a long slideMeta
 *     paints underneath it. On this reel that hid "1 DOT = 1,000 ROWS" — the
 *     isotype scale declaration FACTCHECK.md row 6 cites as the honesty
 *     mitigation for showing 400 dots instead of 400,000 rows.
 *     FIX: the scale declaration moves to its own `scaleNote` prop, rendered
 *     BOTTOM-LEFT under the dot field where there is dead space and nothing to
 *     collide with. slideMeta also gains a hard `maxWidth` that stops short of
 *     the counter card, so this class of collision cannot recur.
 *
 *  #4 MAJOR — the beat ended mid-migration (counter frozen at "6 / 400") because
 *     the composition is registered at 900 frames (30s) while the beat's audio is
 *     20.57s, and remotion_scenes.py truncates the tail. FIX IS AT REGISTRATION:
 *     this fork is registered at 620 frames (20.67s) so p reaches 1.0 and the
 *     chain settles at its true final state. The internal timeline is also pulled
 *     in (outro hold 0.06 -> 0.14) so the settled state is HELD, not just reached.
 *
 *  #10 MINOR — registered at 1920x1080 with every hardcoded pixel scaled by
 *     sc(H), so it renders at a true 3840x2160 under the existing --scale=2.
 *
 * Motion math, palette, dot layout and easing are otherwise VERBATIM from the
 * library component. Pure function of the audio clock; no timers, no randomness
 * beyond the shared `seeded()`.
 *
 * REEL-LOCAL. Register per remotion-src/REGISTER.md.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import { HandleChip } from './ClaudeCodeBeat';
import {clamp, lerp, remap, easeOutCubic, seeded, BG, INK, ACCENT, MUTE, FONT, sc} from './sqlDeckKit';

export const sqlAttritionChainSchema = z.object({
  /** Lower-right author handle chip (e.g. "Supriya"). Omitted → no chip. */
  handle: z.string().optional(),
  data: z.object({
    title: z.string().default(''),
    /** Short. Keep under ~40 chars — it is width-capped so it cannot collide. */
    slideMeta: z.string().default(''),
    /** The isotype scale declaration. Rendered bottom-left, always visible. */
    scaleNote: z.string().default(''),
    total: z.number().default(400),
    startLabel: z.string().default('start'),
    stages: z.array(z.object({label: z.string(), survival: z.number()})).default([]),
    /** Optional exact figure per panel (start + each stage), e.g. "11,369 rows". When set,
     *  dots use the top ~64% of each panel and the figure settles in the band beneath. */
    panelCounts: z.array(z.string()).optional(),
    script: z.string().optional(),
  }),
});
export type SqlAttritionChainProps = z.infer<typeof sqlAttritionChainSchema>;

export const SqlAttritionChain: React.FC<SqlAttritionChainProps> = ({handle, data}) => {
  const frame = useCurrentFrame();
  const {width: W, height: H, durationInFrames} = useVideoConfig();
  const p = clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);
  const S = sc(H);

  const total = data.total;
  const stages = data.stages;
  const cols = stages.length + 1;
  // v2: counter moved inside the 5% title-safe inset (Gate V edge-bleed); panels drop
  // 14*S so their labels stay clear of it.
  const counterTop = Math.max(20 * S, H * 0.05 + 4 * S);
  const padX = 70 * S, padTop = 96 * S + (counterTop - 20 * S);
  // FIX #3: extra bottom padding reserves a clean band for the scale note.
  const padBot = 150 * S + (data.scaleNote ? 34 * S : 0);
  const laneW = (W - padX * 2) / cols;
  const panelW = laneW * 0.78;
  const panelTop = padTop + 10 * S;
  const panelH = H - panelTop - padBot;
  const labels = data.panelCounts;
  const dotsH = labels ? panelH * 0.64 : panelH;

  const counts = [total];
  for (const s of stages) counts.push(Math.round(counts[counts.length - 1] * s.survival));

  const colX = (c: number) => padX + laneW * c + laneW / 2;

  const gridPos = (i: number, count: number, c: number) => {
    const n = Math.max(1, count);
    const cc = Math.max(3, Math.ceil(Math.sqrt(n * (panelW / dotsH))));
    const rr = Math.max(1, Math.ceil(n / cc));
    const ipx = 16 * S, ipy = 18 * S;
    const uw = panelW - ipx * 2, uh = dotsH - ipy * 2;
    const gc = i % cc, gr = Math.floor(i / cc);
    const x = colX(c) - panelW / 2 + ipx + (cc === 1 ? uw / 2 : (gc / (cc - 1)) * uw);
    const y = panelTop + ipy + (rr === 1 ? uh / 2 : (gr / Math.max(1, rr - 1)) * uh);
    return {x, y};
  };
  const lossPos = (i: number, c: number) => ({
    x: colX(c) + (seeded(i) - 0.5) * panelW * 0.7,
    y: panelTop + panelH + 26 * S + seeded(i * 3) * 70 * S,
  });

  const dotR = (() => {
    const n = Math.max(1, counts[0]);
    const cc = Math.max(3, Math.ceil(Math.sqrt(n * (panelW / dotsH))));
    const rr = Math.max(1, Math.ceil(n / cc));
    const uw = panelW - 32 * S, uh = dotsH - 36 * S;
    const pitch = Math.min(cc > 1 ? uw / (cc - 1) : uw, rr > 1 ? uh / (rr - 1) : uh);
    return clamp(pitch * 0.34, 1.3 * S, 6 * S);
  })();

  // FIX #4: longer outro hold so the settled final state is actually held.
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
      stageIdx = k;
      break;
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
          const lp = lossPos(i, k);
          x = lerp(from.x, lp.x, t); y = lerp(from.y, lp.y, t);
          op = remap(t, 0, 0.85, 1, 0);
        }
        placed = true; break;
      }
      if (survives) {
        const set = gridPos(i, toCount, k + 1);
        x = set.x; y = set.y; op = 1; continue;
      }
      op = 0; placed = true; break;
    }
    if (!placed && op > 0) {
      const q = gridPos(i, counts[counts.length - 1], cols - 1);
      x = q.x; y = q.y;
    }
    if (op <= 0.01) continue;
    const isFinal = stageIdx >= stages.length && i < counts[counts.length - 1];
    dots.push(<circle key={i} cx={x} cy={y} r={dotR} fill={isFinal ? ACCENT : INK} opacity={op} />);
  }

  const counterW = 300 * S;
  const counterLeft = W / 2 - counterW / 2;

  return (
    <AbsoluteFill style={{backgroundColor: BG, fontFamily: FONT}}>
      {/* FIX #3: hard width cap — stops 24px short of the counter card, so a long
          slideMeta can never paint underneath it again. */}
      <div style={{
        position: 'absolute', left: 60 * S, top: 34 * S,
        maxWidth: counterLeft - 60 * S - 24 * S,
        fontSize: 13 * S, letterSpacing: '.18em', color: MUTE, fontWeight: 600,
        whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis',
      }}>
        {data.slideMeta}
      </div>

      <svg width={W} height={H} style={{position: 'absolute', inset: 0}}>
        {Array.from({length: cols}).map((_, c) => (
          <g key={c}>
            <rect x={colX(c) - panelW / 2} y={panelTop} width={panelW} height={panelH} rx={6 * S}
              fill="none" stroke={INK} strokeWidth={(c === 0 ? 2.5 : 1.5) * S} strokeOpacity={0.28} />
            <text x={colX(c)} y={panelTop - 16 * S} textAnchor="middle" fontFamily={FONT}
              fontSize={14 * S} fontWeight={700}
              fill={c <= stageIdx ? INK : MUTE} fillOpacity={c <= stageIdx + 1 ? 1 : 0.35}>
              {(c === 0 ? data.startLabel : stages[c - 1].label).toUpperCase()}
            </text>
          </g>
        ))}
        {dots}
        {labels ? labels.slice(0, cols).map((lab, c) => {
          // start figure shows with the intro; each stage's figure once that stage settles
          const at = c === 0 ? 0.02 : ranges[c - 1].b - 0.02;
          const op = clamp(remap(p, at, at + 0.05, 0, 1), 0, 1);
          return (
            <text key={`lab${c}`} x={colX(c)} y={panelTop + dotsH + (panelH - dotsH) * 0.58}
              textAnchor="middle" dominantBaseline="middle" fontFamily={FONT} fontSize={30 * S}
              fontWeight={800} fill={c === cols - 1 ? ACCENT : INK} opacity={op}>{lab}</text>
          );
        }) : null}
      </svg>

      {/* counter — unchanged position, now guaranteed collision-free */}
      <div style={{
        position: 'absolute', left: counterLeft, top: counterTop,
        width: counterW, height: 58 * S, borderRadius: 6 * S,
        background: '#fff', border: `${2 * S}px solid ${ACCENT}`,
        display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
      }}>
        <div style={{fontSize: 30 * S, fontWeight: 800, color: INK, lineHeight: 1}}>
          {curCount} / {total}
        </div>
        <div style={{fontSize: 13 * S, fontWeight: 700, color: ACCENT, marginTop: 3 * S}}>
          {pct >= 1 ? `${pct.toFixed(0)}% remain` : `${pct.toFixed(1)}% remain`}
        </div>
      </div>

      {/* FIX #3: the isotype scale declaration, bottom-left, always readable.
          FACTCHECK.md row 6 depends on this being on screen. */}
      {data.scaleNote ? (
        <div style={{
          position: 'absolute', left: 60 * S, bottom: 46 * S,
          maxWidth: W - 120 * S,
          fontSize: 15 * S, letterSpacing: '.10em', color: INK, fontWeight: 700,
          opacity: clamp(remap(p, 0.02, 0.10, 0, 1), 0, 1),
        }}>
          {data.scaleNote}
        </div>
      ) : null}
      <HandleChip handle={handle} fontSize={H * (H > W ? 0.016 : 0.024)} right={W * 0.07}
        bottom={H * (H > W ? 0.06 : 0.055)} opacity={0.9} />
    </AbsoluteFill>
  );
};
