import csv


class IntCode:
    def __init__(self, numbers: list):
        self.numbers = numbers.copy()
        self.numbers.extend([0 for _ in range(1, 1000000)])
        self.relative_number = 0
        self.cursor = 0
        self.current = 0
        self.current_str = ""

    def is_running(self):
        return self.numbers[self.cursor] != 99

    def process_code(self, input_callback, output_callback):
        # removed recursion because of python recursion limit
        self.current_str = str(self.numbers[self.cursor])
        self.current = int(self.current_str[-1])

        if self.current == 1:
            self.numbers[self.p(3)] = self.numbers[self.p(1)] + self.numbers[self.p(2)]
        if self.current == 2:
            self.numbers[self.p(3)] = self.numbers[self.p(1)] * self.numbers[self.p(2)]
        if self.current == 3:
            input_number = input_callback()
            self.numbers[self.p(1)] = input_number
        if self.current == 4:
            output_callback(self.numbers[(self.p(1))])
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

    def p(self, index):
        mode = int(self.current_str[-(index + 2)]) if len(self.current_str) > (index + 1) else 0
        if mode == 0:
            return self.numbers[self.cursor + index]
        if mode == 1:
            return self.cursor + index
        if mode == 2:
            return self.numbers[self.cursor + index] + self.relative_number


def parse():
    with open('input.txt') as f:
        reader = csv.reader(f)
        first_line = [line for line in reader][0]
        return [int(char) for char in first_line]


class Droid:
    def __init__(self, size: (int, int)):
        self.map = {}
        for y in range(0, size[1]):
            for x in range(0, size[0]):
                self.map[(x, y)] = " "

        self.cursor = (0, 0)
        self.is_x = True
        self.size = size

    def input_callback(self):
        input_value = self.cursor[0 if self.is_x else 1]
        self.is_x = not self.is_x
        return input_value

    def output_callback(self, output):
        self.map[self.cursor] = "#" if output == 1 else "."

    def __str__(self):
        string = ""
        for y in range(0, self.size[1]):
            for x in range(0, self.size[0]):
                string += self.map[(x, y)] if (x, y) in self.map else " "
            string += "\n"
        return string

    def get_points_affected(self):
        return len([key for key in self.map if self.map[key] == "#"])

    def has_hit(self, memory: list, pos: (int, int)) -> bool:
        print(pos)
        self.cursor = pos
        self.is_x = True
        int_code = IntCode(memory)
        while int_code.is_running():
            int_code.process_code(self.input_callback, self.output_callback)
        return self.map[pos] == "#"


def main():
    memory = parse()

    size = (50, 50)
    droid = Droid(size)

    y = 0
    last_hit_x = 0
    while y < size[1]:
        x = last_hit_x
        while x < size[0]:
            if droid.has_hit(memory, (x, y)):
                last_hit_x = x
                x += 1
                while droid.has_hit(memory, (x, y)):
                    x += 1
                break
            x += 1
        y += 1

    print(droid)
    print("points affected:", droid.get_points_affected())


if __name__ == "__main__":
    main()
