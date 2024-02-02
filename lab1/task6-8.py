def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))

def findCharacters(string):
    r = []
    for c in range_char("a", "z"):
        if string.find(c) != -1: r.append(c)
    return r

print(findCharacters("bdgxas"))