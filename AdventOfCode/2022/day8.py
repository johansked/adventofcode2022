# Tree house
# 1. Enough tree to cover the house?
#       Count the number of trees visible from outside of the grid looking in (row, column)
# Input:
# 30373
# 25512
# 65332
# 33549
# 35390
# Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.
# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it.
# Task 1: how many trees are visible from outside the grid?
# Task 2: To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. What is the highest scenic score possible for any tree?
#       A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

import numpy as np

def _count_trees_shorter(view):
    n_trees = 0
    for i in range(0, len(view)):
        if view[i]:
            n_trees += 1
            break
        else:
            n_trees += 1

    return n_trees

def count_non_visible_trees(inp):
    trees = np.array(inp).astype("int")
    trees_t = trees.transpose()

    nrows, ncols = trees.shape

    n_visible = 0
    for i in range(nrows):
        for j in range(ncols):
            current_value = trees[i][j]

            current_row_higher = (trees[i] - current_value) >= 0
            current_column_higher = (trees_t[j] - current_value) >= 0

            left_higher = current_row_higher[:j].sum() > 0
            right_higher = current_row_higher[j+1:].sum() > 0

            top_higher = current_column_higher[:i].sum() > 0
            bottom_higher = current_column_higher[i+1:].sum() > 0

            if not left_higher or not right_higher or not top_higher or not bottom_higher:
                n_visible += 1

    return n_visible


def max_scenic_score(inp):
    trees = np.array(inp).astype("int")
    trees_t = trees.transpose()

    nrows, ncols = trees.shape

    max_scenic_score = 0
    for i in range(nrows):
        for j in range(ncols):
            current_value = trees[i][j]

            current_row_higher = (trees[i] - current_value) >= 0
            current_column_higher = (trees_t[j] - current_value) >= 0

            n_trees_left = _count_trees_shorter(np.flip(current_row_higher[:j]))
            n_trees_right = _count_trees_shorter(current_row_higher[j+1:])
            n_trees_top = _count_trees_shorter(np.flip(current_column_higher[:i]))
            n_trees_bottom = _count_trees_shorter(current_column_higher[i+1:])

            current_scenic_score = n_trees_left*n_trees_right*n_trees_bottom*n_trees_top

            if current_scenic_score > max_scenic_score:
                max_scenic_score = current_scenic_score

    return max_scenic_score

if __name__ == "__main__":
    with open("data/inputd8.txt") as f:
        content = [list(l) for l in f.read().strip().split("\n")]

    n_visible = count_non_visible_trees(content)
    print(f"Task 1: Number of visible trees {n_visible}")

    max_scenic = max_scenic_score(content)
    print(f"Task 2: Max scenic view is {max_scenic}")