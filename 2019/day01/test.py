import day01
import unittest


class TestDay01(unittest.TestCase):
    def setUp(self):
        self.solution = day01.Solution()

    def test_calculate_fuel_01(self):
        self.assertEqual(2, self.solution.calculate_fuel(14))

    def test_calculate_fuel_02(self):
        self.assertEqual(2, self.solution.calculate_fuel(14))

    def test_calculate_fuel_03(self):
        self.assertEqual(654, self.solution.calculate_fuel(1969))

    def test_calculate_fuel_04(self):
        self.assertEqual(33583, self.solution.calculate_fuel(100756))

    def test_rec_calc_fuel_01(self):
        self.assertEqual(2, self.solution.recursive_calculate_fuel(14))

    def test_rec_calc_fuel_02(self):
        self.assertEqual(966, self.solution.recursive_calculate_fuel(1969))

    def test_rec_calc_fuel_03(self):
        self.assertEqual(50346, self.solution.recursive_calculate_fuel(100756))
