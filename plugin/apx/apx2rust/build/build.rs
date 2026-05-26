use std::env;
use std::fs;
use std::path::Path;

use implementation::from_lib;

fn main() {
    from_lib();
    let out_dir = env::var_os("OUT_DIR").unwrap();
    let dest_path = Path::new(&out_dir).join("generated.rs");
    fs::write(&dest_path, "pub fn hello_from_generator() { println!(\"Hello from generated!\") }").unwrap();
    println!("cargo:rerun-if-changed=build.rs");
}
