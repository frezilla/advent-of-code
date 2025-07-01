print("--- Day 1: Not Quite Lisp ---")

instructions = input("Instructions : ")

floor = 0

assignPosition = True
currentPosition = 1
position = 0

for x in instructions:
    if x == "(":
        floor += 1
    elif x == ")":
        floor -= 1

    if floor == -1 and assignPosition :
        assignPosition = False
        position = currentPosition

    currentPosition += 1

print(f"Final floor : {floor}")
if position == 0:
    print("Santa never goes to floor -1")
else:
    print(f"Position of the first character that cause to enter the basement (floor -1): {position}")