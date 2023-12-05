fn main() {
    let results = process(include_str!("../../../input/day04.txt"));
    println!("results are {}, {}", results.0, results.1);
}

#[allow(unused)]
#[derive(Debug, Clone)]
struct Card {
    id: usize,
    winning_count: usize,
    pub copies: usize,
}

fn process(content: &str) -> (u32, u32) {
    let mut points = 0;
    let mut cards: Vec<Card> = Vec::new();
    let mut counts: Vec<u32> = Vec::new();

    for (id, line) in content.lines().enumerate() {
        let mut count = 0;

        let (card_number, rest) = line.split_once(": ").unwrap();
        let (_, _id) = card_number.split_once(" ").unwrap();
        let (winning_numbers, play_numbers) = rest.split_once(" | ").unwrap();
        let wnumbers: Vec<u8> = winning_numbers
            .split(" ")
            .into_iter()
            .filter(|n| !n.is_empty())
            .map(|n| n.parse::<u8>().unwrap())
            .collect();
        let pnumbers: Vec<u8> = play_numbers
            .split(" ")
            .into_iter()
            .filter(|n| !n.is_empty())
            .map(|n| n.parse::<u8>().unwrap())
            .collect();

        for num in pnumbers.iter() {
            if wnumbers.contains(num) {
                count += 1;
            }
        }

        if count > 0 {
            points += 2_u32.pow(count - 1)
        }

        let card = Card {
            id: id + 1,
            copies: 1,
            winning_count: count as usize,
        };
        cards.push(card);
        counts.push(count);
    }

    dbg!(&cards);
    // part2
    for i in 0..cards.len() {
        for j in 1..cards[i].winning_count + 1 {
            cards[i + j].copies += cards[i].copies;
        }
    }

    dbg!(&cards);
    let count_of_cards = cards.iter().map(|c| c.copies as u32).sum::<u32>();
    (points, count_of_cards)
}
#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_process() {
        let example = r#"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"#;
        assert_eq!(process(example), (13, 30));
    }
}
