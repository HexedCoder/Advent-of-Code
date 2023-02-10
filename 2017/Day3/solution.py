def get_input():
    text_file = open("input", "r").read()
    return int(text_file)


def main():
    num_input = get_input()

    print('Part 1:', part_one(num_input))
    print('Part 2:', part_two(num_input))


def part_one(num_input):
    num = 0
    iters = 0
    steps = 0
    direction = 1
    reached = False

    start = [0, 0]

    while not reached:
        if iters % 2 == 0:
            num += 1

        for _ in range(num):
            match direction % 4:
                case 0:
                    start[1] -= 1
                case 1:
                    start[0] += 1
                case 2:
                    start[1] += 1
                case 3:
                    start[0] -= 1
            steps += 1
            if steps + 1 == num_input:
                reached = True
                break

        direction += 1
        iters += 1

    return abs(start[0]) + abs(start[1])


def get_distance(curr, previous_list):
    curr_sum = 0
    for item in previous_list:
        dist = abs(curr[0] - item[0]) < 2 and abs(curr[1] - item[1]) < 2
        if 1 == dist:
            curr_sum += previous_list[item]

    return curr_sum


def part_two(num_input):
    prev_list = {(0,0): 1}
    num = 0
    iters = 0
    steps = 0
    direction = 1

    start = [0, 0]

    while True:
        if iters % 2 == 0:
            num += 1

        for _ in range(num):
            match direction % 4:
                case 0:
                    start[1] -= 1
                case 1:
                    start[0] += 1
                case 2:
                    start[1] += 1
                case 3:
                    start[0] -= 1

            dist = get_distance(start, prev_list)
            prev_list[tuple(start)] = dist
            steps += 1
            if dist >= num_input:
                return dist

        direction += 1
        iters += 1


if __name__ == "__main__":
    main()
