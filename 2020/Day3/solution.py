def get_input():
    rows = len(open('input').readline()) - 1
    reps = rows * 3
    grid = [line.replace('\n', '') * reps for line in open('input').readlines()]

    return grid


def main():
    grid = get_input()

    total = slope(grid, 3, 1)
    print("Part 1:", total)

    total = slope(grid, 1, 1) * slope(grid, 3, 1) * slope(grid, 5, 1) * \
        slope(grid, 7, 1) * slope(grid, 1, 2)
    print("Part 2:", total)


def slope(grid, y_move, x_move):
    trees = 0
    x = 0
    y = 0

    while x < len(grid) - 1:
        y += y_move
        x += x_move
        if '#' == grid[x][y]:
            trees += 1

    return trees


if __name__ == "__main__":
    main()
