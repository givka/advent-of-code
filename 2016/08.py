commands = [line.strip() for line in open("08.in").readlines()]

HEIGHT = 6
WIDTH = 50
MAP = [[' ' for x in range(WIDTH)] for y in range(HEIGHT)]

for command in commands:
    command = command.split()

    if command[0] == "rect":
        xx, yy = command[1].split("x")
        for y in range(int(yy)):
            for x in range(int(xx)):
                MAP[y][x] = "#"

    elif command[0] == "rotate":
        where = int(command[2].split("=")[1])
        by = int(command[4])

        if command[1] == "column":
            new_column = []
            for y in range(HEIGHT):
                new_column.append(MAP[(y-by) % HEIGHT][where])
            for y in range(HEIGHT):
                MAP[y][where] = new_column[y]
        else:
            new_row = []
            for x in range(WIDTH):
                new_row.append(MAP[where][(x-by) % WIDTH])
            for x in range(WIDTH):
                MAP[where][x] = new_row[x]

count = 0

for y in range(HEIGHT):
    for x in range(WIDTH):
        print(MAP[y][x], end="")
        if MAP[y][x] == "#":
            count += 1
    print()

print(count)