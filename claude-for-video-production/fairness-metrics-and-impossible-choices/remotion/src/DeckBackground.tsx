// DeckBackground.tsx — the deck slide behind the narration.
//
// mode "live"  → a live deck.html#<index> iframe (authored CSS/D3 animations play,
//                but reloads the whole deck — heavy). Used for the 8 D3 chart slides.
// mode "still" → a prerendered PNG of the slide (from prerender_deck.py), faded in
//                on Remotion's clock. Used for the ~3.5s "hold" before a doodle/
//                bullets slide — no iframe reload, so the render is fast + smooth.
//                The only thing lost vs live is the slide's entry fade, which we
//                re-add here as the Remotion fade-in.
import { AbsoluteFill, IFrame, Img, interpolate, staticFile, useCurrentFrame } from "remotion";
import { EASE } from "./tokens";

export const DeckBackground: React.FC<{
  slideIndex: number;
  fadeInFrames: number;
  mode?: "live" | "still";
}> = ({ slideIndex, fadeInFrames, mode = "live" }) => {
  const frame = useCurrentFrame();

  if (mode === "still") {
    const o = interpolate(frame, [0, Math.max(fadeInFrames, 8)], [0, 1], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
      easing: EASE,
    });
    return (
      <AbsoluteFill style={{ background: "#fff", opacity: o }}>
        <Img src={staticFile(`deck-stills/slide-${slideIndex}.png`)} style={{ width: 1920, height: 1080 }} />
      </AbsoluteFill>
    );
  }

  const opacity =
    fadeInFrames > 0
      ? interpolate(frame, [0, fadeInFrames], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" })
      : 1;
  return (
    <div style={{ width: "100%", height: "100%", background: "#000", opacity }}>
      <IFrame
        src={`${staticFile("deck/deck.html")}#${slideIndex}`}
        style={{ width: 1920, height: 1080, border: "none", display: "block" }}
        key={`slide-${slideIndex}`}
      />
    </div>
  );
};
