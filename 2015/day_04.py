import hashlib

print("--- Day 4: The Ideal Stocking Stuffer ---")

secretKey = input("Secret key : ")
nbZeros = input("Number of zeros : ")

answer = 0
n= '0'

while 1:
    strValue = str(answer)
    testValue = f"{secretKey}{strValue}"
    md5Value = hashlib.md5(testValue.encode()).hexdigest()

    if md5Value.startswith(n.zfill(int(nbZeros))):
        break

    answer += 1

print(f"Answer : {answer}")
