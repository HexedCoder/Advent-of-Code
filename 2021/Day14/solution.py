def get_input():
    with open("input") as input:
        lines_input = [line for line in (l.strip() for l in input) if line]

    template = lines_input[0]
    rules = {}
    value_count = {}

    for line in lines_input:
        if "->" in line:
            k, v = (line.replace("\n", "").split(" -> "))

            if k not in rules:
                rules[k] = []

            strings = [f"{k[0]}{v}", f"{v}{k[1]}", f"{v}"]

            for string in strings:
                rules[k].append(string)

    for key in rules.keys():
        value_count[key] = 0

    return template, rules, value_count


def init_letters(rules, template):
    letters = {}

    for key in rules.keys():
        letters[key[0]] = 0

    for letter in template:
        letters[letter] += 1

    return letters


def init_insert_count(value_count, rules, letters, template):

    for idx in range(len(template) - 1):
        index = template[idx:idx + 2]

        for value in rules[index]:
            if len(value) != 1:
                value_count[value] += 1
            else:
                letters[value] += 1


def step_through(rules, value_count, letters):
    part_1 = 0

    for step in range(2, 41):
        values = [v for v in value_count.values()]

        index = 0
        for key in value_count.keys():
            count = values[index]

            value_count[key] -= count

            for value in rules[key]:
                if len(value) == 2:
                    value_count[value] += count
                else:
                    letters[value] += count

            index += 1

        if step == 10:
            part_1 = max(letters.values()) - min(letters.values())

    part_2 = max(letters.values()) - min(letters.values())

    return part_1, part_2


def main():
    template, rules, value_count = get_input()
    letters = init_letters(rules, template)
    init_insert_count(value_count, rules, letters, template)
    part_1, part_2 = step_through(rules, value_count, letters)

    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()
