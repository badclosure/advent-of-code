use std::fs;

fn main() {
    let input = fs::read_to_string("../input/day1.txt").unwrap();
    let mut data: Vec<usize> = vec![];
    let mut current: usize = 0;

    for line in input.lines() {
        if line.len() == 0 {
            data.push(current);
            current = 0;
        } else {
            current += line.trim().parse::<usize>().unwrap();
        }
    }

    data.sort();

    println!("day1-part1: {}", data[data.len() - 1]);
    println!(
        "day1-part2: {}",
        data[data.len() - 1] + data[data.len() - 2] + data[data.len() - 3]
    );
}
