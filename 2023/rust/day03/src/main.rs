use std::collections::HashMap;

use regex::Regex;

fn main() {
    let results = process(include_str!("../../../input/day03.txt"));
    println!("part01: {}, {}", results.0, results.1);
}

#[allow(unused)]
#[derive(Debug)]
struct Number {
    row: usize,
    span: (usize, usize),
    value: u32,
    is_part: bool,
    adjacent_gears: Vec<(usize, usize)>,
}

// #[allow(unused)]
// #[derive(Debug)]
// struct Gear {
//     position: (usize, usize),
//     parts: Vec<Number>,
// }

fn process(content: &str) -> (u32, u32) {
    let re = Regex::new(r"\d+").unwrap();

    let mut gears: HashMap<(usize, usize), Vec<u32>> = HashMap::new();

    let mut engine_sum = 0;
    let mut ratio_sum = 0;

    let lines = content
        .lines()
        .map(String::from)
        .collect::<Vec<String>>();

    let mut numbers: Vec<Number> = Vec::new();
    for (row, line) in lines.iter().enumerate() {
        let matches = re.find_iter(line);
        for m in matches {
            let value = m.as_str().parse::<u32>().unwrap();
            let mut is_part = false;
            let mut adjacent_gears: Vec<(usize, usize)> = Vec::new();

            println!("Checking for {}:", m.as_str());

            for y in row.saturating_sub(1)..row + 2 {
                if y >= lines.len() {
                    break;
                }
                for x in m.start().saturating_sub(1)..m.end() + 1 {
                    if x >= line.len() {
                        break;
                    }

                    let to_check = lines.get(y).unwrap().chars().nth(x).unwrap();
                    print!("{}", to_check);
                    if to_check.is_ascii_digit() || to_check == '.' {
                    } else if to_check == '*' {
                        adjacent_gears.push((x, y));
                        is_part = true;
                        if let std::collections::hash_map::Entry::Vacant(e) = gears.entry((x, y)) {
                            e.insert(vec![value]);
                        } else {
                            gears.get_mut(&(x, y)).unwrap().push(value);
                        }
                    } else {
                        is_part = true;
                    }
                }
                println!();
            }

            let number = Number {
                row,
                span: (m.start(), m.end()),
                value: m.as_str().parse::<u32>().unwrap(),
                is_part,
                adjacent_gears,
            };

            if is_part {
                engine_sum += number.value;
            }

            numbers.push(number);
        }
    }

    for (_, parts) in &gears {
        if parts.len() == 2 {
            ratio_sum += parts[0] * parts[1];
        }
    }
    // println!("{:?}", gears);
    (engine_sum, ratio_sum)
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_process() {
        let example = r#"467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."#;
        assert_eq!(process(example), (4361, 467835));
    }
}
