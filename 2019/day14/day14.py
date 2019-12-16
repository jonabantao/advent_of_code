import collections
import math


class Output():
    def __init__(self, input_resources = {}, num_output = 0):
        self.input_resources = input_resources
        self.num_output = num_output


class Solution():
    def solve_a(self, input_list):
        return self.find_ore_required(input_list, 1)

    # Terribad.
    def solve_b(self, input_list):
        num = 2172134
        
        while self.find_ore_required(input_list, num) < 1000000000000:
            num += 1

        return num - 1

    def find_ore_required(self, input_list, fuel_req):
        proc_in = [[[r.split(" ") for r in res_in.split(", ")], res_out.split()]
                   for line in input_list
                   for res_in, res_out in [line.rstrip().split(" => ")]]

        res_map = {}
        res_in_required = collections.defaultdict(int)
        res_in_required["FUEL"] = fuel_req

        for res, out in proc_in:
            res_map[out[1]] = Output(
                {type_r: int(num_r) for num_r, type_r in res},
                int(out[0])
            )

        queue = collections.deque(["FUEL"])

        while queue:
            next_queue = collections.deque()

            while queue:
                proc_res = queue.popleft()

                if proc_res == "ORE" or res_in_required[proc_res] < 1:
                    continue

                record = res_map[proc_res]
                trans_req = math.ceil(
                    res_in_required[proc_res] / record.num_output)
                res_in_required[proc_res] -= (record.num_output * trans_req)

                for res_in, res_in_num in res_map[proc_res].input_resources.items():
                    res_in_required[res_in] += res_in_num * trans_req

                    next_queue.append(res_in)

            queue = next_queue

        return res_in_required["ORE"]



if __name__ == "__main__":
    solution = Solution()

    with open("input.txt") as f:
        input_list = [line.rstrip() for line in f]

        print(solution.solve_a(input_list[:]))
        print(solution.solve_b(input_list[:]))
