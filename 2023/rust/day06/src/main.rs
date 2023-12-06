fn main() {
    let (part1, part2) = process(include_str!("../../../input/day06.txt"));
    println!("part01: {}\npart02: {}", part1, part2);
}

fn calculate(times: Vec<u64>, distances: Vec<u64>) -> u64 {
    let mut result = 1;
    for (t, record) in times.into_iter().zip(distances.into_iter()) {
        for hold in 0..t {
            let d = (t - hold) * hold;
            if d > record {
                result *= t - hold * 2 + 1;
                break;
            }
        }
    }
    result
}

fn process(content: &str) -> (u64, u64) {
    let (t, d) = content.split_once("\n").unwrap();

    // part 01
    let times: Vec<u64> = t[5..]
        .split_whitespace()
        .map(|v| v.parse::<u64>().unwrap())
        .collect();
    let distances: Vec<u64> = d[10..]
        .split_whitespace()
        .map(|v| v.parse::<u64>().unwrap())
        .collect();

    let part1 = calculate(times, distances);

    // part 02
    let times: Vec<u64> = t[5..]
        .replace(" ", "")
        .split_whitespace()
        .map(|v| v.parse::<u64>().unwrap())
        .collect();
    let distances: Vec<u64> = d[10..]
        .replace(" ", "")
        .split_whitespace()
        .map(|v| v.parse::<u64>().unwrap())
        .collect();
    let part2 = calculate(times, distances);

    (part1, part2)
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_process() {
        let example_input = r#"Time:      7  15   30
Distance:  9  40  200"#;
        assert_eq!(process(example_input), (288, 71503));
    }
}
