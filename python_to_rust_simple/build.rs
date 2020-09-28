fn main() -> Result<(), Box<dyn std::error::Error>> {
    tonic_build::compile_protos("../protos/python_to_rust_simple.proto")?;
    Ok(())
}
