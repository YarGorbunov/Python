def func1(num):
    m = []
    for i in range(2, num+1):
        if num % i == 0:
            m.append(i)
    k = 0
    for i in range(1, num+1):
        flag = 1
        for j in m:
            if i % j == 0:
                flag = 0
                break
        if flag:
            k+=1
    return k
