import heapq

def get_input():
    with open("input") as file_input:
        input = [row.split() for row in file_input.read().split("\n")]

    return input


def part_one(file_input):

    start = 0
    adj_list = {}
    for idx, line in enumerate(file_input):
        vert = line[1]
        rate = line[4].split("=")[1][:-1]
        valves = line[9:]
        valves = [valve.replace(",", "") for valve in valves]

        if idx == 0:
            start = vert

        adj_list[vert] = [valves]
        adj_list[vert].append(rate)

    print(adj_list)
    distance(adj_list, start)

    return 0


def distance(grid, start):

    flow = 0
    print(grid[start][0])
    queue = [start]
    heapq.heappush(queue, (0, 0, 0))
    visited = {start}

    while queue:
        curr = heapq.heappop(queue)

        print(curr)
        # for neighbor in curr[1]:
        #     pass
            # if 0 <= neighbor[0] < rows and 0 <= neighbor[
            #     1] < cols and 0 <= curr_row < rows and 0 <= curr_column < cols:
            #
            #     weight = weights[neighbor[0]][neighbor[1]]
            #
            #     if weight + distance < grid[neighbor[0]][neighbor[1]]:
            #         grid[neighbor[0]][neighbor[1]] = distance + weight
            #
            #         heapq.heappush(queue, (
            #             weight + distance, neighbor[0], neighbor[1]))
            #         visited.add((curr_row, curr_column))

    return flow


def main():
    input = get_input()

    part_1 = part_one(input)

    print(f"Part One:", part_1)
    # print(f"Part Two:", part_2)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc

        print_exc()
