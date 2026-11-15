/**
 * PhysicsEngine12.tsx — body scenes for "Measure First." (physics engine, 12 of 12).
 *
 * Reel: books/physics-engine/youtube/measure-first
 * Host: Param Madan · voice Kokoro af_bella
 * Source: github.com/jashshah127/humanitariansai/physics-engine @ 2dc4aa4
 *         (PHASE2.md; MEASUREMENT.md; COVERAGE.md; EVALUATION.md; docs/Physics_Engine_Brief_v2.md).
 *
 * CONTRACT (illustrations/kit.tsx): every scene here is a pure function of
 * useP() — normalized progress across the beat's audio duration. No wall clock,
 * no state, no CSS transitions. Seeking any frame renders identically.
 *
 * COLOR: claude palette, one terracotta moment per beat. The accent marks the
 * trigger, 16/16, the scorable share, coverage, the release gate, and the baseline.
 */
import React from 'react';
import { AbsoluteFill } from 'remotion';
import { CLAUDE } from '../tokens/claude';
import { SAFE } from '../tokens/layout';
import { IlluStage, SERIF, SANS, MONO, remap, ease, useP } from '../illustrations/kit';

const INK = CLAUDE.INK;
const SOFT = CLAUDE.INK_SOFT;
const ACCENT = CLAUDE.SPARK;
const HAIR = CLAUDE.BORDER;

/** Small uppercase label that sets the frame's subject. */
const Eyebrow: React.FC<{ text: string; o: number }> = ({ text, o }) => (
  <div style={{
    fontFamily: SANS, fontSize: 34, letterSpacing: 5, color: SOFT,
    textTransform: 'uppercase', opacity: o, textAlign: 'center',
  }}>{text}</div>
);

/** A stat tile: big value over a small caption. */
const Tile: React.FC<{
  value: string; caption: string; o: number; accent?: boolean; w?: number; size?: number;
}> = ({ value, caption, o, accent = false, w = 500, size = 132 }) => (
  <div style={{
    width: w, padding: '34px 28px 30px', background: CLAUDE.CARD,
    border: `2px solid ${accent ? ACCENT : HAIR}`, opacity: o,
    transform: `translateY(${(1 - o) * 26}px)`,
    display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 12,
  }}>
    <div style={{
      fontFamily: SERIF, fontSize: size, lineHeight: 1.08,
      color: accent ? ACCENT : INK, fontWeight: 600,
    }}>{value}</div>
    <div style={{
      fontFamily: SANS, fontSize: 30, letterSpacing: 2.4, lineHeight: 1.3,
      textTransform: 'uppercase', color: SOFT, textAlign: 'center',
    }}>{caption}</div>
  </div>
);

/** The lesson line that lands at the end of a beat, under a terracotta rule. */
const RecordStrip: React.FC<{ text: string; o: number }> = ({ text, o }) => (
  <div style={{
    position: 'absolute', left: SAFE.x, width: SAFE.w, bottom: 96,
    opacity: o, transform: `translateY(${(1 - o) * 18}px)`,
    display: 'flex', justifyContent: 'center',
  }}>
    <div style={{
      borderTop: `3px solid ${ACCENT}`, paddingTop: 20, maxWidth: 1500,
      fontFamily: SERIF, fontSize: 44, lineHeight: 1.25, color: INK, textAlign: 'center',
    }}>{text}</div>
  </div>
);

/* ────────────────────────────────────────────────────────────────────────────
 * B00B — the promise. Three things this video shows.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe12Promise: React.FC<{ spark?: string; headline?: string }> = ({
  spark = 'Why watch this.',
  headline = 'Why not just train a smarter model?',
}) => {
  const p = useP();
  const head = ease(remap(p, 0.04, 0.18, 0, 1));
  const items = [
    { v: 'Golden set', c: 'how they know it’s right', hot: false },
    { v: 'Benchmark', c: 'what the outside test says', hot: false },
    { v: 'Trigger', c: 'when to fine-tune', hot: true },
  ];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 110, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 26,
      }}>
        <Eyebrow text="What this video is" o={remap(p, 0, 0.08, 0, 1)} />
        <div style={{
          fontFamily: SERIF, fontSize: 92, lineHeight: 1.12, color: INK,
          textAlign: 'center', maxWidth: 1600, fontWeight: 600,
          opacity: head, transform: `translateY(${(1 - head) * 30}px)`,
        }}>{headline}</div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 370, width: SAFE.w, height: 360,
        display: 'flex', justifyContent: 'center', gap: 34,
      }}>
        {items.map((n, i) => (
          <Tile key={n.v} value={n.v} caption={n.c} accent={n.hot} w={520} size={104}
            o={ease(remap(p, 0.16 + i * 0.2, 0.32 + i * 0.2, 0, 1))} />
        ))}
      </div>
      <RecordStrip text="No physics or coding background needed." o={remap(p, 0.84, 0.94, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B01 — the BLUF. The written trigger, and why it hasn't fired.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe12Trigger: React.FC<{ spark?: string }> = ({ spark = 'A written trigger.' }) => {
  const p = useP();
  const rule = ease(remap(p, 0.04, 0.18, 0, 1));
  const c1 = ease(remap(p, 0.30, 0.40, 0, 1));
  const c2 = ease(remap(p, 0.40, 0.50, 0, 1));
  const Cond: React.FC<{ t: string; o: number }> = ({ t, o }) => (
    <div style={{
      width: 700, padding: '26px 40px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: o,
      display: 'flex', alignItems: 'center', gap: 24,
    }}>
      <div style={{ fontFamily: MONO, fontSize: 48, color: SOFT, fontWeight: 700 }}>✕</div>
      <div style={{ fontFamily: SANS, fontSize: 40, color: INK }}>{t}</div>
    </div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 200, width: SAFE.w - 400, top: SAFE.y + 100,
        padding: '30px 50px', background: CLAUDE.CARD, borderLeft: `6px solid ${ACCENT}`, opacity: rule,
      }}>
        <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase' }}>The plan: fine-tune</div>
        <div style={{ fontFamily: SERIF, fontSize: 58, color: INK, lineHeight: 1.25, marginTop: 10 }}>“only if evals plateau below target with full KB coverage.”</div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 360,
        display: 'flex', justifyContent: 'center', gap: 40,
      }}>
        <Cond t="results have plateaued" o={c1} />
        <Cond t="the card library is complete" o={c2} />
      </div>
      <RecordStrip text="It isn’t wrong — it’s thin. More cards would fix that. A smarter model wouldn’t."
        o={remap(p, 0.76, 0.86, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B02 — the golden set, and the textbook cross-check.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe12Golden: React.FC<{ spark?: string }> = ({ spark = 'Checked answers.' }) => {
  const p = useP();
  const t = ease(remap(p, 0.06, 0.18, 0, 1));
  const o1 = ease(remap(p, 0.50, 0.62, 0, 1));
  const o2 = ease(remap(p, 0.66, 0.78, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 110,
        display: 'flex', justifyContent: 'center', gap: 40,
      }}>
        <Tile value="16 / 16" caption="golden-set problems matched" o={t} w={620} size={120} accent />
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 420,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 40,
      }}>
        <Tile value="3.27" caption="OpenStax, published" o={o1} w={440} size={96} />
        <div style={{ fontFamily: MONO, fontSize: 60, color: SOFT, opacity: o2 }}>≈</div>
        <Tile value="3.2667" caption="the engine" o={o2} w={440} size={96} />
      </div>
      <RecordStrip text="Same answer, rounded." o={remap(p, 0.86, 0.94, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B03 — the honest denominator. 18% scorable; 79% is a ceiling.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe12Denominator: React.FC<{ spark?: string }> = ({ spark = 'The honest denominator.' }) => {
  const p = useP();
  const all = ease(remap(p, 0.04, 0.14, 0, 1));
  const s = ease(remap(p, 0.20, 0.34, 0, 1));
  const c = ease(remap(p, 0.62, 0.74, 0, 1));
  const W = 1500;
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: (1920 - W) / 2, width: W, top: SAFE.y + 110, opacity: all,
      }}>
        <div style={{ fontFamily: SERIF, fontSize: 56, fontWeight: 600, color: INK, marginBottom: 18 }}>1,226 UGPhysics problems</div>
        <div style={{ position: 'relative', height: 90, background: CLAUDE.CARD, border: `2px solid ${HAIR}` }}>
          <div style={{ position: 'absolute', left: 0, top: 0, bottom: 0, width: W * 0.183 * s, background: ACCENT }} />
        </div>
        <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: 14, opacity: s }}>
          <div style={{ fontFamily: MONO, fontSize: 38, fontWeight: 700, color: ACCENT }}>18% scorable today</div>
          <div style={{ fontFamily: SANS, fontSize: 34, color: SOFT }}>the rest ask for a derivation, not a number</div>
        </div>
      </div>
      <div style={{
        position: 'absolute', left: (1920 - W) / 2, width: W, top: SAFE.y + 450, opacity: c,
        padding: '26px 40px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`,
        display: 'flex', alignItems: 'center', gap: 34,
      }}>
        <div style={{ fontFamily: SERIF, fontSize: 80, fontWeight: 600, color: INK }}>79%</div>
        <div style={{ fontFamily: SANS, fontSize: 38, color: INK, lineHeight: 1.3 }}>topic coverage — a ceiling, not a score. One card can touch a topic without covering it.</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B04 — evidence. Zero wrong, nothing plateaued.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe12Bottleneck: React.FC<{ spark?: string }> = ({ spark = 'Nothing plateaued.' }) => {
  const p = useP();
  const q = ease(remap(p, 0.30, 0.44, 0, 1));
  const end = ease(remap(p, 0.80, 0.90, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 100,
        display: 'flex', justifyContent: 'center', gap: 34,
      }}>
        <Tile value="60" caption="problems run" o={ease(remap(p, 0.02, 0.10, 0, 1))} w={380} size={100} />
        <Tile value="0" caption="wrong" o={ease(remap(p, 0.08, 0.16, 0, 1))} w={380} size={100} />
        <Tile value="Nearly all" caption="declined" o={ease(remap(p, 0.14, 0.22, 0, 1))} w={440} size={86} />
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x + 200, width: SAFE.w - 400, top: SAFE.y + 380,
        padding: '28px 48px', background: CLAUDE.CARD, borderLeft: `6px solid ${HAIR}`, opacity: q,
      }}>
        <div style={{ fontFamily: SERIF, fontSize: 48, color: INK, lineHeight: 1.3 }}>“No evidence a better model would help, and considerable evidence that more formula cards would.”</div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 640, textAlign: 'center',
        fontFamily: SERIF, fontSize: 72, fontWeight: 600, color: INK, opacity: end,
      }}>The bottleneck is <span style={{ color: ACCENT }}>coverage</span>, not intelligence.</div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B05 — discipline. Indicated work over interesting work; the golden set decides.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe12Discipline: React.FC<{ spark?: string }> = ({ spark = 'The indicated work.' }) => {
  const p = useP();
  const q = ease(remap(p, 0.04, 0.16, 0, 1));
  const qm = ease(remap(p, 0.36, 0.48, 0, 1));
  const gate = ease(remap(p, 0.72, 0.84, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 160, width: SAFE.w - 320, top: SAFE.y + 100,
        padding: '28px 48px', background: CLAUDE.CARD, borderLeft: `6px solid ${ACCENT}`, opacity: q,
      }}>
        <div style={{ fontFamily: SERIF, fontSize: 50, color: INK, lineHeight: 1.3 }}>“Doing the interesting work instead of the indicated work.”</div>
        <div style={{ fontFamily: SANS, fontSize: 32, color: SOFT, marginTop: 10 }}>— what the decision log exists to prevent</div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 330,
        display: 'flex', justifyContent: 'center', gap: 40,
      }}>
        <div style={{
          width: 760, padding: '26px 40px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: qm,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase' }}>Left out on purpose</div>
          <div style={{ fontFamily: SERIF, fontSize: 46, color: INK, marginTop: 8 }}>Quantum: weak cards would raise the number and lower the quality.</div>
        </div>
        <div style={{
          width: 760, padding: '26px 40px', background: CLAUDE.CARD, border: `3px solid ${ACCENT}`, opacity: gate,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: ACCENT, textTransform: 'uppercase', fontWeight: 700 }}>If fine-tuning ever comes</div>
          <div style={{ fontFamily: SERIF, fontSize: 46, color: INK, marginTop: 8 }}>It ships only when it beats the golden set — never on hope.</div>
        </div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B06 — what is still open.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe12Open: React.FC<{ spark?: string }> = ({ spark = 'Still open.' }) => {
  const p = useP();
  const rows = [
    { t: 'Golden set', d: 'far short of the 150–300 problems first planned', at: 0.10, hot: false },
    { t: 'Baseline', d: 'plain AI reasoning, same problems — never run', at: 0.34, hot: true },
    { t: 'Deployment', d: 'nothing deployed yet', at: 0.84, hot: false },
  ];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 170, width: SAFE.w - 340, top: SAFE.y + 100,
        display: 'flex', flexDirection: 'column', gap: 20,
      }}>
        <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase', opacity: remap(p, 0.02, 0.08, 0, 1) }}>From the team’s own status table</div>
        {rows.map((r) => (
          <div key={r.t} style={{
            display: 'flex', alignItems: 'center', gap: 40, padding: '26px 40px', background: CLAUDE.CARD,
            border: `${r.hot ? 3 : 2}px solid ${r.hot ? ACCENT : HAIR}`, opacity: ease(remap(p, r.at, r.at + 0.07, 0, 1)),
          }}>
            <div style={{ width: 340, fontFamily: SERIF, fontSize: 52, fontWeight: 600, color: r.hot ? ACCENT : INK }}>{r.t}</div>
            <div style={{ fontFamily: SANS, fontSize: 38, color: INK, lineHeight: 1.3 }}>{r.d}</div>
          </div>
        ))}
      </div>
      <RecordStrip text="The baseline is “the number the whole project is justified by.”" o={remap(p, 0.60, 0.70, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B07 — the series verdict. Measure first.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe12Verdict: React.FC<{ spark?: string }> = ({ spark = 'For the whole series.' }) => {
  const p = useP();
  const q = ease(remap(p, 0.06, 0.26, 0, 1));
  const sub = ease(remap(p, 0.44, 0.62, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 190, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 60,
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: 104, fontWeight: 600, color: INK, opacity: q, lineHeight: 1.15,
          textAlign: 'center', maxWidth: 1650, transform: `translateY(${(1 - q) * 26}px)`,
        }}>Before a bigger model,<br /><span style={{ color: ACCENT }}>measure first</span>.</div>
        <div style={{
          padding: '28px 48px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: sub,
          fontFamily: SANS, fontSize: 46, color: INK, maxWidth: 1400, textAlign: 'center', lineHeight: 1.35,
        }}>Then build what the measurement points at — even when it’s the boring thing.</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B09 — the outro. Title, terracotta period, host name, credit lines.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe12Outro: React.FC<{ title?: string; handle?: string; subline?: string }> =
({ title = 'Measure First.', handle = 'Param Madan', subline = 'Physics Engine · 12 of 12' }) => {
  const p = useP();
  const rise = ease(remap(p, 0.02, 0.30, 0, 1));
  const nameO = remap(p, 0.24, 0.48, 0, 1);
  const subO = remap(p, 0.44, 0.66, 0, 1);
  const hasDot = title.trim().endsWith('.');
  const stem = hasDot ? title.trim().slice(0, -1) : title.trim();
  return (
    <AbsoluteFill style={{
      background: CLAUDE.PAGE, display: 'flex', flexDirection: 'column',
      alignItems: 'center', justifyContent: 'center', gap: 30,
    }}>
      <div style={{
        fontFamily: SERIF, fontSize: 160, lineHeight: 1.04, fontWeight: 600, color: INK,
        maxWidth: SAFE.w, textAlign: 'center',
        opacity: rise, transform: `translateY(${(1 - rise) * 40}px)`,
      }}>
        {stem}{hasDot && <span style={{ color: ACCENT }}>.</span>}
      </div>
      <div style={{
        fontFamily: SERIF, fontSize: 86, color: INK, opacity: nameO,
        transform: `translateY(${(1 - ease(nameO)) * 22}px)`,
      }}>{handle}</div>
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 12, opacity: subO }}>
        {subline.split(' · ').map((line) => (
          <div key={line} style={{
            fontFamily: SANS, fontSize: 36, letterSpacing: 3, textTransform: 'uppercase',
            color: SOFT, textAlign: 'center', whiteSpace: 'nowrap',
          }}>{line}</div>
        ))}
      </div>
    </AbsoluteFill>
  );
};
