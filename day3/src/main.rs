use std::collections::HashSet;
use std::fs::File;
use std::io::{self, BufReader, BufRead};


fn main() {
    //example1();
    println!(" part 2 result: {}", part2());
}


#[derive(Debug)]
enum Token {
    Symbol(char),
    Int(usize),
}

#[derive(Debug, PartialEq, Eq)]
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

    ///fn is_colliding(&self, in_boundary: Vec<&Position>) -> bool {
    fn is_colliding(&self, in_item: &Item) -> bool {
        for pos in &self.boundary {
            for pos2 in &in_item.boundary {
                if pos == pos2 {
                    return true;
                }
            }
        }
        false
    }

    fn to_int(&self) -> usize {
        match self.token {
            Token::Int(i) => return i,
            Token::Symbol(_) => panic!("cant call this on a symbol"),
        }
    }

    fn get_symbol(&self) -> char {
        match self.token {
            Token::Symbol(s) => return s,
            Token::Int(_) => panic!("shouldnt be calling this here"),
        }
    }
}

fn calc_symbol_boundary(pos: &Position) -> Vec<Position> {
    let mut result: Vec<Position> = Vec::new();

    let start_row = pos.row - 1; 
    let start_col = pos.col - 2;   // had to make this `-2` for some reason, otherwise off by one

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
    symbols: Vec<Item>,
    items: Vec<Item>,
    pos: Position,
}

impl Parser {
    fn new() -> Self {
        let mut symbols = Vec::new();
        let mut items = Vec::new();
        let mut pos = Position{ row: 0, col: 0 };

        Parser { items, symbols, pos }
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

        if !item.is_empty() {
            //panic!("r {} i {}", self.pos.row, item);
            self.handle_number(item.clone());
        }
    }

    fn handle_symbol(&mut self, c: char) {
        let symbol_item = Item::new( 
            Token::Symbol(c), 
            Position { row: self.pos.row, col: self.pos.col }
        );
        self.symbols.push(symbol_item);
    }

    fn handle_number(&mut self, item: String) {
        let number_item = Item::new( 
            Token::Int(item.parse().expect("Couldn't parse into int")), 
            Position { row: self.pos.row, col: self.pos.col - 1 }
        );  
        self.items.push(number_item);
    }


    fn sum_valid_items(&self) -> usize {
        let mut valid_vals: Vec<usize> = Vec::new();

        for s in &self.symbols {
            for i in &self.items {
                if s.is_colliding(i) {
                    println!(" pos: {:?} match: {:?} ", i.pos, i.token);
                    valid_vals.push(i.to_int());
                    }
            } 
            //println!("  - {:?} {:?}", s.token, s.boundary);
        }

        valid_vals.iter().sum()
    }

    fn calculate_star_matches(&self) -> usize {
        let mut valid_vals: Vec<usize> = Vec::new();

        for s in &self.symbols {

            if !(s.get_symbol() == '*') {
                continue;
            }

            let mut star_colliders: Vec<usize> = Vec::new();

            for i in &self.items {
                if s.is_colliding(i) {
                    star_colliders.push(i.to_int());
                    //println!(" ps: {:?} match: {:?} ", i.pos, i.token);

                    if star_colliders.len() == 2 {
                        valid_vals.push(star_colliders[0] * star_colliders[1]);
                        break;
                    }
                    }
            } 
            //println!("  - {:?} {:?}", s.token, s.boundary);
        }

        valid_vals.iter().sum()
    }
}


fn example() -> &'static str {
    r#"467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."#
}

fn example2() -> usize {

    let example = example();

    let mut parser = Parser::new();

    for line in example.lines() {
        println!("{}", line);
        parser.parse(line.to_string());
    }

    parser.calculate_star_matches()
}

fn example1() -> usize {

    let example = example();

    let mut parser = Parser::new();

    for line in example.lines() {
        println!("{}", line);
        parser.parse(line.to_string());
    }

    parser.sum_valid_items()
}


fn part1() -> usize {
    let reader = open_file("input.txt").expect("couldnt open file");
    //let mut unique = HashSet::new();

    let mut parser = Parser::new();

    for line in reader.lines() {
        if let Ok(line) = line {
            parser.parse(line.to_string());
        }
    }

    parser.sum_valid_items()
}

fn part2() -> usize {
    let reader = open_file("input.txt").expect("couldnt open file");
    //let mut unique = HashSet::new();

    let mut parser = Parser::new();

    for line in reader.lines() {
        if let Ok(line) = line {
            parser.parse(line.to_string());
        }
    }

    parser.calculate_star_matches()
}

fn is_symbol(c: char) -> bool {
    match c {
        '=' | '*' | '%' | '&' | '/' | '#' | '@' | '+' | '$' | '-' => true,
        _ => false,
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
        assert_eq!(result, 4361);
    }

    #[test]
    fn test_example2() {
        let result = example2();
        assert_eq!(result, 467835);
    }

    #[test]
    fn test_part1() {
        let result = part1();
        assert_eq!(result, 537832);
    }

    #[test]
    fn test_part2() {
        let result = part2();
        assert_eq!(result, 81939900);
    }

}
