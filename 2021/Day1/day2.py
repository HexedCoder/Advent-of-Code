with open("input.txt", "r") as file_input:
    lines = file_input.read().split("\n")
previous = 0
current = 0
line_count = 0
increase_count = 0
sum_list = []
for line in lines:
    if line_count < len(lines) - 2:
        line_sum = int(lines[line_count]) + int(lines[line_count + 1]) + \
                   int(lines[line_count + 2])
        sum_list.append(line_sum)
        line_count += 1

line_count = 0
for cur_sum in sum_list:
    cur_sum = int(cur_sum)
    if line_count == 0:
        current = cur_sum
        line_count += 1
        continue
    previous = current
    current = cur_sum
    if current > previous:
        increase_count += 1
print(increase_count)
