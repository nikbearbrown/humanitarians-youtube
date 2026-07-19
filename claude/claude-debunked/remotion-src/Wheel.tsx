import React from 'react';
import { AbsoluteFill, interpolate, useCurrentFrame } from 'remotion';

// ── Palette lifted from the original graphic ─────────────────────────────
const BG = '#F4EFE6';
const RUST = '#A93E2C';
const RUST_DARK = '#7A2A1D';
const INK = '#33221B';
const WEDGE = '#F8DCD4';
const PILL_BG = '#F1E8DA';
const AMBER = '#B07C2A';
const GREY = '#9A938A';
const GREEN_TAG = '#2E6E4E';

type Status = 'real' | 'stale' | 'invented';
type Node = {
  x: number; y: number; w?: number;
  title: string; desc: string;
  row: number; status: Status; tag?: string; spark?: boolean;
};

// ── Content: verbatim from the graphic; status from the fact-check ──────
const NODES: Node[] = [
  // Row 0 — models
  { x: 135, y: 165, w: 150, title: 'Claude Opus 4.8', desc: 'Sharper judgment, deeper honesty, agentic coding & computer use', row: 0, status: 'real', spark: true },
  { x: 330, y: 165, w: 160, title: 'Claude Sonnet 4.6', desc: 'Balanced speed + intelligence for business workflows', row: 0, status: 'stale', tag: 'current is Sonnet 5', spark: true },
  { x: 545, y: 165, w: 150, title: 'Claude Haiku 4.5', desc: 'Fast, lightweight model for high-volume tasks', row: 0, status: 'real', spark: true },
  { x: 740, y: 165, w: 190, title: 'Claude Mythos (Preview)', desc: 'Restricted to select security orgs now, public rollout "in coming weeks"', row: 0, status: 'stale', tag: 'still invite-only; no public rollout', spark: true },
  // Row 1 — framework & tools
  { x: 440, y: 298, w: 180, title: 'Claude Managed Agents', desc: 'Hosted, stateful long-running agent sessions', row: 1, status: 'real' },
  { x: 700, y: 292, w: 170, title: 'Claude Marketplace', desc: 'Enterprise-ready partner tools through a unified ecosystem', row: 1, status: 'real', tag: 'real — launched' },
  { x: 330, y: 415, w: 160, title: 'Claude Agent SDK', desc: 'Build & run autonomous self-hosted agents', row: 1, status: 'real' },
  { x: 540, y: 415, w: 150, title: 'Claude API Core', desc: 'The foundation powering every integration', row: 1, status: 'stale', tag: 'API real; not the name' },
  { x: 760, y: 415, w: 170, title: 'MCP', desc: 'Industry standard for connecting AI to tools & data', row: 1, status: 'real' },
  // Row 2 — production & workspace
  { x: 390, y: 545, w: 140, title: 'Claude Code', desc: 'Agentic AI coding tool for developers; tens of parallel subagents', row: 2, status: 'real' },
  { x: 555, y: 545, w: 130, title: 'Cowork', desc: 'Agentic AI for knowledge workers; multi-step tasks', row: 2, status: 'real' },
  { x: 710, y: 545, w: 140, title: 'Claude Design', desc: 'Polished visuals & prototypes, powered by Opus 4.8', row: 2, status: 'stale', tag: 'real — but Opus 4.7' },
  { x: 858, y: 545, w: 130, title: 'Claude Security', desc: 'Zero Trust framework for enterprise agents', row: 2, status: 'real', tag: 'real — shipping' },
  // Row 3 — memory & storage
  { x: 430, y: 686, w: 160, title: 'Claude Context Store', desc: 'Persistent session intelligence', row: 3, status: 'invented' },
  { x: 720, y: 686, w: 160, title: 'Safe Artifact Repo', desc: 'Controlled output storage for compliance', row: 3, status: 'invented' },
  { x: 355, y: 800, w: 140, title: 'Memory Store', desc: 'Long-running memory, with enterprise controls', row: 3, status: 'invented' },
  { x: 545, y: 810, w: 170, title: 'Context Window Cache', desc: 'Optimized token efficiency at scale', row: 3, status: 'invented' },
  { x: 775, y: 800, w: 170, title: 'Model Weights Archive', desc: 'Governed, versioned model storage', row: 3, status: 'invented' },
  // Row 4 — security & governance
  { x: 335, y: 935, w: 175, title: 'Constitutional AI Checker', desc: 'Real-time alignment enforcement on every output', row: 4, status: 'invented', tag: 'method, not product' },
  { x: 565, y: 935, w: 180, title: 'RLHF Compliance Engine', desc: 'Outputs validated against safety standards', row: 4, status: 'invented' },
  { x: 795, y: 935, w: 175, title: 'Adversarial Defense Layer', desc: 'Shields against prompt injection & jailbreaks', row: 4, status: 'invented' },
  // Row 5 — deployment & ci/cd
  { x: 130, y: 1085, w: 175, title: 'Anthropic Inference Cluster', desc: 'Purpose-built compute for LLM serving', row: 5, status: 'invented' },
  { x: 360, y: 1095, w: 180, title: 'Research Workflow Pipeline', desc: 'From experiment to production, safely', row: 5, status: 'invented' },
  { x: 570, y: 1105, w: 165, title: 'Model Safety Evaluator', desc: 'Mandatory checks before every release', row: 5, status: 'invented' },
  { x: 700, y: 1035, w: 150, title: 'RLHF Data Preparer', desc: 'High-quality data for continuous alignment', row: 5, status: 'invented' },
  { x: 810, y: 1105, w: 170, title: 'Instruction Tuning Pipeline', desc: 'Continuous model & agent improvement', row: 5, status: 'invented' },
];

const PILLS = [
  { x: 470, y: 362, label: 'Multimodel input', row: 1 },
  { x: 723, y: 362, label: 'Tool Use (API)', row: 1 },
  { x: 640, y: 618, label: 'Workspace Integration · Chrome · Excel · PowerPoint · Slack', row: 2, wide: true },
  { x: 505, y: 756, label: 'Memory', row: 3 },
  { x: 700, y: 756, label: 'Storage', row: 3 },
  { x: 555, y: 892, label: 'Zero Trust Security Framework', row: 4, wide: true },
  { x: 215, y: 1035, label: 'Compute', row: 5 },
  { x: 455, y: 1035, label: 'CI/CD Pipeline', row: 5 },
  { x: 850, y: 1035, label: 'Model Improvement', row: 5 },
];

// Circuit traces per row: polylines with junction dots at each vertex.
const TRACES: { row: number; pts: [number, number][] }[] = [
  { row: 0, pts: [[120, 140], [940, 140]] },
  { row: 0, pts: [[120, 140], [120, 300]] },
  { row: 1, pts: [[300, 340], [900, 340]] },
  { row: 1, pts: [[320, 390], [900, 390]] },
  { row: 1, pts: [[430, 340], [430, 390]] },
  { row: 2, pts: [[330, 520], [960, 520]] },
  { row: 2, pts: [[330, 460], [330, 520]] },
  { row: 3, pts: [[350, 675], [900, 675]] },
  { row: 3, pts: [[350, 775], [900, 775]] },
  { row: 3, pts: [[560, 675], [560, 775]] },
  { row: 4, pts: [[300, 910], [930, 910]] },
  { row: 5, pts: [[110, 1010], [940, 1010]] },
  { row: 5, pts: [[110, 1010], [110, 1085]] },
];

const WEDGES = [
  'Core\nModels', 'Framework\n& Tools', 'Production &\nWorkspace',
  'Memory &\nStorage', 'Security &\nGovernance', 'Deployment\n& CI/CD',
];

const SANS = '-apple-system, "SF Pro Display", "Helvetica Neue", "Segoe UI", sans-serif';

const Spark: React.FC<{ size: number; color?: string }> = ({ size, color = RUST }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" style={{ display: 'block' }}>
    {Array.from({ length: 8 }, (_, i) => (
      <line key={i} x1={12} y1={12}
        x2={12 + 10 * Math.cos((i * Math.PI) / 4 + 0.2)}
        y2={12 + 10 * Math.sin((i * Math.PI) / 4 + 0.2)}
        stroke={color} strokeWidth={3} strokeLinecap="round" />
    ))}
  </svg>
);

// annular sector path
function wedgePath(cx: number, cy: number, r1: number, r2: number, a0: number, a1: number): string {
  const r = (d: number) => (d * Math.PI) / 180;
  const p = (radius: number, a: number) => `${cx + radius * Math.cos(r(a))} ${cy + radius * Math.sin(r(a))}`;
  return `M ${p(r2, a0)} A ${r2} ${r2} 0 0 1 ${p(r2, a1)} L ${p(r1, a1)} A ${r1} ${r1} 0 0 0 ${p(r1, a0)} Z`;
}

const ROW_START = (row: number) => 70 + row * 52;   // frames: when each row begins
const GRADE_START = 470;                              // verification sweep begins
const clamp = { extrapolateLeft: 'clamp' as const, extrapolateRight: 'clamp' as const };

export const EcosystemWheel: React.FC<{ grade?: boolean; startAt?: number; focus?: 'real' | 'stale' | 'invented' | 'twist' }> = ({ grade = true, startAt = 0, focus }) => {
  const frame = useCurrentFrame() + startAt;
  const focMatch = (n: Node) => !focus ? true : focus === 'twist' ? (n.title === 'Claude Marketplace' || n.title === 'Claude Security') : n.status === focus;
  const titleIn = interpolate(frame, [0, 18], [0, 1], clamp);

  const gradeAt = (i: number) => GRADE_START + 10 + i * 5;

  return (
    <AbsoluteFill style={{ background: BG, fontFamily: SANS }}>
      {/* Title */}
      <div style={{ position: 'absolute', top: 26, width: '100%', textAlign: 'center', opacity: titleIn, transform: `translateY(${(1 - titleIn) * 12}px)` }}>
        <div style={{ fontSize: 42, fontWeight: 800, color: RUST, letterSpacing: '-0.01em' }}>
          Anthropic Claude Agentic AI Ecosystem
        </div>
        <div style={{ fontSize: 19, fontWeight: 600, color: INK, marginTop: 4 }}>
          Understanding the core technology from research to reasoning to production deployment
        </div>
      </div>

      {/* Hub + wedges */}
      <svg width={1000} height={1200} style={{ position: 'absolute', inset: 0 }}>
        {WEDGES.map((label, i) => {
          const a0 = -78 + i * 31;
          const a1 = a0 + 28;
          const inAt = interpolate(frame, [40 + i * 10, 58 + i * 10], [0, 1], clamp);
          const mid = ((a0 + a1) / 2) * (Math.PI / 180);
          const lr = 168;
          const lx = 150 + lr * Math.cos(mid);
          const ly = 640 + lr * Math.sin(mid);
          const rot = (a0 + a1) / 2 + 90;
          return (
            <g key={i} opacity={inAt} transform={`rotate(${(1 - inAt) * -6} 150 640)`}>
              <path d={wedgePath(150, 640, 92, 232, a0, a1)} fill={WEDGE} stroke="#EFC4B8" strokeWidth={2} />
              {label.split('\n').map((line, j) => (
                <text key={j} x={lx} y={ly + (j - 0.5) * 20} fontSize={16.5} fontWeight={800} fill={INK}
                  textAnchor="middle" fontFamily={SANS}
                  transform={`rotate(${rot > 90 && rot < 270 ? rot - 180 : rot} ${lx} ${ly})`}>
                  {line}
                </text>
              ))}
            </g>
          );
        })}
        {/* hub */}
        <g opacity={interpolate(frame, [30, 46], [0, 1], clamp)}>
          <circle cx={150} cy={640} r={86} fill={BG} stroke="#E8DCCB" strokeWidth={2} />
        </g>

        {/* circuit traces */}
        {TRACES.map((t, ti) => {
          const start = ROW_START(t.row);
          const p = interpolate(frame, [start, start + 22], [0, 1], clamp);
          const d = 'M ' + t.pts.map(([x, y]) => `${x} ${y}`).join(' L ');
          return (
            <g key={ti}>
              <path d={d} stroke={RUST} strokeWidth={3} fill="none" pathLength={1}
                strokeDasharray={1} strokeDashoffset={1 - p} strokeLinecap="round" />
              {t.pts.map(([x, y], pi) => (
                <circle key={pi} cx={x} cy={y} r={6} fill={RUST}
                  opacity={p > pi / Math.max(1, t.pts.length - 1) ? 1 : 0} />
              ))}
            </g>
          );
        })}
      </svg>

      {/* hub content (HTML for crisp text) */}
      <div style={{ position: 'absolute', left: 150 - 70, top: 640 - 40, width: 140, textAlign: 'center', opacity: interpolate(frame, [34, 50], [0, 1], clamp) }}>
        <div style={{ display: 'flex', justifyContent: 'center' }}><Spark size={40} /></div>
        <div style={{ fontSize: 26, fontWeight: 800, color: INK, marginTop: 6 }}>CLAUDE</div>
        <div style={{ fontSize: 13, fontWeight: 700, color: RUST, letterSpacing: '0.12em' }}>ANTHROP/C</div>
      </div>

      {/* pills */}
      {PILLS.map((p, i) => {
        const inAt = interpolate(frame, [ROW_START(p.row) + 14, ROW_START(p.row) + 26], [0, 1], clamp);
        return (
          <div key={i} style={{
            position: 'absolute', left: p.x - ((p as any).wide ? 150 : 70), top: p.y - 14,
            width: (p as any).wide ? 300 : 140, textAlign: 'center',
            background: PILL_BG, border: `1.5px solid ${RUST}`, borderRadius: 6,
            fontSize: 13, fontWeight: 700, color: INK, padding: '5px 4px',
            opacity: inAt, transform: `translateY(${(1 - inAt) * 8}px)`,
          }}>
            {p.label}
          </div>
        );
      })}

      {/* nodes */}
      {NODES.map((n, i) => {
        const inAt = interpolate(frame, [ROW_START(n.row) + 18 + (i % 5) * 5, ROW_START(n.row) + 30 + (i % 5) * 5], [0, 1], clamp);
        const g = grade ? interpolate(frame, [gradeAt(i), gradeAt(i) + 12], [0, 1], clamp) : 0;
        const dim = n.status === 'invented' ? g : 0;
        const tagColor = n.status === 'invented' ? GREY : n.status === 'stale' ? AMBER : GREEN_TAG;
        const tagText = n.tag ?? (n.status === 'invented' ? 'not a product' : n.status === 'stale' ? 'outdated' : '');
        return (
          <div key={i} style={{
            position: 'absolute', left: n.x, top: n.y, width: n.w ?? 160,
            opacity: inAt * (1 - dim * 0.45) * (focMatch(n) ? 1 : 0.18),
            transform: `translateY(${(1 - inAt) * 10}px)`,
            filter: dim > 0.5 ? 'grayscale(0.9)' : undefined,
          }}>
            <div style={{ display: 'flex', gap: 6, alignItems: 'flex-start' }}>
              {n.spark && <div style={{ marginTop: 2 }}><Spark size={16} /></div>}
              <div>
                <div style={{ fontSize: 16.5, fontWeight: 800, color: INK, lineHeight: 1.15, textDecoration: dim > 0.5 && n.status === 'invented' ? 'line-through' : 'none', textDecorationColor: RUST }}>
                  {n.title}
                </div>
                <div style={{ fontSize: 12.5, fontWeight: 500, color: RUST_DARK, lineHeight: 1.25, marginTop: 2 }}>
                  {n.desc}
                </div>
                {grade && tagText !== '' && (
                  <div style={{
                    display: 'inline-block', marginTop: 4, fontSize: 11, fontWeight: 800,
                    color: '#FFF', background: tagColor, borderRadius: 4, padding: '2px 7px',
                    opacity: g, transform: `scale(${0.8 + 0.2 * g})`,
                  }}>
                    {tagText.toUpperCase()}
                  </div>
                )}
              </div>
            </div>
          </div>
        );
      })}

      {/* grading phase: the missing flagship + the verdict strip */}
      {grade && (
        <>
          <div style={{
            position: 'absolute', left: 40, top: 292, width: 330,
            background: '#FFFFFF', border: `2.5px solid ${RUST}`, borderRadius: 8,
            padding: '8px 12px', boxShadow: '0 6px 20px rgba(122,42,29,0.18)',
            opacity: ((!focus || focus === 'stale') ? 1 : 0) * interpolate(frame, [GRADE_START + 150, GRADE_START + 165], [0, 1], clamp),
            transform: `translateY(${(1 - interpolate(frame, [GRADE_START + 150, GRADE_START + 165], [0, 1], clamp)) * 10}px)`,
          }}>
            <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
              <Spark size={18} />
              <span style={{ fontSize: 17, fontWeight: 800, color: INK }}>Missing: Claude Fable 5</span>
            </div>
            <div style={{ fontSize: 12.5, color: RUST_DARK, marginTop: 2 }}>
              The flagship isn’t on the wheel at all — in the month it was the biggest AI story running.
            </div>
          </div>
          <div style={{
            position: 'absolute', left: 0, right: 0, bottom: 0, background: RUST,
            color: '#FBF6EC', textAlign: 'center', padding: '14px 0',
            fontSize: 19, fontWeight: 800,
            opacity: ((!focus || focus === 'twist') ? 1 : 0) * interpolate(frame, [GRADE_START + 180, GRADE_START + 195], [0, 1], clamp),
          }}>
            13 of these boxes are not products. Two the debunkers called fake are real. The flagship is missing.
          </div>
        </>
      )}

      {/* credit */}
      <div style={{ position: 'absolute', right: 18, top: 1170, fontSize: 11, color: GREY }}>
        after @rakeshgohel01 — rebuilt & graded in Remotion
      </div>
    </AbsoluteFill>
  );
};

export const WHEEL_FRAMES = 720;
