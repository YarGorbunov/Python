def check(string):
    s = string
    i = 0
    while i < len(s):
        #if i >= len(s): break
        if s[i] < "a" or s[i] > "z":
            s = s[:i] + s[i + 1:]
            i -= 1
        i += 1
    for i in range(1,len(s)):
        if s[i-1] > s[i]:
            return False
    return True

def countA(string):
    return string.count('A')

def fileName(string):
    l = string.split("/")
    return l[len(l)-1].split(".")[0]

