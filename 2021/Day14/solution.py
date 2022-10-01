def get_input():
    with open("input.txt") as file_input:
        lines_input = file_input.readlines()

    polymer_template = lines_input[0].replace("\n", "")

    insertion_rules = {}
    insertion_count = {}

    for line in lines_input:
        if "->" in line:
            line = (line.replace("\n", "").split(" -> "))
            if line[0] not in insertion_rules:
                insertion_rules[line[0]] = []
            string1 = f"{line[0][0]}{line[1]}"
            string2 = f"{line[1]}{line[0][1]}"
            string3 = f"{line[1]}"

            insertion_rules[line[0]].append(string1)
            insertion_rules[line[0]].append(string2)
            insertion_rules[line[0]].append(string3)

    for key in insertion_rules.keys():
        insertion_count[key] = 0

    return polymer_template, insertion_rules, insertion_count


def main():
    polymer_template, insertion_rules, insertion_count = get_input()

    get_template(polymer_template, insertion_rules, insertion_count)


def step_through(insertion_rules, insertion_count, letters):
    for step in range(2, 41):
        values = [value for value in insertion_count.values()]

        index = 0
        for key in insertion_count.keys():
            count = values[index]

            insertion_count[key] -= count
            for value in insertion_rules[key]:
                if len(value) == 2:
                    insertion_count[value] += count
                else:
                    letters[value] += count

            index += 1

        if step == 10:
            minimum = min(letters.values())
            maximum = max(letters.values())
            print("Part 1:", maximum - minimum)
        if step == 40:
            minimum = min(letters.values())
            maximum = max(letters.values())
            print("Part 2:", maximum - minimum)


def get_template(polymer_template, insertion_rules, insertion_count):
    letters = {}

    for key in insertion_rules.keys():
        letters[key[0]] = 0

    for letter in polymer_template:
        letters[letter] += 1

    for current in range(0, len(polymer_template) - 1):
        index = polymer_template[current:current + 2]

        for value in insertion_rules[index]:
            if len(value) != 1:
                insertion_count[value] += 1
            else:
                letters[value] += 1

    step_through(insertion_rules, insertion_count, letters)


if __name__ == "__main__":
    main()
