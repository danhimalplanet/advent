use std::fs;

fn main() {
    let input = match fs::read_to_string("input.txt") {
        Ok(str) => str,
        Err(e) => panic!("oh no! {}", e)
    };

    let mut increases = 0;
    let nums: Vec<i32> = input.lines().map(|x| x.parse::<i32>().unwrap()).collect();
    let mut sums: Vec<i32> = vec![];

    for (i, num) in nums.iter().enumerate() {
        if i < 2 {
            continue;
        }

        let sum = num + &nums[i - 1] + &nums[i - 2];
        sums.push(sum);
    }

    for (j, sum) in sums.iter().enumerate() {
        if j == 0 {
            continue;
        }
        if sum > &sums[j - 1] {
            increases = increases + 1;
        }
    }
    println!("{}", increases);
}