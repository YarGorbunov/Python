def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))

def findCharacters(string):
    r = []
    for c in range_char("a", "z"):
        if string.find(c) != -1: r.append(c)
    return r

def col(string):
    r = []
    for c in range_char("A", "z"):
        if string.find(c) != -1: r.append(c)
    return len(r)

def fileName(string):
    l = string.split("/")
    return l[len(l)-1].split(".")[0]

num = input("Enter task number: ")
while True:
    if (num not in ["0","1","2"]): 
        num = input("Enter task number: ")
    else: break

string = input("Enter input string: ")

if num == "0": print(findCharacters(string))
elif num == "1": print(col(string))
else: print(fileName(string))