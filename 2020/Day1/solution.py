def get_input():
    nums = []

    text_file = open("input", "r").read().split("\n")

    for num in text_file:
        num = int(num)
        nums.append(num)

    nums.sort()
    return nums


def main():
    nums = get_input()

    total = part_one(nums)
    print("Part 1:", total)

    total = part_two(nums)
    print("Part 2:", total)


def part_one(nums):
    for comp_1 in nums:
        for comp_2 in nums:
            if comp_1 + comp_2 == 2020:
                return comp_1 * comp_2
            elif comp_1 + comp_2 > 2020:
                break


def part_two(nums):
    for comp_1 in nums:
        for comp_2 in nums:
            for comp_3 in nums:
                if comp_1 + comp_2 + comp_3 == 2020:
                    return comp_1 * comp_2 * comp_3
                elif comp_1 + comp_2 + comp_3 > 2020:
                    break


if __name__ == "__main__":
    main()
