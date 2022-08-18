def get_input():
    with open("input.txt") as file_input:
        lines_input = file_input.readlines()

    return lines_input


def find_matches(symbol_list):
    return "Junk"


def main():
    symbol_lines = get_input()
    mismatched_symbol = ""
    for line in symbol_lines:
        print(line)
        mismatched_symbol = find_matches(line)

    print("Total Points:", mismatched_symbol)


if __name__ == "__main__":
    main()
