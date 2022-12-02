def get_input():
    text_file = open("input", "r").read().split("\n")
    return text_file


def main():
    text_file = get_input()
    # Rock, Paper, Scissors
    opp = {'A': 1, 'B': 2, 'C': 3}
    me = {'X': 1, 'Y': 2, 'Z': 3}

    score_1 = part_one(me, opp, text_file)
    score_2 = part_two(me, opp, text_file)

    print("Part 1:", score_1)
    print("Part 2:", score_2)


def part_one(me, opp, text_file):
    score = 0

    for line in text_file:
        line = line.split(" ")

        score += me[line[1]]

        if opp[line[0]] == me[line[1]]:
            score += 3
        elif opp[line[0]] == me[line[1]] - 1 or opp[line[0]] == me[line[1]] + 2:
            score += 6

    return score


def part_two(me, opp, text_file):
    score = 0

    for line in text_file:
        line = line.split(" ")

        if 1 == me[line[1]]:

            if opp[line[0]] == 1:
                score += opp[line[0]]
            elif opp[line[0]] == 2:
                score += 1
            else:
                score += 2

        elif 2 == me[line[1]]:
            score += opp[line[0]] + 3

        elif 3 == me[line[1]]:

            score += 6

            if opp[line[0]] == 1:
                score += 2
            elif opp[line[0]] == 2:
                score += 3
            else:
                score += 1

    return score


if __name__ == "__main__":
    main()
