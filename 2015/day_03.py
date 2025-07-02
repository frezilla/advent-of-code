print("--- Day 3: Perfectly Spherical Houses in a Vacuum ---")

def move_step(direction):
    _x = 0
    _y = 0
    if direction == "^":
        _y -= 1
    elif direction == "<":
        _x -= 1
    elif direction == "v":
        _y += 1
    elif direction == ">":
        _x += 1
    return [_x, _y]


x = 0
y = 0

visitedHouses = {(x, y)}

instructions = input("Instructions : ")

for c in instructions:
    array = move_step(c)

    x += array[0]
    y += array[1]

    visitedHouses.add((x, y))

print(f"Number of houses with at least one present : {len(visitedHouses)}")


visitedHouses.clear()

xSanta = 0
ySanta = 0
xRobot = 0
yRobot = 0

for (santa, robot) in zip(instructions[0::2], instructions[1::2]):
    array = move_step(santa)
    xSanta += array[0]
    ySanta += array[1]
    visitedHouses.add((xSanta, ySanta))

    array = move_step(robot)
    xRobot += array[0]
    yRobot += array[1]
    visitedHouses.add((xRobot, yRobot))

print(f"Number of houses with at least one present (with Santa and his robot) : {len(visitedHouses)}")