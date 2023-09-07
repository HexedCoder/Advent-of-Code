with open('input') as file:
    # Sample - 110000000001
    lines = file.readlines()

oxygen_lines = [line.replace("\n", "") for line in lines]
co2_lines = [line.replace("\n", "") for line in lines]


def get_input():
    with open('input', "r") as file:
        # Sample - 110000000001
        lines = file.readlines()

    return lines


def create_dict(lines):
    count_dict = {}
    for number in range(1, 13):
        count_dict[number] = 0

    for line in lines:
        line = line.replace("\n", "")
        number = 1
        for bit in line:
            bit = int(bit)
            if bit == 0:
                count_dict[number] += 1
            number += 1

    return count_dict


def check_power(count_dict):
    gamma_rate = ''
    epsilon_rate = ''
    for zero_count in count_dict.values():
        gamma_rate += '1' if zero_count > 500 else '0'
        epsilon_rate += '0' if zero_count > 500 else '1'

    return int(gamma_rate, base=2) * int(epsilon_rate, base=2)


def oxygen_generator_check():
    high_list = []
    low_list = []
    oxygen_generator_rating = 0
    for index_ in range(0, 12):

        for _line in oxygen_lines:

            low_list.append(_line) if _line[index_] == "0" \
                else high_list.append(_line)

        if len(low_list) < len(high_list) + 1:
            for low_num in low_list:
                oxygen_lines.pop(oxygen_lines.index(low_num))
        else:
            for num in high_list:
                oxygen_lines.pop(oxygen_lines.index(num))
        high_list = []
        low_list = []

        if len(oxygen_lines) == 1:
            oxygen_generator_rating = int(oxygen_lines[0], base=2)
            break
    return oxygen_generator_rating


def co2_scrubber_check():
    high_list = []
    low_list = []
    co2_scrubber_rating = 0
    for index_ in range(0, 12):

        for _line in co2_lines:

            if _line[index_] == "0":
                low_list.append(_line)
            else:
                high_list.append(_line)

        if len(low_list) <= len(high_list):
            for high_num in high_list:
                co2_lines.pop(co2_lines.index(high_num))
        else:
            for num in low_list:
                co2_lines.pop(co2_lines.index(num))
        high_list = []
        low_list = []

        if len(co2_lines) == 1:
            co2_scrubber_rating = int(co2_lines[0], base=2)
            # print(f'{co2_scrubber_rating = }')
            break
    return co2_scrubber_rating


def main():
    # Part 1
    text_file = get_input()
    user_dict = create_dict(text_file)
    power_consumption = check_power(user_dict)

    # Part 2
    oxygen_generator_rating = oxygen_generator_check()
    co2_scrubber_rating = co2_scrubber_check()

    life_support_rating = oxygen_generator_rating * co2_scrubber_rating

    print(f'Part 1: {power_consumption}')
    print(f'Part 2: {life_support_rating}')


if __name__ == "__main__":
    main()
