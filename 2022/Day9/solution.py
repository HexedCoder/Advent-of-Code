def get_input():
    text_file = open("input", "r").read().split("\n")

    horiz = 0
    vert = 0

    horiz_min = 0
    horiz_max = -10000

    vert_min = 0
    vert_max = -10000

    for line in text_file:
        line = line.split()
        if line:
            if line[0] == 'R':
                horiz += int(line[1])
                if horiz > horiz_max:
                    horiz_max = horiz
            elif line[0] == 'L':
                horiz -= int(line[1])
                if horiz < horiz_min:
                    horiz_min = horiz
            elif line[0] == 'U':
                vert += int(line[1])
                if vert > vert_max:
                    vert_max = vert
            elif line[0] == 'D':
                vert -= int(line[1])
                if vert < vert_min:
                    vert_min = vert

    height = abs(horiz_max - horiz_min) + 1
    width = abs(vert_max - vert_min) + 1

    print(f"{width = } {height = }")

    lines = []

    for _ in range(height):
        lines.append(['.' for _ in range(width)])

    return text_file, lines


def main():
    code_input, grid = get_input()

    output = part_one(code_input, grid)
    # print("Part 1:", output)

    # output = part_two(code_input)
    # print("Part 2:", output)


def part_one(code_input, grid):

    visible = 0
    head = [-1, len(grid) - 1]
    # tail = [0, 0]

    for line in code_input:
        print(line)
        if line != '':
            line = line.split()
            print(line, head)

            inc = int(line[1])

            if line[0] == 'R':
                for num in range(inc):
                    grid[head[1]][head[0] + num] = '#'
                head[0] += inc
            elif line[0] == 'L':
                for num in range(inc - 1, 0, -1):
                    grid[head[1]][head[0] - num] = '#'
                head[0] -= inc

            elif line[0] == 'U':
                for num in range(inc):
                    grid[head[1] - num][head[0]] = '#'
                head[1] -= inc
            elif line[0] == 'D':
                for num in range(inc + 1, 0, -1):
                    grid[head[1] + num][head[0]] = '#'
                head[1] += inc

            for line in grid:
                print(line)

        else:
            break
    #
    # print()
    # for line in grid:
    #     print(line)

    return visible


def part_two(code_input):

    return 0


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()
