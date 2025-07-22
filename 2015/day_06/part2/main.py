print("--- Day 6: Probably a Fire Hazard (part 2) ---")


class Data:
    def __init__(self, order, x1, y1, x2, y2):
        self.order = order
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def create_array():
    array = []
    i = 0
    while i < 1000000:
        array.append(0)
        i += 1

    return array


def parse_line(_line):
    _working_line = _line

    if _working_line.startswith("toggle"):
        _order = "toggle"
    elif _working_line.startswith("turn off"):
        _order = "turn off"
    else:
        _order = "turn on"

    _working_line = _working_line[len(_order) + 1:]

    index = _working_line.find(",")
    x1 = int(_working_line[:index])

    _working_line = _working_line[index + 1:]

    index = _working_line.find(" ")
    y1 = int(_working_line[:index])

    _working_line = _working_line[index + len("through "):]

    index = _working_line.find(",")
    x2 = int(_working_line[:index])

    _working_line = _working_line[index + 1:]
    y2 = int(_working_line)

    return Data(_order, x1, y1, x2, y2)


def get_index(_x, _y):
    return _y * 1000 + _x


inputFile = input("Input file name : ")
file = open(inputFile, 'r')

lights = create_array()

for line in file:
    current_line = line.strip()
    data = parse_line(current_line)

    order = data.order
    indexX = data.x1
    while indexX <= data.x2:
        indexY = data.y1
        while indexY <= data.y2:
            current_index = get_index(indexX, indexY)
            indexY += 1
            if order == "turn on":
                lights[current_index] = lights[current_index] + 1
            elif order == "turn off":
                lights[current_index] = lights[current_index] - 1
                if lights[current_index] < 0:
                    lights[current_index] = 0
            else:
                lights[current_index] = lights[current_index] + 2
        indexX += 1

brightness = 0
for x in lights:
    brightness += x

print(f"Total brightness of all lights : {brightness}")
