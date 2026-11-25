//! lookalike_check.rs — ask Gavia's Vegnet about native plants that look like its invasives.
//!
//! A companion to Gavia's `examples/evaluate.rs`, built inside a clone of
//! github.com/nikhil-kunapareddy/gavia at tag v0.5.0: copy it to
//! `desktop/src-tauri/examples/` and run
//!
//! ```sh
//! cargo run --release --example lookalike_check -- \
//!     <lookalikes dir from lookalike_fetch.py> [--split <vegnet val.txt>]
//! ```
//!
//! Same `Detector`, same veg_v1 model, the app's own defaults (threshold 0.25,
//! no tiling) — exactly what Check an image does with Vegnet chosen. For each
//! photo it prints every box; then, per group, how many photos got at least
//! one box and which species the boxes were called. `--split` adds Vegnet's
//! own validation photos (all invasive) as the comparison row.

use std::collections::BTreeMap;
use std::path::{Path, PathBuf};

use gavia_lib::detection::preprocess::TileSettings;
use gavia_lib::detection::{DetectOptions, Detector};

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();
    let dir = PathBuf::from(&args[0]);
    let split = args.iter().position(|a| a == "--split").map(|i| PathBuf::from(&args[i + 1]));
    let model = Path::new(env!("CARGO_MANIFEST_DIR")).join("resources/models/veg_v1.onnx");
    let detector = Detector::load(&model, Some(4), TileSettings::default()).expect("veg_v1 loads");
    let options = DetectOptions::default();

    // (group, mimics, path)
    let mut photos: Vec<(String, String, PathBuf)> = Vec::new();
    let manifest: serde_json::Value =
        serde_json::from_str(&std::fs::read_to_string(dir.join("manifest.json")).unwrap()).unwrap();
    for e in manifest.as_array().unwrap() {
        photos.push((
            e["species"].as_str().unwrap().to_string(),
            e["mimics"].as_str().unwrap().to_string(),
            dir.join(e["file"].as_str().unwrap()),
        ));
    }
    if let Some(split) = &split {
        for line in std::fs::read_to_string(split).unwrap().split_whitespace() {
            photos.push(("vegnet val (invasive)".into(), "-".into(), PathBuf::from(line)));
        }
    }

    println!("Gavia Detector, model {} ({}), app defaults: threshold 0.25, no tiling\n",
             detector.info().name, model.file_name().unwrap().to_string_lossy());
    // group -> (mimics, photos, photos with a box, class -> boxes, best confidence)
    let mut groups: Vec<(String, String, usize, usize, BTreeMap<String, usize>, f64)> = Vec::new();
    for (group, mimics, path) in &photos {
        let outcome = detector.detect(&std::fs::read(path).unwrap(), options).unwrap();
        let boxes: Vec<String> = outcome
            .predictions
            .iter()
            .map(|p| format!("{} {:.2}", p.label, p.confidence))
            .collect();
        println!("{:60} {}", path.file_name().unwrap().to_string_lossy(),
                 if boxes.is_empty() { "-".to_string() } else { boxes.join("; ") });
        if groups.last().map(|g| &g.0 != group).unwrap_or(true) {
            groups.push((group.clone(), mimics.clone(), 0, 0, BTreeMap::new(), 0.0));
        }
        let g = groups.last_mut().unwrap();
        g.2 += 1;
        g.3 += usize::from(!outcome.predictions.is_empty());
        for p in &outcome.predictions {
            *g.4.entry(p.label.clone()).or_default() += 1;
            g.5 = g.5.max(p.confidence);
        }
    }

    println!("\n{:34} {:20} {:>6} {:>9}  boxes called", "group", "looks like", "photos", "boxed");
    for (group, mimics, n, boxed, classes, best) in &groups {
        let called: Vec<String> = classes.iter().map(|(c, k)| format!("{c} {k}")).collect();
        println!("{group:34} {mimics:20} {n:6} {boxed:9}  {}{}", called.join(", "),
                 if *boxed > 0 { format!(" (max {best:.2})") } else { String::new() });
    }
    let natives: Vec<_> = groups.iter().filter(|g| g.1 != "-").collect();
    let (n, boxed): (usize, usize) = natives.iter().fold((0, 0), |a, g| (a.0 + g.2, a.1 + g.3));
    println!("\nall native look-alikes: {boxed} of {n} photos got at least one invasive-plant box");
}
