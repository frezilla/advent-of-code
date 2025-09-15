import re


def check_increasing_straight(password):
    password_length = len(password)
    previous_ascii = -1
    size = 0
    for i in range(password_length):
        current_ascii = ord(password[i])
        if previous_ascii + 1 == current_ascii:
            size += 1
        else:
            size = 0
        if size >= 3:
            return True
        previous_ascii = current_ascii
    return size >= 3


def check_invalid_letter(password):
    if re.search("[iol]", password):
        return False
    else:
        return True


def check_pairs(password):
    map = {}
    for letter in password:
        nb_occ = map.setdefault(letter, 0)
        nb_occ += 1
        map[letter] = nb_occ
    nb_pairs = 0
    for pair in map.items():
        if pair[1] > 1:
            nb_pairs += 1
    return nb_pairs > 1


def inc_letter(letter):
    ascii_code_a = ord('a')
    ascii_code_z = ord('z')
    ascii_code = ord(letter[0])
    if ascii_code_a <= ascii_code <= ascii_code_z:
        ascii_code += 1
        if ascii_code > ascii_code_z:
            ascii_code = ascii_code_a
            carry = True
        else:
            carry = False
        return chr(ascii_code), carry
    else:
        raise ValueError('Invalid letter')


def inc_password(password):
    if not len(password) == 8:
        raise ValueError('Invalid password length')
    if "aaaaaaaa" <= password < "zzzzzzzzz":
        reversed_password = password[::-1]
        new_password = ""
        run = True
        for letter in reversed_password:
            if run:
                result = inc_letter(letter)
                add_letter = result[0]
                run = result[1]
            else:
                add_letter = letter
            new_password += add_letter
        return new_password[::-1]
    else:
        raise ValueError('Invalid password')


print("--- Day 11: Corporate Policy ---")
password = input("Password : ")
valid_password = False
while not valid_password:
    if check_increasing_straight(password) and check_invalid_letter(password) and check_pairs(password):
        print(f"New password : {password}")
        break
    password = inc_password(password)
