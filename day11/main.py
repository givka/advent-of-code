import csv
from dataclasses import dataclass


# noinspection PyPep8Naming
@dataclass
class vec2:
    x: int
    y: int

    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)

    def key(self):
        return self.x, self.y


vec2.ZERO = vec2(0, 0)
vec2.UP = vec2(0, 1)
vec2.DOWN = vec2(0, -1)
vec2.RIGHT = vec2(1, 0)
vec2.LEFT = vec2(-1, 0)


class Robot:
    def __init__(self):
        self.map = {}
        self.position = vec2.ZERO
        self.direction = vec2.UP
        self.count = 0

    def process(self, outputs):
        paint, direction = outputs
        if self.position.key() not in self.map:
            self.count += 1
        self.map[self.position.key()] = paint

        if self.direction == vec2.UP:
            self.direction = vec2.RIGHT if direction == 1 else vec2.LEFT
        elif self.direction == vec2.RIGHT:
            self.direction = vec2.DOWN if direction == 1 else vec2.UP
        elif self.direction == vec2.DOWN:
            self.direction = vec2.LEFT if direction == 1 else vec2.RIGHT
        elif self.direction == vec2.LEFT:
            self.direction = vec2.UP if direction == 1 else vec2.DOWN

        self.position += self.direction

        return self.map[self.position.key()] if self.position.key() in self.map else 0


class IntCode:
    def __init__(self, numbers: list, input_number: int):
        self.numbers = numbers.copy()
        self.numbers.extend([0 for _ in range(1, 1000000)])
        self.input_number = input_number
        self.relative_number = 0
        self.cursor = 0
        self.outputs = []
        self.current = 0
        self.current_str = ""
        self.robot = Robot()
        self.process_code()

    def process_code(self):
        # removed recursion because of python recursion limit
        while self.numbers[self.cursor] != 99:
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

            if len(self.outputs) == 2:
                self.input_number = self.robot.process(self.outputs)
                self.outputs = []

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


def main():
    the_brain = parse()
    int_code = IntCode(the_brain, 0)  # start over black panel
    print("number of painted layers once:", int_code.robot.count)


if __name__ == "__main__":
    main()
