with open("../input/day05.txt", "r") as handle:
    content = handle.readlines()
    stack = content[:9]
    instructions = content[9:]

# TEST_INPUT = """    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2"""

# content = TEST_INPUT.split("\n")
# stack = content[:4]
# instructions = content[4:]


def part1():
    idxs = [stack[-1].index(str(i)) for i in range(1, 10)]

    stacks = []
    stacks2 = []
    for idx in idxs:
        col = []
        col2 = []
        for line in stack[:-1]:
            if line[idx] == " ":
                continue
            else:
                col.append(line[idx])
                col2.append(line[idx])

        stacks.append(col)
        stacks2.append(col2)

    for instruction in instructions:
        if len(instruction) <= 1:
            continue

        particles = instruction.split(" ")
        n_move = int(particles[1])
        from_col = int(particles[3]) - 1
        to_col = int(particles[5]) - 1

        # part1
        for _ in range(n_move):
            to_move = stacks[from_col].pop(0)
            stacks[to_col].insert(0, to_move)

        # part2
        # print(stacks2)
        # print("stack2", n_move, from_col+1, to_col + 1,  stacks2)
        stacks2[to_col] = stacks2[from_col][:n_move] + stacks2[to_col]
        stacks2[from_col] = stacks2[from_col][n_move:]


    print("".join([c[0] for c in stacks]))

    for col in stacks2:
        if len(col) >= 1:
            print(col[0], end="")
        else:
            print(" ", end="")


if __name__ == "__main__":
    part1()
