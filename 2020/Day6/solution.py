def get_input():
    with open('input') as f:
        my_input = f.read().split('\n\n')

    return my_input


def main():
    file_input = get_input()

    ans = part_one(file_input)
    print("Part 1:", ans)

    ans = part_two(file_input)
    print("Part 2:", ans)


def part_one(file_input):
    return sum([len(set(char for char in ans_list if char != '\n')) for ans_list in file_input])


def part_two(file_input):
    file_input = [set(ans_list.split('\n')) for ans_list in file_input]

    num_yes = []
    for idx, ans_set in enumerate(file_input):
        num_yes.append(len(set.intersection(*[set(s) for s in ans_set])))

    return sum(num_yes)



if __name__ == "__main__":
    main()
