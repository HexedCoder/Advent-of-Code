def get_input():
    with open("s_input.txt") as file_input:
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

    num = 0

    for row in grid_input:
        # print(num, row)
        for char in row:
            print(f"{char} ", end="")
        print()
        num += 1

    for fold in folds:
        fold = fold.split("=")
        if fold[0] == "y":
            row_count = 0
            for row in range(int(fold[1]), max_rows + 1):
            for column in range(0, max_columns + 1):
                if grid_input[column][row]


        if fold[0] == "x":
            pass


if __name__ == "__main__":
    # try:
    main()
    # except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
    #     print("Error: ", err)
    #     print("Error.__cause__", err.__cause__)
    #     print("Error.__class__", err.__class__.__name__)
    #     print("Error.with_traceback", err.with_traceback)
