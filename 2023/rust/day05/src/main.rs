fn main() {
    let (part1, part2) = process(include_str!("../../../input/day05.txt"));
    println!("part01: {}\npart02: {}", part1, part2);
}

fn process(content: &str) -> (u32, u32) {
    (0, 0)
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_process() {
        let example_input = r#""#;
        assert_eq!(process(example_input), (0, 0));
    }
}
