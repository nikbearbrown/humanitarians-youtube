// EquationTangent.tsx — the fixed equation-tangent template (brutalist/EQUATIONS.md).
// Five zones, revealed in order with the shared easing:
//   1 symbolic form (KaTeX, real math, white-on-dark)
//   2 LHS / RHS as sentences + the relation sign read as a claim
//   3 glossary with a Role column (the row entering is spotlighted red, then settles)
//   4 worked example with an explicit verdict (numbers in mono)
//   5 values claim (pink) — only when the equation encodes a contestable choice
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import katex from "katex";
import "katex/dist/katex.min.css";
import { COLORS, EASE, ENTER, FONTS } from "./tokens";

export type GlossRow = { sym: string; role: string; mean: string; dom: string };
export type TangentSpec = {
  eyebrow: string;
  title: string;
  latex: string;
  lhs: string;
  rhs: string;
  claim: string;
  glossary: GlossRow[];
  example: { scenario: string; compare: string; cost: string };
  values_claim?: string;
  reentry?: string;
};

const NUM = /(\d[\d.,]*\s*%?|≠)/;
const mono = (t: string) =>
  t.split(NUM).map((p, i) =>
    NUM.test(p) ? <span key={i} style={{ fontFamily: FONTS.mono, fontSize: "0.92em" }}>{p}</span> : <span key={i}>{p}</span>
  );

export const EquationTangent: React.FC<{ spec: TangentSpec; phaseFrames: number }> = ({
  spec,
  phaseFrames,
}) => {
  const frame = useCurrentFrame();
  // reveal helper: 0→1 over ENTER frames starting at `frac` of the beat
  const at = (frac: number) =>
    interpolate(frame, [frac * phaseFrames, frac * phaseFrames + ENTER], [0, 1], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
      easing: EASE,
    });
  const rise = (o: number) => `translateY(${(1 - o) * 14}px)`;

  const eqHtml = katex.renderToString(spec.latex, { throwOnError: false, displayMode: true });

  // glossary timing: each row enters in sequence; the freshly-entered row is red
  const gloStart = 0.32;
  const gloStep = 0.06;
  const rowOpacity = (i: number) => at(gloStart + i * gloStep);
  const rowSpotlight = (i: number) => {
    const f0 = (gloStart + i * gloStep) * phaseFrames;
    return interpolate(frame, [f0, f0 + ENTER, f0 + ENTER * 3], [1, 1, 0], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    });
  };
  const exF = 0.72;
  const vcF = 0.88;

  return (
    <AbsoluteFill style={{ background: COLORS.white, fontFamily: FONTS.overlay, padding: "70px 130px" }}>
      <div style={{ position: "absolute", top: 0, left: 0, right: 0, height: 10, background: COLORS.red }} />
      <div style={{ fontSize: 26, fontWeight: 700, letterSpacing: "0.18em", textTransform: "uppercase", color: COLORS.red }}>
        {spec.eyebrow}
      </div>
      <div style={{ fontSize: 56, color: COLORS.ink, marginTop: 8 }}>{spec.title}</div>

      {/* 1 — symbolic form (real math) */}
      <div style={{ background: COLORS.ink, borderRadius: 8, padding: "26px 0", margin: "22px 0 0", textAlign: "center", opacity: at(0) }}>
        <div style={{ color: "#fff", fontSize: 30 }} dangerouslySetInnerHTML={{ __html: eqHtml }} />
      </div>

      {/* 2 — sides as sentences + sign-as-claim */}
      <div style={{ display: "flex", gap: 60, marginTop: 30 }}>
        <div style={{ flex: 1, opacity: at(0.12), transform: rise(at(0.12)) }}>
          <div style={{ fontSize: 20, fontWeight: 700, letterSpacing: "0.1em", color: COLORS.red }}>LEFT SIDE</div>
          <div style={{ fontSize: 28, color: COLORS.ink, marginTop: 6 }}>{spec.lhs}</div>
        </div>
        <div style={{ flex: 1, opacity: at(0.16), transform: rise(at(0.16)) }}>
          <div style={{ fontSize: 20, fontWeight: 700, letterSpacing: "0.1em", color: COLORS.red }}>RIGHT SIDE</div>
          <div style={{ fontSize: 28, color: COLORS.ink, marginTop: 6 }}>{spec.rhs}</div>
        </div>
      </div>
      <div style={{ fontSize: 28, color: COLORS.ink, marginTop: 18, opacity: at(0.24) }}>{spec.claim}</div>

      {/* 3 — glossary with Role column */}
      <div style={{ marginTop: 24 }}>
        {spec.glossary.map((g, i) => {
          const o = rowOpacity(i);
          const hot = rowSpotlight(i);
          const symColor = `rgb(${Math.round(42 + (200 - 42) * hot)}, ${Math.round(26 + (16 - 26) * hot)}, ${Math.round(14 + (46 - 14) * hot)})`;
          return (
            <div key={i} style={{ display: "flex", fontSize: 25, marginBottom: 8, opacity: o }}>
              <div style={{ width: 150, fontFamily: FONTS.mono, fontWeight: 700, color: symColor }}>{g.sym}</div>
              <div style={{ width: 300, color: COLORS.secondary }}>{g.role}</div>
              <div style={{ flex: 1, color: COLORS.ink }}>{g.mean}</div>
              <div style={{ width: 220, fontFamily: FONTS.mono, color: COLORS.secondary }}>{g.dom}</div>
            </div>
          );
        })}
      </div>

      {/* 4 — worked example (white box, red hairline = mechanics) */}
      <div style={{ marginTop: 22, border: `2px solid ${COLORS.red}`, borderRadius: 8, padding: "16px 22px", opacity: at(exF), transform: rise(at(exF)) }}>
        <div style={{ fontSize: 20, fontWeight: 700, letterSpacing: "0.1em", color: COLORS.red }}>WORKED EXAMPLE</div>
        <div style={{ fontSize: 27, color: COLORS.ink, marginTop: 6 }}>{mono(spec.example.scenario)}</div>
        <div style={{ display: "flex", justifyContent: "space-between", marginTop: 8 }}>
          <div style={{ fontSize: 27, fontFamily: FONTS.mono, fontWeight: 700, color: COLORS.red }}>{spec.example.compare}</div>
          <div style={{ fontSize: 22, color: COLORS.secondary, maxWidth: 900, textAlign: "right" }}>{mono(spec.example.cost)}</div>
        </div>
      </div>

      {/* 5 — values claim (pink = a value judgment) */}
      {spec.values_claim ? (
        <div style={{ marginTop: 16, background: "#fdecea", borderRadius: 8, padding: "14px 22px", opacity: at(vcF) }}>
          <div style={{ fontSize: 20, fontWeight: 700, letterSpacing: "0.1em", color: COLORS.red }}>VALUES CLAIM</div>
          <div style={{ fontSize: 25, color: COLORS.ink, marginTop: 4 }}>{spec.values_claim}</div>
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
