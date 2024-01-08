fn example1() -> usize {
    let example = example();
    let problem = Problem::new();

    for line in example.lines() {
        let tokens = parse(line);
        println!("{:?}", tokens);
    }

    1
}

struct Problem {
    entries: Vec<Entry>
}

#[derive(Debug, Default)]
struct Entry {
    id: usize,
    winning: Vec<usize>,
    valid: Vec<usize>,
}

#[derive(Debug)]
enum Token {
    Ident(String),
    Int(usize),
    Pipe,
    Colon,
}


impl Problem {
    fn new() -> Self {
        Problem { entries: Vec::new() } 
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

fn example() -> &'static str {
    r#"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"#
}

fn main() {
    println!(" example1: {}", example1());
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
