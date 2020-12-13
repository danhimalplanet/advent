use aoc;
use aoc::ANY;

fn main() {
    let puzzle_input = vec![1003240, 19,ANY,ANY,ANY,ANY,ANY,ANY,ANY,ANY,41,ANY,ANY,ANY,37,ANY,ANY,ANY,ANY,ANY,787,ANY,ANY,ANY,ANY,ANY,ANY,ANY,ANY,ANY,ANY,ANY,ANY,13,ANY,ANY,ANY,ANY,ANY,ANY,ANY,ANY,ANY,23,ANY,ANY,ANY,ANY,ANY,29,ANY,571,ANY,ANY,ANY,ANY,ANY,ANY,ANY,ANY,ANY,ANY,ANY,ANY,ANY,ANY,ANY,ANY,17];

    println!("Part 1: {}", aoc::part1(puzzle_input.clone()));
    println!("Part 2: {}", aoc::part2(puzzle_input, true));
}
