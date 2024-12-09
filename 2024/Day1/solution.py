def get_input():
    with open("input") as _input:
        line_input = _input.readlines()
    l_nums = []
    r_nums = []
    for line in line_input:
        l_num, r_num = list(map(int, line.split()))
        l_nums.append(l_num)
        r_nums.append(r_num)
    return l_nums, r_nums

def part_1(l_nums, r_nums):
    output_val = 0
    l_nums = sorted(l_nums)
    r_nums = sorted(r_nums)

    for i in range(len(l_nums)):
        output_val += abs(l_nums[i] - r_nums[i])

    return output_val


def part_2(l_nums, r_nums):
    output_val = 0
    l_nums = sorted(l_nums)
    r_nums = sorted(r_nums)

    for i in range(len(l_nums)):
        output_val += l_nums[i] * r_nums.count(l_nums[i])

    return output_val


def main():
    l_nums, r_nums = get_input()
    print("Part 1:", part_1(l_nums, r_nums))
    print("Part 2:", part_2(l_nums, r_nums))


if __name__ == "__main__":
    main()
