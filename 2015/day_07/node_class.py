import operations


class Node:
    def __init__(self, name, operation, value):
        self.name = name
        self.operation = operation
        self.value = value
        self.children = []
        self.parents = []

    def add_child(self, node):
        self.children.append(node)

    def add_parent(self, parent):
        parent.add_child(self)
        self.parents.append(parent)
        if parent.is_valued():
            self.compute()

    def compute(self):
        if not self.is_valued():
            nb_parents = len(self.parents)
            updated = False
            if nb_parents == 1 and self.parents[0].is_valued():
                updated = True
                if self.operation == "ASSIGN":
                    self.value = self.parents[0].value
                elif self.operation == "NOT":
                    self.value = operations.do_not(self.parents[0].value)
                else:
                    updated = False
            elif nb_parents == 2:
                first_parent = self.parents[0]
                second_parent = self.parents[1]
                if first_parent.is_valued() and second_parent.is_valued():
                    updated = True
                    if self.operation == "AND":
                        self.value = operations.do_and(first_parent.value, second_parent.value)
                    elif self.operation == "LSHIFT":
                        self.value = operations.do_lshift(first_parent.value, second_parent.value)
                    elif self.operation == "OR":
                        self.value = operations.do_or(first_parent.value, second_parent.value)
                    elif self.operation == "RSHIFT":
                        self.value = operations.do_rshift(first_parent.value, second_parent.value)
                    else:
                        updated = False
            else:
                raise Exception("More than two parents")
            if updated:
                self.update_children()

    def is_valued(self):
        return self.value is not None

    def update_children(self):
        for child in self.children:
            child.compute()
