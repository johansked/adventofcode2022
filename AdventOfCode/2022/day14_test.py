import unittest
from importlib import import_module

day14 = import_module("AdventOfCode.2022.day14")

class TestDay14(unittest.TestCase):
    test_input = "498,4 -> 498,6 -> 496,6\n503,4 -> 502,4 -> 502,9 -> 494,9"

    def test_task_1(self):
        expected = 24

        n_units, grid = day14.count_units_at_rest(self.test_input, False)

        self.assertEqual(n_units, expected, f"Expected n units to be {expected}, got {n_units}")

    def test_task_2(self):
        expected = 93

        n_units, grid = day14.count_units_at_rest(self.test_input, True)

        self.assertEqual(n_units, expected, f"Expected n units to be {expected}, got {n_units}")

    def print(self, grid):
        print('\n'.join([' '.join(row) for row in grid.tolist()]))