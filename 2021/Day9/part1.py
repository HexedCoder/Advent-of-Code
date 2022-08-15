def get_input():
    with open("input.txt") as file_input:
        lines_input = file_input.readlines()

    return lines_input


def find_lows(height_list):
    for height in height_list:
        print(height)
        return height


def main():
    height_map = get_input()
    risk_levels = find_lows(height_map)

    print("Risk Level:", risk_levels)


if __name__ == "__main__":
    main()
