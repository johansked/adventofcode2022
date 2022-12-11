import unittest
from importlib import import_module

day11 = import_module("AdventOfCode.2022.day11")

class TestDay11(unittest.TestCase):
    test_input = "Monkey 0:\n  Starting items: 79, 98\n  Operation: new = old * 19\n  Test: divisible by 23\n    If true: throw to monkey 2\n    If false: throw to monkey 3\n\nMonkey 1:\n  Starting items: 54, 65, 75, 74\n  Operation: new = old + 6\n  Test: divisible by 19\n    If true: throw to monkey 2\n    If false: throw to monkey 0\n\nMonkey 2:\n  Starting items: 79, 60, 97\n  Operation: new = old * old\n  Test: divisible by 13\n    If true: throw to monkey 1\n    If false: throw to monkey 3\n\nMonkey 3:\n  Starting items: 74\n  Operation: new = old + 3\n  Test: divisible by 17\n    If true: throw to monkey 0\n    If false: throw to monkey 1"

    def test_task_1(self):
        expected = 10605

        task1_test = day11.run_for_monkey_business(self.test_input, 1, day11.TASK_1_ROUNDS)

        self.assertEqual(task1_test, expected)

    def test_task_2(self):
        expected = 2713310158

        task2_test = day11.run_for_monkey_business(self.test_input, 2, day11.TASK_2_ROUNDS)

        self.assertEqual(task2_test, expected)