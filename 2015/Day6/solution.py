import copy


def get_input():
    text_file = open("input", "r").read().split("\n")

    grid = []
    for _ in range(1000):
        line = []
        for _ in range(1000):
            line.append(0)
        grid.append(line)

    return grid, text_file


def main():
    grid, text_file = get_input()
    grid_2 = copy.deepcopy(grid)

    result = part_one(grid, text_file)
    print(f'Part One: {result}')

    result = part_two(grid_2, text_file)
    print(f'Part Two: {result}')


def part_one(grid, file_input):
    for line in file_input:
        line = line.split()
        cmd = line[1]
        begin_x, begin_y = map(int, (line[-3].split(',')))
        end_x, end_y = map(int, line[-1].split(','))

        for y in range(begin_y, end_y + 1):
            for x in range(begin_x, end_x + 1):
                if 'on' == cmd:
                    grid[y][x] = True
                elif 'off' == cmd:
                        grid[y][x] = False
                else:
                    grid[y][x] = not grid[y][x]

    return sum(sum(n) for n in grid)


def part_two(grid, file_input):
    for line in file_input:
        line = line.split()
        cmd = line[1]
        begin_x, begin_y = map(int, (line[-3].split(',')))
        end_x, end_y = map(int, line[-1].split(','))

        for y in range(begin_y, end_y + 1):
            for x in range(begin_x, end_x + 1):
                if 'on' == cmd:
                    grid[y][x] += 1
                elif 'off' == cmd:
                    if grid[y][x] != 0:
                        grid[y][x] -= 1
                else:
                    grid[y][x] += 2

    return sum(sum(n) for n in grid)


if __name__ == "__main__":
    main()
