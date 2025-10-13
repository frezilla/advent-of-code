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

comet = Reinder("Comet", 14, 10, 127)
dancer = Reinder("Dancer", 16, 11, 162)

print(comet.run(1000))
print(dancer.run(1000))
