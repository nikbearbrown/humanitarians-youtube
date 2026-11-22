import React from 'react';
import { AbsoluteFill, Img, useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { CC, CC_FONT } from '../tokens/claudecode';
import { pickProfessorBear } from '../lib/professorBear';
import { staticFile } from 'remotion';

/**
 * Background AI Agents — concept beats for "Background AI Agents: How AI Works While You Don't"
 * (claude-liam). Every component lays itself out for 16:9 (1920x1080) or 9:16 (1080x1920) from
 * useVideoConfig, so the same component backs the landscape id and its *916 id.
 *
 *   AgentChatVsLoop      chatbot (you are the loop) vs agent (it runs its own loop) + the two analogies
 *   AgentLoopCycle       Goal → Plan → Act → Observe → repeat; model = brain, tools = hands
 *   AgentRunLog          a worked run as a Claude Code style log, each block tagged with its loop step
 *   AgentBackgroundLanes cloud lanes running in parallel while the laptop is closed; done notification
 *   AgentChecklist       risk checklist (tone 'risk') or practice checklist (tone 'practice')
 *   AgentFitSort         task chips sort into "hand it off" vs "keep it yourself"
 *
 * Reveals are driven by `cues` (seconds from the start of the beat), authored from the narration.
 * A person is never an icon (PROFESSOR BEAR LAW): "you" is a Professor Bear portrait, circle-cropped.
 */

// Channel branding (default: the @NikBearBrown claude-liam reel). A reel on another channel passes its
// handle, an optional corner wordmark (public/ path) and, if asked for, a generic profile avatar for "you".
const brand = {
  handle: z.string().default('@NikBearBrown'),
  logo: z.string().optional(),
  avatar: z.enum(['bear', 'profile']).default('bear'),
};
const BrandCtx = React.createContext<{ handle: string; logo?: string; avatar: 'bear' | 'profile' }>({ handle: '@NikBearBrown', avatar: 'bear' });

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const MONO = CC_FONT.mono;

function useClock() {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const portrait = height > width;
  const reveal = (at: number | undefined, soft = false) =>
    at === undefined ? 1 : spring({ frame: frame - Math.round(at * fps), fps,
      config: soft ? { damping: 30, stiffness: 80, mass: 1 } : { damping: 22, stiffness: 140, mass: 0.7 } });
  return { frame, fps, width, height, portrait, t: frame / fps, reveal };
}

const Bug: React.FC<{ width: number; height: number }> = ({ width, height }) => {
  const { handle, logo } = React.useContext(BrandCtx);
  if (logo) {
    return <Img src={staticFile(logo)} style={{ position: 'absolute', right: width * 0.05, bottom: height * 0.05,
      height: 34, opacity: 0.45 }} />;
  }
  return (
    <div style={{ position: 'absolute', right: width * 0.05, bottom: height * 0.05, fontFamily: SANS,
      fontSize: 26, fontWeight: 600, color: CLAUDE.INK_SOFT, opacity: 0.35, letterSpacing: 1 }}>{handle}</div>
  );
};

const Spark: React.FC<{ text: string; at?: number; top?: boolean }> = ({ text, at, top }) => {
  const { reveal, width, height } = useClock();
  const o = Math.min(1, reveal(at));
  return (
    <div style={{ position: 'absolute', left: width * 0.05, right: width * 0.05,
      ...(top ? { top: height * 0.06 } : { bottom: height * 0.11 }),
      display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 14, opacity: o }}>
      <span style={{ color: CLAUDE.SPARK, fontSize: 40, lineHeight: 1 }}>✻</span>
      <span style={{ fontFamily: SERIF, fontSize: 44, color: CLAUDE.INK }}>{text}</span>
    </div>
  );
};

const ProfileAvatar: React.FC<{ size: number }> = ({ size }) => (
  <svg width={size} height={size} viewBox="0 0 100 100" style={{ borderRadius: '50%', boxShadow: '0 6px 18px rgba(61,57,41,0.18)' }}>
    <circle cx="50" cy="50" r="50" fill={CLAUDE.PILL} />
    <circle cx="50" cy="39" r="17" fill={CLAUDE.INK_SOFT} />
    <path d="M18 86 C22 66, 36 59, 50 59 C64 59, 78 66, 82 86 Z" fill={CLAUDE.INK_SOFT} />
    <circle cx="50" cy="50" r="48" fill="none" stroke={CLAUDE.CARD} strokeWidth="4" />
  </svg>
);

const You: React.FC<{ size: number; seed: string; ring?: number }> = ({ size, seed, ring = 0 }) => {
  const { avatar } = React.useContext(BrandCtx);
  return (
  <div style={{ position: 'relative', width: size, height: size }}>
    {avatar === 'profile' ? <ProfileAvatar size={size} /> : (
    <Img src={pickProfessorBear('1x1', seed)} style={{ width: size, height: size, borderRadius: '50%',
      objectFit: 'cover', border: `4px solid ${CLAUDE.CARD}`, boxShadow: '0 6px 18px rgba(61,57,41,0.18)' }} />)}
    {ring > 0 && (
      <div style={{ position: 'absolute', inset: -14, borderRadius: '50%', border: `6px solid ${CLAUDE.SPARK}`,
        opacity: ring, transform: `scale(${0.9 + 0.1 * ring})` }} />
    )}
  </div>
  );
};

const Card: React.FC<{ style?: React.CSSProperties; children: React.ReactNode }> = ({ style, children }) => (
  <div style={{ background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 22,
    boxShadow: '0 8px 24px rgba(61,57,41,0.08)', ...style }}>{children}</div>
);

const Title: React.FC<{ text: string; at?: number }> = ({ text, at }) => {
  const { reveal, width, height, portrait } = useClock();
  const o = Math.min(1, reveal(at));
  return (
    <div style={{ position: 'absolute', left: width * 0.06, right: width * 0.06, top: height * (portrait ? 0.07 : 0.075),
      fontFamily: SERIF, fontSize: portrait ? 76 : 64, color: CLAUDE.INK, opacity: o, lineHeight: 1.1,
      textAlign: portrait ? 'center' : 'left' }}>{text}</div>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// 1. AgentChatVsLoop
// cues: [chatbot, youAreTheLoop, agent, itsOwnLoop, calculator, intern]

export const agentChatVsLoopSchema = z.object({
  title: z.string().default('Chatbot vs Agent'),
  sparkLine: z.string().default('You drive, or it drives.'),
  cues: z.array(z.number()).default([0.5, 3, 5.5, 8, 13, 16]),
  durationSeconds: z.number().optional(),
  ...brand,
});

const LoopRing: React.FC<{ size: number; spin: number; active: number; labels: string[]; accent?: boolean; fontSize?: number }> =
  ({ size, spin, active, labels, accent = true, fontSize = 28 }) => {
  const r = size * 0.36;
  const c = size / 2;
  const pts = labels.map((_, i) => {
    const a = (i / labels.length) * Math.PI * 2 - Math.PI / 2;
    return { x: c + Math.cos(a) * r, y: c + Math.sin(a) * r };
  });
  const dotA = spin * Math.PI * 2 - Math.PI / 2;
  return (
    <div style={{ position: 'relative', width: size, height: size }}>
      <svg width={size} height={size} style={{ position: 'absolute', inset: 0 }}>
        <circle cx={c} cy={c} r={r} fill="none" stroke={CLAUDE.BORDER} strokeWidth={6} />
        <circle cx={c} cy={c} r={r} fill="none" stroke={accent ? CLAUDE.SPARK : CLAUDE.INK_SOFT} strokeWidth={6}
          strokeDasharray={`${2 * Math.PI * r * active} ${2 * Math.PI * r}`} transform={`rotate(-90 ${c} ${c})`} />
        {active > 0.05 && (
          <circle cx={c + Math.cos(dotA) * r} cy={c + Math.sin(dotA) * r} r={14} fill={accent ? CLAUDE.SPARK : CLAUDE.INK} />
        )}
      </svg>
      {labels.map((l, i) => (
        <div key={l} style={{ position: 'absolute', left: pts[i].x, top: pts[i].y, transform: 'translate(-50%,-50%)',
          background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 14, padding: '8px 16px',
          fontFamily: SANS, fontSize, fontWeight: 600, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>{l}</div>
      ))}
    </div>
  );
};

const AgentChatVsLoopInner: React.FC<z.infer<typeof agentChatVsLoopSchema>> = ({ title, sparkLine, cues }) => {
  const { width, height, portrait, t, reveal } = useClock();
  const [cChat, cYou, cAgent, cOwn, cCalc, cIntern] = cues;
  const chatIn = Math.min(1, reveal(cChat));
  const youRing = Math.min(1, reveal(cYou));
  const agentIn = Math.min(1, reveal(cAgent));
  const ownLoop = interpolate(t, [cOwn, cOwn + 3], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const spin = t > cOwn ? ((t - cOwn) / 2.4) % 1 : 0;
  const calcIn = Math.min(1, reveal(cCalc));
  const internIn = Math.min(1, reveal(cIntern));
  // chat exchange: message goes up, answer comes back, then nothing (it waits)
  const msg = interpolate(t, [cChat + 0.6, cChat + 1.6], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const ans = interpolate(t, [cChat + 1.8, cChat + 2.8], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

  const panelW = portrait ? width * 0.88 : width * 0.42;
  const panelH = portrait ? height * 0.33 : height * 0.56;
  const left = portrait ? { left: width * 0.06, top: height * 0.17 } : { left: width * 0.06, top: height * 0.2 };
  const right = portrait ? { left: width * 0.06, top: height * 0.53 } : { left: width * 0.52, top: height * 0.2 };
  const head: React.CSSProperties = { fontFamily: SERIF, fontSize: 48, color: CLAUDE.INK };
  const sub: React.CSSProperties = { fontFamily: SANS, fontSize: 30, color: CLAUDE.INK_SOFT };
  const youSize = portrait ? 150 : 170;
  const ringSize = portrait ? 420 : 470;

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title text={title} at={0} />
      {/* chatbot panel */}
      <Card style={{ position: 'absolute', ...left, width: panelW, height: panelH, opacity: chatIn, padding: 30, boxSizing: 'border-box' }}>
        <div style={head}>Chatbot</div>
        <div style={{ ...sub, marginTop: 6 }}>responds once per message</div>
        <div style={{ position: 'absolute', left: 40, right: 40, top: portrait ? 150 : 190, bottom: portrait ? 90 : 120,
          display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 14 }}>
            <You size={youSize} seed="background-agents-B02" ring={youRing} />
            <div style={{ fontFamily: SANS, fontSize: 30, fontWeight: 600, color: CLAUDE.INK }}>You</div>
          </div>
          <div style={{ flex: 1, position: 'relative', height: 140, margin: '0 24px' }}>
            <div style={{ position: 'absolute', top: 18, left: `${msg * 70}%`, opacity: msg > 0 && msg < 1 ? 1 : msg >= 1 ? 0.35 : 0,
              background: CLAUDE.PILL, borderRadius: 14, padding: '8px 16px', fontFamily: SANS, fontSize: 26, color: CLAUDE.INK }}>question</div>
            <div style={{ position: 'absolute', bottom: 10, right: `${ans * 70}%`, opacity: ans > 0 && ans < 1 ? 1 : ans >= 1 ? 0.35 : 0,
              background: CLAUDE.FOOTER, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 14, padding: '8px 16px',
              fontFamily: SANS, fontSize: 26, color: CLAUDE.INK }}>answer</div>
          </div>
          <div style={{ width: youSize, height: youSize, borderRadius: 30, background: CLAUDE.FOOTER, border: `3px solid ${CLAUDE.BORDER}`,
            display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 70, color: CLAUDE.SPARK }}>✻</div>
        </div>
        <div style={{ position: 'absolute', left: 30, right: 30, bottom: 26, textAlign: 'center', fontFamily: SERIF,
          fontSize: 40, color: CLAUDE.INK, opacity: youRing }}>You are the loop.</div>
      </Card>
      {/* agent panel */}
      <Card style={{ position: 'absolute', ...right, width: panelW, height: panelH, opacity: agentIn, padding: 30, boxSizing: 'border-box' }}>
        <div style={head}>Agent</div>
        <div style={{ ...sub, marginTop: 6 }}>runs its own loop until the goal is met</div>
        <div style={{ position: 'absolute', left: 0, right: 0, top: portrait ? 110 : 150, display: 'flex', justifyContent: 'center',
          transform: `scale(${portrait ? 0.78 : 0.86})`, transformOrigin: 'top center' }}>
          <LoopRing size={ringSize} spin={spin} active={ownLoop} labels={['decide', 'use a tool', 'check', 'keep going']} />
        </div>
        <div style={{ position: 'absolute', left: 30, right: 30, bottom: 26, textAlign: 'center', fontFamily: SERIF,
          fontSize: 40, color: CLAUDE.INK, opacity: ownLoop > 0 ? 1 : 0 }}>It is the loop.</div>
      </Card>
      {/* analogies */}
      <div style={{ position: 'absolute', left: width * 0.06, right: width * 0.06, top: portrait ? height * 0.875 : height * 0.79,
        display: 'flex', flexDirection: 'row', justifyContent: portrait ? 'space-between' : 'space-around', gap: 20 }}>
        <div style={{ opacity: calcIn, fontFamily: SANS, fontSize: portrait ? 30 : 34, color: CLAUDE.INK }}>
          chatbot = <b>a calculator</b>
        </div>
        <div style={{ opacity: internIn, fontFamily: SANS, fontSize: portrait ? 30 : 34, color: CLAUDE.INK }}>
          agent = <b>an intern with a to-do list</b>
        </div>
      </div>
      {!portrait && <Spark text={sparkLine} at={cIntern + 2} />}
      <Bug width={width} height={height} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// 2. AgentLoopCycle
// cues: [goal, plan, act, observe, repeat, brainHands]

export const agentLoopCycleSchema = z.object({
  title: z.string().default('The Agent Loop'),
  steps: z.array(z.object({ label: z.string(), detail: z.string() })).default([
    { label: 'Goal', detail: '“Fix the failing tests in this repo”' },
    { label: 'Plan', detail: 'read the errors → find the file → edit → re-run' },
    { label: 'Act', detail: 'call tools: terminal · file editor · browser · APIs' },
    { label: 'Observe', detail: 'read the output and decide what’s next' },
  ]),
  repeatText: z.string().default('repeat until done, or stuck'),
  cues: z.array(z.number()).default([1, 4, 7, 10, 13, 16]),
  durationSeconds: z.number().optional(),
  ...brand,
});

const AgentLoopCycleInner: React.FC<z.infer<typeof agentLoopCycleSchema>> = ({ title, steps, repeatText, cues }) => {
  const { width, height, portrait, t, reveal } = useClock();
  const stepCues = cues.slice(0, steps.length);
  const cRepeat = cues[steps.length];
  const cBrain = cues[steps.length + 1];
  const active = stepCues.reduce((k, c, i) => (t >= c ? i : k), -1);
  const size = portrait ? 860 : 760;
  const cx = portrait ? width / 2 : width * 0.32;
  const cy = portrait ? height * 0.43 : height * 0.55;
  const r = size * 0.36;
  const pos = (i: number) => {
    const a = (i / steps.length) * Math.PI * 2 - Math.PI / 2;
    return { x: cx + Math.cos(a) * r, y: cy + Math.sin(a) * r, a };
  };
  // the dot travels the arc between the active step and the next one
  const arcStart = active < 0 ? 0 : active;
  const prog = active < 0 ? 0 : interpolate(t, [stepCues[active], stepCues[active] + 1.2], [0, 1],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const repeating = t >= cRepeat;
  const loopPhase = repeating ? ((t - cRepeat) / 2.2) % 1 : 0;
  const dotIndex = repeating ? loopPhase * steps.length : arcStart + (active >= 0 && active < steps.length - 1 ? 0 : 0) + prog * 0.0;
  const da = (dotIndex / steps.length) * Math.PI * 2 - Math.PI / 2;
  const brainIn = Math.min(1, reveal(cBrain));
  const detailBox = portrait
    ? { left: width * 0.07, right: width * 0.07, top: height * 0.71 }
    : { left: width * 0.6, right: width * 0.06, top: height * 0.24 };
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title text={title} at={0} />
      <svg width={width} height={height} style={{ position: 'absolute', inset: 0 }}>
        <circle cx={cx} cy={cy} r={r} fill="none" stroke={CLAUDE.BORDER} strokeWidth={8} />
        {steps.map((_, i) => {
          if (i > active && !repeating) return null;
          const a0 = pos(i).a + 0.32, a1 = pos(i + 1).a - 0.32;
          const p = i < active || repeating ? 1 : prog;
          const am = a0 + (a1 - a0) * p;
          const large = am - a0 > Math.PI ? 1 : 0;
          const d = `M ${cx + Math.cos(a0) * r} ${cy + Math.sin(a0) * r} A ${r} ${r} 0 ${large} 1 ${cx + Math.cos(am) * r} ${cy + Math.sin(am) * r}`;
          return <path key={i} d={d} fill="none" stroke={CLAUDE.INK_SOFT} strokeWidth={8} strokeLinecap="round" />;
        })}
        {repeating && <circle cx={cx + Math.cos(da) * r} cy={cy + Math.sin(da) * r} r={16} fill={CLAUDE.SPARK} />}
      </svg>
      {steps.map((s, i) => {
        const p = pos(i);
        const on = i === active && !repeating;
        const seen = i <= active || repeating;
        return (
          <div key={s.label} style={{ position: 'absolute', left: p.x, top: p.y, transform: `translate(-50%,-50%) scale(${on ? 1.08 : 1})`,
            background: CLAUDE.CARD, color: CLAUDE.INK,
            border: `${on ? 5 : 3}px solid ${on ? CLAUDE.INK : CLAUDE.BORDER}`, borderRadius: 20, padding: '14px 30px',
            fontFamily: SERIF, fontSize: 50, opacity: seen ? 1 : 0.45, boxShadow: '0 8px 22px rgba(61,57,41,0.10)' }}>
            {s.label}
            {on && <div style={{ position: 'absolute', left: -40, right: -40, bottom: -22, height: 8, borderRadius: 4, background: CLAUDE.SPARK }} />}
          </div>
        );
      })}
      {/* centre: the model is the brain */}
      <div style={{ position: 'absolute', left: cx, top: cy, transform: 'translate(-50%,-50%)', textAlign: 'center', opacity: brainIn }}>
                <div style={{ fontFamily: SANS, fontSize: 32, fontWeight: 600, color: CLAUDE.INK }}>the model</div>
        <div style={{ fontFamily: SANS, fontSize: 28, color: CLAUDE.INK_SOFT }}>is the brain</div>
      </div>
      {/* the detail for the step being spoken */}
      <Card style={{ position: 'absolute', ...detailBox, padding: portrait ? '28px 34px' : '34px 40px' }}>
        {steps.map((s, i) => {
          const seen = i <= active || repeating;
          const on = i === active && !repeating;
          return (
            <div key={s.label} style={{ display: 'flex', gap: 18, alignItems: 'baseline', marginBottom: 18, opacity: seen ? (on ? 1 : 0.6) : 0 }}>
              <div style={{ fontFamily: SANS, fontSize: 30, fontWeight: 700, color: CLAUDE.INK, minWidth: portrait ? 140 : 150,
                borderLeft: `8px solid ${on ? CLAUDE.SPARK : 'transparent'}`, paddingLeft: 12 }}>{s.label}</div>
              <div style={{ fontFamily: SANS, fontSize: 30, color: CLAUDE.INK, lineHeight: 1.25 }}>{s.detail}</div>
            </div>
          );
        })}
        <div style={{ fontFamily: SERIF, fontSize: 36, color: CLAUDE.INK, opacity: repeating ? 1 : 0, marginTop: 6 }}>↻ {repeatText}</div>
        <div style={{ fontFamily: SANS, fontSize: 30, color: CLAUDE.INK_SOFT, opacity: brainIn, marginTop: 14 }}>
          tools are the hands
        </div>
      </Card>
      <Bug width={width} height={height} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// 3. AgentRunLog — a worked run in the Claude Code palette, each block tagged with its loop step

export const agentRunLogSchema = z.object({
  title: z.string().default('demo-repo · one goal, one loop'),
  note: z.string().default('Session reconstructed for the film · test output from real runs'),
  blocks: z.array(z.object({
    step: z.string(),
    head: z.string(),
    lines: z.array(z.object({ text: z.string(), kind: z.enum(['out', 'fail', 'ok', 'add', 'del']).default('out') })).default([]),
    at: z.number(),
  })).default([]),
  durationSeconds: z.number().optional(),
  ...brand,
});

const AgentRunLogInner: React.FC<z.infer<typeof agentRunLogSchema>> = ({ title, note, blocks }) => {
  const { width, height, portrait, t, reveal } = useClock();
  const shown = blocks.filter((b) => t >= b.at);
  const current = shown.length - 1;
  const winW = portrait ? width * 0.86 : width * 0.86;
  const winX = (width - winW) / 2;
  const top = portrait ? height * 0.1 : height * 0.07;
  const winH = portrait ? height * 0.78 : height * 0.8;
  const fontSize = portrait ? 30 : 30;
  const colour = { out: CC.INK_2, fail: CC.DEL_FG, ok: CC.ADD_FG, add: CC.ADD_FG, del: CC.DEL_FG } as const;
  const bg = { out: 'transparent', fail: 'transparent', ok: 'transparent', add: CC.ADD_BG, del: CC.DEL_BG } as const;
  // keep the newest blocks in view: drop the oldest when the stack would overflow
  const budget = portrait ? 30 : 21;
  let rows = 0;
  const visible: typeof blocks = [];
  for (let i = shown.length - 1; i >= 0; i--) {
    const need = 1 + shown[i].lines.length + 0.6;
    if (rows + need > budget && visible.length) break;
    rows += need;
    visible.unshift(shown[i]);
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <div style={{ position: 'absolute', left: winX, top, width: winW, height: winH, background: CC.PAGE, borderRadius: 18,
        boxShadow: '0 18px 48px rgba(31,30,27,0.35)', overflow: 'hidden' }}>
        <div style={{ height: 64, background: CC.PANEL, display: 'flex', alignItems: 'center', gap: 12, padding: '0 24px',
          borderBottom: `2px solid ${CC.BORDER}` }}>
          {[CC.TL_RED, CC.TL_YEL, CC.TL_GRN].map((c) => <div key={c} style={{ width: 18, height: 18, borderRadius: 9, background: c }} />)}
          <div style={{ marginLeft: 18, fontFamily: CC_FONT.ui, fontSize: 26, color: CC.INK_2 }}>{title}</div>
        </div>
        <div style={{ padding: portrait ? '24px 26px' : '26px 34px' }}>
          {visible.map((b) => {
            const i = blocks.indexOf(b);
            const on = i === current;
            const o = Math.min(1, reveal(b.at));
            return (
              <div key={i} style={{ display: 'flex', gap: 22, marginBottom: 20, opacity: on ? o : 0.72 }}>
                <div style={{ minWidth: portrait ? 150 : 170, textAlign: 'right' }}>
                  <span style={{ fontFamily: CC_FONT.ui, fontSize: 24, fontWeight: 700, letterSpacing: 2,
                    color: on ? CC.PAGE : CC.INK_2, background: on ? CC.INK : 'transparent', border: `3px solid ${on ? CC.INK : CC.BORDER}`,
                    borderRadius: 10, padding: '4px 12px', position: 'relative', display: 'inline-block' }}>{b.step.toUpperCase()}
                    {on && <span style={{ position: 'absolute', left: -60, right: -60, bottom: -14, height: 6, borderRadius: 3, background: CC.SPARK }} />}</span>
                </div>
                <div style={{ flex: 1, minWidth: 0 }}>
                  <div style={{ fontFamily: MONO, fontSize, color: CC.INK, whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}>{b.head}</div>
                  {b.lines.map((l, k) => (
                    <div key={k} style={{ fontFamily: MONO, fontSize: fontSize - 2, color: colour[l.kind], background: bg[l.kind],
                      whiteSpace: 'pre-wrap', wordBreak: 'break-word', padding: '2px 8px', marginTop: 4, borderRadius: 4 }}>{l.text}</div>
                  ))}
                </div>
              </div>
            );
          })}
        </div>
      </div>
      <div style={{ position: 'absolute', left: winX, right: winX, top: top + winH + 18, fontFamily: SANS, fontSize: 24,
        color: CLAUDE.INK_SOFT, textAlign: portrait ? 'center' : 'left' }}>{note}</div>
      <Bug width={width} height={height} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// 4. AgentBackgroundLanes
// cues: [cloud, assignAndClose, notify, parallel]

export const agentBackgroundLanesSchema = z.object({
  title: z.string().default('What Makes It “Background”'),
  lanes: z.array(z.object({ label: z.string(), rate: z.number() })).default([
    { label: 'Code fix', rate: 0.22 },
    { label: 'Research report', rate: 0.12 },
    { label: 'Data cleanup', rate: 0.17 },
    { label: 'Game asset batch', rate: 0.09 },
  ]),
  notice: z.string().default('Code fix finished · ready for your review'),
  cues: z.array(z.number()).default([1, 5, 9, 13]),
  durationSeconds: z.number().optional(),
  ...brand,
});

const AgentBackgroundLanesInner: React.FC<z.infer<typeof agentBackgroundLanesSchema>> = ({ title, lanes, notice, cues }) => {
  const { width, height, portrait, t, reveal } = useClock();
  const [cCloud, cClose, cNotify, cParallel] = cues;
  const cloudIn = Math.min(1, reveal(cCloud));
  const lid = interpolate(t, [cClose, cClose + 1.2], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const notifyIn = Math.min(1, reveal(cNotify));
  // lane 0 starts when the task is assigned; the others start at the "parallel" cue
  const progress = (i: number) => {
    const start = i === 0 ? cClose : cParallel + i * 0.4;
    const p = Math.max(0, t - start) * lanes[i].rate;
    if (i === 0) return Math.min(1, Math.max(0, (t - cClose) / Math.max(0.1, cNotify - cClose)));
    return Math.min(0.92, p);
  };
  const left = portrait ? { left: width * 0.06, top: height * 0.17, width: width * 0.88, height: height * 0.22 }
    : { left: width * 0.06, top: height * 0.24, width: width * 0.28, height: height * 0.56 };
  const right = portrait ? { left: width * 0.06, top: height * 0.42, width: width * 0.88, height: height * 0.4 }
    : { left: width * 0.38, top: height * 0.24, width: width * 0.56, height: height * 0.56 };
  const chips = ['runs in the cloud', 'asynchronous', 'parallel'];
  const chipAt = [cCloud, cClose, cParallel];
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title text={title} at={0} />
      {/* you + the laptop */}
      <Card style={{ position: 'absolute', ...left, padding: 28, boxSizing: 'border-box', display: 'flex',
        flexDirection: portrait ? 'row' : 'column', alignItems: 'center', justifyContent: 'space-around' }}>
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 12 }}>
          <You size={portrait ? 150 : 170} seed="background-agents-B05" />
          <div style={{ fontFamily: SANS, fontSize: 30, fontWeight: 600, color: CLAUDE.INK }}>{t >= cClose + 1 ? 'You, away' : 'You'}</div>
        </div>
        {/* laptop: the lid folds down at the assign cue */}
        <div style={{ position: 'relative', width: 220, height: 170 }}>
          <div style={{ position: 'absolute', left: 20, right: 20, bottom: 40, height: 120 * (1 - 0.92 * lid),
            background: lid > 0.95 ? CLAUDE.INK_SOFT : CLAUDE.FOOTER, border: `5px solid ${CLAUDE.INK_SOFT}`, borderRadius: 10,
            display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 40, color: CLAUDE.SPARK }}>{lid < 0.5 ? '✻' : ''}</div>
          <div style={{ position: 'absolute', left: 0, right: 0, bottom: 22, height: 20, background: CLAUDE.INK_SOFT, borderRadius: 6 }} />
        </div>
      </Card>
      {/* the cloud: lanes run without you */}
      <Card style={{ position: 'absolute', ...right, padding: 34, boxSizing: 'border-box', opacity: cloudIn }}>
        <div style={{ fontFamily: SERIF, fontSize: 46, color: CLAUDE.INK, marginBottom: 22 }}>In the cloud</div>
        {lanes.map((l, i) => {
          const p = progress(i);
          const started = i === 0 ? t >= cClose : t >= cParallel + i * 0.4;
          const done = p >= 1;
          return (
            <div key={l.label} style={{ marginBottom: portrait ? 26 : 24, opacity: started ? 1 : 0.35 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontFamily: SANS, fontSize: 30, color: CLAUDE.INK, marginBottom: 8 }}>
                <span>{l.label}</span>
                <span style={{ color: done ? CLAUDE.INK : CLAUDE.INK_SOFT, fontWeight: done ? 700 : 400 }}>{done ? '✓ done' : started ? 'working…' : 'queued'}</span>
              </div>
              <div style={{ height: 18, background: CLAUDE.PILL, borderRadius: 9, overflow: 'hidden' }}>
                <div style={{ width: `${p * 100}%`, height: '100%', background: done ? CLAUDE.SPARK : CLAUDE.INK_SOFT, borderRadius: 9 }} />
              </div>
            </div>
          );
        })}
      </Card>
      {/* property chips */}
      <div style={{ position: 'absolute', left: width * 0.06, right: width * 0.06, top: portrait ? height * 0.845 : height * 0.84,
        display: 'flex', gap: 22, justifyContent: 'center', flexWrap: 'wrap' }}>
        {chips.map((c, i) => (
          <div key={c} style={{ opacity: Math.min(1, reveal(chipAt[i])), fontFamily: SANS, fontSize: 30, color: CLAUDE.INK,
            background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 999, padding: '10px 26px' }}>{c}</div>
        ))}
      </div>
      {/* notification */}
      <div style={{ position: 'absolute', right: width * 0.06, top: height * (portrait ? 0.115 : 0.07),
        transform: `translateY(${(1 - notifyIn) * -40}px)`, opacity: notifyIn, background: CLAUDE.CARD,
        border: `3px solid ${CLAUDE.INK_SOFT}`, borderBottom: `8px solid ${CLAUDE.SPARK}`, borderRadius: 18, padding: '16px 26px', boxShadow: '0 12px 30px rgba(61,57,41,0.18)',
        fontFamily: SANS, fontSize: 30, color: CLAUDE.INK, maxWidth: portrait ? width * 0.88 : width * 0.42 }}>
        ✓ {notice}
      </div>
      <Bug width={width} height={height} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// 5. AgentChecklist — tone 'risk' (warning marks) or 'practice' (ticks)

export const agentChecklistSchema = z.object({
  title: z.string().default('The Risks'),
  tone: z.enum(['risk', 'practice']).default('risk'),
  items: z.array(z.object({ label: z.string(), detail: z.string(), answers: z.string().optional(), mark: z.string().optional() })).default([]),
  cues: z.array(z.number()).default([]),
  durationSeconds: z.number().optional(),
  ...brand,
});

const AgentChecklistInner: React.FC<z.infer<typeof agentChecklistSchema>> = ({ title, tone, items, cues }) => {
  const { width, height, portrait, t, reveal } = useClock();
  const active = cues.reduce((k, c, i) => (t >= c ? i : k), -1);
  const top = portrait ? height * 0.2 : height * 0.22;
  const gap = portrait ? 34 : 22;
  const cardH = portrait ? (height * 0.66 - gap * (items.length - 1)) / items.length : (height * 0.62 - gap * (items.length - 1)) / items.length;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title text={title} at={0} />
      {items.map((it, i) => {
        const o = Math.min(1, reveal(cues[i]));
        const on = i === active;
        const mark = it.mark ?? (tone === 'risk' ? '!' : '✓');
        return (
          <div key={it.label} style={{ position: 'absolute', left: width * 0.06, right: width * 0.06, top: top + i * (cardH + gap),
            height: cardH, opacity: o, transform: `translateX(${(1 - o) * 40}px)` }}>
            <Card style={{ height: '100%', boxSizing: 'border-box', display: 'flex', alignItems: 'center', gap: 30,
              padding: portrait ? '0 34px' : '0 40px', border: `3px solid ${on ? CLAUDE.INK : CLAUDE.BORDER}`,
              borderBottom: `${on ? 10 : 3}px solid ${on ? CLAUDE.SPARK : CLAUDE.BORDER}` }}>
              <div style={{ width: 76, height: 76, flexShrink: 0, borderRadius: tone === 'risk' ? 16 : 38,
                background: CLAUDE.FOOTER, color: CLAUDE.INK, border: `5px solid ${on ? CLAUDE.INK : CLAUDE.BORDER}`,
                display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SANS, fontSize: 46, fontWeight: 800 }}>{mark}</div>
              <div style={{ flex: 1 }}>
                <div style={{ fontFamily: SERIF, fontSize: portrait ? 54 : 52, color: CLAUDE.INK, lineHeight: 1.1 }}>{it.label}</div>
                <div style={{ fontFamily: SANS, fontSize: 34, color: CLAUDE.INK_SOFT, marginTop: 8, lineHeight: 1.25 }}>{it.detail}</div>
              </div>
              {it.answers && !portrait && (
                <div style={{ fontFamily: SANS, fontSize: 28, color: CLAUDE.INK_SOFT, background: CLAUDE.PILL, borderRadius: 999,
                  padding: '8px 18px', whiteSpace: 'nowrap' }}>answers: {it.answers}</div>
              )}
            </Card>
          </div>
        );
      })}
      <Bug width={width} height={height} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// 6. AgentFitSort — tasks sort into "hand it to an agent" vs "keep it yourself"

export const agentFitSortSchema = z.object({
  title: z.string().default('Hand It Off, or Keep It?'),
  leftLabel: z.string().default('Hand it to an agent'),
  rightLabel: z.string().default('Keep it yourself'),
  tasks: z.array(z.object({ text: z.string(), why: z.string(), side: z.enum(['left', 'right']) })).default([]),
  cues: z.array(z.number()).default([]),
  durationSeconds: z.number().optional(),
  ...brand,
});

const AgentFitSortInner: React.FC<z.infer<typeof agentFitSortSchema>> = ({ title, leftLabel, rightLabel, tasks, cues }) => {
  const { width, height, portrait, reveal } = useClock();
  const colW = portrait ? width * 0.88 : width * 0.42;
  const colH = portrait ? height * 0.33 : height * 0.62;
  const cols = portrait
    ? { left: { x: width * 0.06, y: height * 0.17 }, right: { x: width * 0.06, y: height * 0.54 } }
    : { left: { x: width * 0.06, y: height * 0.22 }, right: { x: width * 0.52, y: height * 0.22 } };
  const count = { left: 0, right: 0 } as Record<'left' | 'right', number>;
  const rowH = portrait ? 150 : 150;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title text={title} at={0} />
      {(['left', 'right'] as const).map((side) => (
        <Card key={side} style={{ position: 'absolute', left: cols[side].x, top: cols[side].y, width: colW, height: colH,
          background: side === 'left' ? CLAUDE.CARD : CLAUDE.FOOTER }}>
          <div style={{ fontFamily: SERIF, fontSize: 46, color: CLAUDE.INK, padding: '26px 34px 0' }}>
            {side === 'left' ? '✓ ' : '✕ '}{side === 'left' ? leftLabel : rightLabel}</div>
        </Card>
      ))}
      {tasks.map((task, i) => {
        const o = Math.min(1, reveal(cues[i]));
        const k = count[task.side]++;
        const target = cols[task.side];
        const x = target.x + 30;
        const y = target.y + 110 + k * rowH;
        const fromY = height * 0.5;
        return (
          <div key={task.text} style={{ position: 'absolute', left: x, top: interpolate(o, [0, 1], [fromY, y]), width: colW - 60,
            opacity: Math.min(1, o * 1.4), background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 16,
            padding: '14px 22px', boxSizing: 'border-box', boxShadow: '0 6px 16px rgba(61,57,41,0.08)' }}>
            <div style={{ fontFamily: SANS, fontSize: 32, fontWeight: 600, color: CLAUDE.INK }}>{task.text}</div>
            <div style={{ fontFamily: SANS, fontSize: 26, color: CLAUDE.INK_SOFT, marginTop: 4 }}>{task.why}</div>
          </div>
        );
      })}
      <Bug width={width} height={height} />
    </AbsoluteFill>
  );
};

const Pick916: React.FC<{ portrait: React.ReactElement; landscape: React.ReactElement }> = ({ portrait, landscape }) => {
  const { width, height } = useVideoConfig();
  return height > width ? portrait : landscape;
};

// ─────────────────────────────────────────────────────────────────────────────
// Portrait (9:16) views. GATE T's portrait floor is a 72 px text run at 3840 px, i.e. ~68 px type on the
// 1080x1920 design canvas, and the bottom 14% is platform UI, so content stays inside y 96-1651.
// Each view keeps the beat's single idea and drops secondary text (it stays in the 16:9 cut and the voice).

const P = { title: 88, big: 88, body: 68, x0: 54, x1: 1026, top: 160, bottom: 1640 };

const PTitle: React.FC<{ text: string }> = ({ text }) => (
  <div style={{ position: 'absolute', left: P.x0, right: 1080 - P.x1, top: P.top, fontFamily: SERIF, fontSize: P.title,
    color: CLAUDE.INK, lineHeight: 1.08, textAlign: 'center' }}>{text}</div>
);

const PBug: React.FC = () => {
  const { handle, logo } = React.useContext(BrandCtx);
  return logo
    ? <Img src={staticFile(logo)} style={{ position: 'absolute', right: 64, top: 104, height: 30, opacity: 0.45 }} />
    : <div style={{ position: 'absolute', right: 64, top: 104, fontFamily: SANS, fontSize: 30, color: CLAUDE.INK_SOFT, opacity: 0.4 }}>{handle}</div>;
};

const ChatVsLoopP: React.FC<z.infer<typeof agentChatVsLoopSchema>> = ({ title, cues }) => {
  const { t, reveal } = useClock();
  const [cChat, cYou, cAgent, cOwn, cCalc, cIntern] = cues;
  const chatIn = Math.min(1, reveal(cChat));
  const youRing = Math.min(1, reveal(cYou));
  const agentIn = Math.min(1, reveal(cAgent));
  const ownLoop = interpolate(t, [cOwn, cOwn + 3], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const spin = t > cOwn ? ((t - cOwn) / 2.4) % 1 : 0;
  const msg = interpolate(t, [cChat + 0.6, cChat + 1.6], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const ans = interpolate(t, [cChat + 1.8, cChat + 2.8], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const chip = (text: string, o: number): React.CSSProperties => ({ fontFamily: SANS, fontSize: P.body, color: CLAUDE.INK,
    background: CLAUDE.PILL, borderRadius: 16, padding: '4px 20px', opacity: o });
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <PTitle text={title} />
      <Card style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top: 290, height: 600, opacity: chatIn, padding: 30, boxSizing: 'border-box' }}>
        <div style={{ fontFamily: SERIF, fontSize: P.big, color: CLAUDE.INK }}>Chatbot</div>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 20 }}>
          <You size={170} seed="background-agents-B02" ring={youRing} />
          <div style={{ display: 'flex', flexDirection: 'column', gap: 18, alignItems: 'center' }}>
            <div style={chip('question', msg > 0 ? 1 : 0)}>Question</div>
            <div style={chip('answer', ans > 0 ? 1 : 0)}>Answer</div>
          </div>
          <div style={{ width: 170, height: 170, borderRadius: 30, background: CLAUDE.FOOTER, border: `3px solid ${CLAUDE.BORDER}`,
            display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 80, color: CLAUDE.SPARK }}>✻</div>
        </div>
        <div style={{ fontFamily: SERIF, fontSize: P.big, color: CLAUDE.INK, textAlign: 'center', marginTop: 26, opacity: youRing }}>You are the loop.</div>
        <div style={{ fontFamily: SANS, fontSize: P.body, color: CLAUDE.INK, textAlign: 'center', marginTop: 10, opacity: Math.min(1, reveal(cCalc)) }}>= a calculator</div>
      </Card>
      <Card style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top: 910, height: 730, opacity: agentIn, padding: 30, boxSizing: 'border-box' }}>
        <div style={{ fontFamily: SERIF, fontSize: P.big, color: CLAUDE.INK }}>Agent</div>
        <div style={{ display: 'flex', justifyContent: 'center', marginTop: -10 }}>
          <LoopRing size={440} spin={spin} active={ownLoop} labels={['decide', 'act', 'check', 'repeat']} fontSize={P.body} />
        </div>
        <div style={{ fontFamily: SANS, fontSize: P.body, color: CLAUDE.INK, textAlign: 'center', lineHeight: 1.15, opacity: Math.min(1, reveal(cIntern)) }}>
          = an intern with<br />a to-do list</div>
      </Card>
      <PBug />
    </AbsoluteFill>
  );
};

const LoopCycleP: React.FC<z.infer<typeof agentLoopCycleSchema>> = ({ title, steps, repeatText, cues }) => {
  const { t, reveal } = useClock();
  const stepCues = cues.slice(0, steps.length);
  const cRepeat = cues[steps.length];
  const cBrain = cues[steps.length + 1];
  const active = stepCues.reduce((k, c, i) => (t >= c ? i : k), -1);
  const repeating = t >= cRepeat;
  const cx = 540, cy = 660, r = 280;
  const pos = (i: number) => {
    const a = (i / steps.length) * Math.PI * 2 - Math.PI / 2;
    return { x: cx + Math.cos(a) * r, y: cy + Math.sin(a) * r };
  };
  const phase = repeating ? ((t - cRepeat) / 2.2) % 1 : 0;
  const da = phase * Math.PI * 2 - Math.PI / 2;
  const cur = active >= 0 ? steps[active] : null;
  const brainIn = Math.min(1, reveal(cBrain));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <PTitle text={title} />
      <svg width={1080} height={1920} style={{ position: 'absolute', inset: 0 }}>
        <circle cx={cx} cy={cy} r={r} fill="none" stroke={active >= 0 ? CLAUDE.INK_SOFT : CLAUDE.BORDER} strokeWidth={10} />
        {repeating && <circle cx={cx + Math.cos(da) * r} cy={cy + Math.sin(da) * r} r={20} fill={CLAUDE.SPARK} />}
      </svg>
      {steps.map((st, i) => {
        const p = pos(i);
        const on = i === active && !repeating;
        return (
          <div key={st.label} style={{ position: 'absolute', left: p.x, top: p.y, transform: 'translate(-50%,-50%)',
            background: CLAUDE.CARD, color: CLAUDE.INK, border: `${on ? 6 : 3}px solid ${on ? CLAUDE.INK : CLAUDE.BORDER}`,
            borderRadius: 20, padding: '8px 26px', fontFamily: SERIF, fontSize: P.big, opacity: i <= active || repeating ? 1 : 0.45 }}>
            {st.label}
            {on && <div style={{ position: 'absolute', left: -30, right: -30, bottom: -20, height: 10, borderRadius: 5, background: CLAUDE.SPARK }} />}
          </div>
        );
      })}
      <Card style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top: 1060, height: 580, padding: '30px 36px', boxSizing: 'border-box' }}>
        {repeating ? (
          <div style={{ fontFamily: SERIF, fontSize: P.big, color: CLAUDE.INK, lineHeight: 1.15 }}>↻ {repeatText}</div>
        ) : cur && (
          <>
            <div style={{ fontFamily: SERIF, fontSize: P.big, color: CLAUDE.INK }}>{cur.label}</div>
            <div style={{ fontFamily: SANS, fontSize: P.body, color: CLAUDE.INK, lineHeight: 1.18, marginTop: 14 }}>{cur.detail}</div>
          </>
        )}
        <div style={{ position: 'absolute', left: 36, bottom: 30, fontFamily: SANS, fontSize: P.body, color: CLAUDE.INK_SOFT, opacity: brainIn, lineHeight: 1.2 }}>
          the model is the brain<br />tools are the hands</div>
      </Card>
      <PBug />
    </AbsoluteFill>
  );
};

const RunLogP: React.FC<z.infer<typeof agentRunLogSchema>> = ({ title, note, blocks }) => {
  const { t, reveal } = useClock();
  const shown = blocks.filter((b) => t >= b.at);
  const current = shown.length - 1;
  const b = current >= 0 ? blocks[current] : null;
  const colour = { out: CC.INK_2, fail: CC.DEL_FG, ok: CC.ADD_FG, add: CC.ADD_FG, del: CC.DEL_FG } as const;
  const bg = { out: 'transparent', fail: 'transparent', ok: 'transparent', add: CC.ADD_BG, del: CC.DEL_BG } as const;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <div style={{ position: 'absolute', left: 80, width: 920, top: P.top, height: 1240, background: CC.PAGE, borderRadius: 18,
        boxShadow: '0 10px 24px rgba(31,30,27,0.25)', overflow: 'hidden' }}>
        <div style={{ height: 100, background: CC.PANEL, display: 'flex', alignItems: 'center', gap: 12, padding: '0 26px',
          borderBottom: `2px solid ${CC.BORDER}` }}>
          {[CC.TL_RED, CC.TL_YEL, CC.TL_GRN].map((c) => <div key={c} style={{ width: 22, height: 22, borderRadius: 11, background: c }} />)}
          <div style={{ marginLeft: 18, fontFamily: CC_FONT.ui, fontSize: P.body, color: CC.INK_2 }}>{title.split(' · ')[0]}</div>
        </div>
        {/* the trail of loop steps so far */}
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 14, padding: '26px 26px 10px' }}>
          {blocks.map((x, i) => i > current ? null : (
            <span key={i} style={{ fontFamily: CC_FONT.ui, fontSize: 54, fontWeight: 700, letterSpacing: 2, borderRadius: 12, padding: '4px 16px',
              color: i === current ? CC.PAGE : CC.INK, background: i === current ? CC.INK : CC.BORDER }}>{x.step.toUpperCase()}</span>
          ))}
        </div>
        <div style={{ height: 10, margin: '6px 26px 22px', borderRadius: 5, background: CC.SPARK, opacity: b ? 1 : 0 }} />
        {b && (
          <div style={{ padding: '0 26px', opacity: Math.min(1, reveal(b.at)) }}>
            <div style={{ fontFamily: MONO, fontSize: P.body, color: CC.INK, whiteSpace: 'pre-wrap', wordBreak: 'break-word', lineHeight: 1.2 }}>{b.head}</div>
            {b.lines.map((l, k) => (
              <div key={k} style={{ fontFamily: MONO, fontSize: P.body, color: colour[l.kind], background: bg[l.kind], lineHeight: 1.2,
                whiteSpace: 'pre-wrap', wordBreak: 'break-word', padding: '2px 8px', marginTop: 10, borderRadius: 6 }}>{l.text.trim()}</div>
            ))}
          </div>
        )}
      </div>
      <div style={{ position: 'absolute', left: P.x0, right: 1080 - P.x1, top: 1430, fontFamily: SANS, fontSize: P.body,
        color: CLAUDE.INK_SOFT, textAlign: 'center', lineHeight: 1.15 }}>{note}</div>
      <PBug />
    </AbsoluteFill>
  );
};

const BackgroundLanesP: React.FC<z.infer<typeof agentBackgroundLanesSchema>> = ({ title, lanes, notice, cues }) => {
  const { t, reveal } = useClock();
  const [cCloud, cClose, cNotify, cParallel] = cues;
  const lid = interpolate(t, [cClose, cClose + 1.2], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const notifyIn = Math.min(1, reveal(cNotify));
  const progress = (i: number) => i === 0
    ? Math.min(1, Math.max(0, (t - cClose) / Math.max(0.1, cNotify - cClose)))
    : Math.min(0.92, Math.max(0, t - (cParallel + i * 0.4)) * lanes[i].rate);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <PTitle text={title} />
      <div style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top: 370, height: 240, display: 'flex',
        alignItems: 'center', justifyContent: 'space-around' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 24 }}>
          <You size={190} seed="background-agents-B05" />
          <div style={{ fontFamily: SANS, fontSize: 80, fontWeight: 600, color: CLAUDE.INK }}>{t >= cClose + 1 ? 'You, away' : 'You'}</div>
        </div>
        <div style={{ position: 'relative', width: 240, height: 180 }}>
          <div style={{ position: 'absolute', left: 20, right: 20, bottom: 64, height: Math.max(44, 130 * (1 - lid)),
            background: CLAUDE.FOOTER, border: `6px solid ${CLAUDE.INK_SOFT}`, borderRadius: 10 }} />
          <div style={{ position: 'absolute', left: 0, right: 0, bottom: 20, height: 40, background: CLAUDE.INK_SOFT, borderRadius: 8 }} />
        </div>
      </div>
      <Card style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top: 630, height: 740, padding: '24px 34px', boxSizing: 'border-box',
        opacity: Math.min(1, reveal(cCloud)) }}>
        <div style={{ fontFamily: SERIF, fontSize: P.big, color: CLAUDE.INK, marginBottom: 18 }}>In the cloud</div>
        {lanes.map((l, i) => {
          const p = progress(i);
          const started = i === 0 ? t >= cClose : t >= cParallel + i * 0.4;
          return (
            <div key={l.label} style={{ marginBottom: 22, opacity: started ? 1 : 0.35 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontFamily: SANS, fontSize: P.body, color: CLAUDE.INK }}>
                <span>{l.label}</span><span style={{ fontWeight: 700 }}>{p >= 1 ? '✓' : ''}</span>
              </div>
              <div style={{ height: 44, background: CLAUDE.PILL, borderRadius: 22, overflow: 'hidden', marginTop: 8 }}>
                <div style={{ width: `${p * 100}%`, height: '100%', background: p >= 1 ? CLAUDE.SPARK : CLAUDE.INK_SOFT }} />
              </div>
            </div>
          );
        })}
      </Card>
      <div style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top: 1390, boxSizing: 'border-box', opacity: notifyIn,
        background: CLAUDE.CARD, border: `3px solid ${CLAUDE.INK_SOFT}`, borderBottom: `10px solid ${CLAUDE.SPARK}`, borderRadius: 18,
        padding: '16px 28px', fontFamily: SANS, fontSize: P.body, color: CLAUDE.INK, lineHeight: 1.15 }}>✓ {notice}</div>
      <PBug />
    </AbsoluteFill>
  );
};

const ChecklistP: React.FC<z.infer<typeof agentChecklistSchema>> = ({ title, tone, items, cues }) => {
  const { t, reveal } = useClock();
  const active = cues.reduce((k, c, i) => (t >= c ? i : k), -1);
  const top = 380, gap = 22;
  const h = (P.bottom - top - gap * (items.length - 1)) / items.length;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <PTitle text={title} />
      {items.map((it, i) => {
        const o = Math.min(1, reveal(cues[i]));
        const on = i === active;
        const mark = it.mark ?? (tone === 'risk' ? '!' : '✓');
        return (
          <div key={it.label} style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top: top + i * (h + gap), height: h }}>
            <Card style={{ height: '100%', boxSizing: 'border-box', display: 'flex', alignItems: 'center', gap: 26, padding: '0 30px', opacity: 0.35 + 0.65 * o,
              border: `3px solid ${on ? CLAUDE.INK : CLAUDE.GHOST}`, borderBottom: `${on ? 12 : 3}px solid ${on ? CLAUDE.SPARK : CLAUDE.GHOST}` }}>
              <div style={{ width: 110, height: 110, flexShrink: 0, borderRadius: tone === 'risk' ? 20 : 55, background: CLAUDE.FOOTER, opacity: o,
                border: `5px solid ${on ? CLAUDE.INK : CLAUDE.BORDER}`, display: 'flex', alignItems: 'center', justifyContent: 'center',
                fontFamily: SANS, fontSize: 70, fontWeight: 800, color: CLAUDE.INK }}>{mark}</div>
              <div style={{ flex: 1, opacity: o }}>
                <div style={{ fontFamily: SERIF, fontSize: P.big, color: CLAUDE.INK, lineHeight: 1.05 }}>{it.label}</div>
                <div style={{ fontFamily: SANS, fontSize: P.body, color: CLAUDE.INK_SOFT, marginTop: 6, lineHeight: 1.12 }}>{it.detail}</div>
              </div>
            </Card>
          </div>
        );
      })}
      <PBug />
    </AbsoluteFill>
  );
};

const FitSortP: React.FC<z.infer<typeof agentFitSortSchema>> = ({ title, leftLabel, rightLabel, tasks, cues }) => {
  const { reveal } = useClock();
  const col = { left: 380, right: 1030 };
  const count = { left: 0, right: 0 } as Record<'left' | 'right', number>;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <PTitle text={title} />
      {(['left', 'right'] as const).map((side) => (
        <Card key={side} style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top: col[side], height: 610,
          background: side === 'left' ? CLAUDE.CARD : CLAUDE.FOOTER }}>
          <div style={{ fontFamily: SERIF, fontSize: P.big, color: CLAUDE.INK, padding: '22px 30px 0' }}>
            {side === 'left' ? '✓ ' : '✕ '}{side === 'left' ? leftLabel : rightLabel}</div>
        </Card>
      ))}
      {tasks.map((task, i) => {
        const o = Math.min(1, reveal(cues[i]));
        const k = count[task.side]++;
        const y = col[task.side] + 130 + k * 160;
        return (
          <div key={task.text} style={{ position: 'absolute', left: P.x0 + 26, width: P.x1 - P.x0 - 52, top: interpolate(o, [0, 1], [y + 60, y]),
            opacity: Math.min(1, o * 1.4), background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 16,
            padding: '14px 24px', boxSizing: 'border-box', fontFamily: SANS, fontSize: P.body, color: CLAUDE.INK }}>{task.text}</div>
        );
      })}
      <PBug />
    </AbsoluteFill>
  );
};

export const AgentChatVsLoop: React.FC<z.infer<typeof agentChatVsLoopSchema>> = (props) => (
  <BrandCtx.Provider value={{ handle: props.handle ?? '@NikBearBrown', logo: props.logo, avatar: props.avatar ?? 'bear' }}>
    <Pick916 portrait={<ChatVsLoopP {...props} />} landscape={<AgentChatVsLoopInner {...props} />} />
  </BrandCtx.Provider>
);

export const AgentLoopCycle: React.FC<z.infer<typeof agentLoopCycleSchema>> = (props) => (
  <BrandCtx.Provider value={{ handle: props.handle ?? '@NikBearBrown', logo: props.logo, avatar: props.avatar ?? 'bear' }}>
    <Pick916 portrait={<LoopCycleP {...props} />} landscape={<AgentLoopCycleInner {...props} />} />
  </BrandCtx.Provider>
);

export const AgentRunLog: React.FC<z.infer<typeof agentRunLogSchema>> = (props) => (
  <BrandCtx.Provider value={{ handle: props.handle ?? '@NikBearBrown', logo: props.logo, avatar: props.avatar ?? 'bear' }}>
    <Pick916 portrait={<RunLogP {...props} />} landscape={<AgentRunLogInner {...props} />} />
  </BrandCtx.Provider>
);

export const AgentBackgroundLanes: React.FC<z.infer<typeof agentBackgroundLanesSchema>> = (props) => (
  <BrandCtx.Provider value={{ handle: props.handle ?? '@NikBearBrown', logo: props.logo, avatar: props.avatar ?? 'bear' }}>
    <Pick916 portrait={<BackgroundLanesP {...props} />} landscape={<AgentBackgroundLanesInner {...props} />} />
  </BrandCtx.Provider>
);

export const AgentChecklist: React.FC<z.infer<typeof agentChecklistSchema>> = (props) => (
  <BrandCtx.Provider value={{ handle: props.handle ?? '@NikBearBrown', logo: props.logo, avatar: props.avatar ?? 'bear' }}>
    <Pick916 portrait={<ChecklistP {...props} />} landscape={<AgentChecklistInner {...props} />} />
  </BrandCtx.Provider>
);

export const AgentFitSort: React.FC<z.infer<typeof agentFitSortSchema>> = (props) => (
  <BrandCtx.Provider value={{ handle: props.handle ?? '@NikBearBrown', logo: props.logo, avatar: props.avatar ?? 'bear' }}>
    <Pick916 portrait={<FitSortP {...props} />} landscape={<AgentFitSortInner {...props} />} />
  </BrandCtx.Provider>
);

// ─────────────────────────────────────────────────────────────────────────────
// 7. ChannelTitleOutro — title-restate outro for a channel that is NOT claude-liam / @NikBearBrown
// (OUTRO-LOCK reserves ClaudeTitleOutro, its hardcoded handle and mascot, for claude-liam reels).
// Poster-style serif title with the terracotta period, the channel wordmark, the handle. No mascot.

export const channelTitleOutroSchema = z.object({
  title: z.string().default('Title'),
  handle: z.string().default('@HumanitariansAI'),
  logo: z.string().optional(),
  durationSeconds: z.number().optional(),
});

export const ChannelTitleOutro: React.FC<z.infer<typeof channelTitleOutroSchema>> = ({ title, handle, logo }) => {
  const { width, height, portrait, reveal } = useClock();
  const titleIn = Math.min(1, reveal(0.2, true));
  const markIn = Math.min(1, reveal(1.0, true));
  const t = title.replace(/[.]$/, '');
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ width: width * (portrait ? 0.84 : 0.86), textAlign: 'center', opacity: titleIn,
        transform: `translateY(${(1 - titleIn) * 24}px)` }}>
        <div style={{ fontFamily: SERIF, fontSize: portrait ? 138 : 150, lineHeight: 1.1, color: CLAUDE.INK }}>
          {t}<span style={{ color: CLAUDE.SPARK }}>.</span>
        </div>
        <div style={{ marginTop: portrait ? 420 : 60, opacity: markIn, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 22 }}>
          {logo && <Img src={staticFile(logo)} style={{ height: portrait ? 100 : 120 }} />}
          <div style={{ fontFamily: SANS, fontSize: portrait ? 84 : 64, color: CLAUDE.INK_SOFT, letterSpacing: 1 }}>{handle}</div>
        </div>
      </div>
    </AbsoluteFill>
  );
};
