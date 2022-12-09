import unittest
from importlib import import_module

day8 = import_module("AdventOfCode.2022.day8")

class TestDay8(unittest.TestCase):
    test_content = [list(i) for i in "30373\n25512\n65332\n33549\n35390".split("\n")]

    def test_task_1(self):
        expected = 21

        n_visible = day8.count_non_visible_trees(self.test_content)
        self.assertEqual(n_visible, expected, f"Expected task1 test output to be {expected}")

    def test_task_2(self):
        expected = 8

        max_scenic = day8.max_scenic_score(self.test_content)
        self.assertEqual(max_scenic, expected, "Expected task2 test output to be {expected}")