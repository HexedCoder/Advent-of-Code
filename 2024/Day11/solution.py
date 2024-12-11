def get_input():
    graves_input = {}
    with open("input") as file_input:
        file_input = file_input.read().split()

    graves_input = {int(num): file_input.count(num) for num in file_input}
    return graves_input

def blink(current_value):
    if current_value == 0:
        return [1]
    
    str_curr = str(current_value)
    length = len(str_curr)
    
    if length % 2 == 0:
        mid = length // 2
        val_1 = int(str_curr[mid:])
        val_2 = int(str_curr[:mid])
        return [val_1, val_2]
    
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

    return sum(graves_input.values())

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