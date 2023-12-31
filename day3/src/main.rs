use std::collections::HashSet;
use std::fs::File;
use std::io::{self, BufReader, BufRead};


fn main() {
    //example1();
    let _ = example1();
    //let _ = part1();
    
}

#[derive(Debug)]
enum Token {
    Symbol(char),
    Int(usize),
}

#[derive(Debug)]
struct Position {
    row: usize,
    col: usize,
}

#[derive(Debug)]
struct Item {
    token: Token,
    pos: Position,
    boundary: Vec<Position>,
}

impl Item {
    fn new(token: Token, pos: Position) -> Self {
        let boundary: Vec<Position>;
        match token {
            Token::Symbol(_) => boundary = calc_symbol_boundary(&pos),
            Token::Int(val) => boundary = calc_int_boundary(val.to_string(), &pos),
        }

        Item { token, pos, boundary }
    }
}

fn calc_symbol_boundary(pos: &Position) -> Vec<Position> {
    let mut result: Vec<Position> = Vec::new();

    let start_row = pos.row - 1; 
    let start_col = pos.col - 2;

    for i in 0..3 {
        let cur_row = start_row + i;

        for j in 0..3 {
            let cur_col = start_col + j; 

            let npos = Position{
                row: cur_row,
                col: cur_col,
            };

            result.push(npos);
        }
    }

    result
}

fn calc_int_boundary(val: String, pos: &Position) -> Vec<Position> {
    let mut result: Vec<Position> = Vec::new();
    let len = val.len();
    
    let start_col = pos.col - len;
    for i in 0..len {
        let cur_col = start_col + i; 

        let npos = Position{
            row: pos.row,
            col: cur_col,
        };

        result.push(npos);
    }
    
    result
}


#[derive(Debug)]
struct Parser {
    items: Vec<Item>,
    pos: Position,
}

impl Parser {
    fn new() -> Self {
        let mut items = Vec::new();
        let mut pos = Position{ row: 0, col: 0 };

        Parser { items, pos }
    }

    fn parse(&mut self, line: String) {
        self.pos.row += 1;
        self.pos.col = 1;

        let mut item = String::new();

        for c in line.chars() {
            self.pos.col += 1;

            if c == '.' {
                if !item.is_empty() {
                    self.handle_number(item.clone());
                    item.clear();
                }
            }
            else if c.is_digit(10) {
                item.push(c);
            }
            else if is_symbol(c) {
                self.handle_symbol(c);
                if !item.is_empty() {
                    self.handle_number(item.clone());
                    item.clear();
                }
            }
            else {
                panic!("unknown character: {}", c);
            }
        }
    }

    fn handle_symbol(&mut self, c: char) {
        let symbol_item = Item::new( 
            Token::Symbol(c), 
            Position { row: self.pos.row, col: self.pos.col }
        );
        self.items.push(symbol_item);
    }

    fn handle_number(&mut self, item: String) {
        let number_item = Item::new( 
            Token::Int(item.parse().expect("Couldn't parse into int")), 
            Position { row: self.pos.row, col: self.pos.col - 1 }
        );  
        self.items.push(number_item);
    }

    fn filter_symbols(&self) -> Vec<&Item> {
        let mut symbols: Vec<&Item> = Vec::new();
        for item in self.items.iter() {
            match item.token {
                Token::Symbol(_) => symbols.push(item),
                _ => {},
            }
        }
        symbols
    }
}


fn example1() -> usize {

    let example = r#"467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."#;

    let mut parser = Parser::new();

    for line in example.lines() {
        println!("{}", line);
        parser.parse(line.to_string());
    }

    for item in &parser.items {
        println!("  - {:?} {:?}", item.token, item.boundary);
    }

    let symbols = parser.filter_symbols();
    for symbol in symbols {
        println!("  - {:?} {:?}", symbol.token, symbol.boundary);
    }

    1
}

fn part1() -> io::Result<()> {
    let reader = open_file("input.txt")?;
    let mut unique = HashSet::new();

    for line in reader.lines() {
        if let Ok(line) = line {
            // Iterate over characters in the line and add them to the HashSet
            for c in line.chars() {
                unique.insert(c);
            }
        }
    }

    println!("unique chars: {:?}", unique);

    Ok(())
}

fn is_symbol(c: char) -> bool {
    match c {
        '=' | '*' | '%' | '&' | '/' | '#' | '@' | '+' | '$' => true,
        _ => false,
    }
}



fn open_file(file_path: &str) -> io::Result<BufReader<File>> {
    let file = File::open(file_path).expect("failed to open file");
    Ok(BufReader::new(file))
}
