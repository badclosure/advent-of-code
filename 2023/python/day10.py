import numpy as np

with open("../input/day10.txt") as f:
    lines = f.read().splitlines()


counts = np.zeros((len(lines), len(lines[0])))
inout = np.zeros((len(lines), len(lines[0])))

grid = lines
for i in range(len(grid)):
    if "S" in grid[i]:
        s_row = i
        s_col = grid[i].index("S")
        break
print(s_row, s_col)

y = s_row
x = s_col
distance = 0
direction = 1

OUT = 1
INSIDE = -1


def update(y, x, arr, val):
    y0, x0 = arr.shape
    if x >= x0 or y >= y0:
        pass
    else:
        arr[y][x] = val


while True:
    # print(y, x)
    distance += 1
    if direction == 0:
        y -= 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y += 1
    elif direction == 3:
        x -= 1
    else:
        raise ValueError("Not possible")

    counts[y][x] = distance
    p = grid[y][x]
    if p == "S":
        break

    if direction == 3:
        if p == "-":
            update(y - 1, x, inout, INSIDE)
            update(y + 1, x, inout, OUT)
        elif p == "L":
            update(y, x - 1, inout, OUT)
            update(y + 1, x, inout, OUT)
        elif p == "F":
            update(y - 1, x, inout, INSIDE)
            update(y, x - 1, inout, INSIDE)
    elif direction == 2:
        if p == "|":
            update(y, x - 1, inout, INSIDE)
            update(y, x + 1, inout, OUT)
        elif p == "L":
            update(y, x - 1, inout, INSIDE)
            update(y + 1, x, inout, INSIDE)
        elif p == "F":
            update(y, x + 1, inout, OUT)
            update(y + 1, x, inout, OUT)
    elif direction == 1:
        if p == "-":
            update(y - 1, x, inout, OUT)
            update(y + 1, x, inout, INSIDE)
        elif p == "7":
            update(y - 1, x, inout, OUT)
            update(y, x + 1, inout, OUT)
        elif p == "J":
            update(y + 1, x, inout, INSIDE)
            update(y + 1, x, inout, INSIDE)
    elif direction == 0:
        if p == "|":
            update(y, x - 1, inout, OUT)
            update(y, x + 1, inout, INSIDE)
        if p == "F":
            update(y, x - 1, inout, OUT)
            update(y - 1, x, inout, OUT)
        if p == "7":
            update(y, x + 1, inout, INSIDE)
            update(y - 1, x, inout, INSIDE)

    if p in "|-":
        pass
    elif p == "L":
        if direction == 3:
            direction = 0
        if direction == 2:
            direction = 1
    elif p == "J":
        if direction == 1:
            direction = 0
        if direction == 2:
            direction = 3
    elif p == "7":
        if direction == 1:
            direction = 2
        if direction == 0:
            direction = 3
    elif p == "F":
        if direction == 0:
            direction = 1
        if direction == 3:
            direction = 2
    else:
        print(p)
        raise ValueError("Not possible route")


inout[counts > 0] = -1
inout[s_row][s_col] = 0
inout = inout.astype(int)


def grow_inside():
    y0, x0 = inout.shape
    for y in range(y0):
        for x in range(x0):
            if inout[y][x] == 0:
                for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if 0 <= y + dy < y0 and 0 <= x + dx < x0:
                        if inout[y + dy][x + dx] > 0:
                            inout[y, x] = 1


for _ in range(5):
    grow_inside()


# p1
total_steps = counts.max()
counts[counts > total_steps / 2] = total_steps - counts[counts > total_steps / 2]
print(int(counts.max()))

# p2
print((inout > 0).sum())
