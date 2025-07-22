print("--- Day 2: I Was Told There Would Be No Math ---")

inputFile = input("Input file name : ")
file = open(inputFile, 'r')

squareFeet = 0
feetOfRibbon = 0
for line in file:
    currentLine = line.strip()
    tokens = currentLine.split("x")
    l = int(tokens[0])
    w = int(tokens[1])
    h = int(tokens[2])

    side1 = l * w
    perimeter1 = (l + w) * 2
    side2 = w * h
    perimeter2 = (w + h) * 2
    side3 = h * l
    perimeter3 = (h + l) * 2

    sideMin = min([side1, side2, side3])
    perimeterMin = min([perimeter1, perimeter2, perimeter3])

    currentSquareFeet = 2 * side1 + 2 * side2 + 2 * side3 + sideMin
    squareFeet += currentSquareFeet

    currentFeetOfRibbon = perimeterMin + (l * w * h)
    feetOfRibbon += currentFeetOfRibbon

    print(f"Square feet for box {l} * {w} * {h} = {currentSquareFeet} - feet of ribbon = {currentFeetOfRibbon}")

print(f"Total square feet of wrapping feet: {squareFeet} - Total feet of ribbon: {feetOfRibbon}")
