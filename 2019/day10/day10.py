import math

# https://en.wikipedia.org/wiki/Atan2


class Solution():
    def solve_a(self, filename):
        with open(filename) as f:
            asteroid_map = [list(line) for line in f]

            print(self.find_ideal_location_visible_count(asteroid_map))

    def find_ideal_location_visible_count(self, grid):
        count = 0

        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == "#":
                    count = max(count, self.count_visible(x, y, grid))

        return count

    def count_visible(self, x1, y1, grid):
        angles = set()

        for y2, row in enumerate(grid):
            for x2, cell in enumerate(row):
                if x2 == x1 and y2 == y1:
                    continue

                if cell == "#":
                    angles.add(math.atan2(y2 - y1, x2 - x1))

        return len(angles)


if __name__ == "__main__":
    solution = Solution()

    solution.solve_a("input.txt")
