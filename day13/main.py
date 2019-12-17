import csv
from dataclasses import dataclass
from typing import List


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


@dataclass
class Tile:
    pos: vec2
    tile_id: int


Tile.EMPTY = 0
Tile.WALL = 1
Tile.BLOCK = 2
Tile.HORIZONTAL_PADDLE = 3
Tile.BALL = 4


def process(outputs: List[int]):
    tiles = []
    i = 0
    while i < len(outputs):
        x = outputs[i]
        y = outputs[i + 1]
        tile_id = outputs[i + 2]
        tiles.append(Tile(vec2(x, y), tile_id))
        i += 3
    return tiles


def main():
    the_input = parse()
    int_code = IntCode(the_input, 0)

    tiles = process(int_code.outputs)
    block_tiles = [tile for tile in tiles if tile.tile_id == Tile.BLOCK]
    print("number of blocks:", len(block_tiles))


if __name__ == "__main__":
    main()
