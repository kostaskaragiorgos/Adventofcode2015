with open("day5.txt") as f:
    lines = f.read().split("\n")


forbs = ['ab', 'cd', 'pq', 'xy']
vowels =  set("aeiou")
vowelscorrect = 0
for i in lines:
    countw = 0
    for j in i:
        if j in vowels:
            countw  +=1
    if countw >=3:
        vowelscorrect +=1
print(vowelscorrect)