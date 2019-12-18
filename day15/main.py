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

    def key(self):
        return self.x, self.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Tile:
    WALL = 0
    EMPTY = 1
    OXYGEN = 2


class Movement:
    NORTH = vec2(0, 1)
    SOUTH = vec2(0, -1)
    WEST = vec2(-1, 0)
    EAST = vec2(1, 0)


class Droid:
    def __init__(self):
        self.map = {vec2(0, 0): Tile.EMPTY}
        self.pos = vec2(0, 0)
        self.dir = vec2(0, 1)
        self.remaining = {Movement.NORTH, Movement.SOUTH, Movement.WEST, Movement.EAST}
        self.oxygen_pos = vec2(0, 0)

    def print_map(self):
        string = ""
        min_w = min(self.map, key=lambda t: t.x).x
        min_h = min(self.map, key=lambda t: t.y).y
        max_w = max(self.map, key=lambda t: t.x).x
        max_h = max(self.map, key=lambda t: t.y).y

        for y in sorted(range(min_h, max_h + 1), reverse=True):
            for x in range(min_w, max_w + 1):
                if x == self.pos.x and y == self.pos.y:
                    if self.dir == Movement.NORTH:
                        string += "^"
                    if self.dir == Movement.SOUTH:
                        string += "v"
                    if self.dir == Movement.WEST:
                        string += "<"
                    if self.dir == Movement.EAST:
                        string += ">"
                    continue
                if vec2(x, y) not in self.map:
                    string += " "
                    continue
                tile = self.map[vec2(x, y)]
                if tile == Tile.WALL:
                    string += "#"
                if tile == Tile.EMPTY:
                    string += "."
                if tile == Tile.OXYGEN:
                    string += "O"
            string += "\n"
        print(string)

    def get_dir_input(self):
        if self.dir == Movement.NORTH:
            return 1
        if self.dir == Movement.SOUTH:
            return 2
        if self.dir == Movement.WEST:
            return 3
        if self.dir == Movement.EAST:
            return 4

    def process_input(self):
        if (self.pos + Movement.NORTH) not in self.map:
            self.remaining.add(self.pos + Movement.NORTH)
        if (self.pos + Movement.SOUTH) not in self.map:
            self.remaining.add(self.pos + Movement.SOUTH)
        if (self.pos + Movement.WEST) not in self.map:
            self.remaining.add(self.pos + Movement.WEST)
        if (self.pos + Movement.EAST) not in self.map:
            self.remaining.add(self.pos + Movement.EAST)

        new_pos_l = self.pos + self.get_dir_left()

        if new_pos_l not in self.map:
            self.dir = self.get_dir_left()
            return self.get_dir_input()

        if self.map[new_pos_l] == Tile.WALL:
            return self.get_dir_input()
        else:
            self.dir = self.get_dir_left()
            return self.get_dir_input()

    def process_output(self, output):
        new_pos = self.pos + self.dir

        if output == Tile.OXYGEN:
            self.oxygen_pos = new_pos

        self.map[new_pos] = output
        if new_pos in self.remaining:
            self.remaining.remove(new_pos)

        if output == Tile.WALL:
            self.dir = -self.get_dir_left()  # get_dir_right()
        elif output == Tile.EMPTY:
            self.pos += self.dir
        elif output == Tile.OXYGEN:
            self.pos += self.dir

    def get_dir_left(self):
        if self.dir == Movement.NORTH:
            return Movement.WEST
        elif self.dir == Movement.SOUTH:
            return Movement.EAST
        elif self.dir == Movement.WEST:
            return Movement.SOUTH
        elif self.dir == Movement.EAST:
            return Movement.NORTH

    def map_fully_discovered(self):
        return len(self.remaining) == 0


@dataclass
class Cell:
    parent: 'Cell'
    pos: vec2

    def __hash__(self):
        return hash((self.pos.x, self.pos.y))

    def __eq__(self, other):
        return self.pos.x == other.pos.x and self.pos.y == other.pos.y


def breath_first_search(maze: dict, goal: vec2):
    discovered = {}
    start = Cell(None, vec2(0, 0))
    queue = deque([start])
    discovered[start.pos] = start

    good_paths = []
    while len(queue) != 0:
        v = queue.popleft()
        if v.pos == goal:
            return v
        for pos in [v.pos + Movement.NORTH, v.pos + Movement.SOUTH, v.pos + Movement.WEST, v.pos + Movement.EAST]:
            if pos not in maze:
                continue
            if maze[pos] == Tile.WALL:
                continue
            if pos in discovered:
                continue
            cell = Cell(v, pos)
            discovered[cell.pos] = cell
            queue.append(cell)


def main():
    memory = parse()
    int_code = IntCode(memory)
    droid = Droid()

    while droid.map_fully_discovered() is False:
        int_code.process_code(droid.process_input, droid.process_output)

    droid.print_map()
    print("oxygen position:", droid.oxygen_pos)

    cell = breath_first_search(droid.map, droid.oxygen_pos)

    count = 0
    parent = cell.parent
    while parent is not None:
        count+=1
        print(parent.pos)
        parent = cell.parent
    print(count)


if __name__ == "__main__":
    main()
