/**
 * PhysicsEngine10.tsx — body scenes for "Where It Went Wrong." (physics engine, 10 of 12).
 *
 * Reel: books/physics-engine/youtube/where-it-went-wrong
 * Host: Param Madan · voice Kokoro af_bella
 * Source: github.com/jashshah127/humanitariansai/physics-engine @ 2dc4aa4
 *         (engine/grade_mode.py; PHASE2.md grade mode; golden set MECH-003, MECH-007).
 *
 * CONTRACT (illustrations/kit.tsx): every scene here is a pure function of
 * useP() — normalized progress across the beat's audio duration. No wall clock,
 * no state, no CSS transitions. Seeking any frame renders identically.
 *
 * COLOR: claude palette, one terracotta moment per beat. The accent marks the
 * diagnosis, the matched mistake, the first wrong step, and the refusal.
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
export const Pe10Promise: React.FC<{ spark?: string; headline?: string }> = ({
  spark = 'Why watch this.',
  headline = 'Grading that teaches.',
}) => {
  const p = useP();
  const head = ease(remap(p, 0.04, 0.18, 0, 1));
  const items = [
    { v: 'Which', c: 'mistake was made', hot: false },
    { v: 'Where', c: 'the first wrong step', hot: false },
    { v: 'Refuses', c: 'two things, on purpose', hot: true },
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
          <Tile key={n.v} value={n.v} caption={n.c} accent={n.hot} w={520} size={120}
            o={ease(remap(p, 0.16 + i * 0.2, 0.32 + i * 0.2, 0, 1))} />
        ))}
      </div>
      <RecordStrip text="No physics or coding background needed." o={remap(p, 0.84, 0.94, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B01 — the BLUF. A checker marks; grade mode diagnoses.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe10Diagnose: React.FC<{ spark?: string }> = ({ spark = 'Diagnose, don’t mark.' }) => {
  const p = useP();
  const l = ease(remap(p, 0.04, 0.16, 0, 1));
  const r = ease(remap(p, 0.22, 0.36, 0, 1));
  const Col: React.FC<{ head: string; body: string; o: number; hot?: boolean }> = ({ head, body, o, hot = false }) => (
    <div style={{
      width: 780, height: 420, padding: '36px 48px', background: CLAUDE.CARD,
      border: `${hot ? 3 : 2}px solid ${hot ? ACCENT : HAIR}`, opacity: o,
      transform: `translateY(${(1 - o) * 24}px)`, display: 'flex', flexDirection: 'column', gap: 20,
    }}>
      <div style={{ fontFamily: SERIF, fontSize: 64, fontWeight: 600, color: hot ? ACCENT : INK }}>{head}</div>
      <div style={{ height: 2, background: HAIR }} />
      <div style={{ fontFamily: SANS, fontSize: 42, color: INK, lineHeight: 1.35 }}>{body}</div>
    </div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 110, width: SAFE.w,
        display: 'flex', justifyContent: 'center', gap: 56,
      }}>
        <Col head="A checker" body="“Wrong.”" o={l} />
        <Col head="Grade mode" hot o={r}
          body="Tests your number against the right answer and against the classic wrong ones — then names the mistake." />
      </div>
      <RecordStrip text="And quotes the card’s own warning about that mistake."
        o={remap(p, 0.80, 0.90, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B02 — the pattern list, built from the correct formula.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe10Patterns: React.FC<{ spark?: string }> = ({ spark = 'The classic mistakes.' }) => {
  const p = useP();
  const rows = [
    { k: 'sign_flip', f: '−x', d: 'reversed a difference', at: 0.08 },
    { k: 'reciprocal', f: '1 / x', d: 'inverted the whole thing', at: 0.18 },
    { k: 'factor_2', f: '2x · x/2', d: 'lost or gained a factor of 2', at: 0.26 },
    { k: 'sqrt2', f: '√2·x · x/√2', d: 'escape vs. orbital speed', at: 0.38 },
    { k: 'sqrt_forgotten', f: 'x² for x', d: 'forgot the square root', at: 0.58 },
  ];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 190, width: SAFE.w - 380, top: SAFE.y + 96,
        display: 'flex', flexDirection: 'column', gap: 12,
      }}>
        <div style={{
          display: 'flex', fontFamily: SANS, fontSize: 26, letterSpacing: 3, color: SOFT,
          textTransform: 'uppercase', padding: '0 30px', opacity: remap(p, 0.02, 0.08, 0, 1),
        }}>
          <div style={{ width: 400 }}>Pattern</div>
          <div style={{ width: 300 }}>From correct x</div>
          <div>What it catches</div>
        </div>
        {rows.map((r) => (
          <div key={r.k} style={{
            display: 'flex', alignItems: 'center', padding: '16px 30px', background: CLAUDE.CARD,
            border: `2px solid ${HAIR}`, opacity: ease(remap(p, r.at, r.at + 0.06, 0, 1)),
          }}>
            <div style={{ width: 400, fontFamily: MONO, fontSize: 38, fontWeight: 700, color: INK }}>{r.k}</div>
            <div style={{ width: 300, fontFamily: MONO, fontSize: 36, color: INK }}>{r.f}</div>
            <div style={{ fontFamily: SANS, fontSize: 34, color: SOFT }}>{r.d}</div>
          </div>
        ))}
      </div>
      <RecordStrip text="Each wrong version is computed and compared with what the student wrote."
        o={remap(p, 0.82, 0.92, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B03 — the Atwood sign flip, with the card's warning.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe10SignFlip: React.FC<{ spark?: string }> = ({ spark = 'Not a grade — a lesson.' }) => {
  const p = useP();
  const ref = ease(remap(p, 0.06, 0.18, 0, 1));
  const stu = ease(remap(p, 0.26, 0.36, 0, 1));
  const match = ease(remap(p, 0.40, 0.50, 0, 1));
  const warn = ease(remap(p, 0.56, 0.68, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 100,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 40,
      }}>
        <Tile value="1.96" caption="verified · m/s²" o={ref} w={400} size={100} />
        <Tile value="−1.96" caption="student" o={stu} w={400} size={100} />
        <div style={{ opacity: match }}><Chip text="= sign_flip" hot size={52} /></div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x + 200, width: SAFE.w - 400, top: SAFE.y + 400,
        padding: '30px 48px', background: CLAUDE.CARD, borderLeft: `6px solid ${ACCENT}`, opacity: warn,
        transform: `translateY(${(1 - warn) * 20}px)`,
      }}>
        <div style={{ fontFamily: MONO, fontSize: 26, color: SOFT }}>MECH-DYN-ATWOOD · pitfall, quoted in the feedback</div>
        <div style={{ fontFamily: SERIF, fontSize: 52, color: INK, lineHeight: 1.3, marginTop: 10 }}>“Inconsistent sign convention across the two masses’ equations.”</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B04 — divergence. Point at the first wrong step, not the last.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe10FirstWrong: React.FC<{ spark?: string }> = ({ spark = 'The first wrong step.' }) => {
  const p = useP();
  const steps = [
    { k: 'I (moment of inertia)', s: '0.125', r: '0.0625', first: true },
    { k: 'α (angular acceleration)', s: '4.8', r: '9.6', first: false },
    { k: 'ω (final spin speed)', s: '24.0', r: '48.0', first: false },
  ];
  const show = ease(remap(p, 0.10, 0.22, 0, 1));
  const point = ease(remap(p, 0.48, 0.58, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 200, width: SAFE.w - 400, top: SAFE.y + 100,
        display: 'flex', flexDirection: 'column', gap: 14, opacity: show,
      }}>
        <div style={{ display: 'flex', fontFamily: SANS, fontSize: 26, letterSpacing: 3, color: SOFT, textTransform: 'uppercase', padding: '0 30px' }}>
          <div style={{ flex: 1 }}>Student step</div>
          <div style={{ width: 230 }}>Submitted</div>
          <div style={{ width: 230 }}>Reference</div>
        </div>
        {steps.map((x) => {
          const hot = x.first && point > 0;
          return (
            <div key={x.k} style={{
              display: 'flex', alignItems: 'center', padding: '20px 30px', background: CLAUDE.CARD,
              border: `${hot ? 3 : 2}px solid ${hot ? ACCENT : HAIR}`,
              opacity: x.first ? 1 : 1 - point * 0.5,
            }}>
              <div style={{ flex: 1, fontFamily: SERIF, fontSize: 44, color: hot ? ACCENT : INK, fontWeight: 600 }}>{x.k}</div>
              <div style={{ width: 230, fontFamily: MONO, fontSize: 40, color: INK }}>{x.s}</div>
              <div style={{ width: 230, fontFamily: MONO, fontSize: 40, color: SOFT }}>{x.r}</div>
            </div>
          );
        })}
      </div>
      <RecordStrip text="Everything after the first error is downstream of it." o={remap(p, 0.80, 0.90, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B05 — fairness. Two percent tolerance; five results.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe10Fair: React.FC<{ spark?: string }> = ({ spark = 'Fair on purpose.' }) => {
  const p = useP();
  const tol = ease(remap(p, 0.04, 0.16, 0, 1));
  const q = ease(remap(p, 0.20, 0.32, 0, 1));
  const res = ['correct', 'wrong_value', 'wrong_method', 'incomplete', 'not_assessable'];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 100,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 50,
      }}>
        <Tile value="±2%" caption="counts as right" o={tol} w={440} size={110} accent />
        <div style={{
          width: 900, padding: '28px 44px', background: CLAUDE.CARD, borderLeft: `6px solid ${HAIR}`, opacity: q,
        }}>
          <div style={{ fontFamily: SERIF, fontSize: 44, color: INK, lineHeight: 1.3 }}>“Marking 3.2 wrong when the answer is 3.2026 teaches nothing except that the grader is pedantic.”</div>
        </div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 460,
        display: 'flex', justifyContent: 'center', gap: 18,
      }}>
        {res.map((r, i) => (
          <div key={r} style={{ opacity: ease(remap(p, 0.70 + i * 0.04, 0.75 + i * 0.04, 0, 1)) }}>
            <Chip text={r} size={36} />
          </div>
        ))}
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B06 — two refusals, and the honest status.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe10Refuse: React.FC<{ spark?: string }> = ({ spark = 'Two refusals.' }) => {
  const p = useP();
  const a = ease(remap(p, 0.04, 0.16, 0, 1));
  const b = ease(remap(p, 0.26, 0.38, 0, 1));
  const n = ease(remap(p, 0.80, 0.90, 0, 1));
  const Card: React.FC<{ t: string; body: string; o: number; hot?: boolean }> = ({ t, body, o, hot = false }) => (
    <div style={{
      width: 790, height: 330, padding: '32px 44px', background: CLAUDE.CARD,
      border: `${hot ? 3 : 2}px solid ${hot ? ACCENT : HAIR}`, opacity: o,
      transform: `translateY(${(1 - o) * 22}px)`, display: 'flex', flexDirection: 'column', gap: 16,
    }}>
      <div style={{ fontFamily: SERIF, fontSize: 54, fontWeight: 600, color: hot ? ACCENT : INK }}>{t}</div>
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
        <Card t="No unverified grading" hot o={a} body="No verified answer → not_assessable → a human reviews it." />
        <Card t="Nothing stored" o={b} body="Takes the work, returns an assessment, forgets. Storage waits on a privacy review." />
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 520, textAlign: 'center',
        fontFamily: SERIF, fontSize: 56, fontWeight: 600, color: INK, opacity: n,
      }}>Not deployed yet. No student has used it.</div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B07 — the verdict. Which mistake is feedback.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe10Verdict: React.FC<{ spark?: string }> = ({ spark = 'Ask which mistake.' }) => {
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
          fontFamily: SERIF, fontSize: 104, fontWeight: 600, color: INK, opacity: q, lineHeight: 1.15,
          textAlign: 'center', maxWidth: 1650, transform: `translateY(${(1 - q) * 26}px)`,
        }}>Wrong is a verdict.<br /><span style={{ color: ACCENT }}>Which mistake</span> is feedback.</div>
        <div style={{
          padding: '28px 48px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: sub,
          fontFamily: SANS, fontSize: 46, color: INK, maxWidth: 1400, textAlign: 'center', lineHeight: 1.35,
        }}>Ask which step went wrong first — and what mistake gives exactly your number.</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B09 — the outro. Title, terracotta period, host name, credit lines.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe10Outro: React.FC<{ title?: string; handle?: string; subline?: string }> =
({ title = 'Where It Went Wrong.', handle = 'Param Madan', subline = 'Physics Engine · 10 of 12' }) => {
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
