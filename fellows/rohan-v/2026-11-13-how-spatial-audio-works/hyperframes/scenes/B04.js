// B04 · the filters: a dummy head with microphones in its ears is measured from 710 directions (KEMAR's count),
// elevations -40° to 90°. One direction's pair of filters places a sound there. Then the run's own clip: the melody
// circling the head once in 8 s (evidence/circle.wav: azimuth = 360° x time / 8 s, starting straight ahead, turning right).
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 34, exposure: 1.2 });
  K.lights(scene, 0xffffff, 0x404a99);
  const c = env.cue, D = env.D, clip0 = env.data.clip0, clipD = env.data.clipdur;
  const head = K.headModel({ color: 0x343a7a, rim: 0xb8c0ff }); scene.add(head.g);
  scene.add(K.polarFloor(6.0, 0x5f6bd6, -1.25, 0.12));
  const dust = K.dust(scene, 260, 14, 0x8a9bff, 0.05, 41);
  // 710 directions on a sphere of radius 3.2, elevation >= -40°, in measuring order (by elevation ring, then azimuth)
  const RS = 3.2, dirs = [];
  const N0 = 900;
  for (let i = 0; i < N0 && dirs.length < 710; i++) {
    const y = 1 - (i + 0.5) / N0 * 2, rr = Math.sqrt(1 - y * y), ph = i * Math.PI * (3 - Math.sqrt(5));
    const el = Math.asin(y);
    if (el < K.deg(-40)) continue;
    dirs.push({ v: new THREE.Vector3(Math.cos(ph) * rr * RS, y * RS, Math.sin(ph) * rr * RS), el, az: Math.atan2(Math.cos(ph), -Math.sin(ph)) });
  }
  dirs.sort((a, b) => (b.el - a.el) || (a.az - b.az));
  const M = dirs.length;
  const pos = new Float32Array(M * 3), col = new Float32Array(M * 3);
  dirs.forEach((d, i) => { pos[i * 3] = d.v.x; pos[i * 3 + 1] = d.v.y; pos[i * 3 + 2] = d.v.z; });
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos, 3)); geo.setAttribute("color", new THREE.BufferAttribute(col, 3));
  const pts = new THREE.Points(geo, new THREE.PointsMaterial({ map: K.glowTex(), size: 0.2, vertexColors: true, transparent: true,
    depthWrite: false, blending: THREE.AdditiveBlending }));
  scene.add(pts);
  const base = new THREE.Color(0x8a9bff), hot = new THREE.Color(0xffffff), amber = new THREE.Color(0xffb454);
  // the chosen direction: 60° right, on the ear plane
  const pick = K.az(K.deg(60), RS, 0);
  const pickG = K.glow(0x5ce1ff, 0.9, 0); pickG.position.copy(pick); scene.add(pickG);
  const beamR = K.trail(40, 0x5ce1ff, 1), beamL = K.trail(40, 0xc39bff, 1); scene.add(beamR, beamL);
  const snd = K.source(0xffb454, 0.18); scene.add(snd);
  const ring = K.ring(RS, 0xffb454, 0, 0.012); ring.rotation.x = -Math.PI / 2; scene.add(ring);
  const tr = K.trail(90, 0xffb454, 1); scene.add(tr);
  const mics = [head.earL, head.earR];
  const NAMES = ["AHEAD", "AHEAD-RIGHT", "RIGHT", "BEHIND-RIGHT", "BEHIND", "BEHIND-LEFT", "LEFT", "AHEAD-LEFT"];

  return function renderAt(t) {
    // measuring sweep: the dots arrive in order from "seven hundred" over 3 s
    const sweep = K.clamp((t - c.seven) / 3.0) * M;
    const listenDim = 1 - 0.55 * K.prog(t, c.listen - 0.5, 1.2);
    const tc = (t - clip0) / clipD;            // 0..1 during the circling clip
    const sp = K.az(2 * Math.PI * K.clamp(tc), RS, 0);
    for (let i = 0; i < M; i++) {
      const a = K.clamp(sweep - i);           // 0..1: has this direction been measured yet
      const flash = Math.exp(-Math.pow((sweep - i) / 18, 2)) * (sweep < M ? 1 : 0);
      let cc = base.clone().multiplyScalar(0.18 + 0.82 * a).lerp(hot, flash);
      cc.multiplyScalar(a > 0 ? listenDim : 0.06);
      if (tc > 0 && tc < 1) { const dd = dirs[i].v.distanceTo(sp); if (dd < 0.9) cc.lerp(amber, (1 - dd / 0.9) * 0.9); }
      col[i * 3] = cc.r; col[i * 3 + 1] = cc.g; col[i * 3 + 2] = cc.b;
    }
    geo.attributes.color.needsUpdate = true;
    // mics flash while measuring
    const meas = t > c.seven && sweep < M ? 0.6 + 0.4 * Math.sin(t * 20) : 0;
    head.glowL.material.opacity = head.glowR.material.opacity = 0.2 + 0.6 * meas;
    // one direction's filter pair
    const pk = K.prog(t, c.hrtf - 0.2, 0.8) * (1 - K.prog(t, c.listen, 0.8));
    pickG.material.opacity = pk; pickG.scale.setScalar(0.9 + 0.2 * Math.sin(t * 5));
    const bv = K.prog(t, c.hrtf, 0.9);
    const seg = (P, Q, f) => { const a = []; for (let i = 0; i <= 20; i++) a.push(P.clone().lerp(Q, (i / 20) * f)); return a; };
    beamR.userData.set(seg(pick, head.earR.position, bv)); beamL.userData.set(seg(pick, head.earL.position, bv));
    beamR.material.opacity = beamL.material.opacity = 0.9 * pk;
    // the sound: born at the head on "the pair", flies out to that direction on "play it from there"
    const born = K.prog(t, c.pair, 0.6), fly = K.prog(t, c.there - 0.4, 1.0, K.ease.inOut);
    let P = new THREE.Vector3(0, 0, 0).lerp(pick, fly);
    let sz = born * (1 - K.prog(t, c.listen - 0.3, 0.5));
    if (tc > -0.08) { P = sp; sz = K.prog(t, clip0 - 0.6, 0.6) * (1 - K.prog(t, clip0 + clipD, 0.4)); }
    snd.position.copy(P); snd.scale.setScalar(Math.max(0.001, sz));
    ring.material.opacity = 0.35 * K.prog(t, clip0 - 0.8, 0.8) * (1 - K.prog(t, clip0 + clipD, 0.6));
    const tp = [];
    if (tc > 0) { for (let i = 0; i < 90; i++) { const tt = K.clamp(tc - (89 - i) * 0.0035); tp.push(K.az(2 * Math.PI * tt, RS, 0)); } }
    tr.userData.set(tp); tr.material.opacity = tc > 0 && tc < 1.05 ? 0.95 : 0;
    // HUD: where the sound is now, and the dial
    if (tc >= 0 && tc <= 1) {
      const a = (tc * 360) % 360;
      K.setText("dir-now", NAMES[Math.round(a / 45) % 8]);
      K.setAttr("dial-dot", "cx", (40 * Math.sin(K.deg(a))).toFixed(2)); K.setAttr("dial-dot", "cy", (-40 * Math.cos(K.deg(a))).toFixed(2));
    }
    // camera: slow orbit above; settles behind the head for the listening turn
    const u = t / D;
    const ca = K.deg(-35 + 50 * K.ease.inOut(K.clamp(t / (clip0 - 1)))), cr = env.portrait ? 9.8 : 10.4;
    const el = 4.4 + 1.4 * K.prog(t, clip0 - 2, 2, K.ease.inOut);
    cam.position.set(Math.sin(ca) * cr, el, Math.cos(ca) * cr);
    cam.lookAt(0, -0.1, 0);
    dust(t);
    r.render(scene, cam);
  };
}
