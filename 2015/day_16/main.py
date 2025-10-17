class AuntSue:
    def __init__(self, _name):
        self.name = _name
        self.children = None
        self.cats = None
        self.samoyeds = None
        self.pomeranians = None
        self.akitas = None
        self.vizslas = None
        self.goldfish = None
        self.trees = None
        self.cars = None
        self.perfumes = None

    def check(self, _children, _cats, _samoyeds, _pomeranians, _akitas, _vizslas, _goldfish, _trees, _cars, _perfumes):
        return (self.check_field(self.children, _children)
                and self.check_field(self.cats, _cats)
                and self.check_field(self.samoyeds, _samoyeds)
                and self.check_field(self.pomeranians, _pomeranians)
                and self.check_field(self.akitas, _akitas)
                and self.check_field(self.vizslas, _vizslas)
                and self.check_field(self.goldfish, _goldfish)
                and self.check_field(self.trees, _trees)
                and self.check_field(self.cars, _cars)
                and self.check_field(self.perfumes, _perfumes))

    def check_field(self, field1, field2):
        if field1:
            return field1 == field2
        else:
            return True


def load_aunts(_filename):
    file = open(_filename, "r")
    result_list = list()
    for line in file:
        current_line = line.strip()
        datas = current_line.replace(":", "").replace(",", "").split()
        current_aunt = AuntSue(datas[0] + " " + datas[1])
        for index in range(2, len(datas), 2):
            if datas[index] == "children":
                current_aunt.children = int(datas[index + 1])
            elif datas[index] == "cats":
                current_aunt.cats = int(datas[index + 1])
            elif datas[index] == "samoyeds":
                current_aunt.samoyeds = int(datas[index + 1])
            elif datas[index] == "pomeranians":
                current_aunt.pomeranians = int(datas[index + 1])
            elif datas[index] == "akitas":
                current_aunt.akitas = int(datas[index + 1])
            elif datas[index] == "vizslas":
                current_aunt.vizslas = int(datas[index + 1])
            elif datas[index] == "goldfish":
                current_aunt.goldfish = int(datas[index + 1])
            elif datas[index] == "trees":
                current_aunt.trees = int(datas[index + 1])
            elif datas[index] == "cars":
                current_aunt.cars = int(datas[index + 1])
            elif datas[index] == "perfumes":
                current_aunt.perfumes = int(datas[index + 1])
        result_list.append(current_aunt)
    return result_list


print("--- Day 16: Aunt Sue ---")
children = 3
cats = 7
samoyeds = 2
pomeranians = 3
akitas = 0
vizslas = 0
goldfish = 5
trees = 3
cars = 2
perfumes = 1
inputFile = input("Input file name : ")
aunts = load_aunts(inputFile)
for aunt in aunts:
    if aunt.check(children, cats, samoyeds, pomeranians, akitas, vizslas, goldfish, trees, cars, perfumes):
        print(f"Numéro de tante Sue : {aunt.name}")
