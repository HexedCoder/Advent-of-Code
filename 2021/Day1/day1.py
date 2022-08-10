def main():
    text_file = open("input.txt", "r").read().split("\n")

    previous = 0
    current = 0
    line_count = 0
    increase_count = 0
    for line in text_file:
        line = int(line)
        if line_count == 0:
            current = line
            line_count += 1

        previous = current
        current = line
        if current > previous:
            increase_count += 1

    print(increase_count)


# def main():
#     text_file = open("input.txt", "r")
#     data = [int(line[:-1]) for line in text_file]
#     count = 0
#     for first, second in zip(data[:-1], data[1:]):
#         if first < second:
#             count += 1
#
#     print(count)


if __name__ == "__main__":
    main()