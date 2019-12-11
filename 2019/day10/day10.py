import math
import collections

# https://en.wikipedia.org/wiki/Atan2


class Solution():
    def solve_a(self, filename):
        with open(filename) as f:
            asteroid_map = [list(line) for line in f]

            return self.find_ideal_location_visible_count(asteroid_map)[0]

    def solve_b(self, filename):
        with open(filename) as f:
            asteroid_map = [list(line) for line in f]

            ideal_x, ideal_y = self.find_ideal_location_visible_count(asteroid_map)[
                1]

            asteroid200 = self.vaporize_in_order(
                ideal_x, ideal_y, asteroid_map)[199]

            return asteroid200[0] * 100 + asteroid200[1]

    def find_ideal_location_visible_count(self, grid):
        count = 0
        location = None

        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == "#":
                    visible_count = self.count_visible(x, y, grid)

                    if visible_count > count:
                        count = visible_count
                        location = (x, y)

        return (count, location)

    def count_visible(self, x1, y1, grid):
        angles = set()

        for y2, row in enumerate(grid):
            for x2, cell in enumerate(row):
                if x2 == x1 and y2 == y1:
                    continue

                if cell == "#":
                    angles.add(math.atan2(y2 - y1, x2 - x1))

        return len(angles)

    def vaporize_in_order(self, x, y, grid):
        atan2_to_location = self.map_asteroids_from_origin(x, y, grid)

        closest_asteroids_rotation = [sorted(list(asteroids), key=lambda x: x[0], reverse=True)
                                      for degrees, asteroids in
                                      sorted(atan2_to_location.items(), key=lambda x: x[0], reverse=True)]

        vaporized_asteroids_order = []

        while any(asteroids for asteroids in closest_asteroids_rotation):
            for asteroid_list in closest_asteroids_rotation:
                if not asteroid_list:
                    continue

                _, location = asteroid_list.pop()

                vaporized_asteroids_order.append(location)

        return vaporized_asteroids_order

    def map_asteroids_from_origin(self, x1, y1, grid):
        """
        If you swap the y-x arguments around to atan2(x,y) and then order the result by descending, you start at the right position.
        :thinking-face:
        """
        atan2_to_location = collections.defaultdict(set)

        for y2, row in enumerate(grid):
            for x2, cell in enumerate(row):
                if x2 == x1 and y2 == y1:
                    continue

                if cell == "#":
                    angle = math.atan2(x2 - x1, y2 - y1)
                    distance_to_origin = self.calculate_distance(
                        x1, y1, x2, y2)

                    atan2_to_location[angle].add(
                        (distance_to_origin, (x2, y2)))

        return atan2_to_location

    def calculate_distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


if __name__ == "__main__":
    solution = Solution()

    print("Part A:", solution.solve_a("input.txt"))
    print("Part B:", solution.solve_b("input.txt"))
