/**
 * RagOkf.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-rag-vs-okf ("RAG vs. the Open Knowledge Format", @HumanitariansAI).
 *
 * Same contract as ApiGateway.tsx / MonoPoly.tsx (whose stage helpers come from
 * JevExplainer.tsx): each component lays out natively for 16:9 (<Name>) and 9:16
 * (<Name>916) — never a crop — and every motion is a pure function of progress,
 * conformed via `durationSeconds`. One running example throughout: a small shop's
 * knowledge (orders, customers, revenue, refunds). The file contents, scores, agent
 * walk and git output are copied from the reel's evidence/ runs, not hand-made.
 *
 *   RoHook       — RAG, the default pipeline; then Google Cloud's OKF card (June 12, 2026)
 *   RoRag        — 4 raw docs → 11 chunks → vectors; the question's top-3 by cosine
 *   RoOkf        — the bundle's file tree; revenue.md opened (YAML + links); no vectors
 *   RoPhilosophy — a pile searched per question vs. one curated, persistent tree
 *   RoAdvantage  — the agent walks index → links; the same file's git log + diff
 *   RoCuration   — pages written by people or agents, then reviewed; one goes stale
 *   RoScale      — a huge corpus: RAG indexes it unattended, curation can't keep up
 */
import React from 'react';
import { AbsoluteFill, Img, staticFile } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ACC_TEXT, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';

const Pill: React.FC<{ text: string; size: number; a?: number; accent?: boolean; fill?: string; style?: React.CSSProperties }> = ({ text, size, a = 1, accent, fill, style }) => (
  <span style={{
    display: 'inline-block', padding: `${size * 0.16}px ${size * 0.42}px`, borderRadius: size, boxSizing: 'border-box',
    background: fill ?? (accent ? ACC_TEXT : CLAUDE.INK),
    fontFamily: SANS, fontSize: size, lineHeight: 1.1, color: CLAUDE.CARD, opacity: a, whiteSpace: 'nowrap', ...style,
  }}>{text}</span>
);

// a code/file panel: dark ink plate, cream mono text (reads at small sizes, passes contrast)
type Seg = { s: string; link?: boolean; dim?: boolean; add?: boolean; del?: boolean };
const CodePanel: React.FC<{
  name?: string; lines: Seg[][]; size: number; a?: number; shown?: number; style?: React.CSSProperties;
}> = ({ name, lines, size, a = 1, shown = 1, style }) => {
  const n = Math.ceil(lines.length * shown);
  return (
    <div style={{
      position: 'absolute', background: CLAUDE.INK, borderRadius: 16, boxSizing: 'border-box', padding: `${size * 0.6}px ${size * 0.8}px`,
      opacity: a, overflow: 'hidden', ...style,
    }}>
      {name && <div style={{ fontFamily: SANS, fontSize: size * 0.95, color: CLAUDE.PILL, marginBottom: size * 0.45, fontWeight: 600 }}>{name}</div>}
      {lines.slice(0, n).map((segs, i) => (
        <div key={i} style={{ fontFamily: MONO, fontSize: size, lineHeight: 1.38, color: CLAUDE.PAGE, whiteSpace: 'pre' }}>
          {segs.map((g, k) => (
            <span key={k} style={{
              color: g.dim ? '#CFCBBE' : g.add ? '#BFE3B4' : g.del ? '#F4B9A8' : CLAUDE.PAGE,
              borderBottom: g.link ? `${Math.max(3, size * 0.09)}px solid ${CLAUDE.SPARK}` : 'none',
            }}>{g.s}</span>
          ))}
        </div>
      ))}
    </div>
  );
};

const lerp = (a: number, b: number, p: number) => a + (b - a) * p;
const W = (P: boolean) => (P ? 1080 : 1920);
const H = (P: boolean) => (P ? 1920 : 1080);

// ===========================================================================
// RoHook — RAG is the default pipeline; then Google Cloud proposes OKF
// ===========================================================================
export const roHookSchema = z.object({
  title: z.string().default('RAG is the default'),
  steps: z.array(z.string()).default(['your docs', 'chunks', 'vectors', 'search', 'answer']),
  badge: z.string().default('RAG · the usual way'),
  org: z.string().default('Google Cloud'),
  name: z.string().default('Open Knowledge Format'),
  tags: z.array(z.string()).default(['OKF v0.1', 'June 12, 2026']),
  sub: z.string().default('an open spec for agent knowledge'),
  logo: z.string().default('logos/google/google-01.svg'),
  sparkLine: z.string().default('Why something new?'),
  durationSeconds: z.number().optional(),
});
export const roHookMeta = durMeta(5);
export const RoHook: React.FC<z.infer<typeof roHookSchema>> = ({ title, steps, badge, org, name, tags, sub, logo, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const n = steps.length;
  // landscape: one row of steps across the top half; portrait: a column on the left
  const gap = P ? 22 : 40;
  const sw = P ? 400 : (S.w - gap * (n - 1)) / n;
  const sh = P ? 104 : 150;
  const pos = (i: number) => P ? { x: S.x, y: 330 + i * (sh + gap) } : { x: S.x + i * (sw + gap), y: 300 };
  const card = P ? { x: S.x + 460, y: 330, w: S.w - 460, h: 820 } : { x: S.x + 260, y: 560, w: S.w - 520, h: 330 };
  const cIn = ease(ramp(t, 0.36, 0.46));
  const q = ease(ramp(t, 0.58, 0.66));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {steps.map((s, i) => {
        const p = pos(i);
        const a = ease(ramp(t, 0.03 + i * 0.04, 0.1 + i * 0.04));
        const arrow = i < n - 1;
        return (
          <React.Fragment key={s}>
            <Card style={{ left: p.x, top: p.y, width: sw, height: sh, opacity: a * (1 - 0.35 * cIn), display: 'flex', alignItems: 'center', justifyContent: 'center',
              fontFamily: SANS, fontSize: P ? 50 : 44, color: CLAUDE.INK }}>{s}</Card>
            {arrow && (P
              ? <div style={{ position: 'absolute', left: p.x + sw / 2 - 2, top: p.y + sh, width: 4, height: gap, background: CLAUDE.GHOST, opacity: a }} />
              : <div style={{ position: 'absolute', left: p.x + sw, top: p.y + sh / 2 - 2, width: gap, height: 4, background: CLAUDE.GHOST, opacity: a }} />)}
          </React.Fragment>
        );
      })}
      <div style={{ position: 'absolute', opacity: ease(ramp(t, 0.18, 0.26)),
        ...(P ? { left: S.x, top: 330 + n * (sh + gap) + 6 } : { left: S.x, top: 476 }) }}>
        <Pill text={badge} size={P ? 42 : 42} />
      </div>
      <Card accent style={{ left: card.x, top: card.y, width: card.w, height: P ? undefined : card.h, opacity: cIn,
        transform: `translateY(${(1 - cIn) * 30}px)`, padding: P ? '36px 34px' : '34px 48px',
        display: 'flex', flexDirection: P ? 'column' : 'row', alignItems: P ? 'flex-start' : 'center', gap: P ? 24 : 48 }}>
        <Img src={staticFile(logo)} style={{ height: P ? 130 : 190, width: P ? 130 : 190 }} />
        <div style={{ display: 'flex', flexDirection: 'column', gap: P ? 18 : 16 }}>
          <span style={{ fontFamily: SANS, fontSize: P ? 50 : 44, color: CLAUDE.INK_SOFT }}>{org} proposes</span>
          <span style={{ fontFamily: SERIF, fontSize: P ? 96 : 84, lineHeight: 1.04, color: CLAUDE.INK }}>{name}</span>
          <div style={{ display: 'flex', gap: 16, flexWrap: 'wrap' }}>
            {tags.map((g, k) => <Pill key={g} text={g} size={P ? 48 : 40} accent={k === 1} />)}
          </div>
          <span style={{ fontFamily: SANS, fontSize: P ? 48 : 40, color: CLAUDE.INK, opacity: q }}>{sub}</span>
        </div>
      </Card>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RoRag — chunk the pile, embed, rank by similarity to the question, return top-k
// ===========================================================================
const PILE_DEFAULT = [
  { doc: 'meeting-notes.txt', n: 4 },
  { doc: 'support-faq.txt', n: 2 },
  { doc: 'slack-export.txt', n: 3 },
  { doc: 'onboarding.txt', n: 2 },
];
// deterministic dot positions (unit square) for the 11 chunk vectors, in pile order;
// the three nearest the query are the evidence run's top-3 (chunk idx 1, 6, 2)
const DOTS: Array<[number, number]> = [
  [0.22, 0.30], [0.62, 0.30], [0.70, 0.52], [0.18, 0.70], [0.34, 0.86], [0.12, 0.48],
  [0.56, 0.62], [0.88, 0.80], [0.30, 0.16], [0.86, 0.18], [0.44, 0.40],
];
export const roRagSchema = z.object({
  title: z.string().default('RAG: search on demand'),
  pile: z.array(z.object({ doc: z.string(), n: z.number() })).default(PILE_DEFAULT),
  question: z.string().default('How is revenue calculated?'),
  qdot: z.tuple([z.number(), z.number()]).default([0.64, 0.44]),
  top: z.array(z.object({ i: z.number(), score: z.string(), text: z.string() })).default([
    { i: 1, score: '0.50', text: 'Revenue was up again.' },
    { i: 6, score: '0.41', text: 'Is revenue gross or net?' },
    { i: 2, score: '0.32', text: 'Finance says revenue only counts paid orders.' },
  ]),
  toyNote: z.string().default('toy: word-count vectors stand in for embeddings; scores computed'),
  sparkLine: z.string().default('Search, every time.'),
  durationSeconds: z.number().optional(),
});
export const roRagMeta = durMeta(5);
export const RoRag: React.FC<z.infer<typeof roRagSchema>> = ({ title, pile, question, qdot, top, toyNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  // pile column (landscape left / portrait top), vector map (right / middle), results (bottom)
  const pileBox = P ? { x: S.x, y: 300, w: S.w, h: 340 } : { x: S.x, y: 220, w: 600, h: 560 };
  const map = P ? { x: S.x, y: 670, w: S.w, h: 360 } : { x: S.x + 660, y: 220, w: S.w - 660, h: 420 };
  const res = P ? { x: S.x, y: 1050, w: S.w } : { x: S.x + 660, y: 664, w: S.w - 660 };
  const total = pile.reduce((a, p) => a + p.n, 0);
  let k = 0;
  const chunkRects: Array<{ x: number; y: number; w: number; h: number }> = [];
  const docs = pile.map((p, d) => {
    const cols = P ? 4 : 1;
    const dw = P ? (pileBox.w - 3 * 16) / 4 : pileBox.w;
    const dh = P ? pileBox.h : (pileBox.h - 3 * 20) / 4;
    const dx = P ? pileBox.x + d * (dw + 16) : pileBox.x;
    const dy = P ? pileBox.y : pileBox.y + d * (dh + 20);
    const a = ease(ramp(t, 0.02 + d * 0.025, 0.08 + d * 0.025));
    const split = ease(ramp(t, 0.12, 0.22));
    const head = P ? 70 : 64;
    const chunks = Array.from({ length: p.n }, (_, c) => {
      const cw = P ? dw - 32 : (dw - 40 - (p.n - 1) * 14) / p.n;
      const ch = P ? (dh - head - 24 - (p.n - 1) * 10) / p.n : dh - head - 24;
      const x = P ? dx + 16 : dx + 20 + c * (cw + 14);
      const y = P ? dy + head + c * (ch + 10) : dy + head;
      chunkRects[k] = { x, y, w: cw, h: ch };
      k += 1;
      return <div key={c} style={{ position: 'absolute', left: x, top: y, width: cw, height: ch, borderRadius: 8,
        background: CLAUDE.INK_SOFT, boxSizing: 'border-box', opacity: a * (0.4 + 0.6 * split),
        transform: `scale(${lerp(1, 0.92, split)})` }} />;
    });
    void cols;
    return (
      <React.Fragment key={p.doc}>
        <Card style={{ left: dx, top: dy, width: dw, height: dh, opacity: a }} />
        <div style={{ position: 'absolute', left: dx + (P ? 12 : 20), top: dy + (P ? 10 : 12), opacity: a }}>
          <Pill text={P ? p.doc.replace(/-.*|\.txt/g, '') : p.doc} size={P ? 36 : 34} fill={CLAUDE.INK_SOFT} />
        </div>
        {chunks}
      </React.Fragment>
    );
  });
  const dotIn = (i: number) => ease(ramp(t, 0.24 + i * 0.012, 0.32 + i * 0.012));
  const qIn = ease(ramp(t, 0.52, 0.58));
  const lines = ease(ramp(t, 0.62, 0.7));
  const listIn = (r: number) => ease(ramp(t, 0.68 + r * 0.04, 0.74 + r * 0.04));
  const px = (u: number) => map.x + 40 + u * (map.w - 80);
  const py = (v: number) => map.y + 30 + v * (map.h - 60);
  const topIdx = new Set(top.map((r) => r.i));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {docs}
      <Card style={{ left: map.x, top: map.y, width: map.w, height: map.h, opacity: ease(ramp(t, 0.2, 0.26)) }} />
      <div style={{ position: 'absolute', left: map.x + 18, top: map.y + 14, opacity: ease(ramp(t, 0.2, 0.26)) }}>
        <Pill text={`${total} vectors`} size={P ? 40 : 36} fill={CLAUDE.INK_SOFT} />
      </div>
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0 }}>
        {top.map((r) => {
          const [u, v] = DOTS[r.i];
          const x1 = px(qdot[0]), y1 = py(qdot[1]), x2 = px(u), y2 = py(v);
          const len = Math.hypot(x2 - x1, y2 - y1);
          return <line key={r.i} x1={x1} y1={y1} x2={x2} y2={y2} stroke={CLAUDE.SPARK} strokeWidth={5}
            strokeDasharray={len} strokeDashoffset={len * (1 - lines)} />;
        })}
        {DOTS.slice(0, total).map(([u, v], i) => {
          // dots fly from their chunk to the map
          const c = chunkRects[i];
          const p = dotIn(i);
          const x = lerp(c.x + c.w / 2, px(u), p), y = lerp(c.y + c.h / 2, py(v), p);
          const hit = topIdx.has(i) && lines > 0.5;
          return <circle key={i} cx={x} cy={y} r={hit ? 20 : 15} fill={hit ? CLAUDE.INK : CLAUDE.INK_SOFT} opacity={p > 0 ? 1 : 0} />;
        })}
        <circle cx={px(qdot[0])} cy={py(qdot[1])} r={24} fill={CLAUDE.SPARK} opacity={qIn} />
      </svg>
      <div style={{ position: 'absolute', opacity: qIn, ...(P
        ? { left: S.x + 24, top: map.y + map.h - 84 }
        : { left: px(qdot[0]) - 330, top: py(qdot[1]) + 34 }) }}>
        <Pill text={question} size={P ? 44 : 38} accent />
      </div>
      <div style={{ position: 'absolute', left: res.x, top: res.y, width: res.w, display: 'flex', flexDirection: 'column', gap: P ? 14 : 12 }}>
        {top.map((r, j) => (
          <div key={r.i} style={{ display: 'flex', alignItems: 'center', gap: 18, opacity: listIn(j) }}>
            <Pill text={r.score} size={P ? 46 : 38} style={{ fontFamily: MONO }} />
            <span style={{ fontFamily: SANS, fontSize: P ? 46 : 38, color: CLAUDE.INK, whiteSpace: P ? 'normal' : 'nowrap', lineHeight: 1.15 }}>{r.text}</span>
          </div>
        ))}
      </div>
      {!P && <div style={{ position: 'absolute', left: S.x, top: 806, width: 600, fontFamily: SANS, fontSize: 32, lineHeight: 1.2, color: CLAUDE.INK_SOFT,
        opacity: ease(ramp(t, 0.3, 0.36)) }}>{toyNote}</div>}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RoOkf — the bundle: a file tree, one concept file opened, no vectors needed
// ===========================================================================
const TREE: Seg[][] = [
  [{ s: 'okf_bundle/' }],
  [{ s: '├ index.md' }],
  [{ s: '├ tables/' }],
  [{ s: '│ ├ orders.md', dim: true }],
  [{ s: '│ └ customers.md', dim: true }],
  [{ s: '├ metrics/' }],
  [{ s: '│ └ ' }, { s: 'revenue.md', link: true }],
  [{ s: '└ policies/' }],
  [{ s: '  └ refunds.md', dim: true }],
];
// evidence/okf_bundle/metrics/revenue.md (generated: line dropped for space)
const REVENUE: Seg[][] = [
  [{ s: '---', dim: true }],
  [{ s: 'type: ', dim: true }, { s: 'Metric' }],
  [{ s: 'title: ', dim: true }, { s: 'Revenue' }],
  [{ s: 'description: ', dim: true }, { s: 'How revenue is calculated.' }],
  [{ s: 'tags: ', dim: true }, { s: '[sales, finance]' }],
  [{ s: '---', dim: true }],
  [{ s: 'Revenue is the sum of `amount` over' }],
  [{ s: '[orders]', link: true }, { s: '(../tables/orders.md)', dim: true }],
  [{ s: 'with `status = paid`. Refunded orders' }],
  [{ s: 'are excluded; see ' }, { s: '[refunds]', link: true }, { s: '(...)', dim: true }],
];
export const roOkfSchema = z.object({
  title: z.string().default('OKF: a folder of Markdown'),
  file: z.string().default('metrics/revenue.md'),
  yamlLabel: z.string().default('YAML metadata'),
  linkLabel: z.string().default('links between files'),
  notNeeded: z.array(z.string()).default(['embeddings', 'vector database']),
  reads: z.string().default('the agent reads the files directly'),
  sparkLine: z.string().default('Just files.'),
  durationSeconds: z.number().optional(),
});
export const roOkfMeta = durMeta(6);
export const RoOkf: React.FC<z.infer<typeof roOkfSchema>> = ({ title, file, yamlLabel, linkLabel, notNeeded, reads, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const treeIn = ease(ramp(t, 0.02, 0.1));
  const open = ramp(t, 0.12, 0.3);
  const labels = ease(ramp(t, 0.32, 0.4));
  const strike = ease(ramp(t, 0.66, 0.74));
  const size = P ? 28 : 32;
  const tree = P ? { x: S.x, y: 290, w: 440 } : { x: S.x, y: 220, w: 520 };
  const fileBox = P ? { x: S.x, y: 790, w: S.w } : { x: S.x + 560, y: 220, w: 830 };
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <CodePanel lines={TREE} size={P ? 31 : 34} a={treeIn} style={{ left: tree.x, top: tree.y, width: tree.w }} />
      <CodePanel name={file} lines={REVENUE} size={size} a={ease(ramp(t, 0.1, 0.16))} shown={open}
        style={{ left: fileBox.x, top: fileBox.y, width: fileBox.w }} />
      {/* callouts for the two parts of a concept file */}
      <div style={{ position: 'absolute', opacity: labels, display: 'flex', flexDirection: 'column', gap: 18,
        ...(P ? { left: S.x + 470, top: 300, width: S.w - 470 } : { left: fileBox.x + fileBox.w + 30, top: 250, width: S.r - (fileBox.x + fileBox.w + 30) }) }}>
        <Pill text={yamlLabel} size={P ? 40 : 34} style={{ whiteSpace: 'normal' }} />
        <Pill text={linkLabel} size={P ? 40 : 34} accent style={{ whiteSpace: 'normal' }} />
      </div>
      <div style={{ position: 'absolute', display: 'flex', flexWrap: 'wrap', gap: P ? 6 : 22, alignItems: P ? 'flex-start' : 'center', flexDirection: P ? 'column' : 'row',
        ...(P ? { left: S.x + 470, top: 440, width: S.w - 470 } : { left: S.x, top: 830, width: S.w }), opacity: ease(ramp(t, 0.56, 0.62)) }}>
        {notNeeded.map((x) => (
          <span key={x} style={{ position: 'relative', fontFamily: SERIF, fontSize: P ? 60 : 64, color: CLAUDE.INK, padding: '0 6px' }}>
            {x}
            <span style={{ position: 'absolute', left: 0, top: '55%', height: 7, width: `${strike * 100}%`, background: CLAUDE.SPARK }} />
          </span>
        ))}
        <span style={{ fontFamily: SANS, fontSize: P ? 48 : 40, color: ACC_TEXT, fontWeight: 600, opacity: strike }}>not required</span>
      </div>
      {!P && <div style={{ position: 'absolute', opacity: ease(ramp(t, 0.78, 0.84)), left: S.x + 1000, top: 846 }}>
        <Pill text={reads} size={38} />
      </div>}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RoPhilosophy — a raw pile, searched per question vs. one curated, kept tree
// ===========================================================================
export const roPhilosophySchema = z.object({
  title: z.string().default('A pile vs. a library'),
  ragHead: z.string().default('RAG: a raw pile'),
  okfHead: z.string().default('OKF: one curated base'),
  questions: z.array(z.string()).default(['Q1', 'Q2', 'Q3']),
  searchLabel: z.string().default('searches'),
  tree: z.array(z.tuple([z.number(), z.string()])).default([
    [0, 'index.md'], [1, 'tables/'], [2, 'orders.md'], [2, 'customers.md'], [1, 'metrics/'], [2, 'revenue.md'], [1, 'policies/'], [2, 'refunds.md'],
  ]),
  kept: z.string().default('kept between questions'),
  sparkLine: z.string().default('Search it, or keep it.'),
  durationSeconds: z.number().optional(),
});
export const roPhilosophyMeta = durMeta(5);
// scattered page positions inside the pile box (unit square) + tilt in degrees
const PAGES: Array<[number, number, number]> = [
  [0.05, 0.08, -8], [0.38, 0.02, 6], [0.68, 0.12, -4], [0.12, 0.42, 10], [0.48, 0.36, -12],
  [0.74, 0.48, 7], [0.04, 0.72, -5], [0.34, 0.68, 9], [0.62, 0.76, -9],
];
export const RoPhilosophy: React.FC<z.infer<typeof roPhilosophySchema>> = ({ title, ragHead, okfHead, questions, searchLabel, tree, kept, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const colW = P ? S.w : (S.w - 80) / 2;
  const L = P ? { x: S.x, y: 290, h: 470 } : { x: S.x, y: 220, h: 640 };
  const R = P ? { x: S.x, y: 780, h: 480 } : { x: S.x + colW + 80, y: 220, h: 640 };
  const pileTop = L.y + (P ? 120 : 90);
  const pileH = L.h - (P ? 170 : 200);
  const pw = P ? 200 : 210, ph = P ? 130 : 150;
  // three search sweeps, one per question, across the pile
  const sweeps = questions.map((_, i) => ramp(t, 0.08 + i * 0.12, 0.18 + i * 0.12));
  const done = sweeps.filter((s) => s >= 1).length;
  const rIn = ease(ramp(t, 0.52, 0.6));
  const rowH = P ? 46 : 62;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: L.x, top: L.y, fontFamily: SERIF, fontSize: P ? 88 : 58, color: CLAUDE.INK, opacity: ease(ramp(t, 0.02, 0.08)) }}>{ragHead}</div>
      {PAGES.map(([u, v, rot], i) => (
        <Card key={i} style={{ left: L.x + u * (colW - pw), top: pileTop + v * (pileH - ph), width: pw, height: ph,
          transform: `rotate(${rot}deg)`, opacity: ease(ramp(t, 0.02 + i * 0.01, 0.08 + i * 0.01)), padding: 18, display: 'flex', flexDirection: 'column', gap: 12 }}>
          {[0.9, 0.7, 0.8].map((w, k) => <div key={k} style={{ height: 10, width: `${w * 100}%`, borderRadius: 5, background: CLAUDE.BORDER }} />)}
        </Card>
      ))}
      {sweeps.map((s, i) => s > 0 && s < 1 && (
        <div key={i} style={{ position: 'absolute', left: L.x + lerp(-40, colW - 160, s), top: pileTop - 20, width: 200, height: pileH + 40,
          background: `linear-gradient(90deg, transparent, ${CLAUDE.SPARK}55, transparent)` }} />
      ))}
      <div style={{ position: 'absolute', left: L.x, top: L.y + L.h - (P ? 72 : 90), display: 'flex', gap: 14, alignItems: 'center' }}>
        {questions.map((q, i) => <Pill key={q} text={q} size={P ? 44 : 40} accent={sweeps[i] > 0 && sweeps[i] < 1} a={sweeps[i] > 0 ? 1 : 0.4} />)}
        <span style={{ fontFamily: SANS, fontSize: P ? 46 : 42, color: CLAUDE.INK, marginLeft: 10 }}>{done} {searchLabel}</span>
      </div>
      <div style={{ position: 'absolute', left: R.x, top: R.y, fontFamily: SERIF, fontSize: P ? 88 : 58, color: CLAUDE.INK, opacity: rIn }}>{okfHead}</div>
      <Card style={{ left: R.x, top: R.y + (P ? 112 : 90), width: colW, height: tree.length * rowH + (P ? 36 : 50), opacity: rIn }} />
      {tree.map(([d, name], i) => {
        const a = ease(ramp(t, 0.56 + i * 0.015, 0.62 + i * 0.015));
        const y = R.y + (P ? 130 : 114) + i * rowH;
        return (
          <div key={i} style={{ position: 'absolute', left: R.x + 30 + d * (P ? 56 : 70), top: y, display: 'flex', alignItems: 'center', gap: 14, opacity: a }}>
            <div style={{ width: P ? 16 : 20, height: P ? 16 : 20, borderRadius: 4, background: name.endsWith('/') ? CLAUDE.INK_SOFT : CLAUDE.INK }} />
            <span style={{ fontFamily: MONO, fontSize: P ? 38 : 40, color: CLAUDE.INK }}>{name}</span>
          </div>
        );
      })}
      <div style={{ position: 'absolute', opacity: ease(ramp(t, 0.74, 0.8)),
        ...(P ? { left: S.x + 470, top: R.y + 138 } : { left: R.x + colW - 470, top: R.y + 120 }) }}>
        <Pill text={kept} size={P ? 40 : 38} accent />
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RoAdvantage — no retrieval step (follow links) + plain text in git
// ===========================================================================
// from evidence/rag_vs_okf_toy.out.txt and evidence/okf_git_demo.out.txt
export const roAdvantageSchema = z.object({
  title: z.string().default('No retrieval step'),
  walk: z.array(z.string()).default(['index.md', 'metrics/revenue.md', 'tables/orders.md', 'policies/refunds.md']),
  walkNote: z.string().default('4 of 5 files read · 0 vectors'),
  gitLines: z.array(z.string()).default([
    '$ git log --oneline',
    '60e6d0d Exclude refunds from revenue',
    'f49c815 Add revenue metric',
    '$ git diff HEAD~1',
    '- Revenue is the sum of `amount` over [orders].',
    '+ Revenue is the sum of `amount` over [orders]',
    '+ with `status = paid`. Refunded orders…',
  ]),
  gitNote: z.string().default('real git output on the toy bundle'),
  sparkLine: z.string().default('Read it, diff it.'),
  durationSeconds: z.number().optional(),
});
export const roAdvantageMeta = durMeta(5);
export const RoAdvantage: React.FC<z.infer<typeof roAdvantageSchema>> = ({ title, walk, walkNote, gitLines, gitNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const colW = P ? S.w : 640;
  const step = (i: number) => ease(ramp(t, 0.05 + i * 0.08, 0.11 + i * 0.08));
  const gitIn = ramp(t, 0.5, 0.74);
  const top = P ? 300 : 230;
  const sh = P ? 84 : 104, sg = P ? 26 : 40;
  const gitBox = P ? { x: S.x, y: 840, w: S.w } : { x: S.x + colW + 70, y: 230, w: S.w - colW - 70 };
  const seg = (l: string): Seg[] => [{ s: l, dim: l.startsWith('$'), add: l.startsWith('+'), del: l.startsWith('-') }];
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {walk.map((w, i) => {
        const a = step(i);
        const y = top + i * (sh + sg);
        const live = i === walk.length - 1 ? a : a * (1 - step(i + 1)) ;
        return (
          <React.Fragment key={w}>
            <Card style={{ left: S.x, top: y, width: colW, height: sh, opacity: 0.35 + 0.65 * a,
              border: `${live > 0.5 ? 5 : 3}px solid ${live > 0.5 ? CLAUDE.INK : CLAUDE.BORDER}`,
              display: 'flex', alignItems: 'center', gap: 18, padding: '0 26px' }}>
              <span style={{ fontFamily: SANS, fontSize: P ? 42 : 38, color: CLAUDE.INK_SOFT }}>open</span>
              <span style={{ fontFamily: MONO, fontSize: P ? 44 : 40, color: CLAUDE.INK }}>{w}</span>
            </Card>
            {i < walk.length - 1 && <div style={{ position: 'absolute', left: S.x + 60, top: y + sh, width: 5, height: sg * step(i + 1), background: CLAUDE.SPARK }} />}
          </React.Fragment>
        );
      })}
      <div style={{ position: 'absolute', left: S.x, top: top + walk.length * (sh + sg) - (P ? 6 : 10), opacity: step(walk.length - 1) }}>
        <Pill text={walkNote} size={P ? 44 : 38} accent />
      </div>
      <CodePanel name="metrics/revenue.md · git" lines={gitLines.map(seg)} size={P ? 30 : 32} a={ease(ramp(t, 0.46, 0.52))} shown={gitIn}
        style={{ left: gitBox.x, top: gitBox.y, width: gitBox.w, height: P ? 440 : 440 }} />
      <div style={{ position: 'absolute', opacity: ease(ramp(t, 0.76, 0.82)),
        ...(P ? { left: S.x, top: 1290 - 10 - 0 } : { left: gitBox.x, top: 690 }) }}>
        {!P && <span style={{ fontFamily: SANS, fontSize: 34, color: CLAUDE.INK_SOFT }}>{gitNote}</span>}
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RoCuration — every page is written (person or agent) and then reviewed
// ===========================================================================
export const roCurationSchema = z.object({
  title: z.string().default('Someone has to curate it'),
  pages: z.array(z.object({ file: z.string(), by: z.string() })).default([
    { file: 'orders.md', by: 'human:likhith' },
    { file: 'customers.md', by: 'enrich-agent' },
    { file: 'revenue.md', by: 'human:likhith' },
    { file: 'refunds.md', by: 'enrich-agent' },
  ]),
  stale: z.number().default(3),
  writtenLabel: z.string().default('written'),
  verifiedLabel: z.string().default('reviewed'),
  staleLabel: z.string().default('stale: re-check'),
  caption: z.string().default('OKF v0.2 records this per file: generated · verified · stale_after'),
  sparkLine: z.string().default('Curation is work.'),
  durationSeconds: z.number().optional(),
});
export const roCurationMeta = durMeta(5);
export const RoCuration: React.FC<z.infer<typeof roCurationSchema>> = ({ title, pages, stale, writtenLabel, verifiedLabel, staleLabel, caption, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 300 : 230;
  const rh = P ? 196 : 128, rg = P ? 22 : 22;
  const write = (i: number) => ease(ramp(t, 0.06 + i * 0.07, 0.12 + i * 0.07));
  const review = (i: number) => ease(ramp(t, 0.56 + i * 0.05, 0.6 + i * 0.05));
  const flag = ease(ramp(t, 0.82, 0.86));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {pages.map((p, i) => {
        const y = top + i * (rh + rg);
        const w = write(i), r = review(i);
        const isStale = i === stale && flag > 0;
        return (
          <Card key={p.file} style={{ left: S.x, top: y, width: S.w, height: rh, opacity: 0.3 + 0.7 * w,
            border: `${isStale ? 5 : 3}px solid ${isStale ? CLAUDE.SPARK : CLAUDE.BORDER}`,
            display: 'flex', flexDirection: P ? 'column' : 'row', alignItems: P ? 'flex-start' : 'center', justifyContent: P ? 'center' : 'flex-start',
            gap: P ? 14 : 30, padding: P ? '0 28px' : '0 34px' }}>
            <span style={{ fontFamily: MONO, fontSize: P ? 46 : 44, color: CLAUDE.INK, width: P ? 'auto' : 380 }}>{p.file}</span>
            <div style={{ display: 'flex', gap: 16, alignItems: 'center', flexWrap: 'wrap' }}>
              <Pill text={`${writtenLabel} by ${p.by}`} size={P ? 40 : 38} fill={CLAUDE.INK_SOFT} a={w} />
              {!isStale && <Pill text={`${verifiedLabel} ✓`} size={P ? 40 : 38} a={r} />}
              {isStale && <Pill text={staleLabel} size={P ? 40 : 38} accent a={flag} />}
            </div>
          </Card>
        );
      })}
      <div style={{ position: 'absolute', left: S.x, top: top + pages.length * (rh + rg) + (P ? 10 : 6), width: S.w,
        fontFamily: SANS, fontSize: P ? 46 : 38, lineHeight: 1.2, color: CLAUDE.INK, opacity: ease(ramp(t, 0.36, 0.42)) }}>{caption}</div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RoScale — a huge, unstructured corpus: RAG indexes it unattended; curation can't
// ===========================================================================
export const roScaleSchema = z.object({
  title: z.string().default('Where RAG still wins'),
  docs: z.number().default(2000000),
  docsLabel: z.string().default('raw docs, no structure'),
  ragLabel: z.string().default('RAG: chunk + embed, unattended'),
  okfLabel: z.string().default('OKF: pages someone curates'),
  okfShare: z.number().default(0.02),
  toyNote: z.string().default('illustrative scale'),
  sparkLine: z.string().default('Too big to curate.'),
  durationSeconds: z.number().optional(),
});
export const roScaleMeta = durMeta(5);
export const RoScale: React.FC<z.infer<typeof roScaleSchema>> = ({ title, docs, docsLabel, ragLabel, okfLabel, okfShare, toyNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const grow = ease(ramp(t, 0.04, 0.34));
  const n = Math.round(docs * grow);
  const ragFill = ease(ramp(t, 0.38, 0.48));
  const okfFill = ease(ramp(t, 0.56, 0.8)) * okfShare;
  // a wall of tiny doc tiles that fills as the counter climbs
  const cols = P ? 18 : 40, rows = P ? 8 : 6;
  const tile = P ? 44 : 34, tg = P ? 10 : 9;
  const wallX = S.x, wallY = P ? 440 : 330;
  const lit = Math.floor(grow * cols * rows);
  const barTop = P ? wallY + rows * (tile + tg) + 50 : wallY + rows * (tile + tg) + 46;
  const barH = P ? 84 : 72;
  const bar = (i: number, label: string, f: number, accent: boolean) => {
    const y = barTop + i * (barH + (P ? 120 : 100));
    return (
      <React.Fragment key={i}>
        <div style={{ position: 'absolute', left: S.x, top: y - (P ? 66 : 56), fontFamily: SANS, fontSize: P ? 48 : 42, color: CLAUDE.INK }}>{label}</div>
        <div style={{ position: 'absolute', left: S.x, top: y, width: S.w, height: barH, borderRadius: 12, background: CLAUDE.PILL, border: `3px solid ${CLAUDE.BORDER}`, boxSizing: 'border-box' }} />
        <div style={{ position: 'absolute', left: S.x, top: y, width: Math.max(f > 0 ? 14 : 0, S.w * f), height: barH, borderRadius: 12, background: accent ? CLAUDE.SPARK : CLAUDE.INK }} />
      </React.Fragment>
    );
  };
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top: P ? 290 : 196, display: 'flex', alignItems: 'baseline', gap: 22, flexWrap: 'wrap', width: S.w }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 110 : 104, lineHeight: 1, color: ACC_TEXT }}>{n.toLocaleString('en-US')}</span>
        <span style={{ fontFamily: SANS, fontSize: P ? 48 : 42, color: CLAUDE.INK }}>{docsLabel}</span>
        {!P && <span style={{ fontFamily: SANS, fontSize: 32, color: CLAUDE.INK_SOFT, marginLeft: 'auto' }}>{toyNote}</span>}
      </div>
      {Array.from({ length: cols * rows }, (_, i) => (
        <div key={i} style={{ position: 'absolute', left: wallX + (i % cols) * (tile + tg), top: wallY + Math.floor(i / cols) * (tile + tg),
          width: tile, height: tile, borderRadius: 5, background: i < lit ? CLAUDE.INK_SOFT : CLAUDE.PILL }} />
      ))}
      {bar(0, ragLabel, ragFill, false)}
      {bar(1, okfLabel, okfFill, true)}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
