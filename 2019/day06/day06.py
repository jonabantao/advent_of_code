import collections


class Solution():
    def solve(self, filename):
        with open(filename) as f:
            test = [line.strip() for line in f]

            return self.part_a(test)

    def part_a(self, orbit_list):
        obj_orb = self.split_data(orbit_list)
        orbit_map = collections.defaultdict(list)
        orbit_trail = collections.defaultdict(set)
        orbit_count = collections.defaultdict(int)

        for obj, orbiter in obj_orb:
            orbit_map[orbiter].append(obj)

        for obj_orbiter in list(orbit_map.keys()):
            orbit_count[obj_orbiter] = self.count_orbits(
                obj_orbiter, orbit_map, orbit_count, orbit_trail, obj_orbiter)

        stuff = orbit_trail["SAN"].intersection(orbit_trail["YOU"])

        maxstuff = max([orbit_count[de] for de in list(stuff)])

        return (orbit_count["SAN"] - maxstuff) + (orbit_count["YOU"] - maxstuff) - 2

        # return sum(list(orbit_count.values()))

    def split_data(self, orbits):
        return [orbit.split(")") for orbit in orbits]

    def count_orbits(self, obj, orbit_map, orbit_records, trail, defobj):
        if obj in orbit_records:
            trail[defobj].update(trail[obj])
            return orbit_records[obj]

        orbiting = orbit_map[obj]
        trail[defobj].update(orbiting)

        if not orbiting:
            return 0

        # results = [self.count_orbits(
            # orbiting_obj, orbit_map, orbit_records) + 1 for orbiting_obj in orbiting]

        return sum([self.count_orbits(orbiting_obj, orbit_map, orbit_records, trail, defobj) + 1 for orbiting_obj in orbiting])


if __name__ == "__main__":
    solution = Solution()
    stuff = [
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
    print(solution.solve("input.txt"))
    # solution.solve("input.txt", 5)
    # print(solution.part_a(stuff))
