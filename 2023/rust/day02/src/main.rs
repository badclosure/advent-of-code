const CONTENT: &str = include_str!("../input.txt");

fn part0102(content: &str) -> Result<(u32, u32), String> {
    let mut sum_id = 0;
    let mut sum_power = 0;
    for line in content.lines() {
        let (game, cubes) = line.split_once(": ").unwrap();
        let game_id = game[5..game.len()].parse::<u32>().unwrap();
        let mut red = 0;
        let mut green = 0;
        let mut blue = 0;

        for draw in cubes.split("; ") {
            let counts = draw.split(", ");
            for count in counts {
                let (amount, color) = count.split_once(" ").unwrap();
                let amount = amount.parse::<u32>().unwrap();
                match color {
                    "red" => red = red.max(amount),
                    "green" => green = green.max(amount),
                    "blue" => blue = blue.max(amount),
                    _ => (),
                }
            }
        }
        if (red <= 12) && (green <= 13) && (blue <= 14) {
            sum_id += game_id;
        }

        sum_power += red * green * blue;
    }
    Ok((sum_id, sum_power))
}

fn main() {
    println!("part01: {}", part0102(CONTENT).unwrap().0);
    println!("part02: {}", part0102(CONTENT).unwrap().1);
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn works() {
        let example: &str = r#"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"#;

        assert_eq!(part0102(example).unwrap(), (8, 2286));
    }
}
