fn main() {
    let (part1, part2) = process(include_str!("../../../input/day05.txt"));
    println!("part01: {}\npart02: {}", part1, part2);
}

#[derive(Debug)]
struct Converter {
    low: u64,
    high: u64,
    delta: i64,
}

impl Converter {
    pub fn from_line(line: &str) -> Converter {
        let vals = line
            .split_whitespace()
            .map(|v| v.trim().parse::<u64>().unwrap())
            .collect::<Vec<_>>();
        let dst = vals[0];
        let src = vals[1];
        let vrange = vals[2];
        Converter {
            low: src,
            high: src + vrange,
            delta: dst as i64 - src as i64,
        }
    }
}

#[derive(Debug, Clone)]
struct InputRange {
    low: u64,
    high: u64,
}

impl InputRange {
    pub fn new(low: u64, high: u64) -> InputRange {
        InputRange { low, high }
    }

    pub fn convert(&self, delta: i64) -> InputRange {
        InputRange {
            low: (self.low as i64 + delta) as u64,
            high: (self.high as i64 + delta) as u64,
        }
    }
}

fn intersect(irange: &InputRange, conv: &Converter) -> (Vec<InputRange>, Vec<InputRange>, bool) {
    let mut converted = Vec::new();
    let mut untouched = Vec::new();
    let mut conversion = true;

    if irange.high <= conv.low || irange.low >= conv.high {
        untouched.push(irange.convert(0));
        conversion = false;
    } else if conv.low <= irange.low && irange.low < conv.high && irange.high > conv.high {
        converted.push(InputRange::new(irange.low, conv.high).convert(conv.delta));
        untouched.push(InputRange::new(conv.high, irange.high));
    } else if conv.low < irange.high && conv.high > irange.high && irange.low < conv.low {
        converted.push(InputRange::new(conv.low, irange.high).convert(conv.delta));
        untouched.push(InputRange::new(irange.low, conv.low));
    } else if conv.low <= irange.low && conv.high >= irange.high {
        converted.push(irange.convert(conv.delta));
    } else if irange.low < conv.low && irange.high >= conv.high {
        converted.push(InputRange::new(conv.low, conv.high).convert(conv.delta));
        untouched.push(InputRange::new(irange.low, conv.low));
        untouched.push(InputRange::new(conv.high, irange.high));
    } else {
        panic!("Not supposed to be here")
    }

    (converted, untouched, conversion)
}

fn parse_p2(content: &str) -> (Vec<InputRange>, Vec<Vec<Converter>>) {
    let (seeds, mappings) = content.split_once("\n\n").unwrap();
    let seeds = seeds[7..]
        .split_whitespace()
        .map(|s| s.parse::<u64>().unwrap())
        .collect::<Vec<_>>();
    let seeds_ranges = seeds
        .iter()
        .step_by(2)
        .zip(seeds.iter().skip(1).step_by(2))
        .map(|(a, b)| InputRange::new(*a, *a + *b))
        .collect::<Vec<_>>();
    let mappings = mappings
        .split("\n\n")
        .map(|m| {
            m.lines()
                .filter(|m| m.chars().nth(0).unwrap().is_digit(10))
                .map(|line| Converter::from_line(line))
                .collect::<Vec<Converter>>()
        })
        .collect::<Vec<Vec<Converter>>>();

    (seeds_ranges, mappings)
}
fn parse_p1(content: &str) -> (Vec<InputRange>, Vec<Vec<Converter>>) {
    let (seeds, mappings) = content.split_once("\n\n").unwrap();
    let seeds = seeds[7..]
        .split_whitespace()
        .map(|s| s.parse::<u64>().unwrap())
        .collect::<Vec<_>>();
    let seeds_ranges = seeds
        .iter()
        .map(|s| InputRange::new(*s, *s + 1))
        .collect::<Vec<_>>();
    let mappings = mappings
        .split("\n\n")
        .map(|m| {
            m.lines()
                .filter(|m| m.chars().nth(0).unwrap().is_digit(10))
                .map(|line| Converter::from_line(line))
                .collect::<Vec<Converter>>()
        })
        .collect::<Vec<Vec<Converter>>>();

    (seeds_ranges, mappings)
}

fn process(content: &str) -> (u64, u64) {
    let (seeds_ranges, mappings) = parse_p1(content);

    let mut current_ranges = seeds_ranges.clone();

    for mapping_layer in mappings.iter() {
        let mut new_ranges: Vec<InputRange> = Vec::new();
        while current_ranges.len() > 0 {
            let irange = current_ranges.pop().unwrap();
            let mut conversion_count = 0;
            for conv in mapping_layer.into_iter() {
                let (converted, untouched, has_converted) = intersect(&irange, conv);
                new_ranges.extend_from_slice(&converted);
                if has_converted {
                    conversion_count += 1;
                    current_ranges.extend_from_slice(&untouched);
                    break;
                }
            }
            if conversion_count == 0 {
                new_ranges.push(irange);
            }
        }
        current_ranges = new_ranges.clone();
    }

    let min_location_p1 = current_ranges.iter().map(|r| r.low).min().unwrap();

    let (seeds_ranges, mappings) = parse_p2(content);

    let mut current_ranges = seeds_ranges.clone();

    for mapping_layer in mappings.iter() {
        let mut new_ranges: Vec<InputRange> = Vec::new();
        while current_ranges.len() > 0 {
            let irange = current_ranges.pop().unwrap();
            let mut conversion_count = 0;
            for conv in mapping_layer.into_iter() {
                let (converted, untouched, has_converted) = intersect(&irange, conv);
                new_ranges.extend_from_slice(&converted);
                if has_converted {
                    conversion_count += 1;
                    current_ranges.extend_from_slice(&untouched);
                    break;
                }
            }
            if conversion_count == 0 {
                new_ranges.push(irange);
            }
        }
        current_ranges = new_ranges.clone();
    }

    let min_location_p2 = current_ranges.iter().map(|r| r.low).min().unwrap();
    (min_location_p1, min_location_p2)
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_process() {
        let example_input = r#"seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"#;
        assert_eq!(process(example_input), (35, 46));
    }
}
