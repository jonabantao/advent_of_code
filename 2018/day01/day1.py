def main(filename):
    part_one(filename)
    part_two(filename)


def part_one(filename):
    """Starting with a frequency of zero, what is the resulting frequency after all of the 
    changes in frequency have been applied
    """
    with open(filename, "r") as f:
        print(sum([int(num) for num in f.readlines()]))


def part_two(filename):
    """You notice that the device repeats the same frequency change list over and over. 
    To calibrate the device, you need to find the first frequency it reaches twice.

    Note that your device might need to repeat its list of frequency changes many times 
    before a duplicate frequency is found, and that duplicates might be found while in 
    the middle of processing the list.
    """
    curr_freq = 0
    visited_freqs = {curr_freq}

    with open(filename, "r") as f:
        nums = [int(num) for num in f.readlines()]

        while True:
            for num in nums:
                curr_freq += num

                if curr_freq in visited_freqs:
                    print(curr_freq)
                    return

                visited_freqs.add(curr_freq)


if __name__ == "__main__":
    main("input.txt")
