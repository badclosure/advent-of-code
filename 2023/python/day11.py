def process(lines, multiplier: int):
    galaxies = []
    exrows = []
    excols = []
    counts_col = [0] * len(lines[0])

    for row, line in enumerate(lines):
        if "#" not in line:
            exrows.append(row)
        for col, spot in enumerate(line):
            if spot == "#":
                galaxies.append((row, col))
                counts_col[col] += 1


    total = 0
    expansion = multiplier - 1
    while len(galaxies) > 1:
        gal = galaxies.pop(0)
        x0 = gal[1]
        dx = len([x for x in counts_col[:x0] if x == 0])
        x0 += dx * expansion
        y0 = gal[0]
        dy = len([y for y in exrows if y < y0])
        y0 += dy * expansion
        # print(x0, y0)

        for other in galaxies:
            x1 = other[1]
            dx = len([x for x in counts_col[:x1] if x == 0])
            x1 += dx * expansion
            y1 = other[0]
            dy = len([y for y in exrows if y < y1])
            y1 += dy * expansion
            # print(x0, y0, x1, y1)
            total += abs(x1 - x0) + abs(y1 - y0)

    print(total)

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            lines = f.read().splitlines()

    p1 = process(lines, multiplier=2)
    p2 = process(lines, multiplier=1_000_000)