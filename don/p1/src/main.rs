use std::env;
use anyhow::{bail, anyhow, Error};
use ethnum::u256;

fn main() -> Result<(), Error> {
    let args:Vec<String> = env::args().collect();

    if args.len() != 3 {
        bail!("usage: ./p1 num1 num2");
    }

    let error_str = "Postive, Whole, numbers only";

    let num1:u256 = match args[args.len() - 2].parse() {
        Ok(i) => i,
        Err(_) => return Err(anyhow!(error_str)),
    };

    let num2:u256 = match args[args.len() - 1].parse(){
        Ok(i) => i,
        Err(_) => return Err(anyhow!(error_str)),
    };

    println!("{}", num1 + num2);
    Ok(())
}
