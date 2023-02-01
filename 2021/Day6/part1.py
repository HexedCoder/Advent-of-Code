def get_input():
    with open('input') as file_input:
        line_input = file_input.read().split(",")

    return line_input


def build_array(file_input):
    fish_list = [0] * 9

    for fish_count in file_input:
        fish_count = int(fish_count)
        fish_list[fish_count] += 1

    return fish_list


def progress(current_fish):
    part_one = 0
    days = 256

    for day in range(0, days):
        index = 0
        saved = 0

        if day == 80:
            part_one = sum(current_fish)

        for timer in current_fish:
            if index == 0:
                saved = current_fish[0]
                current_fish[0] = 0
            else:
                if index == 6 or index == 8:
                    current_fish[index - 1] += current_fish[index]
                    current_fish[index] = saved
                else:
                    current_fish[index - 1] += timer
                    current_fish[index] = 0

            index += 1


    return part_one, sum(current_fish)


def main():
    fish = get_input()
    current_fish = build_array(fish)

    part_one, part_two = progress(current_fish)

    print("Part 1:", part_one)
    print("Part 2:", part_two)


if __name__ == "__main__":
    main()
