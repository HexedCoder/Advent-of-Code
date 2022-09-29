def get_input():
    with open("input.txt") as file_input:
        lines_input = file_input.readlines()

    return lines_input


def main():
    file_input = get_input()
    for line in file_input:
        line = line.replace("\n", "")
        print(line)

if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        print("Error: ", err)
        print("Error.__cause__", err.__cause__)
        print("Error.__class__", err.__class__.__name__)
        print("Error.with_traceback", err.with_traceback)