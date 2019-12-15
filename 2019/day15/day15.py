import collections


NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

WALL = 0
MOVED = 1
OXYGEN = 2


class Solution():
    def __init__(self):
        self.grid = {
            (0, 0): 1,
        }
        self.min_steps = None
        self.oxygen_system = None

    def solve_a(self, filename):
        with open(filename, "r") as f:
            input_list = [int(num) for num in f.readline().split(",")]
            input_list.extend([0] * 10000)

            self.build_grid_and_find_oxygen_system(input_list, (0, 0))

            return self.min_steps
        
    def solve_b(self, filename):
        with open(filename, "r") as f:
            input_list = [int(num) for num in f.readline().split(",")]
            input_list.extend([0] * 10000)

            # self.build_grid_and_find_oxygen_system(input_list, (0, 0))

            assert(self.min_steps is not None)
            assert(self.oxygen_system is not None)

            return self.find_min_time_to_fill_oxygen()

    def find_min_time_to_fill_oxygen(self):
        visited = set([self.oxygen_system])

        in_dir = collections.deque([(self.oxygen_system, 0)])
        total_min = 0

        while in_dir:
            next_in_dir = collections.deque()

            while in_dir:
                next_pos, minutes = in_dir.pop()
                total_min = max(total_min, minutes)

                for dir_pos in self.find_adjacent_nodes(next_pos):
                    if dir_pos in visited or dir_pos not in self.grid or self.grid[dir_pos] == WALL:
                        continue

                    next_in_dir.append((dir_pos, minutes + 1))

                visited.add(next_pos)

            in_dir = next_in_dir

        return total_min

    def find_adjacent_nodes(self, pos):
        adj_dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        for dir_pos in adj_dir:
            yield (pos[0] + dir_pos[0], pos[1] + dir_pos[1])

    def build_grid_and_find_oxygen_system(self, intcode, start_pos):
        dirs = [NORTH, SOUTH, WEST, EAST]
        dir_grid = {
            NORTH: (0, 1),
            SOUTH: (0, -1),
            WEST: (-1, 0),
            EAST: (1, 0)
        }
        in_dir = collections.deque([
            [[NORTH], dir_grid[NORTH]],
            [[SOUTH], dir_grid[SOUTH]],
            [[WEST], dir_grid[WEST]],
            [[EAST], dir_grid[EAST]],
        ])
        visited = set([start_pos])

        while in_dir:
            next_in_dir = collections.deque()

            while in_dir:
                next_in_queue = in_dir.popleft()
                last_pos = next_in_queue[1]
                next_list = next_in_queue[0]
                steps = len(next_list)

                visited.add(last_pos)

                computer = self.run_intcode_computer(intcode[:], next_list[:])

                for _ in range(steps):
                    out_value = next(computer)

                self.grid[last_pos] = out_value

                if out_value == OXYGEN:
                    self.oxygen_system = last_pos
                    self.min_steps = steps
                elif out_value == MOVED:
                    for dir_step in dirs:
                        dir_pos = (last_pos[0] + dir_grid[dir_step][0],
                                    last_pos[1] + dir_grid[dir_step][1])

                        if dir_pos not in visited:
                            next_in_dir.append(
                                [[dir_step] + next_list, dir_pos])

            in_dir = next_in_dir

    def run_intcode_computer(self, intcode, values):
        curr_ptr = 0
        curr_base = 0

        while True:
            instruction_count = 0
            op_code, mode1, mode2, mode3 = self.translate_modes(
                intcode[curr_ptr])

            if op_code == 99:
                return

            if op_code in [1, 2, 5, 6, 7, 8, 9]:
                param1 = self.translate_value(
                    curr_ptr + 1, mode1, intcode, curr_base)
                param2 = self.translate_value(
                    curr_ptr + 2, mode2, intcode, curr_base)
                param3 = self.translate_value(
                    curr_ptr + 3, mode3, intcode, curr_base)

                if op_code == 1:
                    intcode[param3] = self.op_code1(
                        intcode[param1], intcode[param2])
                elif op_code == 2:
                    intcode[param3] = self.op_code2(
                        intcode[param1], intcode[param2])
                elif op_code == 5:
                    new_ptr_value = self.op_code5(
                        intcode[param1], intcode[param2])

                    curr_ptr = new_ptr_value if new_ptr_value != -1 else curr_ptr + 3
                elif op_code == 6:
                    new_ptr_value = self.op_code6(
                        intcode[param1], intcode[param2])

                    curr_ptr = new_ptr_value if new_ptr_value != -1 else curr_ptr + 3
                elif op_code == 7:
                    self.op_code7(intcode[param1],
                                  intcode[param2], param3, intcode)
                elif op_code == 8:
                    self.op_code8(intcode[param1],
                                  intcode[param2], param3, intcode)
                elif op_code == 9:
                    curr_base += self.op_code9(intcode[param1], intcode)
            elif op_code in [3, 4]:
                param1 = self.translate_value(
                    curr_ptr + 1, mode1, intcode, curr_base)

                if op_code == 3:
                    value_in = values.pop()
                    self.op_code3(param1, value_in, intcode)
                elif op_code == 4:
                    yield self.op_code4(intcode[param1])
            else:
                raise Exception(
                    "Your computer asplode at op_code {}.".format(op_code))

            if op_code == 5 or op_code == 6:
                continue

            if op_code == 1 or op_code == 2 or op_code == 7 or op_code == 8:
                instruction_count += 4
            else:
                instruction_count += 2

            curr_ptr += instruction_count

        raise Exception("Your computer asplode.")

    def op_code1(self, pos1, pos2):
        return pos1 + pos2

    def op_code2(self, pos1, pos2):
        return pos1 * pos2

    def op_code3(self, pos, inp, memory):
        memory[pos] = inp

    def op_code4(self, value):
        return value

    def op_code5(self, param1, param2):
        return param2 if param1 != 0 else -1

    def op_code6(self, param1, param2):
        return param2 if param1 == 0 else -1

    def op_code7(self, param1, param2, param3, memory):
        memory[param3] = int(param1 < param2)

    def op_code8(self, param1, param2, param3, memory):
        memory[param3] = int(param1 == param2)

    def op_code9(self, param1, memory):
        return param1

    def translate_modes(self, mode):
        full_mode = str(mode).zfill(5)

        op_code = int(full_mode[3:])
        mode1 = int(full_mode[2])
        mode2 = int(full_mode[1])
        mode3 = int(full_mode[0])

        return (op_code, mode1, mode2, mode3)

    def translate_value(self, value, mode, memory, curr_base):
        if mode == 0:
            return memory[value]
        elif mode == 1:
            return value
        elif mode == 2:
            return curr_base + memory[value]
        else:
            raise Exception("Invalid mode. Received mode: {}".format(mode))


if __name__ == "__main__":
    solution = Solution()

    print("Part A:", solution.solve_a("input.txt"))
    print("Part B:", solution.solve_b("input.txt"))
