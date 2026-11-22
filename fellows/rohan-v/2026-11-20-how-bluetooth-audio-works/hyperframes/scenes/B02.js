// B02 · the radio: Bluetooth's 79 channels as a row of light columns (2402-2480 MHz); Wi-Fi sits over channels 24-46
// (orange). A packet hops to a new channel every try; the tries are bluetooth.py's own (the first 160 of the listening
// window), shown in slow motion. Lost = red burst, through = green ring. From "Adaptive hopping" the Wi-Fi channels
// go dark and the hops (the adaptive-hopping run's own tries) avoid them.
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 34, exposure: 1.15 });
  K.lights(scene, 0xffffff, 0x224466);
  const c = env.cue, D = env.D, d = env.data;
  scene.add(K.grid(70, 70, 0x2a5a8a, 0.14, -0.01));
  const dust = K.dust(scene, 260, 18, 0x8ac8ff, 0.05, 4);
  const W0 = d.wifi[0], W1 = d.wifi[1], SP = 0.13;
  const X = (ch) => (ch - 39) * SP;
  const cols = [];
  for (let k = 0; k < 79; k++) {
    const inW = k >= W0 && k <= W1;
    const m = K.glowBox(SP * 0.55, 1, SP * 0.55, inW ? 0x6aa0d0 : 0x3da9ff, 0.5);
    m.position.set(X(k), 0.5, 0); m.scale.y = 0.6; scene.add(m); cols.push({ m, inW });
  }
  // Wi-Fi: a soft orange dome over its channels
  const dome = new THREE.Mesh(new THREE.SphereGeometry(1, 64, 32, 0, Math.PI * 2, 0, Math.PI / 2), new THREE.MeshBasicMaterial({ color: 0xff9f43,
    transparent: true, opacity: 0, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide }));
  dome.scale.set((W1 - W0 + 1) * SP / 2, 1.7, 1.1); dome.position.set((X(W0) + X(W1)) / 2, 0, 0); scene.add(dome);
  const domeG = K.glow(0xff9f43, 5, 0); domeG.position.set((X(W0) + X(W1)) / 2, 0.8, 0); scene.add(domeG);
  const pk = K.glowBox(0.3, 0.3, 0.3, 0xffffff, 2); scene.add(pk);
  const pkG = K.glow(0xffffff, 2.2, 0.9); scene.add(pkG);
  const burst = K.glow(0xff5c6c, 2.4, 0); scene.add(burst);
  const okR = K.ripple(0x5be49b, 0.8); scene.add(okR);
  const SLOW = 12;                                              // 1 s of the simulation = 12 s on screen
  const tOff = c.hops - 0.2, tOn = c.afh;
  const hopsAt = (list, t0, t) => {                             // the try under way at screen time t
    const st = (t - t0) / SLOW;
    let i = 0; while (i + 1 < list.length && list[i + 1][0] <= st) i++;
    const next = list[Math.min(i + 1, list.length - 1)];
    const f = list.length > 1 && next[0] > list[i][0] ? K.clamp((st - list[i][0]) / (next[0] - list[i][0])) : 0;
    return { cur: list[i], prev: list[Math.max(i - 1, 0)], f, st };
  };
  const GREEN = new THREE.Color(0x5be49b), REDc = new THREE.Color(0xff5c6c), WHITE = new THREE.Color(0xffffff);
  return function renderAt(t) {
    const show = K.prog(t, 0.1, 1.0);
    const afh = K.prog(t, tOn, 0.8);
    cols.forEach((o, k) => {
      const wave = 0.6 + 0.12 * Math.sin(t * 2 + k * 0.4);
      o.m.scale.y = wave * show; o.m.position.y = o.m.scale.y / 2;
      o.m.material.opacity = (o.inW ? 1 - 0.8 * afh : 1) * show;
      o.m.material.emissiveIntensity = o.inW ? 0.5 * (1 - 0.85 * afh) : 0.55;
    });
    const wOn = K.prog(t, c.wifi - 0.3, 0.6);
    const busy = 0.5 + 0.5 * Math.sin(t * 9.0) * Math.sin(t * 3.1);
    dome.material.opacity = wOn * (0.1 + 0.12 * busy) * (1 - 0.4 * afh); domeG.material.opacity = wOn * 0.35 * (1 - 0.4 * afh);
    // the packet: hops through the "without" run, then (from "Adaptive hopping") the "with" run
    const useOn = t >= tOn;
    const h = hopsAt(useOn ? d.hops_on : d.hops_off, useOn ? tOn : tOff, t);
    const live = t > tOff;
    const from = X(h.prev[1]), to = X(h.cur[1]), f = K.ease.out(K.clamp(h.f * 3));
    const x = K.lerp(from, to, f), y = 0.9 + Math.sin(Math.PI * f) * 1.1;
    pk.position.set(x, y, 0); pkG.position.copy(pk.position);
    const lost = h.cur[2] === 1 && f > 0.95;
    pk.material.color.copy(lost ? REDc : (f > 0.95 ? GREEN : WHITE)); pk.material.emissive.copy(pk.material.color);
    pkG.material.color.copy(pk.material.color);
    pk.visible = pkG.visible = live; pkG.material.opacity = live ? 0.9 : 0;
    const land = K.clamp((h.f * 3 - 1) / 2);
    burst.position.set(to, 0.9, 0); burst.material.opacity = live && h.cur[2] === 1 ? (1 - land) * 0.95 : 0; burst.scale.setScalar(1.2 + 2.0 * land);
    okR.position.set(to, 0.02, 0); okR.scale.setScalar(0.05 + 0.6 * land); okR.material.opacity = live && h.cur[2] === 0 ? 0.8 * (1 - land) : 0;
    K.pin("pl-wifi", new THREE.Vector3((X(W0) + X(W1)) / 2, 2.15, 0), cam, env, 0.95 * wOn);
    K.pin("pl-lo", new THREE.Vector3(X(4), -0.7, 0.4), cam, env, 0.85 * show);
    K.pin("pl-hi", new THREE.Vector3(X(74), -0.7, 0.4), cam, env, 0.85 * show);
    const p = K.prog(t, 0, D, K.ease.inOut);
    const ca = K.deg(-20 + 26 * p), cr = env.portrait ? 12.8 : 10.6;
    cam.position.set(Math.sin(ca) * cr, 3.6 - 0.8 * p, Math.cos(ca) * cr);
    cam.lookAt(0, 0.6, 0);
    dust(t);
    r.render(scene, cam);
  };
}
