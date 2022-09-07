flash_count = 0
flash_day = 0


def get_input():
    with open("input.txt") as file_input:
        lines_input = file_input.readlines()

    new_input = []
    line = []

    for line_ in lines_input:
        line_ = line_.replace("\n", "")
        for item in line_:
            item = int(item)
            line.append(item)

        new_input.append(line)
        line = []

    return new_input


def main():
    global flash_day
    file_input = get_input()

    for day in range(1, 1000):
        row = 0
        non_flash = True

        for line in file_input:
            increment(line)

        while non_flash:
            for line in file_input:
                check(line, row, file_input)
                non_flash = check_each(file_input)
                row += 1

        reset(file_input)

        if day == 100:
            print("Part 1:", flash_count)

        sum_list = 0
        for list in file_input:
            sum_list += sum(list)

        if not sum_list:
            print("Part 2:", day)
            break


def increment(line):
    for num in range(0, len(line)):
        line[num] += 1


def flash(row_input, column_input, file_input):
    global flash_count
    for row in range(row_input - 1, row_input + 2):
        for column in range(column_input - 1, column_input + 2):
                if (row >= 0 and column >= 0) and (row <= 9 and column <= 9):
                    if file_input[row][column] != -1:
                        file_input[row][column] += 1
                        if file_input[row][column] > 9:
                            file_input[row][column] = -1
                            flash_count += 1
                            flash(row, column, file_input)


def check(line, row, file_input):
    global flash_count
    for column in range(0, len(line)):
        if line[column] > 9:
            line[column] = -1
            flash_count += 1
            flash(row, column, file_input)


def check_each(file_input):
    has_flash = False
    for row in range(0, len(file_input)):
        for column in range(0, len(file_input)):
            if file_input[row][column] > 9:
                has_flash = True
                return has_flash

    return has_flash


def reset(file_input):
    for row in range(0, len(file_input)):
        for column in range(0, len(file_input)):
            if file_input[row][column] == -1:
                file_input[row][column] += 1



if __name__ == "__main__":
    main()
