import csv
import math
from dataclasses import dataclass


# noinspection PyPep8Naming
@dataclass
class vec2:
    x: int
    y: int

    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


def parse():
    with open('input.txt') as f:
        reader = csv.reader(f)
        lines = [line for line in reader]
        lines = [line[0] for line in lines]
        return [list(line) for line in lines]


def norm(v: vec2) -> vec2:
    dist = get_distance(v)
    return vec2(round(float(v.x / dist), 3), round(float(v.y / dist), 3))


def get_distance(v: vec2) -> float:
    return round(math.sqrt(math.pow(v.x, 2) + math.pow(v.y, 2)), 3)


def get_angle(v: vec2) -> float:
    axis = vec2(0, -1)
    angle = math.atan2(axis.y, -axis.x) - math.atan2(v.y, -v.x)
    if angle < 0:
        angle += 2 * math.pi
    return round(math.degrees(angle), 3)


def check_in_sight_part1(self, asteroids):
    in_sight = {}

    for other in asteroids:
        if other == self:
            continue
        current_dir = norm(other - self)
        dist = get_distance(other - self)
        if str(current_dir) in in_sight:
            if in_sight[str(current_dir)][0] > dist:
                in_sight[str(current_dir)] = dist, other
        else:
            in_sight[str(current_dir)] = dist, other

    return in_sight


def check_in_sight_part2(self, asteroids):
    in_sight = {}

    for other in asteroids:
        if other == self:
            continue
        current_dir = norm(other - self)
        angle = get_angle(current_dir)
        dist = get_distance(other - self)
        if angle not in in_sight:
            in_sight[angle] = [(dist, other)]
        else:
            in_sight[angle].append((dist, other))

    for key in in_sight:
        in_sight[key].sort(key=lambda t: t[0])

    sorted_dict = {}
    for key in sorted(in_sight, key=lambda t: float(t)):
        sorted_dict[key] = in_sight[key]

    asteroid_in_order = []
    while len(sorted_dict) != 0:
        for key in list(sorted_dict.keys()):
            asteroid_in_order.append(sorted_dict[key][0][1])
            sorted_dict[key].remove(sorted_dict[key][0])
            if len(sorted_dict[key]) == 0:
                del sorted_dict[key]
    return asteroid_in_order


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

    in_sight_part1 = [(asteroid, check_in_sight_part1(asteroid, asteroids)) for asteroid in asteroids]
    best_station = max(in_sight_part1, key=lambda t: len(t[1]))
    print("best station:", best_station[0], "neighbours:", len(best_station[1]))

    asteroids_in_order = check_in_sight_part2(best_station[0], asteroids)
    print("200th asteroid:", asteroids_in_order[199])


if __name__ == "__main__":
    main()
