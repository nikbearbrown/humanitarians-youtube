// theme.ts — caption look, matched to the music-video pipeline
// (aspects/songbird/muzak-overlay theme): Inter 800, white text with a heavy
// shadow, gold accent on emphasis, per-word karaoke highlight. Lecture captions
// sit in the lower band so they never cover slide content.
export const theme = {
  fontFamily: "Inter, system-ui, sans-serif",
  fontWeight: 800,
  lineSize: 52, // px (slightly under the music-video 58 — lecture lines are longer)
  textColor: "#FFFFFF", // sung + current
  currentColor: "#FFFFFF", // brightest word
  sungOpacity: 0.85,
  upcomingOpacity: 0.5,
  accent: "#E0B15E", // amber gold (matches music-video hook color)
  textShadow: "0 2px 18px rgba(0,0,0,0.65)",

  // fade per line
  lineInFrames: 6,
  lineOutFrames: 5,

  // placement — lower band, centered horizontally
  bandCenterY: 0.86, // fraction of frame height
  maxWidth: "78%",

  // legibility scrim behind the caption band
  scrimHeight: 0.26, // fraction of frame height, centered on bandCenterY
  scrimOpacity: 0.55,
};
