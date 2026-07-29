/**
 * ReadingRoadmaps.tsx — reel-local Remotion components for
 *   claude-hai · "Personalized, Project-Driven Reading Roadmaps for CaNCURE Trainees"
 *   (weekly-videos/week-01-paper-introduction/output/personalized-reading-roadmap-introduction)
 *
 * BODY beats B01–B06. Two-skin contract: the Claude UI beats (B00/B07/B08/B09) use the
 * shipping claude scenes; these six render in the HUMANITARIANS editorial palette per the
 * ai-explainer ASK→RESULT LAW ("RESULT graphics render in the channel palette").
 *
 * LAWS kept by every component here:
 *   • Pure function of useP() — no CSS transitions, no timers, no Math.random(). Seeking any
 *     frame renders identically (Remotion determinism).
 *   • ONE dominant meaning-accent per beat (teal = good/kept/authoritative, crimson =
 *     caution). Navy SLATE is neutral structure; gold is fill-only, never text.
 *   • Own <AbsoluteFill> on CREAM. 1920×1080. Everything inside the ~5% title-safe inset.
 *   • Each body beat draws its own low-opacity HAI corner bug lower-right (LOGO LAW; the free
 *     pipeline composites no bug — confirmed).
 *
 * GUARDRAILS enforced on-screen (see SOURCES.md ledger):
 *   • B04 always shows dashed model-proposed edges carrying an "under review" badge — NOT all
 *     prerequisites are approved.
 *   • B06's adaptive panel is greyed + stamped "DEFERRED · not implemented" — future, not shipped.
 *   • No invented numbers on screen (only "38 chapters" / "4 stages" anywhere). B02 similarity is
 *     shown as bar length, never a percentage; B05 rows are illustrative structure from the
 *     draft's own dependency example, never measured results.
 *
 * Self-contained (no toolkit imports) so the identical file is the portable remotion-src copy.
 */
import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig } from 'remotion';
import { z } from 'zod';

// ── HUMANITARIANS palette (editorial, on cream) ────────────────────────────────
const CREAM = '#F3EBDD';   // ground
const INK = '#2F2A26';     // text / marks
const INK_SOFT = '#6E655B';// secondary text
const TEAL = '#1F4E5F';    // accent A: good / kept / authoritative
const CRIMSON = '#E4572E'; // accent B: caution / not-yet / held back
const SLATE = '#29335C';   // structure — entity cards (white text), scaffolding
const GOLD = '#F3A712';    // fill only, never text
const SAGE = '#A8C686';    // human / growth tertiary
const GHOST = '#B7AC9A';   // greyed / deferred
const CARD = '#FBF7EF';    // raised surface on cream
const BORDER = '#D8CBB4';  // hairline

// ── Type stack (editorial): EB Garamond serif + Montserrat sans ────────────────
const SERIF = '"EB Garamond", Georgia, "Times New Roman", serif';
const SANS = '"Montserrat", "Helvetica Neue", Arial, sans-serif';
const MONO = 'ui-monospace, "SF Mono", Menlo, monospace';

// ── Canvas + title-safe inset ──────────────────────────────────────────────────
const CW = 1920, CH = 1080;
const SAFE = 100; // inset ≥ 5% (x 96..1824, y 54..1026 → 100 clears both)

// ── Deterministic motion helpers (the only clock is useP) ──────────────────────
const clamp = (v: number, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const remap = (x: number, x0: number, x1: number, y0: number, y1: number) => {
  const t = clamp((x - x0) / ((x1 - x0) || 1), 0, 1);
  return y0 + (y1 - y0) * t;
};
const ease = (t: number) => 1 - Math.pow(1 - clamp(t, 0, 1), 3);
const useP = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  return clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);
};

// ── Shared marks ────────────────────────────────────────────────────────────────
const Spark: React.FC<{ size?: number; color?: string }> = ({ size = 28, color = TEAL }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" style={{ flexShrink: 0 }}>
    {Array.from({ length: 8 }, (_, i) => (
      <line key={i} x1={12} y1={12}
        x2={12 + 10 * Math.cos((i * Math.PI) / 4 + 0.2)}
        y2={12 + 10 * Math.sin((i * Math.PI) / 4 + 0.2)}
        stroke={color} strokeWidth={3} strokeLinecap="round" />
    ))}
  </svg>
);

/** The ONE serif spark line, top-center, fades in first (SPARK-LINE LAW). */
const SparkLine: React.FC<{ text: string; p: number; accent?: string }> = ({ text, p, accent = TEAL }) => (
  <div style={{
    position: 'absolute', top: 62, left: SAFE, right: SAFE,
    display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 16,
    opacity: remap(p, 0, 0.06, 0, 1),
  }}>
    <Spark size={30} color={accent} />
    <div style={{ fontFamily: SERIF, fontSize: 46, fontStyle: 'italic', color: INK }}>{text}</div>
  </div>
);

/** Channel bug — clean serif wordmark, low opacity, lower-right, inside title-safe. */
const CornerBug: React.FC = () => (
  <div style={{
    position: 'absolute', right: SAFE, bottom: 56,
    display: 'flex', alignItems: 'center', gap: 9, opacity: 0.4,
  }}>
    <Spark size={19} color={INK} />
    <span style={{ fontFamily: SERIF, fontSize: 24, color: INK, letterSpacing: '0.01em' }}>Humanitarians&nbsp;AI</span>
  </div>
);

/** Straight directed connector that draws on with progress d∈[0,1]. */
const DirEdge: React.FC<{
  x1: number; y1: number; x2: number; y2: number; d: number; color: string;
  dashed?: boolean; width?: number;
}> = ({ x1, y1, x2, y2, d, color, dashed, width = 4 }) => {
  const len = Math.hypot(x2 - x1, y2 - y1);
  const dd = ease(d);
  const hx = x1 + (x2 - x1) * dd, hy = y1 + (y2 - y1) * dd;
  const ang = Math.atan2(y2 - y1, x2 - x1);
  const ah = 15;
  return (
    <g>
      <line x1={x1} y1={y1} x2={x2} y2={y2} stroke={color} strokeWidth={width}
        strokeLinecap="round" strokeDasharray={dashed ? '10 9' : len}
        strokeDashoffset={dashed ? 0 : len * (1 - dd)} opacity={dashed ? dd : 1} />
      {dd > 0.98 && (
        <polyline points={`${hx - ah * Math.cos(ang - 0.5)},${hy - ah * Math.sin(ang - 0.5)} ${hx},${hy} ${hx - ah * Math.cos(ang + 0.5)},${hy - ah * Math.sin(ang + 0.5)}`}
          stroke={color} strokeWidth={width} fill="none" strokeLinecap="round" strokeLinejoin="round" />
      )}
    </g>
  );
};

// ════════════════════════════════════════════════════════════════════════════════
// B01 · RoadmapProblemFanout — one fixed book duplicates, fans to distinct projects.
//      Accent: CRIMSON (the "unread" failure mark). "Same book, different projects."
// ════════════════════════════════════════════════════════════════════════════════
export const roadmapProblemFanoutSchema = z.object({
  sparkLine: z.string().default('Same book. Different projects.'),
  bookLabel: z.string().default('38-chapter textbook · topic-ordered'),
  projects: z.array(z.string()).default([
    'LNP–siRNA delivery', 'Photothermal therapy', 'Tumor-targeted imaging', '…',
  ]),
});
export type RoadmapProblemFanoutProps = z.infer<typeof roadmapProblemFanoutSchema>;

export const RoadmapProblemFanout: React.FC<RoadmapProblemFanoutProps> = ({ sparkLine, bookLabel, projects }) => {
  const p = useP();
  const bookX = 235, bookY = 330, bookW = 250, bookH = 430;
  const dupP = remap(p, 0.35, 0.5, 0, 1);
  const cards = projects.slice(0, 4);
  const cardX = 1140, cardW = 620, cardH = 118, gap = 40;
  const cardY = (i: number) => 268 + i * (cardH + gap);

  return (
    <AbsoluteFill style={{ background: CREAM }}>
      <SparkLine text={sparkLine} p={p} accent={CRIMSON} />

      {/* fan arrows (behind cards, in front of book) */}
      <svg width={CW} height={CH} style={{ position: 'absolute', inset: 0 }}>
        {cards.map((_, i) => {
          const d = ease(remap(p, 0.5 + i * 0.07, 0.72 + i * 0.07, 0, 1));
          if (d <= 0) return null;
          const sx = bookX + bookW + 14, sy = bookY + bookH / 2;
          const ex = cardX - 16, ey = cardY(i) + cardH / 2;
          const mx = (sx + ex) / 2;
          const path = `M ${sx} ${sy} C ${mx} ${sy}, ${mx} ${ey}, ${ex} ${ey}`;
          const L = 1100;
          return <path key={i} d={path} fill="none" stroke={INK_SOFT} strokeWidth={3}
            strokeDasharray={L} strokeDashoffset={L * (1 - d)} opacity={0.8} />;
        })}
      </svg>

      {/* duplicated ghost copies of the one book */}
      {[2, 1].map((k) => (
        <div key={k} style={{
          position: 'absolute', left: bookX + k * 20, top: bookY + k * 20, width: bookW, height: bookH,
          background: SLATE, borderRadius: 10, opacity: 0.18 * dupP,
        }} />
      ))}

      {/* the book */}
      <div style={{ position: 'absolute', left: bookX, top: bookY, width: bookW, height: bookH,
        background: SLATE, borderRadius: 10, boxShadow: '0 14px 40px rgba(47,42,38,0.22)', overflow: 'hidden' }}>
        <div style={{ position: 'absolute', left: 12, top: 0, bottom: 0, width: 8, background: 'rgba(0,0,0,0.25)' }} />
        {Array.from({ length: 38 }, (_, i) => {
          const t0 = 0.03 + i * (0.30 / 38);
          const o = remap(p, t0, t0 + 0.05, 0, 1);
          const w = 120 + ((i * 37) % 60); // varied tick widths (deterministic, not random)
          return <div key={i} style={{
            position: 'absolute', left: 40, top: 26 + i * 10, width: w, height: 3,
            background: '#E9E2D3', opacity: 0.85 * o, borderRadius: 2,
          }} />;
        })}
      </div>
      <div style={{ position: 'absolute', left: bookX - 60, top: bookY + bookH + 18, width: bookW + 120,
        textAlign: 'center', fontFamily: SANS, fontSize: 23, color: INK_SOFT, opacity: remap(p, 0.12, 0.22, 0, 1) }}>
        {bookLabel}
      </div>

      {/* "unread" watermark */}
      <div style={{ position: 'absolute', left: bookX - 30, top: bookY + 150, width: bookW + 60, textAlign: 'center',
        transform: 'rotate(-13deg)', fontFamily: SERIF, fontWeight: 700, fontSize: 60, letterSpacing: '0.08em',
        color: CRIMSON, opacity: 0.62 * remap(p, 0.8, 0.94, 0, 1) }}>
        UNREAD
      </div>

      {/* distinct project cards */}
      {cards.map((label, i) => {
        const o = ease(remap(p, 0.5 + i * 0.07, 0.64 + i * 0.07, 0, 1));
        return (
          <div key={i} style={{
            position: 'absolute', left: cardX, top: cardY(i) + (1 - o) * 22, width: cardW, height: cardH,
            background: SLATE, borderRadius: 14, opacity: o, display: 'flex', alignItems: 'center', gap: 20,
            padding: '0 28px', boxShadow: '0 8px 24px rgba(41,51,92,0.18)',
          }}>
            <div style={{ fontFamily: SANS, fontSize: 15, fontWeight: 700, letterSpacing: 2,
              color: 'rgba(255,255,255,0.6)', width: 92 }}>PROJECT {i + 1}</div>
            <div style={{ fontFamily: SERIF, fontSize: 34, color: '#FFFFFF' }}>{label}</div>
          </div>
        );
      })}

      <CornerBug />
    </AbsoluteFill>
  );
};

// ════════════════════════════════════════════════════════════════════════════════
// B02 · RetrieveVsReorder — content→ordering strike; a ranked list re-threads into a
//      dependency path; one high-sim item is held back. THESIS beat. Accent: TEAL.
// ════════════════════════════════════════════════════════════════════════════════
export const retrieveVsReorderSchema = z.object({
  sparkLine: z.string().default('Select by relevance. Order by dependency.'),
  strikeFrom: z.string().default('a content problem'),
  strikeTo: z.string().default('an ordering problem'),
  rankedLabel: z.string().default('retrieval — top matches by similarity'),
  orderedLabel: z.string().default('reorder — sequenced by learning dependency'),
  heldBackLabel: z.string().default('high-similarity, not needed yet — held back'),
});
export type RetrieveVsReorderProps = z.infer<typeof retrieveVsReorderSchema>;

export const RetrieveVsReorder: React.FC<RetrieveVsReorderProps> = ({
  sparkLine, strikeFrom, strikeTo, rankedLabel, orderedLabel, heldBackLabel,
}) => {
  const p = useP();
  // reframe (top band)
  const fromO = remap(p, 0.04, 0.12, 0, 1);
  const strikeD = ease(remap(p, 0.12, 0.22, 0, 1));
  const toO = remap(p, 0.2, 0.3, 0, 1);
  // ranked list (left) — bars sorted by length; NO numbers (no invented specifics)
  const ranked = [0.96, 0.88, 0.78, 0.62, 0.5];
  const listX = 150, listY = 430, barMaxW = 560, rowH = 62;
  // held-back = the top bar (high similarity) but not needed yet
  const heldD = ease(remap(p, 0.86, 1, 0, 1));
  // dependency path (right)
  const pathNodes = ['A', 'B', 'C', 'D'];
  const pnX = 1180, pnY0 = 430, pnStep = 118;

  return (
    <AbsoluteFill style={{ background: CREAM }}>
      <SparkLine text={sparkLine} p={p} accent={TEAL} />

      {/* reframe line */}
      <div style={{ position: 'absolute', top: 160, left: SAFE, right: SAFE, textAlign: 'center' }}>
        <span style={{ fontFamily: SERIF, fontSize: 44, color: INK, opacity: fromO }}>This isn’t </span>
        <span style={{ position: 'relative', fontFamily: SERIF, fontSize: 44, color: INK_SOFT, opacity: fromO }}>
          {strikeFrom}
          <span style={{ position: 'absolute', left: -4, right: -4, top: '52%', height: 4, background: CRIMSON,
            borderRadius: 2, transform: `scaleX(${strikeD})`, transformOrigin: 'left' }} />
        </span>
        <span style={{ fontFamily: SERIF, fontSize: 44, color: INK, opacity: toO }}> — it’s </span>
        <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 46, color: TEAL, opacity: toO }}>{strikeTo}.</span>
      </div>

      {/* LEFT — ranked list (similarity by bar length only) */}
      <div style={{ position: 'absolute', left: listX, top: listY - 54, fontFamily: SANS, fontSize: 20,
        letterSpacing: 1, color: INK_SOFT, opacity: remap(p, 0.3, 0.4, 0, 1) }}>{rankedLabel.toUpperCase()}</div>
      {ranked.map((v, i) => {
        const o = ease(remap(p, 0.32 + i * 0.04, 0.44 + i * 0.04, 0, 1));
        const held = i === 0 ? heldD : 0; // top-similarity item is set aside (faded), not lifted up
        return (
          <div key={i} style={{
            position: 'absolute', left: listX, top: listY + i * rowH, opacity: o * (1 - held * 0.8),
            display: 'flex', alignItems: 'center', gap: 14,
          }}>
            <div style={{ width: barMaxW * v, height: 40, borderRadius: 8,
              background: i === 0 && held > 0.15 ? CRIMSON : SLATE, opacity: 0.9 - i * 0.08 }} />
            <div style={{ fontFamily: MONO, fontSize: 18, color: INK_SOFT }}>§ section {i + 1}</div>
          </div>
        );
      })}
      {/* the ranker can't order — an unanswered "read first?" badge blinks (deterministic) */}
      <div style={{ position: 'absolute', left: listX, top: listY + 5 * rowH + 8,
        fontFamily: SANS, fontSize: 24, fontWeight: 700, color: CRIMSON,
        opacity: remap(p, 0.46, 0.54, 0, 1) * (1 - remap(p, 0.82, 0.88, 0, 1)) * (0.55 + 0.45 * Math.sin(p * 44)) }}>
        read first? — the ranker can’t say
      </div>

      {/* RIGHT — re-threaded dependency path */}
      <div style={{ position: 'absolute', left: pnX - 30, top: pnY0 - 54, fontFamily: SANS, fontSize: 20,
        letterSpacing: 1, color: TEAL, opacity: remap(p, 0.58, 0.68, 0, 1) }}>{orderedLabel.toUpperCase()}</div>
      <svg width={CW} height={CH} style={{ position: 'absolute', inset: 0 }}>
        {pathNodes.slice(0, -1).map((_, i) => {
          const d = ease(remap(p, 0.62 + i * 0.06, 0.74 + i * 0.06, 0, 1));
          return <DirEdge key={i} x1={pnX + 26} y1={pnY0 + i * pnStep + 26} x2={pnX + 26} y2={pnY0 + (i + 1) * pnStep - 2}
            d={d} color={TEAL} width={4} />;
        })}
      </svg>
      {pathNodes.map((n, i) => {
        const o = ease(remap(p, 0.6 + i * 0.06, 0.72 + i * 0.06, 0, 1));
        return (
          <div key={i} style={{
            position: 'absolute', left: pnX, top: pnY0 + i * pnStep, width: 340, height: 54, opacity: o,
            background: CARD, border: `2px solid ${TEAL}`, borderRadius: 10, display: 'flex', alignItems: 'center',
            gap: 14, padding: '0 18px',
          }}>
            <div style={{ width: 34, height: 34, borderRadius: 18, background: TEAL, color: '#fff',
              fontFamily: SANS, fontWeight: 700, fontSize: 18, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>{n}</div>
            <div style={{ fontFamily: MONO, fontSize: 18, color: INK }}>read {n} {i < pathNodes.length - 1 ? 'before' : 'last'}</div>
          </div>
        );
      })}

      {/* held-back tray (bottom-left; the top-similarity section set aside — select, not retrieve) */}
      <div style={{ position: 'absolute', left: listX, top: 806, width: 760, height: 92, opacity: heldD,
        border: `2px dashed ${CRIMSON}`, borderRadius: 12, display: 'flex', alignItems: 'center', gap: 18, padding: '0 24px',
        background: 'rgba(228,87,46,0.07)' }}>
        <div style={{ fontFamily: SANS, fontSize: 15, fontWeight: 700, letterSpacing: 2, color: CRIMSON, whiteSpace: 'nowrap' }}>HELD BACK</div>
        <div style={{ width: 84, height: 26, borderRadius: 6, background: CRIMSON, flexShrink: 0 }} />
        <div style={{ fontFamily: SERIF, fontSize: 24, color: INK }}>{heldBackLabel}</div>
      </div>

      <CornerBug />
    </AbsoluteFill>
  );
};

// ════════════════════════════════════════════════════════════════════════════════
// B03 · RoadmapPipeline — four L→R stages, each with its on-disk artifact chip; a
//      terracotta-equivalent (TEAL) "per student" bracket; chips flip to editable.
//      Accent: TEAL (the reviewable seam). Nodes: SLATE structure.
// ════════════════════════════════════════════════════════════════════════════════
export const roadmapPipelineSchema = z.object({
  sparkLine: z.string().default('Four stages. Four artifacts.'),
  stages: z.array(z.object({ n: z.number(), name: z.string(), artifact: z.string() })).default([
    { n: 1, name: 'Extract sections', artifact: 'sections.json' },
    { n: 2, name: 'Tag metadata', artifact: 'metadata/*.yaml' },
    { n: 3, name: 'Build dependency graph', artifact: 'graph.json' },
    { n: 4, name: 'Sequence roadmap', artifact: 'roadmap.md' },
  ]),
  perTextbookNote: z.string().default('stages 1–3 run once per textbook'),
  perStudentNote: z.string().default('stage 4 runs per student'),
  editableTag: z.string().default('inspectable · human-editable'),
});
export type RoadmapPipelineProps = z.infer<typeof roadmapPipelineSchema>;

export const RoadmapPipeline: React.FC<RoadmapPipelineProps> = ({
  sparkLine, stages, perTextbookNote, perStudentNote, editableTag,
}) => {
  const p = useP();
  const n = stages.length;
  const nodeW = 356, nodeH = 168, gap = 52;
  const totalW = n * nodeW + (n - 1) * gap;
  const x0 = (CW - totalW) / 2;
  const nodeY = 432;
  const nx = (i: number) => x0 + i * (nodeW + gap);
  const editD = remap(p, 0.78, 0.94, 0, 1);

  return (
    <AbsoluteFill style={{ background: CREAM }}>
      <SparkLine text={sparkLine} p={p} accent={TEAL} />

      {/* connector arrows */}
      <svg width={CW} height={CH} style={{ position: 'absolute', inset: 0 }}>
        {stages.slice(0, -1).map((_, i) => {
          const d = ease(remap(p, 0.16 + i * 0.16, 0.28 + i * 0.16, 0, 1));
          return <DirEdge key={i} x1={nx(i) + nodeW + 4} y1={nodeY + nodeH / 2} x2={nx(i + 1) - 4} y2={nodeY + nodeH / 2}
            d={d} color={INK_SOFT} width={4} />;
        })}
      </svg>

      {stages.map((s, i) => {
        const o = ease(remap(p, 0.06 + i * 0.16, 0.2 + i * 0.16, 0, 1));
        const isStudent = i === n - 1;
        return (
          <React.Fragment key={i}>
            {/* node */}
            <div style={{
              position: 'absolute', left: nx(i), top: nodeY + (1 - o) * 20, width: nodeW, height: nodeH, opacity: o,
              background: SLATE, borderRadius: 16, boxShadow: '0 10px 30px rgba(41,51,92,0.18)',
              display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 8, padding: '0 20px',
            }}>
              <div style={{ fontFamily: SANS, fontSize: 15, fontWeight: 700, letterSpacing: 3, color: 'rgba(255,255,255,0.55)' }}>
                STAGE {s.n}
              </div>
              <div style={{ fontFamily: SERIF, fontSize: 30, color: '#fff', textAlign: 'center', lineHeight: 1.15 }}>{s.name}</div>
            </div>
            {/* artifact chip */}
            <div style={{
              position: 'absolute', left: nx(i) + 28, top: nodeY + nodeH + 26, width: nodeW - 56, opacity: o,
              background: CARD, border: `1.5px solid ${BORDER}`, borderRadius: 10, padding: '10px 14px',
              display: 'flex', alignItems: 'center', gap: 10,
            }}>
              <span style={{ fontFamily: MONO, fontSize: 19, color: INK, flex: 1 }}>{s.artifact}</span>
              <span style={{ fontFamily: SANS, fontSize: 16, fontWeight: 700, color: TEAL, opacity: editD }}>✎ edit</span>
            </div>
          </React.Fragment>
        );
      })}

      {/* per-textbook bracket (1..3) */}
      <div style={{ position: 'absolute', left: nx(0), top: nodeY - 44, width: nx(n - 2) + nodeW - nx(0), height: 22,
        borderTop: `3px solid ${INK_SOFT}`, borderLeft: `3px solid ${INK_SOFT}`, borderRight: `3px solid ${INK_SOFT}`,
        opacity: remap(p, 0.62, 0.72, 0, 1) }} />
      <div style={{ position: 'absolute', left: nx(0), top: nodeY - 84, width: nx(n - 2) + nodeW - nx(0), textAlign: 'center',
        fontFamily: SANS, fontSize: 22, color: INK_SOFT, opacity: remap(p, 0.64, 0.74, 0, 1) }}>{perTextbookNote}</div>

      {/* per-student bracket (stage 4) — TEAL accent */}
      <div style={{ position: 'absolute', left: nx(n - 1), top: nodeY - 44, width: nodeW, height: 22,
        borderTop: `3px solid ${TEAL}`, borderLeft: `3px solid ${TEAL}`, borderRight: `3px solid ${TEAL}`,
        opacity: remap(p, 0.68, 0.78, 0, 1) }} />
      <div style={{ position: 'absolute', left: nx(n - 1) - 30, top: nodeY - 84, width: nodeW + 60, textAlign: 'center',
        fontFamily: SANS, fontSize: 22, fontWeight: 700, color: TEAL, opacity: remap(p, 0.7, 0.8, 0, 1) }}>{perStudentNote}</div>

      {/* editable seam caption */}
      <div style={{ position: 'absolute', left: SAFE, right: SAFE, top: nodeY + nodeH + 108, textAlign: 'center',
        fontFamily: SERIF, fontStyle: 'italic', fontSize: 30, color: INK, opacity: editD }}>
        every stage writes an {editableTag} file — reviewable, not a black box.
      </div>

      <CornerBug />
    </AbsoluteFill>
  );
};

// ════════════════════════════════════════════════════════════════════════════════
// B04 · DependencyGraphReview — solid TEAL faculty-approved prerequisite edges vs
//      dashed model-proposed edges that keep a CRIMSON "under review" badge (guardrail:
//      NOT all approved). Accent: TEAL, with the required crimson caution mark.
// ════════════════════════════════════════════════════════════════════════════════
export const dependencyGraphReviewSchema = z.object({
  sparkLine: z.string().default('Faculty approve the prerequisites.'),
  approvedLabel: z.string().default('prerequisite — faculty-approved (authoritative)'),
  proposedLabel: z.string().default('proposed by model — under review'),
  humanLine: z.string().default('Propose: the AI. Approve as authoritative: the faculty.'),
  nodes: z.array(z.string()).default(['particle stability', 'surface chemistry', 'cellular uptake', 'pharmacokinetics']),
});
export type DependencyGraphReviewProps = z.infer<typeof dependencyGraphReviewSchema>;

export const DependencyGraphReview: React.FC<DependencyGraphReviewProps> = ({
  sparkLine, approvedLabel, proposedLabel, humanLine, nodes,
}) => {
  const p = useP();
  const nodeW = 300, nodeH = 94;
  const pos = [
    { x: 250, y: 540 },  // particle stability
    { x: 720, y: 396 },  // surface chemistry
    { x: 1190, y: 540 }, // cellular uptake
    { x: 1560, y: 396 }, // pharmacokinetics
  ];
  const c = (i: number) => ({ x: pos[i].x + nodeW / 2, y: pos[i].y + nodeH / 2 });
  // edges: [from,to,approved]
  const edges: [number, number, boolean][] = [
    [0, 1, true],   // stability → surface chemistry (approved)
    [1, 2, true],   // surface → uptake (approved)
    [2, 3, false],  // uptake → PK (proposed, under review)
    [0, 2, false],  // stability → uptake (proposed)
  ];
  const nodeO = (i: number) => ease(remap(p, 0.05 + i * 0.05, 0.2 + i * 0.05, 0, 1));

  return (
    <AbsoluteFill style={{ background: CREAM }}>
      <SparkLine text={sparkLine} p={p} accent={TEAL} />

      {/* legend */}
      <div style={{ position: 'absolute', right: SAFE, top: 150, display: 'flex', flexDirection: 'column', gap: 12,
        opacity: remap(p, 0.34, 0.44, 0, 1) }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <svg width={46} height={12}><line x1={2} y1={6} x2={44} y2={6} stroke={TEAL} strokeWidth={5} strokeLinecap="round" /></svg>
          <span style={{ fontFamily: SANS, fontSize: 20, color: INK }}>{approvedLabel}</span>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <svg width={46} height={12}><line x1={2} y1={6} x2={44} y2={6} stroke={GOLD} strokeWidth={5} strokeDasharray="8 6" strokeLinecap="round" /></svg>
          <span style={{ fontFamily: SANS, fontSize: 20, color: INK }}>{proposedLabel}</span>
        </div>
      </div>

      {/* edges */}
      <svg width={CW} height={CH} style={{ position: 'absolute', inset: 0 }}>
        {edges.map(([a, b, ok], i) => {
          const d = ok
            ? ease(remap(p, 0.3 + i * 0.05, 0.46 + i * 0.05, 0, 1))
            : ease(remap(p, 0.52 + i * 0.06, 0.68 + i * 0.06, 0, 1));
          if (d <= 0) return null;
          return <DirEdge key={i} x1={c(a).x} y1={c(a).y} x2={c(b).x} y2={c(b).y}
            d={d} color={ok ? TEAL : GOLD} dashed={!ok} width={ok ? 5 : 4} />;
        })}
      </svg>

      {/* approved check badges + under-review crimson badges */}
      {edges.map(([a, b, ok], i) => {
        const mx = (c(a).x + c(b).x) / 2, my = (c(a).y + c(b).y) / 2;
        if (ok) {
          const o = remap(p, 0.42 + i * 0.05, 0.5 + i * 0.05, 0, 1);
          return <div key={i} style={{ position: 'absolute', left: mx - 16, top: my - 40, width: 32, height: 32,
            borderRadius: 16, background: TEAL, color: '#fff', display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontSize: 18, fontWeight: 700, opacity: o }}>✓</div>;
        }
        const o = remap(p, 0.72, 0.82, 0, 1);
        return <div key={i} style={{ position: 'absolute', left: mx - 74, top: my - 18, width: 148, opacity: o,
          background: CRIMSON, color: '#fff', borderRadius: 8, padding: '4px 8px', textAlign: 'center',
          fontFamily: SANS, fontSize: 15, fontWeight: 700, letterSpacing: 0.5 }}>UNDER REVIEW</div>;
      })}

      {/* nodes */}
      {nodes.slice(0, 4).map((label, i) => (
        <div key={i} style={{
          position: 'absolute', left: pos[i].x, top: pos[i].y + (1 - nodeO(i)) * 16, width: nodeW, height: nodeH,
          opacity: nodeO(i), background: SLATE, borderRadius: 12, display: 'flex', alignItems: 'center', justifyContent: 'center',
          padding: '0 16px', boxShadow: '0 8px 22px rgba(41,51,92,0.18)',
        }}>
          <div style={{ fontFamily: SERIF, fontSize: 27, color: '#fff', textAlign: 'center', lineHeight: 1.12 }}>{label}</div>
        </div>
      ))}

      {/* irreducibly-human caption */}
      <div style={{ position: 'absolute', left: SAFE, right: SAFE, bottom: 118, textAlign: 'center',
        fontFamily: SERIF, fontStyle: 'italic', fontSize: 32, color: INK, opacity: remap(p, 0.86, 0.98, 0, 1) }}>
        {humanLine}
      </div>

      <CornerBug />
    </AbsoluteFill>
  );
};

// ════════════════════════════════════════════════════════════════════════════════
// B05 · WeeklyRoadmap — a weekly table fills; conditional pull-forward once faculty-
//      approved prerequisites exist; then splits to two visibly-different project
//      roadmaps. Accent: TEAL (pull-forward + Project A). Rows are illustrative.
// ════════════════════════════════════════════════════════════════════════════════
export const weeklyRoadmapSchema = z.object({
  sparkLine: z.string().default('What · why · which task · what first.'),
  columns: z.array(z.string()).default(['Week', 'Section', 'Why it matters', 'Lab task']),
  rows: z.array(z.object({ week: z.string(), section: z.string(), why: z.string(), task: z.string() })).default([
    { week: 'Wk 1', section: 'particle stability', why: 'assumed by surface chemistry', task: 'formulation setup' },
    { week: 'Wk 2', section: 'surface functionalization', why: 'needed before uptake', task: 'conjugation' },
    { week: 'Wk 3', section: 'cellular uptake', why: 'interprets your assay', task: 'uptake assay' },
  ]),
  readFirstNote: z.string().default('with faculty-approved prerequisites, background can be pulled earlier'),
  compareLabels: z.array(z.string()).default(['Project A — LNP–siRNA', 'Project B — photothermal']),
});
export type WeeklyRoadmapProps = z.infer<typeof weeklyRoadmapSchema>;

export const WeeklyRoadmap: React.FC<WeeklyRoadmapProps> = ({
  sparkLine, columns, rows, readFirstNote, compareLabels,
}) => {
  const p = useP();
  const splitP = ease(remap(p, 0.6, 0.78, 0, 1)); // 0 = single table, 1 = split
  // single table geometry (full width) morphs to the left panel on split
  const fullX = 260, fullW = 1400;
  const leftW = 720;
  const tblX = fullX - splitP * (fullX - SAFE);
  const tblW = fullW - splitP * (fullW - leftW);
  const headY = 250, rowH = 96;
  const colFrac = [0.13, 0.30, 0.35, 0.22];

  // Project B (illustrative reordering of the same attested concept pool — same
  // foundation, different path; the divergence IS the personalization).
  const rowsB = [
    { week: 'Wk 1', section: 'particle stability', why: 'shared foundation', task: 'formulation setup' },
    { week: 'Wk 2', section: 'in-vivo pharmacokinetics', why: 'drives your timing', task: 'PK sampling' },
    { week: 'Wk 3', section: 'surface chemistry', why: 'tunes photothermal dose', task: 'coating' },
  ];
  const rightX = SAFE + leftW + 60, rightW = CW - rightX - SAFE;

  const Table: React.FC<{ x: number; w: number; label?: string; data: typeof rows; accent: string; sharedIdx: number[] }>
    = ({ x, w, label, data, accent, sharedIdx }) => (
      <>
        {label && (
          <div style={{ position: 'absolute', left: x, top: headY - 58, width: w, fontFamily: SANS, fontSize: 24,
            fontWeight: 700, letterSpacing: 1, color: accent }}>{label}</div>
        )}
        {/* header */}
        <div style={{ position: 'absolute', left: x, top: headY, width: w, height: 58, background: SLATE, borderRadius: 10,
          display: 'flex', alignItems: 'center', opacity: remap(p, 0.02, 0.12, 0, 1) }}>
          {columns.map((cName, ci) => (
            <div key={ci} style={{ width: w * colFrac[ci], padding: '0 16px', fontFamily: SANS, fontSize: 19,
              fontWeight: 700, letterSpacing: 1, color: '#fff' }}>{cName}</div>
          ))}
        </div>
        {/* rows */}
        {data.map((r, ri) => {
          const o = ease(remap(p, 0.14 + ri * 0.09, 0.28 + ri * 0.09, 0, 1));
          const shared = sharedIdx.includes(ri);
          const cells = [r.week, r.section, r.why, r.task];
          return (
            <div key={ri} style={{
              position: 'absolute', left: x, top: headY + 66 + ri * rowH, width: w, height: rowH - 14, opacity: o,
              background: CARD, borderRadius: 10, borderLeft: `8px solid ${shared ? BORDER : accent}`,
              display: 'flex', alignItems: 'center', boxShadow: '0 5px 16px rgba(47,42,38,0.08)',
            }}>
              {cells.map((cell, ci) => (
                <div key={ci} style={{ width: w * colFrac[ci], padding: '0 16px',
                  fontFamily: ci === 0 ? SANS : SERIF, fontWeight: ci === 0 ? 700 : 400,
                  fontSize: ci === 1 ? 25 : 21, color: ci === 1 ? INK : INK_SOFT, lineHeight: 1.15 }}>{cell}</div>
              ))}
            </div>
          );
        })}
      </>
    );

  return (
    <AbsoluteFill style={{ background: CREAM }}>
      <SparkLine text={sparkLine} p={p} accent={TEAL} />

      {/* single → left panel (Project A) */}
      <Table x={tblX} w={tblW} label={splitP > 0.15 ? compareLabels[0] : undefined} data={rows} accent={TEAL} sharedIdx={[0]} />

      {/* conditional pull-forward marker (before split) */}
      {splitP < 0.6 && (
        <div style={{ position: 'absolute', left: tblX, top: headY + 66 + rows.length * rowH + 14, width: tblW,
          display: 'flex', alignItems: 'center', gap: 12, opacity: remap(p, 0.46, 0.56, 0, 1) * (1 - remap(p, 0.6, 0.68, 0, 1)) }}>
          <span style={{ fontFamily: SANS, fontSize: 22, fontWeight: 700, color: TEAL }}>↑ conditional</span>
          <span style={{ fontFamily: SERIF, fontStyle: 'italic', fontSize: 24, color: INK }}>{readFirstNote}</span>
        </div>
      )}

      {/* right panel (Project B) appears on split */}
      {splitP > 0.05 && (
        <div style={{ opacity: splitP }}>
          <Table x={rightX} w={rightW} label={compareLabels[1]} data={rowsB} accent={SLATE} sharedIdx={[0]} />
        </div>
      )}

      {/* divergence caption */}
      {splitP > 0.5 && (
        <div style={{ position: 'absolute', left: SAFE, right: SAFE, bottom: 108, textAlign: 'center',
          fontFamily: SERIF, fontStyle: 'italic', fontSize: 28, color: INK, opacity: remap(p, 0.82, 0.94, 0, 1) }}>
          Same foundation, different path — two projects, two roadmaps. That’s the personalization.
        </div>
      )}

      <CornerBug />
    </AbsoluteFill>
  );
};

// ════════════════════════════════════════════════════════════════════════════════
// B06 · LimitsAndFuture — four caution chips, then a greyed adaptive-layer panel
//      stamped DEFERRED · not implemented (guardrail: future, not shipped).
//      Accent: CRIMSON (the "when NOT to trust it" beat).
// ════════════════════════════════════════════════════════════════════════════════
export const limitsAndFutureSchema = z.object({
  sparkLine: z.string().default('Know the edges.'),
  limits: z.array(z.string()).default([
    'Single textbook, one program',
    'Timing = advisor heuristic, not learned',
    'Rule-based, deterministic tagging; uncertain metadata → faculty review',
    'No learning-outcome data yet',
  ]),
  futurePanel: z.string().default('Adaptive layer — faculty assessment + student progress could update the roadmap'),
  futureState: z.string().default('DEFERRED · not implemented'),
});
export type LimitsAndFutureProps = z.infer<typeof limitsAndFutureSchema>;

export const LimitsAndFuture: React.FC<LimitsAndFutureProps> = ({ sparkLine, limits, futurePanel, futureState }) => {
  const p = useP();
  const chips = limits.slice(0, 4);
  const gridX = SAFE + 40, gridW = CW - 2 * (SAFE + 40);
  const colW = (gridW - 40) / 2, chipH = 150, rowGap = 34;
  const gridY = 200;
  const cx = (i: number) => gridX + (i % 2) * (colW + 40);
  const cy = (i: number) => gridY + Math.floor(i / 2) * (chipH + rowGap);
  const panelD = ease(remap(p, 0.56, 0.78, 0, 1));
  const panelY = gridY + 2 * chipH + rowGap + 40;

  return (
    <AbsoluteFill style={{ background: CREAM }}>
      <SparkLine text={sparkLine} p={p} accent={CRIMSON} />

      {/* caution chips */}
      {chips.map((t, i) => {
        const o = ease(remap(p, 0.08 + i * 0.11, 0.22 + i * 0.11, 0, 1));
        return (
          <div key={i} style={{
            position: 'absolute', left: cx(i), top: cy(i) + (1 - o) * 18, width: colW, height: chipH, opacity: o,
            background: CARD, border: `1.5px solid ${BORDER}`, borderLeft: `10px solid ${CRIMSON}`, borderRadius: 14,
            display: 'flex', alignItems: 'center', gap: 22, padding: '0 30px', boxShadow: '0 8px 22px rgba(47,42,38,0.08)',
          }}>
            <svg width={44} height={44} viewBox="0 0 44 44" style={{ flexShrink: 0 }}>
              <path d="M22 6 L40 38 L4 38 Z" fill="none" stroke={CRIMSON} strokeWidth={3.5} strokeLinejoin="round" />
              <line x1={22} y1={18} x2={22} y2={29} stroke={CRIMSON} strokeWidth={3.5} strokeLinecap="round" />
              <circle cx={22} cy={34} r={2} fill={CRIMSON} />
            </svg>
            <div style={{ fontFamily: SERIF, fontSize: 28, color: INK, lineHeight: 1.18 }}>{t}</div>
          </div>
        );
      })}

      {/* greyed future / deferred panel */}
      <div style={{
        position: 'absolute', left: gridX, top: panelY + (1 - panelD) * 24, width: gridW, height: 176, opacity: panelD,
        background: 'rgba(183,172,154,0.16)', border: `2px dashed ${GHOST}`, borderRadius: 16,
        display: 'flex', alignItems: 'center', padding: '0 40px', overflow: 'hidden',
      }}>
        <div style={{ flex: 1 }}>
          <div style={{ fontFamily: SANS, fontSize: 17, fontWeight: 700, letterSpacing: 3, color: GHOST }}>FUTURE WORK</div>
          <div style={{ fontFamily: SERIF, fontSize: 30, color: '#8C8477', marginTop: 8, maxWidth: 860, lineHeight: 1.2 }}>{futurePanel}</div>
        </div>
        {/* DEFERRED stamp */}
        <div style={{ position: 'absolute', right: 40, top: 46, transform: 'rotate(-9deg)',
          border: `4px solid ${CRIMSON}`, borderRadius: 10, padding: '8px 18px', opacity: 0.85 * panelD }}>
          <div style={{ fontFamily: SANS, fontSize: 26, fontWeight: 800, letterSpacing: 2, color: CRIMSON }}>{futureState}</div>
        </div>
      </div>

      <CornerBug />
    </AbsoluteFill>
  );
};
