# Task 1
# Two compartments
# All items of a type in only one compartment
# Elf failed to follow rule above
# Input: list of all items in each rucksack. 
#   Letter (low or upper case) => item type (a and A are different types)
#   Items in one rucksack defined by one line (vJrwpWtwJgWrhcsFMMfFFhFp)
#       First half is the first compartment (vJrwpWtwJgWr). Second halve is the second (hcsFMMfFFhFp)
#   Rearranging with following priority a-z 1-26, A-Z 27-52
#       If an item is find in both compartment, => priority is as above. And the sum of priority will be the sum over all rucksacks

import string

all_letters = string.ascii_letters

def get_sum_priorities_for_items_in_both(day_input):
    priority_sum = 0
    for rucksack in day_input:
        items_in_rucksack = len(rucksack)
        first_compartment = rucksack[:int(items_in_rucksack/2)]
        second_compartment = rucksack[int(items_in_rucksack/2):]

        assert len(first_compartment) == len(second_compartment), f"First comp {len(first_compartment)}. Second comp {len(second_compartment)}"

        # Find shared items as the intersection of the two lists
        shared_items = list(set(first_compartment).intersection(second_compartment))

        for item in shared_items:
            priority_sum += all_letters.index(item) + 1

    return priority_sum

def get_sum_priority_of_badges(day_input):
    total_priority = 0
    for i in range(0, len(day_input), 3):
        elf1, elf2, elf3 = day_input[i:i+3]

        common_item = list(set(elf1).intersection(elf2).intersection(elf3))

        assert len(common_item) > 0, "Expected at least one common item in the group"
        assert len(common_item) == 1, "Expected only one one common item in the group"

        total_priority += all_letters.index(common_item[0]) + 1

    return total_priority
    
if __name__ == "__main__":
    #--- Tests
    test_input = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw".split("\n")
    task1_expected = 157
    task2_expected = 70

    task1_res = get_sum_priorities_for_items_in_both(test_input)
    task2_res = get_sum_priority_of_badges(test_input)
    assert task1_res == task1_expected
    assert task2_res == task2_expected

    #--- Tasks
    with open("data/inputd3.txt") as f:
        content = f.read().strip().split("\n")

    task1_res = get_sum_priorities_for_items_in_both(content)
    task2_res = get_sum_priority_of_badges(content)

    print(f"Task1: Total priority: {task1_res}")
    print(f"Task2: Total priority: {task2_res}")