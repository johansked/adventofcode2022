import unittest
from importlib import import_module

day4 = import_module("AdventOfCode.2022.day4")

class TestDay3(unittest.TestCase):
    def test_full_overlap(self):
        e1_fully_overlap = (0,100,10,20)
        e2_fully_overlap = (10,20,0,200)
        e1_fully_overlap_low_equal = (0, 100, 0, 20)
        e1_fully_overlap_high_equal = (0, 100, 10, 100)
        part_overlap = (0,20,15,40)
        no_overlap = (0,20,50,80)
        e2_e1_fully_overlap = (0,20,0,20)

        self.assertTrue(day4._any_fully_contains(*e1_fully_overlap), "Expected e1 to fully overlap e2")
        self.assertTrue(day4._any_fully_contains(*e2_fully_overlap), "Expected e2 to fully overlap e1")
        self.assertTrue(day4._any_fully_contains(*e2_e1_fully_overlap), "Expected e2 to fully overlap e1")
        self.assertTrue(day4._any_fully_contains(*e1_fully_overlap_low_equal), "Expected e2 to fully overlap e1")
        self.assertTrue(day4._any_fully_contains(*e1_fully_overlap_high_equal), "Expected e2 to fully overlap e1")
        self.assertFalse(day4._any_fully_contains(*part_overlap), "Expected no full overlap")
        self.assertFalse(day4._any_fully_contains(*no_overlap), "Expected no full overlap")

    def test_any_overlap(self):
        e1_overlap_e2 = (0,10,5,20)
        e1_overlap_e2_2 = (5,20,0,10)
        e1_fully_overlap = (0,100,10,20)
        e2_fully_overlap = (10,20,0,200)
        full_overlap = (0,10,0,10)
        no_overlap = (0,10,20,30)

        self.assertTrue(day4._any_overlap(*e1_overlap_e2), "Expected e1 to overlap e2")
        self.assertTrue(day4._any_overlap(*e1_overlap_e2_2), "Expected e1 to overlap e2")
        self.assertTrue(day4._any_overlap(*full_overlap), "Expected e1 to overlap e2")
        self.assertTrue(day4._any_overlap(*e1_fully_overlap), "Expected e1 to overlap e2")
        self.assertTrue(day4._any_overlap(*e2_fully_overlap), "Expected e1 to overlap e2")
        self.assertFalse(day4._any_overlap(*no_overlap), "Expected no overlap")