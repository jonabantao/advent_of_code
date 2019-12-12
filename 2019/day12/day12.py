import re
import fractions
import functools


class Solution():
    def solve_a(self, filename, steps):
        with open(filename) as f:
            moons = [[int(re.sub(".=", "", coord))
                      for coord in line.rstrip()[1:-1].split(", ")] for line in f]
            velocity = [[0, 0, 0] for _ in range(len(moons))]

            for _ in range(steps):
                self.calculate_velocity(moons, velocity)
                self.update_position(moons, velocity)

            return self.calculate_total_energy(moons, velocity)

    def solve_b(self, filename):
        with open(filename) as f:
            moons = [[int(re.sub(".=", "", coord))
                      for coord in line.rstrip()[1:-1].split(", ")] for line in f]
            velocity = [[0, 0, 0] for _ in range(len(moons))]

            """https://i.imgur.com/t85FtZi.jpg"""
            # original = [tuple(coord) for coord in moons]
            #step = 1

            #     self.calculate_velocity(moons, velocity)
            #     self.update_position(moons, velocity)
            #     step += 1

            #     new_coord = set([tuple(coord) for coord in moons])

            #     if len(original & new_coord) == len(original):
            #         return step

            coord_vel_group = [set(), set(), set()]
            time_to_match = [float("inf"), float("inf"), float("inf")]

            step = 0

            while any([num == float("inf") for num in time_to_match]):
                for coord in range(3):
                    coord_vel = []

                    for idx, moon in enumerate(moons):
                        coord_vel.extend([moon[coord], velocity[idx][coord]])

                    coord_vel_tuple = tuple(coord_vel)

                    if coord_vel_tuple in coord_vel_group[coord]:
                        time_to_match[coord] = min(step, time_to_match[coord])

                    coord_vel_group[coord].add(coord_vel_tuple)

                self.calculate_velocity(moons, velocity)
                self.update_position(moons, velocity)

                step += 1

            return int(self.lcm(time_to_match))

    def calculate_velocity(self, moons, velocity):
        for idx, moon in enumerate(moons):
            for other_idx, other_moon in enumerate(moons):
                if idx == other_idx:
                    continue

                for coord in range(3):
                    if moon[coord] < other_moon[coord]:
                        velocity[idx][coord] += 1
                    elif moon[coord] > other_moon[coord]:
                        velocity[idx][coord] -= 1

    def update_position(self, moons, velocity):
        for idx, moon in enumerate(moons):
            for coord in range(3):
                moon[coord] += velocity[idx][coord]

    def calculate_total_energy(self, moons, velocity):
        total = 0

        for idx, moon in enumerate(moons):
            moon_pot_energy = sum([abs(coord) for coord in moon])
            moon_kin_energy = sum([abs(coord) for coord in velocity[idx]])

            total += moon_pot_energy * moon_kin_energy

        return total

    def lcm(self, numbers):
        # https://rik0-techtemple.blogspot.com/2010/09/nice-functional-lcm-in-python.html
        # Because my math is womp womp.
        return functools.reduce(lambda x, y: (x*y)/fractions.gcd(x, y), numbers, 1)


if __name__ == "__main__":
    solution = Solution()

    print("Part A:", solution.solve_a("input.txt", 1000))
    print("Part B:", solution.solve_b("input.txt"))
