/**
 * Higgsfield.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-higgsfield ("Higgsfield and Claude: Directing AI Video", @HumanitariansAI).
 *
 * Same contract as RLHF.tsx (stage helpers from JevExplainer.tsx): each component lays out
 * natively for 16:9 (<Name>) and 9:16 (<Name>916) — never a crop — and every motion is a pure
 * function of progress, conformed via `durationSeconds`. No Higgsfield call was made for this reel:
 * every "shot" is a native rebuilt diagram, and every fact on screen is logged in the reel's SOURCES.md.
 *
 *   HfHook     — one prompt → minutes later → a multi-shot film; who is directing?
 *   HfPlatform — Higgsfield: many image + video models in one place; Cinema Studio, characters, 4K
 *   HfConnect  — Claude app ↔ official MCP connector (OAuth, no API key); Claude Code ↔ CLI + skills
 *   HfRoles    — Claude = director (script, shots, prompts, continuity); Higgsfield = camera crew
 *   HfPipeline — Claude plans → Higgsfield shoots (≤ ~15 s each) → Claude checks → stitched film
 *   HfVoyager  — redrawn from Higgsfield's demo: one prompt → NASA public-domain + labelled AI shots
 *   HfLimits   — paid credits · drift between shots · labelling is your job
 *   HfDirect   — from operating the camera to directing: plan · judge · reject
 */
import React from 'react';
import { AbsoluteFill, Img, staticFile } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ACC_TEXT, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';
import type { Stage } from './JevExplainer';

const W = (P: boolean) => (P ? 1080 : 1920);
const H = (P: boolean) => (P ? 1920 : 1080);

const LOGO = {
  claude: 'logos/claude/claude-01.svg',
  claudeCode: 'logos/claude/claude-code-01.svg',
  higgsfield: 'logos/higgsfield/higgsfield-01.svg',
} as const;

// filled pill (GATE T reads outlined pills as overlapping text — always filled)
const Pill: React.FC<{ text: string; size: number; a?: number; accent?: boolean; fill?: string; color?: string; mono?: boolean; style?: React.CSSProperties }> = ({ text, size, a = 1, accent, fill, color, mono, style }) => (
  <span style={{
    display: 'inline-block', padding: `${size * 0.16}px ${size * 0.42}px`, borderRadius: size, boxSizing: 'border-box',
    background: fill ?? (accent ? ACC_TEXT : CLAUDE.INK),
    fontFamily: mono ? MONO : SANS, fontSize: size, lineHeight: 1.1, color: color ?? CLAUDE.CARD, opacity: a, whiteSpace: 'nowrap', ...style,
  }}>{text}</span>
);

const Label: React.FC<{ text: string; size: number; style?: React.CSSProperties; color?: string; serif?: boolean }> = ({ text, size, style, color, serif }) => (
  <div style={{ position: 'absolute', fontFamily: serif ? SERIF : SANS, fontSize: size, lineHeight: 1.15, color: color ?? CLAUDE.INK, ...style }}>{text}</div>
);

const Logo: React.FC<{ src: string; size: number; style?: React.CSSProperties; a?: number }> = ({ src, size, style, a = 1 }) => (
  <Img src={staticFile(src)} style={{ width: size, height: size, opacity: a, ...style }} />
);

// straight arrow (ink), drawn on a full-frame svg
const Arrow: React.FC<{ st: Stage; x1: number; y1: number; x2: number; y2: number; a: number; w?: number }> = ({ st, x1, y1, x2, y2, a, w = 5 }) => {
  const ang = Math.atan2(y2 - y1, x2 - x1);
  const h = st.P ? 40 : 22, s = st.P ? 22 : 12;
  const p = (dx: number, dy: number) => `${x2 + dx * Math.cos(ang) - dy * Math.sin(ang)},${y2 + dx * Math.sin(ang) + dy * Math.cos(ang)}`;
  return (
    <svg width={W(st.P)} height={H(st.P)} style={{ position: 'absolute', left: 0, top: 0, opacity: a }}>
      <line x1={x1} y1={y1} x2={x2 - h * 0.8 * Math.cos(ang)} y2={y2 - h * 0.8 * Math.sin(ang)} stroke={CLAUDE.INK} strokeWidth={w} />
      <polygon points={`${p(0, 0)} ${p(-h, -s)} ${p(-h, s)}`} fill={CLAUDE.INK} />
    </svg>
  );
};

// a "shot" thumbnail: a small native frame (sky, ground, a sun), filled shapes only
const Shot: React.FC<{ w: number; h: number; variant?: number; dark?: boolean; probe?: boolean; style?: React.CSSProperties }> = ({ w, h, variant = 0, dark, probe, style }) => {
  const sunX = [0.72, 0.3, 0.55, 0.82, 0.4, 0.62][variant % 6];
  const ground = [0.68, 0.74, 0.62, 0.7, 0.66, 0.72][variant % 6];
  const stars = Array.from({ length: 14 }, (_, i) => ({ x: ((i * 37 + variant * 53) % 97) / 97, y: ((i * 61 + variant * 29) % 89) / 89 }));
  return (
    <div style={{ position: 'absolute', width: w, height: h, borderRadius: 14, overflow: 'hidden', background: dark ? '#2B2A24' : CLAUDE.FOOTER, ...style }}>
      <svg width={w} height={h} style={{ position: 'absolute', left: 0, top: 0 }}>
        {dark ? (
          <>
            {stars.map((s, i) => <circle key={i} cx={s.x * w} cy={s.y * h} r={i % 4 === 0 ? 3.5 : 2.2} fill={CLAUDE.PAGE} opacity={0.8} />)}
            {probe && (
              <g transform={`translate(${w * 0.5}, ${h * 0.5})`}>
                <ellipse cx={0} cy={-h * 0.08} rx={h * 0.2} ry={h * 0.07} fill={CLAUDE.GHOST} />
                <rect x={-h * 0.06} y={-h * 0.02} width={h * 0.12} height={h * 0.12} fill={CLAUDE.GHOST} />
                <rect x={h * 0.06} y={h * 0.03} width={h * 0.28} height={h * 0.025} fill={CLAUDE.GHOST} />
              </g>
            )}
          </>
        ) : (
          <>
            <rect x={0} y={0} width={w} height={h * ground} fill={CLAUDE.PILL} />
            <circle cx={w * sunX} cy={h * 0.3} r={h * 0.11} fill={CLAUDE.GHOST} />
            <rect x={0} y={h * ground} width={w} height={h * (1 - ground)} fill={CLAUDE.BORDER} />
            <circle cx={w * (1 - sunX)} cy={h * ground - h * 0.09} r={h * 0.09} fill={CLAUDE.INK_SOFT} />
          </>
        )}
      </svg>
    </div>
  );
};

// a simple non-human character (a round mascot with an antenna), drawn in filled shapes
const Mascot: React.FC<{ size: number; color: string; scarf: string; tall?: number }> = ({ size, color, scarf, tall = 1 }) => (
  <svg width={size} height={size * 1.1} viewBox="0 0 100 110">
    <rect x={47} y={2} width={6} height={18} fill={CLAUDE.INK_SOFT} />
    <circle cx={50} cy={6} r={6} fill={scarf} />
    <ellipse cx={50} cy={62} rx={40} ry={40 * tall} fill={color} />
    <circle cx={36} cy={56} r={7} fill={CLAUDE.CARD} />
    <circle cx={64} cy={56} r={7} fill={CLAUDE.CARD} />
    <rect x={18} y={84} width={64} height={12} rx={6} fill={scarf} />
  </svg>
);

// ===========================================================================
// HfHook — one prompt, minutes later, a multi-shot film. Who is directing?
// ===========================================================================
export const hfHookSchema = z.object({
  title: z.string().default('One prompt, one film'),
  prompt: z.string().default('Make a short animated film about a lost robot.'),
  later: z.string().default('then'),
  shots: z.number().default(4),
  question: z.string().default('How does a chatbot end up directing?'),
  note: z.string().default('illustrative'),
  sparkLine: z.string().default('Who is directing?'),
  durationSeconds: z.number().optional(),
});
export const hfHookMeta = durMeta(5);
export const HfHook: React.FC<z.infer<typeof hfHookSchema>> = ({ title, prompt, later, shots, question, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const pIn = ease(ramp(t, 0.03, 0.12));
  const lIn = ease(ramp(t, 0.2, 0.28));
  const qIn = ease(ramp(t, 0.62, 0.72));
  const pY = P ? 290 : 196, pH = P ? 210 : 130;
  const lY = pY + pH + (P ? 34 : 28);
  const gap = P ? 30 : 28;
  const cols = P ? 2 : shots;
  const fw = (S.w - gap * (cols - 1)) / cols;
  const fh = P ? 230 : 330;
  const fY = lY + (P ? 100 : 90);
  const rows = Math.ceil(shots / cols);
  const qY = fY + rows * fh + (rows - 1) * gap + (P ? 44 : 40);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: S.x, top: pY, width: S.w, height: pH, opacity: pIn, transform: `translateY(${(1 - pIn) * 14}px)`,
        display: 'flex', alignItems: 'center', gap: 30, padding: P ? '0 34px' : '0 40px', ...(P ? { background: CLAUDE.INK, border: `3px solid ${CLAUDE.INK}` } : {}) }}>
        <Logo src={LOGO.claude} size={P ? 90 : 80} />
        <span style={{ fontFamily: SERIF, fontSize: P ? 58 : 58, color: P ? CLAUDE.CARD : CLAUDE.INK, lineHeight: 1.15 }}>{prompt}</span>
      </Card>
      <div style={{ position: 'absolute', left: S.x, top: lY, opacity: lIn, display: 'flex', gap: 20, alignItems: 'center' }}>
        <Pill text={later} size={P ? 46 : 42} />
        <span style={{ fontFamily: SANS, fontSize: P ? 40 : 36, color: CLAUDE.INK_SOFT }}>{note}</span>
      </div>
      {Array.from({ length: shots }, (_, i) => {
        const a = ease(ramp(t, 0.28 + i * 0.07, 0.36 + i * 0.07));
        const c = i % cols, r = Math.floor(i / cols);
        const x = S.x + c * (fw + gap), y = fY + r * (fh + gap);
        return (
          <div key={i} style={{ position: 'absolute', left: x, top: y, width: fw, height: fh, opacity: a, transform: `scale(${0.94 + 0.06 * a})` }}>
            <Shot w={fw} h={fh} variant={i} />
            <div style={{ position: 'absolute', left: fw * [0.55, 0.2, 0.42, 0.62][i % 4], top: fh * 0.36 }}>
              <Mascot size={fh * 0.5} color={CLAUDE.INK_SOFT} scarf={CLAUDE.INK} />
            </div>
            <div style={{ position: 'absolute', left: 16, top: 16 }}><Pill text={`shot ${i + 1}`} size={P ? 40 : 36} /></div>
          </div>
        );
      })}
      <div style={{ position: 'absolute', left: S.x, top: qY, width: S.w, opacity: qIn, transform: `translateY(${(1 - qIn) * 12}px)`,
        fontFamily: SERIF, fontSize: P ? 62 : 64, color: CLAUDE.INK, lineHeight: 1.15 }}>{question}</div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// HfPlatform — many image + video models in one place, plus the studio tools
// ===========================================================================
export const hfPlatformSchema = z.object({
  title: z.string().default('What Higgsfield is'),
  name: z.string().default('Higgsfield'),
  tagline: z.string().default('dozens of models, one place'),
  modelsLabel: z.string().default('image + video models'),
  models: z.array(z.string()).default(['Kling', 'Veo', 'Seedance', 'MiniMax Hailuo', 'Seedream', 'GPT Image']),
  tools: z.array(z.object({ name: z.string(), what: z.string() })).default([
    { name: 'Cinema Studio', what: 'camera-move presets' },
    { name: 'Characters', what: 'kept consistent' },
    { name: '4K', what: 'up to 4K on some tools' },
  ]),
  note: z.string().default("named on Higgsfield's own pages; the list changes"),
  sparkLine: z.string().default('One studio, many models.'),
  durationSeconds: z.number().optional(),
});
export const hfPlatformMeta = durMeta(5);
export const HfPlatform: React.FC<z.infer<typeof hfPlatformSchema>> = ({ title, name, tagline, modelsLabel, models, tools, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const lIn = ease(ramp(t, 0.03, 0.12));
  const logo = P ? 210 : 260;
  const lX = P ? S.x : S.x + 20, lY = P ? 290 : 250;
  const rX = P ? S.x : S.x + 520, rW = P ? S.w : S.r - (S.x + 520);
  const mY = P ? lY + logo + 50 : 200;
  const tY = P ? mY + 330 : 560;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: lX, top: lY, opacity: lIn, display: 'flex', flexDirection: P ? 'row' : 'column', alignItems: P ? 'center' : 'flex-start', gap: P ? 34 : 24 }}>
        <Logo src={LOGO.higgsfield} size={logo} style={{ borderRadius: logo * 0.22 }} />
        <div>
          <div style={{ fontFamily: SERIF, fontSize: P ? 92 : 84, color: CLAUDE.INK, lineHeight: 1 }}>{name}</div>
          <div style={{ fontFamily: SANS, fontSize: P ? 44 : 40, color: CLAUDE.INK_SOFT, marginTop: 14, maxWidth: P ? undefined : 440 }}>{tagline}</div>
        </div>
      </div>
      {/* the models: chips flow into one place */}
      <div style={{ position: 'absolute', left: rX, top: mY, width: rW }}>
        <div style={{ fontFamily: SANS, fontSize: P ? 42 : 38, color: CLAUDE.INK_SOFT, marginBottom: 18, opacity: ease(ramp(t, 0.12, 0.2)) }}>{modelsLabel}</div>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: P ? 18 : 20 }}>
          {models.map((m, i) => {
            const a = ease(ramp(t, 0.14 + i * 0.04, 0.2 + i * 0.04));
            return <Pill key={m} text={m} size={P ? 50 : 48} fill={CLAUDE.INK_SOFT} a={a} style={{ transform: `translateY(${(1 - a) * 16}px)` }} />;
          })}
        </div>
        <div style={{ fontFamily: SANS, fontSize: P ? 36 : 32, color: CLAUDE.INK_SOFT, marginTop: 16, opacity: ease(ramp(t, 0.36, 0.44)) }}>{note}</div>
      </div>
      {/* the tools */}
      <div style={{ position: 'absolute', left: rX, top: tY, width: rW, display: 'flex', flexDirection: P ? 'column' : 'row', gap: P ? 22 : 28 }}>
        {tools.map((tl, i) => {
          const a = ease(ramp(t, 0.42 + i * 0.1, 0.5 + i * 0.1));
          return (
            <div key={tl.name} style={{ flex: 1, position: 'relative', background: P ? CLAUDE.INK : CLAUDE.CARD, border: `3px solid ${P ? (i === 0 ? ACC_TEXT : CLAUDE.INK) : (i === 0 ? ACC_TEXT : CLAUDE.BORDER)}`, borderRadius: 16,
              padding: P ? '22px 30px' : '30px 30px', minHeight: P ? undefined : 300, boxSizing: 'border-box', opacity: a, transform: `translateY(${(1 - a) * 16}px)`, display: 'flex', flexDirection: P ? 'row' : 'column', alignItems: P ? 'baseline' : 'flex-start', gap: P ? 24 : 12 }}>
              <span style={{ fontFamily: SERIF, fontSize: P ? 64 : 62, color: P ? CLAUDE.CARD : CLAUDE.INK, lineHeight: 1.05 }}>{tl.name}</span>
              <span style={{ fontFamily: SANS, fontSize: P ? 44 : 40, color: P ? CLAUDE.PILL : CLAUDE.INK_SOFT }}>{tl.what}</span>
            </div>
          );
        })}
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// HfConnect — Claude app ↔ MCP connector; Claude Code ↔ CLI + skills
// ===========================================================================
export const hfConnectSchema = z.object({
  title: z.string().default('How they connect'),
  appLabel: z.string().default('Claude app'),
  url: z.string().default('mcp.higgsfield.ai/mcp'),
  connectorLabel: z.string().default('official MCP connector'),
  appPills: z.array(z.string()).default(['sign in', 'no API key']),
  codeLabel: z.string().default('Claude Code'),
  codeLines: z.array(z.string()).default(['$ npx skills add higgsfield-ai/skills', '$ higgsfield auth login']),
  codePills: z.array(z.string()).default(['CLI', 'skills pack']),
  sparkLine: z.string().default('Plugged in, two ways.'),
  durationSeconds: z.number().optional(),
});
export const hfConnectMeta = durMeta(5);
export const HfConnect: React.FC<z.infer<typeof hfConnectSchema>> = ({ title, appLabel, url, connectorLabel, appPills, codeLabel, codeLines, codePills, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const lane = (i: number) => {
    const a = ease(ramp(t, 0.04 + i * 0.4, 0.14 + i * 0.4));
    const mid = ease(ramp(t, 0.12 + i * 0.4, 0.24 + i * 0.4));
    const end = ease(ramp(t, 0.22 + i * 0.4, 0.32 + i * 0.4));
    return { a, mid, end };
  };
  const L0 = lane(0), L1 = lane(1);
  const logo = P ? 120 : 150;
  if (P) {
    const laneH = 480;
    const ys = [290, 290 + laneH + 40];
    const render = (k: 0 | 1) => {
      const L = k === 0 ? L0 : L1; const y = ys[k];
      return (
        <React.Fragment key={k}>
          <div style={{ position: 'absolute', left: S.x, top: y, display: 'flex', alignItems: 'center', gap: 24, opacity: L.a }}>
            <Logo src={LOGO.claude} size={logo} />
            <span style={{ fontFamily: SERIF, fontSize: 70, color: CLAUDE.INK }}>{k === 0 ? appLabel : codeLabel}</span>
          </div>
          <Logo src={LOGO.higgsfield} size={logo} a={L.end} style={{ position: 'absolute', left: S.r - logo, top: y, borderRadius: logo * 0.22 }} />
          <Arrow st={st} x1={S.x + 560} y1={y + logo / 2} x2={S.r - logo - 20} y2={y + logo / 2} a={L.end} />
          {k === 0 ? (
            <Card style={{ border: `3px solid ${ACC_TEXT}`, left: S.x, top: y + logo + 30, width: S.w, height: laneH - logo - 40, padding: '28px 34px', opacity: L.mid }}>
              <div style={{ fontFamily: SANS, fontSize: 40, color: CLAUDE.INK_SOFT }}>{connectorLabel}</div>
              <div style={{ fontFamily: MONO, fontSize: 56, color: CLAUDE.INK, marginTop: 14 }}>{url}</div>
              <div style={{ display: 'flex', gap: 18, marginTop: 30 }}>{appPills.map((p) => <Pill key={p} text={p} size={44} />)}</div>
            </Card>
          ) : (
            <div style={{ position: 'absolute', left: S.x, top: y + logo + 30, width: S.w, height: laneH - logo - 40, boxSizing: 'border-box', borderRadius: 16, background: CLAUDE.INK, padding: '28px 34px', opacity: L.mid }}>
              {codeLines.map((c) => <div key={c} style={{ fontFamily: MONO, fontSize: 37, color: CLAUDE.PAGE, lineHeight: 1.45, whiteSpace: 'nowrap' }}>{c}</div>)}
              <div style={{ display: 'flex', gap: 18, marginTop: 24 }}>{codePills.map((p) => <Pill key={p} text={p} size={44} fill={CLAUDE.PAGE} color={CLAUDE.INK} />)}</div>
            </div>
          )}
        </React.Fragment>
      );
    };
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
        <Title st={st} text={title} />
        {render(0)}{render(1)}
        <Spark st={st} text={sparkLine} />
        <Bug st={st} />
      </AbsoluteFill>
    );
  }
  // 16:9 — two horizontal lanes: [logo + label] → card → Higgsfield
  const ys = [200, 600];
  const laneH = 340;
  const cardX = S.x + 420, cardW = S.w - 420 - 270;
  const render = (k: 0 | 1) => {
    const L = k === 0 ? L0 : L1; const y = ys[k];
    const cy = y + laneH / 2;
    return (
      <React.Fragment key={k}>
        <div style={{ position: 'absolute', left: S.x - 20, top: cy - logo / 2 - 40, width: 380, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 14, opacity: L.a }}>
          <Logo src={LOGO.claude} size={logo} />
          <span style={{ fontFamily: SERIF, fontSize: 58, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>{k === 0 ? appLabel : codeLabel}</span>
        </div>
        <Arrow st={st} x1={S.x + 362} y1={cy} x2={cardX - 16} y2={cy} a={L.mid} />
        {k === 0 ? (
          <Card style={{ border: `3px solid ${ACC_TEXT}`, left: cardX, top: y, width: cardW, height: laneH, padding: '34px 40px', opacity: L.mid }}>
            <div style={{ fontFamily: SANS, fontSize: 40, color: CLAUDE.INK_SOFT }}>{connectorLabel}</div>
            <div style={{ fontFamily: MONO, fontSize: 60, color: CLAUDE.INK, marginTop: 16 }}>{url}</div>
            <div style={{ display: 'flex', gap: 20, marginTop: 40 }}>{appPills.map((p) => <Pill key={p} text={p} size={46} />)}</div>
          </Card>
        ) : (
          <div style={{ position: 'absolute', left: cardX, top: y, width: cardW, height: laneH, boxSizing: 'border-box', borderRadius: 16, background: CLAUDE.INK, padding: '34px 40px', opacity: L.mid }}>
            {codeLines.map((c) => <div key={c} style={{ fontFamily: MONO, fontSize: 40, color: CLAUDE.PAGE, lineHeight: 1.5, whiteSpace: 'nowrap' }}>{c}</div>)}
            <div style={{ display: 'flex', gap: 20, marginTop: 30 }}>{codePills.map((p) => <Pill key={p} text={p} size={46} fill={CLAUDE.PAGE} color={CLAUDE.INK} />)}</div>
          </div>
        )}
        <Arrow st={st} x1={cardX + cardW + 16} y1={cy} x2={S.r - logo - 30} y2={cy} a={L.end} />
        <Logo src={LOGO.higgsfield} size={logo} a={L.end} style={{ position: 'absolute', left: S.r - logo - 10, top: cy - logo / 2, borderRadius: logo * 0.22 }} />
      </React.Fragment>
    );
  };
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {render(0)}{render(1)}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// HfRoles — Claude is the director, Higgsfield is the camera crew
// ===========================================================================
export const hfRolesSchema = z.object({
  title: z.string().default('Who does what'),
  director: z.string().default('director'),
  directorJobs: z.array(z.string()).default(['writes the script', 'breaks it into shots', "writes each shot's prompt", 'keeps characters + style consistent']),
  crew: z.string().default('camera crew'),
  crewJobs: z.array(z.string()).default(['generates each image', 'generates each clip']),
  handoff: z.string().default('shot prompts'),
  sparkLine: z.string().default('Director and crew.'),
  durationSeconds: z.number().optional(),
});
export const hfRolesMeta = durMeta(5);
export const HfRoles: React.FC<z.infer<typeof hfRolesSchema>> = ({ title, director, directorJobs, crew, crewJobs, handoff, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const aL = ease(ramp(t, 0.03, 0.1));
  const aR = ease(ramp(t, 0.5, 0.58));
  const gapX = 150;
  const cw = P ? S.w : (S.w - gapX) * 0.56, cw2 = P ? S.w : (S.w - gapX) - cw;
  const y = P ? 290 : 200;
  const h1 = P ? 560 : 720, h2 = P ? 370 : 720;
  const x2 = P ? S.x : S.x + cw + gapX, y2 = P ? y + h1 + 70 : y;
  const logo = P ? 100 : 110;
  const item = (txt: string, a: number, key: string) => P ? (
    <div key={key} style={{ opacity: a, transform: `translateX(${(1 - a) * 18}px)` }}><Pill text={txt} size={44} /></div>
  ) : (
    <div key={key} style={{ display: 'flex', alignItems: 'baseline', gap: 18, opacity: a, transform: `translateX(${(1 - a) * 18}px)` }}>
      <span style={{ fontFamily: SANS, fontSize: P ? 50 : 50, color: CLAUDE.INK }}>✓</span>
      <span style={{ fontFamily: SERIF, fontSize: P ? 56 : 54, color: CLAUDE.INK, lineHeight: 1.12 }}>{txt}</span>
    </div>
  );
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: S.x, top: y, width: cw, height: h1, padding: P ? '30px 36px' : '40px 44px', opacity: aL }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 22, marginBottom: P ? 26 : 40 }}>
          <Logo src={LOGO.claude} size={logo} />
          <Pill text={director} size={P ? 52 : 50} accent />
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: P ? 20 : 34 }}>
          {directorJobs.map((j, i) => item(j, ease(ramp(t, 0.1 + i * 0.09, 0.17 + i * 0.09)), j))}
        </div>
      </Card>
      {P
        ? <Arrow st={st} x1={S.x + S.w / 2} y1={y + h1 + 8} x2={S.x + S.w / 2} y2={y2 - 8} a={aR} />
        : <Arrow st={st} x1={S.x + cw + 16} y1={y + h1 / 2} x2={x2 - 16} y2={y + h1 / 2} a={aR} />}
      {!P && <Label text={handoff} size={36} color={CLAUDE.INK_SOFT} style={{ left: S.x + cw + 6, top: y + h1 / 2 - 104, width: gapX - 12, textAlign: 'center', opacity: aR }} />}
      <Card style={{ left: x2, top: y2, width: cw2, height: h2, padding: P ? '30px 36px' : '40px 44px', opacity: aR }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 22, marginBottom: P ? 26 : 40 }}>
          <Logo src={LOGO.higgsfield} size={logo} style={{ borderRadius: logo * 0.22 }} />
          <Pill text={crew} size={P ? 52 : 50} />
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: P ? 20 : 34 }}>
          {crewJobs.map((j, i) => item(j, ease(ramp(t, 0.58 + i * 0.08, 0.65 + i * 0.08)), j))}
        </div>
        {!P && (
          <div style={{ position: 'relative', marginTop: 44, height: 170 }}>
            {[0, 1].map((k) => (
              <div key={k} style={{ position: 'absolute', left: k * ((cw2 - 88) / 2 + 20), top: 0, opacity: ease(ramp(t, 0.66 + k * 0.06, 0.72 + k * 0.06)) }}>
                <Shot w={(cw2 - 88 - 20) / 2} h={170} variant={k + 1} />
              </div>
            ))}
          </div>
        )}
      </Card>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// HfPipeline — Claude plans → Higgsfield shoots (≤ ~15 s) → Claude checks → stitched film
// ===========================================================================
export const hfPipelineSchema = z.object({
  title: z.string().default('How a film gets built'),
  cols: z.array(z.string()).default(['Claude plans', 'Higgsfield shoots', 'Claude checks']),
  shots: z.array(z.string()).default(['1 · robot wakes', '2 · city at night', '3 · the chase', '4 · home']),
  cap: z.string().default('short clip'),
  rejected: z.number().default(2),   // index of the shot that fails the check and is re-shot
  film: z.string().default('stitched film'),
  sparkLine: z.string().default('Short shots, stitched.'),
  durationSeconds: z.number().optional(),
});
export const hfPipelineMeta = durMeta(6);
export const HfPipeline: React.FC<z.infer<typeof hfPipelineSchema>> = ({ title, cols, shots, cap, rejected, film, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const n = shots.length;
  const top = P ? 300 : 196;
  const headH = P ? 70 : 64;
  const rowGap = P ? 18 : 14;
  const rowH = P ? 110 : 100;
  const gx = P ? 22 : 40;
  const w0 = P ? 360 : 640, w1 = P ? 250 : 560, w2 = S.w - w0 - w1 - 2 * gx;
  const x0 = S.x, x1 = x0 + w0 + gx, x2 = x1 + w1 + gx;
  const rowsY = top + headH + 16;
  // timing: plan rows 0.05–0.25; shoot each 0.25–0.55; check each 0.3–0.62; reshoot 0.62–0.7; stitch 0.7–0.8
  const planA = (i: number) => ease(ramp(t, 0.05 + i * 0.045, 0.1 + i * 0.045));
  const shootA = (i: number) => ease(ramp(t, 0.25 + i * 0.075, 0.31 + i * 0.075));
  const checkA = (i: number) => ease(ramp(t, 0.31 + i * 0.075, 0.35 + i * 0.075));
  const redo = ease(ramp(t, 0.6, 0.68));
  const fY = rowsY + n * (rowH + rowGap) + (P ? 40 : 16);
  const fH = P ? 110 : 86;
  const stitch = ease(ramp(t, 0.68, 0.78));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {[x0, x1, x2].map((x, k) => (
        <div key={k} style={{ position: 'absolute', left: x, top: top, width: [w0, w1, w2][k], display: 'flex', alignItems: 'center', gap: 12,
          opacity: ease(ramp(t, [0.03, 0.22, 0.3][k], [0.09, 0.28, 0.36][k])) }}>
          <Logo src={k === 1 ? LOGO.higgsfield : LOGO.claude} size={P ? 52 : 54} style={{ borderRadius: k === 1 ? 12 : 0, flexShrink: 0 }} />
          <span style={{ fontFamily: SANS, fontSize: P ? 38 : 40, color: CLAUDE.INK, whiteSpace: P ? 'normal' : 'nowrap', lineHeight: 1.05 }}>{P && k === 1 ? `${cols[k]} ${cap}s` : cols[k]}</span>
        </div>
      ))}
      {shots.map((s, i) => {
        const y = rowsY + i * (rowH + rowGap);
        const bad = i === rejected;
        const sa = shootA(i), ca = checkA(i);
        return (
          <React.Fragment key={s}>
            <Card style={{ left: x0, top: y, width: w0, height: rowH, opacity: planA(i), display: 'flex', alignItems: 'center', padding: P ? '0 22px' : '0 30px', ...(P ? { background: CLAUDE.INK, border: `3px solid ${CLAUDE.INK}` } : {}) }}>
              <span style={{ fontFamily: P ? SANS : SERIF, fontSize: P ? 40 : 56, color: P ? CLAUDE.CARD : CLAUDE.INK, whiteSpace: 'nowrap' }}>{s}</span>
            </Card>
            <div style={{ position: 'absolute', left: x1, top: y, width: w1, height: rowH, opacity: sa, transform: `translateX(${(1 - sa) * -20}px)` }}>
              <Shot w={P ? w1 : 200} h={rowH} variant={i + (bad && redo > 0.5 ? 3 : 0)} />
              {!P && <div style={{ position: 'absolute', left: 216, top: rowH / 2 - 26 }}><Pill text={cap} size={42} fill={CLAUDE.INK_SOFT} /></div>}
            </div>
            <div style={{ position: 'absolute', left: x2, top: y, height: rowH, display: 'flex', alignItems: 'center', gap: 14, opacity: ca }}>
              {bad ? (
                redo < 0.5
                  ? <Pill text="✗ reject" size={P ? 42 : 44} accent />
                  : <Pill text="✓ re-shot" size={P ? 42 : 44} a={0.4 + 0.6 * redo} />
              ) : <Pill text="✓ keep" size={P ? 42 : 44} />}
            </div>
          </React.Fragment>
        );
      })}
      {/* the stitched film: one timeline bar of n segments */}
      <div style={{ position: 'absolute', left: S.x, top: fY, width: S.w, height: fH, display: 'flex', gap: 6, opacity: stitch }}>
        {shots.map((s, i) => (
          <div key={s} style={{ flex: 1, background: i === rejected ? CLAUDE.SPARK : CLAUDE.INK, borderRadius: 10,
            transform: `translateY(${(1 - stitch) * (i % 2 ? 24 : -24)}px)` }} />
        ))}
      </div>
      {P ? <div style={{ position: 'absolute', left: S.x, top: fY + fH + 14, opacity: stitch }}><Pill text={film} size={44} /></div>
        : <Label text={film} size={42} style={{ left: S.x, top: fY + fH + 14, opacity: stitch }} />}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// HfVoyager — redrawn from Higgsfield's demo: one prompt → archive + labelled AI shots
// ===========================================================================
export const hfVoyagerSchema = z.object({
  title: z.string().default('A Voyager short'),
  caption: z.string().default("Redrawn from Higgsfield's demo"),
  prompt: z.string().default('one prompt → 8 beats'),
  sources: z.array(z.enum(['archive', 'ai'])).default(['archive', 'archive', 'ai', 'archive', 'ai', 'archive', 'archive', 'ai']),
  archiveLabel: z.string().default('NASA/JPL footage'),
  aiLabel: z.string().default('labelled AI shot'),
  note: z.string().default('NASA/JPL footage is public domain · 8 beats as described, order simplified'),
  sparkLine: z.string().default('Every AI shot labelled.'),
  durationSeconds: z.number().optional(),
});
export const hfVoyagerMeta = durMeta(5);
export const HfVoyager: React.FC<z.infer<typeof hfVoyagerSchema>> = ({ title, caption, prompt, sources, archiveLabel, aiLabel, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const pIn = ease(ramp(t, 0.04, 0.12));
  const n = sources.length;
  const cols = P ? 2 : Math.ceil(n / 2);
  const gap = P ? 26 : 26;
  const cw = (S.w - gap * (cols - 1)) / cols;
  const chH = P ? 54 : 54;
  const ch = P ? 122 : 178;
  const pY = P ? 336 : 196;
  const gY = pY + (P ? 120 : 130);
  const rowStep = ch + chH + (P ? 30 : 30);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Label text={caption} size={P ? 40 : 38} color={CLAUDE.INK_SOFT}
        style={P ? { left: S.x, top: S.y + 170, opacity: pIn } : { right: 1920 - S.r, top: S.y + 50, textAlign: 'right', opacity: pIn }} />
      <div style={{ position: 'absolute', left: S.x, top: pY, display: 'flex', alignItems: 'center', gap: 24, opacity: pIn }}>
        <Logo src={LOGO.claude} size={P ? 80 : 80} />
        <span style={{ fontFamily: SANS, fontSize: P ? 50 : 48, color: CLAUDE.INK }}>+</span>
        <Logo src={LOGO.higgsfield} size={P ? 80 : 80} style={{ borderRadius: 18 }} />
        <Pill text={prompt} size={P ? 48 : 46} style={{ marginLeft: 12 }} />
      </div>
      {sources.map((s, i) => {
        const a = ease(ramp(t, 0.14 + i * 0.05, 0.2 + i * 0.05));
        const la = ease(ramp(t, 0.18 + i * 0.05, 0.24 + i * 0.05));
        const c = i % cols, r = Math.floor(i / cols);
        const x = S.x + c * (cw + gap), y = gY + r * rowStep;
        const ai = s === 'ai';
        return (
          <div key={i} style={{ position: 'absolute', left: x, top: y, width: cw, opacity: a }}>
            <Shot w={cw} h={ch} variant={i} dark probe={ai || i === 0} />
            <div style={{ position: 'absolute', left: 0, top: ch + 12, opacity: la }}>
              <Pill text={ai ? aiLabel : archiveLabel} size={P ? 36 : 36} accent={ai} fill={ai ? undefined : CLAUDE.INK_SOFT} />
            </div>
          </div>
        );
      })}
      {!P && <Label text={note} size={32} color={CLAUDE.INK_SOFT}
        style={{ left: S.x, top: gY + Math.ceil(n / cols) * rowStep - 10, opacity: ease(ramp(t, 0.6, 0.7)) }} />}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// HfLimits — paid credits · drift between shots · labelling is your job
// ===========================================================================
export const hfLimitsSchema = z.object({
  title: z.string().default('The catch'),
  credits: z.string().default('Credits'),
  creditsLine: z.string().default('generations use paid credits'),
  freeLine: z.string().default('free plan: no credits included'),
  drift: z.string().default('Drift'),
  driftLine: z.string().default('characters + style can shift between shots'),
  labels: z.string().default('Labels'),
  labelsLine: z.string().default('disclosing AI footage is on you'),
  sparkLine: z.string().default('Costs, drift, labels.'),
  durationSeconds: z.number().optional(),
});
export const hfLimitsMeta = durMeta(5);
export const HfLimits: React.FC<z.infer<typeof hfLimitsSchema>> = ({ title, credits, creditsLine, freeLine, drift, driftLine, labels, labelsLine, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const y = P ? 280 : 200;
  const gap = P ? 26 : 36;
  const cw = P ? S.w : (S.w - 2 * gap) / 3;
  const chh = P ? 330 : 720;
  const pos = (i: number) => (P ? { left: S.x, top: y + i * (chh + gap) } : { left: S.x + i * (cw + gap), top: y });
  const A = (i: number) => ease(ramp(t, 0.04 + i * 0.25, 0.12 + i * 0.25));
  // credits meter drains in steps as generations tick
  const steps = 5;
  const used = Math.min(steps, Math.floor(ramp(t, 0.1, 0.32) * steps + 0.0001));
  const vis = P ? 120 : 260; // visual area height
  const head = (txt: string, i: number) => <div style={{ alignSelf: 'flex-start', flexShrink: 0 }}><Pill text={txt} size={P ? 46 : 50} accent={i === 0} /></div>;
  const line = (txt: string) => P
    ? <div style={{ flexShrink: 0, alignSelf: 'flex-start', background: CLAUDE.INK, borderRadius: 12, padding: '6px 16px', fontFamily: SANS, fontSize: 38, color: CLAUDE.CARD, lineHeight: 1.2 }}>{txt}</div>
    : <div style={{ fontFamily: SERIF, fontSize: 50, color: CLAUDE.INK, lineHeight: 1.15, flexShrink: 0 }}>{txt}</div>;
  const body = { padding: P ? '24px 30px' : '34px 34px', display: 'flex', flexDirection: 'column' as const, gap: P ? 14 : 26 };
  const driftA = ease(ramp(t, 0.42, 0.52));
  const stamp = ease(ramp(t, 0.66, 0.72));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {/* 1 · credits */}
      <Card style={{ ...pos(0), width: cw, height: chh, opacity: A(0), ...body }}>
        {head(credits, 0)}
        <div style={{ display: 'flex', gap: 10, height: P ? 60 : 90, flexShrink: 0, marginTop: P ? 0 : 20 }}>
          {Array.from({ length: steps }, (_, i) => (
            <div key={i} style={{ flex: 1, borderRadius: 10, background: i < steps - used ? CLAUDE.INK : CLAUDE.PILL }} />
          ))}
        </div>
        {line(creditsLine)}
        <div style={{ fontFamily: SANS, fontSize: P ? 40 : 38, color: CLAUDE.INK_SOFT, marginTop: P ? 0 : 'auto' }}>{freeLine}</div>
      </Card>
      {/* 2 · drift */}
      <Card style={{ ...pos(1), width: cw, height: chh, opacity: A(1), ...body }}>
        {head(drift, 1)}
        <div style={{ display: 'flex', gap: 20, height: vis + (P ? 40 : 46), flexShrink: 0, alignItems: 'flex-end', justifyContent: P ? 'flex-start' : 'center' }}>
          {[0, 1].map((k) => (
            <div key={k} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6 }}>
              <div style={{ width: P ? 130 : 200, height: P ? 90 : 200, background: CLAUDE.FOOTER, borderRadius: 12, display: 'flex', alignItems: 'flex-end', justifyContent: 'center' }}>
                <Mascot size={P ? 70 : 140} color={k === 0 ? CLAUDE.INK_SOFT : (driftA > 0.5 ? CLAUDE.GHOST : CLAUDE.INK_SOFT)}
                  scarf={k === 0 ? CLAUDE.INK : (driftA > 0.5 ? CLAUDE.BORDER : CLAUDE.INK)} tall={k === 0 ? 1 : 1 - 0.25 * driftA} />
              </div>
              <span style={{ fontFamily: SANS, fontSize: P ? 34 : 34, color: CLAUDE.INK_SOFT }}>{k === 0 ? 'shot 1' : 'shot 4'}</span>
            </div>
          ))}
        </div>
        {line(driftLine)}
      </Card>
      {/* 3 · labels */}
      <Card style={{ ...pos(2), width: cw, height: chh, opacity: A(2), ...body }}>
        {head(labels, 2)}
        <div style={{ position: 'relative', height: vis, width: P ? 300 : '100%', flexShrink: 0 }}>
          <Shot w={P ? 300 : cw - 68} h={vis} variant={2} dark probe />
          <div style={{ position: 'absolute', left: 14, top: 14, opacity: stamp, transform: `scale(${1.3 - 0.3 * stamp})`, transformOrigin: 'left top' }}>
            <Pill text="AI-generated" size={P ? 34 : 38} fill={CLAUDE.PAGE} color={CLAUDE.INK} />
          </div>
        </div>
        {line(labelsLine)}
      </Card>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// HfDirect — from operating the camera to directing: plan · judge · reject
// ===========================================================================
export const hfDirectSchema = z.object({
  title: z.string().default('The skill that matters'),
  from: z.string().default('operating the camera'),
  to: z.string().default('directing'),
  steps: z.array(z.string()).default(['write the plan', 'judge each shot', 'know when to reject it']),
  sparkLine: z.string().default("Direct, don't operate."),
  durationSeconds: z.number().optional(),
});
export const hfDirectMeta = durMeta(5);
export const HfDirect: React.FC<z.infer<typeof hfDirectSchema>> = ({ title, from, to, steps, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const fIn = ease(ramp(t, 0.03, 0.1));
  const strike = ease(ramp(t, 0.16, 0.26));
  const toIn = ease(ramp(t, 0.24, 0.34));
  const y = P ? 300 : 200;
  const toY = P ? y + 120 : y;
  const sY = P ? toY + 190 : y + 200;
  const shotsY = P ? sY : y + 200;
  const nS = 4;
  const sGap = P ? 20 : 26;
  const sw = P ? (S.w - sGap) / 2 : (S.w - sGap * (nS - 1)) / nS;
  const sh = P ? 175 : 250;
  const stepY = P ? shotsY + 2 * sh + sGap + 50 : shotsY + sh + 70;
  const rej = 2;
  const judge = (i: number) => (t >= 0.42 + i * 0.05 ? 1 : 0);
  const redo = ease(ramp(t, 0.66, 0.74));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top: y, display: 'flex', alignItems: 'center', gap: 30, opacity: fIn }}>
        <span style={{ position: 'relative', display: 'inline-block' }}>
          <Pill text={from} size={P ? 50 : 52} fill={CLAUDE.INK} style={{ position: 'relative', zIndex: 0 }} />
          <span style={{ position: 'absolute', left: 14, right: 14, top: '50%', height: 7, marginTop: -3, background: CLAUDE.PAGE, transform: `scaleX(${strike})`, transformOrigin: 'left', zIndex: 1 }} />
        </span>
      </div>
      <div style={{ position: 'absolute', left: P ? S.x : S.x + 760, top: toY - (P ? 0 : 26), opacity: toIn, transform: `translateY(${(1 - toIn) * 14}px)`,
        fontFamily: SERIF, fontSize: P ? 130 : 120, color: ACC_TEXT, lineHeight: 1 }}>{to}</div>
      {Array.from({ length: nS }, (_, i) => {
        const c = P ? i % 2 : i, r = P ? Math.floor(i / 2) : 0;
        const x = S.x + c * (sw + sGap), yy = shotsY + r * (sh + sGap);
        const a = ease(ramp(t, 0.3 + i * 0.04, 0.36 + i * 0.04));
        const bad = i === rej;
        const ja = judge(i);
        return (
          <div key={i} style={{ position: 'absolute', left: x, top: yy, width: sw, height: sh, opacity: a }}>
            <Shot w={sw} h={sh} variant={bad && redo > 0.5 ? 5 : i} dark probe={!(bad && redo < 0.5)} />
            <div style={{ position: 'absolute', left: 14, top: 14, opacity: ja }}>
              {bad
                ? (redo < 0.5 ? <Pill text="✗ reject" size={P ? 40 : 40} accent /> : <Pill text="✓ take 2" size={P ? 40 : 40} fill={CLAUDE.PAGE} color={CLAUDE.INK} />)
                : <Pill text="✓" size={P ? 40 : 40} fill={CLAUDE.PAGE} color={CLAUDE.INK} />}
            </div>
          </div>
        );
      })}
      <div style={{ position: 'absolute', left: S.x, top: stepY, width: S.w, display: 'flex', flexDirection: P ? 'column' : 'row', gap: P ? 18 : 26 }}>
        {steps.map((s, i) => {
          const a = ease(ramp(t, 0.4 + i * 0.12, 0.48 + i * 0.12));
          return (
            P ? <div key={s} style={{ opacity: a }}><Pill text={`${i + 1} · ${s}`} size={46} /></div> : (
            <div key={s} style={{ display: 'flex', alignItems: 'baseline', gap: 14, opacity: a }}>
              <span style={{ fontFamily: SERIF, fontSize: 52, color: ACC_TEXT }}>{i + 1}</span>
              <span style={{ fontFamily: SERIF, fontSize: 52, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>{s}</span>
            </div>)
          );
        })}
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
