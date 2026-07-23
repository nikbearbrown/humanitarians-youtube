import { Config } from "@remotion/cli/config";

// JPEG frames render faster; the deck is opaque so no alpha is needed.
Config.setVideoImageFormat("jpeg");
// NOTE: live-HTML decks load katex/d3/their own JS per iframe and can be slow.
// The render script passes `--timeout=120000` (guaranteed CLI flag) for headroom.
Config.overrideWebpackConfig((c) => c);
