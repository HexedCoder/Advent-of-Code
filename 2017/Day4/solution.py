def main():
    print('Part 1:', sum([1 if len(s.split()) == len(set(s.split())) else 0 for s in open('input').readlines()]))
    print('Part 2:', sum([1 if len(list("".join(sorted(w)) for w in s.split())) == len(set(list("".join(sorted(w)) for w in s.split()))) else 0 for s in open('input').readlines()]))


if __name__ == "__main__":
    main()
