import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {z} from 'zod';
import {CLAUDE} from '../tokens/claude';
import {SAFE, SAFE916} from '../tokens/layout';
import {ACCENT, Card, INK, SANS, SERIF, SOFT, STAGE, Spark, useBeat} from './SocialAiVisibility';

/**
 * ContentRepurpose.tsx — concept illustrations (C3) for the ai-explainer reel
 * "AI Content vs. Human Creativity: What Works Better?" (@Shubh & @HumanitariansAI).
 *
 * One human-made long-form video is the source; AI finds its moments, cuts the
 * clips, cascades the transcript into other formats, and is checked against a
 * voice guide; the last scene sorts tasks toward AI or people.
 *
 * These are the 16:9 layouts. Native 9:16 layouts live in ContentRepurpose916.tsx
 * and share these zod schemas; Root.tsx registers `<Name>` and `<Name>916`.
 * Pure functions of the beat clock: `durationSeconds` = the beat's measured audio,
 * and every `*At` prop is a beat fraction placed on the spoken word.
 *
 * Palette: claude C3 stage — cream, warm ink, ONE terracotta accent per beat
 * (playhead · pick ring · trace-back · off-brand flag · verdict rule). Accent is
 * never used for text (WCAG on cream). All example copy is labelled illustrative.
 */

const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const durationProp = {durationSeconds: z.number().default(16)};

export const SparkLine: React.FC<{text: string}> = ({text}) => (
  <div style={{position: 'absolute', left: SAFE.x, top: SAFE.y, width: SAFE.w, display: 'flex', alignItems: 'center',
    justifyContent: 'center', gap: 21}}>
    <Spark size={47} />
    <span style={{fontFamily: SERIF, fontSize: 52, color: INK, fontWeight: 600, lineHeight: 1.1}}>{text}</span>
  </div>
);

export const LogoBug: React.FC<{portrait?: boolean}> = ({portrait = false}) => {
  const S = portrait ? SAFE916 : SAFE;
  const W = portrait ? 1080 : 1920, H = portrait ? 1920 : 1080;
  return <Img src={staticFile('hai-wordmark-outlined.svg')}
    style={{position: 'absolute', right: W - S.r, bottom: H - S.b, height: portrait ? 54 : 34, opacity: 0.55}} />;
};

/** Simple line-drawn format glyphs (ink strokes on a transparent box). */
export type GlyphKind = 'video' | 'lines' | 'doc' | 'slides' | 'bubble' | 'mail';
export const Glyph: React.FC<{kind: GlyphKind; size: number; color?: string}> = ({kind, size, color = INK}) => {
  const sw = 5;
  const common = {fill: 'none', stroke: color, strokeWidth: sw, strokeLinecap: 'round' as const, strokeLinejoin: 'round' as const};
  return (
    <svg width={size} height={size} viewBox="0 0 100 100" style={{flexShrink: 0}}>
      {kind === 'video' && (<>
        <rect x={8} y={20} width={84} height={60} rx={10} {...common} />
        <path d="M 42 36 L 64 50 L 42 64 Z" fill={color} stroke="none" />
      </>)}
      {kind === 'lines' && [24, 40, 56, 72].map((y, i) => (
        <line key={y} x1={14} y1={y} x2={i === 3 ? 60 : 86} y2={y} {...common} />
      ))}
      {kind === 'doc' && (<>
        <path d="M 22 10 L 64 10 L 80 26 L 80 90 L 22 90 Z" {...common} />
        <line x1={32} y1={40} x2={70} y2={40} {...common} />
        <line x1={32} y1={56} x2={70} y2={56} {...common} />
        <line x1={32} y1={72} x2={56} y2={72} {...common} />
      </>)}
      {kind === 'slides' && (<>
        <rect x={34} y={14} width={54} height={54} rx={6} {...common} opacity={0.45} />
        <rect x={23} y={24} width={54} height={54} rx={6} {...common} opacity={0.7} />
        <rect x={12} y={34} width={54} height={54} rx={6} fill={CLAUDE.CARD} stroke={color} strokeWidth={sw} />
      </>)}
      {kind === 'bubble' && (
        <path d="M 14 18 L 86 18 L 86 66 L 46 66 L 28 84 L 30 66 L 14 66 Z" {...common} />
      )}
      {kind === 'mail' && (<>
        <rect x={10} y={22} width={80} height={56} rx={6} {...common} />
        <path d="M 12 26 L 50 54 L 88 26" {...common} />
      </>)}
    </svg>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B02 — the human-made long-form video is the source; AI scans for moments
// ─────────────────────────────────────────────────────────────────────────────
export const repurposeSourceSchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('Start with one human original.'),
  videoLabel: z.string().default('YOUR LONG-FORM VIDEO'),
  videoNote: z.string().default('made by a person'),
  barAt: z.number().default(0.03),
  chapters: z.array(z.object({label: z.string(), at: z.number()})).default([
    {label: 'Ideas', at: 0.31},
    {label: 'Stories', at: 0.365},
    {label: 'Your voice', at: 0.415},
  ]),
  jobLine: z.string().default('AI’s job: find the best moments — not invent them.'),
  jobAt: z.number().default(0.52),
  scanAt: z.number().default(0.7),
  scanSpan: z.number().default(0.14),
  moments: z.array(z.object({label: z.string(), pos: z.number(), at: z.number()})).default([
    {label: 'The hook', pos: 0.256, at: 0.85},
    {label: 'The story', pos: 0.59, at: 0.89},
    {label: 'The tip', pos: 0.923, at: 0.93},
  ]),
});

export const RepurposeSource: React.FC<z.infer<typeof repurposeSourceSchema>> = (props) => {
  const {pop, ramp, p} = useBeat(props.durationSeconds);
  const S = SAFE;
  const bar = {x: S.x, y: 300, w: S.w, h: 240};
  const drawn = ramp(props.barAt, 0.14);
  const n = props.chapters.length;
  const segW = bar.w / n;
  const scanT = clamp01((p - props.scanAt) / props.scanSpan);
  const scanVis = p > props.scanAt ? 1 - ramp(props.scanAt + props.scanSpan + 0.01, 0.04) : 0;
  const headX = bar.x + 30 + scanT * (bar.w - 60);
  const holes = Array.from({length: 30}, (_, i) => bar.x + 30 + i * ((bar.w - 60) / 29));
  const hlW = bar.w * 0.11;
  const cardW = 300, cardH = 112, cardTop = bar.y + bar.h + 58;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} />
      <div style={{position: 'absolute', left: S.x, top: 196, width: S.w, display: 'flex', alignItems: 'baseline', gap: 26,
        opacity: pop(props.barAt)}}>
        <span style={{fontFamily: SANS, fontSize: 44, fontWeight: 700, letterSpacing: '0.1em', color: INK}}>{props.videoLabel}</span>
        <span style={{fontFamily: SERIF, fontSize: 58, fontStyle: 'italic', color: SOFT}}>{props.videoNote}</span>
      </div>
      {/* the film strip — clipped to the drawn width so it reads as the bar being laid down */}
      <div style={{position: 'absolute', left: bar.x, top: bar.y, width: bar.w * drawn, height: bar.h, overflow: 'hidden',
        borderRadius: 26}}>
        <div style={{position: 'absolute', left: 0, top: 0, width: bar.w, height: bar.h, background: CLAUDE.CARD,
          border: `3px solid ${CLAUDE.BORDER}`, borderRadius: 26, boxSizing: 'border-box'}} />
        {props.chapters.map((c, i) => {
          const t = pop(c.at);
          return (
            <div key={i} style={{position: 'absolute', left: i * segW + 10, top: 44, width: segW - 20, height: bar.h - 88,
              borderRadius: 14, background: CLAUDE.FOOTER, border: `2px solid ${CLAUDE.BORDER}`, boxSizing: 'border-box',
              display: 'flex', alignItems: 'center', justifyContent: 'flex-start', paddingLeft: 34, opacity: 0.4 + 0.6 * t}}>
              <span style={{fontFamily: SERIF, fontSize: 64, fontWeight: 700, color: INK, opacity: t,
                transform: `translateY(${(1 - t) * 14}px)`}}>{c.label}</span>
            </div>
          );
        })}
        {holes.map((x, i) => (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: x - bar.x - 9, top: 14, width: 18, height: 16, borderRadius: 4, background: CLAUDE.BORDER}} />
            <div style={{position: 'absolute', left: x - bar.x - 9, top: bar.h - 30, width: 18, height: 16, borderRadius: 4, background: CLAUDE.BORDER}} />
          </React.Fragment>
        ))}
        {props.moments.map((m, i) => {
          const t = pop(m.at);
          return <div key={i} style={{position: 'absolute', left: m.pos * bar.w - hlW / 2, top: 36, width: hlW,
            height: bar.h - 72, borderRadius: 14, border: `5px solid ${INK}`, background: 'rgba(61,57,41,0.10)',
            boxSizing: 'border-box', opacity: t}} />;
        })}
      </div>
      {/* the one accent: a terracotta playhead scanning for moments */}
      <div style={{position: 'absolute', left: headX - 4, top: bar.y - 34, width: 8, height: bar.h + 68, borderRadius: 4,
        background: ACCENT, opacity: scanVis}} />
      <div style={{position: 'absolute', left: headX - 17, top: bar.y - 52, width: 34, height: 34, borderRadius: 17,
        background: ACCENT, opacity: scanVis}} />
      {props.moments.map((m, i) => {
        const t = pop(m.at);
        const cx = bar.x + m.pos * bar.w;
        const left = Math.min(S.r - cardW, Math.max(S.x, cx - cardW / 2));
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: cx - 3, top: bar.y + bar.h, width: 6, height: 58 * t, background: INK}} />
            <Card style={{position: 'absolute', left, top: cardTop, width: cardW, height: cardH, display: 'flex',
              alignItems: 'center', justifyContent: 'center', opacity: t, transform: `translateY(${(1 - t) * -24}px)`}}>
              <span style={{fontFamily: SERIF, fontSize: 56, fontWeight: 700, color: INK}}>{m.label}</span>
            </Card>
          </React.Fragment>
        );
      })}
      <div style={{position: 'absolute', left: S.x, width: S.w, top: 860, textAlign: 'center', fontFamily: SERIF,
        fontSize: 58, color: INK, lineHeight: 1.15, opacity: pop(props.jobAt),
        transform: `translateY(${(1 - pop(props.jobAt)) * 16}px)`}}>{props.jobLine}</div>
      <LogoBug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B04 — three moments become three vertical clips with example captions
// ─────────────────────────────────────────────────────────────────────────────
export const repurposeClipsSchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('Three moments. Three clips.'),
  clips: z.array(z.object({platform: z.string(), moment: z.string(), caption: z.string(), pos: z.number(), at: z.number()})).default([
    {platform: 'Reels', moment: 'Hook', caption: '“Nobody tells you this about posting.”', pos: 0.14, at: 0.15},
    {platform: 'TikTok', moment: 'Story', caption: '“The week everything went wrong.”', pos: 0.5, at: 0.215},
    {platform: 'Shorts', moment: 'Tip', caption: '“Try this before your next post.”', pos: 0.84, at: 0.275},
  ]),
  captionsAt: z.number().default(0.375),
  aiLine: z.string().default('AI trims, resizes and drafts the captions.'),
  aiAt: z.number().default(0.55),
  pickIndex: z.number().default(1),
  pickAt: z.number().default(0.85),
  pickLabel: z.string().default('your pick'),
  youLine: z.string().default('You choose the cut.'),
  caption: z.string().default('Example captions — illustrative'),
});

/** A vertical phone frame; the screen shows a play glyph, the moment and on-screen text bars. */
export const Phone: React.FC<{w: number; h: number; moment: string; momentPx: number; barsIn: number; style?: React.CSSProperties}> = (
  {w, h, moment, momentPx, barsIn, style}) => (
  <div style={{position: 'absolute', width: w, height: h, borderRadius: w * 0.14, background: INK, boxSizing: 'border-box',
    padding: w * 0.045, ...style}}>
    <div style={{width: '100%', height: '100%', borderRadius: w * 0.1, background: CLAUDE.CARD, position: 'relative',
      display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: h * 0.03}}>
      <div style={{position: 'absolute', top: h * 0.03, width: w * 0.28, height: h * 0.018, borderRadius: 6, background: CLAUDE.BORDER}} />
      <svg width={w * 0.34} height={w * 0.34} viewBox="0 0 100 100">
        <circle cx={50} cy={50} r={44} fill={CLAUDE.FOOTER} stroke={CLAUDE.BORDER} strokeWidth={4} />
        <path d="M 40 30 L 70 50 L 40 70 Z" fill={INK} />
      </svg>
      <span style={{fontFamily: SERIF, fontSize: momentPx, fontWeight: 700, color: INK, lineHeight: 1}}>{moment}</span>
      {/* on-screen text: two caption bars near the bottom of the screen */}
      <div style={{position: 'absolute', bottom: h * 0.07, left: '12%', width: '76%', display: 'flex', flexDirection: 'column',
        alignItems: 'center', gap: h * 0.018, opacity: barsIn}}>
        <div style={{width: '100%', height: h * 0.032, borderRadius: 8, background: SOFT, opacity: 0.8}} />
        <div style={{width: '64%', height: h * 0.032, borderRadius: 8, background: SOFT, opacity: 0.8}} />
      </div>
    </div>
  </div>
);

export const RepurposeClips: React.FC<z.infer<typeof repurposeClipsSchema>> = (props) => {
  const {pop, width, height} = useBeat(props.durationSeconds);
  const S = SAFE;
  const bar = {x: S.x, y: 134, w: S.w, h: 50};
  const phoneW = 228, phoneH = 405, phoneTop = 300;
  const colW = S.w / props.clips.length;
  const segW = bar.w * 0.1;
  const pickIn = pop(props.pickAt);
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} />
      <div style={{position: 'absolute', left: bar.x, top: bar.y, width: bar.w, height: bar.h, borderRadius: 16,
        background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, opacity: pop(0.02)}} />
      <svg width={width} height={height} style={{position: 'absolute', inset: 0}}>
        {props.clips.map((c, i) => {
          const t = pop(c.at);
          const sx = bar.x + c.pos * bar.w, cx = S.x + colW * (i + 0.5);
          const y0 = bar.y + bar.h, y1 = phoneTop - 72;
          const d = `M ${sx} ${y0} C ${sx} ${(y0 + y1) / 2}, ${cx} ${(y0 + y1) / 2}, ${cx} ${y1}`;
          return <path key={i} d={d} fill="none" stroke={SOFT} strokeWidth={3} strokeDasharray={600}
            strokeDashoffset={600 * (1 - t)} opacity={0.7} />;
        })}
      </svg>
      {props.clips.map((c, i) => {
        const t = pop(c.at);
        const cx = S.x + colW * (i + 0.5);
        const capIn = pop(props.captionsAt + i * 0.03);
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: bar.x + c.pos * bar.w - segW / 2, top: bar.y + 6, width: segW,
              height: bar.h - 12, borderRadius: 10, background: INK, opacity: 0.3 + 0.55 * pop(0.04)}} />
            <div style={{position: 'absolute', left: cx - 200, width: 400, top: phoneTop - 68, textAlign: 'center',
              fontFamily: SANS, fontSize: 40, fontWeight: 700, color: SOFT, opacity: t}}>{c.platform}</div>
            <Phone w={phoneW} h={phoneH} moment={c.moment} momentPx={56} barsIn={capIn}
              style={{left: cx - phoneW / 2, top: phoneTop + 8, opacity: t,
                transform: `translateY(${(1 - t) * -70}px) scale(${0.7 + 0.3 * t})`}} />
            <div style={{position: 'absolute', left: cx - colW / 2 + 20, width: colW - 40, top: phoneTop + phoneH + 62,
              textAlign: 'center', fontFamily: SERIF, fontStyle: 'italic', fontSize: 42, color: INK, lineHeight: 1.18,
              opacity: capIn}}>{c.caption}</div>
          </React.Fragment>
        );
      })}
      {(() => {
        const cx = S.x + colW * (props.pickIndex + 0.5);
        const pad = 16;
        return (
          <>
            <div style={{position: 'absolute', left: cx - phoneW / 2 - pad, top: phoneTop + 8 - pad, width: phoneW + pad * 2,
              height: phoneH + pad * 2, borderRadius: phoneW * 0.14 + pad, border: `7px solid ${ACCENT}`, boxSizing: 'border-box',
              opacity: pickIn, transform: `scale(${1.08 - 0.08 * pickIn})`}} />
            <div style={{position: 'absolute', left: cx - 120, width: 240, top: phoneTop + 8 + phoneH - 34, height: 58,
              borderRadius: 29, background: CLAUDE.CARD, border: `3px solid ${ACCENT}`, display: 'flex', alignItems: 'center',
              justifyContent: 'center', fontFamily: SANS, fontSize: 40, fontWeight: 700, color: INK, opacity: pickIn}}>{props.pickLabel}</div>
          </>
        );
      })()}
      <div style={{position: 'absolute', left: S.x, width: S.w, top: 896, textAlign: 'center', fontFamily: SERIF, fontSize: 50,
        color: INK, lineHeight: 1.1}}>
        <span style={{opacity: pop(props.aiAt)}}>{props.aiLine}</span>
        <span style={{opacity: pickIn, fontWeight: 700}}>{'  '}{props.youLine}</span>
      </div>
      <div style={{position: 'absolute', left: S.x, top: S.b - 44, fontFamily: SANS, fontSize: 40, color: SOFT,
        opacity: pop(props.captionsAt)}}>{props.caption}</div>
      <LogoBug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B05 — the cascade: video → transcript → blog → carousel → posts + newsletter
// ─────────────────────────────────────────────────────────────────────────────
const nodeSchema = z.object({label: z.string(), glyph: z.enum(['video', 'lines', 'doc', 'slides', 'bubble', 'mail']), at: z.number()});
export const repurposeCascadeSchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('One recording, a week of content.'),
  nodes: z.array(nodeSchema).default([
    {label: 'Long-form video', glyph: 'video', at: 0.02},
    {label: 'Transcript', glyph: 'lines', at: 0.11},
    {label: 'Blog post', glyph: 'doc', at: 0.18},
    {label: 'Carousel', glyph: 'slides', at: 0.365},
  ]),
  leaves: z.array(nodeSchema).default([
    {label: 'Social posts', glyph: 'bubble', at: 0.51},
    {label: 'Newsletter', glyph: 'mail', at: 0.59},
  ]),
  weekLine: z.string().default('One recording — a whole week of content.'),
  weekAt: z.number().default(0.72),
  traceAt: z.number().default(0.86),
  traceLabel: z.string().default('Every piece traces back to the original.'),
});

export const RepurposeCascade: React.FC<z.infer<typeof repurposeCascadeSchema>> = (props) => {
  const {pop, ramp, width, height} = useBeat(props.durationSeconds);
  const S = SAFE;
  const cols = props.nodes.length + 1;
  const gap = 74, leafW = 380;
  const nw = (S.w - leafW - gap * (cols - 1)) / (cols - 1);
  const nh = 270, cy = 500;
  const colX = (i: number) => S.x + i * (nw + gap);
  const leafH = 200, leafGap = 34;
  const leavesH = props.leaves.length * leafH + (props.leaves.length - 1) * leafGap;
  const leafY = (k: number) => cy - leavesH / 2 + k * (leafH + leafGap);
  const braceY = Math.max(cy + nh / 2, cy + leavesH / 2) + 40;
  const lastX = colX(cols - 1);
  const traceT = ramp(props.traceAt, 0.1);
  // trace: from the top of the leaves column, arcing over the chain, down into the original's top
  const x0 = colX(0) + nw / 2, xL = lastX + leafW / 2, yTopLeaf = leafY(0), yTopNode = cy - nh / 2;
  const traceD = `M ${xL} ${yTopLeaf - 8} C ${xL} ${yTopLeaf - 150}, ${x0} ${yTopNode - 170}, ${x0} ${yTopNode - 10}`;
  const NodeCard: React.FC<{n: z.infer<typeof nodeSchema>; x: number; y: number; w: number; h: number; horizontal?: boolean}> = ({n, x, y, w, h, horizontal}) => {
    const t = pop(n.at);
    return (
      <Card style={{position: 'absolute', left: x, top: y, width: w, height: h, boxSizing: 'border-box',
        display: 'flex', flexDirection: horizontal ? 'row' : 'column', alignItems: 'center', justifyContent: 'center',
        gap: horizontal ? 16 : 14, padding: '0 18px', opacity: t, transform: `scale(${0.86 + 0.14 * t})`}}>
        <Glyph kind={n.glyph} size={horizontal ? 84 : 104} />
        <span style={{fontFamily: SERIF, fontSize: 52, fontWeight: 700, color: INK, lineHeight: 1.05,
          textAlign: horizontal ? 'left' : 'center'}}>{n.label}</span>
      </Card>
    );
  };
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} />
      <svg width={width} height={height} style={{position: 'absolute', inset: 0}}>
        <defs>
          <marker id="crArrow" viewBox="0 0 10 10" refX={8} refY={5} markerWidth={5} markerHeight={5} orient="auto">
            <path d="M 0 0 L 10 5 L 0 10 Z" fill={SOFT} />
          </marker>
          <marker id="crArrowAccent" viewBox="0 0 10 10" refX={8} refY={5} markerWidth={4} markerHeight={4} orient="auto">
            <path d="M 0 0 L 10 5 L 0 10 Z" fill={ACCENT} />
          </marker>
        </defs>
        {props.nodes.slice(1).map((n, i) => {
          const t = ramp(n.at - 0.03, 0.04);
          const xa = colX(i) + nw + 8, xb = colX(i + 1) - 10;
          return t > 0 ? <line key={i} x1={xa} y1={cy} x2={xa + (xb - xa) * t} y2={cy} stroke={SOFT} strokeWidth={5}
            markerEnd={t > 0.95 ? 'url(#crArrow)' : undefined} /> : null;
        })}
        {props.leaves.map((l, k) => {
          const t = ramp(l.at - 0.03, 0.05);
          const xa = colX(cols - 2) + nw + 8, ya = cy;
          const xb = lastX - 10, yb = leafY(k) + leafH / 2;
          const d = `M ${xa} ${ya} C ${(xa + xb) / 2} ${ya}, ${(xa + xb) / 2} ${yb}, ${xb} ${yb}`;
          return <path key={k} d={d} fill="none" stroke={SOFT} strokeWidth={5} strokeDasharray={300}
            strokeDashoffset={300 * (1 - t)} markerEnd={t > 0.95 ? 'url(#crArrow)' : undefined} opacity={t > 0 ? 1 : 0} />;
        })}
        {traceT > 0 && <path d={traceD} fill="none" stroke={ACCENT} strokeWidth={8} strokeLinecap="round"
          strokeDasharray={2200} strokeDashoffset={2200 * (1 - traceT)} markerEnd={traceT > 0.97 ? 'url(#crArrowAccent)' : undefined} />}
        {/* the week brace under the whole chain */}
        {(() => {
          const t = ramp(props.weekAt, 0.06);
          const y = braceY, xa = S.x + 10, xb = xa + (S.r - 10 - xa) * t;
          return t > 0 ? <path d={`M ${xa} ${y - 24} L ${xa} ${y} L ${xb} ${y} ${t > 0.98 ? `L ${xb} ${y - 24}` : ''}`}
            fill="none" stroke={INK} strokeWidth={4} opacity={0.7} /> : null;
        })()}
      </svg>
      {props.nodes.map((n, i) => <NodeCard key={i} n={n} x={colX(i)} y={cy - nh / 2} w={nw} h={nh} />)}
      {props.leaves.map((l, k) => <NodeCard key={k} n={l} x={lastX} y={leafY(k)} w={leafW} h={leafH} horizontal />)}
      <div style={{position: 'absolute', left: S.x, width: S.w, top: braceY + 28, textAlign: 'center', fontFamily: SERIF,
        fontSize: 58, fontWeight: 700, color: INK, opacity: pop(props.weekAt + 0.03)}}>{props.weekLine}</div>
      <div style={{position: 'absolute', left: S.x, width: S.w, top: braceY + 120, textAlign: 'center', fontFamily: SERIF,
        fontSize: 56, fontStyle: 'italic', color: INK, opacity: pop(props.traceAt + 0.04)}}>{props.traceLabel}</div>
      <LogoBug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B06 — a short voice guide; an off-brand draft line is flagged and rewritten
// ─────────────────────────────────────────────────────────────────────────────
export const repurposeVoiceCheckSchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('One voice, every platform.'),
  guideTitle: z.string().default('Voice guide'),
  guideAt: z.number().default(0.19),
  rules: z.array(z.object({k: z.string(), v: z.string(), at: z.number()})).default([
    {k: 'SOUND', v: 'warm · plain · curious', at: 0.29},
    {k: 'USE', v: '“you”, “we”, “try this”', at: 0.38},
    {k: 'NEVER', v: '“game-changer”, “hack”, “guaranteed”', at: 0.456},
  ]),
  draftTitle: z.string().default('Draft · LinkedIn post'),
  draftAt: z.number().default(0.54),
  lines: z.array(z.string()).default([
    'Repurposing one video saved our week.',
    'This game-changing hack guarantees results!',
    'The full video is on our channel.',
  ]),
  badIndex: z.number().default(1),
  fixed: z.string().default('Here’s one thing worth trying this week.'),
  flagAt: z.number().default(0.737),
  strikeAt: z.number().default(0.765),
  rewriteAt: z.number().default(0.88),
  rewriteSpan: z.number().default(0.06),
  flagLabel: z.string().default('off-brand'),
  okLabel: z.string().default('on-brand'),
  checkAt: z.number().default(0.95),
  caption: z.string().default('Example voice guide and draft — illustrative'),
});

/** The draft card body — shared by both aspects (sizes passed in). */
export const DraftBody: React.FC<{props: z.infer<typeof repurposeVoiceCheckSchema>; px: number; pillPx: number; gap: number;
  pop: (f: number) => number; ramp: (f: number, d?: number) => number; nowrap?: boolean}> = ({props, px, pillPx, gap, pop, ramp, nowrap = true}) => {
  const flagIn = pop(props.flagAt), strikeIn = ramp(props.strikeAt, 0.05);
  const typed = ramp(props.rewriteAt, props.rewriteSpan);
  const okIn = pop(props.checkAt);
  const fixedShown = props.fixed.slice(0, Math.round(typed * props.fixed.length));
  return (
    <div style={{display: 'flex', flexDirection: 'column', gap}}>
      {props.lines.map((ln, i) => {
        if (i !== props.badIndex) {
          return <div key={i} style={{fontFamily: SERIF, fontSize: px, color: INK, lineHeight: 1.15}}>{ln}</div>;
        }
        return (
          <div key={i} style={{display: 'flex', flexDirection: 'column', gap: gap * 0.45}}>
            <div style={{alignSelf: 'flex-start', height: pillPx * 1.5, padding: `0 ${pillPx * 0.6}px`, borderRadius: pillPx,
              border: `3px solid ${okIn > 0.5 ? INK : ACCENT}`, background: CLAUDE.CARD, display: 'flex', alignItems: 'center',
              fontFamily: SANS, fontSize: pillPx, fontWeight: 700, color: INK, opacity: flagIn}}>
              {okIn > 0.5 ? `✓ ${props.okLabel}` : props.flagLabel}</div>
            <div style={{position: 'relative', alignSelf: 'flex-start', whiteSpace: nowrap ? 'nowrap' : 'normal'}}>
              <span style={{fontFamily: SERIF, fontSize: px, color: INK, lineHeight: 1.15, opacity: 1 - 0.55 * strikeIn}}>{ln}</span>
              {/* accent underline = the flag; ink strike-through on the spoken "rewrite" */}
              <div style={{position: 'absolute', left: 0, right: 0, bottom: -6, height: 7, borderRadius: 4, background: ACCENT,
                opacity: flagIn * (1 - strikeIn)}} />
              <div style={{position: 'absolute', left: 0, width: `${strikeIn * 100}%`, top: '54%', height: 5, background: INK}} />
            </div>
            <div style={{fontFamily: SERIF, fontSize: px, color: INK, lineHeight: 1.15, fontWeight: 700, minHeight: px * 1.15}}>
              {fixedShown}</div>
          </div>
        );
      })}
    </div>
  );
};

export const RepurposeVoiceCheck: React.FC<z.infer<typeof repurposeVoiceCheckSchema>> = (props) => {
  const {pop, ramp} = useBeat(props.durationSeconds);
  const S = SAFE;
  const top = 170, bottom = 920;
  const leftW = 700, gap = 40;
  const gIn = pop(props.guideAt), dIn = pop(props.draftAt);
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} />
      <Card style={{position: 'absolute', left: S.x, top, width: leftW, height: bottom - top, boxSizing: 'border-box',
        padding: '40px 48px', background: CLAUDE.FOOTER, opacity: gIn, transform: `translateY(${(1 - gIn) * 20}px)`}}>
        <div style={{fontFamily: SERIF, fontSize: 60, fontWeight: 700, color: INK, marginBottom: 34}}>{props.guideTitle}</div>
        {props.rules.map((r, i) => {
          const t = pop(r.at);
          return (
            <div key={i} style={{marginBottom: 46, opacity: t, transform: `translateX(${(1 - t) * 18}px)`}}>
              <div style={{fontFamily: SANS, fontSize: 40, fontWeight: 700, letterSpacing: '0.12em', color: SOFT}}>{r.k}</div>
              <div style={{fontFamily: SERIF, fontSize: 54, color: INK, lineHeight: 1.15, marginTop: 6}}>{r.v}</div>
            </div>
          );
        })}
      </Card>
      <Card style={{position: 'absolute', left: S.x + leftW + gap, top, width: S.w - leftW - gap, height: bottom - top,
        boxSizing: 'border-box', padding: '40px 52px', opacity: dIn, transform: `translateY(${(1 - dIn) * 20}px)`}}>
        <div style={{fontFamily: SANS, fontSize: 40, fontWeight: 700, color: SOFT, marginBottom: 36}}>{props.draftTitle}</div>
        <DraftBody props={props} px={50} pillPx={40} gap={44} pop={pop} ramp={ramp} />
      </Card>
      <div style={{position: 'absolute', left: S.x, top: S.b - 50, fontFamily: SANS, fontSize: 40, color: SOFT,
        opacity: gIn}}>{props.caption}</div>
      <LogoBug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B07 — what works better? tasks slide toward AI or toward people
// ─────────────────────────────────────────────────────────────────────────────
export const creativityBalanceSchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('What works better?'),
  leftPole: z.string().default('AI'),
  rightPole: z.string().default('People'),
  polesAt: z.number().default(0.04),
  leftNote: z.string().default('alone: sounds like everyone else'),
  rightNote: z.string().default('alone: can’t keep up'),
  leftNoteAt: z.number().default(0.57),
  rightNoteAt: z.number().default(0.76),
  rows: z.array(z.object({label: z.string(), side: z.enum(['L', 'R']), at: z.number()})).default([
    {label: 'Speed', side: 'L', at: 0.085},
    {label: 'Volume', side: 'L', at: 0.115},
    {label: 'Formatting', side: 'L', at: 0.155},
    {label: 'Original idea', side: 'R', at: 0.305},
    {label: 'Story', side: 'R', at: 0.38},
    {label: 'Final call', side: 'R', at: 0.422},
  ]),
  verdict: z.string().default('Best: the pair — AI for scale, people for meaning.'),
  verdictAt: z.number().default(0.9),
});

export const CreativityBalance: React.FC<z.infer<typeof creativityBalanceSchema>> = (props) => {
  const {pop, ramp} = useBeat(props.durationSeconds);
  const S = SAFE;
  const cx = S.x + S.w / 2;
  const pIn = pop(props.polesAt);
  const rowsTop = 330, rowH = 74, rowGap = 14;
  const chipW = 400;
  const vIn = pop(props.verdictAt);
  const poleBlock = (side: 'L' | 'R') => {
    const note = side === 'L' ? props.leftNote : props.rightNote;
    const nAt = side === 'L' ? props.leftNoteAt : props.rightNoteAt;
    return (
      <div style={{position: 'absolute', top: 150, width: 760, left: side === 'L' ? S.x : S.r - 760,
        textAlign: side === 'L' ? 'left' : 'right', opacity: pIn}}>
        <div style={{fontFamily: SERIF, fontSize: 80, fontWeight: 700, color: INK, lineHeight: 1}}>
          {side === 'L' ? props.leftPole : props.rightPole}</div>
        <div style={{fontFamily: SANS, fontSize: 46, color: SOFT, marginTop: 14, fontStyle: 'italic', opacity: pop(nAt)}}>{note}</div>
      </div>
    );
  };
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} />
      {poleBlock('L')}
      {poleBlock('R')}
      <div style={{position: 'absolute', left: cx - 2, top: rowsTop - 20, width: 4,
        height: (rowH + rowGap) * props.rows.length + 20, background: CLAUDE.GHOST, opacity: 0.6 * pIn}} />
      {props.rows.map((r, i) => {
        const y = rowsTop + i * (rowH + rowGap);
        const appear = pop(r.at);
        const slide = ramp(r.at + 0.012, 0.05);
        const e = slide * slide * (3 - 2 * slide);
        const endX = r.side === 'L' ? S.x : S.r - chipW;
        const x = (cx - chipW / 2) + (endX - (cx - chipW / 2)) * e;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: S.x, top: y + rowH / 2 - 1, width: S.w, height: 2,
              background: CLAUDE.BORDER, opacity: appear}} />
            <Card style={{position: 'absolute', left: x, top: y, width: chipW, height: rowH, display: 'flex',
              alignItems: 'center', justifyContent: 'center', opacity: appear,
              background: r.side === 'L' ? CLAUDE.FOOTER : CLAUDE.CARD,
              border: `3px solid ${CLAUDE.BORDER}`}}>
              <span style={{fontFamily: SERIF, fontSize: 52, fontWeight: 700, color: INK}}>{r.label}</span>
            </Card>
          </React.Fragment>
        );
      })}
      <div style={{position: 'absolute', left: S.x, width: S.w, top: 880, textAlign: 'center', fontFamily: SERIF,
        fontSize: 58, fontWeight: 700, color: INK, opacity: vIn, transform: `translateY(${(1 - vIn) * 16}px)`}}>{props.verdict}</div>
      <div style={{position: 'absolute', left: cx - 320, width: 640 * vIn, top: 972, height: 8, borderRadius: 4, background: ACCENT}} />
      <LogoBug />
    </AbsoluteFill>
  );
};
