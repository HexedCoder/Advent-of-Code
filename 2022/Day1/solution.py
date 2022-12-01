def get_input():
    text_file = open("input.txt", "r").read().split("\n")
    return text_file


def main():
    text_file = get_input()
    loads = []

    curr = 0
    for line in text_file:
        if line == '':
            loads.append(curr)
            curr = 0
        else:
            curr += int(line)

    loads.sort(reverse=True)
    print(loads)

    loads = [loads[num] for num in range(3)]

    print("Part 1: ", loads[0])
    print("Part 2: ", sum(loads))


if __name__ == "__main__":
    main()
