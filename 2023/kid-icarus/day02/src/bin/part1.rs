use std::collections::HashMap;

fn part_one(input: &str) -> u64 {
    let max_cubes = HashMap::from([("red", 12), ("green", 13), ("blue", 14)]);
    // for each game, add up all the colors from each set
    let games = input.split('\n');
    games.fold(0, |mut acc, game| {
        if game.is_empty() {
            return acc;
        }
        let mut iter = game.split(": ");
        let game = iter.next().unwrap();
        let game_id = game.split(' ').next_back().unwrap().parse::<u64>().unwrap();
        let sets = iter.next().unwrap();
        let mut is_valid = true;
        sets.split("; ").for_each(|set| {
            let mut game_cubes = HashMap::new();
            set.split(", ").for_each(|cubes| {
                let mut iter = cubes.split_whitespace();
                let num: u64 = iter.next().unwrap().parse().unwrap();
                let color = iter.next().unwrap();
                *game_cubes.entry(color).or_insert(0) += num;
            });

            for (k, v) in &game_cubes {
                if let Some(max_cube) = max_cubes.get(k) {
                    if v > max_cube {
                        is_valid = false;
                        return;
                    }
                }
            }
        });
        if is_valid {
            acc += game_id;
        }
        acc
    })
}

fn main() {
    let input = include_str!("input.txt");
    println!("part one: {}", part_one(input));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";

        assert_eq!(part_one(input), 8);
    }
}
