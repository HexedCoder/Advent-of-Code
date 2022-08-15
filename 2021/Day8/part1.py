
def get_input():
    with open("input.txt") as file_input:
        input_lines = file_input.readlines()

    output_values = []

    for line in input_lines:
        line = line[line.index("|") + 1:]
        line = line.split()
        output_values.append(line)

    return output_values


def check_unique(values):
    unique_nums = [2, 3, 4, 7]
    all_values = [value for value_list in values for value in value_list]
    unique_value_list = []

    for value in all_values:
        if len(value) in unique_nums:
            unique_value_list.append(value)

    return unique_value_list


def main():
    output_values = get_input()
    unique_nums = check_unique(output_values)

    print("Unique Values:", len(unique_nums))


if __name__ == "__main__":
    main()