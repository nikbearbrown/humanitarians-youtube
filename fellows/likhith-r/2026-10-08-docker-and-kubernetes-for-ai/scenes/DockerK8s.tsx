/**
 * DockerK8s.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-docker-kubernetes ("Docker and Kubernetes for AI", @HumanitariansAI).
 *
 * Same contract as JevExplainer.tsx / MoeExplainer.tsx (whose stage helpers it reuses):
 * each component lays out natively for 16:9 (<Name>) and 9:16 (<Name>916) — never a
 * crop — and every motion is a pure function of progress, conformed via `durationSeconds`.
 * Version numbers, error text, user counts and replica counts are illustrative and
 * labelled so on screen; the mechanisms (image layers, replicas, self-healing, load
 * balancing) follow the Docker and Kubernetes docs — see the reel's SOURCES.md.
 * Accent: fills/borders use the darker terracotta ACC_TEXT (GATE T §8.3); text is INK.
 *
 *   DkHook      — same command: laptop ✓ works, production server ✗ crashes
 *   DkDrift     — laptop vs. server: library, OS and driver versions disagree
 *   DkImage     — layers stack into one container image; copies run on any host
 *   DkOverload  — users climb, one container's load maxes out, it crashes
 *   DkCluster   — a control plane over machines, each running containers
 *   DkScale     — scale up with demand, replace a failed copy, spread traffic
 *   DkTogether  — Docker = portable image; Kubernetes = scalable, resilient fleet
 */
import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ACC_TEXT, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';

const Note: React.FC<{ x: number; y: number; w: number; a: number; text: string; align?: 'left' | 'right' | 'center' }> = ({ x, y, w, a, text, align = 'left' }) => (
  <div style={{ position: 'absolute', left: x, top: y, width: w, textAlign: align, fontFamily: SANS, fontSize: 42, color: CLAUDE.INK_SOFT, opacity: a }}>{text}</div>
);

// a status badge: ✓ (ink pill) or ✗ (accent pill)
const Badge: React.FC<{ ok: boolean; text: string; a: number; size?: number }> = ({ ok, text, a, size = 52 }) => (
  <span style={{
    display: 'inline-flex', alignItems: 'center', gap: 14, padding: '10px 26px', borderRadius: 999, opacity: a,
    background: ok ? CLAUDE.INK : ACC_TEXT,   // filled pill: an outline reads as a second label (GATE T §8.6b)
    fontFamily: SANS, fontSize: size, fontWeight: 700, color: CLAUDE.CARD, whiteSpace: 'nowrap',
  }}>{ok ? '✓' : '✗'} {text}</span>
);

// ===========================================================================
// DkHook — the same command on two machines: works on the laptop, crashes in production
// ===========================================================================
export const dkHookSchema = z.object({
  title: z.string().default('Works on my machine.'),
  command: z.string().default('$ python serve.py'),
  okLines: z.array(z.string()).default(['loading model…', 'listening on :8000']),
  errLines: z.array(z.string()).default(['loading model…', 'Error: version mismatch']),
  caption: z.string().default('same code, different result'),
  note: z.string().default('illustrative output'),
  sparkLine: z.string().default('Why does it break?'),
  durationSeconds: z.number().optional(),
});
export const dkHookMeta = durMeta(4);
export const DkHook: React.FC<z.infer<typeof dkHookSchema>> = ({ title, command, okLines, errLines, caption, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 290 : 210;
  const gap = P ? 30 : 80;
  const cw = P ? S.w : (S.w - gap) / 2;
  const ch = P ? 470 : 560;
  const panels = [
    { name: 'your laptop', lines: okLines, ok: true, at: 0.04 },
    { name: 'production server', lines: errLines, ok: false, at: 0.34 },
  ];
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {panels.map((p, i) => {
        const a = ease(ramp(t, p.at, p.at + 0.1));
        const res = ease(ramp(t, p.at + 0.16, p.at + 0.24));
        const left = P ? S.x : S.x + i * (cw + gap);
        const y = P ? top + i * (ch + gap) : top;
        return (
          <Card key={p.name} accent={!p.ok && res > 0.5} style={{
            left, top: y, width: cw, height: ch, opacity: a, borderWidth: !p.ok && res > 0.5 ? 6 : 3,
            borderColor: !p.ok && res > 0.5 ? ACC_TEXT : CLAUDE.BORDER,
          }}>
            <div style={{ position: 'absolute', left: 40, top: 30, fontFamily: SERIF, fontSize: P ? 60 : 64, color: CLAUDE.INK }}>{p.name}</div>
            <div style={{ position: 'absolute', left: 40, top: P ? 110 : 140, right: 40, fontFamily: MONO, fontSize: P ? 46 : 44, color: CLAUDE.INK, lineHeight: P ? 1.3 : 1.5 }}>
              <div>{command}</div>
              {p.lines.map((l, k) => (
                <div key={k} style={{
                  opacity: ease(ramp(t, p.at + 0.06 + k * 0.06, p.at + 0.1 + k * 0.06)),
                  color: !p.ok && k === p.lines.length - 1 ? ACC_TEXT : CLAUDE.INK_SOFT,
                  fontWeight: !p.ok && k === p.lines.length - 1 ? 700 : 400,
                  whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis',
                }}>{l}</div>
              ))}
            </div>
            <div style={{ position: 'absolute', left: 40, bottom: P ? 30 : 44 }}>
              <Badge ok={p.ok} text={p.ok ? 'works' : 'crashes'} a={res} size={P ? 50 : 56} />
            </div>
          </Card>
        );
      })}
      <div style={{
        position: 'absolute', left: S.x, width: S.w, top: P ? top + 2 * ch + gap + 30 : top + ch + 40,
        display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', opacity: ease(ramp(t, 0.66, 0.76)),
      }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 60 : 66, color: CLAUDE.INK, fontStyle: 'italic' }}>{caption}</span>
        {!P && <span style={{ fontFamily: SANS, fontSize: 42, color: CLAUDE.INK_SOFT }}>{note}</span>}
      </div>
      <Spark st={st} text={P ? '' : sparkLine} at={0.82} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// DkDrift — laptop vs. server: the environment rows disagree, one by one
// ===========================================================================
export const dkDriftSchema = z.object({
  title: z.string().default('Every machine is different'),
  rows: z.array(z.object({ label: z.string(), laptop: z.string(), server: z.string() })).default([
    { label: 'PyTorch', laptop: '2.3', server: '1.13' },
    { label: 'Python', laptop: '3.11', server: '3.8' },
    { label: 'OS', laptop: 'macOS 14', server: 'Ubuntu 20.04' },
    { label: 'GPU driver', laptop: 'CUDA 12', server: 'CUDA 11' },
  ]),
  caption: z.string().default('one mismatch is enough to crash'),
  note: z.string().default('illustrative versions'),
  sparkLine: z.string().default('Environments drift.'),
  durationSeconds: z.number().optional(),
});
export const dkDriftMeta = durMeta(6);
export const DkDrift: React.FC<z.infer<typeof dkDriftSchema>> = ({ title, rows, caption, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 320 : 200;
  const labelW = P ? 220 : 560;
  const colW = (S.w - labelW) / 2;
  const headH = P ? 90 : 90;
  const rowH = P ? 170 : 135;
  const flag = ease(ramp(t, 0.6, 0.7));
  const fs = P ? 44 : 56;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, width: S.w, opacity: ease(ramp(t, 0.02, 0.1)) }}>
        {(P ? ['laptop', 'server'] : ['your laptop', 'production server']).map((h, i) => (
          <div key={h} style={{
            position: 'absolute', left: labelW + i * colW, width: colW, top: 0, height: headH, textAlign: 'center',
            fontFamily: SERIF, fontSize: P ? 50 : 58, color: CLAUDE.INK,
          }}>{h}</div>
        ))}
        <div style={{ position: 'absolute', left: 0, top: headH - 6, width: S.w, height: 4, background: CLAUDE.INK }} />
      </div>
      {rows.map((r, i) => {
        // rows land in narration order across the first half of the beat
        const a = ease(ramp(t, 0.1 + i * 0.1, 0.18 + i * 0.1));
        const y = top + headH + 20 + i * rowH;
        const cell = (v: string, k: number, bad: boolean) => (
          <div style={{
            position: 'absolute', left: labelW + k * colW + 16, width: colW - 32, top: 12, height: rowH - 24, boxSizing: 'border-box',
            display: 'flex', alignItems: 'center', justifyContent: 'center', borderRadius: 12, background: CLAUDE.CARD,
            border: `${bad ? 6 : 3}px solid ${bad ? ACC_TEXT : CLAUDE.BORDER}`,
            fontFamily: MONO, fontSize: fs, fontWeight: bad ? 700 : 400, color: CLAUDE.INK, whiteSpace: 'nowrap',
          }}>{v}</div>
        );
        return (
          <div key={r.label} style={{ position: 'absolute', left: S.x, top: y, width: S.w, height: rowH, opacity: a }}>
            <div style={{ position: 'absolute', left: 0, top: 0, height: rowH, display: 'flex', alignItems: 'center', fontFamily: SANS, fontSize: fs, color: CLAUDE.INK }}>{r.label}</div>
            {cell(r.laptop, 0, false)}
            {cell(r.server, 1, flag > 0.5 && r.laptop !== r.server)}
          </div>
        );
      })}
      <div style={{
        position: 'absolute', left: S.x, top: top + headH + 20 + rows.length * rowH + (P ? 30 : 16), width: S.w,
        display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', flexWrap: 'wrap', gap: 10, opacity: flag,
      }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 60 : 64, color: CLAUDE.INK, fontStyle: 'italic' }}>{caption}</span>
        <span style={{ fontFamily: SANS, fontSize: 42, color: CLAUDE.INK_SOFT }}>{note}</span>
      </div>
      <Spark st={st} text={P ? sparkLine : ''} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// DkImage — the layers stack into one image; the same image runs on every host
// ===========================================================================
export const dkImageSchema = z.object({
  title: z.string().default('Docker: one portable image'),
  layers: z.array(z.string()).default(['base OS (e.g. Ubuntu)', 'GPU libraries (CUDA)', 'Python + libraries', 'your serving code', 'model weights']),
  imageLabel: z.string().default('container image'),
  hosts: z.array(z.string()).default(['laptop', 'server', 'cloud']),
  note: z.string().default('GPU hosts still need their own driver'),
  sparkLine: z.string().default('Ship the whole box.'),
  durationSeconds: z.number().optional(),
});
export const dkImageMeta = durMeta(6);
export const DkImage: React.FC<z.infer<typeof dkImageSchema>> = ({ title, layers, imageLabel, hosts, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 320 : 200;
  const stackW = P ? S.w : 900;
  const lh = P ? 96 : 108;
  const lg = 12;
  const pad = 26;
  const n = layers.length;
  const boxH = 90 + n * lh + (n - 1) * lg + pad;   // header + layers
  const boxed = ease(ramp(t, 0.42, 0.52));
  const hostsX = P ? S.x : S.x + stackW + 90;
  const hostsW = P ? S.w : S.r - hostsX;
  const hostsTop = P ? top + boxH + 50 : top;
  const hostGap = P ? 24 : 30;
  const hostW = P ? (S.w - hostGap * (hosts.length - 1)) / hosts.length : hostsW;
  const hostH = P ? 250 : (boxH - hostGap * (hosts.length - 1)) / hosts.length;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {/* the image frame draws around the finished stack */}
      <div style={{
        position: 'absolute', left: S.x, top, width: stackW, height: boxH, boxSizing: 'border-box', borderRadius: 18,
        border: `6px solid ${ACC_TEXT}`, opacity: boxed, background: CLAUDE.CARD,
      }} />
      <div style={{ position: 'absolute', left: S.x + pad, top: top + 18, fontFamily: MONO, fontSize: P ? 46 : 50, fontWeight: 700, color: CLAUDE.INK, opacity: boxed }}>
        {imageLabel}
      </div>
      {layers.map((l, i) => {
        // bottom layer first: the stack builds upward
        const k = n - 1 - i;
        const a = ease(ramp(t, 0.04 + k * 0.065, 0.11 + k * 0.065));
        return (
          <div key={l} style={{
            position: 'absolute', left: S.x + pad, width: stackW - pad * 2, height: lh, top: top + 90 + i * (lh + lg) - (1 - a) * 40,
            boxSizing: 'border-box', borderRadius: 10, opacity: a,
            background: i === n - 1 ? CLAUDE.INK : CLAUDE.FOOTER, border: `3px solid ${i === n - 1 ? CLAUDE.INK : CLAUDE.BORDER}`,
            display: 'flex', alignItems: 'center', paddingLeft: 30,
            fontFamily: SANS, fontSize: P ? 46 : 50, color: i === n - 1 ? CLAUDE.CARD : CLAUDE.INK,
          }}>{l}</div>
        );
      })}
      {hosts.map((h, i) => {
        const a = ease(ramp(t, 0.58 + i * 0.07, 0.66 + i * 0.07));
        const pos = P
          ? { left: S.x + i * (hostW + hostGap), top: hostsTop }
          : { left: hostsX, top: hostsTop + i * (hostH + hostGap) };
        return (
          <Card key={h} style={{
            ...pos, width: hostW, height: hostH, opacity: a, transform: `translateX(${(1 - a) * (P ? 0 : -40)}px) translateY(${(1 - a) * (P ? -30 : 0)}px)`,
            display: 'flex', flexDirection: P ? 'column' : 'row', alignItems: 'center', justifyContent: P ? 'center' : 'space-between',
            padding: P ? 10 : '0 40px', gap: P ? 18 : 0,
          }}>
            <span style={{ fontFamily: SERIF, fontSize: P ? 56 : 62, color: CLAUDE.INK }}>{h}</span>
            <Badge ok text="same" a={ease(ramp(t, 0.64 + i * 0.07, 0.7 + i * 0.07))} size={P ? 44 : 48} />
          </Card>
        );
      })}
      <Note x={S.x} y={P ? hostsTop + hostH + 26 : top + boxH + 24} w={P ? S.w : stackW}
        a={ease(ramp(t, 0.8, 0.88))} text={note} />
      <Spark st={st} text={P ? sparkLine : ''} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// DkOverload — users climb, one container's load maxes out, and it falls over
// ===========================================================================
export const dkOverloadSchema = z.object({
  title: z.string().default('One container hits a wall'),
  users: z.number().default(5000),
  note: z.string().default('illustrative traffic'),
  sparkLine: z.string().default('One is not enough.'),
  durationSeconds: z.number().optional(),
});
export const dkOverloadMeta = durMeta(4.5);
export const DkOverload: React.FC<z.infer<typeof dkOverloadSchema>> = ({ title, users, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 320 : 220;
  const grow = ease(ramp(t, 0.04, 0.6));
  const count = Math.round(50 + (users - 50) * grow);
  const load = Math.min(1, ramp(t, 0.12, 0.62));
  const crash = ease(ramp(t, 0.66, 0.74));
  // geometry: users block → stream → container
  const uW = P ? S.w : 520, uH = P ? 230 : 560;
  const cX = P ? S.x : S.r - 640, cY = P ? top + uH + 250 : top;
  const cW = P ? S.w : 640, cH = P ? 440 : 560;
  const sx0 = P ? S.x + S.w / 2 : S.x + uW + 20, sy0 = P ? top + uH + 20 : top + uH / 2;
  const sx1 = P ? S.x + S.w / 2 : cX - 20, sy1 = P ? cY - 20 : top + cH / 2;
  const dots = P ? 5 : 14;   // portrait path is short: fewer dots so they read as separate requests
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: S.x, top, width: uW, height: uH, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 6 }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 130 : 150, color: CLAUDE.INK, lineHeight: 1 }}>{count.toLocaleString('en-US')}</span>
        <span style={{ fontFamily: SANS, fontSize: P ? 46 : 50, color: CLAUDE.INK_SOFT }}>users sending requests</span>
      </Card>
      {/* requests streaming toward the single container; dropped (scattered) once it crashes */}
      <svg width={P ? 1080 : 1920} height={P ? 1920 : 1080} style={{ position: 'absolute', left: 0, top: 0 }}>
        {Array.from({ length: dots }).map((_, k) => {
          const speed = 1.5 + 2.5 * grow;
          const u = ((t * speed * 3 + k / dots) % 1);
          const x = sx0 + (sx1 - sx0) * u, y = sy0 + (sy1 - sy0) * u;
          const fall = crash * u * (P ? 0 : 90) * ((k % 3) - 1);
          const show = ramp(t, 0.04 + (k % dots) * 0.01, 0.08 + (k % dots) * 0.01) * (1 - crash * 0.6);
          return <circle key={k} cx={x + (P ? fall : 0)} cy={y + (P ? 0 : fall)} r={P ? 14 : 16} fill={CLAUDE.INK_SOFT} opacity={show} />;
        })}
      </svg>
      <Card accent={crash > 0.5} style={{
        left: cX, top: cY, width: cW, height: cH, borderWidth: crash > 0.5 ? 7 : 3, borderColor: crash > 0.5 ? ACC_TEXT : CLAUDE.BORDER,
        borderStyle: crash > 0.5 ? 'dashed' : 'solid',
      }}>
        <div style={{ position: 'absolute', left: 40, top: 30, fontFamily: MONO, fontSize: P ? 48 : 52, fontWeight: 700, color: CLAUDE.INK }}>1 container</div>
        <div style={{ position: 'absolute', left: 40, top: P ? 100 : 110, fontFamily: SANS, fontSize: P ? 44 : 46, color: CLAUDE.INK_SOFT }}>model server</div>
        <div style={{ position: 'absolute', left: 40, right: 40, top: P ? 175 : 250 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', fontFamily: SANS, fontSize: P ? 44 : 46, color: CLAUDE.INK }}>
            <span>load</span><span style={{ fontWeight: 700 }}>{Math.round(load * 100)}%</span>
          </div>
          <div style={{ marginTop: 12, height: P ? 50 : 60, borderRadius: 10, background: CLAUDE.BORDER }}>
            <div style={{ height: '100%', width: `${load * 100}%`, borderRadius: 10, background: load > 0.85 ? ACC_TEXT : CLAUDE.INK }} />
          </div>
        </div>
        <div style={{ position: 'absolute', left: 40, bottom: P ? 24 : 44, display: 'flex', alignItems: 'center' }}>
          <Badge ok={false} text="crashed" a={crash} size={P ? 44 : 48} />
          <span style={{ marginLeft: 20, fontFamily: SANS, fontSize: P ? 42 : 44, color: CLAUDE.INK, opacity: crash }}>requests dropped</span>
        </div>
      </Card>
      <Note x={S.x} y={P ? top + uH + 30 : top + uH + 30} w={P ? S.w / 2 - 60 : uW} a={ease(ramp(t, 0.1, 0.2))} text={note} />
      <Spark st={st} text={P ? sparkLine : ''} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// DkCluster — a control plane manages machines, each running containers
// ===========================================================================
export const dkClusterSchema = z.object({
  title: z.string().default('Kubernetes: the orchestrator'),
  control: z.string().default('Kubernetes control plane'),
  machines: z.array(z.number().int()).default([3, 2, 3]),   // containers per machine
  caption: z.string().default('many containers · many machines'),
  sparkLine: z.string().default('One brain, many machines.'),
  durationSeconds: z.number().optional(),
});
export const dkClusterMeta = durMeta(4);
export const DkCluster: React.FC<z.infer<typeof dkClusterSchema>> = ({ title, control, machines, caption, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 320 : 200;
  const cpW = P ? S.w : 1000, cpH = P ? 130 : 130;
  const cpX = P ? S.x : S.x + (S.w - cpW) / 2;
  const m = machines.length;
  const gap = P ? 26 : 50;
  const nTop = top + cpH + (P ? 90 : 110);
  const nW = P ? S.w : (S.w - gap * (m - 1)) / m;
  const nH = P ? 210 : 470;
  const cpIn = ease(ramp(t, 0.02, 0.12));
  const maxPods = Math.max(...machines);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{
        left: cpX, top, width: cpW, height: cpH, opacity: cpIn, background: CLAUDE.INK, border: `3px solid ${CLAUDE.INK}`,
        display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SERIF, fontSize: P ? 56 : 62, color: CLAUDE.CARD,
      }}>{control}</Card>
      {/* wires from the control plane to every machine */}
      <svg width={P ? 1080 : 1920} height={P ? 1920 : 1080} style={{ position: 'absolute', left: 0, top: 0 }}>
        {machines.map((_, i) => {
          const d = ease(ramp(t, 0.16 + i * 0.04, 0.3 + i * 0.04));
          const x0 = P ? S.x + 40 : cpX + cpW * (i + 0.5) / m, y0 = top + cpH + 14;
          const x1 = P ? S.x + 40 : S.x + i * (nW + gap) + nW / 2, y1 = P ? nTop + i * (nH + gap) + nH / 2 : nTop - 14;
          if (P) {
            return <line key={i} x1={x0 - 24} y1={y0} x2={x0 - 24} y2={y0 + (y1 - y0) * d} stroke={CLAUDE.INK_SOFT} strokeWidth={6} />;
          }
          return <line key={i} x1={x0} y1={y0} x2={x0 + (x1 - x0) * d} y2={y0 + (y1 - y0) * d} stroke={CLAUDE.INK_SOFT} strokeWidth={6} />;
        })}
      </svg>
      {machines.map((pods, i) => {
        const a = ease(ramp(t, 0.2 + i * 0.05, 0.3 + i * 0.05));
        const left = P ? S.x + 40 : S.x + i * (nW + gap);
        const w = P ? S.w - 40 : nW;
        const y = P ? nTop + i * (nH + gap) : nTop;
        const inner = 30;
        const podGap = 18;
        const podW = P ? (w - inner * 2 - podGap * (maxPods - 1)) / maxPods : w - inner * 2;
        const podH = P ? nH - 110 : (nH - 110 - inner - podGap * (maxPods - 1)) / maxPods;
        return (
          <Card key={i} style={{ left, top: y, width: w, height: nH, opacity: a, background: CLAUDE.FOOTER }}>
            <div style={{ position: 'absolute', left: inner, top: 20, fontFamily: SANS, fontSize: P ? 44 : 48, color: CLAUDE.INK }}>machine {i + 1}</div>
            {Array.from({ length: pods }).map((_, k) => {
              const pa = ease(ramp(t, 0.38 + (i * 3 + k) * 0.035, 0.46 + (i * 3 + k) * 0.035));
              return (
                <div key={k} style={{
                  position: 'absolute', boxSizing: 'border-box', borderRadius: 10, opacity: pa,
                  left: P ? inner + k * (podW + podGap) : inner, top: P ? 90 : 90 + k * (podH + podGap),
                  width: podW, height: podH, background: CLAUDE.CARD, border: `3px solid ${CLAUDE.BORDER}`,
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  fontFamily: MONO, fontSize: P ? 42 : 44, color: CLAUDE.INK, transform: `scale(${0.85 + 0.15 * pa})`,
                }}>container</div>
              );
            })}
          </Card>
        );
      })}
      <div style={{
        position: 'absolute', left: S.x, width: S.w, top: P ? nTop + m * (nH + gap) + 10 : nTop + nH + 30,
        fontFamily: SERIF, fontSize: P ? 58 : 62, color: CLAUDE.INK, fontStyle: 'italic', opacity: ease(ramp(t, 0.62, 0.72)),
      }}>{caption}</div>
      <Spark st={st} text={P ? sparkLine : ''} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// DkScale — scale up with demand, replace a failed copy, spread the traffic
// ===========================================================================
export const dkScaleSchema = z.object({
  title: z.string().default('Scale, heal, balance'),
  from: z.number().int().default(2),
  to: z.number().int().default(5),
  failAt: z.number().int().default(2),   // index of the copy that fails
  phases: z.array(z.string()).default(['scale up', 'self-heal', 'load balance']),
  note: z.string().default('illustrative replica counts'),
  sparkLine: z.string().default('No one paged at 3 a.m.'),
  durationSeconds: z.number().optional(),
});
export const dkScaleMeta = durMeta(5);
export const DkScale: React.FC<z.infer<typeof dkScaleSchema>> = ({ title, from, to, failAt, phases, note }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 300 : 190;
  // three phases, each on its spoken clause
  const p1 = [0.04, 0.34], p2 = [0.38, 0.62], p3 = [0.66, 0.96];
  const fail = ease(ramp(t, p2[0], p2[0] + 0.06));
  const replace = ease(ramp(t, p2[0] + 0.12, p2[0] + 0.2));
  const route = ease(ramp(t, p3[0], p3[0] + 0.1));
  const active = t < p2[0] ? 0 : t < p3[0] ? 1 : 2;
  // phase chips
  const chipH = P ? 90 : 84;
  const chipGap = P ? 16 : 24;
  const chipW = (S.w - chipGap * 2) / 3;
  // load balancer + replicas
  const lbTop = top + chipH + (P ? 40 : 40);
  const lbH = P ? 100 : 100;
  const rTop = lbTop + lbH + (P ? 70 : 90);
  const rGap = P ? 16 : 24;
  const rW = P ? S.w : (S.w - rGap * (to - 1)) / to;
  const rH = P ? 118 : 360;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {phases.map((ph, i) => (
        <div key={ph} style={{
          position: 'absolute', left: S.x + i * (chipW + chipGap), top, width: chipW, height: chipH, boxSizing: 'border-box',
          borderRadius: 999, border: `${active === i ? 6 : 3}px solid ${active === i ? ACC_TEXT : CLAUDE.BORDER}`,
          background: CLAUDE.CARD, display: 'flex', alignItems: 'center', justifyContent: 'center',
          fontFamily: SANS, fontSize: P ? 42 : 46, fontWeight: active === i ? 700 : 400, color: active === i ? CLAUDE.INK : CLAUDE.INK_SOFT,
        }}>{P ? ph : `${i + 1}. ${ph}`}</div>
      ))}
      <Card style={{
        left: S.x, top: lbTop, width: S.w, height: lbH, background: CLAUDE.INK, border: `3px solid ${CLAUDE.INK}`,
        display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SERIF, fontSize: P ? 52 : 56, color: CLAUDE.CARD,
      }}>incoming traffic · load balancer</Card>
      {/* routes from the balancer to each live copy (phase 3) */}
      <svg width={P ? 1080 : 1920} height={P ? 1920 : 1080} style={{ position: 'absolute', left: 0, top: 0 }}>
        {Array.from({ length: to }).map((_, i) => {
          if (P) {
            const y = rTop + i * (rH + rGap) + rH / 2;
            return <line key={i} x1={S.x + 20} y1={lbTop + lbH} x2={S.x + 20} y2={lbTop + lbH + (y - lbTop - lbH) * route} stroke={CLAUDE.INK_SOFT} strokeWidth={6} />;
          }
          const x = S.x + i * (rW + rGap) + rW / 2;
          return <line key={i} x1={x} y1={lbTop + lbH} x2={x} y2={lbTop + lbH + (rTop - lbTop - lbH) * route} stroke={CLAUDE.INK_SOFT} strokeWidth={6} />;
        })}
      </svg>
      {Array.from({ length: to }).map((_, i) => {
        const born = i < from ? 1 : ease(ramp(t, p1[0] + (i - from) * 0.08, p1[0] + 0.1 + (i - from) * 0.08));
        const failed = i === failAt && fail > 0.5 && replace < 0.5;
        const reborn = i === failAt && replace >= 0.5;
        const share = route > 0 ? Math.round(100 / to) : null;
        const pos = P
          ? { left: S.x + 50, top: rTop + i * (rH + rGap), width: S.w - 50, height: rH }
          : { left: S.x + i * (rW + rGap), top: rTop, width: rW, height: rH };
        return (
          <Card key={i} style={{
            ...pos, opacity: born, transform: `scale(${0.85 + 0.15 * born})`,
            borderWidth: failed ? 7 : 3, borderColor: failed ? ACC_TEXT : CLAUDE.INK, borderStyle: failed ? 'dashed' : 'solid',
            display: 'flex', flexDirection: P ? 'row' : 'column', alignItems: 'center', justifyContent: P ? 'space-between' : 'center',
            gap: P ? 0 : 20, padding: P ? '0 30px' : 0,
          }}>
            <span style={{ fontFamily: MONO, fontSize: P ? 44 : 46, fontWeight: 700, color: CLAUDE.INK }}>copy {i + 1}</span>
            <span style={{ fontFamily: SANS, fontSize: P ? 42 : 44, fontWeight: failed ? 700 : 400, color: failed ? ACC_TEXT : CLAUDE.INK_SOFT, whiteSpace: 'nowrap' }}>
              {failed ? '✗ failed' : reborn ? '✓ replaced' : share !== null && route > 0.5 ? `${share}% of traffic` : '✓ running'}
            </span>
          </Card>
        );
      })}
      <div style={{
        position: 'absolute', left: S.x, width: S.w - (P ? 0 : 140), top: P ? rTop + to * (rH + rGap) + 14 : rTop + rH + 34,
        display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', flexWrap: 'wrap', gap: 10,
      }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 58 : 62, color: CLAUDE.INK }}>
          replicas: {from + Math.round((to - from) * ease(ramp(t, p1[0], p1[1])))}
        </span>
        <span style={{ fontFamily: SANS, fontSize: 42, color: CLAUDE.INK_SOFT }}>{note}</span>
      </div>
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// DkTogether — Docker makes one portable image; Kubernetes runs a resilient fleet of it
// ===========================================================================
export const dkTogetherSchema = z.object({
  title: z.string().default('Together'),
  left: z.object({ name: z.string(), gives: z.string() }).default({ name: 'Docker', gives: 'portable' }),
  right: z.object({ name: z.string(), gives: z.string() }).default({ name: 'Kubernetes', gives: 'scalable · resilient' }),
  copies: z.number().int().default(6),
  sparkLine: z.string().default('Pack it, then run it.'),
  durationSeconds: z.number().optional(),
});
export const dkTogetherMeta = durMeta(4.5);
export const DkTogether: React.FC<z.infer<typeof dkTogetherSchema>> = ({ title, left, right, copies, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 300 : 200;
  const gap = P ? 30 : 90;
  const lW = P ? S.w : 640, lH = P ? 340 : 740;
  const rX = P ? S.x : S.x + lW + gap, rY = P ? top + lH + gap : top;
  const rW = P ? S.w : S.r - rX, rH = P ? 600 : 740;
  const lIn = ease(ramp(t, 0.04, 0.16));
  const rIn = ease(ramp(t, 0.4, 0.5));
  const cols = 3, rows = Math.ceil(copies / cols);
  const pad = 36, cg = 22;
  const cW = (rW - pad * 2 - cg * (cols - 1)) / cols;
  const cH = (rH - 230 - pad - cg * (rows - 1)) / rows;
  // the original image is the one filled accent; its copies are plain cards (no accent-outlined text, GATE T §8.3)
  const imgChip = (w: number, h: number, fs: number, original = false) => (
    <div style={{
      width: w, height: h, boxSizing: 'border-box', borderRadius: 12, background: original ? ACC_TEXT : CLAUDE.FOOTER,
      border: original ? 'none' : `3px solid ${CLAUDE.BORDER}`,
      display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: MONO, fontSize: fs, fontWeight: original ? 700 : 400,
      color: original ? CLAUDE.CARD : CLAUDE.INK,
    }}>image</div>
  );
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: S.x, top, width: lW, height: lH, opacity: lIn, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: P ? 20 : 36 }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 76 : 84, color: CLAUDE.INK }}>{left.name}</span>
        {imgChip(P ? 380 : 420, P ? 120 : 170, P ? 52 : 60, true)}
        <span style={{ fontFamily: SANS, fontSize: P ? 52 : 58, fontWeight: 700, color: CLAUDE.INK, opacity: ease(ramp(t, 0.16, 0.26)) }}>{left.gives}</span>
      </Card>
      <Card style={{ left: rX, top: rY, width: rW, height: rH, opacity: rIn, border: `4px solid ${CLAUDE.INK_SOFT}` }}>
        <div style={{ position: 'absolute', left: pad, top: 26, fontFamily: SERIF, fontSize: P ? 76 : 84, color: CLAUDE.INK }}>{right.name}</div>
        {Array.from({ length: copies }).map((_, i) => {
          const a = ease(ramp(t, 0.46 + i * 0.03, 0.54 + i * 0.03));
          return (
            <div key={i} style={{
              position: 'absolute', left: pad + (i % cols) * (cW + cg), top: 140 + Math.floor(i / cols) * (cH + cg), opacity: a,
              transform: `scale(${0.8 + 0.2 * a})`,
            }}>{imgChip(cW, cH, P ? 42 : 46)}</div>
          );
        })}
        <div style={{
          position: 'absolute', left: pad, right: pad, bottom: 26, fontFamily: SANS, fontSize: P ? 52 : 58, fontWeight: 700,
          color: CLAUDE.INK, opacity: ease(ramp(t, 0.62, 0.72)),
        }}>{right.gives}</div>
      </Card>
      <Spark st={st} text={P ? sparkLine : ''} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
