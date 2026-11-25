//! listen.rs — print every window Gavia's call detector scores in a recording.
//!
//! What "Check an audio" computes, without the window around it. Built inside a
//! clone of github.com/nikhil-kunapareddy/gavia at tag v0.5.0: copy to
//! `desktop/src-tauri/examples/` and run
//!
//! ```sh
//! cargo run --release --example listen -- <recording> [<recording> ...]
//! ```

use std::path::PathBuf;

use gavia_lib::calls::CallDetector;

fn main() {
    let model = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("resources/calls/looncall_v1.onnx");
    let detector = CallDetector::load(&model, None).expect("call model loads");
    let threshold = detector.info().threshold;
    for file in std::env::args().skip(1) {
        let heard = detector
            .listen(&std::fs::read(&file).unwrap(), 4.0 * 3600.0)
            .unwrap_or_else(|e| panic!("{file}: {e}"));
        let calls = heard.windows.iter().filter(|w| w.probability >= threshold).count();
        println!(
            "{} · {:.1} s, {} Hz, {} ch · {} windows, {calls} at or above {threshold}",
            PathBuf::from(&file).file_name().unwrap().to_string_lossy(),
            heard.duration_seconds, heard.sample_rate, heard.channels, heard.windows.len()
        );
        for w in &heard.windows {
            println!(
                "  {:5.1}-{:5.1} s  P {:.3}{}",
                w.start, w.end, w.probability,
                if w.probability >= threshold { "  <- call" } else { "" }
            );
        }
    }
}
