#!/usr/bin/env python3

def main():
    everyone = []
    total = 0
    file_name = "input.txt"
    lines = (line for line in open(file_name))

    while True:
        try:
            total += int(next(lines))
        except ValueError:
            everyone.append(total)
            total = 0
        except StopIteration:
            everyone = sorted(everyone, reverse=True)[:3]
            break

    print("Part 1", everyone[0], "\nPart 2", sum(everyone))


if __name__ == "__main__":
    main()
