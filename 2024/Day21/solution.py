def get_input():
    with open("input", "r") as file:
        file_input = file.read().split("\n")
    return file_input

def generate_presses(layer, key_sequence, leg_lengths):
    total_presses = 0
    for i in range(len(key_sequence)):
        start_key = key_sequence[i - 1] if i > 0 else 'A'
        end_key = key_sequence[i]
        total_presses += leg_lengths[(layer, start_key, end_key)]
    return total_presses

def calculate_layers(code, num_keyboards):
    directional_pad = [" ^A", "<v>"]
    numeric_pad = ["789", "456", "123", " 0A"]
    pad_coords = {key: (x, y) for y, row in enumerate(directional_pad) for x, key in enumerate(row)}    
    leg_lengths = {(0, start_key, end_key): 1 for start_key in pad_coords for end_key in pad_coords}
    
    output = 0
    for layer in range(1, num_keyboards + 1):
        if layer == num_keyboards:
            pad_coords = {key: (x, y) for y, row in enumerate(numeric_pad) for x, key in enumerate(row)}

        for start_key, (start_x, start_y) in pad_coords.items():
            for end_key, (end_x, end_y) in pad_coords.items():
                if end_x > start_x:
                    horizontal_movement = '>' * (end_x - start_x)
                else:
                    horizontal_movement = '<' * (start_x - end_x)
                
                if end_y < start_y:
                    vertical_movement = '^' * (start_y - end_y)
                else:
                    vertical_movement = 'v' * (end_y - start_y)

                option1 = None
                option2 = None

                if (end_x, start_y) != pad_coords[' ']:
                    option1 = generate_presses(layer - 1, horizontal_movement + vertical_movement + 'A', leg_lengths)

                if (start_x, end_y) != pad_coords[' ']:
                    option2 = generate_presses(layer - 1, vertical_movement + horizontal_movement + 'A', leg_lengths)

                if option1 and option2:
                    leg_lengths[(layer, start_key, end_key)] = min(option1, option2)
                elif option1:
                    leg_lengths[(layer, start_key, end_key)] = option1
                else:
                    leg_lengths[(layer, start_key, end_key)] = option2

    output += generate_presses(num_keyboards, code, leg_lengths)
    return output

def solve(input_data, num_keyboards):
    total_complexity = 0

    for code in input_data:
        sequence_length = calculate_layers(code, num_keyboards)
        total_complexity += sequence_length * int(code[:-1])

    return total_complexity

def main():
    input_data = get_input()

    part_1 = solve(input_data, 3)    
    print(f"Part One: {part_1}")

    part_2 = solve(input_data, 26)
    print(f"Part Two: {part_2}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
