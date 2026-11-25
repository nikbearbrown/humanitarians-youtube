// B03 · front or back: a sound at 30° in front and its mirror at 150° behind sit on the same "cone of confusion"
// around the ear axis: same path lengths to both ears, so the same timing and loudness. Outer-ear folds break the tie.
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 42, exposure: 1.2 });
  K.lights(scene, 0xffffff, 0x404a99);
  const c = env.cue, D = env.D;
  const head = K.headModel(); scene.add(head.g);
  scene.add(K.polarFloor(6.5, 0x5f6bd6, -1.25, 0.16));
  const dust = K.dust(scene, 300, 14, 0x8a9bff, 0.06, 31);
  const R = 3.6;
  const A = K.az(K.deg(30), R), B = K.az(K.deg(150), R);
  const sA = K.source(0xffb454, 0.2), sB = K.source(0xff7ab6, 0.2);
  sA.position.copy(A); sB.position.copy(B); scene.add(sA, sB);
  // cone of confusion: apex at the head, axis = the ear axis (+x), half-angle 60°
  const L = R * Math.cos(K.deg(60)), rad = R * Math.sin(K.deg(60));
  const cone = new THREE.Mesh(new THREE.ConeGeometry(rad, L, 96, 1, true), new THREE.MeshBasicMaterial({ color: 0x8a9bff,
    transparent: true, opacity: 0.06, side: THREE.DoubleSide, depthWrite: false, blending: THREE.AdditiveBlending }));
  cone.rotation.z = Math.PI / 2; cone.position.x = L / 2;     // ConeGeometry's apex is +y: rotate it to -x, so the apex sits at the head
  const coneW = new THREE.Mesh(new THREE.ConeGeometry(rad, L, 24, 4, true), new THREE.MeshBasicMaterial({ color: 0x8a9bff,
    wireframe: true, transparent: true, opacity: 0.12, depthWrite: false, blending: THREE.AdditiveBlending }));
  coneW.rotation.z = Math.PI / 2; coneW.position.x = L / 2;
  scene.add(cone, coneW);
  const circ = K.ring(rad, 0xdfe3ff, 0.55, 0.02); circ.rotation.y = Math.PI / 2; circ.position.x = L; scene.add(circ);
  // the four paths (to each ear), equal in pairs
  const ER = head.earR.position, EL = head.earL.position;
  const mk = (col) => { const l = K.trail(60, col, 1); scene.add(l); return l; };
  const pAR = mk(0x5ce1ff), pAL = mk(0xc39bff), pBR = mk(0x5ce1ff), pBL = mk(0xc39bff);
  const seg = (P, Q, f) => { const pts = []; for (let i = 0; i <= 30; i++) pts.push(P.clone().lerp(Q, (i / 30) * f)); return pts; };
  // outer ears: a forward-facing shell behind each ear
  const pinnaMat = new THREE.MeshStandardMaterial({ color: 0x9aa8ff, emissive: 0x5a64d8, emissiveIntensity: 0.5, roughness: 0.4,
    side: THREE.DoubleSide, transparent: true, opacity: 0 });
  const pinGeo = new THREE.SphereGeometry(0.34, 32, 16, 0, Math.PI, 0, Math.PI * 0.5);
  const pR = new THREE.Mesh(pinGeo, pinnaMat), pL = new THREE.Mesh(pinGeo, pinnaMat);
  pR.position.set(1.06, 0.02, 0.12); pR.rotation.set(0, Math.PI / 2 + 0.25, Math.PI / 2);
  pL.position.set(-1.06, 0.02, 0.12); pL.rotation.set(0, -Math.PI / 2 - 0.25, Math.PI / 2);
  scene.add(pR, pL);
  const rings = [];
  for (let i = 0; i < 5; i++) { const m = K.ripple(0xff7ab6, 0.5); scene.add(m); rings.push(m); }

  return function renderAt(t) {
    const onA = K.prog(t, c.mirror - 0.4, 0.7), onB = K.prog(t, c.mirror + 0.3, 0.7);
    sA.scale.setScalar(Math.max(0.001, onA)); sB.scale.setScalar(Math.max(0.001, onB));
    const cv = K.prog(t, c.same - 0.2, 1.2);
    cone.material.opacity = 0.06 * cv; coneW.material.opacity = 0.12 * cv; circ.material.opacity = 0.55 * cv;
    const pv = K.prog(t, c.same, 1.0);
    pAR.userData.set(seg(A, ER, pv)); pAL.userData.set(seg(A, EL, pv)); pBR.userData.set(seg(B, ER, pv)); pBL.userData.set(seg(B, EL, pv));
    const fold = K.prog(t, c.folds, 1.0);
    for (const p of [pAR, pAL]) p.material.opacity = 0.85 * pv;
    for (const p of [pBR, pBL]) p.material.opacity = 0.85 * pv * (1 - 0.65 * fold);
    pinnaMat.opacity = 0.6 * K.prog(t, c.outer - 0.1, 0.8);
    // the behind source's waves get scattered by the folds: its ripples break up
    for (let i = 0; i < rings.length; i++) {
      const age = ((t - c.folds) + i * 0.6) % 3.0;
      const R2 = 0.2 + age * 1.5;
      rings[i].position.set(B.x, 0, B.z); rings[i].scale.setScalar(R2);
      rings[i].material.opacity = t > c.folds ? 0.5 * (1 - age / 3) * fold : 0;
    }
    head.glowR.material.opacity = 0.55 * pv; head.glowL.material.opacity = 0.4 * pv;
    // camera: from above and behind-right, a slow orbit that shows the cone
    const u = t / D;
    const ca = K.deg(-12 + 16 * u), cr = 4.2;
    cam.position.set(1.5 + Math.sin(ca) * cr, (env.portrait ? 10.6 : 11.2) - 0.5 * u, 0.3 + Math.cos(ca) * cr);
    cam.lookAt(1.5, 0, 0.3);
    dust(t);
    r.render(scene, cam);
  };
}
