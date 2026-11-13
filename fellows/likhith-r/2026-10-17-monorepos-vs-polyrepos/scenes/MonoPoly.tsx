/**
 * MonoPoly.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-monorepos-polyrepos ("Monorepos vs. Polyrepos", @HumanitariansAI).
 *
 * Same contract as KvCache.tsx / JevExplainer.tsx (whose stage helpers it reuses):
 * each component lays out natively for 16:9 (<Name>) and 9:16 (<Name>916) — never a
 * crop — and every motion is a pure function of progress, conformed via `durationSeconds`.
 * Google's figures come from Potvin & Levenberg, CACM 2016 (Jan 2015 snapshot).
 * The commit, sparse-checkout counts and cache hits/misses are recorded output of the
 * reel's evidence/mono_demo.sh and evidence/build_cache_toy.py. Project names are a toy repo.
 *
 *   MpHook    — Google: ~2 billion lines, 25,000+ developers, one repository
 *   MpPoly    — one repo per project: own team, own history, own CI
 *   MpMono    — one repo for everything: shared history, shared tooling
 *   MpAtomic  — many PRs + version drift vs. one atomic commit across three projects
 *   MpSlow    — a plain clone + full build: fine when small, crawls when huge
 *   MpSparse  — git sparse-checkout: only two folders land on disk (102 of 403 files)
 *   MpCache   — remote build cache: build, reuse on a new laptop, rebuild only dependents
 */
import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ACC_TEXT, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';

const Path: React.FC<{ p: string }> = ({ p }) => {
  const i = p.indexOf('/');
  return i < 0 ? <>{p}</> : <span style={{ textAlign: 'center', lineHeight: 1.15 }}><span style={{ color: CLAUDE.INK_SOFT }}>{p.slice(0, i + 1)}</span><br />{p.slice(i + 1)}</span>;
};

const Small: React.FC<{ text: string; style?: React.CSSProperties }> = ({ text, style }) => (
  <div style={{ position: 'absolute', fontFamily: SANS, fontSize: 34, color: CLAUDE.INK_SOFT, ...style }}>{text}</div>
);

// a little commit-history strip: dots on a line, each popping in at its own time
const History: React.FC<{ n: number; w: number; at: (i: number) => number; t: number; r: number }> = ({ n, w, at, t, r }) => (
  <div style={{ position: 'relative', width: w, height: r * 2 }}>
    <div style={{ position: 'absolute', left: 0, top: r - 2, width: w, height: 4, background: CLAUDE.BORDER }} />
    {Array.from({ length: n }, (_, i) => {
      const a = ease(ramp(t, at(i), at(i) + 0.05));
      return <div key={i} style={{
        position: 'absolute', left: (i + 0.5) * (w / n) - r, top: 0, width: r * 2, height: r * 2, borderRadius: r,
        background: CLAUDE.INK_SOFT, opacity: a, transform: `scale(${0.4 + 0.6 * a})`,
      }} />;
    })}
  </div>
);

// ===========================================================================
// MpHook — Google keeps ~2 billion lines from 25,000+ developers in one repo
// ===========================================================================
export const mpHookSchema = z.object({
  title: z.string().default('Google’s codebase'),
  lines: z.number().default(2),
  linesLabel: z.string().default('billion lines of code'),
  devs: z.number().default(25000),
  devsLabel: z.string().default('developers'),
  repoLabel: z.string().default('one repository'),
  source: z.string().default('Jan 2015 · Potvin & Levenberg, CACM 2016'),
  sparkLine: z.string().default('Why just one?'),
  durationSeconds: z.number().optional(),
});
export const mpHookMeta = durMeta(5);
export const MpHook: React.FC<z.infer<typeof mpHookSchema>> = ({ title, lines, linesLabel, devs, devsLabel, repoLabel, source, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 330 : 250;
  const l = ease(ramp(t, 0.06, 0.4));
  const d = ease(ramp(t, 0.2, 0.5));
  const statW = P ? S.w : 720;
  // the repository box: the developers (dots) all land inside the same one
  const boxX = P ? S.x : S.x + statW + 60;
  const boxY = P ? top + 470 : top;
  const boxW = P ? S.w : S.w - statW - 60;
  const boxH = P ? 480 : 640;
  const cols = P ? 12 : 12, rows = P ? 6 : 8;
  const dot = P ? 26 : 30;
  const glow = ease(ramp(t, 0.58, 0.66));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, width: P ? S.w / 2 - 20 : statW, opacity: ease(ramp(t, 0.04, 0.1)) }}>
        <div style={{ fontFamily: SERIF, fontSize: P ? 150 : 170, lineHeight: 1, color: CLAUDE.INK }}>≈{(lines * l).toFixed(1)}</div>
        <div style={{ fontFamily: SANS, fontSize: P ? 52 : 46, color: CLAUDE.INK, marginTop: 8 }}>{linesLabel}</div>
      </div>
      <div style={{ position: 'absolute', left: P ? S.x + S.w / 2 + 20 : S.x, top: P ? top : top + 270, width: P ? S.w / 2 - 20 : statW, opacity: ease(ramp(t, 0.18, 0.24)) }}>
        <div style={{ fontFamily: SERIF, fontSize: P ? 150 : 170, lineHeight: 1, color: CLAUDE.INK }}>{Math.round((devs * d) / 1000)}k+</div>
        <div style={{ fontFamily: SANS, fontSize: P ? 52 : 46, color: CLAUDE.INK, marginTop: 8 }}>{devsLabel}</div>
      </div>
      <Small text={source} style={{ left: S.x, top: P ? top + 260 : top + 530, width: statW, fontSize: P ? 40 : 34, opacity: ease(ramp(t, 0.3, 0.38)) }} />
      <Card accent={glow > 0.5} style={{ left: boxX, top: boxY, width: boxW, height: boxH, opacity: ease(ramp(t, 0.08, 0.16)) }}>
        <div style={{ position: 'absolute', left: 0, right: 0, top: P ? 40 : 48, display: 'grid', justifyContent: 'center',
          gridTemplateColumns: `repeat(${cols}, ${dot}px)`, gap: P ? 22 : 18 }}>
          {Array.from({ length: cols * rows }, (_, i) => {
            const a = ease(ramp(t, 0.2 + (i / (cols * rows)) * 0.32, 0.26 + (i / (cols * rows)) * 0.32));
            return <div key={i} style={{ width: dot, height: dot, borderRadius: dot / 2, background: CLAUDE.INK_SOFT, opacity: 0.3 + 0.6 * a,
              transform: `translateY(${(1 - a) * -30}px)` }} />;
          })}
        </div>
        <div style={{ position: 'absolute', left: 0, right: 0, bottom: P ? 34 : 40, textAlign: 'center', fontFamily: SERIF,
          fontSize: P ? 84 : 76, color: glow > 0.5 ? ACC_TEXT : CLAUDE.INK }}>{repoLabel}</div>
      </Card>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MpPoly — every project its own repository, team, history and CI
// ===========================================================================
export const mpPolySchema = z.object({
  title: z.string().default('Polyrepo: one repo per project'),
  repos: z.array(z.object({ name: z.string(), team: z.string() })).default([
    { name: 'web.git', team: 'Web team' }, { name: 'mobile.git', team: 'Mobile team' },
    { name: 'billing.git', team: 'Billing team' }, { name: 'search.git', team: 'Search team' },
  ]),
  footer: z.string().default('own history · own CI · own releases'),
  sparkLine: z.string().default('Own repo, own rules.'),
  durationSeconds: z.number().optional(),
});
export const mpPolyMeta = durMeta(5);
export const MpPoly: React.FC<z.infer<typeof mpPolySchema>> = ({ title, repos, footer, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const n = repos.length;
  const top = P ? 330 : 250;
  const gap = P ? 36 : 44;
  const perRow = P ? 2 : n;
  const cw = (S.w - gap * (perRow - 1)) / perRow;
  const ch = P ? 420 : 520;
  const own = ease(ramp(t, 0.55, 0.65));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {repos.map((r, i) => {
        const a = ease(ramp(t, 0.06 + i * 0.08, 0.16 + i * 0.08));
        const x = S.x + (i % perRow) * (cw + gap);
        const y = top + Math.floor(i / perRow) * (ch + gap);
        // each repo's history ticks on its own clock — teams don't wait on each other
        const offs = [0.1, 0.26, 0.04, 0.18][i % 4];
        return (
          <Card key={r.name} style={{ left: x, top: y, width: cw, height: ch, opacity: a, transform: `translateY(${(1 - a) * 24}px)`,
            padding: P ? '30px 30px' : '34px 30px', display: 'flex', flexDirection: 'column', gap: P ? 30 : 40 }}>
            <div style={{ fontFamily: MONO, fontSize: P ? 50 : 46, color: CLAUDE.INK }}>{r.name}</div>
            <div style={{ alignSelf: 'flex-start', background: CLAUDE.PILL, borderRadius: 30, padding: '10px 24px',
              fontFamily: SANS, fontSize: P ? 50 : 38, color: CLAUDE.INK }}>{r.team}</div>
            <History n={5} w={cw - 60} r={P ? 18 : 22} t={t} at={(k) => 0.2 + offs + k * 0.11} />
            <div style={{ fontFamily: SANS, fontSize: P ? 50 : 40, color: CLAUDE.INK_SOFT }}>own history</div>
          </Card>
        );
      })}
      {/* walls between repos: the ownership boundary */}
      {!P && repos.slice(1).map((_, i) => (
        <div key={i} style={{ position: 'absolute', left: S.x + (i + 1) * (cw + gap) - gap / 2 - 3, top: top - 10, width: 6, height: ch + 20,
          borderLeft: `6px dashed ${CLAUDE.SPARK}`, opacity: own }} />
      ))}
      {P && <>
        <div style={{ position: 'absolute', left: S.x + cw + gap / 2 - 3, top: top - 10, height: 2 * ch + gap + 20, borderLeft: `6px dashed ${CLAUDE.SPARK}`, opacity: own }} />
        <div style={{ position: 'absolute', top: top + ch + gap / 2 - 3, left: S.x, width: S.w, borderTop: `6px dashed ${CLAUDE.SPARK}`, opacity: own }} />
      </>}
      {!P && <div style={{ position: 'absolute', left: S.x, top: top + ch + 40, width: S.w, fontFamily: SERIF, fontSize: 56, color: CLAUDE.INK, opacity: own }}>{footer}</div>}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MpMono — every project in one repository: one shared history, one toolchain
// ===========================================================================
export const mpMonoSchema = z.object({
  title: z.string().default('Monorepo: one repo for everything'),
  repoName: z.string().default('company.git'),
  folders: z.array(z.string()).default(['apps/web', 'apps/mobile', 'services/billing', 'libs/auth']),
  // which folder each commit on the shared history touches
  touches: z.array(z.number()).default([0, 3, 1, 2, 0, 3, 2, 1]),
  historyLabel: z.string().default('one shared history'),
  tools: z.array(z.string()).default(['one build', 'one test runner', 'one set of rules']),
  sparkLine: z.string().default('One repo, one history.'),
  durationSeconds: z.number().optional(),
});
export const mpMonoMeta = durMeta(5);
export const MpMono: React.FC<z.infer<typeof mpMonoSchema>> = ({ title, repoName, folders, touches, historyLabel, tools, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const n = folders.length;
  const top = P ? 320 : 230;
  const pad = P ? 28 : 36;
  const perRow = P ? 2 : n;
  const fg = P ? 24 : 28;
  const fw = (S.w - 2 * pad - fg * (perRow - 1)) / perRow;
  const fh = P ? 150 : 150;
  const fRows = Math.ceil(n / perRow);
  const histY = top + pad + 70 + fRows * (fh + fg) + (P ? 30 : 30);
  const boxH = histY - top + (P ? 150 : 140);
  const cAt = (i: number) => 0.22 + i * 0.065;
  // which folder the newest landed commit touched (flashes as the commit lands)
  const flash = (f: number) => touches.reduce((m, tf, i) => (tf === f ? Math.max(m, 1 - Math.abs((t - cAt(i) - 0.02) / 0.05)) : m), 0);
  const toolsY = top + boxH + (P ? 50 : 40);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: S.x, top, width: S.w, height: boxH, opacity: ease(ramp(t, 0.04, 0.12)) }}>
        <div style={{ position: 'absolute', left: pad, top: pad - 6, fontFamily: MONO, fontSize: P ? 50 : 44, color: CLAUDE.INK }}>{repoName}</div>
      </Card>
      {folders.map((f, i) => {
        const a = ease(ramp(t, 0.08 + i * 0.04, 0.16 + i * 0.04));
        const x = S.x + pad + (i % perRow) * (fw + fg);
        const y = top + pad + 70 + Math.floor(i / perRow) * (fh + fg);
        const fl = flash(i);
        return (
          <div key={f} style={{ position: 'absolute', left: x, top: y, width: fw, height: fh, borderRadius: 12, boxSizing: 'border-box',
            border: `3px solid ${CLAUDE.BORDER}`, background: `rgba(115,112,95,${0.04 + 0.08 * fl})`, borderColor: fl > 0.3 ? CLAUDE.INK_SOFT : CLAUDE.BORDER, opacity: a,
            display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: MONO, fontSize: P ? 44 : 38, color: CLAUDE.INK }}>{f}</div>
        );
      })}
      <div style={{ position: 'absolute', left: S.x + pad, top: histY }}>
        <History n={touches.length} w={S.w - 2 * pad} r={18} t={t} at={cAt} />
      </div>
      <Small text={historyLabel} style={{ left: S.x + pad, top: histY + 54, fontSize: P ? 50 : 40, color: CLAUDE.INK, opacity: ease(ramp(t, 0.24, 0.32)) }} />
      <div style={{ position: 'absolute', left: S.x, top: toolsY, width: S.w, display: 'flex', flexWrap: 'wrap', gap: P ? 22 : 28 }}>
        {tools.map((tl, i) => (
          <div key={tl} style={{ background: CLAUDE.PILL, borderRadius: 40, padding: P ? '14px 30px' : '14px 34px', fontFamily: SANS,
            fontSize: P ? 50 : 42, color: CLAUDE.INK, opacity: ease(ramp(t, 0.6 + i * 0.05, 0.68 + i * 0.05)) }}>{tl}</div>
        ))}
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MpAtomic — many PRs that drift apart vs. one commit that changes every caller
// ===========================================================================
export const mpAtomicSchema = z.object({
  title: z.string().default('One change, every caller'),
  manyLabel: z.string().default('Many repos'),
  manyRows: z.array(z.object({ repo: z.string(), uses: z.string() })).default([
    { repo: 'auth.git', uses: 'v2 released' }, { repo: 'web.git', uses: 'on auth v2' }, { repo: 'mobile.git', uses: 'still on auth v1' },
  ]),
  manyNote: z.string().default('3 PRs, landing on 3 timelines'),
  oneLabel: z.string().default('One repo'),
  commit: z.string().default('commit a8f51ce'),
  message: z.string().default('auth: rename login to signIn'),
  files: z.array(z.string()).default(['libs/auth/index.ts', 'apps/web/main.ts', 'apps/mobile/main.ts']),
  oneNote: z.string().default('1 commit · 3 projects · 1 version of auth'),
  source: z.string().default('recorded git output · evidence/mono_demo.sh'),
  sparkLine: z.string().default('One commit, every caller.'),
  durationSeconds: z.number().optional(),
});
export const mpAtomicMeta = durMeta(6);
export const MpAtomic: React.FC<z.infer<typeof mpAtomicSchema>> = ({ title, manyLabel, manyRows, manyNote, oneLabel, commit, message, files, oneNote, source, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 320 : 240;
  const colW = P ? S.w : (S.w - 70) / 2;
  const rowH = P ? 84 : 124;
  const leftX = S.x;
  const rightX = P ? S.x : S.x + colW + 70;
  const rightTop = P ? top + 80 + manyRows.length * (rowH + 14) + 40 : top;
  const land = ease(ramp(t, 0.36, 0.44));             // the one commit lands everywhere at once
  const drift = ease(ramp(t, 0.5, 0.58));
  const fileH = P ? 56 : 76;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {/* LEFT / TOP — polyrepo: the same change is three PRs that land at different times */}
      <div style={{ position: 'absolute', left: leftX, top, fontFamily: SERIF, fontSize: P ? 64 : 56, color: CLAUDE.INK, opacity: ease(ramp(t, 0.02, 0.08)) }}>{manyLabel}</div>
      {manyRows.map((r, i) => {
        const a = ease(ramp(t, 0.06 + i * 0.12, 0.14 + i * 0.12));
        const late = i === manyRows.length - 1;
        return (
          <Card key={r.repo} accent={late && drift > 0.5} style={{ left: leftX, top: top + 80 + i * (rowH + 14), width: colW, height: rowH, opacity: 0.4 + 0.6 * a,
            display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '0 26px' }}>
            <span style={{ fontFamily: MONO, fontSize: P ? 44 : 38, color: CLAUDE.INK }}>{r.repo}</span>
            <span style={{ fontFamily: SANS, fontSize: P ? 46 : 38, color: late && drift > 0.5 ? ACC_TEXT : CLAUDE.INK_SOFT }}>{r.uses}</span>
          </Card>
        );
      })}
      {!P && <Small text={manyNote} style={{ left: leftX, top: top + 80 + manyRows.length * (rowH + 14) + 8, width: colW, fontSize: P ? 46 : 38, opacity: ease(ramp(t, 0.3, 0.36)) }} />}
      {/* RIGHT / BOTTOM — monorepo: the recorded commit touching three projects */}
      <div style={{ position: 'absolute', left: rightX, top: rightTop, fontFamily: SERIF, fontSize: P ? 64 : 56, color: CLAUDE.INK, opacity: ease(ramp(t, 0.24, 0.3)) }}>{oneLabel}</div>
      <Card style={{ left: rightX, top: rightTop + 80, width: colW, padding: P ? '24px 28px' : '26px 30px', opacity: ease(ramp(t, 0.26, 0.34)) }}>
        <div style={{ fontFamily: MONO, fontSize: P ? 44 : 38, color: CLAUDE.INK }}>{commit}</div>
        <div style={{ fontFamily: MONO, fontSize: P ? 40 : 38, color: CLAUDE.INK_SOFT, marginTop: 8 }}>{message}</div>
        {files.map((f) => (
          <div key={f} style={{ marginTop: 14, height: fileH, borderRadius: 10, display: 'flex', alignItems: 'center', padding: '0 20px',
            background: `rgba(115,112,95,${0.04 + 0.05 * land})`, borderLeft: `8px solid ${land > 0.5 ? CLAUDE.SPARK : CLAUDE.BORDER}`,
            fontFamily: MONO, fontSize: P ? 42 : 40, color: CLAUDE.INK }}>{f}</div>
        ))}
      </Card>
      <div style={{ position: 'absolute', left: rightX, top: rightTop + 80 + (P ? 140 : 150) + files.length * (fileH + 14) + (P ? 14 : 24), width: colW,
        fontFamily: SANS, fontSize: P ? 46 : 42, color: CLAUDE.INK, opacity: drift }}>✓ {oneNote}</div>
      <Small text={source} style={{ left: rightX, top: rightTop + 80 + (P ? 140 : 150) + files.length * (fileH + 14) + (P ? 76 : 80), width: colW,
        fontSize: P ? 40 : 30, opacity: ease(ramp(t, 0.6, 0.66)) }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MpSlow — the same plain clone + full build: quick when small, crawls when huge
// ===========================================================================
export const mpSlowSchema = z.object({
  title: z.string().default('The catch: scale'),
  rows: z.array(z.object({ label: z.string(), size: z.string(), rate: z.number() })).default([
    { label: 'small repo', size: 'a few projects', rate: 1 },
    { label: 'giant repo', size: 'every project, all history', rate: 0.09 },
  ]),
  steps: z.array(z.string()).default(['git clone', 'full build']),
  note: z.string().default('illustrative · plain git, rebuild everything'),
  sparkLine: z.string().default('Fine small. Slow huge.'),
  durationSeconds: z.number().optional(),
});
export const mpSlowMeta = durMeta(5);
export const MpSlow: React.FC<z.infer<typeof mpSlowSchema>> = ({ title, rows, steps, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 330 : 250;
  const blockH = P ? 440 : 290;
  const labelW = P ? 0 : 330;
  const barX = S.x + labelW;
  const barW = S.w - labelW;
  const barH = P ? 48 : 44;
  const run = ramp(t, 0.12, 0.9);
  const spin = ['◐', '◓', '◑', '◒'][Math.floor(t * 40) % 4];
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {rows.map((r, ri) => {
        const y = top + ri * (blockH + (P ? 40 : 30));
        const a = ease(ramp(t, 0.04 + ri * 0.08, 0.12 + ri * 0.08));
        const big = ri === rows.length - 1;
        return (
          <React.Fragment key={r.label}>
            <div style={{ position: 'absolute', left: S.x, top: y, width: P ? S.w : labelW - 30, opacity: a }}>
              <div style={{ fontFamily: SERIF, fontSize: P ? 72 : 60, color: CLAUDE.INK, lineHeight: 1.05 }}>{r.label}</div>
              <div style={{ fontFamily: SANS, fontSize: P ? 48 : 34, color: CLAUDE.INK_SOFT, marginTop: 8 }}>{r.size}</div>
            </div>
            {steps.map((s, si) => {
              const p = Math.min(1, ramp(t, 0.12 + si * (big ? 0.2 : 0.18), 0.32 + si * (big ? 0.2 : 0.18)) * (big ? r.rate * 2.2 : 1));
              const done = !big && p >= 1;
              const by = y + (P ? 170 : 14) + si * (barH + (P ? 100 : 92));
              return (
                <React.Fragment key={s}>
                  <div style={{ position: 'absolute', left: barX, top: by, fontFamily: MONO, fontSize: P ? 44 : 36, color: CLAUDE.INK, opacity: a }}>
                    {s}{big && run > 0.05 ? `  ${spin} still running…` : done ? '  ✓ done' : ''}
                  </div>
                  <div style={{ position: 'absolute', left: barX, top: by + (P ? 62 : 54), width: barW, height: barH, borderRadius: barH / 2,
                    background: CLAUDE.PILL, opacity: a, overflow: 'hidden' }}>
                    <div style={{ width: `${p * 100}%`, height: '100%', borderRadius: barH / 2, background: big ? CLAUDE.SPARK : CLAUDE.INK_SOFT }} />
                  </div>
                </React.Fragment>
              );
            })}
          </React.Fragment>
        );
      })}
      <Small text={note} style={{ left: S.x, top: top + rows.length * (blockH + (P ? 40 : 30)) - (P ? 10 : 20), width: S.w, fontSize: P ? 40 : 32, opacity: ease(ramp(t, 0.4, 0.48)) }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MpSparse — git sparse-checkout: only the folders you ask for land on disk
// ===========================================================================
export const mpSparseSchema = z.object({
  title: z.string().default('Fix 1: sparse checkout'),
  command: z.string().default('git sparse-checkout set apps/web libs/auth'),
  folders: z.array(z.string()).default(['apps/web', 'apps/mobile', 'services/billing', 'services/search', 'services/ads', 'libs/auth', 'libs/ui', 'tools/ci']),
  picked: z.array(z.string()).default(['apps/web', 'libs/auth']),
  onDisk: z.number().default(102),
  total: z.number().default(403),
  countLabel: z.string().default('files on disk'),
  skipLabel: z.string().default('not downloaded'),
  source: z.string().default('recorded output · evidence/mono_demo.sh'),
  sparkLine: z.string().default('Only what you need.'),
  durationSeconds: z.number().optional(),
});
export const mpSparseMeta = durMeta(5);
export const MpSparse: React.FC<z.infer<typeof mpSparseSchema>> = ({ title, command, folders, picked, onDisk, total, countLabel, skipLabel, source, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 320 : 240;
  const gridW = P ? S.w : 1120;
  const perRow = P ? 2 : 4;
  const g = P ? 20 : 22;
  const tw = (gridW - g * (perRow - 1)) / perRow;
  const th = P ? 100 : 190;
  const cmdH = P ? 170 : 96;
  const gridTop = top + cmdH + (P ? 230 : 44);
  const typed = Math.floor(ramp(t, 0.04, 0.28) * command.length);
  const sel = ease(ramp(t, 0.32, 0.42));
  const n = Math.round(onDisk * ease(ramp(t, 0.36, 0.56)));
  const cx = P ? S.x : S.x + gridW + 70;
  const cy = P ? top + cmdH + 30 : gridTop;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: S.x, top, width: S.w, height: cmdH, padding: P ? '22px 28px' : '0 30px', display: 'flex', alignItems: 'center',
        fontFamily: MONO, fontSize: P ? 46 : 42, color: CLAUDE.INK, lineHeight: 1.35, opacity: ease(ramp(t, 0, 0.06)) }}>
        <span><span style={{ color: CLAUDE.INK_SOFT }}>$ </span>{command.slice(0, typed)}</span>
      </Card>
      {folders.map((f, i) => {
        const on = picked.includes(f);
        const a = ease(ramp(t, 0.1 + i * 0.02, 0.16 + i * 0.02));
        return (
          <div key={f} style={{
            position: 'absolute', left: S.x + (i % perRow) * (tw + g), top: gridTop + Math.floor(i / perRow) * (th + g), width: tw, height: th,
            borderRadius: 12, boxSizing: 'border-box',
            border: on ? `${3 + 3 * sel}px solid ${sel > 0.5 ? CLAUDE.SPARK : CLAUDE.BORDER}` : `3px dashed ${CLAUDE.GHOST}`,
            background: on ? CLAUDE.CARD : 'transparent',
            opacity: a * (on ? 1 : 1 - 0.5 * sel),                        // skipped folders stay ≥ 50%
            display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
            fontFamily: MONO, fontSize: P ? 42 : 40, color: CLAUDE.INK,
          }}><Path p={f} /></div>
        );
      })}
      <div style={{ position: 'absolute', left: cx, top: cy, width: P ? S.w : S.w - gridW - 70, opacity: ease(ramp(t, 0.34, 0.4)),
        ...(P ? { display: 'flex', alignItems: 'center', gap: 36 } : {}) }}>
        <div style={{ fontFamily: SERIF, fontSize: P ? 150 : 190, lineHeight: 1, color: CLAUDE.INK, flexShrink: 0 }}>
          {n}<span style={{ fontSize: P ? 70 : 80, color: CLAUDE.INK_SOFT }}> / {total}</span>
        </div>
        <div>
          <div style={{ fontFamily: SANS, fontSize: P ? 50 : 44, color: CLAUDE.INK, marginTop: 12 }}>{countLabel}</div>
          <div style={{ fontFamily: SANS, fontSize: P ? 44 : 36, color: CLAUDE.INK_SOFT, marginTop: 14, opacity: sel }}>dashed = {skipLabel}</div>
        </div>
      </div>
      <Small text={source} style={{ left: P ? S.x : cx, top: P ? gridTop + 4 * (th + g) + 10 : cy + 400, width: P ? S.w : S.w - gridW - 70,
        fontSize: P ? 40 : 30, opacity: ease(ramp(t, 0.5, 0.56)) }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MpCache — remote build cache: build once, reuse anywhere, rebuild only what changed
// ===========================================================================
const cachePhase = z.object({ label: z.string(), built: z.array(z.string()) });
export const mpCacheSchema = z.object({
  title: z.string().default('Fix 2: remote build cache'),
  targets: z.array(z.string()).default(['libs/auth', 'libs/ui', 'apps/web', 'apps/mobile', 'services/billing', 'services/search', 'services/ads', 'tools/ci']),
  phases: z.array(cachePhase).default([
    { label: 'build 1 · empty cache', built: ['libs/auth', 'libs/ui', 'apps/web', 'apps/mobile', 'services/billing', 'services/search', 'services/ads', 'tools/ci'] },
    { label: 'build 2 · new laptop, same code', built: [] },
    { label: 'build 3 · edit libs/auth', built: ['libs/auth', 'apps/web', 'apps/mobile', 'services/billing'] },
  ]),
  edited: z.string().default('libs/auth'),
  source: z.string().default('recorded output · evidence/build_cache_toy.py'),
  sparkLine: z.string().default('Built once, reused.'),
  durationSeconds: z.number().optional(),
});
export const mpCacheMeta = durMeta(6);
export const MpCache: React.FC<z.infer<typeof mpCacheSchema>> = ({ title, targets, phases, edited, source, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 320 : 240;
  const gridW = P ? S.w : 1160;
  const perRow = P ? 2 : 4;
  const g = P ? 20 : 22;
  const tw = (gridW - g * (perRow - 1)) / perRow;
  const th = P ? 150 : 230;
  const bounds = [0.04, 0.34, 0.6];                  // phase start times (progress)
  const ph = t < bounds[1] ? 0 : t < bounds[2] ? 1 : 2;
  const p0 = bounds[ph];
  const p1 = ph < 2 ? bounds[ph + 1] : 0.92;
  const phase = phases[ph];
  const local = ramp(t, p0 + 0.02, p1 - 0.06);
  const gridTop = top + (P ? 250 : 100);
  const builtNow = phase.built.length, reusedNow = targets.length - phase.built.length;
  const statX = P ? S.x : S.x + gridW + 70;
  const statY = P ? top + 76 : gridTop;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, fontFamily: MONO, fontSize: P ? 46 : 42, color: CLAUDE.INK, opacity: ease(ramp(t, 0.02, 0.06)) }}>
        {phase.label}
      </div>
      {targets.map((tg, i) => {
        const isBuilt = phase.built.includes(tg);
        const k = phase.built.indexOf(tg);
        // built targets fill in dependency order; reused ones snap in at the phase start
        const prog = isBuilt ? ease(ramp(local, k / Math.max(1, builtNow), (k + 1) / Math.max(1, builtNow))) : ease(ramp(t, p0, p0 + 0.05));
        const isEdit = ph === 2 && tg === edited;
        return (
          <div key={tg} style={{
            position: 'absolute', left: S.x + (i % perRow) * (tw + g), top: gridTop + Math.floor(i / perRow) * (th + g), width: tw, height: th,
            borderRadius: 12, boxSizing: 'border-box', border: `${isEdit ? 6 : 3}px ${isBuilt ? "solid" : "dashed"} ${isEdit ? CLAUDE.SPARK : isBuilt ? CLAUDE.INK_SOFT : CLAUDE.GHOST}`,
            background: isBuilt ? `rgba(115,112,95,${0.04 + 0.08 * prog})` : CLAUDE.CARD,
            display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 6,
          }}>
            <span style={{ fontFamily: MONO, fontSize: P ? 40 : 38, color: CLAUDE.INK, display: 'flex' }}><Path p={tg} /></span>
            <span style={{ fontFamily: SANS, fontSize: P ? 40 : 36, color: CLAUDE.INK_SOFT, opacity: prog }}>
              {isBuilt ? (prog < 1 ? 'building…' : 'built') : '✓ reused'}
            </span>
          </div>
        );
      })}
      <div style={{ position: 'absolute', left: statX, top: statY, width: P ? S.w : S.w - gridW - 70 }}>
        <div style={{ display: 'flex', gap: P ? 60 : 0, flexDirection: P ? 'row' : 'column' }}>
          <div>
            <div style={{ fontFamily: SERIF, fontSize: P ? 110 : 150, lineHeight: 1, color: CLAUDE.INK }}>{builtNow}</div>
            <div style={{ fontFamily: SANS, fontSize: P ? 50 : 42, color: CLAUDE.INK }}>built</div>
          </div>
          <div style={{ marginTop: P ? 0 : 30 }}>
            <div style={{ fontFamily: SERIF, fontSize: P ? 110 : 150, lineHeight: 1, color: CLAUDE.INK }}>{reusedNow}</div>
            <div style={{ fontFamily: SANS, fontSize: P ? 50 : 42, color: CLAUDE.INK }}>reused</div>
          </div>
        </div>
      </div>
      <Small text={source} style={{ left: S.x, top: P ? gridTop + 4 * (th + g) + 10 : gridTop + 2 * (th + g) + 24, width: S.w,
        fontSize: P ? 40 : 30, opacity: ease(ramp(t, 0.1, 0.16)) }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
