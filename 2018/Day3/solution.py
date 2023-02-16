import copy


def get_input():
    with open('input') as f:
        file_input = [piece for piece in [line.replace('@', '').split() for line in f.read().split('\n') if line]]
        f.seek(0)

    height = 0
    width = 0

    for _, loc, size in file_input:
        x, y = map(int, loc[:-1].split(','))
        w, h = map(int, size.split('x'))
        if width < x + w:
            width = x + w + 1
        if height < y + h:
            height = y + h + 1

    grid = [['' for _ in range(width)] for _ in range(height)]

    return grid, file_input


def part_one(grid, inputs):
    for _, loc, size in inputs:
        x, y = map(int, loc[:-1].split(','))
        width, height = map(int, size.split('x'))
        for row in range(y, y + height):
            for col in range(x, x + width):
                if '' == grid[row][col]:
                    grid[row][col] = 0
                else:
                    grid[row][col] += 1

    total = 0
    for line in grid:
        for num in line:
            if num and num > 0:
                total += 1

    return total


def part_two(grid, inputs):
    for id, loc, size in inputs:
        id = int(id[1:])
        x, y = map(int, loc[:-1].split(','))
        width, height = map(int, size.split('x'))
        for row in range(y, y + height):
            for col in range(x, x + width):
                if '' == grid[row][col]:
                    grid[row][col] = id
                else:
                    grid[row][col] = -1

    for id, loc, size in inputs:
        id = int(id[1:])
        x, y = map(int, loc[:-1].split(','))
        width, height = map(int, size.split('x'))

        destroyed = False
        for row in range(y, y + height):
            for col in range(x, x + width):
                if id != grid[row][col]:
                    destroyed = True

        if not destroyed:
            return id

    return None


def main():
    grid, inputs = get_input()

    print('Part One:', part_one(copy.deepcopy(grid), inputs))
    print('Part Two:', part_two(grid, inputs))


if __name__ == "__main__":
    main()
