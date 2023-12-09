from math import lcm


def get_input():
    with open("input") as file_input:
        puzzle_input = file_input.read().split("\n")
        lines_input = []

    for line in puzzle_input:
        if line:
            lines_input.append(line)
    return lines_input


def part_one(file_input):
    moves = file_input[0]
    mapping = {}
    found = "AAA"

    print(moves)
    for line in file_input[1:]:
        letter, direction = line.replace("(", "").replace(")", "").split(" = ")
        mapping[letter] = direction.split(', ')

    # print(mapping)

    total_score = 0
    idx = 0
    while found != "ZZZ":
        direction = 0 if moves[idx] == 'L' else 1
        found = mapping[found][direction]
        idx = (idx + 1) % len(moves)
        # print(idx, found)
        total_score += 1

    return total_score


def part_two(file_input):
    moves = file_input[0]
    mapping = {}
    found = []
    for move in file_input[1:]:
        letter, _ = move.replace("(", "").replace(")", "").split(" = ")
        if letter[-1] == 'A':
            found.append([letter, 0])

    for line in file_input[1:]:
        letter, direction = line.replace("(", "").replace(")", "").split(" = ")
        mapping[letter] = direction.split(', ')

    total_score = 0
    idx = 0
    done = False
    while not done:
        direction = 0 if moves[idx] == 'L' else 1

        for l_idx, start in enumerate(found):
            end = mapping[start[0]][direction]
            found[l_idx][0] = end
            if end[-1] == 'Z':
                # print(end, total_score)
                found[l_idx][1] = total_score + 1
        done = all(item[1] != 0 for item in found)
        total_score += 1
        idx = (idx + 1) % len(moves)

    values = [val[1] for val in found]
    result_lcm = 1
    for num in values:
        result_lcm = lcm(result_lcm, num)
    return result_lcm


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
