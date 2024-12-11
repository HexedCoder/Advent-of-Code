def get_input():
    with open("input") as file_input:
        lines_input = [list(map(int, row)) for row in file_input.read().split("\n")]

    start_points = [(y, x) for y in range(len(lines_input)) for x in range(len(lines_input[0])) if lines_input[y][x] == 0]

    return lines_input, start_points
   

def get_peaks(start_points, grid, p1=True):
    row_width, column_width = len(grid), len(grid[0])

    total_peaks = 0
    for start_point in start_points:
        peaks = []        
        start_row, start_column = start_point

        queue = [(start_row, start_column)]
        while queue:
            current_row, current_column = queue.pop() 
            neighbors = [(current_row + x_offset, current_column + y_offset) for x_offset, y_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
            
            for neighbor_row, neighbor_col in neighbors:
                if -1 < neighbor_row < row_width and -1 < neighbor_col < column_width:
                    if grid[neighbor_row][neighbor_col] == grid[current_row][current_column] + 1:
                        queue.append((neighbor_row, neighbor_col))
                        if grid[neighbor_row][neighbor_col] == 9:
                            peaks.append((neighbor_row, neighbor_col))

        total_peaks += len(set(peaks)) if p1 else len(peaks) 
        
    return total_peaks


def main():

    grid, start_points = get_input()

    part_1 = get_peaks(start_points, grid)
    part_2 = get_peaks(start_points, grid, False)

    print(f"Part One:", part_1)
    print(f"Part Two:", part_2)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc

        print_exc()