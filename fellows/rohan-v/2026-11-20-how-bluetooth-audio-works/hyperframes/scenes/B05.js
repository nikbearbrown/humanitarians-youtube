// B05 · lip sync: two lanes running toward you, PICTURE (violet) and SOUND (blue). Each event (a drum hit on screen)
// has a flash on the picture lane and a pulse on the sound lane. The sound pulses arrive late (Bluetooth's delay);
// from "holds the picture" the picture lane is held back by the same amount and the pairs line up. For "A game" the
// picture can't wait: a gold button-press marker stays put while its sound lags. Illustration: the delay is drawn at
// 250 ms, inside the 170-370 ms the two published tests measured.
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 34, exposure: 1.15 });
  K.lights(scene, 0xffffff, 0x224466);
  const c = env.cue, D = env.D;
  scene.add(K.grid(70, 70, 0x2a5a8a, 0.14, -1.6));
  const dust = K.dust(scene, 240, 18, 0x8ac8ff, 0.05, 7);
  const SPD = 3.0, LAG = 0.25 * SPD * 4;           // 250 ms, drawn 4x longer than life so you can see it
  const laneY = [0.9, -0.5];
  const lanes = laneY.map((y, i) => { const m = K.slab(14, 0.05, i ? 0x3da9ff : 0xb48cff, 0.5); m.position.set(0, y, 0); scene.add(m); return m; });
  const now = K.slab(0.06, 2.6, 0xffffff, 0.5); now.position.set(2.5, 0.2, 0); scene.add(now);
  const EV = 9, pic = [], snd = [];
  for (let i = 0; i < EV; i++) {
    const a = K.glowBox(0.5, 0.5, 0.06, 0xb48cff, 1.2); scene.add(a); pic.push(a);
    const b = K.glowBox(0.18, 0.5, 0.18, 0x3da9ff, 1.2); scene.add(b); snd.push(b);
  }
  const press = K.glowBox(0.44, 0.44, 0.44, 0xffd166, 1.4); scene.add(press);
  const lagBar = K.slab(1, 0.08, 0xffd166, 0); scene.add(lagBar);
  return function renderAt(t) {
    const on = K.prog(t, 0.1, 0.8);
    const hold = K.prog(t, c.holds - 0.1, 1.1, K.ease.inOut) * (1 - K.prog(t, c.game - 0.3, 0.6));
    const game = K.prog(t, c.game - 0.3, 0.6);
    let lagX = 0;
    for (let i = 0; i < EV; i++) {
      const x = 2.5 - (((i * 1.6 - t * SPD * 0.5) % 14.4) + 14.4) % 14.4 + 7.2;
      pic[i].position.set(x - LAG * hold, laneY[0], 0);
      snd[i].position.set(x - LAG, laneY[1], 0);
      const vis = on * (1 - game * 0.75);
      pic[i].material.opacity = vis; snd[i].material.opacity = vis;
      const hitP = Math.max(0, 1 - Math.abs(pic[i].position.x - 2.5) / 0.3), hitS = Math.max(0, 1 - Math.abs(snd[i].position.x - 2.5) / 0.3);
      pic[i].material.emissiveIntensity = 1 + 3 * hitP; snd[i].material.emissiveIntensity = 1 + 3 * hitS;
      if (i === 0) lagX = x;
    }
    // the game: a button press now, its sound late
    const gx = 2.5 - ((t * SPD * 0.5) % 4.8) + 1.4;
    press.position.set(gx, laneY[0], 0); press.material.opacity = game;
    lagBar.position.set(2.5 - LAG / 2, 0.2, 0.05); lagBar.scale.x = LAG;
    lagBar.material.opacity = 0.8 * K.prog(t, c.behind, 0.5) * (1 - hold * 0.9);
    K.pin("pl-vid", new THREE.Vector3(-5.6, laneY[0] + 0.55, 0), cam, env, 0.9 * on);
    K.pin("pl-snd", new THREE.Vector3(-5.6, laneY[1] - 0.55, 0), cam, env, 0.9 * on);
    K.pin("pl-lag", new THREE.Vector3(2.5 - LAG / 2, env.portrait ? 1.75 : 0.55, 0.05), cam, env, 0.95 * K.prog(t, c.behind, 0.5) * (1 - hold));
    const p = K.prog(t, 0, D, K.ease.inOut);
    const ca = K.deg(-28 + 18 * p), cr = env.portrait ? 12.5 : 10.8;
    cam.position.set(0.8 + Math.sin(ca) * cr, 2.6, Math.cos(ca) * cr);
    cam.lookAt(0.6, 0.1, 0);
    dust(t);
    r.render(scene, cam);
  };
}
