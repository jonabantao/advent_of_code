import collections


class Solution():
    def solve_a(self, filename):
        with open(filename, "r") as f:
            input_list = [int(num) for num in f.readline().split(",")]
            input_list.extend([0] * 10000)

            black = set()
            white = set()

            self.paint_grid(black, white, input_list, 0)

            return len(black) + len(white)

    def solve_b(self, filename):
        with open(filename, "r") as f:
            input_list = [int(num) for num in f.readline().split(",")]
            input_list.extend([0] * 10000)

            black = set()
            white = set()

            self.paint_grid(black, white, input_list, 1)

            painted = black.union(white)
            max_row = max([row for row, col, in painted])
            max_col = max([col for row, col in painted])
            min_row = min([row for row, col, in painted])
            min_col = min([col for row, col, in painted])

            row_range = abs(max_row - min_row)
            col_range = abs(max_col - min_col)

            grid = [[" " for i in range(col_range + 1)]
                    for j in range(row_range + 1)]

            for row, col in black:
                grid[row + abs(min_row)][col + abs(min_col)] = " "

            for row, col in white:
                grid[row + abs(min_row)][col + abs(min_col)] = "O"

            for line in grid:
                # Mirrored
                print("".join(line))

    def paint_grid(self, black, white, input_list, initial_input):
            DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
            curr_dir = 1
            curr_pos = [0, 0]
            values = collections.deque()
            computer = self.run_intcode_computer(input_list, values)

            while True:
                try:
                    curr_pos_tuple = tuple(curr_pos)

                    if curr_pos_tuple in black:
                        values.appendleft(0)
                    elif curr_pos_tuple in white:
                        values.appendleft(1)
                    else:
                        values.appendleft(initial_input)

                    color_to_paint = next(computer)

                    if color_to_paint == 0:
                        black.add(curr_pos_tuple)

                        if curr_pos_tuple in white:
                            white.remove(curr_pos_tuple)
                    elif color_to_paint == 1:
                        white.add(curr_pos_tuple)

                        if curr_pos_tuple in black:
                            black.remove(curr_pos_tuple)

                    dir_to_turn = next(computer)

                    if dir_to_turn == 0:
                        curr_dir = (curr_dir - 1) % 4
                    elif dir_to_turn == 1:
                        curr_dir = (curr_dir + 1) % 4
                    else:
                        raise Exception("How did you get dir: {}".format(curr_dir))

                    curr_pos[0] += DIRS[curr_dir][0]
                    curr_pos[1] += DIRS[curr_dir][1]
                except StopIteration:
                    break

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
    print("Part B:")
    solution.solve_b("input.txt")
