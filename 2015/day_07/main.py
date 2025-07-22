import node_class


def convert_value(value):
    if value.isnumeric():
        return int(value)
    else:
        return None


def get_from_node(name, value):
    if name in dictionary:
        return dictionary[name]
    else:
        _node = node_class.Node(name, None, value)
        dictionary[name] = _node
        return _node


def get_to_node(name):
    if name in dictionary:
        return dictionary[name]
    else:
        _node = node_class.Node(name, None, None)
        dictionary[name] = _node
        return _node


print("--- Day 7: Some Assembly Required ---")

inputFile = input("Input file name : ")
file = open(inputFile, 'r')
wireName = input("Name of the wire : ")

dictionary = {}

for line in file:
    current_line = line.strip()
    datas = current_line.split()

    nb_datas = len(datas)

    if nb_datas == 3:
        node = get_to_node(datas[2])
        node.operation = "ASSIGN"
        from_node = get_from_node(datas[0], convert_value(datas[0]))
        node.add_parent(from_node)
    elif nb_datas == 4:
        node = get_to_node(datas[3])
        node.operation = "NOT"
        from_node = get_from_node(datas[1], convert_value(datas[1]))
        node.add_parent(from_node)
    elif nb_datas == 5:
        node = get_to_node(datas[4])
        node.operation = datas[1]
        from_node1 = get_from_node(datas[0], convert_value(datas[0]))
        node.add_parent(from_node1)
        from_node2 = get_from_node(datas[2], convert_value(datas[2]))
        node.add_parent(from_node2)
    else:
        raise Exception(f"Parse error {current_line}")

print(f"Signal provided to wire {wireName} is {dictionary[wireName].value}")

wireNameToOverride = input("Name of wire you want to override: ")
dictionary[wireNameToOverride].value = dictionary[wireName].value
dictionary[wireNameToOverride].update_children()
print(f"New signal provided to wire {wireName} is {dictionary[wireName].value}")