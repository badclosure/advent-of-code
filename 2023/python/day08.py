import sys
from math import lcm


def process(nodes, maps, steps, p2=False):
    nsteps = []
    for node in nodes:
        total = 0
        while True:
            step = steps[total % len(steps)]
            node = maps[node][step]
            total += 1
            if not p2:
                if node == "ZZZ":
                    nsteps.append(total)
                    break
            else:
                if node.endswith("Z"):
                    nsteps.append(total)
                    break
    return nsteps


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as handle:
            content = handle.read()
            lines = content.splitlines()

    else:
        raise ValueError("Need content")

    maps = {}
    steps = [int(x == "R") for x in list(lines[0])]

    for line in lines[2:]:
        node, d = line.split(" = ")
        maps[node] = d[1:-1].split(", ")

    p1_nodes = ["AAA"]
    p2_nodes = [node for node in maps.keys() if node.endswith("A")]

    nsteps_p1 = process(p1_nodes, maps, steps)
    nsteps_p2 = process(p2_nodes, maps, steps, p2=True)

    print(nsteps_p1[0])
    print(lcm(*nsteps_p2))
