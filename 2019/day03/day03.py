import collections


class Solution():
    def solve_part_a(self, filename):
        with open(filename) as f:
            wire1 = f.readline().split(",")
            wire2 = f.readline().split(",")

            return self.find_closest_intersecting_manhattan_distance(wire1, wire2)

    def solve_part_b(self, filename):
        with open(filename) as f:
            wire1 = f.readline().split(",")
            wire2 = f.readline().split(",")

            return self.find_smallest_signal(wire1, wire2)

    def find_closest_intersecting_manhattan_distance(self, wire1, wire2):
        wire1_path = set()
        wire1_location = [0, 0]
        wire2_location = [0, 0]
        min_distance = float("inf")

        for path in self.traverse_wire(wire1, wire1_location):
            wire1_path.add(path)

        for path in self.traverse_wire(wire2, wire2_location):
            if path in wire1_path:
                min_distance = min(min_distance, sum(
                    [abs(num) for num in path]))

        return min_distance if min_distance != float("inf") else -1

    def find_smallest_signal(self, wire1, wire2):
        wire1_path_steps = collections.defaultdict(lambda: float("inf"))
        wire1_location = [0, 0]
        wire2_location = [0, 0]
        min_signal = float("inf")
        wire1_steps = 0
        wire2_steps = 0

        for path in self.traverse_wire(wire1, wire1_location):
            wire1_steps += 1
            wire1_path_steps[path] = min(wire1_path_steps[path], wire1_steps)

        for path in self.traverse_wire(wire2, wire2_location):
            wire2_steps += 1

            if path in wire1_path_steps:
                min_signal = min(
                    min_signal, wire1_path_steps[path] + wire2_steps)

        return min_signal if min_signal != float("inf") else -1

    def traverse_wire(self, wire, location):
        DIRECTION = {
            "R": (0, 1),
            "L": (0, -1),
            "U": (1, 0),
            "D": (-1, 0)
        }

        for path in wire:
            next_x, next_y, = DIRECTION[path[0]]
            steps = int(path[1:])

            for _ in range(steps):
                location[0] += next_x
                location[1] += next_y

                yield tuple(location)


if __name__ == "__main__":
    solution = Solution()

    print("Part A:", solution.solve_part_a("input.txt"))
    print("Part B:", solution.solve_part_b("input.txt"))
