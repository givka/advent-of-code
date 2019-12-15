import csv


def parse():
    with open('input.txt') as f:
        reader = csv.reader(f)
        line = [line for line in reader][0]
        return [int(number) for number in line]


class IntCode:
    def __init__(self, numbers: list, input_number: int, relative_number: int):
        self.numbers = numbers
        self.numbers.extend([0 for _ in range(1, 10000)])
        self.input_number = input_number
        self.relative_number = relative_number
        self.cursor = 0
        self.outputs = []
        self.current = 0
        self.current_str = ""
        self.process_code()

    def process_code(self):
        if self.numbers[self.cursor] == 99:
            return

        self.current_str = str(self.numbers[self.cursor])
        self.current = int(self.current_str[-1])

        if self.current == 1:
            self.numbers[self.p(3)] = self.numbers[self.p(1)] + self.numbers[self.p(2)]
        if self.current == 2:
            self.numbers[self.p(3)] = self.numbers[self.p(1)] * self.numbers[self.p(2)]
        if self.current == 3:
            self.numbers[self.p(1)] = self.input_number
        if self.current == 4:
            self.outputs.append(self.numbers[(self.p(1))])
        if self.current == 5:
            self.cursor = self.numbers[(self.p(2))] if self.numbers[(self.p(1))] != 0 else self.cursor + 3
        if self.current == 6:
            self.cursor = self.numbers[(self.p(2))] if self.numbers[(self.p(1))] == 0 else self.cursor + 3
        if self.current == 7:
            self.numbers[(self.p(3))] = 1 if self.numbers[self.p(1)] < self.numbers[self.p(2)] else 0
        if self.current == 8:
            self.numbers[(self.p(3))] = 1 if self.numbers[self.p(1)] == self.numbers[self.p(2)] else 0
        if self.current == 9:
            self.relative_number += self.numbers[self.p(1)]

        if self.current in [1, 2, 7, 8]:
            self.cursor += 4
        if self.current in [3, 4, 9]:
            self.cursor += 2

        self.process_code()

    def p(self, index):
        mode = int(self.current_str[-(index + 2)]) if len(self.current_str) > (index + 1) else 0
        if mode == 0:
            return self.numbers[self.cursor + index]
        if mode == 1:
            return self.cursor + index
        if mode == 2:
            return self.numbers[self.cursor + index] + self.relative_number


def main():
    numbers = parse()
    int_code = IntCode(numbers, 1, 0)
    print("outputs:", int_code.outputs)


if __name__ == "__main__":
    main()
