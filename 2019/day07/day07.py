import itertools


class Solution():
    def solve_a(self, filename):
        with open(filename, "r") as f:
            input_list = [int(num) for num in f.readline().split(",")]

            return max([self.amplify(input_list, perm) for perm in itertools.permutations(range(5), 5)])

    def amplify(self, intcode, settings):
        val = 0

        for phase in settings:
            values = [val, phase]
            val = self.run_intcode_computer(intcode[:], values)

        return val

    def run_intcode_computer(self, intcode, values):
        curr_ptr = 0
        last_value = None  # For testing op_code 4

        while True:
            instruction_count = 0
            op_code, mode1, mode2 = self.translate_modes(intcode[curr_ptr])

            if op_code == 99:
                break

            if op_code in [1, 2, 5, 6, 7, 8]:
                param1 = self.translate_value(curr_ptr + 1, mode1, intcode)
                param2 = self.translate_value(curr_ptr + 2, mode2, intcode)
                index = intcode[curr_ptr + 3]

                if op_code == 1:
                    intcode[index] = self.op_code1(param1, param2)
                elif op_code == 2:
                    intcode[index] = self.op_code2(param1, param2)
                elif op_code == 5:
                    new_ptr_value = self.op_code5(param1, param2)

                    curr_ptr = new_ptr_value if new_ptr_value != -1 else curr_ptr + 3
                elif op_code == 6:
                    new_ptr_value = self.op_code6(param1, param2)

                    curr_ptr = new_ptr_value if new_ptr_value != -1 else curr_ptr + 3
                elif op_code == 7:
                    self.op_code7(param1, param2, index, intcode)
                elif op_code == 8:
                    self.op_code8(param1, param2, index, intcode)
            else:
                if op_code == 3:
                    value_in = values.pop()
                    self.op_code3(intcode[curr_ptr + 1], value_in, intcode)
                elif op_code == 4:
                    param1 = self.translate_value(curr_ptr + 1, mode1, intcode)

                    last_value = self.op_code4(param1)

            if op_code == 5 or op_code == 6:
                continue

            if op_code == 1 or op_code == 2 or op_code == 7 or op_code == 8:
                instruction_count += 4
            else:
                instruction_count += 2

            curr_ptr += instruction_count

        return last_value

    def part_a_tester(self, intcode, value_in):
        self.run_intcode_computer(intcode, value_in)

        return intcode

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

    def translate_modes(self, mode):
        full_mode = str(mode).zfill(4)

        op_code = int(full_mode[2:])
        mode1 = int(full_mode[1])
        mode2 = int(full_mode[0])

        return (op_code, mode1, mode2)

    def translate_value(self, value, mode, memory):
        if mode == 0:
            return memory[memory[value]]
        else:
            return memory[value]


if __name__ == "__main__":
    solution = Solution()

    print("Part A:", solution.solve_a("input.txt"))
