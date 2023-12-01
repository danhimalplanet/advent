use std::fs;
fn main() {
    let mut sum: u64 = 0;
    let input = fs::read_to_string("input.txt").unwrap();
    input.split('\n').for_each(|line| {
        let mut num = String::new();
        if line.is_empty() {
            return;
        }
        let mut numeric_chars = line.chars().filter(|c| c.is_numeric());
        let first = numeric_chars.next().unwrap();
        num.push(first);
        let last = match numeric_chars.next_back() {
            Some(c) => c,
            None => first,
        };
        num.push(last);
        let num: u64 = num.parse().unwrap();
        sum += num;
    });
    println!("Sum: {}", sum);
}
