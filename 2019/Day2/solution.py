def get_input():
    text_file = open("input", "r").readline()
    return text_file


def main():
    text_file = get_input()

    total = part_one(text_file)
    print("Part 1:", total)
    total = part_two(text_file)
    print("Part 2:", total)


def part_one(text_file):

    idx = 0
    nums = [int(num) for num in text_file.split(',')]

    while 99 != nums[idx]:
        nums[1] = 12
        nums[2] = 2

        if nums[idx] == 1:
            result = nums[nums[idx + 1]] + nums[nums[idx + 2]]
            nums[nums[idx + 3]] = result
        elif nums[idx] == 2:
            result = nums[nums[idx + 1]] * nums[nums[idx + 2]]
            nums[nums[idx + 3]] = result

        idx += 4

    return nums[0]


def part_two(text_file):

    saved_nums = [int(num) for num in text_file.split(',')]

    for subj in range(99):
        for verb in range(99):
            nums = saved_nums.copy()

            idx = 0
            result = 0

            nums[1] = subj
            nums[2] = verb

            while 99 != nums[idx]:

                if nums[idx] == 1:
                    result = nums[nums[idx + 1]] + nums[nums[idx + 2]]
                    nums[nums[idx + 3]] = result
                elif nums[idx] == 2:
                    result = nums[nums[idx + 1]] * nums[nums[idx + 2]]
                    nums[nums[idx + 3]] = result

                idx += 4

            if result == 19690720:
                return 100 * subj + verb

    print('Not Found')
    return 0


if __name__ == "__main__":
    main()
