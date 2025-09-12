def look_and_say(val):
    result = ''
    sub_string = ""
    previous_char = None
    for current_char in val:
        if current_char == previous_char:
            sub_string += current_char
        else:
            if len(sub_string) > 0:
                result += str(len(sub_string)) + sub_string[0]
            sub_string = current_char
            previous_char = current_char
    result += str(len(sub_string)) + sub_string[0]
    return result

print("--- 10: Elves Look, Elves Say ---")

puzzle = input("Puzzle initial : ")

value = puzzle
for i in range(0, 40):
    value = look_and_say(value)
print(f"The length of the result is {len(value)} (40 times)")

value = puzzle
for i in range(0, 50):
    value = look_and_say(value)
print(f"The length of the result is {len(value)} (50 times)")
