def avgASCII(string):
    s = 0
    k = 0
    for c in string:
        s += ord(c)
        k += 1
    return s/k

def sortASCII(l):
    return sorted(l, key=avgASCII)

