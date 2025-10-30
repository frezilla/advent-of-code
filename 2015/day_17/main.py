def bit_value(_value, _index):
    return _value >> (_index - 1) & 1


def load_containers(_filename):
    file = open(_filename, "r")
    result_list = list()
    for line in file:
        current_line = line.strip()
        result_list.append(int(current_line))
    return list(result_list.sort(reverse=True))


def test_combination(_value, _containers, _target):
    nb_bits = _value.bit_length()
    container_value = _containers[len(_containers) - nb_bits]
    if container_value > _target:
        return 0
    elif container_value == _target:
        return 1
    else:
        mask = int('0' + ''.join('1' for i in range(nb_bits - 1)), 2)
        new_value = mask or _value
        return test_combination(new_value, _containers, _target - container_value)


print("--- Day 17: No Such Thing as Too Much ---")
# filename = input("Input file name : ")
filename = '/home/frederic/Téléchargements/puzzle.txt'
containers = load_containers(filename)
LITERS = 25
nb_containers = len(containers)
max_value = int(''.join('1' for i in range(pow(nb_containers, 2).bit_length())), 2)
nb_combinations = 0
for i in range(max_value, 0, - 1):
    nb_combinations += test_combination(i, containers, LITERS)
print(f"Nombre de combinaisons: {nb_combinations}")