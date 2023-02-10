def get_input():
    nums = [int(num) for num in open("input")]
    return nums


def main():
    nums = get_input()

    print('Part One:', part_one(nums.copy()))
    print('Part Two:', part_two(nums))


def part_one(nums):
    idx, steps = 0, 0

    while True:
        try:
            nums[idx] += 1
            idx += (nums[idx] -1)
            steps += 1

        except IndexError:
            return steps


def part_two(nums):
    idx, steps = 0, 0

    while True:

        try:
            if nums[idx] > 2:
                nums[idx] -= 1
                idx += (nums[idx] + 1)
            else:
                nums[idx] += 1
                idx += (nums[idx] - 1)

            steps += 1

        except IndexError:
            return steps


if __name__ == "__main__":
    main()
