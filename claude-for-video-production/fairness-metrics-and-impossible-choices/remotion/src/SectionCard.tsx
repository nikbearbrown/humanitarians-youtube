// SectionCard.tsx — native Remotion render of the title / "Part N" divider / close
// slides, so they DON'T reload the deck iframe (that reload hitched the export at
// each section boundary). Mirrors the deck's divider look (red or black card, red
// accent, eased rise) and animates on Remotion's own clock — smooth + deterministic.
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { OVERLAY_FONT as fontFamily } from "./fonts";
import { COLORS, EASE } from "./tokens";

export type SectionSpec = {
  eyebrow: string;
  title: string;
  subtitle?: string;
  bg: "red" | "black";
};

export const SectionCard: React.FC<{ spec: SectionSpec }> = ({ spec }) => {
  const frame = useCurrentFrame();
  const onRed = spec.bg === "red";
  const bg = onRed ? COLORS.red : "#111111";
  const eyebrowColor = onRed ? "rgba(255,255,255,0.82)" : COLORS.red;
  const subColor = onRed ? "rgba(255,255,255,0.92)" : "#c9c4bd";

  // staggered eased rise (no bounce), Remotion clock
  const rise = (delay: number) => {
    const o = interpolate(frame, [delay, delay + 12], [0, 1], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
      easing: EASE,
    });
    return { opacity: o, transform: `translateY(${(1 - o) * 22}px)` };
  };

  return (
    <AbsoluteFill style={{ background: bg, fontFamily, padding: "0 130px", justifyContent: "center" }}>
      {!onRed ? (
        <div style={{ position: "absolute", top: 0, left: 0, right: 0, height: 10, background: COLORS.red }} />
      ) : null}
      <div style={{ fontSize: 26, fontWeight: 700, letterSpacing: "0.18em", textTransform: "uppercase", color: eyebrowColor, ...rise(0) }}>
        {spec.eyebrow}
      </div>
      <div style={{ fontSize: 104, lineHeight: 1.02, color: "#fff", letterSpacing: "-0.02em", maxWidth: 1500, marginTop: 30, ...rise(4) }}>
        {spec.title}
      </div>
      <div style={{ width: 120, height: 8, background: onRed ? "rgba(255,255,255,0.9)" : COLORS.red, margin: "40px 0 0", ...rise(8) }} />
      {spec.subtitle ? (
        <div style={{ fontSize: 34, lineHeight: 1.3, color: subColor, maxWidth: 1300, marginTop: 36, ...rise(10) }}>
          {spec.subtitle}
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
