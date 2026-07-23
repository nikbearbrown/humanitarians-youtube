(c) => {
      clear(c);
      const wrap = d3.select(c);
      const data = {
        calib: { rows: [['TPR', 0.83, 0.50], ['FPR', 0.20, 0.10], ['PPV', 0.86, 0.83]], note: 'Calibration holds · equalized odds breaks — TPR differs sharply between groups.' },
        eo: { rows: [['TPR', 0.70, 0.70], ['FPR', 0.15, 0.15], ['PPV', 0.88, 0.67]], note: 'Equalized odds holds · calibration breaks — PPV (precision) diverges.' },
      };
      let cur = 'calib';
      const btnRow = wrap.append('div').style('display', 'flex').style('gap', '12px').style('margin', '4px 0 8px');
      const note = wrap.append('div').style('font', `600 25px ${FONT}`).style('color', N7).style('min-height', '34px').style('margin-bottom', '6px');
      const W = 1480, H = 500, m = { t: 30, r: 30, b: 60, l: 70 };
      const svg = svgIn(wrap.node(), W, H);
      const x0 = d3.scaleBand().domain(['TPR', 'FPR', 'PPV']).range([m.l, W - m.r]).padding(0.34);
      const x1 = d3.scaleBand().domain(['a', 'b']).range([0, x0.bandwidth()]).padding(0.18);
      const y = d3.scaleLinear().domain([0, 1]).range([H - m.b, m.t]);
      // gridlines + axis
      svg.append('g').selectAll('line').data(y.ticks(5)).join('line')
        .attr('x1', m.l).attr('x2', W - m.r).attr('y1', y).attr('y2', y)
        .attr('stroke', N1).attr('stroke-width', 1);
      svg.append('g').selectAll('text').data(y.ticks(5)).join('text')
        .attr('x', m.l - 14).attr('y', (d) => y(d) + 5).attr('text-anchor', 'end')
        .attr('font-family', FONT).attr('font-size', 18).attr('fill', N4)
        .text(d3.format('.0%'));
      svg.append('line').attr('x1', m.l).attr('x2', W - m.r).attr('y1', y(0)).attr('y2', y(0)).attr('stroke', BLACK).attr('stroke-width', 2);
      svg.selectAll('text.mx').data(['TPR', 'FPR', 'PPV']).join('text').attr('class', 'mx')
        .attr('x', (d) => x0(d) + x0.bandwidth() / 2).attr('y', H - m.b + 34).attr('text-anchor', 'middle')
        .attr('font-family', FONT).attr('font-weight', 700).attr('font-size', 24).attr('fill', BLACK).text((d) => d);
      // legend
      const leg = svg.append('g').attr('transform', `translate(${W - m.r - 290},${m.t - 4})`);
      [['Group A · base rate 0.6', RED], ['Group B · base rate 0.3', N4]].forEach((d, i) => {
        const g = leg.append('g').attr('transform', `translate(0,${i * 26})`);
        g.append('rect').attr('width', 18).attr('height', 18).attr('fill', d[1]);
        g.append('text').attr('x', 26).attr('y', 14).attr('font-family', FONT).attr('font-size', 18).attr('fill', N5).text(d[0]);
      });
      const barG = svg.append('g');
      const lblG = svg.append('g');
      const draw = () => {
        note.text(data[cur].note);
        const flat = [];
        data[cur].rows.forEach((r) => { flat.push({ m: r[0], g: 'a', v: r[1] }); flat.push({ m: r[0], g: 'b', v: r[2] }); });
        const bars = barG.selectAll('rect').data(flat, (d) => d.m + d.g);
        bars.join(
          (en) => en.append('rect')
            .attr('x', (d) => x0(d.m) + x1(d.g)).attr('width', x1.bandwidth())
            .attr('y', y(0)).attr('height', 0)
            .attr('fill', (d) => d.g === 'a' ? RED : N4),
          (up) => up,
        ).transition().duration(D)
          .attr('x', (d) => x0(d.m) + x1(d.g)).attr('width', x1.bandwidth())
          .attr('y', (d) => y(d.v)).attr('height', (d) => y(0) - y(d.v))
          .attr('fill', (d) => d.g === 'a' ? RED : N4);
        const labs = lblG.selectAll('text').data(flat, (d) => d.m + d.g);
        labs.join(
          (en) => en.append('text').attr('text-anchor', 'middle')
            .attr('font-family', FONT).attr('font-weight', 700).attr('font-size', 19).attr('fill', BLACK)
            .attr('opacity', 0),
          (up) => up,
        ).attr('x', (d) => x0(d.m) + x1(d.g) + x1.bandwidth() / 2)
          .text((d) => d3.format('.2f')(d.v))
          .transition().duration(D)
          .attr('y', (d) => y(d.v) - 10).attr('opacity', 1);
      };
      const mkBtn = (id, label) => {
        const b = btnRow.append('button').text(label)
          .style('font', `700 21px ${FONT}`).style('padding', '11px 22px')
          .style('border', `2px solid ${BLACK}`).style('cursor', 'pointer')
          .style('border-radius', '0').style('transition', 'all .2s');
        const paint = () => {
          const on = cur === id;
          b.style('background', on ? RED : '#fff').style('color', on ? '#fff' : BLACK)
            .style('border-color', on ? RED : BLACK);
        };
        b.on('click', () => { cur = id; btns.forEach((p) => p()); draw(); });
        const paintRef = paint; paint();
        return paintRef;
      };
      const btns = [];
      btns.push(mkBtn('calib', 'Calibration holds'));
      btns.push(mkBtn('eo', 'Equalized odds holds'));
      draw();
    }
