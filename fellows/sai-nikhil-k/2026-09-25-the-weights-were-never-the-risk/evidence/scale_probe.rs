//! Scratch probe for the 2026-09-25-the-weights-were-never-the-risk reel (not part of Gavia): what reduction
//! would jpeg-decoder's own `scale()` pick for a 640 target, against the
//! Pillow-compatible `draft_factor` Gavia ships?
use gavia_lib::detection::loader::draft_factor;
use std::io::Cursor;

fn main() {
    let split = std::env::args().nth(1).expect("val.txt");
    let text = std::fs::read_to_string(split).unwrap();
    let (mut n, mut differ) = (0, 0);
    for path in text.split_whitespace() {
        let bytes = std::fs::read(path).unwrap();
        let mut d = jpeg_decoder::Decoder::new(Cursor::new(&bytes));
        d.read_info().unwrap();
        let info = d.info().unwrap();
        let (w, h) = (u32::from(info.width), u32::from(info.height));
        let (sw, sh) = d.scale(640, 640).unwrap();
        let native = (w as f64 / f64::from(sw)).round() as u32;
        let ours = draft_factor(w, h, 640);
        n += 1;
        if native != ours {
            differ += 1;
        }
        let name = path.rsplit('/').next().unwrap();
        println!("{name:34} {w}x{h}  jpeg-decoder scale() -> {sw}x{sh} (f={native})  draft_factor f={ours}{}",
            if native != ours { "  DIFFER" } else { "" });
    }
    println!("\n{differ} of {n} photos: jpeg-decoder's own scale() picks a different reduction than Pillow's draft()");
}
