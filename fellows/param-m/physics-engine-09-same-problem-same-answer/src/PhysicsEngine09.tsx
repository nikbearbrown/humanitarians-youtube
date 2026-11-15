/**
 * PhysicsEngine09.tsx — body scenes for "Same Problem, Same Answer." (physics engine, 9 of 12).
 *
 * Reel: books/physics-engine/youtube/same-problem-same-answer
 * Host: Param Madan · voice Kokoro af_bella
 * Source: github.com/jashshah127/humanitariansai/physics-engine @ 2dc4aa4
 *         (engine/README.md V2 routing; eval/demo.py checks 1–2; EVALUATION.md).
 *
 * CONTRACT (illustrations/kit.tsx): every scene here is a pure function of
 * useP() — normalized progress across the beat's audio duration. No wall clock,
 * no state, no CSS transitions. Seeking any frame renders identically.
 *
 * COLOR: claude palette, one terracotta moment per beat. The accent marks the
 * no-randomness claim, formula selection, the ambiguous route, and parse.
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

/** A small mono chip — one value or name. */
const Chip: React.FC<{ text: string; o?: number; hot?: boolean; size?: number }> = ({
  text, o = 1, hot = false, size = 40,
}) => (
  <span style={{
    display: 'inline-block', padding: '10px 24px', background: CLAUDE.CARD,
    border: `${hot ? 3 : 2}px solid ${hot ? ACCENT : HAIR}`, opacity: o, whiteSpace: 'nowrap',
    fontFamily: MONO, fontSize: size, fontWeight: 600, color: hot ? ACCENT : INK,
  }}>{text}</span>
);

/* ────────────────────────────────────────────────────────────────────────────
 * B00B — the promise. Three things this video shows.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe9Promise: React.FC<{ spark?: string; headline?: string }> = ({
  spark = 'Why watch this.',
  headline = 'Why the answer never drifts.',
}) => {
  const p = useP();
  const head = ease(remap(p, 0.04, 0.18, 0, 1));
  const items = [
    { v: 'The solver', c: 'can’t disagree with itself', hot: false },
    { v: '2 sources', c: 'where variation sneaks in', hot: false },
    { v: '3 routes', c: 'decided before solving', hot: true },
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
          <Tile key={n.v} value={n.v} caption={n.c} accent={n.hot} w={520} size={96}
            o={ease(remap(p, 0.14 + i * 0.2, 0.30 + i * 0.2, 0, 1))} />
        ))}
      </div>
      <RecordStrip text="No physics or coding background needed." o={remap(p, 0.84, 0.94, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B01 — the BLUF. Ten byte-identical runs; the solver isn't the cause.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe9Solver: React.FC<{ spark?: string }> = ({ spark = 'Ten runs, one answer.' }) => {
  const p = useP();
  const grid = ease(remap(p, 0.04, 0.20, 0, 1));
  const then = ease(remap(p, 0.40, 0.54, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 160, width: SAFE.w - 320, top: SAFE.y + 100,
        display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: 16, opacity: grid,
      }}>
        {Array.from({ length: 10 }, (_, i) => (
          <div key={i} style={{
            padding: '16px 0', textAlign: 'center', background: CLAUDE.CARD, border: `2px solid ${HAIR}`,
            fontFamily: MONO, fontSize: 30, color: INK, whiteSpace: 'nowrap',
            opacity: ease(remap(p, 0.04 + i * 0.012, 0.10 + i * 0.012, 0, 1)),
          }}>#{i + 1}  a = 1.96</div>
        ))}
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 350, textAlign: 'center',
        fontFamily: SERIF, fontSize: 64, fontWeight: 600, color: INK, opacity: grid,
      }}>Byte-identical. <span style={{ color: ACCENT }}>SymPy has no randomness.</span></div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 470,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 24, opacity: then,
      }}>
        <div style={{ fontFamily: SANS, fontSize: 38, color: SOFT }}>Two answers to one problem? Then it’s</div>
        <Chip text="which formula" />
        <div style={{ fontFamily: SANS, fontSize: 38, color: SOFT }}>or</div>
        <Chip text="model sampling" />
      </div>
      <RecordStrip text="So the engine checks before solving, and labels every answer with its route."
        o={remap(p, 0.82, 0.92, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B02 — two places variation can enter.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe9Sources: React.FC<{ spark?: string }> = ({ spark = 'Only two places.' }) => {
  const p = useP();
  const Card: React.FC<{ n: string; t: string; body: string; o: number; hot?: boolean }> = ({ n, t, body, o, hot = false }) => (
    <div style={{
      width: 790, height: 420, padding: '34px 44px', background: CLAUDE.CARD,
      border: `${hot ? 3 : 2}px solid ${hot ? ACCENT : HAIR}`, opacity: o,
      transform: `translateY(${(1 - o) * 24}px)`, display: 'flex', flexDirection: 'column', gap: 18,
    }}>
      <div style={{ fontFamily: SERIF, fontSize: 90, fontWeight: 600, color: hot ? ACCENT : SOFT, lineHeight: 1 }}>{n}</div>
      <div style={{ fontFamily: SERIF, fontSize: 56, fontWeight: 600, color: INK }}>{t}</div>
      <div style={{ height: 2, background: HAIR }} />
      <div style={{ fontFamily: SANS, fontSize: 38, color: INK, lineHeight: 1.3 }}>{body}</div>
    </div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 100,
        display: 'flex', justifyContent: 'center', gap: 48,
      }}>
        <Card n="1" t="Formula selection" hot o={ease(remap(p, 0.06, 0.16, 0, 1))}
          body="Two cards could answer, nothing chooses — whichever comes first wins." />
        <Card n="2" t="Model sampling" o={ease(remap(p, 0.44, 0.54, 0, 1))}
          body="A language model does part of the work, and samples differently each run." />
      </div>
      <RecordStrip text="Running it twice won’t catch the first. SymPy can’t disagree with itself."
        o={remap(p, 0.80, 0.90, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B03 — three routes, counted before solving.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe9Routes: React.FC<{ spark?: string }> = ({ spark = 'Count before solving.' }) => {
  const p = useP();
  const rows = [
    { n: '1 card closes', r: 'deterministic_script', what: 'final answer', at: 0.10, hot: false },
    { n: '0 cards close', r: 'no_deterministic_path', what: 'model or human · gap logged', at: 0.34, hot: false },
    { n: '2+ cards close', r: 'ambiguous_multiple_deterministic_paths', what: 'all answers back · model picks the formula, not the math', at: 0.58, hot: true },
  ];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 60, width: SAFE.w - 120, top: SAFE.y + 100,
        display: 'flex', flexDirection: 'column', gap: 20,
      }}>
        {rows.map((x) => {
          const o = ease(remap(p, x.at, x.at + 0.08, 0, 1));
          return (
            <div key={x.n} style={{
              display: 'flex', alignItems: 'center', gap: 34, padding: '24px 40px', background: CLAUDE.CARD,
              border: `${x.hot ? 3 : 2}px solid ${x.hot ? ACCENT : HAIR}`, opacity: o,
              transform: `translateX(${(1 - o) * -24}px)`,
            }}>
              <div style={{ width: 360, fontFamily: SERIF, fontSize: 50, fontWeight: 600, color: INK }}>{x.n}</div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                <div style={{ fontFamily: MONO, fontSize: 36, fontWeight: 700, color: x.hot ? ACCENT : INK, whiteSpace: 'nowrap' }}>{x.r}</div>
                <div style={{ fontFamily: SANS, fontSize: 34, color: SOFT }}>{x.what}</div>
              </div>
            </div>
          );
        })}
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B04 — the constructed ambiguity: v = 30 vs v ≈ 2.37.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe9Ambiguous: React.FC<{ spark?: string }> = ({ spark = 'Two right answers?' }) => {
  const p = useP();
  const k = ease(remap(p, 0.04, 0.16, 0, 1));
  const a = ease(remap(p, 0.28, 0.38, 0, 1));
  const b = ease(remap(p, 0.38, 0.48, 0, 1));
  const ask = ease(remap(p, 0.80, 0.90, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 100, textAlign: 'center', opacity: k,
      }}>
        <Chip text="knowns: v0=0, a=2.5, t=12, m=2, k=500, x=0.15  ·  find v" size={36} />
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 220,
        display: 'flex', justifyContent: 'center', gap: 60,
      }}>
        {[
          { c: 'Constant acceleration', v: 'v = 30.0 m/s', o: a },
          { c: 'Spring energy', v: 'v ≈ 2.37 m/s', o: b },
        ].map((x) => (
          <div key={x.c} style={{
            width: 680, padding: '30px 44px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`,
            opacity: x.o, transform: `translateY(${(1 - x.o) * 22}px)`, display: 'flex', flexDirection: 'column', gap: 14,
          }}>
            <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase', whiteSpace: 'nowrap' }}>{x.c} · closes</div>
            <div style={{ fontFamily: MONO, fontSize: 64, fontWeight: 700, color: INK }}>{x.v}</div>
          </div>
        ))}
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 500, textAlign: 'center',
        fontFamily: SANS, fontSize: 38, color: SOFT, opacity: remap(p, 0.56, 0.66, 0, 1),
      }}>Silently taking the first card would look consistent — and could be confidently wrong.</div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 600, textAlign: 'center', opacity: ask,
      }}>
        <Chip text="status: needs_llm_arbitration — both reported" hot size={42} />
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B05 — why: fairness, debugging, cost.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe9Why: React.FC<{ spark?: string }> = ({ spark = 'Three reasons.' }) => {
  const p = useP();
  const items = [
    { v: 'Fairness', c: 'same problem, same reference', hot: true, at: 0.14 },
    { v: 'Debugging', c: 'route + card = what to fix', hot: false, at: 0.42 },
    { v: 'Cost', c: 'solve is cheaper than a model call', hot: false, at: 0.72 },
  ];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 170, width: SAFE.w,
        display: 'flex', justifyContent: 'center', gap: 34,
      }}>
        {items.map((n) => (
          <Tile key={n.v} value={n.v} caption={n.c} accent={n.hot} w={540} size={100}
            o={ease(remap(p, n.at, n.at + 0.1, 0, 1))} />
        ))}
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B06 — the limit. Ten runs prove the solver; parse can vary.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe9Limit: React.FC<{ spark?: string }> = ({ spark = 'What it proves.' }) => {
  const p = useP();
  const a = ease(remap(p, 0.04, 0.16, 0, 1));
  const b = ease(remap(p, 0.20, 0.34, 0, 1));
  const q = ease(remap(p, 0.62, 0.74, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 100,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 30,
      }}>
        <div style={{ opacity: b }}><Chip text="parse · model · can vary" hot size={34} /></div>
        <div style={{ fontFamily: MONO, fontSize: 54, color: SOFT, opacity: b }}>→</div>
        <div style={{ opacity: a }}><Chip text="retrieve · plan · solve · verify · proven" size={34} /></div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 210, textAlign: 'center',
        fontFamily: SANS, fontSize: 36, color: SOFT, opacity: b,
      }}>Newer Claude models take no randomness setting.</div>
      <div style={{
        position: 'absolute', left: SAFE.x + 170, width: SAFE.w - 340, top: SAFE.y + 360,
        padding: '34px 54px', background: CLAUDE.CARD, borderLeft: `6px solid ${ACCENT}`, opacity: q,
        transform: `translateY(${(1 - q) * 20}px)`,
      }}>
        <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase' }}>The team’s own hard question</div>
        <div style={{ fontFamily: SERIF, fontSize: 54, color: INK, lineHeight: 1.3, marginTop: 12 }}>“Is the routing decision the right one, or is it just a way of avoiding hard problems?”</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B07 — the verdict. Ask which method, and why.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe9Verdict: React.FC<{ spark?: string }> = ({ spark = 'Ask for the method.' }) => {
  const p = useP();
  const q = ease(remap(p, 0.06, 0.26, 0, 1));
  const sub = ease(remap(p, 0.44, 0.60, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 190, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 60,
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: 96, fontWeight: 600, color: INK, opacity: q, lineHeight: 1.15,
          textAlign: 'center', maxWidth: 1650, transform: `translateY(${(1 - q) * 26}px)`,
        }}>Consistency you can <span style={{ color: ACCENT }}>explain</span><br />beats consistency you hope for.</div>
        <div style={{
          padding: '28px 48px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: sub,
          fontFamily: SANS, fontSize: 46, color: INK, maxWidth: 1400, textAlign: 'center', lineHeight: 1.35,
        }}>Ask which method it chose, and why. If the method can change, so can the answer.</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B09 — the outro. Title, terracotta period, host name, credit lines.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe9Outro: React.FC<{ title?: string; handle?: string; subline?: string }> =
({ title = 'Same Problem, Same Answer.', handle = 'Param Madan', subline = 'Physics Engine · 9 of 12' }) => {
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
