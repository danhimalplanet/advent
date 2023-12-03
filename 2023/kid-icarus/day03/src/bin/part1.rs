fn part_one(_input: &str) -> u64 {
    let lines = input.lines();
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
}
