def get_input():
    with open('input') as f:
        file_input = [piece for piece in [line.split('->') for line in f.read().split('\n') if line]]

    var_dict = {}
    op_list = []

    for ops, var in file_input:
        var = var.strip()
        try:
            ops = int(ops.strip())
            var_dict[var] = ops
        except ValueError:
            ops = ops.strip().split()
            op_list.append([ops, var])

    for line in op_list:
        if line[1] not in var_dict.keys() and not line[1].isdigit():
            var_dict[line[1]] = 0

    return op_list, var_dict


def main():
    op_list, var_dict = get_input()

    result = part_one(op_list, var_dict)
    print(f'Part One: {result}')

    result = part_two(op_list, var_dict, result)
    print(f'Part Two: {result}')


def part_one(op_list, var_dict):
    for line in op_list:
        if line[1] not in var_dict.keys() and not line[1].isdigit():
            var_dict[line[1]] = 0

    for _ in range(25):
        for cmd in op_list:
            if 1 == len(cmd[0]):
                if cmd[0][0] not in var_dict:
                    var_dict[cmd[0][0]] = 0
                var_dict[cmd[1]] = var_dict[cmd[0][0]]

            elif 3 == len(cmd[0]):
                val_1 = int(cmd[0][0]) if cmd[0][0].isdigit() else var_dict[cmd[0][0]]
                val_2 = int(cmd[0][2]) if cmd[0][2].isdigit() else var_dict[cmd[0][2]]

                if cmd[0][-2] == 'AND':
                    var_dict[cmd[1]] = val_1 & val_2
                if cmd[0][-2] == 'OR':
                    var_dict[cmd[1]] = val_1 | val_2

                if cmd[0][-2] == 'LSHIFT':
                    var_dict[cmd[1]] = val_1 << val_2

                if cmd[0][-2] == 'RSHIFT':
                    var_dict[cmd[1]] = val_1 >> val_2

            else:
                if cmd[0][-2] == 'NOT':
                    var_dict[cmd[1]] = ~var_dict[cmd[0][1]]

    return var_dict['a']


def part_two(op_list, var_dict, part_two_res):
    var_dict['b'] = part_two_res

    return part_one(op_list, var_dict)


if __name__ == "__main__":
    main()
