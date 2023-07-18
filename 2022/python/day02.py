import os
from typing import Tuple

scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3,
}

stra_win = ["B", "C", "A"]
stra_draw = ["A", "B", "C"]
stra_lose = ["C", "A", "B"]


def compute_outcome1(left: str, right: str) -> int:
    delta = scores[right] - scores[left]
    if (delta == 1) or (delta == -2):
        return scores[right] + 6
    elif delta == 0:
        return scores[right] + 3
    else:
        return scores[right]


def compute_outcome2(left: str, right: str) -> int:
    if right == "X":
        return scores[stra_lose[scores[left] - 1]]
    elif right == "Y":
        return scores[stra_draw[scores[left] - 1]] + 3
    else:
        return scores[stra_win[scores[left] - 1]] + 6


def parse_line(line: str) -> Tuple[str, str]:
    inputs = line.rstrip("\n").split(" ")
    return (inputs[0], inputs[1])


def main():
    with open("../input/day2.txt", "r") as handle:
        lines = handle.readlines()

    sum_score1 = 0
    sum_score2 = 0
    for line in lines:
        if len(line) > 1:
            numbers = parse_line(line)
            sum_score1 += compute_outcome1(*numbers)
            sum_score2 += compute_outcome2(*numbers)

    print(f"day2-part1: {sum_score1}")
    print(f"day2-part2: {sum_score2}")


if __name__ == "__main__":
    main()
