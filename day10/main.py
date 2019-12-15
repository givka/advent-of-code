import csv
import math
from dataclasses import dataclass


def parse():
    with open('input.txt') as f:
        reader = csv.reader(f)
        lines = [line for line in reader]
        lines = [line[0] for line in lines]
        return [list(line) for line in lines]


def norm(x, y):
    dist = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    return round(float(x / dist), 3), round(float(y / dist), 3)


def check_in_sight(self, asteroids):
    in_sight = set([])

    for other in asteroids:
        if other == self:
            continue
        current_dir = norm(other.x - self.x, other.y - self.y)
        in_sight.add(current_dir)  # it is a set, will not add twice

    return len(in_sight)  # actually take not the closest ones


# noinspection PyPep8Naming
@dataclass
class vec2:
    x: int
    y: int


def main():
    the_map = parse()
    height = len(the_map)
    width = len(the_map[0])

    asteroids = []
    for x in range(0, width):
        for y in range(0, height):
            current = the_map[y][x]
            if current == "#":
                asteroids.append(vec2(x, y))

    numbers = [check_in_sight(asteroid, asteroids) for asteroid in asteroids]
    print("best station:", max(numbers))


if __name__ == "__main__":
    main()
