import collections


class Solution():
    def solve_part_a(self, filename):
        with open(filename) as f:
            input_data = [line.strip() for line in f]

            return self.find_total_direct_and_indirect_orbits(input_data)

    def solve_part_b(self, filename):
        with open(filename) as f:
            input_data = [line.strip() for line in f]

            return self.find_min_orbital_transfer_between_me_and_santa(input_data)

    def find_total_direct_and_indirect_orbits(self, orbit_list):
        orbit_trail = self.setup_data(orbit_list)

        return sum([len(trail) for trail in orbit_trail.values()])

    def find_min_orbital_transfer_between_me_and_santa(self, orbit_list):
        orbit_trail = self.setup_data(orbit_list)

        common_objs = orbit_trail["SAN"].intersection(orbit_trail["YOU"])
        closest_obj_orbit_count = max([len(orbit_trail[obj]) for obj in common_objs])

        santa_orbit_count_to_closest_obj = len(orbit_trail["SAN"]) - closest_obj_orbit_count
        my_orbit_count_to_closest_obj = len(orbit_trail["YOU"]) - closest_obj_orbit_count

        # -2 to remove self and santa orbits
        return santa_orbit_count_to_closest_obj + my_orbit_count_to_closest_obj - 2

    def setup_data(self, orbit_list):
        orbit_data = self.split_data(orbit_list)
        orbit_map = {orbiting: orbited for orbited, orbiting in orbit_data}
        orbit_trail = collections.defaultdict(set)

        for orbit_check in list(orbit_map.keys()):
            self.record_orbit_trail(orbit_check, orbit_trail, orbit_map, orbit_check)

        return orbit_trail

    def split_data(self, orbits):
        return [orbit.split(")") for orbit in orbits]

    def record_orbit_trail(self, obj, orbit_trail, orbit_map, start_obj):
        if obj in orbit_trail:
            orbit_trail[start_obj].update(orbit_trail[obj])
            return

        if obj not in orbit_map:
            return

        next_obj = orbit_map[obj]
        orbit_trail[start_obj].add(next_obj)

        self.record_orbit_trail(next_obj, orbit_trail, orbit_map, start_obj)


if __name__ == "__main__":
    solution = Solution()

    print("Part A:", solution.solve_part_a("input.txt"))
    print("Part B:", solution.solve_part_b("input.txt"))
