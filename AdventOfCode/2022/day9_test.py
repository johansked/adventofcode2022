import unittest
from importlib import import_module

day9 = import_module("AdventOfCode.2022.day9")

class TestDay9(unittest.TestCase):
    def test_task_1(self):
        tests = [
            {
                "input": day9._parse_input("R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2"),
                "expected": 13,
                "n_knots": 2
            }
        ]

        for test in tests:
            n_visited_points = day9.find_unique_visited_points(test["input"], test["n_knots"])
            self.assertEqual(
                n_visited_points, 
                test["expected"], 
                f"Expected test input to have visited {test['expected']}, found {n_visited_points}")

    def test_task_2(self):
        tests = [
            {
                "input": day9._parse_input("R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2"),
                "expected": 1,
                "n_knots": 10
            },
            {
                "input": day9._parse_input("R 5\nU 8\nL 8\nD 3\nR 17\nD 10\nL 25\nU 20"),
                "expected": 36,
                "n_knots": 10
            }
        ]

        for test in tests:
            n_visited_points = day9.find_unique_visited_points(test["input"], test["n_knots"])
            self.assertEqual(
                n_visited_points, 
                test["expected"], 
                f"Expected test input to have visited {test['expected']}, found {n_visited_points}")