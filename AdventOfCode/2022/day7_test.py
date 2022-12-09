import unittest
from importlib import import_module

day7 = import_module("AdventOfCode.2022.day7")

class TestDay7(unittest.TestCase):
    test_input = "$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k"
    test_expected_task_1 = 95437
    test_expected_task_2 = 24933642

    def setUp(self) -> None:
        _, self.directory = day7._parse_directory(0, self.test_input.strip().split("\n"))

    def test_task_1(self):
        task1_res = day7._task1(self.directory, day7.SIZE_TH, 0)

        self.assertEqual(
            task1_res, 
            self.test_expected_task_1, 
            f"Expected task 1 to return size {self.test_expected_task_1}, got {task1_res}")

    def test_task_2(self):
        task2_required_additional = day7._calculate_required_additional_size(self.directory)
        task2_res = day7._task2(self.directory, task2_required_additional, self.directory["size"])

        self.assertEqual(
            task2_res, 
            self.test_expected_task_2, 
            f"Expected task 2 to return size {self.test_expected_task_2}, got {task2_res}")

    def test_run(self):
        task1_res, task2_res = day7.run(self.test_input.strip().split("\n"))

        self.assertEqual(
            task1_res, 
            self.test_expected_task_1, 
            f"Expected task 1 from run to return size {self.test_expected_task_1}, got {task1_res}")

        self.assertEqual(
            task2_res, 
            self.test_expected_task_2, 
            f"Expected task 2 from run to return size {self.test_expected_task_2}, got {task2_res}")
