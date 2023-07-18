import os

INPUT_TEST = f"""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


with open("../input/day03.txt", "r") as handle:
    content = handle.readlines()


def part1():
    idx_sum = 0

    for line in content:
        if len(line) > 1:
            idx_half = int(len(line) / 2)
            first = line[:idx_half]
            second = line[idx_half:]
            dup = [c for c in letters if (c in first and c in second)]
            idx_sum += letters.index(dup[0]) + 1

    print(idx_sum)


def part2():
    num_groups = int((len(content) - 1) / 3)
    group_priorities = 0

    for i in range(num_groups):
        common = [
            c
            for c in letters
            if (
                c in content[i * 3]
                and c in content[i * 3 + 1]
                and c in content[i * 3 + 2]
            )
        ]
        group_priorities += letters.index(common[0]) + 1

    print(group_priorities)


if __name__ == "__main__":
    part1()
    part2()
