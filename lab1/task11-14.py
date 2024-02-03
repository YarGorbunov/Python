def avgASCII(string):
    s = 0
    k = 0
    for c in string:
        s += ord(c)
        k += 1
    return s/k

def sort1(l):
    return sorted(l, key=avgASCII)

def sort2(l):
    a = avgASCII(l[0])
    def keyFunc(string):
        return (avgASCII(string) - a) ** 2
    return sorted(l, key=keyFunc)

def sort3(l):
    def keyFunc(string):
        k = 0
        for i in range(1,len(string)):
            if ((string[i-1] in ["a", "e", "y", "u", "i", "o"]) and (string[i] not in ["a", "e", "y", "u", "i", "o"])) or ((string[i-1] not in ["a", "e", "y", "u", "i", "o"]) and (string[i] in ["a", "e", "y", "u", "i", "o"])):
                k += 1
        return k
    return sorted(l, key=keyFunc)

def sort4(l):
    a = 0
    for i in range(2, len(l[0])):
        if (ord(l[0][i-2]) + ord(l[0][i-1]) + ord(l[0][i])) / 3 > a: a = (ord(l[0][i-2]) + ord(l[0][i-1]) + ord(l[0][i])) / 3
    def keyFunc(string):
        max = 0
        for i in range(2, len(string)):
            if (ord(string[i-2]) + ord(string[i-1]) + ord(string[i])) / 3 > max: max = (ord(string[i-2]) + ord(string[i-1]) + ord(string[i])) / 3
        disp = 0
        for i in range(2, len(string)):
            disp += ((ord(string[i-2]) + ord(string[i-1]) + ord(string[i])) / 3) ** 2
        disp /= len(string) - 2
        return disp
    return sorted(l, key=keyFunc)

num = input("Enter task number: ")
while True:
    if (num not in ["0","1","2","3"]): 
        num = input("Enter task number: ")
    else: break

l = []
s = input()
l.append(s)
while s != "": 
    s = input()
    if (s != ""): l.append(s)

if num == "0": print(sort1(l))
elif num == "1": print(sort2(l))
elif num == "2": print(sort3(l))
else: print(sort4(l))