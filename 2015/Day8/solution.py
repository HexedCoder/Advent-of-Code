def get_input():
    with open('input') as f:
        file_input = [piece for piece in [line.split('->') for line in f.read().split('\n') if line]]

    return file_input


def main():
    file_input = get_input()

    result = part_one(file_input)
    print(f'Part One: {result}')

    result = part_two(file_input)
    print(f'Part Two: {result}')


def part_one(file_input):
    return 0


def part_two(file_input):
    return 0


if __name__ == "__main__":
    main()
