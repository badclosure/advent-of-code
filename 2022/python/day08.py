import numpy as np

with open("../input/day08.txt", "r") as handle:
    lines = handle.readlines()

trees = []

for line in lines:
    trees.append(np.array([int(x) for x in line.strip("\n")]))

trees = np.stack(trees)

nrow, ncol = trees.shape

nvisible = 99 + 99 + 97 + 97
max_score = 0

for i in range(1, nrow-1):
    for j in range(1, ncol-1):
        height = trees[i, j]
        visible_top = trees[:i, j].max() < height
        visible_bottom = trees[i+1:, j].max() < height
        visible_left = trees[i, :j].max() < height
        visible_right = trees[i, j+1:].max() < height

        if any([visible_top, visible_left , visible_right , visible_bottom]):
            nvisible += 1

        smaller_left = np.where(trees[i, :j] >= height)[0]
        if len(smaller_left) > 0:
            score_left = j - smaller_left[-1]
        else:
            score_left = j
        
        smaller_right = np.where(trees[i, j+1:] >= height)[0]
        if len(smaller_right) > 0:
            score_right = smaller_right[0] + 1
        else:
            score_right = ncol - j - 1

        smaller_top = np.where(trees[:i, j] >= height)[0]
        if len(smaller_top) > 0:
            score_top = i - smaller_top[-1]
        else:
            score_top = i

        smaller_bottom = np.where(trees[i+1:, j] >= height)[0]
        if len(smaller_bottom) > 0:
            score_bottom  = smaller_bottom[0] + 1
        else:
            score_bottom = nrow - i - 1

        current_score = score_bottom * score_top * score_left * score_right
        if current_score > max_score:
            max_score = current_score
            
print("part1", nvisible)
print("part2", max_score)

