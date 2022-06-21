import re
with open("day06.txt") as f:
    lines = f.read()
    lines = lines.split("\n")
    lines = [re.findall('[0-9]+', line) for line in lines]
    print(lines)