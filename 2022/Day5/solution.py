import copy


def get_input():
    text_file = open("input", "r").read().split("\n")

    stacks = []
    rules = []
    idx = 0

    for line in text_file:
        if '1' == line.split()[0]:
            num_stacks = len(line.split())
            for num in range(num_stacks):
                stack = []
                stacks.append(stack)
            break
        idx += 1

    for line in text_file:
        if '1' == line.split()[0]:
            break

        idx = 0
        for num in range(1, len(line) - 1, 4):
            if ' ' != line[num]:
                stacks[idx].append(line[num])
            idx += 1

    for line in text_file:
        line = line.split()
        if line and 'move' == line[0]:
            rules.append([int(line[1]), int(line[3]) - 1, int(line[5]) - 1])

    return stacks, rules


def main():
    stacks, rules = get_input()

    stack_2 = copy.deepcopy(stacks)
    output_1 = part_one(stacks, rules)
    print("Part 1:", end=" ")
    print_data(output_1)

    output_2 = part_two(stack_2, rules)
    print("Part 2:", end=" ")
    print_data(output_2)


def print_data(output_1):
    for stack in output_1:
        print(stack[-1], end='')
    print()


def part_one(stacks, rules):

    for stack in stacks:
        stack.reverse()

    for rule in rules:
        for _ in range(rule[0]):
            element = stacks[rule[1]].pop()
            stacks[rule[2]].append(element)

    return stacks


def part_two(stacks, rules):

    for stack in stacks:
        stack.reverse()

    for rule in rules:
        tmp_stack = []
        for _ in range(rule[0]):
            element = stacks[rule[1]].pop()
            tmp_stack.append(element)
        for _ in range(rule[0]):
            element = tmp_stack.pop()
            stacks[rule[2]].append(element)

    return stacks


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()
