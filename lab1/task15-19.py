def func1(l):
    return l.index(min(l))

def func2(l, a, b):
    k = 0
    for i in l:
        if i >= a and i <= b:
            k += 1
    return k

