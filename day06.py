import re
from cv2 import line
import numpy as np

def turnon(arr, ax, ay, bx, by):
    for i in range(ax, bx+1):
        for j in range(ay, by+1):
            arr[i][j] = 1
    return arr

def toggle(arr, ax, ay, bx, by):
    for i in range(ax, bx+1):
        for j in range(ay, by+1):
            if arr[i][j] == 1:
                arr[i][j] = 0
            else:
                arr[i][j] = 1;
    return arr

def turnoff(arr, ax, ay, bx, by):
    for i in range(ax, bx+1):
        for j in range(ay, by+1):
            arr[i][j] = 0
    return arr
action = []
arr = np.zeros((1000,1000))
with open("day06.txt") as f:
    lines = f.read()
    lines = lines.split("\n")
    action = [line[0:8] for line in lines]
    lines = [re.findall('[0-9]+', line) for line in lines]
    print(action)
    print(lines)
    for i in action:
        for j in lines:
            if i == 'turn on':
                turnon(arr, int(j[0]), int(j[1]), int(j[2]), int(j[3]))
            elif i == 'turn off':
                turnoff(arr, int(j[0]), int(j[1]), int(j[2]), int(j[3]))
            else:
                toggle(arr, int(j[0]), int(j[1]), int(j[2]), int(j[3]))

print(np.count_nonzero(arr==1))