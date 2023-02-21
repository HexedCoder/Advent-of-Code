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

    return op_list, var_dict


def main():
    op_list, var_dict = get_input()

    result = part_one(op_list, var_dict)
    print(f'Part One: {result}')

    result = part_two(op_list, var_dict)
    print(f'Part Two: {result}')


def part_one(op_list, var_dict):

    curr = ''
    while 'a' not in var_dict:
        try:
            for idx, cmd in enumerate(op_list):
                curr = cmd
                print(cmd)

                if 1 == len(cmd[0]):
                    ops = cmd[0][0]
                    if ops not in var_dict:
                        var_dict[ops] = 0
                    var_dict[cmd[1]] = var_dict[ops]
                    print(ops, var_dict[ops])
                    raise SyntaxError

                else:

                    if cmd[0][-2] == 'AND':
                        if cmd[0][0] in  var_dict and cmd[0][2] in var_dict:
                            var_dict[cmd[1]] = var_dict[cmd[0][0]] & var_dict[cmd[0][2]]
                            raise SyntaxError
                    if cmd[0][-2] == 'OR':
                        if cmd[0][0] in var_dict and cmd[0][2] in var_dict:
                            var_dict[cmd[1]] = var_dict[cmd[0][0]] | var_dict[cmd[0][2]]
                            raise SyntaxError
                    if cmd[0][-2] ==  'LSHIFT':
                        if cmd[0][0] in var_dict and cmd[0][2] in var_dict:
                            var_dict[cmd[1]] = var_dict[cmd[0][0]] << int(cmd[0][2])
                            raise SyntaxError
                    if cmd[0][-2] == 'RSHIFT':
                        if cmd[0][0] in var_dict and cmd[0][2] in var_dict:
                            var_dict[cmd[1]] = var_dict[cmd[0][0]] >> int(cmd[0][2])
                            raise SyntaxError
                    if cmd[0][-2] == 'NOT':
                        if cmd[0][1] in var_dict:
                            var_dict[cmd[1]] = ~ var_dict[cmd[0][1]]
                            raise SyntaxError

        except KeyError:
            item = op_list.index(curr)
            to_add = op_list.pop(item)
            op_list.append(to_add)

        except SyntaxError:
            print('Removing', curr)
            item = op_list.index(curr)
            op_list.pop(item)
            print(len(op_list))

    return var_dict['a']


def part_two(op_list, var_dict):
    pass


if __name__ == "__main__":
    main()
