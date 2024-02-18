def findPairAmount(fileName):
    file = open(fileName,"r")
    fileLines = file.readlines()
    N,K = int(fileLines[0].split()[0]), int(fileLines[0].split()[1])
    amount = 0
    #for i in range(1,len(fileLines)):
    #    for j in range(i+1,len(fileLines)):
    #        if int(fileLines[i]) + int(fileLines[j]) >= K:
    #            amount += 1
    fileLines = fileLines[1:]
    fileLines.sort(key=int)
    for i in range(len(fileLines)):
        if int(fileLines[i]) >= K:
            amount += len(fileLines[(i+1):])
        else:
            for j in range(i+1,len(fileLines)):
                if int(fileLines[i]) + int(fileLines[j]) >= K:
                    amount += len(fileLines[j:])
                    break

    return amount

print(findPairAmount("27-169A.txt"))
#print(findPairAmount("test.txt"))