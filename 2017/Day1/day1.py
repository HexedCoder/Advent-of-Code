def get_input():
    text_file = open("input", "r").read().split()
    return text_file


def main():
    text_file = get_input()

    total = 0
    curr = 0

    for line in text_file:
        for num in line:
            num = int(num)
            prev = curr
            curr = num

            if prev == curr:
                total += num

        if curr == int(line[0]):
            total += curr

    print("Part 1:", total)

    total = 0
    idx = 0

    for line in text_file:
        index = int(len(line)/2)

        for num in line:
            num = int(num)
            cmp = int(line[idx - index])

            if num == cmp:
                total += num

            idx += 1

    print("Part 2:", total)


if __name__ == "__main__":
    main()
