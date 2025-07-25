class Node:
    def __init__(self, name):
        self.name = name
        self.weight = None

    def __eq__(self, other):
        if isinstance(other, Node):
            return other.name == self.name
        else:
            return False

    def __hash__(self):
        return hash(self.name)
