def get_input():
    with open("input") as file_input:
        maze_input, direction_input = file_input.read().split("\n\n")
    
    maze = [list(char) for char in maze_input.split("\n")]

    maze_2 = []
    for line in maze_input.split("\n"):
        expanded_line = [char for char in line for _ in range(2)]
        expanded_line = "".join(expanded_line).replace("@@", "@.").replace("OO", "[]")
        maze_2.append(list(expanded_line))
    directions = list(direction_input.replace("\n", ""))

    return maze, maze_2, directions

def get_edges(position, direction, maze):
    x, y, = position
    edges = []
    dx, dy = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}[direction]
    while 0 <= x < len(maze) and 0 <= y < len(maze[0]):
        x += dx
        y += dy
        if maze[x][y] == "#":
            break
        edges.append((x, y))
        if maze[x][y] == ".":
            break

    if any(maze[px][py] == '.' for px, py in edges):
        return edges
    else:
        return []


def part_one(maze, directions):
    output = 0

    start_pos = None
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == "@":
                start_pos = (i, j)
                break

    x, y, = start_pos
    for direction in directions:
        push_list = get_edges((x, y), direction, maze)
        
        for push in push_list:      
            px, py = push
            maze[px][py] = "O"
            
        if push_list:
            maze[x][y] = '.'

            direction_dict = {"^": (x - 1, y), "v": (x + 1, y), "<": (x, y - 1), ">": (x, y + 1)}
            x, y = direction_dict[direction]

            maze[x][y] = '@'

    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == "O":
                output += y * 100 + x
    
    return output


def part_two(maze, directions):
    output = 0

    start_pos = None
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
                if cell == "@":
                    start_pos = (i, j)
                    break

    x, y, = start_pos
    for direction in directions:
        push_list = get_edges((x, y), direction, maze)
        if direction == "^" and maze[x - 1][y] != '.':
            for px, py in push_list:
                if px == '.':
                    continue

                if maze[px][py] in "[]":
                    offset = 1 if maze[px][py] == "[" else -1
                    if (px, py + offset) not in push_list:
                        new_edges = get_edges((px + 1, py + offset), direction, maze)
                        if not new_edges or new_edges in push_list:
                            push_list.clear()
                        else:
                            push_list.extend([('.', '.')])
                            push_list.extend(new_edges)

        elif direction == "v" and maze[x + 1][y] != '.':
            for px, py in push_list:
                if px == '.':
                    continue

                if maze[px][py] in "[]":
                    offset = 1 if maze[px][py] == "[" else -1
                    if (px, py + offset) not in push_list:
                        new_edges = get_edges((px - 1, py + offset), direction, maze)
                        if not new_edges or new_edges in push_list:
                            push_list.clear()
                        else:
                            push_list.extend([('.', '.')])
                            push_list.extend(new_edges)

        if push_list:
            i = len(push_list) - 1
            while i > 0:
                px, py = push_list[i]
                nx, ny = push_list[i - 1]

                if nx == '.':
                    maze[px][py] = '.'
                    i -= 1
                else:
                    maze[px][py] = maze[nx][ny]
                
                i -= 1

            maze[x][y] = '.'
            direction_dict = {"^": (x - 1, y), "v": (x + 1, y), "<": (x, y - 1), ">": (x, y + 1)}
            x, y = direction_dict[direction]

            maze[x][y] = '@'

    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == "[":
                output += y * 100 + x
    
    return output

def main():

    maze, maze_2, directions = get_input()

    part_1 = part_one(maze, directions)
    print(f"Part One:", part_1)

    part_2 = part_two(maze_2, directions)
    print(f"Part Two:", part_2)

if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()
