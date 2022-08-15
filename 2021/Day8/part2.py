index = 1


def get_input():
    with open("input.txt") as file_input:
        input_lines = file_input.readlines()

    normal_values = []
    output_list = []

    for line in input_lines:
        value_sep_index = line.index("|")

        output = line[value_sep_index + 1:].split()
        output = ["".join(sorted(output, key=lambda k: k)) for output in output]
        output_list.append(output)

        regular_input = line[:value_sep_index].split()
        normal_values.append(regular_input)

    return normal_values, output_list


def get_unique(values):
    new_values = []
    values.sort(key=len)
    for value in values:
        value = sorted(value)
        value = "".join(value)
        new_values.append(value)

    unique_nums = [""].copy() * 10

    # ab: 1
    # abef: 4
    # abd: 7
    # abcdefg: 8

    # bcdef: 5
    # acdfg: 2
    # abcdf: 3  cdf
    # abcdef: 9
    # bcdefg: 6
    # abcdeg: 0 -cdf

    d_value = ""
    ef_value = ""

    for value in new_values:
        if len(value) == 2:  # 1
            unique_nums[1] = value

        if len(value) == 4:  # 4
            unique_nums[4] = value
            for char in value:
                if char not in unique_nums[1]:
                    ef_value += char

        if len(value) == 3:  # 7
            unique_nums[7] = value
            for char in value:
                if char not in unique_nums[1]:
                    d_value = char

        if len(value) == 7:  # 8
            unique_nums[8] = value

        if len(value) == 5:  # 2 / 3 / 5
            is_match = False
            for char in unique_nums[1]:
                if char in value:
                    is_match = True
                else:
                    is_match = False
                    break
            if is_match:
                unique_nums[3] = value
                continue
            for char in ef_value:
                if char in value:
                    is_match = True
                else:
                    is_match = False
                    break
            if is_match:
                unique_nums[5] = value
            else:
                unique_nums[2] = value

        if len(value) == 6:  # 0 / 6 / 9
            is_match = False
            for char in unique_nums[3]:
                if char in value:
                    is_match = True
                else:
                    is_match = False
                    break
            if is_match:
                unique_nums[9] = value
            else:
                is_match = True
                for char in unique_nums[1]:
                    if char in value:
                        is_match = True
                    else:
                        is_match = False
                        break
                if is_match:
                    unique_nums[0] = value
                else:
                    unique_nums[6] = value

    return unique_nums


def get_number(key_list: list, output_values: list):
    global index
    print(index, key_list)
    index += 1
    output_num = ""
    for output_value_list in output_values:
        print(output_value_list)
        output_num += str(key_list.index(output_value_list))
    output_num = int(output_num)

    return output_num


def decipher_nums(output_values_index, normal_values):
    output_value = 0
    initial_breakdown = get_unique(normal_values)

    output_value += get_number(initial_breakdown, output_values_index)

    return output_value


def main():
    normal_values, output_values = get_input()
    new_sum = 0
    for value in range(0, len(normal_values)):
        new_sum += decipher_nums(output_values[value], normal_values[value])
    print()
    print("Final Sum:", new_sum)


if __name__ == "__main__":
    main()