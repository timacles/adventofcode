mod main;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example1() {
        let result = part1("example1.txt").unwrap_or_default();
        assert_eq!(result, 142);
    }
}

