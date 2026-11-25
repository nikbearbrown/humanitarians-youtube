// B01 · pitch: a sung note is a wave that repeats. A copy of the wave slides along it; where the two line up, the
// slide is one period: 2.23 ms -> 448 Hz. The wave and the line-up score are autotune.py's own frame (the A4, 1.26 s).
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 32, exposure: 1.15 });
  K.lights(scene, 0xffffff, 0x553366);
  const c = env.cue, D = env.D, d = env.data;
  scene.add(K.grid(60, 60, 0x6a4a7a, 0.16, -2.4));
  const dust = K.dust(scene, 360, 16, 0xd8a8ff, 0.06, 13);
  const XW = 0.75;                                     // scene units per millisecond
  const wave = d.wave, step = d.step_ms, tau = d.tau_ms;
  const pk = Math.max(...wave.map(Math.abs));
  const N = wave.length, x0 = -(N - 1) * step * XW / 2;
  const pts = wave.map((v, i) => new THREE.Vector3(x0 + i * step * XW, (v / pk) * 1.25, 0));
  const orig = K.tubeN(pts, 0.05, 0xff6fa8, 1, 900, 10); scene.add(orig);
  const origGlow = K.tubeN(pts, 0.16, 0xff6fa8, 0.18, 900, 10); scene.add(origGlow);
  const copy = K.tubeN(pts.map((p) => new THREE.Vector3(p.x, p.y, 0.3)), 0.045, 0xffc857, 0.0, 900, 10); scene.add(copy);
  const copyGlow = K.tubeN(pts.map((p) => new THREE.Vector3(p.x, p.y, 0.3)), 0.15, 0xffc857, 0.0, 900, 10); scene.add(copyGlow);
  // one marker per repeat (period boundaries, at the wave's peaks)
  let i0 = 0; for (let i = 0; i < Math.round(tau / step); i++) if (wave[i] > wave[i0]) i0 = i;
  const marks = [];
  for (let k = 0; k < 8; k++) {
    const x = x0 + (i0 * step + k * tau) * XW;
    if (x > -x0) break;
    const m = K.slab(0.03, 3.4, 0xb79cff, 0); m.position.set(x, 0, -0.05); scene.add(m);
    const gl = K.glow(0xb79cff, 0.9, 0); gl.position.set(x, 1.85, -0.05); scene.add(gl);
    marks.push({ m, gl });
  }
  const lockRing = K.glow(0xffc857, 5, 0); lockRing.position.set(0, 0, 0.2); scene.add(lockRing);
  const cm = d.cmnd, cmAt = (lag) => { const f = lag / step, i = Math.min(cm.length - 2, Math.floor(f)), a = f - i; return cm[i] * (1 - a) + cm[i + 1] * a; };
  const tS = c.slides, tL = Math.max(c.line, c.slides + 1.2);

  return function renderAt(t) {
    const show = K.prog(t, 0.1, 1.2);
    orig.material.opacity = show; origGlow.material.opacity = 0.18 * show;
    K.drawTube(orig, K.prog(t, 0.1, 2.2, K.ease.inOut)); K.drawTube(origGlow, K.prog(t, 0.1, 2.2, K.ease.inOut));
    // count the repeats on "is its pitch"
    marks.forEach((o, k) => {
      const on = K.prog(t, c.pitch + k * 0.18, 0.35) * (1 - 0.6 * K.prog(t, c.slides, 0.6));
      o.m.material.opacity = 0.45 * on; o.gl.material.opacity = on;
    });
    // the slide: 0 -> 1.45 periods, then settle back on one period exactly at "line up"
    let lag = 0;
    if (t > tS) {
      const a = K.prog(t, tS, (tL - tS) * 0.72, K.ease.inOut);
      const b = K.prog(t, tS + (tL - tS) * 0.72, (tL - tS) * 0.28 + 0.15, K.ease.inOut);
      lag = tau * (1.45 * a - 0.45 * b);
    }
    const cOn = K.prog(t, tS - 0.3, 0.5);
    copy.position.x = copyGlow.position.x = lag * XW;
    const match = Math.exp(-Math.pow((lag - tau) / (tau * 0.06), 2));
    copy.material.opacity = cOn * (0.55 + 0.45 * match); copyGlow.material.opacity = cOn * (0.12 + 0.3 * match);
    lockRing.material.opacity = cOn * match * (0.55 + 0.15 * Math.sin(t * 5)) * K.prog(t, tL - 0.2, 0.4);
    // HUD: the dot rides the line-up curve
    const dot = document.getElementById("cm-dot");
    if (dot) {
      const svg = dot.ownerSVGElement, pw = svg.width.baseVal.value, ph = svg.height.baseVal.value;
      const lagmax = step * (cm.length - 1);
      dot.setAttribute("cx", (Math.min(lag, lagmax) / lagmax * pw).toFixed(1));
      dot.setAttribute("cy", (Math.min(cmAt(Math.min(lag, lagmax)), 1.6) / 1.6 * ph).toFixed(1));
      dot.style.opacity = cOn.toFixed(3);
    }
    K.setText("lagpin", `SLID ${lag.toFixed(2)} ms`);
    K.pin("lagpin", new THREE.Vector3(copy.position.x + x0 + (N - 1) * step * XW * 0.3, 1.95, 0.3), cam, env, cOn * 0.95);
    K.pin("perpin", new THREE.Vector3(x0 + (i0 * step + 2.5 * tau) * XW, -1.9, 0), cam, env,
      K.prog(t, c.pitch, 0.5) * (1 - K.prog(t, c.slides, 0.5)));
    // camera: a slow drift around the wave
    const ca = K.deg(-18 + 16 * (t / D)), cr = env.portrait ? 13.5 : 12.2;
    cam.position.set(Math.sin(ca) * cr, 2.2 + 0.6 * Math.sin(t * 0.2), Math.cos(ca) * cr);
    cam.lookAt(0, -0.1, 0);
    dust(t);
    r.render(scene, cam);
  };
}
