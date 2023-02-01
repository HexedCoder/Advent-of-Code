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
    final_list = []
    for zero_count in count_dict.values():
        if zero_count > 500:
            final_list.append(0)
        else:
            final_list.append(1)

    gamma_rate = ""

    for number in final_list:
        gamma_rate = f"{gamma_rate}{number}"

    epsilon_rate = ''.join('1' if x == '0' else '0' for x in gamma_rate)

    gamma_rate = int(gamma_rate, base=2)
    epsilon_rate = int(epsilon_rate, base=2)
    power_consumption = gamma_rate * epsilon_rate

    return power_consumption


def oxygen_generator_check():
    high_list = []
    low_list = []
    oxygen_generator_rating = 0
    for index_ in range(0, 12):

        for _line in oxygen_lines:

            if _line[index_] == "0":
                low_list.append(_line)
            else:
                high_list.append(_line)

        if len(low_list) <= len(high_list):
            for low_num in low_list:
                oxygen_lines.pop(oxygen_lines.index(low_num))
        else:
            for num in high_list:
                oxygen_lines.pop(oxygen_lines.index(num))
        high_list = []
        low_list = []

        if len(oxygen_lines) == 1:
            oxygen_generator_rating = int(oxygen_lines[0], base=2)
            # print(f'{oxygen_generator_rating = }')
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
