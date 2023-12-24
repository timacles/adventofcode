use std::fs::File;
use regex::Regex;
use std::io::{self, BufRead};

fn match_digit(pattern: &Regex, in_line: &String) -> Vec<String> {
    let mut matched_integers = Vec::new();

    for int in pattern.find_iter(&in_line) {
        //println!("Found integer: {}", int.as_str());
        matched_integers.push(int.as_str().to_string());
    }

    matched_integers
}


fn main() -> io::Result<()> {
    let file_path = "example1.txt";
    let pattern = Regex::new(r"[0-9]").unwrap();

    println!("In file {}", file_path);

    let file = File::open(file_path)?;
    let reader = io::BufReader::new(file);

    let mut count = 0;

    for line in reader.lines() {
        match line {
            Ok(line_content) => {
                count += 1;

                let out = match_digit(&pattern, &line_content);
                let first = out.first().cloned().unwrap_or_default();
                let last = out.last().cloned().unwrap_or_default();

                println!("{}) [{}] >> {}{}", count, out.join(""), first, last);
            }
            Err(err) => {
                eprintln!("Error reading line: {}", err);
            }
        }
    }

    
    Ok(())
}
