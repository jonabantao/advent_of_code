import collections


class Solution():
    def solve_a(self, filename, width, height):
        with open(filename) as f:
            data = [int(num) for line in f for num in list(line)]
            image = self.create_image(data, width, height)

            result = min([collections.Counter(layer)
                          for layer in image], key=lambda x: x[0])

            return result[2] * result[1]

    def solve_b(self, filename, width, height):
        with open(filename) as f:
            data = [int(num) for line in f for num in list(line)]
            image = self.create_image(data, width, height)

            self.read_message(image, width)

    def create_image(self, data, width, height):
        image = []
        total_per_layer = width * height

        for idx in range(0, len(data), total_per_layer):
            image.append(data[idx:idx + total_per_layer])

        return image

    def read_message(self, layers, width):
        message = []
        PRINT_OUT = {
            0: " ",
            1: "X",
            2: " ",
        }

        for idx in range(len(layers[0])):
            value = PRINT_OUT[2]

            for layer in layers:
                if layer[idx] != 2:
                    value = PRINT_OUT[layer[idx]]
                    break

            message.append(value)

        for idx in range(0, len(layers[0]), width):
            print("".join(message[idx:idx + width]))


if __name__ == "__main__":
    solution = Solution()

    print("Part A:", solution.solve_a("input.txt", 25, 6))
    print("Part B:")
    solution.solve_b("input.txt", 25, 6)
