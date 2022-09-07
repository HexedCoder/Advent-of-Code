def get_input():
    with open("input.txt") as file_input:
        lines_input = file_input.readlines()

    return lines_input


def main():
    part_1()
    part_2()


def part_1():
    symbol_lines = get_input()
    potential_list = ["{", "(", "[", "<", "}", ")", "]", ">"]
    mismatched_total = 0
    bad_symbol = []
    for line in symbol_lines:
        symbol_list = []
        line = line.replace("\n", "")

        for symbol in line:
            if potential_list.index(symbol) < 4:
                symbol_list.append(symbol)
            else:
                compare_symbol = symbol_list.pop()

                if potential_list[
                    potential_list.index(compare_symbol) + 4] != symbol:
                    bad_symbol.append(symbol)
    for symbol in bad_symbol:
        if symbol == ")":
            mismatched_total += 3
        if symbol == "]":
            mismatched_total += 57
        if symbol == "}":
            mismatched_total += 1197
        if symbol == ">":
            mismatched_total += 25137
    print("Part 1:", mismatched_total)


def part_2():
    symbol_lines = get_input()
    potential_list = ["{", "(", "[", "<", "}", ")", "]", ">"]
    mismatched_lines = []
    for line in symbol_lines:
        symbol_list = []
        line = line.replace("\n", "")
        mismatched_total = 0

        index = 0
        for symbol in line:
            if potential_list.index(symbol) < 4:
                symbol_list.append(symbol)
            else:
                compare_symbol = symbol_list.pop()

                if potential_list[potential_list.index(compare_symbol) + 4] != symbol:
                    break

            if index == len(line) - 1:
                for rem_symbol in symbol_list[::-1]:
                    mismatched_total *= 5
                    needed_symbol = potential_list[potential_list.index(rem_symbol) + 4]
                    if needed_symbol == ")":
                        mismatched_total += 1
                    if needed_symbol == "]":
                        mismatched_total += 2
                    if needed_symbol == "}":
                        mismatched_total += 3
                    if needed_symbol == ">":
                        mismatched_total += 4

            index += 1
        if mismatched_total > 0:
            mismatched_lines.append(mismatched_total)
    mismatched_lines.sort()
    middle_index = int((len(mismatched_lines) / 2) + .5)
    print("Part 2:", mismatched_lines[middle_index - 1])


if __name__ == "__main__":
    main()