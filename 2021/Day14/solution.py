def get_input():
    with open("s_input.txt") as file_input:
        lines_input = file_input.readlines()

    polymer_template = lines_input[0].replace("\n", "")

    insertion_rules = {}

    for line in lines_input:
        if "->" in line:
            line = (line.replace("\n", "").split(" -> "))
            insertion_rules[line[0]] = line[1]

    return polymer_template, insertion_rules


def main():
    polymer_template, insertion_rules = get_input()

    count = 10
    new_template = get_template(insertion_rules, polymer_template, count)
    min, max = get_count(new_template)
    print("Part One:", max - min)
    print()

    count = 20
    new_template = get_template(insertion_rules, polymer_template, count)
    min, max = get_count(new_template)
    print("Part Two:", max - min)


def get_count(new_template):
    letter_dict = {}
    for char in new_template:
        if char not in letter_dict:
            letter_dict[char] = 1
        else:
            letter_dict[char] += 1

    return min(letter_dict.values()), max(letter_dict.values())


def get_template(insertion_rules, polymer_template, iter_count):
    new_template = ""
    for step in range(1, iter_count + 1):
        new_template = ""
        previous_char = ""
        for char in polymer_template:
            if previous_char == "":
                previous_char = char
                continue

            curr = f"{previous_char}{char}"
            new_char = insertion_rules[curr]

            new_template = f"{new_template}{previous_char}{new_char}"

            previous_char = char

        new_template = f"{new_template}{previous_char}"
        print("Step", step)

        polymer_template = new_template
    return new_template


if __name__ == "__main__":
    main()
