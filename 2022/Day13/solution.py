from json import loads
import typing

def get_input():
    with open("input") as file_input:
        input = file_input.read().split('\n\n')

        lines_input = []

        for line in input:
            lines_input.append(line.split('\n'))

    return lines_input


def part_one(file_input):

    master_lists = []
    sorted = 0

    for index, line in enumerate(file_input, 1):
        list_1, list_2 = loads(line[0]), loads(line[1])

        list_sorted = True
        for curr_index in range(len(list_1)):
            if isinstance(list_1[curr_index], int) and isinstance(list_2[curr_index], int):
                if list_1 >= list_2:
                    list_sorted = False
                    break

            elif isinstance(list_1[curr_index], list) and isinstance(list_2[curr_index], list):
                if list_1[curr_index] >= list_2[curr_index]:
                    list_sorted = False
                    break

            elif isinstance(list_1[curr_index], list) and isinstance(list_2[curr_index], int) or isinstance(list_2[curr_index], list) and isinstance(list_1[curr_index], int):
                if list_1[curr_index][0] >= list_2[curr_index]:
                    list_sorted = False
                    break

        if list_sorted:
            print(list_1, list_2, "Sorted")
            sorted += index
        else:
            print(list_1, list_2, "Not sorted")

    return sorted


def main():
    input = get_input()

    part_1 = part_one(input)

    print(f"Part One:", part_1)
    # print(f"Part Two:", part_2)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc

        print_exc()
