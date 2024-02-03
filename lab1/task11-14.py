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

