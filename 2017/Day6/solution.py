import copy
import math


def get_input():
    with open('input') as f:
        registers = list(map(int, f.read().split()))

    return registers


def main():
    registers = get_input()

    result = part_one(registers.copy())
    print(f'Part One: {result[0]}')

    result = part_two(result[1])
    print(f'Part Two: {result}')


def part_one(registers):
    status = []
    state = ''
    iters = 0

    while state not in status:
        if not state:
            state = registers
        status.append(copy.deepcopy(registers))

        max_reg = max(state)
        avg = math.ceil(max_reg / len(state))
        idx = state.index(max_reg)
        state[idx] = 0
        while max_reg > 0:
            idx = (idx + 1) % len(registers)
            state[idx] += avg if max_reg >= avg else max_reg
            max_reg -= avg if max_reg >= avg else max_reg

        iters += 1

    status.append(copy.deepcopy(registers))

    return iters, copy.deepcopy(registers)


def part_two(registers):
    status = []
    state = ''
    iters = 0
    times = 2

    while times > 0:
        if state in status and times > 0:
            times -= 1
            if 0 == times:
                break

        if not state:
            state = registers
        status.append(copy.deepcopy(registers))

        max_reg = max(state)
        avg = math.ceil(max_reg / len(state))
        idx = state.index(max_reg)
        state[idx] = 0
        while max_reg > 0:
            idx = (idx + 1) % len(registers)
            state[idx] += avg if max_reg >= avg else max_reg
            max_reg -= avg if max_reg >= avg else max_reg

        iters += 1

    return iters - 1


if __name__ == "__main__":
    main()
