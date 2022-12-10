# Cathode-Ray Tube 
# screen and simple CPU that are both driven by a precise clock circuit. 
# The clock circuit ticks at a constant rate; each tick is called a cycle
# The CPU has a single register, X, which starts with the value 1. Two operations:
#   addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
#   noop takes one cycle to complete. It has no other effect.
#
#   signal strength: cycle number * X during the 20th cycle and every 40 cycles after that
# Task 1: Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?
#
# It seems like the X register controls the horizontal position of a sprite. Specifically, the sprite is 3 pixels wide, 
# and the X register sets the horizontal position of the middle of that sprite. (In this system, there is no such thing as "vertical position": 
# if the sprite's horizontal position puts its pixels where the CRT is currently drawing, then those pixels will be drawn.)
# This CRT screen draws the top row of pixels left-to-right, then the row below that
# CRT draws a single pixel during each cycle
# If the sprite is positioned such that one of its three pixels is the pixel currently being drawn, the screen produces a lit pixel (#); otherwise, the screen leaves the pixel dark (.).

import re
import numpy as np

# CPU
NOOP_CYCLES = 1
ADD_CYCLES = 2
FIRST_CYCLE_TO_CALCULATE = 20
CALCULATE_INTERVAL = 40
noop_pattern = re.compile("noop")
addx_pattern = re.compile("addx (.*)")

# CRT
SPRITE_WIDTH = 3
CRT_WIDTH = 40
CRT_HEIGHT = 6

def _generate_crt_screen(n_rows, n_cols, empty_char = "."):
    return np.full(n_rows * n_cols, empty_char)

def _parse_operation(operation):
    n_cycles_to_complete = 0
    to_add = 0
    if noop_pattern.search(operation):
        to_add = 0
        n_cycles_to_complete = NOOP_CYCLES
    elif addx_pattern.search(operation):
        to_add = int(addx_pattern.search(operation).group(1))
        n_cycles_to_complete = ADD_CYCLES
    else:
        raise Exception(f"Unknown operation {operation}")

    return n_cycles_to_complete, to_add

def sum_signal_strength(operations, first_cycle_to_calculate = FIRST_CYCLE_TO_CALCULATE, calculation_interval = CALCULATE_INTERVAL):
    operation_list = operations.strip().split("\n")

    X = 1
    current_cycle = 1
    sum_signal_strength = 0

    for operation in operation_list:
        n_cpu_cycles_to_complete, to_add = _parse_operation(operation)

        for i in range(n_cpu_cycles_to_complete):
            current_cycle += 1
            if i == (n_cpu_cycles_to_complete - 1):
                X += to_add

            if (current_cycle >= first_cycle_to_calculate) and ((current_cycle - first_cycle_to_calculate) % calculation_interval == 0):
                sum_signal_strength += X * current_cycle

    return sum_signal_strength

def generate_crt_drawing(operations):
    operation_list = operations.strip().split("\n")

    X = 1
    crt_screen = _generate_crt_screen(CRT_HEIGHT, CRT_WIDTH)
    sprite_position = np.array(range(SPRITE_WIDTH))
    crt_draw_position = 0
    current_cycle = 1

    for operation in operation_list:
        n_cpu_cycles_to_complete, to_add = _parse_operation(operation)

        for i in range(n_cpu_cycles_to_complete):
            curr_row_pixel = crt_draw_position % CRT_WIDTH
            if curr_row_pixel in sprite_position:
                crt_screen[crt_draw_position] = "#"
            
            if i == (n_cpu_cycles_to_complete - 1):
                X += to_add
                sprite_position = np.array(range(X-SPRITE_WIDTH,X)) + 2

            current_cycle += 1
            crt_draw_position += 1

    return crt_screen.reshape(CRT_HEIGHT, CRT_WIDTH) 

if __name__ == "__main__":
    with open("data/inputd10.txt") as f:
        inp = f.read()

    signal_strength = sum_signal_strength(inp)

    print(f"Task 1: Sum signal strength is {signal_strength}")

    screen = generate_crt_drawing(inp)  
    print("Task 2:")
    print('\n'.join([' '.join(row) for row in screen.tolist()]))
            