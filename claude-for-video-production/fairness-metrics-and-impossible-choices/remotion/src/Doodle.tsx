// Doodle.tsx — Remotion-native progressive-disclosure sketch (bears-doodles style:
// line art on white, one narration line = one new element drawn on). No Manim.
//
// A doodle is a declarative spec: a list of elements, each tied to a caption line
// (`atLine`). The element draws on at the frame that line is spoken. Strokes use
// pathLength=1 + dashoffset so the draw-on is deterministic (no DOM measuring).
//
// Coordinates are on a 1920x1080 board. Timing comes from the slide's caption
// lines (slide-local frames); this component runs inside the post-hold Sequence,
// so it subtracts holdFrames to get phase-local appear times.
import { interpolate, useCurrentFrame } from "remotion";
import { OVERLAY_FONT as fontFamily } from "./fonts"; // local Inter, matches the other overlays
import { COLORS, DRAW as DRAW_F, EASE, ENTER, FONTS } from "./tokens";
import type { CaptionLine } from "./Captions";
const INK = COLORS.ink; // brutalist DESIGN.md warm ink (no pure black, no blue)
const DRAW = DRAW_F; // frames to draw a stroke
const FADE = ENTER; // frames to fade in a label/dots
const isNumeric = (s: string) => /^\s*[\d.,/%\s]+$/.test(s) && /\d/.test(s);

// timing: `atLine` ties the element to a caption line (preferred — locks to the
// spoken word); `atFrac` schedules it at a fraction of the doodle window (used when
// captions aren't available yet). One of the two should be set.
type Timing = { atLine?: number; atFrac?: number };

export type DoodleEl = Timing &
  (
    | { kind: "label"; text: string; x: number; y: number; size?: number; color?: string; anchor?: "start" | "middle" | "end" }
    | { kind: "rect"; x: number; y: number; w: number; h: number; color?: string }
    | { kind: "line"; x1: number; y1: number; x2: number; y2: number; color?: string }
    | { kind: "arrow"; x1: number; y1: number; x2: number; y2: number; color?: string }
    | { kind: "circle"; cx: number; cy: number; r: number; color?: string }
    | { kind: "dots"; x: number; y: number; cols: number; rows: number; gap: number; filled: number; color?: string }
  );

export type DoodleSpec = { title?: string; elements: DoodleEl[] };

const appearFrame = (el: Timing, lines: CaptionLine[], hold: number, phaseFrames: number) => {
  if (el.atLine != null && lines.length > 0) {
    const ln = lines[Math.min(el.atLine, lines.length - 1)];
    return Math.max(0, (ln ? ln.startFrame : 0) - hold);
  }
  if (el.atFrac != null) return Math.round(el.atFrac * phaseFrames);
  return 0;
};

export const Doodle: React.FC<{
  spec: DoodleSpec;
  lines: CaptionLine[];
  holdFrames: number;
  phaseFrames: number;
}> = ({ spec, lines, holdFrames, phaseFrames }) => {
  const frame = useCurrentFrame();

  const drawn = (appear: number) => interpolate(frame - appear, [0, DRAW], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: EASE,
  });
  const faded = (appear: number) => interpolate(frame - appear, [0, FADE], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: EASE,
  });

  return (
    <svg viewBox="0 0 1920 1080" style={{ width: "100%", height: "100%", background: "#fff" }}>
      {spec.title ? (
        <text x={120} y={130} fontFamily={fontFamily} fontSize={66} fill={INK} fontWeight={700}>
          {spec.title}
        </text>
      ) : null}
      {spec.elements.map((el, i) => {
        const appear = appearFrame(el, lines, holdFrames, phaseFrames);
        if (frame < appear) return null;
        const color = el.color || INK;
        const d = drawn(appear);
        const o = faded(appear);
        const strokeProps = {
          stroke: color,
          strokeWidth: 4,
          fill: "none",
          strokeLinecap: "round" as const,
          strokeLinejoin: "round" as const,
          pathLength: 1,
          strokeDasharray: 1,
          strokeDashoffset: 1 - d,
        };
        switch (el.kind) {
          case "label":
            return (
              <text key={i} x={el.x} y={el.y} opacity={o} fill={color}
                fontFamily={isNumeric(el.text) ? FONTS.mono : fontFamily} fontSize={el.size || 46}
                textAnchor={el.anchor || "start"}
                transform={`translate(0 ${(1 - o) * 14})`}>
                {el.text}
              </text>
            );
          case "rect":
            return <rect key={i} x={el.x} y={el.y} width={el.w} height={el.h} rx={10} {...strokeProps} />;
          case "line":
            return <line key={i} x1={el.x1} y1={el.y1} x2={el.x2} y2={el.y2} {...strokeProps} />;
          case "circle":
            return <circle key={i} cx={el.cx} cy={el.cy} r={el.r} {...strokeProps} />;
          case "arrow": {
            const ang = Math.atan2(el.y2 - el.y1, el.x2 - el.x1);
            const hl = 22;
            const ax = el.x2 - hl * Math.cos(ang - Math.PI / 6);
            const ay = el.y2 - hl * Math.sin(ang - Math.PI / 6);
            const bx = el.x2 - hl * Math.cos(ang + Math.PI / 6);
            const by = el.y2 - hl * Math.sin(ang + Math.PI / 6);
            return (
              <g key={i}>
                <line x1={el.x1} y1={el.y1} x2={el.x2} y2={el.y2} {...strokeProps} />
                <path d={`M${ax} ${ay} L${el.x2} ${el.y2} L${bx} ${by}`}
                  stroke={color} strokeWidth={4} fill="none" strokeLinecap="round"
                  strokeLinejoin="round" opacity={d} />
              </g>
            );
          }
          case "dots": {
            const dots = [];
            let n = 0;
            for (let r = 0; r < el.rows; r++) {
              for (let c = 0; c < el.cols; c++) {
                const isFilled = n < el.filled;
                dots.push(
                  <circle key={`${i}-${n}`} cx={el.x + c * el.gap} cy={el.y + r * el.gap} r={12}
                    fill={isFilled ? color : "none"} stroke={color} strokeWidth={3} opacity={o} />
                );
                n++;
              }
            }
            return <g key={i}>{dots}</g>;
          }
          default:
            return null;
        }
      })}
    </svg>
  );
};
