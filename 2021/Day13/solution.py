def get_input():
    with open("input") as file_input:
        lines_input = file_input.readlines()

    max_columns = 0
    max_rows = 0
    folds = []
    coords = []

    for line in lines_input:
        if line[0] != "f":
            line = line.replace("\n", "")
            if line != "":

                line = line.split(",")
                coords.append((int(line[0]), int(line[1])))

                if int(line[0]) > max_rows:
                    max_rows = int(line[0])

                if int(line[1]) > max_columns:
                    max_columns = int(line[1])

        else:
            line = line.split()
            folds.append(line[-1])

    all_rows = []
    for num in range(0, max_columns + 1):
        row = ["." for _ in range(0, max_rows + 1)]
        all_rows.append(row)

    return all_rows, folds, coords, max_columns, max_rows


def main():
    grid_input, folds, coords, max_columns, max_rows = get_input()

    for coord in coords:
        x = coord[0]
        y = coord[1]
        grid_input[y][x] = "#"


    # part1
    total = fold_grid(folds, grid_input, max_columns, max_rows)
    print(f"Part 1: {total}")

    print()

    # part2
    fold_grid(folds, grid_input, max_columns, max_rows, True)
    print(f"Part 2:")
    print_grid(grid_input, folds, True)


def fold_grid(folds, grid_input, max_columns, max_rows, part_2=False):
    total_folds = 0
    for fold in folds:
        if total_folds == 0 or part_2:
            fold = fold.split("=")
            if fold[0] == "y":
                for row in range(0, max_rows + 1):
                    for column in range(int(fold[1]), max_columns + 1):
                        if grid_input[column][row] == "#":
                            grid_input[column][row] = "."
                            grid_input[(int(fold[1]) - (column - int(fold[1])))][
                                row] = "#"

            elif fold[0] == "x":
                for row in range(int(fold[1]), max_rows + 1):
                    for column in range(0, max_columns + 1):
                        if grid_input[column][row] == "#":
                            grid_input[column][row] = "."
                            grid_input[column][
                                (int(fold[1]) - (row - int(fold[1])))] = "#"
        total_folds += 1

    total_dots = 0
    for line in grid_input:
        for char in line:
            if char == "#":
                total_dots += 1

    return total_dots


def print_grid(grid_input, folds, part_2=False):
    hor_split = -1
    vert_split = -1
    num_folds = 0

    for fold in folds:
        if num_folds == 0 or part_2:
            fold = fold.split("=")
            if fold[0] == "y":
                vert_split = int(fold[1])
            if fold[0] == "x":
                hor_split = int(fold[1])
            num_folds += 1

    vertical = 0
    for row in grid_input:
        horizontal = 0
        # print(num, row)
        for char in row:
            if hor_split != horizontal:
                print(f"{char} ", end="")
            else:
                break
            horizontal += 1

        print()

        if (vert_split - 2) < vertical < (vert_split + 1):
            break
        vertical += 1


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        print("Error: ", err)
        print("Error.__cause__", err.__cause__)
        print("Error.__class__", err.__class__.__name__)
        print("Error.with_traceback", err.with_traceback)
