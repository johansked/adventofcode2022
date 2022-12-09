import unittest
from importlib import import_module

day3 = import_module("AdventOfCode.2022.day3")

class TestDay3(unittest.TestCase):
    test_input = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw".split("\n")
    
    def test_task_1(self):
        expected = 157

        task1_res = day3.get_sum_priorities_for_items_in_both(self.test_input)

        self.assertEqual(task1_res, expected)

    def test_task_2(self):
        expected = 70

        task2_res = day3.get_sum_priority_of_badges(self.test_input)

        self.assertEqual(task2_res, expected)