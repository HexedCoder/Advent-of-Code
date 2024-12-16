import time
# < 7727

def get_input():
    with open("input") as file_input:
        file_input = file_input.read().split("\n")
    
    robots = [
        [list(map(int, value[2:].split(","))) for value in line.split(" ")]
        for line in file_input
    ]

    return robots

def part_one(robots):
    output = 1
    locations = [0, 0, 0, 0]

    maze_height, maze_width  = 103, 101

    for robot in robots:
        curr_pos, curr_vel = robot    
        ch_x = (curr_pos[0] + curr_vel[0] * 100) % maze_width
        ch_y = (curr_pos[1] + curr_vel[1] * 100) % maze_height

        idx = 0
        if ch_x > maze_width // 2:
            idx += 1
        if ch_y > maze_height // 2:
            idx += 2

        if ch_x != maze_width // 2 and ch_y != maze_height // 2:
            locations[idx] += 1

    for loc in locations:
        output *= loc
    return output


def part_two(robots):
    output = 0
    maze_height, maze_width  = 103, 101

    curr = 'X'
    for num in range(0, 1000000):
        if output != 0:
            break

        maze = [['.' for _ in range(maze_width)] for _ in range(maze_height)]
        for robot in robots:
            curr_pos, curr_vel = robot
            
            ch_x = (curr_pos[0] + curr_vel[0] * num) % maze_width
            ch_y = (curr_pos[1] + curr_vel[1] * num) % maze_height

            maze[ch_y][ch_x] = curr

        valid = False
        for m in maze:
            if "XXXXXXXX" in "".join(m):
                valid = True
                break

        if valid:
            output = num
            break

    return output, maze

def main():

    robots = get_input()

    part_1 = part_one(robots)
    print(f"Part One:", part_1)

    part_2, maze = part_two(robots)
    print(f"Part Two:", part_2)

    for m in maze:
        print("".join(m))

if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()
