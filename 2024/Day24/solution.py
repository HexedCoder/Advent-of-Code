def get_input():
    with open("input", "r") as file:
        wire_input, gate_input = file.read().split('\n\n')

    wire_input = wire_input.strip().split('\n')
    links = {}
    for wire in wire_input:
        wire_name, value = wire.split(': ')
        links[wire_name] = int(value)

    gate_input = gate_input.strip().split('\n')
    gates = []
    for gate in gate_input:
        gates.append(gate)

    return links, gates


def process_gates(links, gates):
    unresolved = gates[:]
    while unresolved:
        next_unresolved = []
        for gate in unresolved:
            parts = gate.split(' -> ')
            operation, output_wire = parts
            if ' AND ' in operation:
                inputs = operation.split(' AND ')
                operator = '&'
            elif ' OR ' in operation:
                inputs = operation.split(' OR ')
                operator = '|'
            elif ' XOR ' in operation:
                inputs = operation.split(' XOR ')
                operator = '^'

            resolved_inputs = []
            all_resolved = True
            for input_wire in inputs:
                if input_wire in links:
                    resolved_inputs.append(links[input_wire])
                else:
                    all_resolved = False
                    break

            if all_resolved:
                links[output_wire] = compute(resolved_inputs, operator)
            else:
                next_unresolved.append(gate)

        unresolved = next_unresolved

    return links

def compute(inputs, operator):
    val1, val2 = inputs
    if operator == '&':
        return val1 & val2
    elif operator == '|':
        return val1 | val2
    elif operator == '^':
        return val1 ^ val2
    return None

def swap_keys(value_1, value_2, gates, reverse_gates):
    temp = reverse_gates[value_1]
    reverse_gates[value_1] = reverse_gates[value_2]
    reverse_gates[value_2] = temp

    temp = gates[reverse_gates[value_1]]
    gates[reverse_gates[value_1]] = gates[reverse_gates[value_2]]
    gates[reverse_gates[value_2]] = temp


def build_dicts(gates_input):
    gates = {}
    reverse_gates = {}
    for line in gates_input:
        gate_info, result = line.split(" -> ")
        
        gate_1, operator, gate_2 = gate_info.split()
        if gate_1 <= gate_2:
            gate_1, gate_2 = gate_1, gate_2
        else:
            gate_1, gate_2 = gate_2, gate_1

        operator = operator[0].replace('A', '&').replace('O', '|').replace('X', '^')
        gates[(gate_1, gate_2, operator)] = result
        reverse_gates[result] = (gate_1, gate_2, operator)

    return (gates, reverse_gates)

# https://circuitfever.com/full-adder-verilog-code shows the carry concept
def part_two(gates_input):
    gates, reverse_gates = build_dicts(gates_input)
    invalid_gates = set()

    iterations = int(max(reverse_gates)[1:])
    for idx in range(iterations):
        curr_x = f'x{idx:02}'
        curr_y = f'y{idx:02}'
        curr_z = f'z{idx:02}'
        xor_val = gates[(curr_x, curr_y, '^')]
        and_val = gates[(curr_x, curr_y, '&')]
        if 0 == idx:
            carry = and_val
        else:
            swap_val_1 = None
            swap_val_2 = None

            smaller_wire, larger_wire = (carry, xor_val) if carry < xor_val else (xor_val, carry)
            xor_key = smaller_wire, larger_wire, '^'
            if xor_key not in gates:               
                for wire in reverse_gates[curr_z]:
                    if wire not in xor_key:
                        smaller_wire = wire
                        break
                for wire in xor_key:
                    if wire not in reverse_gates[curr_z]:
                        larger_wire = wire
                        break

                invalid_gates.add(smaller_wire)
                swap_val_1 = smaller_wire

                invalid_gates.add(larger_wire)
                swap_val_2 = larger_wire
            elif gates[xor_key] != curr_z:
                swap_val_1 = curr_z
                invalid_gates.add(curr_z)

                swap_val_2 = gates[xor_key]
                invalid_gates.add(gates[xor_key])
            
            if swap_val_1 and swap_val_2:
                swap_keys(swap_val_1, swap_val_2, gates, reverse_gates)

            xor_val = gates[(curr_x, curr_y, '^')]
            carry_and = (carry, xor_val, '&') if carry < xor_val else (xor_val, carry, '&')
            carry = gates[carry_and]

            and_val = gates[(curr_x, curr_y, '&')]
            carry_or = (carry, and_val, '|') if carry < and_val else (and_val, carry, '|')
            carry = gates[carry_or]

    return ','.join(sorted(invalid_gates))

def part_one(links):
    output = ""
    sorted_links = [val for key, val in sorted(links.items(), reverse=True) if key[0] == 'z']
    for val in sorted_links:
        output = f"{output}{val}"
    return int(output, 2)

def main():
    links, gates = get_input()
    links = process_gates(links, gates)

    part_1 = part_one(links)
    print(f"Part One: {part_1}")

    part_2 = part_two(gates)
    print(f"Part Two: {part_2}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
