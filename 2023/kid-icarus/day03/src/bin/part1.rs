fn part_one(input: &str) -> u64 {
    let lines = input.lines();
    lines.enumerate();
    0
}

fn is_symbol(c: char) -> bool {
    !c.is_numeric() && c != '.'
}

fn main() {
    let input = include_str!("input.txt");
    println!("part one: {}", part_one(input));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = "foo";

        assert_eq!(part_one(input), 8);
    }

    #[test]
    fn test_is_symbol() {
        assert!(is_symbol('a'));
        assert!(!is_symbol('1'));
        assert!(!is_symbol('.'));
        assert!(is_symbol(' '));
        assert!(is_symbol('!'));
    }
}
