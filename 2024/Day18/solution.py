def get_input():
    with open("input", "r") as file:
        file_input = [list(map(int, line.split(","))) for line in file.read().split("\n")]

    return file_input

def solve(input_data, p1):
    height, width = 70, 70

    if p1:
        corrupted = {(x, y) for x, y in input_data[:1024]}
    else:
        corrupted = set()
        
    start = (0, 0)
    end = (height, width)

    for coord in input_data:
        if not p1:
            corrupted.add(tuple(coord))

        queue = [(start, 0)]
        visited = set([start])
        path_found = False

        while queue:
            (x, y), steps = queue.pop(0)
            if (x, y) == end:
                if p1:
                    return steps

                path_found = True
                break
            directions = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
            for nx, ny in directions:
                if 0 <= nx <= height and 0 <= ny <= width and (nx, ny) not in corrupted and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), steps + 1))

        if not p1 and not path_found:
            return f"{coord[0]},{coord[1]}"
    if p1:
        return len(queue)

def main():

    input_data = get_input()

    part_1 = solve(input_data, True)
    print(f"Part One:", part_1)

    part_2 = solve(input_data, False)
    print(f"Part Two:", part_2)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        print("Exiting...")