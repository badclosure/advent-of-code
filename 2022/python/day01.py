def get_data():
    with open("../input/day1.txt", "r") as handle:
        lines = handle.readlines()

    sum_calories = 0
    data = []
    for line in lines:
        if line == "\n":
            data.append(sum_calories)
            sum_calories = 0
        else:
            sum_calories += int(line.strip("\n"))
    return data


def part1():
    data = get_data()
    print(f"day1-part1: {max(data)}")


def part2():
    data = get_data()
    sum_calories = sum(sorted(data)[-3:])
    print(f"day1-part2: {sum_calories}")


if __name__ == "__main__":
    part1()
    part2()
