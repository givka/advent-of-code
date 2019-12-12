from dataclasses import dataclass


@dataclass
class Token:
    direction: str
    steps: int
    is_vertical: bool


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


def parse_token(token: str):
    direction = token[0]
    steps = int(token[1:])

    return Token(direction, steps, direction == 'U' or direction == 'D')


def get_offset(token: Token):
    if token.direction == 'R':
        return Point(1, 0)
    elif token.direction == 'L':
        return Point(-1, 0)
    elif token.direction == 'U':
        return Point(0, 1)
    elif token.direction == 'D':
        return Point(0, -1)


with open('input.txt') as f:
    lines = [line.strip().split(',') for line in f.readlines()]
    first_tokens = [parse_token(token) for token in lines[0]]
    second_tokens = [parse_token(token) for token in lines[1]]

grid = {}
intersections = []
lengths = []

current = Point(0, 0)

for first_token in first_tokens:
    grid[current.x, current.y] = 1
    offset = get_offset(first_token)

    for x in range(1, first_token.steps + 1):
        current += offset
        grid[current.x, current.y] = 1

step = 0
current = Point(0, 0)

for second_token in second_tokens:
    grid[current.x, current.y] = 1
    offset = get_offset(second_token)

    for x in range(1, second_token.steps + 1):
        current += offset
        step += 1
        if (current.x, current.y) in grid and grid[current.x, current.y] == 1:
            intersections.append(current)
        grid[current.x, current.y] = -step

step = 0
current = Point(0, 0)

for first_token in first_tokens:
    offset = get_offset(first_token)
    for x in range(1, first_token.steps + 1):
        current += offset
        step += 1
        if grid[current.x, current.y] < 0:
            lengths.append(-grid[current.x, current.y] + step)

distances = [abs(intersection.x) + abs(intersection.y) for intersection in intersections]
print("min distance:", min(distances))
print("min length:", min(lengths))
