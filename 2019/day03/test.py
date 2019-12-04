import day03
import unittest


class TestDay03(unittest.TestCase):
    def setUp(self):
        self.solution = day03.Solution()

    def test_part_a_01(self):
        self.assertEqual(
            6,
            self.solution.find_closest_intersecting_manhattan_distance(
                ["R8", "U5", "L5", "D3"],
                ["U7", "R6", "D4", "L4"]
            )
        )

    def test_part_a_02(self):
        self.assertEqual(
            159,
            self.solution.find_closest_intersecting_manhattan_distance(
                ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
                ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
            )
        )

    def test_part_a_03(self):
        self.assertEqual(
            135,
            self.solution.find_closest_intersecting_manhattan_distance(
                ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"],
                ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
            )
        )

    def test_part_b_01(self):
        self.assertEqual(
            30,
            self.solution.find_smallest_signal(
                ["R8", "U5", "L5", "D3"],
                ["U7", "R6", "D4", "L4"]
            )
        )

    def test_part_b_02(self):
        self.assertEqual(
            610,
            self.solution.find_smallest_signal(
                ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
                ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
            )
        )

    def test_part_b_03(self):
        self.assertEqual(
            410,
            self.solution.find_smallest_signal(
                ["R98", "U47", "R26", "D63", "R33", "U87",
                    "L62", "D20", "R33", "U53", "R51"],
                ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
            )
        )
