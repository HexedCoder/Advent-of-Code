with open("input.txt", "r") as file:
    # Sample - 110000000001
    lines = file.readlines()

count_dict = {}
for number in range(1, 13):
    count_dict[number] = 0

for line in lines:
    line = line.replace("\n", "")
    number = 1
    for bit in line:
        bit = int(bit)
        if bit == 0:
            count_dict[number] += 1
        number += 1

final_list = []
for zero_count in count_dict.values():
    if zero_count > 500:
        final_list.append(0)
    else:
        final_list.append(1)

gamma_rate = ""

for number in final_list:
    gamma_rate = f"{gamma_rate}{number}"

epsilon_rate = ''.join('1' if x == '0' else '0' for x in gamma_rate)

gamma_rate = int(gamma_rate, base=2)
epsilon_rate = int(epsilon_rate, base=2)
power_consumption = gamma_rate * epsilon_rate

print(power_consumption)
