def get_input():
    with open("input.txt") as file_input:
        lines_input = file_input.readlines()

    list_int_input = []

    for line in lines_input:

        line = line.replace("\n", "")
        line_int = []

        for num in line:
            num = int(num)
            line_int.append(num)
        list_int_input.append(line_int)


    return list_int_input


def find_lows(height_list):
    lows = []
    y = 0
    for each_line in height_list:
        x = 0
        for number in each_line:
            if x == 0:
                if y == 0:
                    if height_list[y][x + 1] > number and height_list[y + 1][x] > number:
                        lows.append(number + 1)

                elif y < len(height_list) - 1:

                    if height_list[y][x + 1] > number and height_list[y - 1][x] > number and height_list[y + 1][x] > number:
                        lows.append(number + 1)
                else:

                    if height_list[y][x + 1] > number and height_list[y - 1][x] > number:
                        lows.append(number + 1)
            elif x < len(each_line) - 1:

                if y == 0:
                    if height_list[y][x - 1] > number and height_list[y][x + 1] > number and height_list[y + 1][x] > number:
                        lows.append(number + 1)

                elif y < len(height_list) - 1:
                    if height_list[y][x - 1] > number and height_list[y][x + 1] > number and height_list[y - 1][x] > number and height_list[y + 1][x] > number:
                        lows.append(number + 1)

                elif y == len(height_list) - 1:
                    if height_list[y][x - 1] > number and height_list[y][x + 1] > number and height_list[y - 1][x] > number:
                        lows.append(number + 1)

            else:
                if y == 0:
                    if height_list[y][x - 1] > number and height_list[y + 1][x] > number:

                        lows.append(number + 1)

                elif y < len(height_list) - 1:
                    if height_list[y][x - 1] > number and height_list[y - 1][x] > number and height_list[y + 1][x] > number:

                        lows.append(number + 1)

                elif y == len(height_list) - 1:
                    if height_list[y][x - 1] > number and height_list[y - 1][x] > number:

                        lows.append(number + 1)

            x += 1
        y += 1

    return lows


def main():
    height_map = get_input()
    low_points = find_lows(height_map)

    print("Risk Level:", sum(low_points))


if __name__ == "__main__":
    main()
