def get_input():
    with open("input") as file_input:
        puzzle_input = file_input.read().split("\n\n")
        lines_input = []
        p1_seeds = []

        tmp = []
        p2_seeds = []

        seeds = list(map(int, puzzle_input[0][6:].split()))
        for idx, num in enumerate(seeds):
            idx += 1
            if not idx % 2:
                continue
            tmp.append([num, seeds[idx]])
            p1_seeds.append(num)
            p1_seeds.append(seeds[idx])
        for minimum, maximum in tmp:
            p2_seeds.append([minimum, minimum + maximum])

        for line in puzzle_input[1:]:
            if line:
                lines_input.append(line)
    return p1_seeds, p2_seeds, lines_input


def part_one(seeds, file_input):
    mapping = {"seed-to-soil": [], "soil-to-fertilizer": [], "fertilizer-to-water": [], "water-to-light": [], "light-to-temperature": [], "temperature-to-humidity": [], "humidity-to-location": []}

    for line in file_input:
        map_type = line[0:line.index(' ')]
        values = line[line.index(':'):].split('\n')[1:]
        values = [list(map(int, nums.split())) for nums in values if nums]

        for dst, src, val_range in values:
            mapping[map_type].append([dst, src, val_range])

    low = 1000000000
    for seed in seeds:
        prev = seed
        for key in mapping.keys():
            try:
                for idx, values in enumerate(mapping[key]):
                    max_num = mapping[key][idx][1] + mapping[key][idx][2]
                    if mapping[key][idx][1] <= prev <= max_num:
                        prev = prev + mapping[key][idx][0] - mapping[key][idx][1]
                        break
                raise KeyError
            except KeyError:
                pass
        if prev < low:
            low = prev

    return low


def check_seed(attempt, seeds):
    for min_num, max_num in seeds:
        if min_num <= attempt <= max_num:
            return True

    return False


def part_two(seeds, file_input):
    mapping = {'humidity-to-location': [], 'temperature-to-humidity': [], 'light-to-temperature': [], 'water-to-light': [], 'fertilizer-to-water': [], 'soil-to-fertilizer': [], 'seed-to-soil': []}

    for line in file_input:
        map_type = line[0:line.index(' ')]
        values = line[line.index(':'):].split('\n')[1:]
        values = [list(map(int, nums.split())) for nums in values if nums]

        for dst, src, val_range in values:
            mapping[map_type].append([dst, src, val_range - 1])

    min_seed = 1000000000000
    max_seed = 0
    for low, high in seeds:
        if low < min_seed:
            min_seed = low
        if high > max_seed:
            max_seed = high

    prev = 0
    while True:
        prev += 1
        answer = get_attempt(prev, mapping)
        skip_answer = get_attempt(prev + 30000, mapping)

        if skip_answer == answer + 30000:
            prev += 30000

        if min_seed <= answer <= max_seed:
            if check_seed(answer, seeds):
                prev -= 30000
                for num in range(30000):
                    if get_attempt(num, mapping):
                        return prev
                    prev += 1


def get_attempt(attempt, mapping):
    for key in mapping.keys():
        for idx, _ in enumerate(mapping[key]):
            min_num = mapping[key][idx][0]
            max_num = min_num + mapping[key][idx][2]
            if min_num <= attempt <= max_num:
                attempt = attempt - mapping[key][idx][0] + mapping[key][idx][1]
                break
    return attempt


def main():
    p1_seeds, p2_seeds, puzzle_input = get_input()

    part_1 = part_one(p1_seeds, puzzle_input)
    part_2 = part_two(p2_seeds, puzzle_input)

    print(f"Part One:", part_1)
    print(f"Part Two:", part_2)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()
