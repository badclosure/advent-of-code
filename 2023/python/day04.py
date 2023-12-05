example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def process(lines):
    points_total = 0
    cards_total = 0
    count_winning_numbers = []
    cards = [1] * len(lines)
    for line in lines:
        numbers = line.split(": ")[1]
        winning_numbers, my_numbers = numbers.split(" | ")
        winning_numbers = [
            int(n) for n in winning_numbers.split(" ") if n != " " and n != ""
        ]
        my_numbers = [int(n) for n in my_numbers.split(" ") if n != " " and n != ""]

        count = 0
        for num in my_numbers:
            if num in winning_numbers:
                count += 1

        if count > 0:
            points_total += 2 ** (count - 1)

        count_winning_numbers.append(count)

    print(f"points total is {points_total}")

    for i in range(len(cards)):
        next_few = count_winning_numbers[i]
        for j in range(1, next_few + 1):
            cards[i + j] += cards[i]

    print(cards)
    print(f"count of final cards is {sum(cards)}")


if __name__ == "__main__":
    with open("../input/day04.txt") as f:
        content = [line.strip() for line in f.readlines()]
    process(content)
    # process(example.split("\n"))
