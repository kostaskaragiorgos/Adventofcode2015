from os import read


def findfloor(s):
    floor = 0
    for i in s:
        if i == "(":
            floor += 1
        else:
            floor -= 1
    return floor

def findbs(s):
    floor = 0
    counter = 0
    for i in s:
        if i == "(":
            floor +=1
        else:
            floor -= 1
        counter +=1
        if floor == -1:
            return counter

with open("day1.txt") as f:
    lines = f.read()
    lines = lines.strip("\n")
    print(findfloor(lines))
    print(findbs(lines))
        