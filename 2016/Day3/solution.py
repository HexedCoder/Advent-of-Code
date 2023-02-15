def get_input():
    text_file = open('input').readlines()
    return text_file


def main():
    file_input = get_input()
    output = part_one(file_input)
    print("Part 1:", output)

    output = part_two(file_input)
    print("Part 2:", output)


def part_one(text_file):
    valid = 0

    for line in text_file:
        nums = [int(num) for num in line.split()]
        if nums[0] + nums[1] > nums[2] and nums[1] + nums[2] > nums[0] and \
                nums[0] + nums[2] > nums[1]:
            valid += 1

    return valid


def part_two(text_file):
    valid = 0
    read = 0
    nums = []

    for line in text_file:
        nums.append([int(num) for num in line.split()])
        read += 1

        if read == 3:
            nums = [[nums[x][y] for x in range(3)] for y in range(3)]
            for triangle in nums:
                if triangle[0] + triangle[1] > triangle[2] and triangle[1] + \
                        triangle[2] > triangle[0] and \
                        triangle[0] + triangle[2] > triangle[1]:
                    valid += 1
            read = 0
            nums = []

    return valid


if __name__ == "__main__":
    main()
