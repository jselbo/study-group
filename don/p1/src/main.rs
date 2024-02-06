use std::env;
use anyhow::{bail, anyhow, Error};

fn main() -> Result<(), Error> {
    let args:Vec<String> = env::args().collect();

    if args.len() != 3 {
        bail!("usage: ./p1 num1 num2");
    }

    let error_str = "Postive, Whole, numbers only";

    let num1:u128 = match args[args.len() - 2].parse() {
        Ok(i) => i,
        Err(_) => return Err(anyhow!(error_str)),
    };

    let num2:u128 = match args[args.len() - 1].parse(){
        Ok(i) => i,
        Err(_) => return Err(anyhow!(error_str)),
    };

    println!("{}", num1 + num2);
    Ok(())
}
