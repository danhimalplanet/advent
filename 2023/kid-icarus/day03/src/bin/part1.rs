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
    fn is_adjacent_to_symbol(&self, row: u32, col: u32) -> bool {
        for delta_row in [self.height - 1, 0, 1].iter().cloned() {
            for delta_col in [self.width - 1, 0, 1].iter().cloned() {
                if delta_row == 0 && delta_col == 0 {
                    continue;
                }

                let neighbor_row = (row + delta_row) % self.height;
                let neighbor_col = (col + delta_col) % self.width;
                let idx = self.get_index(neighbor_row, neighbor_col);
                if is_symbol(self.cells[idx]) {
                    return true;
                }
            }
        }
        false
    }
}

fn part_one(input: &str) -> u64 {
    let grid = Grid::new(input);
    let mut state = State::Start;
    let mut sum: u64 = 0;
    let mut current_num = String::new();
    for row in 0..grid.height {
        for col in 0..grid.width {
            let idx = grid.get_index(row, col);
            let is_adjacent = grid.is_adjacent_to_symbol(row, col);
            let cell = grid.cells[idx];
            let is_num = cell.is_numeric();
            match (&state, is_num, is_adjacent) {
                (State::Start, true, true) => {
                    current_num.push(cell);
                    state = State::Ignore;
                }
                (State::Start, true, false) => {
                    current_num.push(cell);
                    state = State::Look;
                }
                (State::Start, false, _) => {
                    current_num.push(cell);
                    state = State::Look;
                }
                // in the middle of a string, we are adjacent
                (State::Look, true, true) => {
                    current_num.push(cell);
                    state = State::Ignore;
                }
                // in the middle of a num, we are not adjacent
                (State::Look, true, false) => {
                    current_num.push(cell);
                }
                // if not a num, clear the string
                (State::Look, false, _) => {
                    current_num.clear();
                }
                // in the middle of an adjacent num, keep pushing
                (State::Ignore, true, _) => {
                    current_num.push(cell);
                    // edge case for literally the last cell
                    if idx == grid.cells.len() - 1 {
                        sum += current_num.parse::<u64>().expect("not a number");
                        current_num.clear();
                    }
                }
                // if we're adjacent and done with num, sum it
                (State::Ignore, false, _) => {
                    state = State::Look;
                    sum += current_num.parse::<u64>().expect("not a number");
                    current_num.clear();
                }
            }
        }
    }
    sum
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
    fn test_get_index() {
        let input = "....
..*.
...*";
        let grid = Grid::new(input);
        assert_eq!(grid.cells[grid.get_index(1, 2)], '*');
        assert_eq!(grid.cells[grid.get_index(0, 0)], '.');
        assert_eq!(grid.cells[grid.get_index(2, 3)], '*');
    }

    #[test]
    fn test_is_adjacent() {
        let input = ".5....
..*.4.
......";
        let grid = Grid::new(input);
        assert!(grid.is_adjacent_to_symbol(0, 1));
        assert!(!grid.is_adjacent_to_symbol(1, 4));
    }

    #[test]
    fn test_is_adjacent_edge() {
        let input =".............152#............*......792...334......741........................570*....335..............137..........338..........*......+...
952.........................................................793......583..........623............11........730............50.116.........446";
        let grid = Grid::new(input);
        assert!(grid.is_adjacent_to_symbol(1, 137));
    }

    #[test]
    fn test_part_one() {
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
        assert_eq!(part_one(input), 4361);
    }

    #[test]
    fn test_part_one_edge() {
        let input =".............152#............*......792...334......741........................570*....335..............137..........338..........*......+...
952.........................................................793......583..........623............11........730............50.116.........446";
        assert_eq!(part_one(input), 1791);
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
