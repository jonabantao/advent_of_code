class Solution():
    def fft(self, input_list, end_phase):
        phase = 0
        pattern = [0, 1, 0, -1]
        curr_idx = 0
        next_input = []
        result_to_sum = []

        while phase < end_phase:
            next_input.clear()

            while curr_idx < len(input_list):
                skippedFirstValue = False
                result_to_sum.clear()
                sub_idx = 0

                while sub_idx < len(input_list):
                    for num in pattern:
                        if sub_idx >= len(input_list):
                            break

                        repeat = 0

                        if not skippedFirstValue:
                            skippedFirstValue = True
                            repeat += 1


                        while repeat <= curr_idx:
                            if sub_idx >= len(input_list):
                                break


                            result_to_sum.append(input_list[sub_idx] * num)
                            repeat += 1
                            sub_idx += 1

                sum_result = abs(sum(result_to_sum)) % 10
                next_input.append(sum_result)
                curr_idx += 1

            input_list = next_input[:]
            curr_idx = 0
            phase += 1

        return "".join(str(num) for num in input_list)[:8]



if __name__ == "__main__":
    sol = Solution()

    with open("input.txt") as f:
        raw_in = f.readline().rstrip()
        offset_b = int(raw_in[:7])
        input_list = [int(num) for num in raw_in]
        b_input = (input_list * 10000)[offset_b:]

        print("Part A:", sol.fft(input_list[:], 100))
        # print("Part B:", sol.fft(b_input, 100))
