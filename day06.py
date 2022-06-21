import re
import numpy as np

def turnon(arr, ax, ay, bx, by):
    for i in range(ax, bx+1):
        for j in range(ay, by+1):
            arr[i][j] = 1
    return arr

with open("day06.txt") as f:
    lines = f.read()
    lines = lines.split("\n")
    lines = [re.findall('[0-9]+', line) for line in lines]
    print(lines)