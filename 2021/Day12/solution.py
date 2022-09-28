cave_dict = {}
lap_count = 0


def get_input():
    with open("input.txt") as file_input:
        lines_input = file_input.readlines()

    return lines_input


def make_dict(file_input):
    global cave_dict
    for line in file_input:
        line = line.replace("\n", "").split("-")
        if line[0] not in cave_dict.keys():
            cave_dict[line[0]] = []
        if line[1] not in cave_dict.keys():
            cave_dict[line[1]] = []
        cave_dict[line[0]].append(line[1])
        cave_dict[line[1]].append(line[0])


def dfs(current_vertex, track, small_caves, part_2):
    global cave_dict
    global lap_count
    track = f"{track} {current_vertex}"

    if current_vertex != "end":
        for vertex in cave_dict[current_vertex]:
            if vertex in cave_dict.keys():
                if vertex != "start":
                    if part_2:
                        if vertex not in track or vertex.isupper():
                            dfs(vertex, track, small_caves, 1)
                        elif small_caves == 0:
                            dfs(vertex, track, small_caves + 1, 1)
                    else:
                        if vertex not in track or vertex.isupper():
                            dfs(vertex, track, small_caves, 0)

    else:
        lap_count += 1


def main():
    global lap_count

    file_input = get_input()
    make_dict(file_input)

    dfs("start", "", 0, False)
    print("Part One:", lap_count)

    lap_count = 0

    dfs("start", "", 0, 1)
    print("Part Two", lap_count)


if __name__ == "__main__":
    main()
