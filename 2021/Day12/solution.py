cave_dict = {}
lap_count = 0


def get_input():
    with open("input") as file_input:
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


def dfs(current_vertex, track, small_caves_entered=False, part_2=False):
    global cave_dict
    global lap_count
    track = f"{track} {current_vertex}"

    if current_vertex != "end":
        for vertex in cave_dict[current_vertex]:
            if vertex in cave_dict.keys():
                if vertex != "start":
                    if part_2:
                        if vertex not in track or vertex.isupper():
                            dfs(vertex, track, small_caves_entered, part_2=True)
                        elif small_caves_entered == 0:
                            dfs(vertex, track, small_caves_entered=True, part_2=True)
                    else:
                        if vertex not in track or vertex.isupper():
                            dfs(vertex, track)

    else:
        lap_count += 1


def main():
    global lap_count

    file_input = get_input()
    make_dict(file_input)

    start_vertex = "start"
    start_track = ""

    dfs(start_vertex, start_track)
    print(f"Part One: {lap_count:,}")

    lap_count = 0

    dfs(start_vertex, start_track, part_2=True)
    print(f"Part Two: {lap_count:,}")


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        print("Error: ", err)
        print("Error.__cause__", err.__cause__)
        print("Error.__class__", err.__class__.__name__)
        print("Error.with_traceback", err.with_traceback)
