import sys
from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    Right = 0
    Down = 1
    Left = 2
    Up = 3


@dataclass(frozen=True)
class Tile:
    x: int
    y: int


starting = [(Tile(0, 0), Direction.Right)]
cached = set()
energized = set()


def travel(tile: Tile, direction: Direction):
    global starting
    global cached
    global energized
    x = tile.x
    y = tile.y

    while 0 <= x < len(lines[0]) and 0 <= y < len(lines):
        if (x, y, direction) in cached:
            return
        else:
            cached.add((x, y, direction))
        energized.add((x, y))

        if lines[y][x] == ".":
            match direction:
                case Direction.Right:
                    x += 1
                case Direction.Down:
                    y += 1
                case Direction.Left:
                    x -= 1
                case Direction.Up:
                    y -= 1

        elif lines[y][x] == "-":
            match direction:
                case Direction.Right:
                    x += 1
                case Direction.Up | Direction.Down:
                    starting.append((Tile(x + 1, y), Direction.Right))
                    starting.append((Tile(x - 1, y), Direction.Left))
                    return
                case Direction.Left:
                    x -= 1

        elif lines[y][x] == "|":
            match direction:
                case Direction.Left | Direction.Right:
                    starting.append((Tile(x, y + 1), Direction.Down))
                    starting.append((Tile(x, y - 1), Direction.Up))
                    return
                case Direction.Down:
                    y += 1
                case Direction.Up:
                    y -= 1
        elif lines[y][x] == "/":
            match direction:
                case Direction.Right:
                    direction = Direction.Up
                    y -= 1
                case Direction.Down:
                    direction = Direction.Left
                    x -= 1
                case Direction.Left:
                    direction = Direction.Down
                    y += 1
                case Direction.Up:
                    direction = Direction.Right
                    x += 1
        elif lines[y][x] == "\\":
            match direction:
                case Direction.Right:
                    direction = Direction.Down
                    y += 1
                case Direction.Down:
                    direction = Direction.Right
                    x += 1
                case Direction.Left:
                    direction = Direction.Up
                    y -= 1
                case Direction.Up:
                    direction = Direction.Left
                    x -= 1
    return


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            lines = f.read().splitlines()
    else:
        lines = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....""".splitlines()

    # part 01
    starting = [(Tile(0, 0), Direction.Right)]
    cached = set()
    energized = set()
    while len(starting) > 0:
        travel(*starting.pop())

    print(len(energized))

    # part 02
    starting_p2 = []
    counts = []

    for x, direction in zip([0, len(lines[0]) - 1], [Direction.Right, Direction.Left]):
        for y in range(len(lines)):
            starting_p2.append((Tile(x, y), direction))

    for y, direction in zip([0, len(lines) - 1], [Direction.Down, Direction.Up]):
        for x in range(len(lines[0])):
            starting_p2.append((Tile(x, y), direction))

    for tile, direction in starting_p2:
        starting = [(tile, direction)]
        cached = set()
        energized = set()
        while len(starting) > 0:
            travel(*starting.pop())

        counts.append(len(energized))

    print(max(counts))
