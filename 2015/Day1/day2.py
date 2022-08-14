def get_input():
    text_file = open("input.txt", "r").read().split("\n")
    return text_file


def main():
    text_file = get_input()
    increase_count = check_increase(text_file)

    print(increase_count)


def check_increase(lines):
    current = 0
    line_count = 0
    increase_count = 0
    sum_list = []
    for _ in lines:
        if line_count < len(lines) - 2:
            line_sum = int(lines[line_count]) + int(lines[line_count + 1]) + \
                       int(lines[line_count + 2])
            sum_list.append(line_sum)
            line_count += 1

    line_count = 0
    for cur_sum in sum_list:
        cur_sum = int(cur_sum)
        if line_count == 0:
            current = cur_sum
            line_count += 1
            continue
        previous = current
        current = cur_sum
        if current > previous:
            increase_count += 1
    return increase_count


if __name__ == "__main__":
    main()