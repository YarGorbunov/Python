def func1(l):
    return l.index(min(l))

def func2(l, a, b):
    k = 0
    for i in l:
        if i > a and i < b:
            k += 1
    return k

def func3(l):
    minEl = min(l)
    first = -1
    last = -1
    for i in range(0,len(l)):
        if l[i] == minEl:
            if first == -1: first = i
            else: last = i
    k = 0
    for i in range(0,len(l)):
        if i > first and i < last: k += 1
    return k

def func4(l, a, b):
    k = 0
    for i in l:
        if i >= a and i <= b:
            k += 1
    return k

def func5(l1, l2):
    l = []
    for i in l1:
        if i not in l2 and l1.count(i) == 1: l.append(i)
    for i in l2:
        if i not in l1 and l2.count(i) == 1: l.append(i)
    return l

num = input("Enter task number: ")
while True:
    if (num not in ["0","1","2","3","4"]): 
        num = input("Enter task number: ")
    else: break

if num in ["0","2"]:
    l = []
    s = input()
    l.append(int(s))
    while s != "": 
        s = input()
        if (s != ""): l.append(int(s))
    if num == "0": print(func1(l))
    else: print(func3(l))
    exit()
elif num in ["1","3"]:
    l = []
    s = input()
    l.append(int(s))
    while s != "": 
        s = input()
        if (s != ""): l.append(int(s))
    a = input()
    b = input()
    if num == "1": print(func2(l, int(a), int(b)))
    else: print(func4(l, int(a), int(b)))
else:
    l1 = []
    s = input()
    l1.append(int(s))
    while s != "": 
        s = input()
        if (s != ""): l1.append(int(s))
    l2 = []
    s = input()
    l2.append(int(s))
    while s != "": 
        s = input()
        if (s != ""): l2.append(int(s))
    print(func5(l1,l2))