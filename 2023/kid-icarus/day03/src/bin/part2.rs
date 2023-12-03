fn part_two(_input: &str) -> u64 {
    todo!()
}

fn main() {
    let input = include_str!("input.txt");
    println!("part one: {}", part_two(input));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_two() {
        let input = "foo";

        assert_eq!(part_two(input), 8);
    }
}
