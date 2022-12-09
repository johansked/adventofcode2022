# Section as a unique ID
# Each elf assigned a range of ids
# Many assignment overlap
# Pair up and make list of section assignment for each pair
#   2-4,6-8
#   2-3,4-5
#   5-7,7-9
#   2-8,3-7
#   6-6,4-6
#   2-6,4-8
# First pair of elves, first elf assigned sec 2-4, second elf 6-8
#
# Some pairs, one assigment fully contains the other. I.e. 2-8,3-7 => one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning
# Task1: Find how many pairs where one range fully contains the other
# Task2: Find how many paris where any overlap between ranges

def _split_elf_tasks(elf):
    return [int(elf_task) for elf_task in elf.split("-")]

def _any_fully_contains(min_e1, max_e1, min_e2, max_e2):
    # Task 1
    min_dif = min_e1 - min_e2
    max_dif = max_e1 - max_e2

    e1_fully_contains = min_dif <= 0 and max_dif >= 0
    e2_fully_contains = min_dif >= 0 and max_dif <= 0

    return e1_fully_contains or e2_fully_contains

def _any_overlap(min_e1, max_e1, min_e2, max_e2):
    # Task 2
    e1_min_in_e2 = min_e1 >= min_e2 and min_e1 <= max_e2
    e1_max_in_e2 = max_e1 >= min_e2 and max_e1 <= max_e2
    e2_min_in_e1 = min_e2 >= min_e1 and min_e2 <= max_e1
    e2_max_in_e1 = max_e2 >= min_e1 and max_e2 <= max_e1

    return e1_min_in_e2 or e1_max_in_e2 or e2_min_in_e1 or e2_max_in_e1

def count_full_overlap(day_input):
    n_total_overlaps = 0
    for pair in day_input:
        elf1, elf2 = pair.split(",")

        min_elf1, max_elf1 = _split_elf_tasks(elf1)
        min_elf2, max_elf2 = _split_elf_tasks(elf2)

        is_overlapping = _any_fully_contains(min_elf1, max_elf1, min_elf2, max_elf2)

        n_total_overlaps += 1 if is_overlapping else 0

    return n_total_overlaps

def count_any_overlap(day_input):
    n_overlaps = 0
    for pair in day_input:
        elf1, elf2 = pair.split(",")

        min_elf1, max_elf1 = _split_elf_tasks(elf1)
        min_elf2, max_elf2 = _split_elf_tasks(elf2)

        is_overlapping = _any_overlap(min_elf1, max_elf1, min_elf2, max_elf2)

        n_overlaps += 1 if is_overlapping else 0

    return n_overlaps

if __name__ == '__main__':
    with open("data/inputd4.txt") as f:
        content = f.read().strip().split("\n")

    n_total_overlaps = count_full_overlap(content)
    n_overlaps = count_any_overlap(content)

    print(f"Task1: N fully overlapping: {n_total_overlaps}")
    print(f"Task2: N overlapping: {n_overlaps}")