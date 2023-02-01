def get_input():
    with open("input") as file_input:
        line_input = file_input.read().split(",")

    line_input = [int(x) for x in line_input]

    return line_input


def check_fuel(input_list):
    # stores the fuel required to move to each value
    index_cost_list = []

    min_number = min(input_list)
    max_number = max(input_list)

    step_array = fuel_cost_list(max_number)

    for step in range(min_number, max_number + 1):
        total_fuel = 0
        for crab in input_list:

            steps = abs(crab - step)
            if steps != 0:
                total_fuel += step_array[steps - 1]

        index_cost_list.append(total_fuel)

    return index_cost_list


def fuel_cost_list(max_number):
    step_array = []
    total_fuel = 0

    for extra_fuel in range(1, max_number + 1):
        total_fuel += extra_fuel
        step_array.append(total_fuel)

    return step_array


def main():
    crab_list = get_input()
    calc_movement_list = check_fuel(crab_list)

    print("Lowest fuel cost:", min(calc_movement_list))


if __name__ == "__main__":
    main()
