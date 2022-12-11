# Monkey in the Middle
# To get your stuff back, you need to be able to predict where the monkeys will throw your items.
# monkeys operate based on how worried you are about each item
# After each monkey inspects an item but before it tests your worry level, 
# worry level to be divided by three and rounded down to the nearest integer
# Monkey turn:
#   Inspects and throws all of its items on at the time and in listed order
#   When a monkey throws an item to another monkey, the item goes on the end of the recipient monkey's list
#   If a monkey is holding no items at the start of its turn, its turn ends
#   Item value = worry level

import re
import numpy as np
from copy import deepcopy

AFTER_INSPECTION_DENOMINATOR = 3
TASK_1_ROUNDS = 20
TASK_2_ROUNDS = 10000

monkey_pattern = re.compile("Monkey\s(\d+):")
starting_item_pattern = re.compile("\s+Starting\sitems:\s(.+)")
operation_pattern = re.compile("\s+Operation\:.+([+,-,/,*])\s(\w+|\d+)")
test_pattern = re.compile("\s+Test:\sdivisible\sby\s(\d+)")
statement_pattern = re.compile("\s+If\s(true|false).+(\d+)")

def _parse_input(inp):
    def _create_monkey(indx):
        return {
            "monkey": indx,
            "items": [],
            "operation": [],
            "test": {},
            "nInspectedItems": 0
        }
    monkeys = []
    for line in inp.strip().split("\n"):
        monkey_res = monkey_pattern.search(line)
        if monkey_res:
            monkey_index = int(monkey_res.group(1))
            monkeys.append(_create_monkey(monkey_index))
            continue
        
        starting_item_res = starting_item_pattern.search(line)
        if starting_item_res:
            starting_items = starting_item_res.group(1).split(",")
            starting_items = [int(indx.strip()) for indx in starting_items]
            monkeys[-1]["items"] = starting_items
            continue

        operation_res = operation_pattern.search(line)
        if operation_res:
            operator = operation_res.group(1)
            try:
                value = int(operation_res.group(2))
            except ValueError:
                value = operation_res.group(2)
            monkeys[-1]["operation"] = [operator, value]
            continue

        test_res = test_pattern.search(line)
        if test_res:
            value = int(test_res.group(1))
            monkeys[-1]["test"]["value"] = value
            continue

        statement_res = statement_pattern.search(line)
        if statement_res:
            test = bool(statement_res.group(1))
            value = int(statement_res.group(2))
            monkeys[-1]["test"][statement_res.group(1)] = value
            continue

    return monkeys

def _round(monkeys, decrease_worry_by = None, modulus = None):
    for (i, monkey) in enumerate(monkeys):
        while len(monkey["items"]) > 0:
            # Next item
            current_item = monkey["items"].pop(0)
            
            # Check worry level
            operation, value = monkey["operation"]

            if value == "old":
                value = int(current_item)

            if operation == "+":
                current_item += value
            elif operation == "-":
                current_item -= value
            elif operation == "/":
                current_item /= value
            elif operation == "*":
                current_item *= value

            # Worry decreases
            if decrease_worry_by is not None:
                current_item = current_item // decrease_worry_by
            if modulus is not None:
                current_item %= modulus

            # Check where to throw
            if current_item % monkey["test"]["value"] == 0:
                recipient_indx = monkey["test"]["true"]
            else:
                recipient_indx = monkey["test"]["false"]
            

            monkeys[recipient_indx]["items"].append(current_item)
            monkey["nInspectedItems"] += 1



def _calculate_monkey_business(monkeys, top = 2):
    inspected_items = sorted([m["nInspectedItems"] for m in monkeys], reverse=True)

    monkey_business = inspected_items[0]
    for i in range(top - 1):
        monkey_business *= inspected_items[i+1]
    return monkey_business

def run_for_monkey_business(day_input, task, rounds):
    monkeys = _parse_input(day_input)

    decrease_worry_by = None
    modulus = None

    if task == 1:
        decrease_worry_by = AFTER_INSPECTION_DENOMINATOR
    else:
        modulus = int(np.prod([m["test"]["value"] for m in monkeys]))

    for j in range(rounds):
        _round(monkeys, decrease_worry_by=decrease_worry_by, modulus=modulus)

    return _calculate_monkey_business(monkeys)


if __name__ == "__main__":
    with open("data/inputd11.txt") as f:
        inp = f.read()

    task1_mb = run_for_monkey_business(inp, 1, TASK_1_ROUNDS)
    task2_mb = run_for_monkey_business(inp, 2, TASK_2_ROUNDS)

    print(f"Task 1: Level of monkey business {task1_mb}")
    print(f"Task 2: Level of monkey business {task2_mb}")

