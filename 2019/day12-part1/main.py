import re
from dataclasses import dataclass


def regex(string: str) -> (int, int, int):
    results = re.search(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>", string)
    return vec3(int(results[1]), int(results[2]), int(results[3]))


def parse():
    with open('input.txt') as f:
        lines = [regex(line.strip()) for line in f.readlines()]
        return lines


# noinspection PyPep8Naming
@dataclass
class vec3:
    x: int
    y: int
    z: int

    def __add__(self, other):
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self):
        return '<x={:3d}, y={:3d}, z={:3d}>'.format(self.x, self.y, self.z)


class Moon:
    def __init__(self, pos):
        self.pos = pos
        self.vel = vec3(0, 0, 0)
        self.pot = 0
        self.kin = 0
        self.energy = 0

    def process(self, moons):
        self.apply_gravity(moons)

    def apply_gravity(self, moons):
        for other in moons:
            if other is self:
                continue
            if self.pos.x < other.pos.x:
                self.vel.x += 1
            if self.pos.x > other.pos.x:
                self.vel.x -= 1
            if self.pos.y < other.pos.y:
                self.vel.y += 1
            if self.pos.y > other.pos.y:
                self.vel.y -= 1
            if self.pos.z < other.pos.z:
                self.vel.z += 1
            if self.pos.z > other.pos.z:
                self.vel.z -= 1

    def __str__(self):
        return f"pos={self.pos}, vel={self.vel}"

    def apply_vel(self):
        self.pos += self.vel
        self.pot = abs(self.pos.x) + abs(self.pos.y) + abs(self.pos.z)
        self.kin = abs(self.vel.x) + abs(self.vel.y) + abs(self.vel.z)
        self.energy = self.pot * self.kin


def main():
    the_input = parse()
    moons = [Moon(line) for line in the_input]

    steps = range(0, 1000+1)
    for step in steps:
        print("\nAfter", step, "steps:")
        for moon in moons:
            print(moon)
        print("energy:", sum([moon.energy for moon in moons]))

        for moon in moons:
            moon.apply_gravity(moons)
        for moon in moons:
            moon.apply_vel()



if __name__ == "__main__":
    main()
