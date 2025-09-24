import re

print("--- Day 12: JSAbacusFramework.io ---")
inputFile = input("Input file name : ")
file = open(inputFile, 'r')
amount = 0
for line in file:
    current_line = line.strip()
    result = re.findall("-?[0-9]+", current_line)
    for number in result:
        amount += int(number)
print(f"Sum of all numbers : {amount}")