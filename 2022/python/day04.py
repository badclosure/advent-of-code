TEST_INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

with open("../input/day04.txt", "r") as handle:
    content = handle.readlines()


def parse_line(line):
    lr = line.split(",")
    left = lr[0]
    right = lr[1]
    left_min = int(left.split("-")[0])
    left_max = int(left.split("-")[1])

    right_min = int(right.split("-")[0])
    right_max = int(right.split("-")[1])

    return left_min, left_max, right_min, right_max


def part1():
    num_contains = 0
    for line in content:
        if len(line) <= 1:
            continue
        lmin, lmax, rmin, rmax = parse_line(line)
        if (lmin <= rmin and lmax >= rmax) or (lmin >= rmin and lmax <= rmax):
            num_contains += 1
    return num_contains


def part2():
    num_overlaps = 0
    for line in content:
        if len(line) <= 1:
            continue

        lmin, lmax, rmin, rmax = parse_line(line)
        if (
            (lmin <= rmin and lmax >= rmin)
            or (lmin <= rmax and lmax >= rmax)
            or (rmin <= lmin and rmax >= lmin)
            or (rmin <= lmax and rmax >= lmax)
        ):
            num_overlaps += 1

    return num_overlaps


if __name__ == "__main__":
    print(f"day04-part1: {part1()}")
    print(f"day04-part2: {part2()}")
