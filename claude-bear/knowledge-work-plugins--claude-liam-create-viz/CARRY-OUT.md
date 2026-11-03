# CARRY-OUT.md

**Carry-out line:** Create-viz doesn't start by making a chart pretty — it
starts by matching the chart type to what the data actually shows. Style
comes after accuracy, never instead of it.

**Wrong guess it's built to defeat:** that "create a visualization" means
Claude will just make an existing chart idea look nicer — pick some colors,
clean it up. The actual order is reversed: the skill first reads the
*relationship* in the data (a trend, a comparison, a distribution, a
correlation) and picks the chart type from a fixed table before any styling
happens, then enforces rules that can't be styled away — bar charts start at
zero, axis breaks are never hidden, colors carry meaning instead of
decoration.

**Secondhand test:** "It doesn't make your chart pretty — it picks the right
chart for what your data shows, then keeps it honest" survives being
repeated by someone who wasn't fully listening, and stays true. It
compresses the distinction that matters (chart-type selection + accuracy
rules vs. decoration), not the topic (data visualization in general).
