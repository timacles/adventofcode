//use std::env;
use std::fs;
use regex::Regex;

fn match_digit(pattern: Regex, in_line: String) -> String {
    for int in pattern.find_iter(&in_line) {
        println!("Found integer: {}", int.as_str());
        return int.as_str().to_string();
    }
    return "none".to_string()
}


fn main() {
    let file_path = "example1.txt";
    let pattern = Regex::new(r"[0-9]").unwrap();

    // --snip--
    println!("In file {}", file_path);

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    println!("\n===\n\n{contents}");


    match_digit(pattern, contents);
}
