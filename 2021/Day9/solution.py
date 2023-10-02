width = 0
bottom = 0
_map = []


def get_input():
    with open('input') as file_input:
        lines_input = file_input.readlines()

    list_int_input = []

    for line in lines_input:
        line = list(map(int, line.replace("\n", "")))
        list_int_input.append([num for num in line])

    return list_int_input


def find_lows(height_list):
    basin_coord = []
    basin_nums = []

    for y, row in enumerate(height_list):
        for x, number in enumerate(row):
            neighbors = [
                (x - 1, y), (x + 1, y),  # Left and right
                (x, y - 1), (x, y + 1)   # Above and below
            ]

            valid_basin = True
            for neighbor_x, neighbor_y in neighbors:

                if 0 <= neighbor_x < len(row) and 0 <= neighbor_y < len(height_list):
                    if height_list[neighbor_y][neighbor_x] <= number:
                        valid_basin = False
                        break

            if valid_basin:
                basin_coord.append((x, y))
                basin_nums.append(number + 1)

    return basin_coord, sum(basin_nums)


def check(x, y):
    global width, bottom, _map
    points = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dir_x, dir_y in directions:
        x_temp = x + dir_x
        y_temp = y + dir_y
            
        while x_temp <= width and x_temp >= 0 and y_temp >= 0 and y_temp <= bottom:
            if _map[y_temp][x_temp] != 9:
                points.append((x_temp, y_temp))
            else:
                break

            x_temp += dir_x
            y_temp += dir_y

    return points


def basin_size(height_list, map_):
    global width, bottom, _map
    width = len(map_[1]) - 1
    bottom = len(map_) - 1
    _map = map_
    basin_sizes = []

    for index, coord in enumerate(height_list):
        x = coord[0]
        y = coord[1]
        size = 0

        result = check(x, y)
        size += len(result)

        for neighbor_x, neighbor_y in result:
            new_result = check(neighbor_x, neighbor_y)

            for point in new_result:
                if point not in result:
                    result.append(point)
                    size += 1

        basin_sizes.append(size)
        index += 1

    basin_sizes.sort(reverse=True)

    return basin_sizes


def main():
    height_map = get_input()
    basin_points, basin_nums = find_lows(height_map)
    top_basin_sizes = basin_size(basin_points, height_map)

    product = top_basin_sizes[0] * top_basin_sizes[1] * top_basin_sizes[2]

    print("Part 1:", basin_nums)
    print("Part 2:", product)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()