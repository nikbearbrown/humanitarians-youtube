/**
 * SpecDriven.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-spec-driven-development ("Spec-Driven Development", @HumanitariansAI).
 *
 * Same contract as JevExplainer.tsx (whose stage helpers it reuses): each component
 * lays out natively for 16:9 (<Name>) and 9:16 (<Name>916) — never a crop — and
 * every motion is a pure function of progress, conformed via `durationSeconds`.
 * Example content (a login feature, file names, a drift function) is illustrative
 * and labelled so on screen; the argument follows GitHub's Spec Kit post (SOURCES.md).
 *
 *   SpecVibeGrowth     — files multiply, then some break with no explanation
 *   SpecSourceOfTruth  — prompt history struck out; the spec is the source of truth
 *   SpecGuesswork      — a vague prompt → three guesses; the spec locks one
 *   SpecReview         — a change checked line by line against the spec
 *   SpecVersions       — spec.md versions travel with each commit
 *   SpecDrift          — generated code not in the spec is flagged on sight
 *   SpecScale          — qualitative: prompt-only breakage climbs; spec-driven stays flat
 */
import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ACC_TEXT, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';

const Note: React.FC<{ x: number; y: number; w: number; a: number; text: string }> = ({ x, y, w, a, text }) => (
  <div style={{ position: 'absolute', left: x, top: y, width: w, fontFamily: SANS, fontSize: 36, color: CLAUDE.INK_SOFT, opacity: a }}>{text}</div>
);

// ===========================================================================
// SpecVibeGrowth — the project grows file by file; then things break, unexplained
// ===========================================================================
export const specVibeGrowthSchema = z.object({
  title: z.string().default('Vibe coding, file by file'),
  files: z.array(z.string()).default(['app.py', 'auth.py', 'db.py', 'api.py', 'models.py', 'utils.py', 'views.py', 'config.py', 'tests.py']),
  broken: z.array(z.number()).default([1, 4, 6]),
  sparkLine: z.string().default('Nobody can say why.'),
  durationSeconds: z.number().optional(),
});
export const specVibeGrowthMeta = durMeta(5);
export const SpecVibeGrowth: React.FC<z.infer<typeof specVibeGrowthSchema>> = ({ title, files, broken, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const perRow = 3;
  const gap = P ? 26 : 34;
  const top = P ? 330 : 270;
  const tileW = P ? (S.w - gap * 2) / 3 : 360;
  const tileH = P ? 190 : 150;
  const gridX = P ? S.x : S.x;
  const shown = Math.floor(ramp(t, 0.06, 0.5) * files.length + 1e-4);
  const brk = ease(ramp(t, 0.56, 0.68));
  const sideX = S.x + perRow * (tileW + gap) + 60;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {files.map((f, i) => {
        const on = i < shown;
        const bad = broken.includes(i) && brk > 0.3;
        return (
          <Card key={f} accent={bad} style={{
            left: gridX + (i % perRow) * (tileW + gap), top: top + Math.floor(i / perRow) * (tileH + gap),
            width: tileW, height: tileH, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 6,
            fontFamily: MONO, fontSize: P ? 38 : 40, color: CLAUDE.INK, opacity: on ? 1 : 0,
            transform: `translateY(${on ? 0 : 16}px)`,
          }}>
            {f}
            {bad && <span style={{ fontFamily: SANS, fontSize: 38, color: ACC_TEXT, opacity: brk }}>✕ broke</span>}
          </Card>
        );
      })}
      <div style={{
        position: 'absolute', ...(P ? { left: S.x, top: top + 3 * (tileH + gap) + 30 } : { left: sideX, top: top + 30 }),
        width: P ? S.w : S.r - sideX, fontFamily: SERIF, fontSize: P ? 64 : 72, color: CLAUDE.INK, lineHeight: 1.2,
      }}>
        <div>{shown} files</div>
        <div style={{ fontSize: P ? 50 : 52, color: ACC_TEXT, opacity: brk, marginTop: 20 }}>{broken.length} breaking</div>
        <div style={{ fontFamily: SANS, fontSize: 38, color: CLAUDE.INK_SOFT, opacity: brk, marginTop: 14 }}>illustrative project</div>
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// SpecSourceOfTruth — prompt history is struck out; the spec becomes the truth
// ===========================================================================
export const specSourceOfTruthSchema = z.object({
  title: z.string().default('The spec is the source of truth'),
  prompts: z.array(z.string()).default(['"make a login page"', '"no, add Google too"', '"undo that last part"']),
  sections: z.array(z.object({ head: z.string(), line: z.string() })).default([
    { head: 'Requirements', line: 'email and password sign-in' },
    { head: 'Behavior', line: 'lock after 5 failed tries' },
    { head: 'Constraints', line: 'no third-party auth' },
  ]),
  sparkLine: z.string().default('Spec first, code second.'),
  durationSeconds: z.number().optional(),
});
export const specSourceOfTruthMeta = durMeta(6);
export const SpecSourceOfTruth: React.FC<z.infer<typeof specSourceOfTruthSchema>> = ({ title, prompts, sections, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 430 : 270;   // portrait title wraps to two lines
  const colW = P ? S.w : (S.w - 80) * 0.42;
  const specX = P ? S.x : S.x + colW + 80;
  const specW = P ? S.w : S.w - colW - 80;
  const specTop = P ? top + prompts.length * 62 + 16 : top;
  const strike = ease(ramp(t, 0.44, 0.56));
  const specIn = ease(ramp(t, 0.3, 0.42));
  const pill = ease(ramp(t, 0.62, 0.72));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, fontFamily: SANS, fontSize: 38, color: CLAUDE.INK_SOFT }}>{P ? '' : 'prompt history'}</div>
      {prompts.map((p, i) => {
        const a = ease(ramp(t, 0.06 + i * 0.06, 0.14 + i * 0.06));
        return (
          <div key={p} style={{
            position: 'absolute', left: S.x, top: top + (P ? 0 : 70) + i * (P ? 62 : 110), width: colW,
            fontFamily: SANS, fontSize: P ? 40 : 42, color: CLAUDE.INK, opacity: a * (1 - strike * 0.45),
            textDecoration: strike > 0.5 ? 'line-through' : 'none', textDecorationColor: CLAUDE.SPARK,
          }}>{p}</div>
        );
      })}
      <Card accent={pill > 0.5} style={{
        left: specX, top: specTop, width: specW, padding: P ? '30px 36px' : '34px 44px', opacity: specIn,
        transform: `translateY(${(1 - specIn) * 20}px)`,
      }}>
        <div style={{ fontFamily: MONO, fontSize: 44, color: CLAUDE.INK, marginBottom: 20 }}>spec.md</div>
        {sections.map((s) => (
          <div key={s.head} style={{ marginBottom: 18 }}>
            <div style={{ fontFamily: SANS, fontSize: 38, color: CLAUDE.INK_SOFT }}>{s.head}</div>
            <div style={{ fontFamily: P ? SANS : SERIF, fontSize: P ? 70 : 50, lineHeight: 1.15, color: CLAUDE.INK }}>{s.line}</div>
          </div>
        ))}
        <div style={{
          display: 'inline-block', marginTop: 10, padding: '8px 24px', borderRadius: 999, background: CLAUDE.SPARK,
          fontFamily: SANS, fontSize: 38, color: CLAUDE.CARD, opacity: pill,
        }}>source of truth</div>
      </Card>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// SpecGuesswork — a vague prompt forks into guesses; the spec locks the intent
// ===========================================================================
export const specGuessworkSchema = z.object({
  title: z.string().default('Less guesswork'),
  prompt: z.string().default('"add login"'),
  guesses: z.array(z.string()).default(['email and password', 'Google sign-in', 'magic link']),
  lockedIndex: z.number().int().default(0),
  spec: z.string().default('spec: email and password, lock after 5 tries'),
  sparkLine: z.string().default('Intended, not inferred.'),
  durationSeconds: z.number().optional(),
});
export const specGuessworkMeta = durMeta(5);
export const SpecGuesswork: React.FC<z.infer<typeof specGuessworkSchema>> = ({ title, prompt, guesses, lockedIndex, spec, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 330 : 270;
  const n = guesses.length;
  const gap = P ? 24 : 36;
  const gW = P ? S.w : (S.w - gap * (n - 1)) / n;
  const gH = P ? 170 : 190;
  const gTop = top + (P ? 150 : 150);
  const specIn = ease(ramp(t, 0.46, 0.56));
  const lock = ease(ramp(t, 0.58, 0.68));
  const specTop = gTop + (P ? n * (gH + gap) + 20 : gH + 50);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, fontFamily: MONO, fontSize: P ? 50 : 56, color: CLAUDE.INK, opacity: ease(ramp(t, 0.04, 0.12)) }}>
        prompt: {prompt}
      </div>
      {guesses.map((g, i) => {
        const a = ease(ramp(t, 0.14 + i * 0.07, 0.24 + i * 0.07));
        const on = i === lockedIndex && lock > 0.5;
        return (
          <Card key={g} accent={on} style={{
            left: S.x + (P ? 0 : i * (gW + gap)), top: gTop + (P ? i * (gH + gap) : 0), width: gW, height: gH,
            display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 16,
            background: on ? CLAUDE.SPARK : CLAUDE.CARD, fontFamily: P ? SANS : SERIF, fontSize: P ? 70 : 50,   // portrait: 9:16 GATE T floor
            color: on ? CLAUDE.CARD : CLAUDE.INK, opacity: a * (i === lockedIndex ? 1 : 1 - lock * 0.5),
          }}>
            <span style={{ fontFamily: SANS, fontSize: 40, opacity: 1 - lock }}>?</span>{g}
          </Card>
        );
      })}
      <div style={{
        position: 'absolute', left: S.x, top: specTop, width: S.w, fontFamily: MONO, fontSize: P ? 66 : 46, lineHeight: 1.2,
        color: CLAUDE.INK, opacity: specIn, borderLeft: `8px solid ${CLAUDE.SPARK}`, paddingLeft: 24,
      }}>{spec}</div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// SpecReview — the change is checked against the spec, line by line
// ===========================================================================
export const specReviewSchema = z.object({
  title: z.string().default('Review against the spec'),
  items: z.array(z.object({ text: z.string(), ok: z.boolean() })).default([
    { text: 'email and password sign-in', ok: true },
    { text: 'lock after 5 failed tries', ok: false },
    { text: 'no third-party auth', ok: true },
  ]),
  diffLabel: z.string().default('diff: +84 −12 lines'),
  sparkLine: z.string().default('Check intent, not guesses.'),
  durationSeconds: z.number().optional(),
});
export const specReviewMeta = durMeta(5);
export const SpecReview: React.FC<z.infer<typeof specReviewSchema>> = ({ title, items, diffLabel, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 330 : 270;
  const rowH = P ? 250 : 140;   // portrait: text wraps above its mark
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, fontFamily: MONO, fontSize: 42, color: CLAUDE.INK_SOFT, opacity: ease(ramp(t, 0.04, 0.12)) }}>
        {diffLabel} · checked against spec.md
      </div>
      {items.map((it, i) => {
        const a = ease(ramp(t, 0.12 + i * 0.08, 0.22 + i * 0.08));
        const mark = ease(ramp(t, 0.4 + i * 0.1, 0.48 + i * 0.1));
        return (
          <Card key={it.text} accent={!it.ok && mark > 0.5} style={{
            left: S.x, top: top + 100 + i * (rowH + 24), width: S.w, height: rowH, padding: P ? '0 30px' : '0 44px',
            display: 'flex', flexDirection: P ? 'column' : 'row', alignItems: P ? 'flex-start' : 'center',
            justifyContent: P ? 'center' : 'space-between', gap: P ? 8 : 20, opacity: a,
          }}>
            <span style={{ fontFamily: P ? SANS : SERIF, fontSize: P ? 70 : 54, lineHeight: 1.1, color: CLAUDE.INK }}>{it.text}</span>
            <span style={{
              fontFamily: SANS, fontSize: P ? 48 : 46, whiteSpace: 'nowrap', opacity: mark,
              color: it.ok ? CLAUDE.INK : ACC_TEXT,
            }}>{it.ok ? '✓ matches' : '✕ missing'}</span>
          </Card>
        );
      })}
      <Note x={S.x} y={top + 100 + items.length * (rowH + 24) + 10} w={S.w} a={ease(ramp(t, 0.7, 0.8))} text="illustrative review" />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// SpecVersions — the spec is versioned beside the code; context survives
// ===========================================================================
export const specVersionsSchema = z.object({
  title: z.string().default('The spec travels with the code'),
  commits: z.array(z.object({ who: z.string(), spec: z.string() })).default([
    { who: 'session 1', spec: 'spec.md v1' },
    { who: 'session 2', spec: 'spec.md v2' },
    { who: 'new teammate', spec: 'spec.md v3' },
  ]),
  sparkLine: z.string().default('Context stays in the repo.'),
  durationSeconds: z.number().optional(),
});
export const specVersionsMeta = durMeta(5);
export const SpecVersions: React.FC<z.infer<typeof specVersionsSchema>> = ({ title, commits, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 450 : 380;   // portrait title wraps to two lines
  const n = commits.length;
  const line = ease(ramp(t, 0.06, 0.5));
  // landscape: commits left→right on a horizontal line; portrait: top→bottom
  const span = P ? 720 : S.w - 520;
  const pos = (i: number) => (n === 1 ? 0 : (i / (n - 1)) * span);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{
        position: 'absolute', background: CLAUDE.INK_SOFT,
        ...(P ? { left: S.x + 30, top: top + 20, width: 6, height: span * line }
              : { left: S.x + 40, top: top + 39, height: 6, width: span * line }),
      }} />
      {commits.map((c, i) => {
        const a = ease(ramp(t, 0.12 + i * 0.14, 0.22 + i * 0.14));
        const last = i === n - 1;
        const x = P ? S.x : S.x + pos(i);
        const y = P ? top + pos(i) : top;
        return (
          <div key={c.who} style={{ position: 'absolute', left: x, top: y, opacity: a, width: P ? S.w : 520 }}>
            <div style={{
              width: 84, height: 84, borderRadius: 999, marginLeft: P ? 0 : 10,
              background: last ? ACC_TEXT : CLAUDE.CARD, border: `5px solid ${last ? ACC_TEXT : CLAUDE.INK_SOFT}`,
              boxSizing: 'border-box',
            }} />
            <div style={{ position: P ? 'absolute' : 'static', left: 110, top: -6, marginTop: P ? 0 : 26 }}>
              <div style={{ fontFamily: SANS, fontSize: P ? 44 : 50, color: CLAUDE.INK_SOFT }}>{c.who}</div>
              <div style={{ display: 'flex', gap: 14, marginTop: 12 }}>
                <span style={{ fontFamily: MONO, fontSize: P ? 42 : 46, whiteSpace: 'nowrap', color: CLAUDE.INK, padding: '10px 18px', border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 10, background: CLAUDE.CARD }}>code</span>
                <span style={{ fontFamily: MONO, fontSize: P ? 42 : 46, whiteSpace: 'nowrap', color: ACC_TEXT, padding: '10px 18px', border: `2px solid ${ACC_TEXT}`, borderRadius: 10, background: CLAUDE.CARD }}>{c.spec}</span>
              </div>
            </div>
          </div>
        );
      })}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// SpecDrift — generated code not in the spec is flagged on sight
// ===========================================================================
export const specDriftSchema = z.object({
  title: z.string().default('Drift is visible'),
  fns: z.array(z.object({ name: z.string(), inSpec: z.boolean() })).default([
    { name: 'sign_in()', inSpec: true },
    { name: 'lock_account()', inSpec: true },
    { name: 'reset_password()', inSpec: true },
    { name: 'track_analytics()', inSpec: false },
  ]),
  sparkLine: z.string().default('Not in the spec? Flag it.'),
  durationSeconds: z.number().optional(),
});
export const specDriftMeta = durMeta(5);
export const SpecDrift: React.FC<z.infer<typeof specDriftSchema>> = ({ title, fns, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 330 : 260;
  const rowH = P ? 150 : 118;
  const flag = ease(ramp(t, 0.5, 0.6));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, fontFamily: SANS, fontSize: 38, color: CLAUDE.INK_SOFT }}>generated code</div>
      {fns.map((f, i) => {
        const a = ease(ramp(t, 0.08 + i * 0.07, 0.18 + i * 0.07));
        const bad = !f.inSpec && flag > 0.4;
        return (
          <Card key={f.name} accent={bad} style={{
            left: S.x, top: top + 70 + i * (rowH + 20), width: S.w, height: rowH, padding: P ? '0 30px' : '0 44px',
            display: 'flex', alignItems: 'center', justifyContent: 'space-between', opacity: a,
            background: bad ? 'rgba(217,119,87,0.08)' : CLAUDE.CARD,
          }}>
            <span style={{ fontFamily: MONO, fontSize: P ? 46 : 52, color: CLAUDE.INK }}>{f.name}</span>
            <span style={{ fontFamily: SANS, fontSize: P ? 38 : 44, color: f.inSpec ? CLAUDE.INK_SOFT : ACC_TEXT, opacity: f.inSpec ? a : flag }}>
              {f.inSpec ? '✓ in spec' : '✕ not in spec'}
            </span>
          </Card>
        );
      })}
      <Note x={S.x} y={top + 70 + fns.length * (rowH + 20) + 6} w={S.w} a={flag} text="illustrative code" />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// SpecScale — qualitative curves: prompt-only breakage climbs, spec-driven stays low
// ===========================================================================
export const specScaleSchema = z.object({
  title: z.string().default('Fast, and maintainable'),
  xLabel: z.string().default('project size →'),
  yLabel: z.string().default('things breaking'),
  vibeLabel: z.string().default('prompt-only'),
  specLabel: z.string().default('spec-driven'),
  note: z.string().default('qualitative sketch, not data'),
  sparkLine: z.string().default('Demo to maintainable.'),
  durationSeconds: z.number().optional(),
});
export const specScaleMeta = durMeta(5);
export const SpecScale: React.FC<z.infer<typeof specScaleSchema>> = ({ title, xLabel, yLabel, vibeLabel, specLabel, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 360 : 270;
  const W = P ? S.w - 100 : S.w - 360;   // headroom for the round line cap
  const H = P ? 700 : 560;
  const ox = S.x + 60, oy = top + H;
  const draw = ease(ramp(t, 0.1, 0.6));
  const lab = ease(ramp(t, 0.6, 0.7));
  // y = breakage (0 bottom → 1 top) over x = size (0 → 1)
  const vibe = (x: number) => 0.08 + 0.85 * Math.pow(x, 2.4);
  const spec = (x: number) => 0.1 + 0.16 * x;
  const path = (f: (x: number) => number) => {
    const pts: string[] = [];
    const steps = 40;
    for (let i = 0; i <= steps * draw; i++) {
      const x = i / steps;
      pts.push(`${(ox + x * W).toFixed(1)},${(oy - f(x) * H).toFixed(1)}`);
    }
    return pts.length > 1 ? `M${pts.join(' L')}` : '';
  };
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <svg width={P ? 1080 : 1920} height={P ? 1920 : 1080} style={{ position: 'absolute', left: 0, top: 0 }}>
        <line x1={ox} y1={oy} x2={ox + W} y2={oy} stroke={CLAUDE.INK_SOFT} strokeWidth={4} />
        <line x1={ox} y1={oy} x2={ox} y2={top} stroke={CLAUDE.INK_SOFT} strokeWidth={4} />
        <path d={path(vibe)} fill="none" stroke={CLAUDE.INK_SOFT} strokeWidth={10} strokeLinecap="round" />
        <path d={path(spec)} fill="none" stroke={ACC_TEXT} strokeWidth={12} strokeLinecap="round" />
      </svg>
      <div style={{ position: 'absolute', left: ox + W - 280, top: oy + 20, width: 300, textAlign: 'right', fontFamily: SANS, fontSize: 38, color: CLAUDE.INK_SOFT }}>{xLabel}</div>
      <div style={{ position: 'absolute', left: ox + 24, top: top - 10, fontFamily: SANS, fontSize: 38, color: CLAUDE.INK_SOFT }}>{yLabel}</div>
      <div style={{
        position: 'absolute', opacity: lab, fontFamily: SERIF, fontSize: P ? 50 : 54, color: CLAUDE.INK,
        ...(P ? { left: ox + W - 330, top: oy - vibe(1) * H + 10 } : { left: ox + W + 30, top: oy - vibe(1) * H - 30 }),
      }}>{vibeLabel}</div>
      <div style={{
        position: 'absolute', opacity: lab, fontFamily: SERIF, fontSize: P ? 50 : 54, color: ACC_TEXT,
        ...(P ? { left: ox + W - 290, top: oy - spec(1) * H - 80 } : { left: ox + W + 30, top: oy - spec(1) * H - 34 }),
      }}>{specLabel}</div>
      <Note x={S.x} y={oy + (P ? 80 : 70)} w={S.w} a={lab} text={note} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
