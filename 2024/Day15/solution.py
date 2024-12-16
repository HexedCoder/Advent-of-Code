def get_input():
    with open("input") as file_input:
        maze_input, direction_input = file_input.read().split("\n\n")
    
    maze = [list(char) for char in maze_input.split("\n")]

    maze_2 = []
    for line in maze_input.split("\n"):
        line = list(line)
        line = [char for char in line for _ in range(2)]
        line = list("".join(line).replace("@@", "@.").replace("OO", "[]"))

        maze_2.append(line)
    directions = list(direction_input)

    return maze, maze_2, directions

def get_edges(position, direction, maze):
    x, y, = position
    if direction == "^":
        edges = []
        while x >= 0:
            x -= 1
            if maze[x][y] == "#":
                break
            edges.append((x, y))
            if maze[x][y] == ".":
                break
    elif direction == "v":
        edges = []
        while x < len(maze):
            x += 1
            if maze[x][y] == "#":
                break
            edges.append((x, y))
            if maze[x][y] == '.':
                break
    elif direction == "<":
        edges = []
        while y >= 0:
            y -= 1
            if maze[x][y] == "#":
                break
            edges.append((x, y))
            if maze[x][y] == '.':
                break
    elif direction == ">":
        edges = []
        while y < len(maze[0]):
            y += 1
            if maze[x][y] == "#":
                break
            edges.append((x, y))
            if maze[x][y] == '.':
                break
    else:
        return []
    if any(maze[px][py] == '.' for px, py in edges):
        return edges
    else:
        return []


def part_one(maze, directions):
    output = 0

    start_pos = None
    for i, row in enumerate(maze):
        if not start_pos:
            for j, cell in enumerate(row):
                if cell == "@":
                    start_pos = (i, j)
                    break

    block = "#"
    path = "."
    character = "@"

    x, y, = start_pos
    direction_dict = {"^": (x - 1, y), "v": (x + 1, y), "<": (x, y - 1), ">": (x, y + 1)}

    for direction in directions:
        push_list = get_edges((x, y), direction, maze)
        if push_list:
            for push in push_list:      
                px, py = push
                maze[px][py] = "O"
            
            maze[x][y] = path

            x, y = direction_dict[direction]
            direction_dict = {"^": (x - 1, y), "v": (x + 1, y), "<": (x, y - 1), ">": (x, y + 1)}

            maze[x][y] = character

    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == "O":
                output += y * 100 + x
    
    return output


def part_two(maze, directions):
    output = 0

    start_pos = None
    for i, row in enumerate(maze):
        if not start_pos:
            for j, cell in enumerate(row):
                if cell == "@":
                    start_pos = (i, j)
                    break

    block = "#"
    path = "."
    character = "@"

    x, y, = start_pos
    direction_dict = {"^": (x - 1, y), "v": (x + 1, y), "<": (x, y - 1), ">": (x, y + 1)}

    for direction in directions:
        push_list = get_edges((x, y), direction, maze)
        if direction == "^" and maze[x - 1][y] != path:
            for px, py in push_list:
                if px == '.':
                    continue

                if maze[px][py] == "[":
                    if (px, py + 1) not in push_list:
                        new_edges = get_edges((px + 1, py + 1), direction, maze)
                        if not new_edges or new_edges in push_list:
                            push_list.clear()
                        else:
                            push_list.extend([('.', '.')])
                            push_list.extend(new_edges)
                elif maze[px][py] == "]":
                    if (px, py - 1) not in push_list:
                        new_edges = get_edges((px + 1, py - 1), direction, maze)
                        if not new_edges or new_edges in push_list:
                            push_list.clear()
                        else:
                            push_list.extend([('.', '.')])
                            push_list.extend(new_edges)
        elif direction == "v" and maze[x + 1][y] != path:
            for px, py in push_list:
                if px == '.':
                    continue

                if maze[px][py] == "[":
                    if (px, py + 1) not in push_list:
                        new_edges = get_edges((px - 1, py + 1), direction, maze)
                        if not new_edges or new_edges in push_list:
                            push_list.clear()
                        else:
                            push_list.extend([('.', '.')])
                            push_list.extend(new_edges)
                elif maze[px][py] == "]":
                    if (px, py - 1) not in push_list:
                        new_edges = get_edges((px - 1, py - 1), direction, maze)
                        if not new_edges or new_edges in push_list:
                            push_list.clear()
                        else:
                            push_list.extend([('.', '.')])
                            push_list.extend(new_edges)

        if push_list:
            for i in range(len(push_list) - 1, 0, -1):
                px, py = push_list[i]
                nx, ny = push_list[i - 1]

                try:
                    maze[px][py] = maze[nx][ny]
                except TypeError:
                    try:                        
                        maze[nx][ny] = path   
                    except TypeError:
                        maze[px][py] = path   
                    i -= 1     
                    continue

            maze[x][y] = path
            x, y = direction_dict[direction]
            direction_dict = {"^": (x - 1, y), "v": (x + 1, y), "<": (x, y - 1), ">": (x, y + 1)}

            maze[x][y] = character

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
