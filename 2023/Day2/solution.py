def get_input():
    with open("input") as file_input:
        puzzle_input = file_input.read().split("\n")
        lines_input = []

        for line in puzzle_input:
            if line:
                lines_input.append(line)

    return lines_input


def part_one(file_input):
    max_cubes = {"red": 12, "green": 13, "blue": 14}
    total = 0

    for idx, line in enumerate(file_input, 1):
        line = line.split(': ')[1]
        games = line.split('; ')
        valid = True
        for game in games:
            sets = game.split(', ')
            for cube_set in sets:
                if valid:
                    curr_cubes = {"red": 0, "green": 0, "blue": 0}

                    container = cube_set.split()
                    container[0] = int(container[0])
                    curr_cubes[container[1]] += container[0]
                    for color, cubes in curr_cubes.items():
                        if curr_cubes[color] > max_cubes[color]:
                            valid = False
                            break
        if valid:
            total += idx

    return total


def part_two(file_input):
    power = []

    for idx, line in enumerate(file_input):
        cubes = [0, 0, 0]  # RBG
        line = line.split(': ')[1]
        sets = line.split('; ')
        for hand in sets:
            hand = hand.split(', ')

            for cube in hand:
                num_cubes, color = int(cube.split()[0]), cube.split()[1]
                match color:
                    case "red":
                        cubes[0] = max(num_cubes, cubes[0])
                    case "blue":
                        cubes[1] = max(num_cubes, cubes[1])
                    case "green":
                        cubes[2] = max(num_cubes, cubes[2])

        power.append(cubes[0] * cubes[1] * cubes[2])

    return sum(power)


def main():
    puzzle_input = get_input()

    part_1 = part_one(puzzle_input)
    part_2 = part_two(puzzle_input)

    print(f"Part One:", part_1)
    print(f"Part Two:", part_2)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()
