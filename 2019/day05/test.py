import day05
import unittest


class TestDay05(unittest.TestCase):
    def setUp(self):
        self.solution = day05.Solution()

    def test_intcode_computer_01(self):
        self.assertListEqual([1002, 4, 3, 4, 99], self.solution.part_a_tester(
            [1002, 4, 3, 4, 33], 1))

    def test_intcode_computer_02(self):
        self.assertListEqual([1101, 100, -1, 4, 99], self.solution.part_a_tester(
            [1101, 100, -1, 4, 0], 1))

    def test_intcode_computer_modify_ptr_01(self):
        self.assertEqual(1, self.solution.run_intcode_computer(
            [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 8))

    def test_intcode_computer_modify_ptr_02(self):
        self.assertEqual(0, self.solution.run_intcode_computer(
            [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 438))

    def test_intcode_computer_modify_ptr_03(self):
        self.assertEqual(0, self.solution.run_intcode_computer(
            [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 8))

    def test_intcode_computer_modify_ptr_04(self):
        self.assertEqual(1, self.solution.run_intcode_computer(
            [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], -3218))

    def test_intcode_computer_modify_ptr_05(self):
        self.assertEqual(1, self.solution.run_intcode_computer(
            [3, 3, 1108, -1, 8, 3, 4, 3, 99], 8))

    def test_intcode_computer_modify_ptr_06(self):
        self.assertEqual(0, self.solution.run_intcode_computer(
            [3, 3, 1108, -1, 8, 3, 4, 3, 99], 18))

    def test_intcode_computer_modify_ptr_07(self):
        self.assertEqual(1, self.solution.run_intcode_computer(
            [3, 3, 1107, -1, 8, 3, 4, 3, 99], 3))

    def test_intcode_computer_modify_ptr_08(self):
        self.assertEqual(0, self.solution.run_intcode_computer(
            [3, 3, 1107, -1, 8, 3, 4, 3, 99], 3212))

    def test_intcode_computer_jump_01(self):
        self.assertEqual(0, self.solution.run_intcode_computer(
            [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], 0))

    def test_intcode_computer_jump_02(self):
        self.assertEqual(1, self.solution.run_intcode_computer(
            [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], 3212))

    def test_intcode_computer_jump_03(self):
        self.assertEqual(0, self.solution.run_intcode_computer(
            [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 0))

    def test_intcode_computer_jump_04(self):
        self.assertEqual(1, self.solution.run_intcode_computer(
            [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 32512))

    def test_intcode_computer_long_01(self):
        self.assertEqual(999, self.solution.run_intcode_computer(
            [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
             1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
             999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], -32))

    def test_intcode_computer_long_02(self):
        self.assertEqual(1000, self.solution.run_intcode_computer(
            [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
             1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
             999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 8))

    def test_intcode_computer_long_03(self):
        self.assertEqual(1001, self.solution.run_intcode_computer(
            [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
             1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
             999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 84))
