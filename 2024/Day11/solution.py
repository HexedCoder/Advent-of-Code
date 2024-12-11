def get_input():
    graves_input = {}
    with open("input") as file_input:
        for line in file_input:
            for num in line.split():
                if num not in graves_input:
                    graves_input[int(num)] = 0
                graves_input[int(num)] += 1

    return graves_input

def blink(current_value):
    if current_value == 0:
        return [1]
    elif len(str(current_value)) % 2 == 0:
        str_curr = str(current_value)
        val_1 = int(str_curr[len(str_curr) // 2:])
        val_2 = int(str_curr[:len(str_curr) // 2])
        return [val_1, val_2]
    else:
        return [current_value * 2024]


def solve(graves_input, num):  
    for _ in range(num):
        new_graves = {}
        for key, value in graves_input.items():
            get_vals = blink(key)
            for val in get_vals:
                if val not in new_graves:
                    new_graves[val] = 0
                new_graves[val] += value
        graves_input = new_graves

    output = sum(graves_input[key] for key in graves_input if graves_input[key] > 0)
    return output

def main():

    graves_dict = get_input()

    part_1 = solve(graves_dict, 25)
    print(f"Part One:", part_1)

    part_2 = solve(graves_dict, 75)
    print(f"Part Two:", part_2)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()