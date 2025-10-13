class Person:
    def __init__(self, name, rules):
        self.name = name
        self.left_neighbor = None
        self.right_neighbor = None
        self.rules = rules

    def compute_happiness(self):
        if self.left_neighbor:
            left_value = self.rules[self.left_neighbor.name()]
        else:
            left_value = 0
        if self.right_neighbor:
            right_value = self.rules[self.right_neighbor.name()]
        else:
            right_value = 0
        return left_value + right_value

    def left_neighbor(self, left_neighbor):
        self.left_neighbor = left_neighbor

    def name(self):
        return self.name

    def right_neighbor(self, right_neighbor):
        self.right_neighbor = right_neighbor


def read_rules(filename):
    rules = list()
    file = open(filename, 'r')
    for line in file:
        line = line.strip().split()
        rules.append((line[0], line[10], line[2], line[3]))
    return rules


def read_person_from_rules(rules):
    persons = set()
    for rule in rules:
        persons.add(rule[0])
    return persons


def run(link, persons):
    new_value= ""
    if len(link) > 0:
        new_value = link + " "
    if len(persons) == 1:
        new_value += persons[0]
        print(f"{new_value}")
    else:
        for index in range(len(persons)):
            current_name = persons.pop(index)
            new_value += current_name
            run(new_value, persons)
            persons.insert(index, current_name)


print("--- Day 13: Knights of the Dinner Table ---")
inputFile = input("Input file name : ")
rules = read_rules(inputFile)
persons = read_person_from_rules(rules)
run("", list(persons))
