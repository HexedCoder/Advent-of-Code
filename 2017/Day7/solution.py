import copy
import math


def get_input():
    with open('input') as file:
        programs = file.readlines()

    program_info = []
    supported = []
    for program in programs:

        ending = []
        if '->' in program:
            index = program.index('-')
            initial = program[:index]
            ending = program[index + 2:-1].replace(' ', '').split(',')
            program = initial

        program = program.split()
        if ending:
            program.append(ending)
            supported += ending

        program[1] = int(program[1][1:-1])
        program_info.append(program)
        program_info.sort(key= lambda k: k[1])

    return program_info, supported


def main():
    programs, supported = get_input()

    result = part_one(programs, supported)
    print(f'Part One: {result}')

    result = part_two(programs, supported)
    print(f'Part Two: {result}')


def part_one(programs, supported):

    for program in programs:
        if program[0] not in supported:
            return program[0]


def part_two(programs, supported):

    for program in programs:
        if program[0] not in supported:
            return program[0]


if __name__ == "__main__":
    main()
