def get_input():
    text_file = open("input", "r").read().splitlines()
    return text_file


def check_cpu(x, sig_str):
    if x in range(20, 221, 40):
        return x * sig_str

    else:
        return 0


def check_grid(x, cycle, grid):
    choices = [x - 1, x, x + 1]

    crt = (cycle - 1) % 40
    if crt in choices:
        grid[cycle - 1] = '#'


def main():
    text_file = get_input()

    score_1 = part_one(text_file)
    print("Part 1:", score_1)

    score_2 = part_two(text_file)

    print("Part 2:")
    num = 1
    for char in score_2:
        print(char, end='')
        if num % 40 == 0:
            print()
        num += 1


def part_one(text_file):
    x = 1
    sig_str = 0
    cycle = 0
    for val in text_file:
        val = val.split()

        if val and 'addx' == val[0]:
            cycle += 1
            sig_str += check_cpu(cycle, x)
            cycle += 1
            sig_str += check_cpu(cycle, x)
            x += int(val[1])

        elif 'noop' == val[0]:
            cycle += 1
            sig_str += check_cpu(cycle, x)

    return sig_str


def part_two(text_file):

    grid = list('.' * 240)
    x = 1
    cycle = 0

    for val in text_file:
        val = val.split()

        if val and 'addx' == val[0]:
            cycle += 1
            check_grid(x, cycle, grid)
            cycle += 1
            check_grid(x, cycle, grid)
            x += int(val[1])

        elif 'noop' == val[0]:
            cycle += 1
            check_grid(x, cycle, grid)

    return grid


if __name__ == "__main__":
    main()
