use std::fs;

fn main() {
    let input = fs::read_to_string("../input/day2.txt").unwrap();
    let mut sum_score1: u32 = 0;
    let mut sum_score2: u32 = 0;

    for line in input.lines() {
        if line.len() == 0 {
            continue;
        } else {
            let (left, right) = parse_line(line);
            sum_score1 += compute_outcome1(&left, &right);
            sum_score2 += compute_outcome2(&left, &right);
        }
    }

    println!("day2-part1: {}", sum_score1);
    println!("day2-part2: {}", sum_score2);
}

fn parse_line(line: &str) -> (String, String) {
    let output: Vec<String> = line.trim().split(" ").map(|m| m.to_string()).collect();

    (
        output.get(0).unwrap().to_owned(),
        output.get(1).unwrap().to_owned(),
    )
}

fn compute_outcome1(left: &String, right: &String) -> u32 {
    let val_left = match left.as_str() {
        "A" => 1,
        "B" => 2,
        "C" => 3,
        _ => 4,
    };
    let val_right = match right.as_str() {
        "X" => 1,
        "Y" => 2,
        "Z" => 3,
        _ => 4,
    };

    let delta: i32 = val_right as i32 - val_left as i32;
    if (delta == 1) || (delta == -2) {
        val_right + 6
    } else if delta == 0 {
        val_right + 3
    } else {
        val_right
    }
}
fn compute_outcome2(left: &String, right: &String) -> u32 {
    let val_left = match left.as_str() {
        "A" => 1,
        "B" => 2,
        "C" => 3,
        _ => 4,
    };
    let retval = match right.as_str() {
        "X" => {
            if val_left == 1 {
                3
            } else {
                val_left - 1
            }
        }
        "Y" => 3 + val_left,
        "Z" => {
            if val_left == 3 {
                6 + 1
            } else {
                6 + val_left + 1
            }
        }
        _ => 4,
    };

    retval
}

#[cfg(test)]
mod test {
    use super::*;

    const INPUT: &str = r"A Y
B X
C Z";

    #[test]
    fn part2_test() {
        let mut result = 0;
        for line in INPUT.lines() {
            let (left, right) = parse_line(line);
            result += compute_outcome2(&left, &right);
        }
        assert_eq!(result, 12);
    }
}
