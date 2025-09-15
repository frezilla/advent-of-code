def format_result(value):
    result = ""
    character = value[0]
    value_length = len(value)
    nb_groups = value_length // 9
    remain = value_length % 9
    for i in range(0, nb_groups):
        result += '9' + character
    if remain > 0:
        result += str(remain) + character
    return result


def look_and_say(val):
    result = ''
    sub_string = ""
    previous_char = None
    for current_char in val:
        if current_char == previous_char:
            sub_string += current_char
        else:
            sub_string_length = len(sub_string)
            if sub_string_length > 0:
                result += format_result(sub_string)
            sub_string = current_char
            previous_char = current_char
    result += format_result(sub_string)
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
