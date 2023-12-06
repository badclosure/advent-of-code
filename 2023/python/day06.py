import sys

example_input = """Time:      7  15   30
Distance:  9  40  200"""


def process(times, distances):
    result = 1
    for t, record in zip(times, distances):
        for hold in range(t):
            d = (t - hold) * hold  # (hold == speed)
            if d > record:
                break

        result *= t - hold * 2 + 1
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            lines = f.read().splitlines()
    else:
        lines = example_input.splitlines()

    # p1
    times = [int(x) for x in lines[0][6:].split()]
    distances = [int(x) for x in lines[1][10:].split()]
    print(process(times, distances))

    # p2
    times = [int(lines[0][6:].replace(" ", ""))]
    distances = [int(lines[1][10:].replace(" ", ""))]
    print(process(times, distances))
