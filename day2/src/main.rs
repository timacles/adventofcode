use std::fs::File;
use std::io::{self, BufRead};

static MAX_RED: i32 = 12;
static MAX_GREEN: i32 = 13;
static MAX_BLUE: i32 = 14;

#[derive(Debug)]
enum Token {
    Integer(i32),
    Identifier(String),
    Delimiter(String),
    Whitespace(String),
}


impl Token {
    fn new(value: &String) -> Self {

        if is_whitespace(value) { Token::Whitespace(" ".to_string()) }
        else if is_delim(value) { Token::Delimiter(value.to_string()) }
        else if is_ident(value) { Token::Identifier(value.to_string()) }
        else if is_integer(value) { Token::Integer(value.parse::<i32>().unwrap()) }
        else {
            panic!("Token: {} not found", value);
        } 
    }

    fn get_int(&self) -> i32 {
        let result = match self {
            Token::Integer(v) => v,
            _ => {
                panic!("Couldnt extract int value")
            }
        };
        *result
    }

    fn get_ident(&self) -> &str {
        match self {
            Token::Identifier(v) => v.as_str(),
            _ => {
                panic!("Couldnt extract Identifier value")
            }
        }
    }

    fn as_str(&self) -> String {
        match self {
            Token::Identifier(v) => v.to_string(),
            Token::Integer(v) => v.to_string().clone(),
            Token::Delimiter(v) => v.to_string(),
            Token::Whitespace(v) => v.to_string(),
        }
    }
}


fn parse_tokens(text: &str) -> Vec<Token> {
    let mut result: Vec<Token> = Vec::new();
    let mut current_word = String::new();    

    for c in text.chars() {
        if c.is_whitespace() {
            if !current_word.is_empty() {
                result.push(Token::new(&current_word));
                current_word.clear();
            }
        }
        else if is_delim(&c.to_string()) {
            result.push(Token::new(&current_word));
            current_word.clear();
            result.push(Token::new(&c.to_string()));
        } else {
            current_word.push(c);
        }
    }
    result.push(Token::new(&current_word));

    result
}

#[derive(Debug)]
struct Entry {
    id: i32,
    red: Vec<i32>,
    green: Vec<i32>,
    blue: Vec<i32>,
}

impl Entry {
    fn new(tokens: &mut TokenStream) -> Self {

        let id = tokens.consume_id_tokens();

        let mut red: Vec<i32> = Vec::new();
        let mut blue: Vec<i32> = Vec::new();
        let mut green: Vec<i32> = Vec::new();

        let mut current_val: i32;
        let mut current_color: String;

        // The integer token is always followed by a color token
        // seems to work so far.
        while let Some(token) = tokens.get_token() {
            match token {
                Token::Integer(v) => {
                    current_val = *v;
                    //println!(" peek int val: {:?}", current_val);

                    if let Some(token) = tokens.peek_token() {
                        match token {
                            Token::Identifier(v) => {
                                current_color = v.to_string();
                                match current_color.as_str() {
                                    "red" => { red.push(current_val); },
                                    "green" => { green.push(current_val); },
                                    "blue" => { blue.push(current_val); },
                                    _ => { panic!("color not found") }
                                }
                                
                                //println!(" peek int val: {:?}", current_color);
                            },
                            _ => {}
                        }
                    }

                },
                _ => {}
            }
        }

        Entry {
            id,
            red,
            blue,
            green,
        }
    }

    fn is_valid(&self) -> bool {
        for val in &self.red {
            if *val > MAX_RED { return false; }
        }
        for val in &self.green {
            if *val > MAX_GREEN { return false; }
        }
        for val in &self.blue {
            if *val > MAX_BLUE { return false; }
        }
        true
    }

    fn calculate_product(&self) -> i32 {
        let max_green = &self.green.iter().max().unwrap();
        let max_red = &self.red.iter().max().unwrap();
        let max_blue = &self.blue.iter().max().unwrap();

        *max_green * *max_red * *max_blue
    }

}

struct TokenStream {
    text: String,
    tokens: Vec<Token>,
    pos: usize,
}

impl TokenStream {
    fn new(line: &str) -> Self {
        let tokens = parse_tokens(line);

        TokenStream {
            text: line.to_string(),
            tokens,
            pos: 0,
        }
    }

    fn consume_id_tokens(&mut self) -> i32 {
        if let Some(id_token) = self.tokens.get(1).take() {
            self.pos = 3;
            id_token.get_int()
        } else {
            panic!("couldnt find id token");
        }
    }

    fn peek_token(&self) -> Option<&Token> {
        self.tokens.get(self.pos)
    }

    fn get_token(&mut self) -> Option<&Token> {
        let t = self.tokens.get(self.pos);
        self.pos += 1;
        t
    }

    fn prev_token(&self) -> Option<&Token> {
        self.tokens.get(self.pos - 1)
    }


    fn get_tokens(&self) -> &Vec<Token> {
        &self.tokens
    }

    fn print_contents(self) {
        for t in self.tokens {
            println!("  - {:?}", t);
        }
    }
}

fn example1() -> i32 {

    let example = r#"
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"#;
    
    let mut valid_ids: Vec<i32> = Vec::new();

    for line in example.lines() {
        if line.is_empty() { continue }
        let mut token_stream = TokenStream::new(line);
        let entry = Entry::new(&mut token_stream);

        if entry.is_valid() {
            valid_ids.push(entry.id);
            println!("  valid {:?}", entry);
        }

        println!("{}", line);
    }


    valid_ids.iter().sum()
}


fn example2() -> i32 {

    let example = r#"
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"#;
    
    let mut products: Vec<i32> = Vec::new();

    for line in example.lines() {
        if line.is_empty() { continue }
        let mut token_stream = TokenStream::new(line);
        let entry = Entry::new(&mut token_stream);

        let product = entry.calculate_product();
        products.push(product);
    }

    products.iter().sum()
}

fn part1(file_path: &str) -> Result<i32, io::Error> {
    println!("opening: {}", file_path);
    let file = File::open(file_path)?;
    let reader = io::BufReader::new(file);


    let mut valid_ids: Vec<i32> = Vec::new();
    let mut _count = 0;

    for line in reader.lines() {
        match line {
            Ok(line_content) => {
                //if line.is_empty() { continue }
                let mut token_stream = TokenStream::new(&line_content);
                let entry = Entry::new(&mut token_stream);

                if entry.is_valid() {
                    valid_ids.push(entry.id);
                    println!(" > {}", line_content);
                    println!("   valid: {:?}", entry);
                }
            },
            Err(err) => {
                panic!("failed to parse {}", err);
            }
        }
    }

    let sum: i32 = valid_ids.iter().sum();
    println!("TOTAL: {}", sum);

    Ok(sum)
}


fn part2(file_path: &str) -> Result<i32, io::Error> {
    println!("opening: {}", file_path);
    let file = File::open(file_path)?;
    let reader = io::BufReader::new(file);

    let mut products: Vec<i32> = Vec::new();

    for line in reader.lines() {
        match line {
            Ok(line_content) => {
                let mut token_stream = TokenStream::new(&line_content);
                let entry = Entry::new(&mut token_stream);

                let product = entry.calculate_product();
                products.push(product);

            },
            Err(err) => {
                panic!("failed to parse {}", err);
            }
        }
    }

    let sum: i32 = products.iter().sum();
    println!("TOTAL: {}", sum);

    Ok(sum)
}

fn main() {
    //example1();

    let result = part2("input.txt");

    println!("\n===\nMain finished executing.\n");
}



fn read_file(path: &str) -> Result<i32, io::Error> {
    let file = File::open(path)?;
    let reader = io::BufReader::new(file);
    for line in reader.lines() {
        match line {
            Ok(content) => {
                println!("{}", content.to_string());
            }
            Err(err) => {
                eprintln!("Error reading line: {}", err);
            }
        }
    }
    Ok(0)
}




fn is_delim(in_char: &str) -> bool {
    match in_char {
        ";" | "," | ":" => true,
        _ => false,
    }
}

fn is_whitespace(in_char: &str) -> bool {
    if in_char.trim() == "" {
        return true
    }
    false
} 

fn is_ident(in_str: &str) -> bool {
    match in_str {
        "Game" => true,
        "red" => true,
        "blue" => true,
        "green" => true,
        _ => false
    }
}

fn is_integer(in_str: &str) -> bool {
    true
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
    fn test_example1() {
        let result = example1();
        assert_eq!(result, 8);
    }

    #[test]
    fn test_example2() {
        let result = example2();
        assert_eq!(result, 2286);
    }

    #[test]
    fn test_part1() {
        let result = part1("input.txt").unwrap();
        assert_eq!(result, 1853);
    }

    #[test]
    fn count_tokens() {
        let line = "Game 34: 1 blue, 9 red; 3 blue, 4 red; 3 blue, 5 green, 10 red; 2 blue, 9 red, 5 green";
        println!("line: {}", line);
        let tokens = parse_tokens(line);
        let length = tokens.len();
        let last = tokens.last().unwrap().as_str();
        assert_eq!(length, 32);
        assert_eq!(last, "green");
    }

}
