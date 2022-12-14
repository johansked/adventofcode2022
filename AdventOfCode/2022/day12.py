# Hill Climbing Algorithm
# You ask the device for a heightmap of the surrounding area 
# he elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation
# Current position S elevation a
# Best signal position E elevation z
# Reach E with as few step as possible 
# One step úp, down, left, right where de == 1

import string
import numpy as np
import sys

START_MARKER = "S"
START_HEIGHT = "a"
END_MARKER = "E"
END_HEIGHT = "z"
STEP_LENGTH = 1
MAX_ELEVATION_DIFF = 1

elevation_order = string.ascii_lowercase

def _parse_input(day_input):
    return day_input.strip().split("\n")

def _find_start_and_end(elevation_map):
    start_cords = [[i, e.index(START_MARKER)] for i,e in enumerate(elevation_map) if START_MARKER in e][0]
    end_cords = [[i, e.index(END_MARKER)] for i,e in enumerate(elevation_map) if END_MARKER in e][0]

    return start_cords, end_cords

def _calculate_delta(start_elevation, destination, elevation_map, elevation_order):
    dest_elev = elevation_map[destination[0]][destination[1]]

    return elevation_order.index(start_elevation) - elevation_order.index(dest_elev)

def _build_adjacency_matrix(elevation_map, elevation_order):
    n_rows = len(elevation_map)
    n_cols = len(elevation_map[0])

    adj = np.zeros((n_rows*n_cols, n_rows*n_cols))

    for i in range(n_rows):
        for j in range(n_cols):
            current_elevation = elevation_map[i][j]
            left_cords = right_cords = up_cords = down_cords = None

            if j != 0:
                # left
                left_cords = [i, j - 1]

            if j != (n_cols - 1):
                # right
                right_cords = [i, j + 1]

            if i != 0:
                # down
                up_cords = [i - 1, j]

            if i != (n_rows - 1):
                # up
                down_cords = [i + 1, j]

            to_check = [cords for cords in [left_cords, right_cords, down_cords, up_cords] if cords != None]
            for cords in to_check:
                delta = _calculate_delta(current_elevation, cords, elevation_map, elevation_order)
                if delta <= MAX_ELEVATION_DIFF:
                    row, col = cords
                    adj[(i*n_cols) + j][(row*n_cols) + col] = 1
                    #adj[(row*n_cols) + col][(i*n_cols) + j] = 1

    return adj


def _ddijkstra(adj, src):
    def _min_distance(dist, sptSet, n_verticies):
 
        # Initialize minimum distance for next node
        min = sys.maxsize
        min_index = -1
 
        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(n_verticies):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
 
        return min_index

    n_verticies = adj.shape[0]

    dist = [sys.maxsize] * n_verticies
    dist[src] = 0
    sptSet = [False] * n_verticies

    for cout in range(n_verticies):
        x = _min_distance(dist, sptSet, n_verticies)
        sptSet[x] = True

        for y in range(n_verticies):
            if adj[x][y] > 0 and sptSet[y] == False and \
                    dist[y] > dist[x] + adj[x][y]:
                dist[y] = dist[x] + adj[x][y]

    return dist

def calculate_all_distances_to_end(day_inp):
    global elevation_order

    elevation_map = _parse_input(day_inp)
    start_cords, end_cords = _find_start_and_end(elevation_map)
    elevation_map[end_cords[0]] = elevation_map[end_cords[0]].replace(END_MARKER, END_HEIGHT) # Replace end with height
    elevation_map[start_cords[0]] = elevation_map[start_cords[0]].replace(START_MARKER, START_HEIGHT) # Replace end with height
    adj = _build_adjacency_matrix(elevation_map, elevation_order)

    end_position_in_adj = end_cords[0] * len(elevation_map[0]) + end_cords[1]

    distances = _ddijkstra(adj, end_position_in_adj)

    return distances, elevation_map

def find_shorted_path(distances, elevation_map):
    start_cords, _ = _find_start_and_end(elevation_map)
    start_position_in_adj = start_cords[0] * len(elevation_map[0]) + start_cords[1]

    return int(distances[start_position_in_adj])

def find_shorted_path_for_a(distances, elevation_map):
    min_dist = sys.maxsize
    for i in range(len(elevation_map)):
        for j in range(len(elevation_map[0])):
            if elevation_map[i][j] == "a":
                indx = i * len(elevation_map[0]) + j

                if distances[indx] < min_dist:
                    min_dist = distances[indx]

    return int(min_dist)


test_input = "Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi"
expected = 31
test_dist = find_shorted_path(test_input)

assert test_dist == expected


with open('data/inputd12.txt') as f:
    content = f.read()

dist, elevation_map = calculate_all_distances_to_end(content)

dist = find_shorted_path(dist, elevation_map)
print(f"Task 1: Shortest dist {dist}")

dist = find_shorted_path_for_a(dist, elevation_map)
print(f"Task 2: Shortest dist {dist}")
