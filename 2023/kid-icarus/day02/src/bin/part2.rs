use std::collections::HashMap;

fn part_two(input: &str) -> u64 {
    // for each game, add up all the colors from each set
    let games = input.split('\n');
    games.fold(0, |mut acc, game| {
        if game.is_empty() {
            return acc;
        }
        let sets = game.split(": ").nth(1).unwrap();
        let mut min_cubes = HashMap::new();
        sets.split("; ").for_each(|set| {
            set.split(", ").for_each(|cubes| {
                let mut iter = cubes.split_whitespace();
                let num: u64 = iter.next().unwrap().parse().expect("not a valid digit");
                let color = iter.next().unwrap();
                let entry = *min_cubes.entry(color).or_insert(num);
                if let Some(min_cube) = min_cubes.get_mut(color) {
                    if entry > num {
                        *min_cube = entry;
                    } else {
                        *min_cube = num;
                    }
                }
            });
        });
        let mut power = 1;
        for (_k, v) in min_cubes {
            power *= v;
        }
        acc += power;
        acc
    })
}

fn main() {
    let input = include_str!("input.txt");
    println!("part two: {}", part_two(input));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_two() {
        let input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";

        assert_eq!(part_two(input), 2286);
    }
}
