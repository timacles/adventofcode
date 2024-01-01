use std::fs::File;
use regex::Regex;
use std::io::{self, BufRead};
use std::collections::HashMap;
use std::collections::BTreeMap;
use lazy_static::lazy_static;

lazy_static! {
    static ref KEY_MAP: HashMap<&'static str, i32> = HashMap::from([
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
        ("6", 6),
        ("7", 7),
        ("8", 8),
        ("9", 9),
    ]);
}

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

/// Find positions of each digit, in word form or numerical
fn find_digit_positions(in_str: &str) -> BTreeMap<usize, &str> {

    let mut pos_map: BTreeMap<usize, &str> = BTreeMap::new();

    for key in KEY_MAP.keys(){
        let v: Vec<_> = in_str.match_indices(key).collect();
        for (pos, _) in v {
            println!("   :: matched ind: {} - {}", pos.to_string(), key);
            pos_map.insert(pos, key); 
        }
    }

    pos_map
}

fn replace_word_ints(in_str: &str) -> String {

    let pos_map = find_digit_positions(&in_str);

    // replace each occurence in sorted order one at a time
    let mut new_str = String::new();
    for (pos, val) in pos_map.iter() {
        let replaced_val = KEY_MAP.get(val).expect("NONE").to_string();
        new_str = new_str + &replaced_val;
    }

    //println!(" org >> {}", in_str);
    //println!(" new >> {}", new_str);
    new_str.to_string()
}

fn convert_to_int(first: &String, last: &String) -> i32 {
    let combined = format!("{}{}", first, last);
    let parsed_number: Result<i32, _> = combined.parse();

    match parsed_number {
        Ok(parsed) => {
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

                let temp_sum: i32 = ints1.iter().sum();

                if line_content.len() == 10 {
                    println!("  {} :: {}", line_content, out1);
                }
                //println!("  {} :: {} >> {}", line_content, out1, temp_sum);
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
   
    let result2 = part2("input1.txt").unwrap_or_default();
    println!(" part 2 result: {}", result2);

    Ok(())
}

/*
 ****************************************************************
 * TESTS ********************************************************
 ****************************************************************
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
        let line = "threeighthreetwonenineighteightwo";
        let result = replace_word_ints(line);
        let to_int = extract_digits(&result);

        assert_eq!(result, "383219882");
    }

    #[test]
    fn replace_overlapping() {
        let line = "eight5oneights";
        let result = replace_word_ints(line);
        let to_int = extract_digits(&result);
        assert_eq!(to_int, 88);
    }

    #[test]
    fn replace_overlapping_demon() {
        let line = "sevenine";
        let result = replace_word_ints(line);
        let to_int = extract_digits(&result);
        assert_eq!(to_int, 79);

        let line = "threeight";
        let result = replace_word_ints(line);
        let to_int = extract_digits(&result);
        assert_eq!(to_int, 38);

        let line = "eightwo";
        let result = replace_word_ints(line);
        let to_int = extract_digits(&result);
        assert_eq!(to_int, 82);

        let line = "nineight";
        let result = replace_word_ints(line);
        let to_int = extract_digits(&result);
        assert_eq!(to_int, 98);
    }
}
