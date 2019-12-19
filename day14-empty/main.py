import csv


def parse():
    with open('input.txt') as f:
        reader = csv.reader(f)
        return [line for line in reader]


def main():
    memory = parse()
    print(memory)


if __name__ == "__main__":
    main()
