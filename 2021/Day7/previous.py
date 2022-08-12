def get_input():
    with open("input.txt") as file_input:
        line_input = file_input.read().split(",")

    return line_input


def build_array(input_list):
    cost_list = []
    input_list = [int(x) for x in input_list]
    min_number = min(input_list)
    max_number = max(input_list)

    for step in range(min_number, max_number + 1):
        total_fuel = 0
        for crab in input_list:
            move = 1

            steps = abs(crab - step)
            total_fuel += sum([moves*move for moves in range(steps+1)])

            move += 1

        cost_list.append(total_fuel)

    return cost_list


def main():
    crab_list = get_input()
    calc_movement = build_array(crab_list)

    print("Lowest fuel cost:", min(calc_movement))


if __name__ == "__main__":
    main()