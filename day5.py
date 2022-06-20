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



with open("day5.txt") as f:
    lines = f.read().split("\n")
    for i in lines:
        print(vows(i))
        print(contfor(i))





