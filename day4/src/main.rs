use std::fs::File;
use std::io::{self, BufReader, BufRead};

fn main() {
    println!(" Example 1: {}", example1());
    println!(" Part 1: {}", part1());
    println!(" Example 2: {}", example2());
    println!(" Part 2: {}", part2());
}


fn part1() -> usize {
    let reader = open_file("input.txt").expect("couldnt open file");
    let mut problem = Problem::new();
    for line in reader.lines() {
        if let Ok(line) = line {
            problem.load_entry(&line);
        }
    }
    problem.result()
}

fn part2() -> usize {
    let reader = open_file("input.txt").expect("couldnt open file");
    let mut problem = Problem::new();
    for line in reader.lines() {
        if let Ok(line) = line {
            problem.load_entry(&line);
        }
    }
    problem.result2()
}

fn example2() -> usize {
    let example = example();
    let mut problem = Problem::new();

    for line in example.lines() {
        problem.load_entry(line);
    }

    problem.result2()
}

fn example1() -> usize {
    let example = example();
    let mut problem = Problem::new();

    for line in example.lines() {
        problem.load_entry(line);
    }

    problem.result()
}

#[derive(Debug, Default, Clone)]
struct Entry {
    id: usize,
    winning: Vec<usize>,
    valid: Vec<usize>,
    points: usize,
    points2: usize,
    repetitions: usize,
}

struct Problem {
    entries: Vec<Entry>
}

impl Problem {
    fn new() -> Self {
        Problem { entries: Vec::new() } 
    }
    
    fn load_entry(&mut self, line: &str) {
        let tokens = parse(line);
        let mut entry = Entry::default();

        entry.id = tokens[1].get_int();

        let mut pipe_consumed = false;
        for token in tokens.iter().skip(3) {
            match token {
                Token::Pipe => {
                    pipe_consumed = true;
                    continue;
                },
                _ => {} ,
            }

            if !pipe_consumed {
                entry.winning.push(token.get_int())
            } else {
                let i = token.get_int();
                if entry.winning.contains(&i) {
                    entry.valid.push(i);
                    if entry.points == 0 {
                        entry.points = 1;
                    } else {
                        entry.points *= 2;
                    }
                }
            }
        }
        //println!(" {:?}", entry);
        self.entries.push(entry);
    }

    fn result(&self) -> usize {
        let mut result: usize = 0;
        for entry in &self.entries {
            result += entry.points;
        }
        result
    } 


    fn result2(&mut self) -> usize {

        let mut cloned: Vec<Entry> = self.entries.clone();

        for (idx, entry) in self.entries.iter().enumerate() {

            //println!("id: {} repetitions: {}", entry.id, cloned[idx].repetitions);
            cloned[idx].points2 = cloned[idx].points2 + 1;

            for i in 0..entry.valid.len()  {
                let j = i + 1;
                cloned[idx + j].repetitions = cloned[idx+j].repetitions + 1;
                //print!("  idx: {} reps: {}", idx + j, cloned[idx + j].repetitions);
            }

            for _ in 0..cloned[idx].repetitions  {

                for i in 0..entry.valid.len()  {
                    let j = i + 1;
                    cloned[idx + j].repetitions = cloned[idx+j].repetitions + 1;
                    //print!("  idx: {} reps: {}", idx + j, cloned[idx + j].repetitions);
                }

                cloned[idx].points2 = cloned[idx].points2 + 1;
                //print!("  pts: {}", cloned[idx].points2);
            }

            //print!("  >>> ids 2 stats: {}", cloned[2].repetitions);
            println!("\n=> {} points\n========", cloned[idx].points2);
        }

        let mut result = 0;
        for entry in cloned {
            result += entry.points2;
        }
        result
    }

}



fn example() -> &'static str {
    r#"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"#
}



fn is_delim(in_char: char) -> bool {
    match in_char {
        ':' | '|' => true,
        _ => false,
    }
}

fn is_whitespace(in_char: char) -> bool {
    if in_char == ' ' {
        return true
    }
    false
} 

#[derive(Debug)]
enum Token {
    Ident(String),
    Int(usize),
    Pipe,
    Colon,
}

impl Token {
    fn get_int(&self) -> usize {
        match self {
            Token::Int(i) => *i,
            _ => panic!("unexpected token: {:?}", self)
        }
    }
}

fn parse(line: &str) -> Vec<Token> {
    let mut item = String::new();
    let mut tokens: Vec<Token> = Vec::new();

    for c in line.chars() {
        if is_whitespace(c) {
            if !item.is_empty() {
                tokens.push(to_token(&item));
                item.clear();
            }
        }
        else if is_delim(c) {
            if !item.is_empty() {
                tokens.push(to_token(&item));
                item.clear();
            }
            tokens.push(to_delim_token(c));
        } else {
            item.push(c);
        }
    }
    tokens.push(to_token(&item));
    tokens
}

fn to_token(item: &str) -> Token {
    match item {
        "Card" => Token::Ident(item.to_string()),
        _ => Token::Int(item.parse().expect("couldnt parse into int"))
    }
}

fn to_delim_token(c: char) -> Token {
    match c {
        ':' => Token::Colon,
        '|' => Token::Pipe,
        _ => panic!("impossible delimiter {}", c),
    }
}

fn open_file(file_path: &str) -> io::Result<BufReader<File>> {
    let file = File::open(file_path).expect("failed to open file");
    Ok(BufReader::new(file))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example1() {
        let result = example1();
        assert_eq!(result, 13);
    }

    #[test]
    fn test_example2() {
        let result = example2();
        assert_eq!(result, 30);
    }

    #[test]
    fn test_part1() {
        assert_eq!(part1(), 21485);
    }
}
