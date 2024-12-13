def get_input():
    with open("input") as file_input:
        file_input = file_input.read()
    
    plot_inputs = [list(char) for char in file_input.split("\n")]

    return plot_inputs

def check_location(plot_inputs):
    plot_inputs = list(plot_inputs)
    total_corners = 0
    
    for plot in plot_inputs:
        x, y = plot

        dirs = {
            "N": (x - 1, y) not in plot_inputs,
            "E": (x, y + 1) not in plot_inputs,
            "S": (x + 1, y) not in plot_inputs,
            "W": (x, y - 1) not in plot_inputs,
            "NE": (x - 1, y + 1) not in plot_inputs,
            "NW": (x - 1, y - 1) not in plot_inputs,
            "SE": (x + 1, y + 1) not in plot_inputs,
            "SW": (x + 1, y - 1) not in plot_inputs
        }

        checks = [
            dirs["N"] == dirs["E"] and (dirs["N"] or dirs["NE"]),
            dirs["E"] == dirs["S"] and (dirs["E"] or dirs["SE"]),
            dirs["S"] == dirs["W"] and (dirs["S"] or dirs["SW"]),
            dirs["W"] == dirs["N"] and (dirs["W"] or dirs["NW"])
        ]

        total_corners += sum(checks)

    return total_corners

def process_position(plot_inputs, position, p1):
    x, y = position
    
    visited = set()
    queue = [position]
    perimeter = 0

    while queue:
        x, y = queue.pop(0)
        value = plot_inputs[x][y]
        visited.add((x, y))

        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        for nx, ny in neighbors:
            valid = 0 <= nx < len(plot_inputs) and 0 <= ny < len(plot_inputs[0])
            if valid and plot_inputs[nx][ny] == value:
                if (nx, ny) not in visited:

                    if (nx, ny) not in queue:
                        queue.append((nx, ny))
                        
                    visited.add(position)
            else:
                if p1:
                    perimeter += 1

    if not p1:
        perimeter += check_location(visited)

    return visited, perimeter


def solve(plot_inputs, p1):
    output = 0
    checked_positions = set()
    for x in range(len(plot_inputs)):
        for y in range(len(plot_inputs[0])):
            if (x, y) not in checked_positions:
                positions, perimeter = process_position(plot_inputs, (x, y), p1)
                output += perimeter * len(positions)
                checked_positions.update(positions)
    return output

def main():

    plot_inputs = get_input()

    part_1 = solve(plot_inputs, True)
    print(f"Part One:", part_1)

    part_2 = solve(plot_inputs, False)
    print(f"Part Two:", part_2)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()
