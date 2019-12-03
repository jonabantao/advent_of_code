import math


class Solution():
    def solve_part_a(self, filename):
        total = 0

        with open(filename, "r") as f:
            for line in f:
                mass = int(line.strip())

                total += self.calculate_fuel(mass)

        return total

    def solve_part_b(self, filename):
        total = 0

        with open(filename, "r") as f:
            for line in f:
                starting_fuel = int(line.strip())

                total += self.recursive_calculate_fuel(starting_fuel)

        return total

    def calculate_fuel(self, mass):
        return math.floor(mass / 3) - 2

    def recursive_calculate_fuel(self, fuel):
        if self.calculate_fuel(fuel) <= 0:
            return 0

        required_fuel = self.calculate_fuel(fuel)

        return required_fuel + self.recursive_calculate_fuel(required_fuel)


if __name__ == "__main__":
    solution = Solution()

    print("Part A:", solution.solve_part_a("input.txt"))
    print("Part B:", solution.solve_part_b("input.txt"))
