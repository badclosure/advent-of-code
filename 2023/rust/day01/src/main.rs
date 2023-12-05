const REPLACEMENT: [(&str, &str); 9] = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
];

fn part01(content: &str) -> u32 {
    let mut sum = 0;
    for line in content.lines() {
        let digits: Vec<u32> = line
            .chars()
            .into_iter()
            .filter(|c| c.is_numeric())
            .map(|c| c.to_digit(10).unwrap())
            .collect();

        sum += digits.get(0).unwrap() * 10 + digits.get(digits.len() - 1).unwrap();
    }

    println!("PART01: {}", sum);
    sum
}

fn get_first_digit(line: &str) -> u32 {
    let mut retval = 0;
    'outer: for i in 0..line.len() {
        if line.chars().nth(i).unwrap().is_digit(10) {
            retval = line.chars().nth(i).unwrap().to_digit(10).unwrap();
            break 'outer;
        } else {
            for (spelled, numeric) in REPLACEMENT.into_iter() {
                if i + spelled.len() > line.len() {
                    continue;
                }
                if &line[i..i + spelled.len()] == spelled {
                    retval = numeric.parse::<u32>().unwrap();
                    break 'outer;
                }
            }
        }
    }
    retval
}

fn get_last_digit(line: &str) -> u32 {
    let mut retval: u32 = 0;
    'outer: for i in (0..line.len()).rev() {
        if line.chars().nth(i).unwrap().is_digit(10) {
            retval = line.chars().nth(i).unwrap().to_digit(10).unwrap();
            break 'outer;
        } else {
            for (spelled, numeric) in REPLACEMENT.into_iter() {
                if i < spelled.len() {
                    continue;
                }
                if &line[i - spelled.len() + 1..i + 1] == spelled {
                    retval = numeric.parse::<u32>().unwrap();
                    break 'outer;
                }
            }
        }
    }
    retval
}

fn part02(content: &str) -> u32 {
    let mut sum = 0;
    for line in content.lines() {
        let first_digit = get_first_digit(line);
        let last_digit = get_last_digit(line);
        sum += first_digit * 10 + last_digit;
    }

    println!("PART02: {}", sum);
    sum
}

fn main() {
    let content = include_str!("../input.txt");
    part01(content);
    part02(content);
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_part01() {
        let test_input = r#"1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"#;
        assert_eq!(part01(test_input), 142);
    }

    #[test]
    fn test_part02() {
        let test_input = r#"two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"#;
        assert_eq!(part02(test_input), 281);
    }
}
