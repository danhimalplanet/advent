use std::collections::HashMap;

enum State {
    Start, // we just started, can transition into ignore (found num), or look (found not num)
    Ignore,
    Look,
}

pub struct Grid {
    width: u32,
    height: u32,
    cells: Vec<char>,
}

impl Grid {
    fn new(input: &str) -> Grid {
        let lines: Vec<&str> = input.lines().collect();
        let height = lines.len();
        let width = lines[0].len();
        let cells: Vec<char> = lines
            .into_iter()
            .flat_map(|line| line.chars().collect::<Vec<_>>())
            .collect();

        Grid {
            width: width.try_into().expect("too many columns"),
            height: height.try_into().expect("too many rows"),
            cells,
        }
    }
    fn get_index(&self, row: u32, col: u32) -> usize {
        (row * self.width + col) as usize
    }
    fn is_adjacent_to_symbol(&self, row: u32, col: u32) -> Option<usize> {
        for delta_row in [self.height - 1, 0, 1].iter().cloned() {
            for delta_col in [self.width - 1, 0, 1].iter().cloned() {
                if delta_row == 0 && delta_col == 0 {
                    continue;
                }

                let neighbor_row = (row + delta_row) % self.height;
                let neighbor_col = (col + delta_col) % self.width;
                let idx = self.get_index(neighbor_row, neighbor_col);
                if is_symbol(self.cells[idx]) {
                    return Some(idx);
                }
            }
        }
        None
    }
}

fn part_two(input: &str) -> u64 {
    let mut adjacent_hash_map: HashMap<usize, Vec<u64>> = HashMap::new();
    let grid = Grid::new(input);
    let mut state = State::Start;
    let mut sum: u64 = 0;
    let mut current_num = String::new();
    let mut current_gear_idx: Option<usize> = None;
    for row in 0..grid.height {
        for col in 0..grid.width {
            let idx = grid.get_index(row, col);
            let is_adjacent = grid.is_adjacent_to_symbol(row, col);
            let cell = grid.cells[idx];
            let is_num = cell.is_numeric();
            match (&state, is_num, is_adjacent) {
                (State::Start, true, Some(idx)) => {
                    adjacent_hash_map.insert(idx, Vec::new());
                    current_gear_idx = Some(idx);
                    current_num.push(cell);
                    state = State::Ignore;
                }
                (State::Start, true, None) => {
                    current_num.push(cell);
                    state = State::Look;
                }
                (State::Start, false, _) => {
                    current_num.push(cell);
                    state = State::Look;
                }
                // in the middle of a string, we are adjacent
                (State::Look, true, Some(idx)) => {
                    current_num.push(cell);
                    adjacent_hash_map.entry(idx).or_default();
                    current_gear_idx = Some(idx);
                    state = State::Ignore;
                }
                // in the middle of a num, we are not adjacent
                (State::Look, true, None) => {
                    current_num.push(cell);
                }
                // if not a num, clear the string
                (State::Look, false, _) => {
                    current_num.clear();
                    current_gear_idx = None;
                }
                // in the middle of an adjacent num, keep pushing
                (State::Ignore, true, _) => {
                    current_num.push(cell);
                    // edge case for last cell
                    if idx == grid.cells.len() - 1 {
                        current_num.parse::<u64>().expect("not a number");
                        adjacent_hash_map
                            .get_mut(&current_gear_idx.expect("no gear idx"))
                            .expect("no gear idx")
                            .push(current_num.parse::<u64>().expect("not a number"));
                        current_num.clear();
                        current_gear_idx = None;
                    }
                }
                // if we're adjacent and done with num, sum it
                (State::Ignore, false, _) => {
                    state = State::Look;
                    current_num.parse::<u64>().expect("not a number");
                    adjacent_hash_map
                        .get_mut(&current_gear_idx.expect("no gear idx"))
                        .expect("no gear idx")
                        .push(current_num.parse::<u64>().expect("not a number"));
                    current_num.clear();
                    current_gear_idx = None;
                }
            }
        }
    }
    for (_idx, nums) in adjacent_hash_map {
        if nums.len() == 2 {
            sum += nums[0] * nums[1];
        }
    }
    sum
}

fn is_symbol(c: char) -> bool {
    c == '*'
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
        let input = "467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..";
        assert_eq!(part_two(input), 467835);
    }

    #[test]
    fn test_is_symbol() {
        assert!(is_symbol('*'));
        assert!(!is_symbol('1'));
        assert!(!is_symbol('.'));
        assert!(!is_symbol(' '));
        assert!(!is_symbol('!'));
    }
}
