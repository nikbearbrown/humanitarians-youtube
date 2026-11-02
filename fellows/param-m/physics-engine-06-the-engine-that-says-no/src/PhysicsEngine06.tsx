/**
 * PhysicsEngine06.tsx — body scenes for "The Engine That Says No." (physics engine, 6 of 12).
 *
 * Reel: books/physics-engine/youtube/the-engine-that-says-no
 * Host: Param Madan · voice Kokoro af_bella
 * Source: github.com/jashshah127/humanitariansai/physics-engine @ 2dc4aa4
 *         (engine/pipeline.py plan(); PHASE1.md; PHASE2.md; eval/ci_check.py).
 *
 * CONTRACT (illustrations/kit.tsx): every scene here is a pure function of
 * useP() — normalized progress across the beat's audio duration. No wall clock,
 * no state, no CSS transitions. Seeking any frame renders identically.
 *
 * COLOR: claude palette, one terracotta moment per beat. The accent marks the
 * "no" branch, the named gap, the unverified badge, zero wrong, and the refusal.
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
const Chip: React.FC<{ text: string; o?: number; hot?: boolean; struck?: boolean; size?: number }> = ({
  text, o = 1, hot = false, struck = false, size = 40,
}) => (
  <span style={{
    display: 'inline-block', padding: '10px 24px', background: CLAUDE.CARD,
    border: `${hot ? 3 : 2}px solid ${hot ? ACCENT : HAIR}`, opacity: o, whiteSpace: 'nowrap',
    fontFamily: MONO, fontSize: size, fontWeight: 600, color: hot ? ACCENT : struck ? SOFT : INK,
    textDecoration: struck ? 'line-through' : 'none',
  }}>{text}</span>
);

const Arrow: React.FC<{ o?: number }> = ({ o = 1 }) => (
  <div style={{ fontFamily: MONO, fontSize: 54, color: SOFT, opacity: o }}>→</div>
);

/* ────────────────────────────────────────────────────────────────────────────
 * B00B — the promise. Three things this video shows.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe6Promise: React.FC<{ spark?: string; headline?: string }> = ({
  spark = 'Why watch this.',
  headline = 'Can it answer at all?',
}) => {
  const p = useP();
  const head = ease(remap(p, 0.04, 0.18, 0, 1));
  const items = [
    { v: 'Closure', c: 'what it means', hot: false },
    { v: '3 ways', c: 'a plan can fail', hot: false },
    { v: 'Saying no', c: 'and when it was a bug', hot: true },
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
          <Tile key={n.v} value={n.v} caption={n.c} accent={n.hot} w={520} size={100}
            o={ease(remap(p, 0.14 + i * 0.2, 0.30 + i * 0.2, 0, 1))} />
        ))}
      </div>
      <RecordStrip text="No physics or coding background needed." o={remap(p, 0.84, 0.94, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B01 — the BLUF. One question before solving; two branches.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe6Closure: React.FC<{ spark?: string }> = ({ spark = 'Ask before solving.' }) => {
  const p = useP();
  const q = ease(remap(p, 0.04, 0.18, 0, 1));
  const yes = ease(remap(p, 0.40, 0.50, 0, 1));
  const no = ease(remap(p, 0.52, 0.64, 0, 1));
  const Branch: React.FC<{ head: string; body: string; o: number; hot?: boolean }> = ({ head, body, o, hot = false }) => (
    <div style={{
      width: 700, padding: '30px 42px', background: CLAUDE.CARD,
      border: `${hot ? 3 : 2}px solid ${hot ? ACCENT : HAIR}`, opacity: o,
      transform: `translateY(${(1 - o) * 22}px)`, display: 'flex', flexDirection: 'column', gap: 14,
    }}>
      <div style={{ fontFamily: SERIF, fontSize: 64, fontWeight: 600, color: hot ? ACCENT : INK }}>{head}</div>
      <div style={{ fontFamily: SANS, fontSize: 40, color: INK, lineHeight: 1.3 }}>{body}</div>
    </div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 200, width: SAFE.w - 400, top: SAFE.y + 100,
        padding: '34px 50px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: q,
        transform: `translateY(${(1 - q) * 24}px)`, textAlign: 'center',
      }}>
        <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase', marginBottom: 12 }}>The closure check</div>
        <div style={{ fontFamily: SERIF, fontSize: 60, fontWeight: 600, color: INK, lineHeight: 1.2 }}>With what we’re given, can the equations pin down every unknown?</div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 400,
        display: 'flex', justifyContent: 'center', gap: 60,
      }}>
        <Branch head="Yes → solve" body="SymPy does the math." o={yes} />
        <Branch head="No → stop" body="Say why. Mark it not verified. Hand it on." o={no} hot />
      </div>
      <RecordStrip text="It never fills the gap with a guess." o={remap(p, 0.84, 0.93, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B02 — three named ways to fail closure.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe6Reasons: React.FC<{ spark?: string }> = ({ spark = 'Every failure has a name.' }) => {
  const p = useP();
  const rows = [
    { n: '1', t: 'Missing knowns', code: "missing knowns: ['k']", at: 0.12, hot: true },
    { n: '2', t: 'The solver errors', code: 'solver raised …Error', at: 0.44 },
    { n: '3', t: 'No definite answer', code: 'did not resolve to a determinate solution', at: 0.56 },
  ];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 130, width: SAFE.w - 260, top: SAFE.y + 100,
        display: 'flex', flexDirection: 'column', gap: 22,
      }}>
        {rows.map((r) => {
          const o = ease(remap(p, r.at, r.at + 0.07, 0, 1));
          return (
            <div key={r.n} style={{
              display: 'flex', alignItems: 'center', gap: 36, padding: '26px 40px', background: CLAUDE.CARD,
              border: `${r.hot ? 3 : 2}px solid ${r.hot ? ACCENT : HAIR}`, opacity: o,
              transform: `translateX(${(1 - o) * -24}px)`,
            }}>
              <div style={{ fontFamily: SERIF, fontSize: 80, fontWeight: 600, color: r.hot ? ACCENT : SOFT, width: 60 }}>{r.n}</div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                <div style={{ fontFamily: SERIF, fontSize: 54, fontWeight: 600, color: INK }}>{r.t}</div>
                <div style={{ fontFamily: MONO, fontSize: 34, color: SOFT, whiteSpace: 'nowrap' }}>reason: {r.code}</div>
              </div>
            </div>
          );
        })}
      </div>
      <RecordStrip text="The reason is recorded every time — a failure points at what to fix."
        o={remap(p, 0.82, 0.92, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B03 — the damped oscillator: unverified, and into the coverage queue.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe6Queue: React.FC<{ spark?: string }> = ({ spark = 'No card? Say so.' }) => {
  const p = useP();
  const prob = ease(remap(p, 0.04, 0.14, 0, 1));
  const none = ease(remap(p, 0.26, 0.36, 0, 1));
  const badge = ease(remap(p, 0.50, 0.60, 0, 1));
  const queue = ease(remap(p, 0.66, 0.78, 0, 1));
  // A decaying wave: the oscillator whose bouncing dies away.
  const pts = Array.from({ length: 121 }, (_, i) => {
    const x = i / 120;
    return `${(x * 560).toFixed(1)},${(80 - 70 * Math.exp(-3 * x) * Math.cos(x * 22)).toFixed(1)}`;
  }).join(' ');
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 110,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 34,
      }}>
        <div style={{
          width: 640, padding: '26px 36px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: prob,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase' }}>Damped oscillator</div>
          <svg width={560} height={160} viewBox="0 0 560 160" style={{ marginTop: 10 }}>
            <polyline points={pts} fill="none" stroke={INK} strokeWidth={4} />
          </svg>
        </div>
        <Arrow o={none} />
        <div style={{ opacity: none, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 16 }}>
          <Chip text="no card covers it" struck />
        </div>
        <Arrow o={badge} />
        <Chip text="unverified" hot o={badge} size={46} />
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x + 420, width: SAFE.w - 840, top: SAFE.y + 430,
        padding: '28px 40px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: queue,
        transform: `translateY(${(1 - queue) * 20}px)`, display: 'flex', flexDirection: 'column', gap: 12,
      }}>
        <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase' }}>Coverage queue</div>
        <div style={{ fontFamily: MONO, fontSize: 40, color: INK }}>+ damped_frequency</div>
        <div style={{ fontFamily: SANS, fontSize: 34, color: SOFT }}>→ the to-do list for the next card</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B04 — evidence. Sixty problems, zero wrong, nearly all declined.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe6Sixty: React.FC<{ spark?: string }> = ({ spark = 'Read the zero carefully.' }) => {
  const p = useP();
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 150,
        display: 'flex', justifyContent: 'center', gap: 40,
      }}>
        <Tile value="60" caption="UGPhysics problems" o={ease(remap(p, 0.04, 0.14, 0, 1))} w={480} size={140} />
        <Tile value="0" caption="wrong answers" o={ease(remap(p, 0.14, 0.24, 0, 1))} w={480} size={140} accent />
        <Tile value="Nearly all" caption="declined" o={ease(remap(p, 0.30, 0.40, 0, 1))} w={480} size={110} />
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 520, textAlign: 'center',
        fontFamily: SANS, fontSize: 40, color: SOFT, opacity: remap(p, 0.42, 0.52, 0, 1),
      }}>The library is thin, and most of the benchmark asks for derivations, not numbers.</div>
      <RecordStrip text="Here, zero wrong mostly measures honesty — not coverage."
        o={remap(p, 0.80, 0.90, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B05 — the turn. Solvable problems declined by a decimal conversion.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe6Hidden: React.FC<{ spark?: string }> = ({ spark = 'When no was wrong.' }) => {
  const p = useP();
  const a = ease(remap(p, 0.06, 0.16, 0, 1));
  const b = ease(remap(p, 0.18, 0.28, 0, 1));
  const c = ease(remap(p, 0.32, 0.42, 0, 1));
  const d = ease(remap(p, 0.44, 0.52, 0, 1));
  const quote = ease(remap(p, 0.60, 0.72, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 130,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 14,
      }}>
        <Chip text="problem in symbols" o={a} size={32} />
        <Arrow o={b} />
        <Chip text="SymPy solves it" o={b} size={32} />
        <Arrow o={c} />
        <Chip text="float( ) at the end" o={c} hot size={32} />
        <Arrow o={d} />
        <Chip text="declined" o={d} struck size={32} />
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 230, textAlign: 'center',
        fontFamily: SANS, fontSize: 34, color: SOFT, opacity: b,
      }}>a = g·(m2 − m1)/(m1 + m2) — exact, just not a decimal.</div>
      <div style={{
        position: 'absolute', left: SAFE.x + 110, width: SAFE.w - 220, top: SAFE.y + 360,
        padding: '36px 56px', background: CLAUDE.CARD, borderLeft: `6px solid ${ACCENT}`, opacity: quote,
        transform: `translateY(${(1 - quote) * 20}px)`,
      }}>
        <div style={{ fontFamily: SERIF, fontSize: 54, color: INK, lineHeight: 1.3 }}>“An interface limitation was being reported as a coverage gap.”</div>
        <div style={{ fontFamily: SANS, fontSize: 34, color: SOFT, marginTop: 18 }}>Worse than an honest gap: it hid what the engine could already do. — PHASE2.md</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B06 — consequence. Grade mode refuses to grade without a verified reference.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe6Refuse: React.FC<{ spark?: string }> = ({ spark = 'No reference, no grade.' }) => {
  const p = useP();
  const a = ease(remap(p, 0.06, 0.16, 0, 1));
  const b = ease(remap(p, 0.16, 0.26, 0, 1));
  const c = ease(remap(p, 0.30, 0.42, 0, 1));
  const ci = ease(remap(p, 0.72, 0.84, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{ position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 96 }}>
        <Eyebrow text="Grade mode" o={a} />
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 170,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 16,
      }}>
        <Chip text="student’s work" o={a} size={34} />
        <Arrow o={b} />
        <Chip text="no verified answer" o={b} size={34} />
        <Arrow o={c} />
        <Chip text="not_assessable" o={c} hot size={40} />
        <Arrow o={c} />
        <Chip text="human review" o={c} size={34} />
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 330, textAlign: 'center',
        fontFamily: SERIF, fontSize: 64, fontWeight: 600, color: INK, opacity: remap(p, 0.46, 0.58, 0, 1),
      }}>Never marked wrong against an answer it can’t verify.</div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 500, textAlign: 'center', opacity: ci,
      }}>
        <span style={{
          padding: '14px 34px', border: `2px solid ${HAIR}`, background: CLAUDE.CARD,
          fontFamily: MONO, fontSize: 36, color: INK,
        }}>eval/ci_check.py · “must refuse” — an automated test, not a habit</span>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B07 — the verdict. Trust a tool that is allowed to say no.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe6Verdict: React.FC<{ spark?: string }> = ({ spark = 'Could it have said no?' }) => {
  const p = useP();
  const q = ease(remap(p, 0.06, 0.24, 0, 1));
  const sub = ease(remap(p, 0.44, 0.60, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 200, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 60,
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: 100, fontWeight: 600, color: INK, opacity: q, lineHeight: 1.15,
          textAlign: 'center', maxWidth: 1650, transform: `translateY(${(1 - q) * 26}px)`,
        }}>Trust a tool that’s allowed<br />to say <span style={{ color: ACCENT }}>“I can’t.”</span></div>
        <div style={{
          padding: '28px 48px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: sub,
          fontFamily: SANS, fontSize: 46, color: INK, maxWidth: 1400, textAlign: 'center', lineHeight: 1.35,
        }}>If it never says no, treat every answer as a guess until you’ve checked it.</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B09 — the outro. Title, terracotta period, host name, credit lines.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe6Outro: React.FC<{ title?: string; handle?: string; subline?: string }> =
({ title = 'The Engine That Says No.', handle = 'Param Madan', subline = 'Physics Engine · 6 of 12' }) => {
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
