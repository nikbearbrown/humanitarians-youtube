//! seal_check.rs — what Gavia 0.3.1's loon model shows on seal photos, at the
//! app's own threshold.
//!
//! A companion to Gavia's `examples/evaluate.rs` (same Detector, same loader,
//! same defaults). Copy into a checkout of github.com/nikhil-kunapareddy/gavia at
//! tag v0.3.1, as `desktop/src-tauri/examples/seal_check.rs`, then:
//!
//! ```sh
//! cargo run --release --example seal_check -- --split <split.txt>
//! ```
//!
//! For the whole-photo pass and the tiled pass it prints, at confidence 0.25 (the
//! threshold the app ships with): boxes drawn ("loons" a reviewer would see),
//! labelled seals in the split, seals overlapped by a box at IoU >= 0.5, and the
//! highest confidence of any box.

use std::path::PathBuf;

use gavia_lib::detection::detector::default_thread_count;
use gavia_lib::detection::preprocess::TileSettings;
use gavia_lib::detection::{DetectOptions, Detector};

type Box = [f64; 4];

fn iou(a: &Box, b: &Box) -> f64 {
    let iw = (a[2].min(b[2]) - a[0].max(b[0])).max(0.0);
    let ih = (a[3].min(b[3]) - a[1].max(b[1])).max(0.0);
    let inter = iw * ih;
    let area = |r: &Box| (r[2] - r[0]) * (r[3] - r[1]);
    inter / (area(a) + area(b) - inter)
}

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();
    let split = args
        .iter()
        .position(|a| a == "--split")
        .and_then(|i| args.get(i + 1))
        .expect("usage: seal_check --split <split.txt>");
    let model = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("resources/models/loon_v1.onnx");
    let images: Vec<PathBuf> = std::fs::read_to_string(split)
        .unwrap()
        .split_whitespace()
        .map(PathBuf::from)
        .collect();
    let detector = Detector::load(&model, Some(default_thread_count()), TileSettings::default())
        .unwrap_or_else(|e| panic!("{e}"));

    for tiled in [false, true] {
        let options = DetectOptions {
            confidence_threshold: Some(0.25),
            iou_threshold: Some(0.45),
            tiling: Some(tiled),
        };
        let (mut boxes, mut seals, mut hit, mut top) = (0usize, 0usize, 0usize, 0.0f64);
        for path in &images {
            let outcome = detector.detect(&std::fs::read(path).unwrap(), options).unwrap();
            let (w, h) = (f64::from(outcome.image_width), f64::from(outcome.image_height));
            let preds: Vec<Box> = outcome
                .predictions
                .iter()
                .map(|p| {
                    top = top.max(p.confidence);
                    [p.x / 100.0 * w, p.y / 100.0 * h, (p.x + p.width) / 100.0 * w,
                     (p.y + p.height) / 100.0 * h]
                })
                .collect();
            boxes += preds.len();
            let label = PathBuf::from(path.to_string_lossy().replace("/images/", "/labels/"))
                .with_extension("txt");
            for line in std::fs::read_to_string(label).unwrap().lines() {
                let v: Vec<f64> = line.split_whitespace().skip(1).map(|s| s.parse().unwrap()).collect();
                let t = [(v[0] - v[2] / 2.0) * w, (v[1] - v[3] / 2.0) * h,
                         (v[0] + v[2] / 2.0) * w, (v[1] + v[3] / 2.0) * h];
                seals += 1;
                if preds.iter().any(|p| iou(p, &t) >= 0.5) {
                    hit += 1;
                }
            }
        }
        println!(
            "{:6}  images {}  seals {}  boxes at 0.25 {}  seals boxed {}  top confidence {:.3}",
            if tiled { "tiled" } else { "whole" },
            images.len(), seals, boxes, hit, top
        );
    }
}
