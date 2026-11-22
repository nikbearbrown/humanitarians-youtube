// B02 · off key: the singer's pitch drawn through a 3D piano roll. Lit lanes are the notes of C major; the soft boxes
// are the notes the tune meant. The track is autotune.py's detected pitch (every 10 ms).
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 34, exposure: 1.15 });
  K.lights(scene, 0xffffff, 0x553366);
  const c = env.cue, D = env.D, roll = env.data.roll;
  scene.add(K.grid(60, 60, 0x6a4a7a, 0.14, -3.2));
  const dust = K.dust(scene, 340, 16, 0xd8a8ff, 0.06, 21);
  const R = K.pianoRoll(scene, roll, { xs: 2.9 });
  const tr = R.tube("detected", 0xff8a5b, 0.045);
  const trG = R.tube("detected", 0xff8a5b, 0.14); trG.material.opacity = 0.16;
  const head = K.glow(0xff8a5b, 1.2, 0); scene.add(head);
  // the semitone band between C4 and C#4 lights up on "A semitone"
  const band = K.slab((R.t1 - R.t0 + 0.4) * 2.9, R.Y(61) - R.Y(60), 0xffc857, 0);
  band.position.set(R.X((R.t0 + R.t1) / 2), (R.Y(60) + R.Y(61)) / 2, -0.04); scene.add(band);
  const names = { 60: "C4", 62: "D4", 64: "E4", 67: "G4", 69: "A4" };
  const tDraw0 = c.singer - 0.2, tDraw1 = Math.min(c.twenty + 0.6, D - 1.2);
  return function renderAt(t) {
    const rt = R.t0 + (R.t1 - R.t0) * K.prog(t, tDraw0, tDraw1 - tDraw0, (x) => x);
    R.drawTo("detected", rt);
    trG.geometry.setDrawRange(0, tr.geometry.drawRange.count); trG.visible = tr.visible;
    head.position.copy(R.at("detected", rt)); head.material.opacity = t > tDraw0 && t < tDraw1 + 0.4 ? 0.9 : 0;
    band.material.opacity = 0.22 * K.prog(t, c.semitone, 0.5) * (1 - K.prog(t, c.singer, 0.6));
    R.notes.forEach((n) => { n.box.material.opacity = 0.05 + 0.13 * K.prog(t, c.cmajor - 0.3 + (n.a - R.t0) * 0.3, 0.5); });
    for (const m in names) K.pin("pn" + m, new THREE.Vector3(R.X(R.t0 - 0.26), R.Y(+m), 0), cam, env, K.prog(t, 0.4, 0.8) * 0.9);
    // camera: from a low angle on the left, easing out to see the whole phrase
    const p = K.prog(t, 0, D, K.ease.inOut);
    const cx = K.lerp(-3.2, 0.6, p), cr = (env.portrait ? 12.5 : 11.2) + 1.5 * p;
    cam.position.set(cx + 3.0, 1.4 + 1.2 * p, cr);
    cam.lookAt(cx + 0.2, 0.1, 0);
    dust(t);
    r.render(scene, cam);
  };
}
