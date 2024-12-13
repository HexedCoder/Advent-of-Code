import re

def get_input():
    with open("input") as file_input:
        file_input = file_input.read().split("\n\n")
    
    games_info = []

    for section in file_input:
        match = re.search(r"Button A: X\+(\d+), Y\+(\d+)\s+Button B: X\+(\d+), Y\+(\d+)\s+Prize: X=(\d+), Y=(\d+)", section)
        if match:
            x1, y1, x2, y2, solx, soly = map(int, match.groups())
            games_info.append([(x1, y1), (x2, y2), (solx, soly)])

    return games_info

def part_one(games_info):
    output = 0

    for game in games_info:
        A, B, Sol = game
        A_x, A_y = A
        B_x, B_y = B
        Sol_x, Sol_y = Sol

        min_cost = None
        best_a, best_b = None, None

        for a in range(Sol_x // A_x + 1):
            if (Sol_x - A_x * a) % B_x == 0: # If the numbers reach solution
                b = (Sol_x - A_x * a) // B_x # Calculate the b number
                if A_y * a + B_y * b == Sol_y: # Ensure solution reached
                    cost = 3 * a + b
                    if not min_cost or cost < min_cost:
                        min_cost = cost
                        best_a, best_b = a, b
        if min_cost:
            output += best_a * 3 + best_b

    return output

def solve(games_info, p2):
    output = 0

    for game in games_info:
        A, B, Sol = game
        A_1, A_2 = A
        B_1, B_2 = B
        C_1, C_2 = Sol

        if p2:
            C_1 += 10000000000000
            C_2 += 10000000000000

        v_1 = (C_1 * B_2 - C_2 * B_1) / (A_1 * B_2 - A_2 * B_1)
        v_2 = (C_1 - A_1 * v_1) / B_1

        if v_1 % 1 == 0 and v_2 % 1 == 0:
            output += (3 * v_1) + v_2

    return int(output)

def main():

    games_info = get_input()

    part_1 = solve(games_info, False)
    print(f"Part One:", part_1)

    part_2 = solve(games_info, True)
    print(f"Part Two:", part_2)

if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()
