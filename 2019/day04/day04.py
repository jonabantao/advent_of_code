import collections


class Solution():
    def solve_part_a(self, low, high):
        count = 0

        for num in range(low, high + 1):
            if self.part_a(str(num)):
                count += 1

        return count

    def solve_part_b(self, low, high):
        count = 0

        for num in range(low, high + 1):
            if self.part_b(str(num)):
                count += 1

        return count

    def part_a(self, num):
        found_pair = False

        for idx in range(len(num) - 1):
            first = int(num[idx])
            second = int(num[idx + 1])

            if first > second:
                return False

            if first == second:
                found_pair = True

        return found_pair

    def part_b(self, num):
        pairs = collections.defaultdict(int)

        for idx in range(len(num) - 1):
            first = int(num[idx])
            second = int(num[idx + 1])

            if first > second:
                return False

            if first == second:
                pairs[first] += 1

        return any(count == 1 for count in pairs.values())


if __name__ == "__main__":
    solution = Solution()

    print("Part A:", solution.solve_part_a(356261, 846303))
    print("Part B:", solution.solve_part_b(356261, 846303))
