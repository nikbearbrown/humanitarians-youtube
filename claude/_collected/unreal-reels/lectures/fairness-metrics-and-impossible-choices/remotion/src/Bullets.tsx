// Bullets.tsx — the text-heavy fallback. When a slide has no D3 chart and no
// authored doodle, we don't stare at it: after the live hold, the slide's key
// points animate in as bullets, one per narration line. Deck typography (Lato),
// NU-red dash markers — matches the deck, not a separate "doodle" style.
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { OVERLAY_FONT as fontFamily } from "./fonts";
import { COLORS, EASE, ENTER, FONTS, NUM_RE } from "./tokens";
import type { CaptionLine } from "./Captions";

const NU_RED = COLORS.red;
const INK = COLORS.ink;
const PAST = COLORS.secondary;

export type Bullet = { text: string; atLine?: number; atFrac?: number };
export type BulletSpec = { title?: string; bullets: Bullet[] };

// set numeric tokens (60%, 0.8, 0.6/0.3) in mono so data reads as data
const withMonoNumbers = (text: string) =>
  text.split(NUM_RE).map((part, i) =>
    NUM_RE.test(part) ? (
      <span key={i} style={{ fontFamily: FONTS.mono, fontSize: "0.92em" }}>{part}</span>
    ) : (
      <span key={i}>{part}</span>
    )
  );

const appearFrame = (b: Bullet, lines: CaptionLine[], hold: number, phase: number, i: number) => {
  if (b.atLine != null && lines.length > 0) {
    const ln = lines[Math.min(b.atLine, lines.length - 1)];
    return Math.max(0, (ln ? ln.startFrame : 0) - hold);
  }
  if (b.atFrac != null) return Math.round(b.atFrac * phase);
  return Math.round((i / 6) * phase); // last-resort even stagger
};

export const Bullets: React.FC<{
  spec: BulletSpec;
  lines: CaptionLine[];
  holdFrames: number;
  phaseFrames: number;
}> = ({ spec, lines, holdFrames, phaseFrames }) => {
  const frame = useCurrentFrame();
  const items = spec.bullets;
  const appears = items.map((b, i) => appearFrame(b, lines, holdFrames, phaseFrames, i));
  let current = -1;
  for (let i = 0; i < appears.length; i++) if (appears[i] <= frame) current = i;

  const n = items.length;
  const size = n > 6 ? 40 : n > 4 ? 48 : 56;
  const gap = n > 6 ? 26 : 34;

  return (
    <AbsoluteFill style={{ background: "#fff", fontFamily, padding: "110px 130px" }}>
      <div style={{ position: "absolute", top: 0, left: 0, right: 0, height: 10, background: NU_RED }} />
      {spec.title ? (
        <>
          <div style={{ fontSize: 68, fontWeight: 400, color: INK, letterSpacing: "-0.01em", maxWidth: 1500 }}>
            {withMonoNumbers(spec.title)}
          </div>
          <div style={{ width: 96, height: 6, background: NU_RED, margin: "26px 0 54px" }} />
        </>
      ) : null}
      <div style={{ display: "flex", flexDirection: "column", gap, maxWidth: 1500 }}>
        {items.map((b, i) => {
          if (frame < appears[i]) return null;
          const local = frame - appears[i];
          const o = interpolate(local, [0, ENTER], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: EASE });
          const isCurrent = i === current;
          return (
            <div
              key={i}
              style={{
                display: "flex",
                alignItems: "flex-start",
                gap: 28,
                opacity: o,
                transform: `translateX(${(1 - o) * -36}px)`,
              }}
            >
              <div style={{ width: 38, height: 6, background: NU_RED, marginTop: size * 0.55, flex: "0 0 auto" }} />
              <div
                style={{
                  fontSize: size,
                  lineHeight: 1.3,
                  fontWeight: isCurrent ? 700 : 400,
                  color: isCurrent ? INK : PAST,
                }}
              >
                {withMonoNumbers(b.text)}
              </div>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
