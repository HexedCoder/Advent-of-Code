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


def compute(inputs, operator):
    val1, val2 = inputs
    if operator == '&':
        return val1 & val2
    elif operator == '|':
        return val1 | val2
    elif operator == '^':
        return val1 ^ val2
    return None


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


def solve(links):
    output = ""
    sorted_links = [val for key, val in sorted(links.items(), reverse=True) if key[0] == 'z']
    for val in sorted_links:
        output = f"{output}{val}"
    return int(output, 2)


def main():
    links, gates = get_input()
    links = process_gates(links, gates)
    part_1 = solve(links)
    print(f"Part One: {part_1}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
