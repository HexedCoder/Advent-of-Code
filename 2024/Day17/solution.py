def get_input():
    with open("input", "r") as file:
        register_vals, instructions = file.read().split("\n\n")

    register_vals = [int(line.split(": ")[1]) for line in register_vals.split("\n")]
    instructions = list(map(int, instructions.split(" ")[1].split(",")))
    
    return (register_vals, instructions)

def part_one(input_data):
    register_vals, instructions = input_data
    A, B, C = register_vals
    output = ""
    i = 0
    while i < len(instructions):
        opcode = instructions[i]
        operand = instructions[i + 1]
        if opcode in (0, 2, 5, 6, 7):
            match operand:
                case 4:
                    operand = A
                case 5:
                    operand = B
                case 6:
                    operand = C
                case 7:
                    operand = -1
                            
        if opcode == 0:
            A //= (2 ** operand)

        elif opcode == 1:
            B ^= operand

        elif opcode == 2:
            B = operand % 8

        if opcode == 3:
            if A != 0:
                i = operand
                continue

        elif opcode == 4:
            B ^= C

        elif opcode == 5:
            output += f"{operand % 8},"

        elif opcode == 6:
            B = A // (2 ** operand)

        elif opcode == 7:
            C = A // (2 ** operand)

        i += 2

    return output[:-1]

def part_two(input_data):
    register_vals, instructions = input_data
    A, B, C = register_vals
    offset = 0o756104632
    
    for output in range(1_000_000): 
        A = (output * 2**27) + offset

        output_list = []
        i = 0
        cmp_idx = 0

        while i < len(instructions):
            opcode = instructions[i]
            operand = instructions[i + 1]
            if opcode in (0, 2, 5, 6, 7):
                match operand:
                    case 4:
                        operand = A
                    case 5:
                        operand = B
                    case 6:
                        operand = C

            if opcode == 0:
                A //= (2 ** operand)

            elif opcode == 1:
                B ^= operand

            elif opcode == 2:
                B = operand % 8

            if opcode == 3:
                if A != 0:
                    i = operand
                    continue

            elif opcode == 4:
                B ^= C

            elif opcode == 5:
                output_list.append(operand % 8)
                if instructions[cmp_idx] != output_list[-1]:
                    break

                cmp_idx += 1
                if cmp_idx == len(instructions):
                    break

            elif opcode == 6:
                B = A // (2 ** operand)

            elif opcode == 7:
                C = A // (2 ** operand)

            i += 2
        
        if instructions == output_list:
            return (output * 2**27) + offset

def main():

    input_data = get_input()

    part_1 = part_one(input_data)
    print(f"Part One:", part_1)

    part_2 = part_two(input_data)
    print(f"Part Two:", part_2)

if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception):
        print("Exiting...")