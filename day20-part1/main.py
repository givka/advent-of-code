from collections import deque
from dataclasses import dataclass


def parse():
    with open('input.txt') as f:
        return f.read()


# noinspection PyPep8Naming
@dataclass
class vec2:
    x: int
    y: int

    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return vec2(-self.x, -self.y)

    def __mul__(self, other):
        return vec2(other * self.x, other * self.y)

    def __rmul__(self, other):
        return self.__mul__(other)

    def key(self):
        return self.x, self.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


@dataclass
class Cell:
    parent: 'Cell' or None
    pos: vec2

    def count(self, acc=0):
        if self.parent is None:
            return acc
        return self.parent.count(acc + 1)


NORTH = vec2(0, 1)
SOUTH = vec2(0, -1)
WEST = vec2(-1, 0)
EAST = vec2(1, 0)


def print_map(my_map):
    string = ""
    width = max(my_map, key=lambda t: t.x).x
    height = max(my_map, key=lambda t: t.y).y

    for y in range(0, height + 1):
        for x in range(0, width + 1):
            if vec2(x, y) in my_map:
                string += my_map[vec2(x, y)]
            else:
                string += " "
        string += "\n"
    print(string)


def breath_first_search(maze: dict, start: vec2, goal: vec2, gates: dict) -> Cell:
    discovered = {}
    start = Cell(None, start)
    queue = deque([start])
    discovered[start.pos] = start

    while len(queue) != 0:
        current = queue.popleft()
        if current.pos == goal:
            return current.count()
        neighbours = [current.pos + NORTH, current.pos + SOUTH,
                      current.pos + WEST, current.pos + EAST]
        for neighbour in neighbours:

            if neighbour not in maze:
                continue

            if maze[neighbour] in gates and maze[neighbour] not in ["AA", "ZZ"]:
                neighbour = [i for i in gates[maze[neighbour]] if i != current.pos][0]
            if maze[neighbour] in ["#", " "]:
                continue
            if neighbour in discovered:
                continue

            cell = Cell(current, neighbour)
            discovered[cell.pos] = cell
            queue.append(cell)


def fill_gates(my_map: dict, gates: dict):
    for key in [k for k in my_map if my_map[k] == "."]:
        neighbours = [NORTH, SOUTH, WEST, EAST]
        for n in neighbours:
            current = key + n
            current2 = key + 2 * n
            if my_map[current] != "#" and my_map[current] != ".":
                if n == SOUTH or n == WEST:
                    gate = my_map[current2] + my_map[current]

                else:
                    gate = my_map[current] + my_map[current2]
                if gate not in gates:
                    gates[gate] = [key]
                else:
                    gates[gate].append(key)
                my_map[current] = gate


def main():
    maze = parse()
    my_map = {}
    gates = {}

    x = 0
    y = 0
    for char in maze:
        if char == "\n":
            y += 1
            x = 0
        else:
            my_map[vec2(x, y)] = char
            x += 1

    fill_gates(my_map, gates)

    print(gates)

    steps = breath_first_search(my_map, gates["AA"][0], gates["ZZ"][0], gates)
    print("steps:", steps)


if __name__ == "__main__":
    main()
