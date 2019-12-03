import day02
import unittest


class TestDay02(unittest.TestCase):
    def setUp(self):
        self.solution = day02.Solution()

    def test_part_a_01(self):
        self.assertListEqual(
            [2, 0, 0, 0, 99], self.solution.part_a([1, 0, 0, 0, 99]))

    def test_part_a_02(self):
        self.assertListEqual([2, 3, 0, 6, 99],
                             self.solution.part_a([2, 3, 0, 3, 99]))

    def test_part_a_03(self):
        self.assertListEqual([2, 4, 4, 5, 99, 9801],
                             self.solution.part_a([2, 4, 4, 5, 99, 0]))

    def test_part_a_04(self):
        self.assertListEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], self.solution.part_a(
            [1, 1, 1, 4, 99, 5, 6, 0, 99]))
