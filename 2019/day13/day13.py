import collections

EMPTY = 0
WALL = 1
BLOCK = 2
PADDLE = 3
BALL = 4

class Solution():
    def solve_a(self, filename):
        with open(filename, "r") as f:
            input_list = [int(num) for num in f.readline().split(",")]
            input_list.extend([0] * 10000)

            computer = self.run_intcode_computer(input_list, [])

            tiles = {
                EMPTY: set(),
                WALL: set(),
                BLOCK: set(),
                PADDLE: set(),
                BALL: set(),
            }

            self.setup_tiles(tiles, computer)

            return len(tiles[BLOCK])


    def solve_b(self, filename):
        with open(filename, "r") as f:
            input_list = [int(num) for num in f.readline().split(",")]
            input_list.extend([0] * 10000)

            computer = self.run_intcode_computer(input_list, [])

            tiles = {
                EMPTY: set(),
                WALL: set(),
                BLOCK: set(),
                PADDLE: set(),
                BALL: set(),
            }

            self.setup_tiles(tiles, computer)
            
            # Freeplay
            input_list[0] = 2
            score = 0
            score_code = (-1, 0)
            values = collections.deque([])

            arcade = self.run_intcode_computer(input_list, values)

            paddle_x_pos = list(tiles[PADDLE])[0][0]
            ball_x_pos = list(tiles[BALL])[0][0]

            try:
                while True:
                    x_coord = next(arcade)
                    y_coord = next(arcade)
                    tile_type = next(arcade)
        
                    coord = (x_coord, y_coord)

                    if coord == score_code:
                        score = tile_type

                    if tile_type == PADDLE:
                        paddle_x_pos = x_coord
                    elif tile_type == BALL:
                        ball_x_pos = x_coord

                    if paddle_x_pos == ball_x_pos:
                        values.append(0)
                    elif paddle_x_pos > ball_x_pos:
                        values.append(-1)
                    else:
                        values.append(1)

            except StopIteration:
                return score

    def setup_tiles(self, tiles, computer):
        try:
            while True:
                x_coord = next(computer)
                y_coord = next(computer)
                tile_type = next(computer)

                coord = (x_coord, y_coord)

                tiles[tile_type].add(coord)
        except StopIteration:
            return

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
