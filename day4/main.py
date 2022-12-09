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

def split_elf_tasks(elf):
    return [int(elf_task) for elf_task in elf.split("-")]

def any_fully_contains(min_e1, max_e1, min_e2, max_e2):
    # Task 1
    min_dif = min_e1 - min_e2
    max_dif = max_e1 - max_e2

    e1_fully_contains = min_dif <= 0 and max_dif >= 0
    e2_fully_contains = min_dif >= 0 and max_dif <= 0

    return e1_fully_contains or e2_fully_contains

def any_overlap(min_e1, max_e1, min_e2, max_e2):
    # Task 2
    e1_min_in_e2 = min_e1 >= min_e2 and min_e1 <= max_e2
    e1_max_in_e2 = max_e1 >= min_e2 and max_e1 <= max_e2
    e2_min_in_e1 = min_e2 >= min_e1 and min_e2 <= max_e1
    e2_max_in_e1 = max_e2 >= min_e1 and max_e2 <= max_e1

    return e1_min_in_e2 or e1_max_in_e2 or e2_min_in_e1 or e2_max_in_e1

def task_1(file):
    with open(file) as f:
        content = f.read().strip().split("\n")

    n_total_overlaps = 0
    for pair in content:
        elf1, elf2 = pair.split(",")

        min_elf1, max_elf1 = split_elf_tasks(elf1)
        min_elf2, max_elf2 = split_elf_tasks(elf2)

        is_overlapping = any_fully_contains(min_elf1, max_elf1, min_elf2, max_elf2)

        n_total_overlaps += 1 if is_overlapping else 0

    print(f"Task1: N fully overlapping: {n_total_overlaps}")

def task_2(file):
    with open(file) as f:
        content = f.read().strip().split("\n")

    n_overlaps = 0
    for pair in content:
        elf1, elf2 = pair.split(",")

        min_elf1, max_elf1 = split_elf_tasks(elf1)
        min_elf2, max_elf2 = split_elf_tasks(elf2)

        is_overlapping = any_overlap(min_elf1, max_elf1, min_elf2, max_elf2)

        n_overlaps += 1 if is_overlapping else 0

    print(f"Task2: N overlapping: {n_overlaps}")

if __name__ == '__main__':
    e1_fully_overlap = (0,100,10,20)
    e2_fully_overlap = (10,20,0,200)
    e1_fully_overlap_low_equal = (0, 100, 0, 20)
    e1_fully_overlap_high_equal = (0, 100, 10, 100)
    part_overlap = (0,20,15,40)
    no_overlap = (0,20,50,80)
    e2_e1_fully_overlap = (0,20,0,20)

    assert any_fully_contains(*e1_fully_overlap) == True, "Expected e1 to fully overlap e2"
    assert any_fully_contains(*e2_fully_overlap) == True, "Expected e2 to fully overlap e1"
    assert any_fully_contains(*e2_e1_fully_overlap) == True, "Expected e2 to fully overlap e1"
    assert any_fully_contains(*e1_fully_overlap_low_equal) == True, "Expected e2 to fully overlap e1"
    assert any_fully_contains(*e1_fully_overlap_high_equal) == True, "Expected e2 to fully overlap e1"
    assert any_fully_contains(*part_overlap) == False, "Expected no full overlap"
    assert any_fully_contains(*no_overlap) == False, "Expected no full overlap"

    e1_overlap_e2 = (0,10,5,20)
    e1_overlap_e2_2 = (5,20,0,10)
    e1_fully_overlap = (0,100,10,20)
    e2_fully_overlap = (10,20,0,200)
    full_overlap = (0,10,0,10)
    no_overlap = (0,10,20,30)

    assert any_overlap(*e1_overlap_e2) == True, "Expected e1 to overlap e2"
    assert any_overlap(*e1_overlap_e2_2) == True, "Expected e1 to overlap e2"
    assert any_overlap(*full_overlap) == True, "Expected e1 to overlap e2"
    assert any_overlap(*e1_fully_overlap) == True, "Expected e1 to overlap e2"
    assert any_overlap(*e2_fully_overlap) == True, "Expected e1 to overlap e2"
    assert any_overlap(*no_overlap) == False, "Expected no overlap"

    task_1("data/inputd4.txt")
    task_2("data/inputd4.txt")