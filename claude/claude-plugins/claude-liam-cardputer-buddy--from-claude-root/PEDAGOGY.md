# PEDAGOGY — claude-liam-cardputer-buddy

## Skill reviewed
`anthropics/claude-plugins-official/plugins/cwc-makers/skills/cardputer-buddy/SKILL.md`

## What learners will be able to do
- Distinguish when this skill applies: iterate-after-provisioning, not first install (m5-onboard)
- Understand the /flash/ device layout and launcher auto-discovery (every .py in apps/ = menu entry)
- Use hello_cardputer.py as the canonical template for keyboard polling, font, and exit
- Choose the correct push script: install_apps.py (full push) vs push.py (single file)
- Use tail_serial.py and repl_run.py for live debugging

## What makes this teachable
The launcher auto-discovery pattern (scan apps/ at boot) is elegant and requires no registration code.
The three dev-loop scripts have clear scope separation when explained together.
The template reference (hello_cardputer.py) is concrete and learnable.

## Gaps the teardown surfaces
- PORT rediscovery: detect.py is from provisioning session; no guidance if port changes
- push.py vs install_apps.py distinction buried — easy to reach for the wrong one
- BLE flow in claude_buddy.py referenced but protocol not documented
- hello_cardputer.py named as template but required function signatures not spelled out inline

## VERDICT: PASS

Trigger distinction, device layout, and three dev-loop scripts are complete and concrete.
Teardown adds value by surfacing the PORT gap and the two-push-script ambiguity.
