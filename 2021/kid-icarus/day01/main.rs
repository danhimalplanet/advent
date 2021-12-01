use std::fs;

fn main() {
    let input = match fs::read_to_string("input.txt") {
        Ok(str) => str,
        Err(e) => panic!("oh no! {}", e)
    };

    let mut increases = 0;
    let nums: Vec<i32> = input.lines().map(|x| x.parse::<i32>().unwrap()).collect();
    for (i, num) in nums.iter().enumerate() {
        if i == 0 {
            continue;
        }

        if num > &nums[i - 1] {
            increases = increases + 1;
        }
    }
    println!("{}", increases);
}