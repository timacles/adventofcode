use std::fs::File;
use std::io::{self, BufReader, BufRead};

fn main() {
    //println!("Example 1: {}", example1());
    //println!("Part 1: {}", part1());
    //println!("Example 2: {}", example2());
    println!("Part 2: {}", part2());
}

fn solve(problem: &Problem) -> usize {
    let mut locations: Vec<usize> = Vec::new();

    for seed in &problem.seeds {
        //println!("seed: {} =========================", seed);
        let mut source = *seed; 
        for map in &problem.maps {
            //println!("  map: {}", map.label);
            let mut dest = source;
            for entry in &map.entries {
                let result = entry.get_dest(source);
                match result {
                    Some(val) => { dest = val; },
                    None => {}
                }
            }
            source = dest;
            //println!(" - {:?}", dest);
        }
        locations.push(source);
        //println!(" location: {:?}", source);
    }
    let min = locations.iter().min().unwrap();
    *min
}

fn solve2(problem: &Problem) -> usize {
    let mut locations: Vec<usize> = Vec::new();

    for seed in &problem.seeds2 {
        //println!("seed: {} =========================", seed);
        let mut source = *seed; 
        for map in &problem.maps {
            //println!("  map: {}", map.label);
            let mut dest = source;
            for entry in &map.entries {
                let result = entry.get_dest(source);
                match result {
                    Some(val) => { dest = val; },
                    None => {}
                }
            }
            source = dest;
            //println!(" - {:?}", dest);
        }
        locations.push(source);
        //println!(" location: {:?}", source);
    }
    let min = locations.iter().min().unwrap();
    *min
}

#[derive(Debug)]
struct Problem {
    seeds: Vec<usize>,
    seeds2: Vec<usize>,
    maps: Vec<Map>,
}

#[derive(Debug)]
struct Map {
    label: String,
    entries: Vec<Entry>
}

#[derive(Debug)]
struct Entry {
    dest: usize,
    source: usize,
    length: usize
}

impl Entry {
    fn get_dest(&self, val: usize) -> Option<usize> {
        if val >= self.source && val < self.source + self.length {
            let diff = val - self.source;
            Some(self.dest + diff)
        } else { 
            None 
        }
    }
}

fn get_seeds_part2(in_vals: &Vec<usize>) -> Vec<usize> {
    let mut seeds: Vec<usize> = Vec::new();

    for (i, &start) in in_vals.iter().enumerate().step_by(2) {

        let end = start + in_vals[i + 1];

        for j in start..=end {
            seeds.push(j);
        }
    }

    seeds
}


impl Problem {
    fn new() -> Self {
        Problem {
            seeds: Vec::new(),
            seeds2: Vec::new(),
            maps: Vec::new(),
        }
    }


    fn parse(&mut self, line: &str) {

        if line.is_empty() { return; }

        let split: Vec<&str> = line.split_whitespace().collect();

        if split[0] == "seeds:" {
            self.seeds = split.iter().skip(1).filter_map(|s| s.parse().ok()).collect();
            self.seeds2 = get_seeds_part2(&self.seeds);
        } else if split[1] == "map:" {
            let map = Map { 
                label: split[0].to_string(),
                entries: Vec::new(),
            };
            self.maps.push(map);
        } else {
            let vals: Vec<usize> = split.iter().filter_map(|s| s.parse().ok()).collect();
            let entry = Entry {
                dest: vals[0], 
                source: vals[1],
                length: vals[2]
            };
            if let Some(last_map) = self.maps.last_mut() {
                last_map.entries.push(entry);
            }
        }
    }
}




fn example() -> &'static str {
    r#"seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"#
}


fn example1() -> usize {
    let example = example();
    let mut problem = Problem::new();

    for line in example.lines() {
        problem.parse(line);
    }

    solve(&problem)
}


fn example2() -> usize {
    let example = example();
    let mut problem = Problem::new();

    for line in example.lines() {
        problem.parse(line);
    }

    solve2(&problem)
}

fn part1() -> usize {
    let reader = open_file("input.txt").expect("couldnt open file");
    let mut problem = Problem::new();
    for line in reader.lines() {
        if let Ok(line) = line {
            problem.parse(&line);
        }
    }
    solve(&problem)
}


fn part2() -> usize {
    let reader = open_file("input.txt").expect("couldnt open file");
    let mut problem = Problem::new();
    for line in reader.lines() {
        if let Ok(line) = line {
            problem.parse(&line);
        }
    }
    solve2(&problem)
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
        assert_eq!(result, 35);
    }

    #[test]
    fn test_part1() {
        assert_eq!(part1(), 240320250);
    }

    #[test]
    fn test_example2() {
        let result = example2();
        assert_eq!(result, 46);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2(), 28580589);
    }
}
