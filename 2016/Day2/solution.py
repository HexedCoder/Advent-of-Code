def get_input():
    text_file = open('input').read()

    return text_file


def main():
    file_input = get_input()
    output = part_one(file_input)
    print("Part 1:", output)

    output = part_two(file_input)
    print("Part 2:", output)


def part_one(text_file):
    grid = [[str(x + y) for x in range(1, 4)] for y in range(0, 9, 3)]

    code = ''
    edge = len(grid[0]) - 1
    EOF = len(text_file)

    # starting_location [1,1]
    x = 1
    y = 1
    for idx, direction in enumerate(text_file, 1):
        if 'U' == direction:
            x = x - 1 if x > 0 else 0
        if 'D' == direction:
            x = x + 1 if x < edge else edge
        if 'L' == direction:
            y = y - 1 if y > 0 else 0
        if 'R' == direction:
            y = y + 1 if y < edge else edge
        if '\n' == direction or EOF == idx:
            code += grid[x][y]

    return code


def part_two(text_file):
    grid = [['', '', '1', '', ''], ['', '2', '3', '4', ''], ['5', '6', '7', '8', '9'], ['', 'A', 'B', 'C', ''], ['', '', 'D', '', '']]

    code = ''
    edge = len(grid[0]) - 1
    EOF = len(text_file)

    # starting_location [1,1]
    x = 2
    y = 0
    for idx, direction in enumerate(text_file, 1):
        if 'U' == direction:
            x = x - 1 if (x > 0 and grid[x-1][y]) else x
        if 'D' == direction:
            x = x + 1 if (x < edge and grid[x+1][y]) else x
        if 'L' == direction:
            y = y - 1 if (y > 0 and grid[x][y-1]) else y
        if 'R' == direction:
            y = y + 1 if (y < edge and grid[x][y+1]) else y
        if '\n' == direction or EOF == idx:
            code += grid[x][y]

    return code


if __name__ == "__main__":
    main()
