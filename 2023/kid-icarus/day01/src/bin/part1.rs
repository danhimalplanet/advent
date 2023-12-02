fn part_one(input: &str) -> u64 {
    input.split('\n').fold(0, |acc, line| {
        if line.is_empty() {
            return acc;
        }
        let mut num = String::new();
        let mut numeric_chars = line.chars().filter(|c| c.is_numeric());
        let first = numeric_chars.next().unwrap();
        num.push(first);
        let last = match numeric_chars.next_back() {
            Some(c) => c,
            None => first,
        };
        num.push(last);
        let num: u64 = num.parse().unwrap();
        acc + num
    })
}

fn main() {
    let input = include_str!("input.txt");
    println!("sum: {}", part_one(input));
}

#[cfg(test)]
mod tests {
    #[test]
    fn test_part_one() {
        let input = "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet";
        assert_eq!(super::part_one(input), 142);
    }
}
