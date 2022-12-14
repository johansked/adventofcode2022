# Regolith Reservoir
# Sand begins pouring into the cave! If you don't quickly figure out where the sand is going, you could quickly become trapped!
# You scan a two-dimensional vertical slice of the cave above you (your puzzle input) 
# and discover that it is mostly air with structures made of rock.
# 
# x,y coordinates that form the shape of the path, where x represents distance to the right and y represents distance down. 
# Each path appears as a single line of text in your scan.
#  After the first point of each path, each point indicates the end of a straight horizontal or vertical line to be drawn from the previous point
# 498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9
# This scan means that there are two paths of rock
# the first path consists of two straight lines,
#  and the second path consists of three straight lines
# the first path consists of a line of rock from 498,4 through 498,6 and another line of rock from 498,6 through 496,6.
# The sand is pouring into the cave from point 500,0.
# Sand is produced one unit at a time
# and the next unit of sand is not produced until the previous unit of sand comes to rest
# Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. 
# If all three possible destinations are blocked, the unit of sand comes to rest
import numpy as np

SAND_START_POINT = [500,0]
SAND_UNITS = 1
FLOOR_DISTANCE = 2
AIR_MARKER = "."
ROCK_MARKER = "#"
SAND_MARKER = "o"

def _create_grid(lines, with_floor):
    global SAND_START_POINT

    sand_start_point = list(SAND_START_POINT)
    min_y = max_y = sand_start_point[1]
    min_x = max_x = sand_start_point[0]
    padding = 8

    paths = []
    for line in lines:
        path = []
        cords = line.split("->")
        for cord in cords:
            x,y = cord.strip().split(",")
            x = int(x)
            y = int(y)
            path.append((x,y))

            if x > max_x:
                max_x = x
            if x < min_x:
                min_x = x
            if y > max_y:
                max_y = y
            if y < min_y:
                min_y = y
        
        paths.append(path)


    padding_x = ((max_y - min_y) + padding) * 2

    n_rows = max_y + padding - min_y
    n_cols = max_x + padding_x - min_x
    grid = np.full((n_rows, n_cols), AIR_MARKER)

    sand_start_point = [sand_start_point[0] + padding_x//2 - min_x, sand_start_point[1] + padding//2 - min_y]
    grid[sand_start_point[1], sand_start_point[0]] = SAND_MARKER

    if with_floor:
        grid[max_y + padding//2 + FLOOR_DISTANCE] = ROCK_MARKER

    for path in paths:
        for i in range(len(path) - 1):
            start_x, start_y = path[i]
            end_x, end_y = path[i + 1]

            start_x += padding_x//2 - min_x
            end_x += padding_x//2 - min_x
            start_y += padding//2 - min_y
            end_y += padding//2 - min_y

            if start_x > end_x:
                temp = start_x
                start_x = end_x
                end_x = temp

            if start_y > end_y:
                temp = start_y
                start_y = end_y
                end_y = temp

            grid[start_y:end_y+1, start_x:end_x+1] = ROCK_MARKER

    return grid, sand_start_point


def _unit(grid, sand_start_point):
    is_end = False
    sand_cords = list(sand_start_point)
    is_at_rest = False
    while not is_at_rest:
        if sand_cords[1] + 1 >= grid.shape[0]:
            is_end = True
            break

        block_below = grid[sand_cords[1] + 1][sand_cords[0]]
        block_diag_left = grid[sand_cords[1]+1][sand_cords[0]-1]
        block_diag_right = grid[sand_cords[1]+1][sand_cords[0]+1]

        if block_below not in [SAND_MARKER, ROCK_MARKER]:
            # Fall down
            sand_cords[1] += 1
        elif block_diag_left not in [SAND_MARKER,ROCK_MARKER]:
            # Fall down left
            sand_cords[1] += 1
            sand_cords[0] -= 1
        elif block_diag_right not in [SAND_MARKER,ROCK_MARKER]:
            # Fall down right
            sand_cords[1] += 1
            sand_cords[0] += 1
        else:
            if sand_cords == sand_start_point:
                is_end = True
                break 
            is_at_rest = True
            grid[sand_cords[1]][sand_cords[0]] = SAND_MARKER

    return is_end

def count_units_at_rest(day_input, with_floor):
    lines = day_input.strip().split("\n")
    grid, sand_start_point_in_grid = _create_grid(lines, with_floor)
    is_end = False
    n_units_at_rest = 0
    while not is_end:
        is_end = _unit(grid, sand_start_point_in_grid)
        if not is_end:
            n_units_at_rest += 1

    if with_floor:
        n_units_at_rest += 1

    return n_units_at_rest, grid
    
if __name__ == '__main__':
    with open('data/inputd14.txt') as f:
        content = f.read()

    n_units, grid = count_units_at_rest(content, False)
            
    with open("day14task1.txt", "w") as f:
        f.writelines('\n'.join([' '.join(row) for row in grid.tolist()]))

    print(f"Task 1: N units at rest {n_units}")

    n_units, grid = count_units_at_rest(content, True)
            
    with open("day14task2.txt", "w") as f:
        f.writelines('\n'.join([' '.join(row) for row in grid.tolist()]))

    print(f"Task 1: N units at rest {n_units}")