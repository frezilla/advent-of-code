class Reinder:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time

    def run(self, time):
        cycle_time = self.fly_time + self.rest_time
        distance = 0
        if cycle_time > 0:
            nb_cycles = time // cycle_time
            distance += self.speed * self.fly_time * nb_cycles
            distance += self.speed * min(self.fly_time, time % cycle_time)
        return distance

print("--- Day 14: Reindeer Olympics ---")
TIME = 2503
inputFile = input("Input file name : ")
file = open(inputFile, 'r')
reinders = []
for line in file:
    datas = line.strip().split()
    reinders.append(Reinder(datas[0], int(datas[3]), int(datas[6]), int(datas[13])))
max_distance = 0
for reinder in reinders:
    distance = reinder.run(TIME)
    if distance > max_distance:
        max_distance = distance
print(f"Distance maximale parcourue par le vainqueur = {max_distance}")
