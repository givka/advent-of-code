import csv
from collections import deque
from dataclasses import dataclass


class IntCode:
    def __init__(self, numbers: list):
        self.numbers = numbers.copy()
        self.numbers.extend([0 for _ in range(1, 1000000)])
        self.relative_number = 0
        self.cursor = 0
        self.current = 0
        self.current_str = ""

    def is_finished(self):
        return self.numbers[self.cursor] == 99

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


# noinspection PyPep8Naming
@dataclass
class vec2:
    x: int
    y: int

    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return vec2(-self.x, -self.y)

    def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Movement:
    NORTH = vec2(0, 1)
    SOUTH = vec2(0, -1)
    WEST = vec2(-1, 0)
    EAST = vec2(1, 0)


class Robot:
    def __init__(self):
        self.map = {}
        self.ascii = {i: chr(i) for i in range(129)}
        self.cursor = vec2(0, 0)
        self.pos = vec2(0, 0)
        self.intersections = []

    def test(self, m):
        for i in m:
            self.output_callback(i)

    def output_callback(self, output):
        char = self.ascii[output]

        if char == "^" or char == "v" or char == "<" or char == ">":
            self.pos = vec2(self.cursor.x, self.cursor.y)

        if char == "\n":
            self.cursor.x = 0
            self.cursor.y += 1
        else:
            self.map[vec2(self.cursor.x, self.cursor.y)] = char
            self.cursor.x += 1

    def input_callback(self):
        print("input:", 0)
        input()
        return 0

    def print_map(self):
        min_w = min(self.map, key=lambda t: t.x).x
        min_h = min(self.map, key=lambda t: t.y).y
        max_w = max(self.map, key=lambda t: t.x).x
        max_h = max(self.map, key=lambda t: t.y).y
        string = ""
        for y in range(min_h, max_h + 1):
            for x in range(min_w, max_w + 1):
                if vec2(x, y) not in self.map:
                    continue
                if vec2(x, y) in self.intersections:
                    string += "O"
                else:
                    string += self.map[vec2(x, y)]
            string += "\n"
        print(string)

    def get_intersections(self):

        for pos in self.map:
            if self.map[pos] != "#":
                continue
            neighbours = [pos + Movement.NORTH,
                          pos + Movement.SOUTH,
                          pos + Movement.WEST,
                          pos + Movement.EAST]

            intersection = True
            for neighbour in neighbours:
                if neighbour not in self.map or self.map[neighbour] != "#":
                    intersection = False
                    break
            if intersection:
                self.intersections.append(vec2(pos.x, pos.y))

    def get_sum_alignment_parameters(self):
        alignment_parameters = [i.x * i.y for i in self.intersections]
        return sum(alignment_parameters)


def main():
    memory = parse()
    robot = Robot()
    int_code = IntCode(memory)

    while int_code.is_finished() is False:
        int_code.process_code(robot.input_callback, robot.output_callback)

    robot.get_intersections()
    robot.print_map()
    print("sum alignment parameters:", robot.get_sum_alignment_parameters())


if __name__ == "__main__":
    main()
