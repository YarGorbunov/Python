def func1(l):
    return l.index(min(l))

def func2(l, a, b):
    k = 0
    for i in l:
        if i >= a and i <= b:
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

