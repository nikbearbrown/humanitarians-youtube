//! noise_check.rs — loonet's drone-noise test, scored by Gavia's own call detector.
//!
//! A companion to Gavia's `tests/call_parity.rs`, built inside a clone of
//! github.com/nikhil-kunapareddy/gavia at tag v0.5.0 (the call code is
//! unchanged since v0.4.0): copy it to `desktop/src-tauri/examples/` and run
//!
//! ```sh
//! cargo run --release --example noise_check -- <clips dir from drone_mix.py>
//! ```
//!
//! Every clip is one 3 s, 48 kHz WAV, so `CallDetector::listen` returns one
//! window per clip; its probability is compared with the threshold the app
//! ships (looncall_v1.json, 0.5) and with the Python score drone_mix.py wrote.

use std::collections::BTreeMap;
use std::path::PathBuf;

use gavia_lib::calls::CallDetector;

fn main() {
    let dir = PathBuf::from(std::env::args().nth(1).expect("usage: noise_check <clips dir>"));
    let model = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("resources/calls/looncall_v1.onnx");
    let detector = CallDetector::load(&model, None).expect("call model loads");
    let threshold = detector.info().threshold;

    let python: BTreeMap<String, f64> = std::fs::read_to_string(dir.join("python_scores.csv"))
        .map(|t| {
            t.lines()
                .skip(1)
                .map(|l| {
                    let f: Vec<&str> = l.split(',').collect();
                    (f[0].to_string(), f[3].parse().unwrap())
                })
                .collect()
        })
        .unwrap_or_default();

    let manifest = std::fs::read_to_string(dir.join("manifest.csv")).expect("manifest.csv");
    // snr -> (loon windows, caught, other windows, false alarms)
    let mut table: Vec<(String, [usize; 4])> = Vec::new();
    let (mut worst, mut flipped, mut n) = (0.0f64, 0usize, 0usize);
    for line in manifest.lines().skip(1) {
        let f: Vec<&str> = line.split(',').collect();
        let (wav, snr, label) = (f[0], f[1].to_string(), f[2] == "1");
        let heard = detector
            .listen(&std::fs::read(dir.join(wav)).unwrap(), 4.0 * 3600.0)
            .unwrap_or_else(|e| panic!("{wav}: {e}"));
        assert_eq!(heard.windows.len(), 1, "{wav}: one 3 s clip, one window");
        let p = heard.windows[0].probability;
        let yes = p >= threshold;
        if table.last().map(|(s, _)| s != &snr).unwrap_or(true) {
            table.push((snr.clone(), [0; 4]));
        }
        let row = &mut table.last_mut().unwrap().1;
        if label {
            row[0] += 1;
            row[1] += usize::from(yes);
        } else {
            row[2] += 1;
            row[3] += usize::from(yes);
        }
        if let Some(&q) = python.get(wav) {
            worst = worst.max((p - q).abs());
            flipped += usize::from(yes != (q >= threshold));
            n += 1;
        }
    }

    println!("Gavia CallDetector ({}), threshold {threshold}", detector.info().name);
    println!("{:>7} | loon recall    | false alarms", "SNR dB");
    for (snr, [loons, caught, others, alarms]) in &table {
        println!(
            "{snr:>7} | {caught:2}/{loons} = {:.2} | {alarms}/{others}",
            *caught as f64 / *loons as f64
        );
    }
    if n > 0 {
        println!("vs Python (BirdNET TFLite + weights.npz): {n} clips, worst |P difference| {worst:.6}, {flipped} on the other side of {threshold}");
    }
}
