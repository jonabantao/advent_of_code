import day04
import unittest


class TestDay04(unittest.TestCase):
    def setUp(self):
        self.solution = day04.Solution()

    def test_part_a_01(self):
        self.assertTrue(self.solution.part_a("111111"))

    def test_part_a_02(self):
        self.assertFalse(self.solution.part_a("223450"))

    def test_part_a_03(self):
        self.assertFalse(self.solution.part_a("123789"))

    def test_part_b_01(self):
        self.assertTrue(self.solution.part_b("112233"))

    def test_part_b_02(self):
        self.assertFalse(self.solution.part_b("123444"))

    def test_part_b_03(self):
        self.assertFalse(self.solution.part_b("124444"))

    def test_part_b_04(self):
        self.assertTrue(self.solution.part_b("111122"))
