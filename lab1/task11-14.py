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