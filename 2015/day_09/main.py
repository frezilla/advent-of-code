from graph_class import Graph

print("--- Day 9: All in a Single Night ---")

inputFile = input("Input file name : ")
file = open(inputFile, 'r')

myGraph = Graph()

for line in file:
    datas = line.strip().split()
    myGraph.add(datas[0], datas[2], int(datas[4]))
