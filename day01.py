from os import read


def findfloor(s):
    floor = 0
    for i in s:
        if i == "(":
            floor += 1
        else:
            floor -= 1
    return floor

with open("day1.txt") as f:
    lines = f.read()
    lines = lines.strip("\n")
    print(findfloor(lines))
        