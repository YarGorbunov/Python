import random
N = int(input())
fileFirst = open("output1.txt","w")
numberList = []
for _ in range(N):
    number = random.randint(1,20)
    numberList.append(number)
    fileFirst.write(str(number)+"\n")
fileSecond = open("output2.txt","w")
cur = 1
for number in numberList:
    cur *= number
    fileSecond.write(str(cur)+"\n")