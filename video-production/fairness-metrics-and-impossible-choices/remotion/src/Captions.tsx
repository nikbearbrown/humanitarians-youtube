// Captions.tsx — per-slide karaoke captions, frames LOCAL to the slide.
//
// Same renderer idea as the music-video LyricLayer karaoke branch: each word
// lights at the frame it is actually spoken (from forced alignment), upcoming
// words sit dim, sung words recede. Exact narration text, no drift.
import {
  AbsoluteFill,
  interpolate,
  useCurrentFrame,
} from "remotion";
import { OVERLAY_FONT as fontFamily } from "./fonts"; // local Inter (loaded from a real file)
import { theme } from "./theme";

export type CaptionWord = { text: string; startFrame: number; endFrame: number };
export type CaptionLine = {
  text: string;
  startFrame: number;
  endFrame: number;
  words: CaptionWord[];
};

export const Captions: React.FC<{ lines: CaptionLine[] }> = ({ lines }) => {
  const frame = useCurrentFrame();

  // active line = the last line whose window contains the current frame
  let active: CaptionLine | null = null;
  for (const ln of lines) {
    if (frame >= ln.startFrame && frame <= ln.endFrame + theme.lineOutFrames) {
      active = ln;
    }
  }
  if (!active) return null;

  const local = frame - active.startFrame;
  const remaining = active.endFrame - frame;
  const inOp = interpolate(local, [0, theme.lineInFrames], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const outOp = interpolate(remaining, [0, theme.lineOutFrames], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const opacity = Math.min(inOp, outOp);

  // current word = last word whose onset has passed
  let cur = -1;
  for (let i = 0; i < active.words.length; i++) {
    if (active.words[i].startFrame <= frame) cur = i;
  }

  return (
    <AbsoluteFill>
      {/* legibility scrim */}
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: `${(theme.bandCenterY - theme.scrimHeight / 2) * 100}%`,
          height: `${theme.scrimHeight * 100}%`,
          background: `linear-gradient(to bottom, rgba(0,0,0,0), rgba(0,0,0,${theme.scrimOpacity}) 45%, rgba(0,0,0,${theme.scrimOpacity}) 55%, rgba(0,0,0,0))`,
          opacity,
        }}
      />
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: `${theme.bandCenterY * 100}%`,
          transform: "translateY(-50%)",
          display: "flex",
          justifyContent: "center",
        }}
      >
        <div
          style={{
            fontFamily,
            fontWeight: theme.fontWeight,
            fontSize: theme.lineSize,
            lineHeight: 1.2,
            textAlign: "center",
            maxWidth: theme.maxWidth,
            textShadow: theme.textShadow,
            opacity,
            display: "flex",
            gap: 14,
            flexWrap: "wrap",
            justifyContent: "center",
          }}
        >
          {active.words.map((w, i) => {
            const state = i > cur ? "upcoming" : i === cur ? "current" : "sung";
            const wo =
              state === "upcoming"
                ? theme.upcomingOpacity
                : state === "current"
                ? 1
                : theme.sungOpacity;
            return (
              <span
                key={i}
                style={{
                  opacity: Math.min(wo, outOp),
                  color: state === "current" ? theme.currentColor : theme.textColor,
                  display: "inline-block",
                }}
              >
                {w.text}
              </span>
            );
          })}
        </div>
      </div>
    </AbsoluteFill>
  );
};
