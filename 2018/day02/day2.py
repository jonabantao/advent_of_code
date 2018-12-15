def main(filename):
    strings = []

    with open(filename, "r") as f:
        strings = [line.strip() for line in f.readlines()]

    part_one(strings)
    part_two(strings)


def part_one(string_arr):
    """To make sure you didn't miss any, you scan the likely candidate boxes again, counting 
    the number that have an ID containing exactly two of any letter and then separately counting
    those with exactly three of any letter. You can multiply those two counts together to get 
    a rudimentary checksum and compare it to what your device predicts.
    """
    two_count = 0
    three_count = 0

    for string in string_arr:
        char_count = {}

        for char in string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        counts = char_count.values()

        if 2 in counts:
            two_count += 1
        if 3 in counts:
            three_count += 1

    print(two_count * three_count)


def part_two(string_arr):
    """The boxes will have IDs which differ by exactly one character at the same position in both strings.

    What letters are common between the two correct box IDs?
    """
    for idx, string1 in enumerate(string_arr[:-1]):
        for string2 in string_arr[(idx + 1):]:
            mismatch_count = 0
            last_idx_mismatch = None

            for idx2, _ in enumerate(string1):
                if string1[idx2] != string2[idx2]:
                    mismatch_count += 1
                    last_idx_mismatch = idx2

            if mismatch_count == 1:
                print(string1[0:(last_idx_mismatch)] +
                      string1[(last_idx_mismatch + 1):])


if __name__ == "__main__":
    main("input.txt")
