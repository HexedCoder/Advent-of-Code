width = 0
bottom = 0
_map = []


def get_input():
    with open("input.txt") as file_input:
        lines_input = file_input.readlines()

    list_int_input = []

    for line in lines_input:

        line = line.replace("\n", "")
        line_int = []

        for num in line:
            num = int(num)
            line_int.append(num)
        list_int_input.append(line_int)

    return list_int_input


def main():
    cavern_graph = get_input()
    for line in cavern_graph:
        for num in line:
            print(num, end=" ")
        print()


if __name__ == "__main__":
    main()
