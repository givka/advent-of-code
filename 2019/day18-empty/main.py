import csv
from functools import reduce


def parse():
    with open('input.txt') as f:
        reader = csv.reader(f)
        return reduce(lambda t1, t2: t1 + t2 + "\n", [line[0] for line in reader], "")


def main():
    memory = parse()
    print(memory)


if __name__ == "__main__":
    main()
