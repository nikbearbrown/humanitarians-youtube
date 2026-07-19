// fonts.ts — overlay + mono typefaces, loaded from real local files.
//
// Font loading MUST happen inside a component (render scope), not at module scope:
// calling delayRender() during webpack module-eval throws before Remotion's scope
// exists (that was the crash). So we expose a hook the root component calls. Uses
// only the core `remotion` package — no extra @remotion/* package (avoids version
// mismatch). Live deck slides keep Lato (loaded in their own iframe).
import { useEffect, useState } from "react";
import { continueRender, delayRender, staticFile } from "remotion";

export const OVERLAY_FONT = "InterLocal";
export const MONO_FONT = "JetBrainsMonoLocal, ui-monospace, Menlo, monospace";

const FACES: ReadonlyArray<[string, string, string]> = [
  ["InterLocal", "fonts/Inter-Regular.ttf", "400"],
  ["InterLocal", "fonts/Inter-Bold.ttf", "700"],
  ["JetBrainsMonoLocal", "fonts/JetBrainsMono-Regular.ttf", "400"],
  ["JetBrainsMonoLocal", "fonts/JetBrainsMono-Bold.ttf", "700"],
];

export const useOverlayFonts = () => {
  const [handle] = useState(() => delayRender("overlay-fonts"));
  useEffect(() => {
    Promise.all(
      FACES.map(([family, url, weight]) => {
        const face = new FontFace(family, `url(${staticFile(url)})`, { weight });
        return face.load().then((loaded) => {
          (document.fonts as FontFaceSet).add(loaded);
        });
      })
    ).finally(() => continueRender(handle));
  }, [handle]);
};
