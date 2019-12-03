class Solution():
    def solve_part_a(self, filename):
        with open(filename, "r") as f:
            input_list = [int(num) for num in f.readline().split(",")]

            input_list[1] = 12
            input_list[2] = 2

            return self.part_a(input_list)

    def solve_part_b(self, filename):
        with open(filename, "r") as f:
            input_list = [int(num) for num in f.readline().split(",")]

            for noun in range(0, 100):
                for verb in range(0, 100):
                    dup_list = input_list[:]
                    dup_list[1] = noun
                    dup_list[2] = verb

                    result = self.part_a(dup_list)

                    if result == 19690720:
                        return noun * 100 + verb

        return None

    def part_a(self, intcode):
        for idx in range(0, len(intcode), 4):
            op_code = intcode[idx]

            if op_code == 99:
                break

            pos1 = intcode[intcode[idx + 1]]
            pos2 = intcode[intcode[idx + 2]]

            if op_code == 1:
                intcode[intcode[idx + 3]] = self.op_code1(pos1, pos2)
            elif op_code == 2:
                intcode[intcode[idx + 3]] = self.op_code2(pos1, pos2)

        return intcode[0]

    def op_code1(self, pos1, pos2):
        return pos1 + pos2

    def op_code2(self, pos1, pos2):
        return pos1 * pos2


if __name__ == "__main__":
    solution = Solution()

    print("Part A:", solution.solve_part_a("input.txt"))
    print("Part B:", solution.solve_part_b("input.txt"))
