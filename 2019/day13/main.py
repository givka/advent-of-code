import csv
from dataclasses import dataclass


class IntCode:
    def __init__(self, numbers: list, input_number: int, show_map=False):
        self.numbers = numbers.copy()
        self.numbers.extend([0 for _ in range(1, 1000000)])
        self.input_number = input_number
        self.relative_number = 0
        self.cursor = 0
        self.outputs = []
        self.current = 0
        self.current_str = ""
        self.game = Game(show_map)

    def is_finished(self):
        return self.numbers[self.cursor] == 99

    def process_code(self):
        # removed recursion because of python recursion limit
        self.current_str = str(self.numbers[self.cursor])
        self.current = int(self.current_str[-1])

        if self.current == 1:
            self.numbers[self.p(3)] = self.numbers[self.p(1)] + self.numbers[self.p(2)]
        if self.current == 2:
            self.numbers[self.p(3)] = self.numbers[self.p(1)] * self.numbers[self.p(2)]
        if self.current == 3:
            self.numbers[self.p(1)] = self.game.process_input()
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

        if len(self.outputs) == 3:
            self.game.update_map(self.outputs)
            self.outputs.clear()

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


class Game:
    def __init__(self, show_map):
        self.score = 0
        self.tiles = {}
        self.paddle_pos = vec2(0, 0)
        self.ball_pos = vec2(0, 0)
        self.show_map = show_map

    def print_map(self):
        string = f"\nscore: {self.score}\n"
        for y in range(0, max(self.tiles, key=lambda t: t[1])[1] + 1):
            for x in range(0, max(self.tiles, key=lambda t: t[0])[0] + 1):
                if (x, y) not in self.tiles:
                    continue
                tile = self.tiles[(x, y)]
                if tile.tile_id == Tile.EMPTY:
                    string += " "
                if tile.tile_id == Tile.WALL:
                    string += "X"
                if tile.tile_id == Tile.BLOCK:
                    string += "="
                if tile.tile_id == Tile.HORIZONTAL_PADDLE:
                    string += "-"
                    self.paddle_pos = vec2(x, y)
                if tile.tile_id == Tile.BALL:
                    string += "o"
                    self.ball_pos = vec2(x, y)
            string += "\n"
        print(string)

    def update_map(self, outputs):
        x, y, tile_id = outputs
        if x == -1 and y == 0:
            self.score = tile_id
        else:
            self.tiles[(x, y)] = Tile(vec2(x, y), tile_id)
        if tile_id == Tile.HORIZONTAL_PADDLE:
            self.paddle_pos = vec2(x, y)
        if tile_id == Tile.BALL:
            self.ball_pos = vec2(x, y)

        if self.show_map:
            self.print_map()

    def process_input(self):
        joystick = 0
        if self.paddle_pos.x < self.ball_pos.x:
            joystick = 1
        if self.paddle_pos.x == self.ball_pos.x:
            joystick = 0
        if self.paddle_pos.x > self.ball_pos.x:
            joystick = -1

        return joystick

    def get_number_of_specific_tiles(self, tile_id):
        tiles = [self.tiles[key] for key in self.tiles]
        return len([tile for tile in tiles if tile.tile_id == tile_id])


def main():
    memory = parse()

    int_code = IntCode(memory, 0)
    while int_code.is_finished() is False:
        int_code.process_code()
    print("number of blocks:", int_code.game.get_number_of_specific_tiles(Tile.BLOCK))

    memory[0] = 2  # play
    show_map = False
    int_code = IntCode(memory, 0, show_map)
    while int_code.is_finished() is False:
        int_code.process_code()
    print("score:", int_code.game.score)


if __name__ == "__main__":
    main()
