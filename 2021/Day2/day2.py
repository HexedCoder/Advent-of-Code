with open("input.txt", "r") as file_input:
    lines = file_input.readlines()

fwd = "forward"
up = "up"
down = "down"
hor_pos = 0
aim = 0
depth = 0

for line in lines:
    line = line.split()
    if line[0] == fwd:
        hor_pos += int(line[1])
        depth += aim * int(line[1])
    if line[0] == up:
        aim -= int(line[1])
    if line[0] == down:
        aim += int(line[1])

print(depth * hor_pos)
