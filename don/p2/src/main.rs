use anyhow::{Error, Result};
use std::env;
use std::fs;

fn get_pass_key(val: &str) -> u32 {
    let mut num_vec: Vec<u32> = vec![];
    for ele in val.chars() {
        if ele.is_numeric() {
            num_vec.push(u32::from(ele));
        }
    }

    let first_digit: u32 = match num_vec.first() {
        Some(&val) => val,
        None => 0,
    };

    let last_digit: u32 = match num_vec.last() {
        Some(&val) => val,
        None => 0,
    };

    let combined: String = format!("{}{}", std::char::from_u32(first_digit).unwrap(), std::char::from_u32(last_digit).unwrap());
    combined.parse().unwrap()
}

fn main() -> Result<(), Error> {
    let args: Vec<String> = env::args().collect();
    let file_path: &str = &args[1];

    let file: String = fs::read_to_string(file_path)?;
    let lines: Vec<&str> = file.split('\n').collect();

    let mut ret: u32 = 0;
    for line in lines {
        ret += get_pass_key(line);
    }

    print!("{}", ret);

    Ok(())
}
