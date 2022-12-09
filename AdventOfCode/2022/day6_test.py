import unittest
from importlib import import_module

day6 = import_module("AdventOfCode.2022.day6")

class TestDay6(unittest.TestCase):
    def test_sequences(self):
        tests = [
            {"input": "bvwbjplbgvbhsrlpgdmjqwftvncz", "expected": 5, "seqSize": 4},
            {"input": "nppdvjthqldpwncqszvftbrmjlhg", "expected": 6, "seqSize": 4},
            {"input": "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "expected": 10, "seqSize": 4},
            {"input": "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", "expected": 11, "seqSize": 4},
            {"input": "mjqjpqmgbljsphdztnvjfqwrcgsmlb", "expected": 19, "seqSize": 14},
            {"input": "bvwbjplbgvbhsrlpgdmjqwftvncz", "expected": 23, "seqSize": 14},
            {"input": "nppdvjthqldpwncqszvftbrmjlhg", "expected": 23, "seqSize": 14},
            {"input": "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "expected": 29, "seqSize": 14},
            {"input": "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", "expected": 26, "seqSize": 14},
        ]
        for test in tests:
            start_position = day6.check_buffer_for_start(test["input"], test["seqSize"])
            self.assertEqual(
                start_position, 
                test["expected"], 
                f"Expected seq start to be {test['expected']}, got {start_position}")