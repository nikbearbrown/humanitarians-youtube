# SOURCES — stable-element-refs

Every on-screen claim, number, and code snippet mapped to its source.

## Core facts

| Claim | Value | Source |
|---|---|---|
| Button "Confirm Order" at (960,540) on 1920×1080 | exact per card | video-ideas.md Candidate 2 example seed |
| After resize to 1440×900, button moves to (720,405) | exact per card | same |
| ref="confirm_order_1" persists across resize | exact per card | same |
| JavaScript setAttribute for stable refs | `element.setAttribute('data-ref', ...)` | browser-use-demo browser_element_script.js pattern |
| Source folder | `browser_use_demo/browser_tool_utils/` | video-ideas.md Candidate 2 source |

## Beat-level citations

- B01 coords: 960,540 on 1920×1080; 720,405 on 1440×900 — both from the card's example seed
- B03 morph: two-state animation uses the same coords from the seed

Source credit shown on screen: "Source: Claude Quickstarts (Anthropic)"
