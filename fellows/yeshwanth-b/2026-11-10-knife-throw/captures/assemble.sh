#!/bin/zsh
# Concatenate the harness pieces into capture_driver.gd and copy it into the capture project.
cd "${0:A:h}" && cat core.gd takes.gd > capture_driver.gd && cp capture_driver.gd capture/harness/ || exit 1
cp run_take.sh capture/harness/
