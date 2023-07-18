use std::{fs, println};

const LETTERS: &'static str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

fn main() {
    let input = fs::read_to_string("../input/day03.txt").unwrap();

    let mut priority_sum = 0;
    let mut priority_group = 0;

    // part 1
    for line in input.lines() {
        let num_char = line.len() / 2;
        let first = line[0..num_char].to_string();
        let second = line[num_char..].to_string();

        for char in LETTERS.chars() {
            if first.contains(char) && second.contains(char) {
                priority_sum += 1 + LETTERS.chars().position(|c| c == char).unwrap();
            }
        }
    }

    // part 2
    let lines: Vec<&str> = input.lines().collect();
    let num_groups = lines.len() / 3;
    for i in 0..num_groups {
        for char in LETTERS.chars() {
            if lines[i * 3].contains(char)
                && lines[i * 3 + 1].contains(char)
                && lines[i * 3 + 2].contains(char)
            {
                priority_group += 1 + LETTERS.chars().position(|c| c == char).unwrap();
            }
        }
    }
    println!("day03-part1: {}", priority_sum);
    println!("day03-part2: {}", priority_group);
}
