def get_input():
    text_file = open("input", "r").read().split("\n")
    return text_file


def main():
    text_file = get_input()

    part_one(text_file)
    part_two(text_file)


def part_one(text_file):
    nums = []
    total = []

    for line in text_file:
        line = line.split("\t")
        for num in line:
            nums.append(int(num))
        total.append(max(nums) - min(nums))
        nums = []
    print("Part 1:", sum(total))


def part_two(text_file):
    nums = []
    total = []

    for line in text_file:
        line = line.split("\t")
        for num in line:
            nums.append(int(num))
        nums.sort(reverse=True)
        for num in nums:
            for check in nums:
                if num != check:
                    if num % check == 0:
                        total.append(int(num / check))
                        break
        nums = []

    print("Part 2:", sum(total))


if __name__ == "__main__":
    main()
