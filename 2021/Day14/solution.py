def get_input():
    with open("input") as file_input:
        lines_input = [line.replace('\n', '') for line in
                       file_input.read().split('\n') if line]

    template = lines_input[0]
    insertion_rules = {}
    value_count = {}

    for line in lines_input:
        if "->" in line:
            k, v = (line.replace("\n", "").split(" -> "))

            if k not in insertion_rules:
                insertion_rules[k] = []

            strings = [f"{k[0]}{v}", f"{v}{k[1]}", f"{v}"]

            for string in strings:
                insertion_rules[k].append(string)

    for key in insertion_rules.keys():
        value_count[key] = 0

    return template, insertion_rules, value_count


def initialize_letters(insertion_rules, template):
    letters = {}
    for key in insertion_rules.keys():
        letters[key[0]] = 0

    for letter in template:
        letters[letter] += 1

    return letters


def initialize_insertion_count(value_count, insertion_rules, letters,
                               template):
    for idx in range(len(template) - 1):
        index = template[idx:idx + 2]

        for value in insertion_rules[index]:
            if len(value) != 1:
                value_count[value] += 1
            else:
                letters[value] += 1


def step_through(insertion_rules, value_count, letters):
    part_1 = 0

    for step in range(2, 41):
        values = [v for v in value_count.values()]

        index = 0
        for key in value_count.keys():
            count = values[index]

            value_count[key] -= count
            for value in insertion_rules[key]:
                if len(value) == 2:
                    value_count[value] += count
                else:
                    letters[value] += count

            index += 1

        if step == 10:
            part_1 = max(letters.values()) - min(letters.values())

    part_2 = max(letters.values()) - min(letters.values())

    return part_1, part_2


def build_template(template, insertion_rules, value_count):
    letters = initialize_letters(insertion_rules, template)

    initialize_insertion_count(value_count, insertion_rules, letters,
                               template)

    return step_through(insertion_rules, value_count, letters)


def main():
    template, insertion_rules, value_count = get_input()

    part_1, part_2 = build_template(template, insertion_rules, value_count)

    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()
