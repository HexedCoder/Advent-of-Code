import heapq


def get_input_1():
    with open("input") as file_input:
        lines_input = file_input.read().split("\n")

    grid = []
    weights = []
    for idx, val in enumerate(lines_input):
        grid.append([99999999 for _ in range(len(lines_input[0]))])
        weights.append([int(char) for char in val])

    return grid, weights


def get_input_2():
    with open("input") as file_input:
        lines_input = file_input.read().split("\n")

    grid = []
    weights = []

    for idx, val in enumerate(lines_input) :
        list = []
        grid.append([99999999 for _ in range(5 * len(lines_input[0]))])
        for num in range(0, 5):
            for char in val:
                char = int(char) + num
                if char > 9:
                    char = (int(char) % 10) + 1

                list.append(char)
        weights.append(list)


    d = len(weights)
    max_list_size = len(weights) * 5
    extended_weights = [[0 for _ in range(max_list_size)] for _ in range(max_list_size)]

    for y_index, y in enumerate(extended_weights):
        for x_index, x in enumerate(y):
            n = weights[y_index % d][x_index % d]
            extended_weights[y_index][x_index] = (n + ((y_index // d) + (
                        x_index // d)) - 1) % 9 + 1  # formula: i = (n - 1) % 9 + 1

    grid = []
    for _, _ in enumerate(extended_weights):
        grid.append([99999999 for _ in range(len(extended_weights[0]))])

    return grid, extended_weights


def distance(grid, weights):
    rows, cols = len(weights), len(weights[0])

    queue = []
    heapq.heappush(queue, (0, 0, 0))
    visited = {(0, 0)}
    grid[0][0] = 0

    while queue:
        distance, curr_row, curr_column = heapq.heappop(queue)

        neighbors = [(curr_row + 1, curr_column), (curr_row - 1, curr_column),
                     (curr_row, curr_column + 1), (curr_row, curr_column - 1)]

        if curr_row == rows - 1 and curr_column == cols - 1:
            grid[curr_row][curr_column] = distance
            break

        for neighbor in neighbors:
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and 0 <= curr_row < rows and 0 <= curr_column < cols:

                weight = weights[neighbor[0]][neighbor[1]]

                if weight + distance < grid[neighbor[0]][neighbor[1]]:
                    grid[neighbor[0]][neighbor[1]] = distance + weight

                    heapq.heappush(queue, (
                    weight + distance, neighbor[0], neighbor[1]))
                    visited.add((curr_row, curr_column))

    return grid[rows - 1][cols - 1]


def main():
    grid, weights = get_input_1()
    part_1 = distance(grid, weights)
    print(f"Part One:", part_1)

    grid, weights = get_input_2()
    part_2 = distance(grid, weights)
    print(f"Part Two:", part_2)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc

        print_exc()
