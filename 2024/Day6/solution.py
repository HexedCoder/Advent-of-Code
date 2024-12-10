
def get_input():
    with open("input") as _input:
        maze_input = _input.read().split("\n")
    
    maze = []
    for row in maze_input:
        maze.append(list(row))
    
    return maze

def part_1(maze):
    max_x = len(maze[0])
    max_y = len(maze)
    coords = set()

    for i, row in enumerate(maze):
        if "^" in row:
            coords.add((i, row.index("^")))
            break
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)} 

    for x, y in coords:
        direction = "^"
        while True:
            dx, dy = directions[direction]
            nx, ny = x + dx, y + dy
            if 0 <= nx < max_y and 0 <= ny < max_x:
                if maze[nx][ny] in [".", "X", "^"]:
                    if maze[nx][ny] == ".":
                        maze[nx][ny] = "X"
                    x, y = nx, ny
                else:
                    direction = {"^": ">", ">": "v", "v": "<", "<": "^"}[direction]
            else:
                break

    return sum([1 for row in maze for cell in row if cell == "X"]) + 1
    
def is_loop(maze, start_x, start_y, direction, directions):
    max_x = len(maze[0])
    max_y = len(maze)
    visited = set()
    
    x, y = start_x, start_y
    while True:
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        if (nx, ny, direction) in visited:
            return True  #
        if 0 <= nx < max_y and 0 <= ny < max_x:
            if maze[nx][ny] in [".", "X", "^"]:
                visited.add((nx, ny, direction))
                x, y = nx, ny
            else:
                direction = {"^": ">", ">": "v", "v": "<", "<": "^"}[direction]
        else:
            return False  


def part_2(maze):
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    possible_positions = set()

    start_x, start_y = next(
        (i, row.index("^")) for i, row in enumerate(maze) if "^" in row
    )

    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "." and (y, x) != (start_x, start_y):
                maze[y][x] = "#"
                if is_loop(maze, start_x, start_y, "^", directions):
                    possible_positions.add((y, x))
                maze[y][x] = "."

    return len(possible_positions)


def main():
    print("Part 1:", part_1(get_input()))
    print("Part 2:", part_2(get_input()))


if __name__ == "__main__":
    main()
