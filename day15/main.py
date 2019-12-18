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
        self.oxygen_to_fill = set()

    def print_map(self) -> None:
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

    def get_dir_input(self) -> int:
        if self.dir == Movement.NORTH:
            return 1
        if self.dir == Movement.SOUTH:
            return 2
        if self.dir == Movement.WEST:
            return 3
        if self.dir == Movement.EAST:
            return 4

    def process_input(self) -> int:
        # self.print_map()
        # input()

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

    def process_output(self, output) -> None:
        new_pos = self.pos + self.dir

        if output == Tile.OXYGEN:
            self.oxygen_pos = new_pos
            self.oxygen_to_fill.add(self.oxygen_pos)

        self.map[new_pos] = output
        if new_pos in self.remaining:
            self.remaining.remove(new_pos)

        if output == Tile.WALL:
            self.dir = -self.get_dir_left()  # get_dir_right()
        elif output == Tile.EMPTY:
            self.pos += self.dir
        elif output == Tile.OXYGEN:
            self.pos += self.dir

    def get_dir_left(self) -> vec2:
        if self.dir == Movement.NORTH:
            return Movement.WEST
        elif self.dir == Movement.SOUTH:
            return Movement.EAST
        elif self.dir == Movement.WEST:
            return Movement.SOUTH
        elif self.dir == Movement.EAST:
            return Movement.NORTH

    def map_fully_discovered(self) -> bool:
        return len(self.remaining) == 0

    def map_has_empty_tiles(self) -> bool:
        empty_tiles = [key for key in self.map if self.map[key] == Tile.EMPTY]
        return len(empty_tiles) != 0

    def fill_oxygen(self) -> None:
        for ox in list(self.oxygen_to_fill):
            neighbours = [ox + Movement.NORTH, ox + Movement.SOUTH,
                          ox + Movement.WEST, ox + Movement.EAST]
            for neighbour in neighbours:
                if self.map[neighbour] == 1:
                    self.map[neighbour] = 2
                    self.oxygen_to_fill.add(neighbour)
            self.oxygen_to_fill.remove(ox)

    def get_minutes_to_fill_oxygen(self) -> int:
        count = 0
        while self.map_has_empty_tiles():
            count += 1
            self.fill_oxygen()
            # self.print_map()
            # input()
        return count


@dataclass
class Cell:
    parent: 'Cell' or None
    pos: vec2

    def count(self, acc=0):
        if self.parent is None:
            return acc
        return self.parent.count(acc + 1)


def breath_first_search(maze: dict, goal: vec2) -> Cell:
    discovered = {}
    start = Cell(None, vec2(0, 0))
    queue = deque([start])
    discovered[start.pos] = start

    while len(queue) != 0:
        current = queue.popleft()
        if current.pos == goal:
            return current.count()
        neighbours = [current.pos + Movement.NORTH, current.pos + Movement.SOUTH,
                      current.pos + Movement.WEST, current.pos + Movement.EAST]
        for neighbour in neighbours:
            if neighbour not in maze or maze[neighbour] == Tile.WALL or neighbour in discovered:
                continue
            cell = Cell(current, neighbour)
            discovered[cell.pos] = cell
            queue.append(cell)


def main():
    memory = parse()
    int_code = IntCode(memory)
    droid = Droid()

    while droid.map_fully_discovered() is False:
        int_code.process_code(droid.process_input, droid.process_output)

    print("minimum inputs:", breath_first_search(droid.map, droid.oxygen_pos))

    print("minutes to fill oxygen:", droid.get_minutes_to_fill_oxygen())


if __name__ == "__main__":
    main()
