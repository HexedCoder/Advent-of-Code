from itertools import product


def get_input():
    with open("input") as _input:
        file_input = _input.read().split("\n")
    
    equations = [[int(solution), list(map(int, params.split()))] for equation in file_input for solution, params in [equation.split(":")]]
    return equations


def check_expression(params, operators, target):
    result = params[0]
    for idx, operator in enumerate(operators):
        if operator == '+':
            result += params[idx + 1]
        elif operator == '*':
            result *= params[idx + 1]
        elif operator == '|':
            result = int(f"{result}{params[idx + 1]}")
        else:
            return 0
        
        if result > target:
            return 0
    return result


def solve(equations, operators):
    total = 0
    for solution, params in equations:
        for ops in product(operators, repeat=len(params) - 1):
            result = check_expression(params, ops, solution)
            if result == solution:
                total += result
                break
    return total


def main():
    equations = get_input()
    print("Part 1:", solve(equations, ['+', '*']))
    print("Part 2:", solve(equations, ['+', '*', '|']))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
