use std::collections::HashMap;

fn main() {
    let input = include_str!("input.txt");
    println!("sum: {}", part_two(input));
}

fn part_two(input: &str) -> u64 {
    let mut sum: u64 = 0;
    input.split('\n').for_each(|line| {
        let mut num = String::new();
        let new_line = line.to_string();
        if line.is_empty() {
            return;
        }
        let written_numbers = HashMap::from([
            ("one", "1"),
            ("two", "2"),
            ("three", "3"),
            ("four", "4"),
            ("five", "5"),
            ("six", "6"),
            ("seven", "7"),
            ("eight", "8"),
            ("nine", "9"),
        ]);

        let mut i = 0;
        let mut first: char = '\0';

        // first pass go forward
        'outer: while i < new_line.len() {
            let mut word = String::new();
            let mut j = i;

            let c = new_line.chars().nth(j).unwrap();
            if c.is_numeric() {
                first = c;
                break;
            }
            while j < new_line.len() {
                let c = new_line.chars().nth(j).unwrap();
                word.push(c);
                if let Some(replacement) = written_numbers.get(word.as_str()) {
                    first = replacement.chars().next().unwrap();
                    break 'outer;
                }
                j += 1;
            }
            i += 1;
        }
        num.push(first);

        // second pass go backwards
        let mut i = new_line.len() - 1;
        let mut last: char = '\0';
        'outer: while i > 0 {
            let mut word = String::new();
            let mut j = i;
            let c = new_line.chars().nth(j).unwrap();
            if c.is_numeric() {
                last = c;
                break 'outer;
            }
            while j > 0 {
                let c = new_line.chars().nth(j).unwrap();
                let ah = word.clone();
                word = String::from(c);
                word.push_str(ah.as_str());
                if let Some(replacement) = written_numbers.get(word.as_str()) {
                    last = replacement.chars().next().unwrap();
                    break 'outer;
                }
                j -= 1;
            }
            i -= 1;
        }

        if last == '\0' {
            println!("NO LAST!: {}", last);
            num.push(first);
        } else {
            num.push(last);
        }

        println!(
            "line: {}, num: {}, first: {}, last: {}",
            line, num, first, last
        );
        sum += num.parse::<u64>().unwrap();
    });

    sum
}

#[cfg(test)]
mod tests {
    #[test]
    fn test_part_two() {
        let input = "two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7seven8threeeight"; // 29 + 83 + 13 + 24 + 42 + 14 + 78
        assert_eq!(super::part_two(input), 283);
    }

    #[test]
    fn test_part_two_2() {
        let input = "ctrv3hmvjphrffktwothree";
        assert_eq!(super::part_two(input), 33);
    }

    #[test]
    fn test_part_two_3() {
        let input = "oneight";
        assert_eq!(super::part_two(input), 18);
    }
}
