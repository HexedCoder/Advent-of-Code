def get_input():
    with open("input") as file_input:
        lines_input = [list (row) for row in file_input.read().split("\n")]

    return lines_input


def distance(grid, row, column):
    queue = [(row, column, 0)]
    visited = {(row, column)}
    while queue:
        curr_row, curr_column, distance = queue.pop(0)

        neighbors = [(curr_row + 1, curr_column), (curr_row - 1, curr_column), (curr_row, curr_column + 1), (curr_row, curr_column - 1)]

        if grid[curr_row][curr_column] == 'E':
            return distance

        for neighbor in neighbors:
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                if 0 <= curr_row < len(grid) and 0 <= curr_column < len(grid[0]):

                    if grid[neighbor[0]][neighbor[1]] == 'E' and ord('z') - ord(grid[curr_row][curr_column]) <= 1:
                        queue.append((neighbor[0], neighbor[1], 1 + distance))
                    elif grid[neighbor[0]][neighbor[1]] != 'E' and (neighbor[0], neighbor[1]) not in visited and ord(grid[neighbor[0]][neighbor[1]]) - ord(grid[curr_row][curr_column]) <= 1:
                        queue.append((neighbor[0], neighbor[1], 1 + distance))
                        visited.add((neighbor[0], neighbor[1]))


def main():

    grid = get_input()

    rows, cols = len(grid), len(grid[0])

    part_1 = 0
    part_2 = 999999999999

    for row in range(rows):
        for column in range(cols):
            if grid[row][column] == 'S':
                grid[row][column] = 'a'
                part_1 = distance(grid, row, column)

    for row in range(rows):
        for column in range(cols):
            if grid[row][column] == 'S' or grid[row][column] == 'a':
                grid[row][column] = 'a'
                num = distance(grid, row, column)
                if num and num < part_2:
                    part_2 = num

    print(f"Part One:", part_1)
    print(f"Part Two:", part_2)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc

        print_exc()
