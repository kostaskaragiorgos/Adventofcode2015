def vows(stragg):
    countw = 0
    vowels =  set("aeiou")
    for i in stragg:
        if i in vowels:
            countw += 1
    if countw >=3:
        return True
    return False


def contfor(stragg):
    forbs = ['ab', 'cd', 'pq', 'xy']
    containsfor = any(forb in stragg for forb in forbs)
    if  containsfor:
        return False
    return True


def twiceinarow(stragg):
    for i in range(len(stragg)-1 ):
        if stragg[i] == stragg[i+1]:
            return True
    return False


nicewordscounter = 0
with open("day5.txt") as f:
    lines = f.read().split("\n")
    for i in lines:
        if vows(i) and contfor(i) and twiceinarow(i):
            nicewordscounter +=1

print(nicewordscounter)





