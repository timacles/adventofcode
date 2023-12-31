use std::env;
use std::fs::File;
use regex::Regex;
use std::io::{self, BufRead};
use std::collections::HashMap;
use std::collections::BTreeMap;

// 3kmtjlfbgssixmspkfzrgxtctksix4onetwones

fn extract_digits(in_line: &str) -> i32 {

    let pattern = Regex::new(r"[0-9]").unwrap();
    let mut matched_integers = Vec::new();

    for int in pattern.find_iter(&in_line) {
        matched_integers.push(int.as_str().to_string());
    }

    let first = matched_integers.first().cloned().unwrap_or_default();
    let last = matched_integers.last().cloned().unwrap_or_default();
    let number = convert_to_int(&first, &last);

    number
}

fn replace_word_ints(in_str: &str) -> String {

    let mut out_str = in_str.to_string();
    let mut pos_map: BTreeMap<usize, &str> = BTreeMap::new();

    let keymap: HashMap<&str, i32> = HashMap::from([
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
    ]);

    // find location of each word
    for key in keymap.keys(){
        if let Some(position) = in_str.find(key) {
            pos_map.insert(position, key); 
        }
    }

    // replace words in sorted order
    for (_key, val) in pos_map.iter() {
        let nval = keymap.get(val).expect("NONE").to_string();
        out_str = out_str.replace(val, &nval);
    }

    out_str
}

fn convert_to_int(first: &String, last: &String) -> i32 {
    let combined = format!("{}{}", first, last);
    let parsed_number: Result<i32, _> = combined.parse();

    match parsed_number {
        Ok(parsed) => {
            //println!("Successfully parsed: {}", parsed);
            parsed
        }
        Err(e) => {
            println!("Failed to parse: {}", e);
            0
        }
    }
}

fn extract1(line: &str) -> i32 {

    let out = extract_digits(line);

    out
}

fn extract2(line: &str) -> i32 {

    let replaced = replace_word_ints(line);
    let out = extract_digits(&replaced);

    out
}


fn part1(file_path: &str) -> Result<i32, io::Error> {
    
    let file = File::open(file_path)?;
    let reader = io::BufReader::new(file);

    let mut ints1: Vec<i32> = Vec::new();

    let mut _count = 0;
    for line in reader.lines() {
        match line {
            Ok(line_content) => {
                _count += 1;
                let out1 = extract1(&line_content);
                ints1.push(out1);
            }
            Err(err) => {
                eprintln!("Error reading line: {}", err);
            }
        }
    }
    
    let total_sum1: i32 = ints1.iter().sum();
    Ok(total_sum1)
}

fn part2(file_path: &str) -> Result<i32, io::Error> {
    
    let file = File::open(file_path)?;
    let reader = io::BufReader::new(file);

    let mut ints1: Vec<i32> = Vec::new();

    let mut _count = 0;
    for line in reader.lines() {
        match line {
            Ok(line_content) => {
                _count += 1;
                let out1 = extract2(&line_content);
                ints1.push(out1);
            }
            Err(err) => {
                eprintln!("Error reading line: {}", err);
            }
        }
    }
    
    let total_sum1: i32 = ints1.iter().sum();
    Ok(total_sum1)
}


fn main() -> io::Result<()> {
   
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!("Requires a file argument: {} <your_argument>", args[0]);
        std::process::exit(1);
    }
    let file_path = &args[1];

    
    Ok(())
}

/****************************************************************
 * TESTS 
 */

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example1() {
        let result = part1("example1.txt").unwrap_or_default();
        assert_eq!(result, 142);
    }

    #[test]
    fn part1_input() {
        let result = part1("input1.txt").unwrap_or_default();
        assert_eq!(result, 53386);
    }

    #[test]
    fn example2() {
        let result = part2("example2.txt").unwrap_or_default();
        assert_eq!(result, 281);
    }

    #[test]
    fn trouble_line1() {
        let line = "3kmtjlfbgssixmspkfzrgxtctksix4onetwones";
        let result = replace_word_ints(line);
        let to_int = extract_digits(&result);

        assert_eq!(result, "3kmtjlfbgs6mspkfzrgxtctk6412nes");
        assert_eq!(to_int, 32);
    }
}
