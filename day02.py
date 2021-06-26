with open("day2.txt") as f:
    lines = f.read()
    lines = lines.split("\n")
    lines = [line.split('x') for line in lines]

def sqrf(lista):
    sqf = 2*int(lista[0])*int(lista[1]) + 2*int(lista[1])*int(lista[2]) + 2*int(lista[2])*int(lista[0])
    slack = min(int(lista[0]) * int(lista[1]), int(lista[1]) * int(lista[2]), int(lista[0])* int(lista[2]))
    return sqf , slack


twrappingpaper = 0
for i in lines:
    a,b = sqrf(i)
    twrappingpaper += (a+b)

print(twrappingpaper)

