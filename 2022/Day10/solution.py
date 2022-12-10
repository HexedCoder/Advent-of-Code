def get_input():
    text_file = open("input", "r").read().split("\n")
    return text_file


def main():
    text_file = get_input()

    score_1 = part_one(text_file)
    print("Part 1:", score_1)

    score_2 = part_two(text_file)
    print("Part 2:", score_2)


def part_one(text_file):
    contained = 0
    assignment = []

    total = 0
    curr_reg = 0
    for line, val in enumerate(text_file):
        val = val.split()
        if val and 'addx' == val[0]:
            val[1] = int(val[1])
            if curr_reg < 20 <= curr_reg + val[1]:
                print(curr_reg, total)
                total += line * val[1]
            if curr_reg < 60 <= curr_reg + val[1]:
                print(curr_reg, total)
                total += line * val[1]
            if curr_reg < 1000 <= curr_reg + val[1]:
                print(curr_reg, total)
                total += line * val[1]
            if curr_reg < 140 <= curr_reg + val[1]:
                print(curr_reg, total)
                total += line * val[1]
            if curr_reg < 180 <= curr_reg + val[1]:
                print(curr_reg, total)
                total += line * val[1]
            if curr_reg < 220 <= curr_reg + val[1]:
                print(curr_reg, total)
                total += line * val[1]
            curr_reg += val[1]

        # else:
        #     curr_reg += 1

    print(total)

    return contained


def part_two(text_file):
    overlap = 0

    return overlap


if __name__ == "__main__":
    main()
