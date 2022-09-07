def get_input():
    with open("s_input.txt") as file_input:
        lines_input = file_input.readlines()

    return lines_input


def find_matches(symbol_list):
    return "Junk"


def main():
    open_symbols = ["[", "(", "{", "<", "]", ")", "}", ">"]
    symbol_stack = []
    symbol_lines = get_input()
    mismatched_symbol = []
    index = 0
    for line in symbol_lines:
        symbol_list = []
        if index == 2:
            print(line)
            for symbol in line:
                if symbol != "\n":
                    symbol_stack.append(symbol)
                if symbol in close_symbols:
                    index = close_symbols.index(symbol)
                    try:
                        symbol_stack.reverse()
                        symbol_list.remove(open_symbols[index])
                        symbol_stack.reverse()
                    except ValueError:
                        print("Error")
                        mismatched_symbol.append(symbol)
                elif symbol in open_symbols:
                    symbol_list.append(symbol)

            mismatched_symbol = find_matches(line)
            index += 1
        index += 1

    print(symbol_stack)

    # print("Total Points:", mismatched_symbol)


if __name__ == "__main__":
    main()
