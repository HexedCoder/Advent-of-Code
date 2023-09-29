from collections import defaultdict

graph = []

def extract_value(string):
    return map(int, string.split("=")[1].split(".."))


def get_input():
    with open("input") as file:
        x_range, y_range = file.readline().strip().split(": ")[1].split(", ")

    x_lower, x_upper = extract_value(x_range)
    y_lower, y_upper = extract_value(y_range)

    return [x_lower, y_lower, x_upper, y_upper]


def main():
    input_data = get_input()

    output = check_impacts(input_data)
    print("Part 1:", output[0])
    print("Part 2:", output[1])


def check_impact(input_ranges, check_pos):
    x_lower, y_lower, x_upper, y_upper = input_ranges
    x_velo, y_velo = check_pos

    step = 0
    x, y = (0, 0)
    max_y = 0

    while True:
        if step > 0:
            if x_velo > 0:
                x_velo -= 1
            elif x_velo < 0:
                x_velo += 1
            else:
                x_velo = 0
            y_velo -= 1

        x += x_velo
        y += y_velo

        if y > max_y:
            max_y = y
        

        if x < -15000 or x > x_upper:
            break
        if y < y_lower or y > 15000:
            break
        if x_lower <= x <= x_upper and y_lower <= y <= y_upper:
            return max_y

        step += 1

    return None


def check_impacts(input_ranges):
    x_upper = input_ranges[2]

    max_impact = -10000
    impact_count = 0

    for x_velocity in range(x_upper + 1):
        for y_velocity in range(-15000, 15000):
            hit = check_impact(input_ranges, (x_velocity, y_velocity))
            if hit != None:
                impact_count += 1
                if hit > max_impact:
                    max_impact = hit

    return max_impact, impact_count


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc

        print_exc()
