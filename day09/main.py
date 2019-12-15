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
            self.set_param(3, self.get_param(1) + self.get_param(2))
        if self.current == 2:
            self.set_param(3, self.get_param(1) * self.get_param(2))
        if self.current == 3:
            self.set_param(1, self.input_number)
        if self.current == 4:
            self.outputs.append(self.get_param(1))
        if self.current == 5:
            self.cursor = self.get_param(2) if self.get_param(1) != 0 else self.cursor + 3
        if self.current == 6:
            self.cursor = self.get_param(2) if self.get_param(1) == 0 else self.cursor + 3
        if self.current == 7:
            self.set_param(3, 1 if self.get_param(1) < self.get_param(2) else 0)
        if self.current == 8:
            self.set_param(3, 1 if self.get_param(1) == self.get_param(2) else 0)
        if self.current == 9:
            self.relative_number += self.get_param(1)

        if self.current in [1, 2, 7, 8]:
            self.cursor += 4
        if self.current in [3, 4, 9]:
            self.cursor += 2

        self.process_code()

    def get_param(self, index):
        parameter = self.numbers[self.cursor + index]
        mode = int(self.current_str[-(index + 2)]) if len(self.current_str) > (index + 1) else 0
        if mode == 0:
            return self.numbers[parameter]
        if mode == 1:
            return parameter
        if mode == 2:
            return self.numbers[parameter + self.relative_number]

    def set_param(self, index, value):
        parameter = self.numbers[self.cursor + index]
        mode = int(self.current_str[-(index + 2)]) if len(self.current_str) > (index + 1) else 0
        if mode == 0:
            self.numbers[parameter] = value
        if mode == 2:
            self.numbers[parameter + self.relative_number] = value


def main():
    numbers = parse()
    int_code = IntCode(numbers, 1, 0)
    print("outputs:", int_code.outputs)


if __name__ == "__main__":
    main()
