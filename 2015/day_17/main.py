def compute_sums(_containers, _index):
    sum_containers = 0
    for index in range(_containers.size()):
        sum_containers += _containers[index]
    end_index = min(_index, _containers.size())
    sum_before = 0
    for index in range(end_index):
        sum_before += _containers[index]
    sum_after = sum_containers - sum_before
    return [sum_before, sum_after]


def load_containers(_filename):
    file = open(_filename, "r")
    result_list = list()
    for line in file:
        current_line = line.strip()
        result_list.append(int(current_line))
    return list(reversed(result_list))


def process(containers):



print("--- Day 17: No Such Thing as Too Much ---")
filename = input("Input file name : ")
containers = load_containers(filename)
LITERS = 150