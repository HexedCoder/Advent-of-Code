from string import ascii_letters, digits
def get_input():
    with open("input") as _input:
        file_input = _input.read()
    valid_names = "".join([ascii_letters, digits])

    antennas_grid = {char: [] for char in file_input if char in valid_names if file_input.count(char) > 1}
    antenna_map = file_input.split("\n")
    antennas_grid = {char: [(line.index(char), i) for i, line in enumerate(antenna_map) if char in line] for char in antennas_grid}
    antinode_map = [["." for _ in range(len(antenna_map[0]))] for _ in range(len(antenna_map))]
    return antennas_grid, antinode_map

def find_nodes(antennas_grid, antinode_map, part_two):
    antinode_locs = set()
    x_bound = len(antinode_map[0])
    y_bound = len(antinode_map)
    for _, positions in antennas_grid.items():
        for x, y in positions:
            for sim_x, sim_y in positions:
                if sim_x == x and sim_y == y:
                    continue

                dx = abs(sim_x - x)
                if sim_x > x:
                    dx = -dx
                dy = sim_y - y
                new_x1 = x + dx
                new_y1 = y - dy
                if part_two:    
                    antinode_locs.add((x, y))
                    antinode_locs.add((sim_x, sim_y))

                while True:
                    if new_x1 > -1 and new_y1 > -1 and new_x1 < x_bound and new_y1 < y_bound:
                        # go in a line from 0, 0 to x_bound, y_bound along the line 
                        antinode_locs.add((new_x1, new_y1))
                        antinode_map[new_y1][new_x1] = "#"
                        if not part_two:
                            break

                        new_x1 += dx
                        new_y1 -= dy
                    else:
                        break
                new_x2 = sim_x - dx
                new_y2 = sim_y + dy
                while True:
                    if new_x2 > -1 and new_y2 > -1 and new_x2 < x_bound and new_y2 < y_bound:
                        antinode_locs.add((new_x2, new_y2))
                        antinode_map[new_y2][new_x2] = "#"
                        if not part_two:
                            break

                        new_x2 -= dx
                        new_y2 += dy
                    else:
                        break
                    
    return antinode_locs

def solve(antennas_grid, antinode_map, part_two):
    antinode_locs = find_nodes(antennas_grid, antinode_map, part_two)

    return len(antinode_locs)

def main():
    antennas_grid, antinode_map = get_input()
    print("Part 1:", solve(antennas_grid, antinode_map, False))
    print("Part 2:", solve(antennas_grid, antinode_map, True))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")