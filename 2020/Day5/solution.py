from math import floor, ceil


def get_input():
    with open('input') as f:
        input = f.read().split('\n')

    return input


def main():
    file_input = get_input()

    total = part_one(file_input)
    print("Part 1:", total[0])
    print("Part 2:", total[1])


def get_size(line):
    row = line[0:7]
    row_min = 0
    row_max = 127
    total = row_max + row_min

    for dir_ in row:
        if 'F' == dir_:
            row_max = floor(total / 2)
        else:
            row_min = ceil(total / 2)

        total = row_max + row_min

    col = line[7:]
    col_min = 0
    col_max = 7
    total = col_max + col_min

    for dir_ in col:
        if 'L' == dir_:
            col_max = floor(total / 2)
        else:
            col_min = ceil(total / 2)

        total = col_max + col_min

    return row_min * 8 + col_min


def part_one(file_input):
    _max = -1
    _min = 1000
    seats = []

    for line in file_input:
        size = get_size(line)
        seats.append(int(size))
        if size > _max:
            _max = size
        if size < _min:
            _min = size

    for idx, seat in enumerate(sorted(seats), start=_min):
        if idx != seat:
            return _max, idx


if __name__ == "__main__":
    main()
