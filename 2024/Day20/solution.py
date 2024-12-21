def get_input():
    with open("input", "r") as file:
        file_input = file.read().split("\n")
    return file_input

def calculate_distances(grid):  
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                start = (r, c)

    height, width = len(grid), len(grid[0])
    distance_list = [[0] * width for _ in range(height)]
    
    queue = [start]
    while queue:
        curr_x, curr_y = queue.pop()
        
        directions = [(curr_x - 1, curr_y), (curr_x + 1, curr_y), (curr_x, curr_y - 1), (curr_x, curr_y + 1)]
        for new_x, new_y in directions:
            if 0 <= new_x < height and 0 <= new_y < width and grid[new_x][new_y] != '#' and 0 == distance_list[new_x][new_y]:

                if (new_x, new_y) not in queue:
                    distance_list[new_x][new_y] = distance_list[curr_x][curr_y] + 1
                    queue.append((new_x, new_y))
    
    return distance_list

def calculate_savings(distances, grid, cheat_distance):
    height, width = len(grid), len(grid[0])
    total_savings = []

    for x in range(height):
        for y in range(width):
            if distances[x][y] != 0:

                for check_x in range(cheat_distance * 2 + 1):
                    check_x -= cheat_distance
                    for check_y in range(cheat_distance * 2 + 1):
                        check_y -= cheat_distance

                        cheat_cost = abs(check_x) + abs(check_y)
                        if cheat_cost <= cheat_distance:
                            new_x = x + check_x
                            new_y = y + check_y
                            if 0 <= new_x < height and 0 <= new_y < width and grid[new_x][new_y] != '#' and distances[new_x][new_y]:
                                initial_cost = distances[x][y] - distances[new_x][new_y]

                                total_savings.append(initial_cost - cheat_cost)

    return total_savings

def solve(input_data, cheat_distance):
    grid = [list(row) for row in input_data]
    
    distances = calculate_distances(grid)
    savings = calculate_savings(distances, grid, cheat_distance)
    return sum([1 for savings in savings if savings >= 100])

def main():
    input_data = get_input()

    result = solve(input_data, 2)
    print(f"Part One: {result}")

    result = solve(input_data, 20)
    print(f"Part Two: {result}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
