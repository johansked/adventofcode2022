# Stacks of marked creates
# Giant cargo crane moving creates between stacks
# Drawing of starting stacks of create and the rearrangement process
# Example
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
#
# Three stacks of creates
# In each step a quantity of creates are moved I.e. 3 creates are moved from 1 to 3 in step 2
# Task1: Which create will end up on top of each pile?
# Task2: and the ability to pick up and move multiple crates at once. i.e. order is kept when moving
import re

step_pattern = re.compile("move (\d+) from (\d+) to (\d+)")

def parser(content):
    creates_info = []
    steps_info = []
    first_block = True

    for line in content:
        if first_block:
            if line == "":
                first_block = False
                continue

            creates_info.append(line)
        else:
            res = step_pattern.search(line)
            if res:
                number_of_creates, from_pile, to_pile = res.group(1,2,3)
                steps_info.append([int(number_of_creates), int(from_pile), int(to_pile)])

    # Format piles
    creates_info.reverse()
    pile_ids = re.findall("\d+", creates_info[0]) 
    pile_ids = [int(idx) for idx in pile_ids]

    n_piles = len(pile_ids)
    piles = [[] for i in range(n_piles)]

    for pile_line in creates_info[1:]:
        for i in range(n_piles):
            # Assume [N] [A] 
            if i == 0:
                indx = 0
            else:
                indx += 4
            
            pile_info = pile_line[indx+1]

            if pile_info != " ":
                piles[i].append(pile_info)

    return piles, steps_info

def do_movement(pile_info, steps_info, keep_order_when_moved):
    for step in steps_info:
        n_creates, from_pile, to_pile = step

        n_poped = 0
        to_move = []
        while n_poped < n_creates:
            to_move.append(pile_info[from_pile - 1].pop())
            n_poped += 1

        if keep_order_when_moved:
            to_move.reverse()

        pile_info[to_pile - 1] += to_move

    return pile_info

def run(path, keep_order_when_moved, task_id):
    with open(path) as f:
        content = f.read().strip().split("\n")

    pile_info, steps_info = parser(content)

    pile_info = do_movement(pile_info, steps_info, keep_order_when_moved)

    print(f"{task_id}: The current top creates are {''.join([p[-1] for p in pile_info])}")


if __name__ == '__main__':
    run("data/inputd5.txt", False, "Task1")
    run("data/inputd5.txt", True, "Task2")
