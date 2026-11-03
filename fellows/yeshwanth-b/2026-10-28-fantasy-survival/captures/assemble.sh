#!/bin/zsh
# Concatenate the harness pieces into capture_driver.gd and copy it into the capture project.
cd "${0:A:h}" && python3 - <<'PY'
core=open('core.gd').read(); surv=open('survival.gd').read(); takes=open('takes.gd').read()
i=surv.index('func snapshot() -> Dictionary:'); j=surv.index('# --- look and walk')
core=core.replace('SNAPSHOT_PLACEHOLDER', surv[:j].rstrip())
header=open('header.txt').read()
open('capture_driver.gd','w').write(header + core + '\n\n' + surv[j:] + '\n' + takes)
PY
cp capture_driver.gd ../capture/harness/
