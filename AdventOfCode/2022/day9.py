# Rope bridge
# Where not to step
# Rope with knot at each end.
#     ...TH...
# the head (H) and tail (T) must always be touching  (diagonally adjacent and even overlapping both count as touching)
# 
# ....
# .TH.
# ....
#
# ....
# .H..
# ..T.
# ....
#
# ...
# .H. (H covers T)
# ...
#
# If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:
# Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:
# So either move one step left,right or diagonal
# You just need to work out where the tail goes as the head follows a series of motions. Assume the head and the tail both start at the same position, overlapping.
#
# Example
# R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2
#
# This series of motions moves the head right four steps, then up four steps, then left three steps, then down one step, and so on. After each step, you'll need to update the position of the tail if the step means the head is no longer adjacent to the tail
#
# After simulating the rope, you can count up all of the positions the tail visited at least once.
# Task: How many positions does the tail of the rope visit at least once?

def _parse_input(inp):
    return [
        (line.split(" ")[0], int(line.split(" ")[1])) 
    for line in inp.split("\n") ]

def _walk(knot_positions, steps, direction, tail_visited_points, step_length = 1):
    for step in range(steps):
        # Move head in dir one step
        if direction == "R":
            knot_positions[0][1] += 1
        elif direction == "L":
            knot_positions[0][1] -= 1
        elif direction == "U":
            knot_positions[0][0] += 1
        else:
            knot_positions[0][0] -= 1

        for i in range(len(knot_positions) - 1):
            # Check if tail should move
            head_tail_row_dif = knot_positions[i][0] - knot_positions[i + 1][0]
            head_tail_col_dif = knot_positions[i][1] - knot_positions[i + 1][1]

            col_step = step_length if head_tail_col_dif > 0 else -step_length
            row_step = step_length if head_tail_row_dif > 0 else -step_length

            if (abs(head_tail_col_dif) > 1 and abs(head_tail_row_dif) > 0) or (abs(head_tail_col_dif) > 0 and abs(head_tail_row_dif) > 1):
                # . . .
                # . . H
                # T . .
                # => move T one row and one col

                knot_positions[i + 1][1] += col_step
                knot_positions[i + 1][0] += row_step
                
            elif abs(head_tail_row_dif) > 1:
                # H  
                # . 
                # T 
                # => move tail one row

                knot_positions[i + 1][0] += row_step
            elif abs(head_tail_col_dif) > 1:
                # T . H
                # => move tail one col
                    
                knot_positions[i + 1][1] += col_step
                
            else:
                continue

        if knot_positions[-1] not in tail_visited_points:
            tail_visited_points.append(list(knot_positions[-1]))

def find_unique_visited_points(instructions, n_knots = 10):
    knot_positions = [[0,0] for i in range(n_knots)]
    visited_points = []

    for instruction in instructions:
        direction, steps = instruction
        _walk(knot_positions, steps, direction, visited_points)

    return len(visited_points)

if __name__ == "__main__":
    with open("data/inputd9.txt") as f:
        inp = _parse_input(f.read().strip())

    points_task_1 = find_unique_visited_points(inp, 2)
    points_task_2 = find_unique_visited_points(inp, 10)

    print(f"Task 1: Number of points visited at least once {points_task_1}")
    print(f"Task 2: Number of points visited at least once {points_task_2}")
