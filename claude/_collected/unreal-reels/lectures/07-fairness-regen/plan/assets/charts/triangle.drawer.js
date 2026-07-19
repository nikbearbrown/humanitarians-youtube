(c) => {
      clear(c);
      const W = 1000, H = 600;
      const svg = svgIn(c, W, H);
      const nodes = [
        { id: 'cal', t: 'Calibration parity', s: 'honest probabilities', x: W / 2, y: 130 },
        { id: 'eo', t: 'Equalized odds', s: 'equal error rates', x: 180, y: 470 },
        { id: 'dp', t: 'Demographic parity', s: 'equal positive rate', x: W - 180, y: 470 },
      ];
      const by = Object.fromEntries(nodes.map((n) => [n.id, n]));
      const edges = [['cal', 'eo'], ['eo', 'dp'], ['cal', 'dp']];
      const eKey = (a, b) => [a, b].sort().join('-');

      const eg = svg.append('g');
      const lines = {};
      edges.forEach(([a, b]) => {
        const p = by[a], q = by[b];
        const L = eg.append('line').attr('x1', p.x).attr('y1', p.y).attr('x2', q.x).attr('y2', q.y)
          .attr('stroke', N2).attr('stroke-width', 5).attr('stroke-linecap', 'round')
          .attr('opacity', 0);
        const len = Math.hypot(q.x - p.x, q.y - p.y);
        L.attr('stroke-dasharray', len).attr('stroke-dashoffset', len)
          .transition().duration(D).attr('opacity', 1).attr('stroke-dashoffset', 0);
        lines[eKey(a, b)] = L;
      });

      const ng = svg.append('g');
      const groups = {};
      nodes.forEach((n, i) => {
        const g = ng.append('g').attr('transform', `translate(${n.x},${n.y})`).attr('opacity', 0);
        g.append('circle').attr('r', 19).attr('fill', BLACK);
        g.append('text').attr('text-anchor', 'middle').attr('y', -34)
          .attr('font-family', FONT).attr('font-weight', 700).attr('font-size', 27).attr('fill', BLACK)
          .text(n.t);
        g.append('text').attr('text-anchor', 'middle').attr('y', -8)
          .attr('font-family', FONT).attr('font-size', 19).attr('fill', N4)
          .text(n.s);
        const badge = g.append('text').attr('text-anchor', 'middle').attr('y', 50)
          .attr('font-family', FONT).attr('font-weight', 700).attr('font-size', 21).attr('fill', RED)
          .attr('opacity', 0).text('breaks');
        g.transition().delay(D * 0.5 + i * 120).duration(D * 0.6).attr('opacity', 1);
        groups[n.id] = { g, badge, circle: g.select('circle') };
      });

      const caption = svg.append('text').attr('x', W / 2).attr('y', H - 6)
        .attr('text-anchor', 'middle').attr('font-family', FONT).attr('font-size', 24).attr('fill', N5);

      const order = ['cal', 'dp', 'eo']; // which one breaks
      let k = 0;
      const tick = () => {
        const broken = order[k];
        const kept = nodes.map((n) => n.id).filter((id) => id !== broken);
        nodes.forEach((n) => {
          const o = groups[n.id];
          const isBroken = n.id === broken;
          o.circle.transition().duration(420)
            .attr('fill', isBroken ? '#fff' : BLACK)
            .attr('stroke', isBroken ? RED : 'none')
            .attr('stroke-width', isBroken ? 4 : 0)
            .attr('stroke-dasharray', isBroken ? '4 4' : 'none');
          o.badge.transition().duration(420).attr('opacity', isBroken ? 1 : 0);
          o.g.transition().duration(420).attr('opacity', isBroken ? 0.55 : 1);
        });
        edges.forEach(([a, b]) => {
          const L = lines[eKey(a, b)];
          const satisfied = a !== broken && b !== broken;
          L.transition().duration(420)
            .attr('stroke', satisfied ? RED : N1)
            .attr('stroke-width', satisfied ? 7 : 4)
            .attr('stroke-dasharray', satisfied ? 'none' : '6 8');
        });
        const nm = { cal: 'calibration', eo: 'equalized odds', dp: 'demographic parity' };
        caption.text(`Keep ${nm[kept[0]]} + ${nm[kept[1]]}  →  ${nm[broken]} must give`);
        k = (k + 1) % order.length;
      };
      setTimeout(tick, D + 200);
      if (!RM) this._timer = setInterval(tick, 2600);
    }
