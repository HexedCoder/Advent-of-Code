def get_input():
    text_file = open("input", "r").read().split("\n")
    return text_file


def main():
    text_file = get_input()
    values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

    score_1 = part_one(values, text_file)
    score_2 = part_two(values, text_file)

    print("Part 1:", score_1)
    print("Part 2:", score_2)


def part_one(values, text_file):
    score = 0

    for line in text_file:
        set_1 = set()
        set_2 = set()
        split = int(len(line) / 2)

        for char in line[:split]:
            set_1.add(char)
        for char in line[split:]:
            set_2.add(char)

        char = list(set_1.intersection(set_2))[0]

        try:
            score += values[char]
        except:
            score += values[char.lower()] + 26

    return score


def part_two(values, text_file):
    lines = []
    line_count = 0
    score = 0

    for line in text_file:
        line_count %= 3
        my_set = set()
        for char in line:
            my_set.add(char)
        if 0 == line_count:
            lines = my_set
        else:
            lines = list(my_set.intersection(lines))
            if 2 == line_count:
                try:
                    score += values[lines[0]]
                except:
                    score += values[lines[0].lower()] + 26

        line_count += 1

    return score


if __name__ == "__main__":
    main()
