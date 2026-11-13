// B05 · head tracking: a voice straight ahead; you turn your head 40° right (spatial.py's case).
// Tracking off: the sound is rendered at 0° from your nose, so it turns with you. Tracking on: the motion sensors
// render it at -40° from your nose, so it stays where it was in the room.
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 34, exposure: 1.2 });
  K.lights(scene, 0xffffff, 0x404a99);
  const c = env.cue, D = env.D, TURN = K.deg(env.data.turn);
  const head = K.headModel(); scene.add(head.g);
  // the room: a square floor grid and four corner posts, so "stays put" has something to stay put against
  const grid = new THREE.GridHelper(14, 14, 0x6f7be6, 0x2b3380); grid.position.y = -1.25;
  grid.material.transparent = true; grid.material.opacity = 0.35; grid.material.depthWrite = false; scene.add(grid);
  for (const [x, z] of [[-6, -6], [6, -6], [-6, 6], [6, 6]]) {
    const p = new THREE.Mesh(new THREE.BoxGeometry(0.12, 3.2, 0.12), new THREE.MeshStandardMaterial({ color: 0x3b44a8, emissive: 0x1a2070, roughness: 0.6 }));
    p.position.set(x, 0.35, z); scene.add(p);
  }
  const dust = K.dust(scene, 260, 14, 0x8a9bff, 0.05, 51);
  const DIST = 4.2;
  const voice = K.source(0xffb454, 0.22); scene.add(voice);
  const ghost = K.glow(0xffb454, 1.6, 0); ghost.position.copy(K.az(0, DIST)); scene.add(ghost);   // where it was
  const beam = K.trail(30, 0xffb454, 1); scene.add(beam);
  const arc = K.trail(60, 0xff8a7a, 1); scene.add(arc);
  // motion sensors: three gyro rings round the head
  const gyro = new THREE.Group();
  for (const [rx, ry] of [[Math.PI / 2, 0], [0, 0], [0, Math.PI / 2]]) {
    const g = K.ring(1.32, 0x7cf0b4, 0, 0.012); g.rotation.set(rx, ry, 0); gyro.add(g);
  }
  scene.add(gyro);
  const tA0 = env.data.a0, tA1 = env.data.a1, tB0 = env.data.b0;
  const turnUp = (t, t0) => K.prog(t, t0, 1.5, K.ease.inOut);

  return function renderAt(t) {
    // phase A: turn (tracking off) then back; phase B: turn again (tracking on)
    const aTurn = turnUp(t, tA0) * (1 - K.prog(t, tA1 + 0.6, 1.2, K.ease.inOut));
    const bTurn = turnUp(t, tB0);
    const phaseB = t >= tB0 - 0.8;
    const yaw = phaseB ? bTurn * TURN : aTurn * TURN;        // + = right
    head.g.rotation.y = -yaw;
    const soundRoom = phaseB ? 0 : yaw;                       // off: follows the nose; on: stays at 0°
    const S = K.az(soundRoom, DIST);
    voice.position.copy(S);
    voice.scale.setScalar(Math.max(0.001, K.prog(t, 0.2, 0.8)));
    ghost.material.opacity = phaseB ? 0 : 0.35 * Math.min(1, yaw / TURN);
    // beam from the nose to the sound
    const nose = K.az(yaw, 1.15);
    const pts = []; for (let i = 0; i <= 20; i++) pts.push(nose.clone().lerp(S, i / 20));
    beam.userData.set(pts); beam.material.opacity = 0.5;
    // the swept arc (tracking off): how far the sound moved in the room
    const ap = []; const n = Math.max(2, Math.round(60 * Math.min(1, soundRoom / TURN)));
    for (let i = 0; i < n; i++) ap.push(K.az((soundRoom * i) / (n - 1), DIST, -1.2));
    arc.userData.set(ap); arc.material.opacity = phaseB ? 0 : 0.9 * Math.min(1, soundRoom / TURN * 3);
    const gv = K.prog(t, c.sensors - 0.2, 0.8);
    gyro.children.forEach((g, i) => { g.material.opacity = 0.8 * gv; g.rotation.z = t * (0.6 + i * 0.25); });
    gyro.rotation.y = -yaw;
    // HUD readouts (rounded degrees)
    const hd = Math.round((yaw * 180) / Math.PI);
    if (!phaseB) { K.setText("off-h", hd + "°"); K.setText("off-s", Math.round((soundRoom * 180) / Math.PI) + "°"); }
    else { K.setText("off-h", "40°"); K.setText("off-s", "40°"); K.setText("on-h", hd + "°"); K.setText("on-s", "0°"); }
    // camera: above and behind, so left/right and the room both read
    const u = t / D;
    const ca = K.deg(-14 + 18 * u), cr = env.portrait ? 7.6 : 8.0;
    cam.position.set(0.8 + Math.sin(ca) * cr, 6.4 - 0.5 * u, Math.cos(ca) * cr);
    cam.lookAt(0.8, -0.5, -1.6);
    dust(t);
    r.render(scene, cam);
  };
}
