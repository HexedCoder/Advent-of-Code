def get_input():
    with open("input") as file_input:
        puzzle_input = file_input.read().split("\n")
        lines_input = []

        for line in puzzle_input:
            if line:
                lines_input.append(line)

    return lines_input


def check_sides(start, end, y, file_input):
    for row in range(y - 1, y + 2):
        if row == -1:
            continue
        for x in range(start - 1, end + 1):
            if x == -1:
                continue
            try:
                if not file_input[row][x].isdigit() and file_input[row][x] != '.':
                    return True
            except IndexError:
                continue

    return False


def part_one(file_input):
    total = 0
    start = None

    for y, line in enumerate(file_input):
        is_num = False
        for x, char in enumerate(line):
            if char.isdigit():
                if not is_num:
                    start = x
                    is_num = True

                if x == len(line) - 1:
                    if check_sides(start, x, y, file_input):
                        total += int(line[start:x + 1])

            else:
                if is_num:
                    if check_sides(start, x, y, file_input):
                        total += int(line[start:x])
                is_num = False

    return total


def print_surrounding(base, file_input):
    nums = []
    for row in range(base[0] - 1, base[0] + 2):
        if row < 0:
            continue
        is_num = False
        for x in range(base[1] - 1, base[1] + 2):
            if x < 0:
                continue
            try:
                if file_input[row][x].isdigit():
                    if not is_num:
                        is_num = True

                    if x == base[1] + 1:
                        start = x
                        end = x
                        try:
                            while file_input[row][start - 1].isdigit():
                                start -= 1
                        except IndexError:
                            pass

                        try:
                            while file_input[row][end + 1].isdigit():
                                end += 1
                        except IndexError:
                            pass

                        nums.append(int(file_input[row][start:end+1]))

                else:
                    if is_num:
                        start = x
                        while file_input[row][start - 1].isdigit():
                            start -= 1
                        nums.append(int(file_input[row][start:x]))
                        is_num = False

            except IndexError:
                continue
    return nums


def part_two(file_input):
    total = 0
    bases = []

    for y, line in enumerate(file_input):
        for x, char in enumerate(line):
            if not char.isdigit() and char != '.':
                bases.append([y, x])

    for base in bases:
        nums = print_surrounding(base, file_input)
        if len(nums) == 2:
            total += (nums[0] * nums[1])

    return total


def main():
    puzzle_input = get_input()

    part_1 = part_one(puzzle_input)
    part_2 = part_two(puzzle_input)

    print(f"Part One:", part_1)
    print(f"Part Two:", part_2)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()
