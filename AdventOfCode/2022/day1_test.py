import unittest
from importlib import import_module

day1 = import_module("AdventOfCode.2022.day1")

class TestDay1(unittest.TestCase):
    test_input = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000\n".split("\n")

    def test_task_1(self):
        expected = 24000
        top = 1

        result = day1.get_sum_max_calories(self.test_input, top)
        self.assertEqual(result, expected, f"Expected max calories to be {expected}, got {result}")

    def test_task_2(self):
        expected = 45000
        top = 3

        result = day1.get_sum_max_calories(self.test_input, top)
        self.assertEqual(result, expected, f"Expected max calories to be {expected}, got {result}")
    