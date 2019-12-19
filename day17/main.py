import csv
import re
from dataclasses import dataclass


class IntCode:
    def __init__(self, numbers: list):
        self.numbers = numbers.copy()
        self.numbers.extend([0 for _ in range(1, 1000000)])
        self.relative_number = 0
        self.cursor = 0
        self.current = 0
        self.current_str = ""
        self.pattern = []

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
        self.dir = vec2(0, 0)
        self.input_ascii = ""
        self.cursor_input_ascii = 0
        self.score = 0

    def output_callback(self, output):
        if output not in self.ascii:
            self.score = output
            return

        char = self.ascii[output]

        if char == "^" or char == "v" or char == "<" or char == ">":
            self.pos = vec2(self.cursor.x, self.cursor.y)
            if char == "^":
                self.dir = Movement.NORTH
            if char == "v":
                self.dir = Movement.SOUTH
            if char == "<":
                self.dir = Movement.WEST
            if char == ">":
                self.dir = Movement.EAST

        if char == "\n":
            self.cursor.x = 0
            self.cursor.y -= 1
        else:
            self.map[vec2(self.cursor.x, self.cursor.y)] = char
            self.cursor.x += 1

    def input_callback(self):
        if self.cursor_input_ascii > len(self.input_ascii) - 1:
            if self.cursor_input_ascii == len(self.input_ascii):
                self.cursor_input_ascii += 1
                return ord("n")
            if self.cursor_input_ascii == len(self.input_ascii) + 1:
                self.cursor_input_ascii += 1
                return ord("\n")

        self.cursor_input_ascii += 1
        return ord(self.input_ascii[self.cursor_input_ascii - 1])

    def print_map(self):
        min_w = min(self.map, key=lambda t: t.x).x
        min_h = min(self.map, key=lambda t: t.y).y
        max_w = max(self.map, key=lambda t: t.x).x
        max_h = max(self.map, key=lambda t: t.y).y
        string = ""
        for y in sorted(range(min_h, max_h + 1), reverse=True):
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
            neighbours = [pos + Movement.NORTH, pos + Movement.SOUTH,
                          pos + Movement.WEST, pos + Movement.EAST]

            intersection = True
            for neighbour in neighbours:
                if neighbour not in self.map or self.map[neighbour] != "#":
                    intersection = False
                    break
            if intersection:
                self.intersections.append(vec2(pos.x, pos.y))

    def get_sum_alignment_parameters(self):
        alignment_parameters = [abs(i.x * i.y) for i in self.intersections]
        return sum(alignment_parameters)

    def create_input_ascii(self):
        neighbours = [Movement.NORTH, Movement.SOUTH, Movement.WEST, Movement.EAST]

        commands = []
        command = None
        turn = ""

        for n in neighbours:
            if self.pos + n in self.map and self.map[self.pos + n] == "#":
                command = vec2(0, 0)
                turn = self.new_turn(n)
                self.dir = n
                break

        while len([key for key in self.map if self.map[key] == "#"]) != 0:
            command += self.dir
            self.pos += self.dir
            self.map[self.pos] = ";"
            pos = self.pos + self.dir
            if pos in self.map and self.map[pos] == "#":
                continue
            for n in neighbours:
                if n == self.dir or n == -self.dir:
                    continue
                if self.pos + n not in self.map:
                    continue
                if self.map[self.pos + n] == "#":
                    commands.append((turn, abs(command.x + command.y)))
                    command = vec2(0, 0)
                    turn = self.new_turn(n)
                    self.dir = n
                    break

        commands.append((turn, abs(command.x + command.y)))  # last command
        unique_commands = list(set(commands))

        string = ''
        for command in commands:
            string += str(unique_commands.index(command))

        patterns = set()  # give patterns of given length
        find_pattern(string, patterns)
        # there are multiple combinations of patterns, we take the first one
        patterns = sorted([list(p) for p in patterns][0], reverse=True)  # sort the list because of the string replace

        functions = {}
        char_int = ord('A')
        main_routine = format_message(commands)
        for pattern in patterns:
            look_for_commands = [unique_commands[int(char)] for char in pattern]
            look_string = format_message(look_for_commands)
            functions[chr(char_int)] = look_string
            main_routine = re.sub(look_string, chr(char_int), main_routine)
            char_int += 1
        functions["main"] = main_routine

        # hardcoded, could be done in generic way
        input_message = ""
        input_message += functions["main"] + "\n"
        input_message += functions["A"] + "\n"
        input_message += functions["B"] + "\n"
        input_message += functions["C"] + "\n"

        self.input_ascii = input_message
        self.cursor_input_ascii = 0

    def new_turn(self, new_pos):
        if self.dir == Movement.NORTH:
            return "R" if new_pos == Movement.EAST else "L"
        if self.dir == Movement.EAST:
            return "R" if new_pos == Movement.SOUTH else "L"
        if self.dir == Movement.SOUTH:
            return "R" if new_pos == Movement.WEST else "L"
        if self.dir == Movement.WEST:
            return "R" if new_pos == Movement.NORTH else "L"


def format_message(commands):
    string = ""
    for c in commands:
        string += c[0] + "," + str(c[1]) + ","
    return string[:-1]


def find_pattern(string: str, patterns: set, memory=None, level=1):
    if memory is None:
        memory = ['' for _ in range(0, 3)]

    for i in range(2, len(string)):  # begin at 2 to get group of 2 minimum
        look_for = string[0:i]
        memory[level - 1] = look_for
        z = re.finditer(look_for, string)
        matches = [zz.start() for zz in z]
        if level != len(memory) and len(matches) == 1:  # we want groups of 2 minimum
            break
        string_to_empty = re.sub(look_for, '', string)
        if level == len(memory) and len(look_for) > 1 and len(string_to_empty) == 0:
            patterns.add((memory[0], memory[1], memory[2]))
        if level < len(memory):
            find_pattern(string_to_empty, patterns, memory, level + 1)


def main():
    memory = parse()
    robot = Robot()
    memory[0] = 1  # first we get the map
    int_code = IntCode(memory)

    while int_code.is_finished() is False:
        int_code.process_code(robot.input_callback, robot.output_callback)

    robot.get_intersections()
    robot.print_map()
    print("sum alignment parameters:", robot.get_sum_alignment_parameters())

    memory[0] = 2  # then we move the robot
    int_code = IntCode(memory)
    robot.create_input_ascii()

    while int_code.is_finished() is False:
        int_code.process_code(robot.input_callback, robot.output_callback)

    print("score:", robot.score)


if __name__ == "__main__":
    main()
