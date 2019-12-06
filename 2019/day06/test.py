import day06
import unittest


class TestDay06(unittest.TestCase):
    def setUp(self):
        self.solution = day06.Solution()

    def test_part_a(self):
        test_case = [
            "COM)B",
            "B)C",
            "C)D",
            "D)E",
            "E)F",
            "B)G",
            "G)H",
            "D)I",
            "E)J",
            "J)K",
            "K)L",
        ]
        self.assertEqual(42, self.solution.find_total_direct_and_indirect_orbits(test_case))

    def test_part_b(self):
        test_case = [
            "COM)B",
            "B)C",
            "C)D",
            "D)E",
            "E)F",
            "B)G",
            "G)H",
            "D)I",
            "E)J",
            "J)K",
            "K)L",
            "K)YOU",
            "I)SAN",
        ]
        self.assertEqual(4, self.solution.find_min_orbital_transfer_between_me_and_santa(test_case))
