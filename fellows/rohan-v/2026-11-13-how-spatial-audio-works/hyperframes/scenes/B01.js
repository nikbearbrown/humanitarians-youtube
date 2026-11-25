// B01 · timing (ITD): a sound on your right reaches the right ear first; the gap shrinks as it moves in front.
// Wavefronts are slowed down ~1e5x so you can watch them; the HUD numbers are spatial.py's measured ITDs.
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 34, exposure: 1.2 });
  K.lights(scene, 0xffffff, 0x404a99);
  const c = env.cue, D = env.D;
  const head = K.headModel(); scene.add(head.g);
  scene.add(K.polarFloor(6.5, 0x5f6bd6, -1.25, 0.2));
  const dust = K.dust(scene, 380, 14, 0x8a9bff, 0.06, 11);
  const src = K.source(0xffb454, 0.2); scene.add(src);
  const N = 7, rings = [];
  for (let i = 0; i < N; i++) { const m = K.ripple(0xffb454, 0.7); scene.add(m); rings.push(m); }
  const shells = [];
  for (let i = 0; i < N; i++) { const m = K.shell(0xffb454, 0.03); scene.add(m); shells.push(m); }
  // the two paths: straight to the near ear, around the head to the far ear
  const pathR = K.trail(80, 0x5ce1ff, 1), pathL = K.trail(120, 0xc39bff, 1);
  scene.add(pathR, pathL);
  const itd = env.data.itd;
  const itdAt = (dg) => { dg = Math.min(90, Math.max(0, dg)); const i = Math.min(5, Math.floor(dg / 15)); const f = (dg - i * 15) / 15;
    return itd[i].measured_ms + (itd[i + 1].measured_ms - itd[i].measured_ms) * f; };
  const DIST = 4.6, SPEED = 2.6, PERIOD = 1.15;
  const tMove0 = c.gap + 1.6, tMove1 = Math.min(c.front + 0.2, D - 0.6);

  return function renderAt(t) {
    // source angle: 90° (side) until after "the gap is", then glide to 0° (ahead) by "in front of you"
    const mv = K.prog(t, tMove0, tMove1 - tMove0, K.ease.inOut);
    const dg = 90 * (1 - mv), th = K.deg(dg);
    const S = K.az(th, DIST, 0);
    src.position.copy(S);
    const on = K.prog(t, c.right - 0.3, 0.6);
    src.scale.setScalar(Math.max(0.001, on));
    // ear distances: near ear direct; far ear wraps around the head (Woodworth: + a(θ + sinθ), a = 1)
    const dR = S.distanceTo(head.earR.position) - 0.1;
    const dL = dR + (th + Math.sin(th));
    let hitR = 0, hitL = 0;
    const nE = Math.floor((t - c.right) / PERIOD);
    for (let i = 0; i < N; i++) {
      const k = nE - i, live = t > c.right && k >= 0;
      const age = live ? t - (c.right + k * PERIOD) : 0;
      const R = age * SPEED;
      const o = live ? Math.max(0, 1 - R / 8.5) : 0;
      rings[i].position.set(S.x, 0, S.z); rings[i].scale.setScalar(Math.max(0.01, R));
      rings[i].material.opacity = 0.75 * o * on;
      shells[i].position.copy(S); shells[i].scale.setScalar(Math.max(0.01, R)); shells[i].material.opacity = 0.03 * o * on;
      if (live) { hitR += Math.exp(-Math.pow((R - dR) / 0.22, 2)); hitL += Math.exp(-Math.pow((R - dL) / 0.22, 2)); }
    }
    head.glowR.material.opacity = Math.min(1, hitR * 1.2); head.glowL.material.opacity = Math.min(1, hitL * 1.2);
    head.glowR.scale.setScalar(0.7 + hitR * 0.9); head.glowL.scale.setScalar(0.7 + hitL * 0.9);
    head.earR.material.emissiveIntensity = 0.5 + hitR * 2.5; head.earL.material.emissiveIntensity = 0.5 + hitL * 2.5;
    // paths (draw on at "right ear first")
    const pv = K.prog(t, c.first - 0.1, 0.9);
    const ptsR = [], ptsL = [];
    const ER = head.earR.position.clone();
    for (let i = 0; i <= 40; i++) ptsR.push(S.clone().lerp(ER, (i / 40) * pv));
    // tangent from S to the unit circle, then the arc to the left ear
    const d = Math.hypot(S.x, S.z), phiS = Math.atan2(S.z, S.x), off = Math.acos(1 / d);
    const tang = [phiS - off, phiS + off];
    // pick the tangent point on the side nearer the left ear (-x): go around the front or back, whichever is shorter
    const angL = Math.PI;
    const arcLen = (a) => { let x = Math.abs(((angL - a) + Math.PI * 3) % (Math.PI * 2) - Math.PI); return x; };
    const a0 = arcLen(tang[0]) < arcLen(tang[1]) ? tang[0] : tang[1];
    const T = new THREE.Vector3(Math.cos(a0) * 1.02, 0, Math.sin(a0) * 1.02);
    const full = [];
    for (let i = 0; i <= 30; i++) full.push(S.clone().lerp(T, i / 30));
    let delta = ((angL - a0) + Math.PI * 3) % (Math.PI * 2) - Math.PI;
    for (let i = 1; i <= 50; i++) { const a = a0 + (delta * i) / 50; full.push(new THREE.Vector3(Math.cos(a) * 1.04, 0, Math.sin(a) * 1.04)); }
    const nL = Math.max(1, Math.round(full.length * pv));
    for (let i = 0; i < nL; i++) ptsL.push(full[i]);
    pathR.userData.set(ptsR); pathL.userData.set(ptsL);
    pathR.material.opacity = pathL.material.opacity = 0.9 * pv * (1 - 0.6 * mv);
    // HUD readouts
    K.setText("itd-n", itdAt(dg).toFixed(2));
    K.setText("itd-a", dg < 0.5 ? "SOUND STRAIGHT AHEAD" : `SOUND AT ${Math.round(dg)}° RIGHT`);
    const gapFrac = itdAt(dg) / 0.661;
    const lane = document.getElementById("pulse-l");
    if (lane) lane.style.transform = `translateX(${(gapFrac * 0.6 * (lane.parentElement.clientWidth - lane.offsetLeft * 1.15)).toFixed(1)}px)`;
    const now = document.getElementById("itd-now");
    if (now) { const svg = now.ownerSVGElement, pw = svg.width.baseVal.value, ph = svg.height.baseVal.value;
      now.setAttribute("cx", (dg / 90 * pw).toFixed(1)); now.setAttribute("cy", (ph - itdAt(dg) / 0.7 * ph).toFixed(1)); }
    // camera: behind and above the listener, a slow drift
    const ca = K.deg(-14 + 10 * (t / D)), cr = (env.portrait ? 8.6 : 9.2) - 0.8 * (t / D);
    cam.position.set(1.6 + Math.sin(ca) * cr, (env.portrait ? 5.6 : 5.0) - 0.6 * (t / D), Math.cos(ca) * cr);
    cam.lookAt(1.7, -0.3, -0.7);
    dust(t);
    r.render(scene, cam);
  };
}
